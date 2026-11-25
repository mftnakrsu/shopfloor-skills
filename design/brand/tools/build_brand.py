#!/usr/bin/env python3
"""Build every file in assets/brand/ from one set of constants.

The symbol is a yamazumi chart of a balanced line: three stations split their work into
1, 2 and 3 blocks, and every stack ends level just under one takt line.

Outputs SVG files only. render_fallbacks.py turns them into PNG, GIF and ICO files.
Needs fontTools and the two Barlow Semi Condensed fonts (SIL OFL 1.1); see ../README.md.
"""
import argparse
import os
import re

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

# ------------------------------------------------------------------ constants

GRAPHITE = "#1F2428"
GREEN = "#2E8A55"        # Line Green, on light backgrounds
GREEN_DARK = "#3FA56A"   # Line Green, on dark backgrounds
CHALK = "#F1F4F2"
MUTE_LIGHT = "#5B6368"
MUTE_DARK = "#A9B3AE"
GH_DARK = "#0D1117"

NAME = "shopfloor-skills"
TAGLINE = "Agent Skills for people who run production lines."
SOCIAL_LINE = "Claude Code  ·  OpenCode  ·  Qwen Code  ·  Cursor"

# Symbol geometry on a 256-unit canvas. Columns are 48 wide and 32 apart.
COLS = [(24, 72), (104, 152), (184, 232)]
STACK_TOP, STACK_BOTTOM, BLOCK_GAP = 48, 224, 16
TAKT = (8, 16, 248, 32)            # x0, y0, x1, y1
MARK_BOX = (8, 16, 248, 224)       # the ink bounds of the symbol

# Small-size cut on a 16-unit grid: every edge on a whole pixel at 16 px.
SMALL_TAKT = (0, 1, 16, 3)
SMALL_COLS = [(0, 4), (6, 10), (12, 16)]
SMALL_STACKS = [[(4, 15)], [(4, 9), (10, 15)], [(4, 7), (8, 11), (12, 15)]]

# Favicon tile on a 16-unit grid, 1 px margin inside a rounded tile.
FAV_TAKT = (1, 1, 15, 3)
FAV_COLS = [(1, 5), (6, 10), (11, 15)]

WORD_XHEIGHT = 80     # x-height of the wordmark in the lockup, in symbol units
WORD_GAP = 64         # symbol to wordmark
TILE_RX = 56
TILE_SCALE = 0.625

ANIM_SECONDS = 8


# ------------------------------------------------------------------ geometry

def blocks():
    """Work blocks in fill order: station 1, then 2 from the bottom, then 3 from the bottom."""
    out = []
    for (x0, x1), k in zip(COLS, (1, 2, 3)):
        h = (STACK_BOTTOM - STACK_TOP - BLOCK_GAP * (k - 1)) / k
        stack = []
        for i in range(k):
            y = STACK_TOP + i * (h + BLOCK_GAP)
            stack.append((x0, y, x1, y + h))
        out += reversed(stack)
    return out


def rect_d(x0, y0, x1, y1):
    return f"M{x0:g} {y0:g}H{x1:g}V{y1:g}H{x0:g}Z"


def rects(boxes):
    return "".join(rect_d(*b) for b in boxes)


def small_blocks(cols, stacks):
    return [(x0, y0, x1, y1) for (x0, x1), stack in zip(cols, stacks) for (y0, y1) in stack]


# ------------------------------------------------------------------ type

_num = re.compile(r"-?\d+\.\d+")


def tidy(d, nd=2):
    def r(m):
        t = f"{round(float(m.group(0)), nd):.{nd}f}".rstrip("0").rstrip(".")
        return "0" if t in ("-0", "") else t
    return _num.sub(r, d)


class Face:
    """A TTF with GPOS pair kerning, set as SVG path data."""

    def __init__(self, path):
        self.font = TTFont(path)
        self.upem = self.font["head"].unitsPerEm
        self.cmap = self.font.getBestCmap()
        self.glyphs = self.font.getGlyphSet()
        self.hmtx = self.font["hmtx"]
        self.xheight = self.font["OS/2"].sxHeight
        self.pairs, self.classes = self._kerning()

    def _kerning(self):
        pairs, classes = {}, []
        if "GPOS" not in self.font:
            return pairs, classes
        gpos = self.font["GPOS"].table
        ids = set()
        for record in gpos.FeatureList.FeatureRecord:
            if record.FeatureTag == "kern":
                ids.update(record.Feature.LookupListIndex)
        for index in sorted(ids):
            lookup = gpos.LookupList.Lookup[index]
            subs = lookup.SubTable
            if lookup.LookupType == 9:
                subs = [s.ExtSubTable for s in subs]
            for st in subs:
                if not hasattr(st, "Format") or not hasattr(st, "Coverage"):
                    continue
                if st.Format == 1:
                    cover = st.Coverage.glyphs
                    for i, pair_set in enumerate(st.PairSet):
                        for rec in pair_set.PairValueRecord:
                            v = getattr(rec.Value1, "XAdvance", 0) if rec.Value1 else 0
                            pairs.setdefault((cover[i], rec.SecondGlyph), v)
                elif st.Format == 2:
                    classes.append(st)
        return pairs, classes

    def _kern(self, left, right):
        if (left, right) in self.pairs:
            return self.pairs[(left, right)]
        for st in self.classes:
            if left in st.Coverage.glyphs:
                c1 = st.ClassDef1.classDefs.get(left, 0)
                c2 = st.ClassDef2.classDefs.get(right, 0)
                rec = st.Class1Record[c1].Class2Record[c2]
                return getattr(rec.Value1, "XAdvance", 0) if rec.Value1 else 0
        return 0

    def size_for_xheight(self, xh):
        return xh / self.xheight * self.upem

    def set(self, text, size, x=0.0, baseline=0.0):
        """Return (path data, (xmin, ymin, xmax, ymax)) of the ink, with x at the left ink edge."""
        s = size / self.upem
        names = [self.cmap[ord(ch)] for ch in text]
        first = BoundsPen(self.glyphs)
        self.glyphs[names[0]].draw(first)
        x -= first.bounds[0] * s if first.bounds else 0
        pen, bounds = SVGPathPen(self.glyphs), BoundsPen(self.glyphs)
        cx = 0.0
        for i, g in enumerate(names):
            m = (s, 0, 0, -s, x + cx * s, baseline)
            self.glyphs[g].draw(TransformPen(pen, m))
            self.glyphs[g].draw(TransformPen(bounds, m))
            cx += self.hmtx[g][0] + (self._kern(g, names[i + 1]) if i + 1 < len(names) else 0)
        return tidy(pen.getCommands()), bounds.bounds


# ------------------------------------------------------------------ svg helpers

def svg(w, h, title, body, desc=None, extra=""):
    labels = "title desc" if desc else "title"
    head = f'  <title id="title">{title}</title>\n'
    if desc:
        head += f'  <desc id="desc">{desc}</desc>\n'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" width="{w:g}" height="{h:g}" '
            f'role="img" aria-labelledby="{labels}"{extra}>\n{head}{body}\n</svg>\n')


def symbol_body(ink, accent, indent="  ", animated=False):
    cls = ' class="takt"' if animated else ""
    lines = [f'{indent}<path fill="{accent}"{cls} d="{rect_d(*TAKT)}"/>']
    if animated:
        for i, b in enumerate(blocks(), 1):
            x0, y0, x1, y1 = b
            lines.append(f'{indent}<rect class="b b{i}" x="{x0:g}" y="{y0:g}" width="{x1 - x0:g}" '
                         f'height="{y1 - y0:g}" fill="{ink}"/>')
    else:
        lines.append(f'{indent}<path fill="{ink}" d="{rects(blocks())}"/>')
    return "\n".join(lines)


def tile_transform(size=256, scale=TILE_SCALE):
    """Centre the ink bounds of the symbol on the tile."""
    cx = (MARK_BOX[0] + MARK_BOX[2]) / 2
    cy = (MARK_BOX[1] + MARK_BOX[3]) / 2
    return f"translate({size / 2 - cx * scale:g} {size / 2 - cy * scale:g}) scale({scale:g})"


# ------------------------------------------------------------------ animation

# Each block grows up from its own base, one after the other, until every stack meets the
# takt line. The takt line is dim while the line is unbalanced and full when it is balanced.
# Times are fractions of one loop. The resting state of every element is the static logo.
FILL_START, FILL_STEP, FILL_LEN = 0.06, 0.065, 0.085
HOLD_END, FADE_END = 0.86, 0.94
TAKT_DIM = 0.35
START_AT = 0.5   # the loop opens in the held, full state, so a first glance shows the whole logo


def block_window(i):
    start = FILL_START + i * FILL_STEP
    return start, start + FILL_LEN


def takt_window():
    _, end = block_window(len(blocks()) - 1)
    return end, end + 0.04


def pct(f):
    return f"{f * 100:.1f}".rstrip("0").rstrip(".") + "%"


def animation_css(selector_prefix=""):
    p = selector_prefix
    rules = [
        f"{p}.b {{ transform-box: fill-box; transform-origin: 50% 100%; "
        f"animation-duration: {ANIM_SECONDS}s; animation-delay: {-START_AT * ANIM_SECONDS:g}s; "
        f"animation-iteration-count: infinite; "
        f"animation-timing-function: cubic-bezier(.3, 0, .2, 1); }}",
        f"{p}.takt {{ animation: takt {ANIM_SECONDS}s linear {-START_AT * ANIM_SECONDS:g}s infinite; }}",
    ]
    for i in range(len(blocks())):
        a, b = block_window(i)
        rules.append(f"{p}.b{i + 1} {{ animation-name: fill{i + 1}; }}")
        rules.append(f"@keyframes fill{i + 1} {{ 0%, {pct(a)} {{ transform: scaleY(0); opacity: 1; }} "
                     f"{pct(b)}, {pct(HOLD_END)} {{ transform: scaleY(1); opacity: 1; }} "
                     f"{pct(FADE_END)} {{ transform: scaleY(1); opacity: 0; }} "
                     f"100% {{ transform: scaleY(0); opacity: 0; }} }}")
    a, b = takt_window()
    rules.append(f"@keyframes takt {{ 0%, {pct(a)} {{ opacity: {TAKT_DIM}; }} {pct(b)}, {pct(HOLD_END)} {{ opacity: 1; }} "
                 f"{pct(FADE_END)}, 100% {{ opacity: {TAKT_DIM}; }} }}")
    rules.append(f"@media (prefers-reduced-motion: reduce) {{ {p}.b, {p}.takt {{ animation: none; }} }}")
    return "\n".join("    " + r for r in rules)


def ease(t):
    """Close to cubic-bezier(.3, 0, .2, 1)."""
    return t * t * (3 - 2 * t)


def state_at(f):
    """(list of (scaleY, opacity) per block, takt opacity) at loop fraction f; used for GIF frames."""
    out = []
    for i in range(len(blocks())):
        a, b = block_window(i)
        if f <= a:
            s, o = 0.0, 1.0
        elif f < b:
            s, o = ease((f - a) / (b - a)), 1.0
        elif f <= HOLD_END:
            s, o = 1.0, 1.0
        elif f < FADE_END:
            s, o = 1.0, 1 - ease((f - HOLD_END) / (FADE_END - HOLD_END))
        else:
            s, o = 0.0, 0.0
        out.append((s, o))
    a, b = takt_window()
    if f <= a:
        t = TAKT_DIM
    elif f < b:
        t = TAKT_DIM + (1 - TAKT_DIM) * (f - a) / (b - a)
    elif f <= HOLD_END:
        t = 1.0
    elif f < FADE_END:
        t = 1 - (1 - TAKT_DIM) * (f - HOLD_END) / (FADE_END - HOLD_END)
    else:
        t = TAKT_DIM
    return out, t


def frame_body(ink, accent, f, indent="  "):
    """The symbol at loop fraction f as plain SVG, without CSS animation."""
    states, takt = state_at(f)
    lines = [f'{indent}<path fill="{accent}" opacity="{takt:.3f}" d="{rect_d(*TAKT)}"/>']
    for (x0, y0, x1, y1), (s, o) in zip(blocks(), states):
        if s <= 0 or o <= 0:
            continue
        h = (y1 - y0) * s
        lines.append(f'{indent}<rect x="{x0:g}" y="{y1 - h:.3f}" width="{x1 - x0:g}" height="{h:.3f}" '
                     f'fill="{ink}" opacity="{o:.3f}"/>')
    return "\n".join(lines)


# ------------------------------------------------------------------ builders

class Brand:
    def __init__(self, semibold, medium):
        self.bold = Face(semibold)
        self.medium = Face(medium)
        size = self.bold.size_for_xheight(WORD_XHEIGHT)
        self.word_size = size
        self.word_baseline = 128 + WORD_XHEIGHT / 2

    def wordmark(self, x, baseline, xheight=WORD_XHEIGHT):
        return self.bold.set(NAME, self.bold.size_for_xheight(xheight), x, baseline)

    def text(self, s, xheight, x, baseline, face=None):
        face = face or self.medium
        return face.set(s, face.size_for_xheight(xheight), x, baseline)

    # logo/ ---------------------------------------------------------

    def lockup_horizontal(self, ink, accent, label):
        x0 = 256 + WORD_GAP
        d, (_, _, x1, _) = self.wordmark(x0, self.word_baseline)
        w = round(x1 + 2)
        body = (f'  <g id="symbol">\n{symbol_body(ink, accent, "    ")}\n  </g>\n'
                f'  <path id="wordmark" fill="{ink}" d="{d}"/>')
        return svg(w, 256, f"{NAME}, horizontal lockup{label}", body)

    def lockup_stacked(self, ink, accent, label):
        d0, (bx0, by0, bx1, by1) = self.wordmark(0, 0)
        width = bx1 - bx0
        pad = 8
        w = round(width + 2 * pad)
        sym_x = (w - 256) / 2
        baseline = 256 + 56 - by0       # cap and ascender tops sit 56 units below the symbol box
        d, (_, _, _, y1) = self.wordmark(pad, baseline)
        h = round(y1 + pad)
        body = (f'  <g id="symbol" transform="translate({sym_x:g} 0)">\n{symbol_body(ink, accent, "    ")}\n  </g>\n'
                f'  <path id="wordmark" fill="{ink}" d="{d}"/>')
        return svg(w, h, f"{NAME}, stacked lockup{label}", body)

    def wordmark_svg(self, ink, label):
        _, (_, by0, _, _) = self.wordmark(0, 0)
        pad = 4
        d, (_, _, x1, y1) = self.wordmark(pad, pad - by0)
        return svg(round(x1 + pad), round(y1 + pad), f"{NAME}, wordmark{label}", f'  <path fill="{ink}" d="{d}"/>')

    # hero ----------------------------------------------------------

    def hero(self, ink, accent, mute, label, frame=None):
        """1280 x 360 banner: the symbol fills up, the name and tagline sit beside it."""
        scale = 0.86
        sym_h = 256 * scale
        sym_x, sym_y = 96, (360 - sym_h) / 2
        text_x = sym_x + 256 * scale + WORD_GAP * scale
        word_xh = 66
        word_base = sym_y + (MARK_BOX[1] + 104) * scale
        wd, (_, _, wx1, _) = self.wordmark(text_x, word_base, word_xh)
        td, (_, _, tx1, _) = self.text(TAGLINE, 19.5, text_x + 2, word_base + 62)
        if frame is None:
            style = f"  <style>\n{animation_css()}\n  </style>\n"
            mark = symbol_body(ink, accent, "    ", animated=True)
        else:
            style, mark = "", frame_body(ink, accent, frame, "    ")
        body = (f"{style}  <g transform=\"translate({sym_x:g} {sym_y:g}) scale({scale:g})\">\n{mark}\n  </g>\n"
                f'  <path fill="{ink}" d="{wd}"/>\n  <path fill="{mute}" d="{td}"/>')
        assert wx1 < 1280 - 64 and tx1 < 1280 - 64, (wx1, tx1)
        desc = ("Three stations of a production line. Their work blocks stack up one after the other "
                "until every stack ends level just under the green takt line: a balanced line.")
        return svg(1280, 360, f"{NAME}{label}", body, desc=f"{TAGLINE} {desc}")

    def hero_frame(self, theme, f, background):
        ink, accent, mute = THEMES[theme]
        s = self.hero(ink, accent, mute, "", frame=f)
        return s.replace("\n  <g transform", f'\n  <rect width="1280" height="360" fill="{background}"/>\n  <g transform', 1)

    # social preview --------------------------------------------------

    def social(self):
        w, h = 1280, 640
        scale = 1.05
        sym_x, sym_y = 112, (h - 256 * scale) / 2 - 8
        text_x = sym_x + 256 * scale + 72
        wd, (_, _, wx1, _) = self.wordmark(text_x, 0, 62)
        word_base = sym_y + (MARK_BOX[1] + 96) * scale
        wd, (_, _, wx1, _) = self.wordmark(text_x, word_base, 62)
        td, (_, _, tx1, _) = self.text("Agent Skills for people who", 24, text_x + 2, word_base + 74)
        td2, _ = self.text("run production lines.", 24, text_x + 2, word_base + 74 + 50)
        ld, (_, _, lx1, _) = self.text(SOCIAL_LINE, 13.5, text_x + 2, h - 96)
        assert max(wx1, tx1, lx1) < w - 64, (wx1, tx1, lx1)
        body = (f'  <rect width="{w}" height="{h}" fill="{GRAPHITE}"/>\n'
                f'  <g transform="translate({sym_x:g} {sym_y:g}) scale({scale:g})">\n{symbol_body(CHALK, GREEN_DARK, "    ")}\n  </g>\n'
                f'  <path fill="{CHALK}" d="{wd}"/>\n'
                f'  <path fill="{MUTE_DARK}" d="{td}{td2}"/>\n'
                f'  <path fill="{GREEN_DARK}" d="{ld}"/>')
        return svg(w, h, NAME, body, desc=TAGLINE)


THEMES = {
    "light": (GRAPHITE, GREEN, MUTE_LIGHT),
    "dark": (CHALK, GREEN_DARK, MUTE_DARK),
}


def symbol_svg(ink, accent, label):
    return svg(256, 256, f"{NAME} symbol{label}", symbol_body(ink, accent))


def symbol_small_svg(ink, accent, label):
    body = (f'  <path fill="{accent}" d="{rect_d(*SMALL_TAKT)}"/>\n'
            f'  <path fill="{ink}" d="{rects(small_blocks(SMALL_COLS, SMALL_STACKS))}"/>')
    return svg(16, 16, f"{NAME} symbol, small-size cut{label}", body)


def icon_tile_svg():
    body = (f'  <rect width="256" height="256" rx="{TILE_RX}" fill="{GRAPHITE}"/>\n'
            f'  <g transform="{tile_transform()}">\n{symbol_body(CHALK, GREEN_DARK, "    ")}\n  </g>')
    return svg(256, 256, f"{NAME} icon", body)


def icon_tile_animated_svg(frame=None):
    if frame is None:
        style = f"  <style>\n{animation_css()}\n  </style>\n"
        mark = symbol_body(CHALK, GREEN_DARK, "    ", animated=True)
    else:
        style, mark = "", frame_body(CHALK, GREEN_DARK, frame, "    ")
    body = (f'{style}  <rect width="256" height="256" rx="{TILE_RX}" fill="{GRAPHITE}"/>\n'
            f'  <g transform="{tile_transform()}">\n{mark}\n  </g>')
    desc = ("On a graphite tile, work blocks stack up on three stations until every stack "
            "ends level just under the green takt line.")
    return svg(256, 256, f"{NAME} icon, animated", body, desc=desc)


def favicon_svg():
    """16-unit favicon tile: pixel-exact at 16, 32 and 48 px."""
    stacks = [[(4, 15)], [(4, 9), (10, 15)], [(4, 7), (8, 11), (12, 15)]]
    body = (f'  <rect width="16" height="16" rx="3" fill="{GRAPHITE}"/>\n'
            f'  <path fill="{GREEN_DARK}" d="{rect_d(*FAV_TAKT)}"/>\n'
            f'  <path fill="{CHALK}" d="{rects(small_blocks(FAV_COLS, stacks))}"/>')
    return svg(16, 16, f"{NAME}", body)


def full_bleed_svg(size, scale):
    """Square without rounded corners, for platforms that mask the icon themselves."""
    body = (f'  <rect width="{size}" height="{size}" fill="{GRAPHITE}"/>\n'
            f'  <g transform="{tile_transform(size, scale)}">\n{symbol_body(CHALK, GREEN_DARK, "    ")}\n  </g>')
    return svg(size, size, f"{NAME} icon", body)


# ------------------------------------------------------------------ contrast

def luminance(hex_colour):
    rgb = [int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


# ------------------------------------------------------------------ main

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--semibold", required=True, help="BarlowSemiCondensed-SemiBold.ttf")
    parser.add_argument("--medium", required=True, help="BarlowSemiCondensed-Medium.ttf")
    parser.add_argument("--out", default="assets/brand")
    parser.add_argument("--site", default="docs-site", help="docs site root; its logo files are written too")
    args = parser.parse_args()
    out = args.out
    b = Brand(args.semibold, args.medium)

    files = {
        "logo/symbol-ink.svg": symbol_svg(GRAPHITE, GREEN, ""),
        "logo/symbol-white.svg": symbol_svg(CHALK, GREEN_DARK, ", for dark backgrounds"),
        "logo/symbol-small-ink.svg": symbol_small_svg(GRAPHITE, GREEN, ""),
        "logo/symbol-small-white.svg": symbol_small_svg(CHALK, GREEN_DARK, ", for dark backgrounds"),
        "logo/wordmark-ink.svg": b.wordmark_svg(GRAPHITE, ""),
        "logo/wordmark-white.svg": b.wordmark_svg(CHALK, ", for dark backgrounds"),
        "logo/lockup-horizontal-ink.svg": b.lockup_horizontal(GRAPHITE, GREEN, ""),
        "logo/lockup-horizontal-white.svg": b.lockup_horizontal(CHALK, GREEN_DARK, ", for dark backgrounds"),
        "logo/lockup-stacked-ink.svg": b.lockup_stacked(GRAPHITE, GREEN, ""),
        "logo/lockup-stacked-white.svg": b.lockup_stacked(CHALK, GREEN_DARK, ", for dark backgrounds"),
        "logo/icon-tile.svg": icon_tile_svg(),
        "icons/favicon.svg": favicon_svg(),
        "icons/app-icon-full-bleed.svg": full_bleed_svg(256, 0.72),
        "icons/maskable.svg": full_bleed_svg(256, 0.5),
        "hero-light.svg": b.hero(*THEMES["light"], ""),
        "hero-dark.svg": b.hero(*THEMES["dark"], ", for dark backgrounds"),
        "icon-tile-animated.svg": icon_tile_animated_svg(),
        "social-preview.svg": b.social(),
    }
    for name, text in files.items():
        write(os.path.join(out, name), text)
    if args.site and os.path.isdir(args.site):
        write(os.path.join(args.site, "src/assets/logo-light.svg"), files["logo/lockup-horizontal-ink.svg"])
        write(os.path.join(args.site, "src/assets/logo-dark.svg"), files["logo/lockup-horizontal-white.svg"])
        write(os.path.join(args.site, "src/assets/icon-tile-animated.svg"), files["icon-tile-animated.svg"])
        write(os.path.join(args.site, "public/favicon.svg"), files["icons/favicon.svg"])
    print(f"wrote {len(files)} files to {out}")
    for fg, bg, what in [
        (GRAPHITE, "#FFFFFF", "Graphite on white"), (GREEN, "#FFFFFF", "Line Green on white"),
        (GREEN, CHALK, "Line Green on Chalk"), (GREEN_DARK, GH_DARK, "Line Green (dark) on #0D1117"),
        (GREEN_DARK, GRAPHITE, "Line Green (dark) on Graphite"), (CHALK, GRAPHITE, "Chalk on Graphite"),
        (CHALK, GH_DARK, "Chalk on #0D1117"), (MUTE_LIGHT, "#FFFFFF", "Mute on white"),
        (MUTE_DARK, GRAPHITE, "Mute (dark) on Graphite"), (MUTE_DARK, GH_DARK, "Mute (dark) on #0D1117"),
    ]:
        print(f"  {what}: {contrast(fg, bg):.1f}:1")


if __name__ == "__main__":
    main()
