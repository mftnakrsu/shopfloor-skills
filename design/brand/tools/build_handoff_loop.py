#!/usr/bin/env python3
"""Build the hand-off loop diagram (design spec, section 4.2) as a static SVG.

Standard library only. The diagram brings its own Chalk card, so it reads on light and dark
pages. Update AVAILABLE and SOON when a skill ships, then run this script again.
"""
import argparse
import os

GRAPHITE, GREEN, CHALK, MUTE, LINE = "#1F2428", "#2E8A55", "#F1F4F2", "#5B6368", "#6B7479"
AVAILABLE = {"lead-daily-routine"}
SOON = {"solve-8d"}
FONT = "'Barlow Semi Condensed', 'Segoe UI', system-ui, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

W, H = 1280, 650
LANES = [(40, "See the problem"), (490, "Fix the cause"), (940, "Hold the gain")]
NODE_W, NODE_H = 300, 46

# name -> (lane, y, skills shown in the box)
NODES = {
    "ldr": (0, 110, ["lead-daily-routine"]),
    "spc": (0, 200, ["measure-spc"]),
    "oee": (0, 290, ["measure-oee"]),
    "gemba": (0, 380, ["lead-gemba-walk"]),
    "audit": (0, 470, ["audit-process"]),
    "vsm": (0, 560, ["improve-vsm"]),
    "solve": (1, 110, ["solve-5why", "solve-fishbone", "solve-8d"]),
    "smed": (1, 250, ["improve-smed"]),
    "tpm": (1, 320, ["improve-tpm"]),
    "kaizen": (1, 410, ["improve-kaizen"]),
    "flow": (1, 540, ["improve-tpt", "improve-kanban-pull", "improve-line-balancing"]),
    "cp": (2, 110, ["plan-control-plan"]),
    "wi": (2, 330, ["plan-workstation-instructions"]),
}


def box(name):
    lane, y, skills = NODES[name]
    h = NODE_H + 22 * (len(skills) - 1)
    return LANES[lane][0], y, NODE_W, h


def side(name, which, dy=0.0):
    x, y, w, h = box(name)
    return {"l": (x, y + h / 2 + dy), "r": (x + w, y + h / 2 + dy),
            "t": (x + w / 2, y), "b": (x + w / 2, y + h)}[which]


def curve(a, b, dya=0.0, dyb=0.0):
    (x1, y1), (x2, y2) = side(a, "r", dya), side(b, "l", dyb)
    mid = (x1 + x2) / 2
    return f"M{x1:g} {y1:g}C{mid:g} {y1:g} {mid:g} {y2:g} {x2 - 2:g} {y2:g}", (x1, y1, x2, y2)


def edges():
    """(path, label, label x, label y, text-anchor) for every hand-off in spec section 4.2."""
    out = []
    d, (x1, y1, _, _) = curve("ldr", "solve", 0, -22)
    out.append((d, "red KPI, cause unknown", (x1 + LANES[1][0]) / 2, y1 - 9, "middle"))
    (x1, y1), (_, y2) = side("spc", "t"), side("ldr", "b")
    out.append((f"M{x1:g} {y1:g}V{y2 + 2:g}", "out of control: escalate", x1 + 10, (y1 + y2) / 2 + 5, "start"))
    d, (x1, y1, x2, y2) = curve("oee", "smed", -10, 0)
    out.append((d, "set-up loss", x2 - 10, y2 - 9, "end"))
    d, (x1, y1, x2, y2) = curve("oee", "tpm", 4, 0)
    out.append((d, "breakdowns", x2 - 10, y2 + 18, "end"))
    d, (x1, y1, x2, y2) = curve("oee", "solve", -16, 0)
    out.append((d, "defects", x1 + 12, y1 - 9, "start"))
    d, (x1, y1, x2, y2) = curve("gemba", "kaizen", 0, 0)
    out.append((d, "observations", x2 - 10, y2 - 9, "end"))
    d, _ = curve("gemba", "solve", -10, 14)
    out.append((d, "", 0, 0, "start"))
    d, (x1, y1, x2, y2) = curve("audit", "solve", -10, 30)
    out.append((d, "findings", x1 + 12, y1 - 9, "start"))
    # audit-process to the control plan: along the gap between lanes 2 and 3
    x1, y1 = side("audit", "r", 10)
    x2, y2 = side("cp", "l", 12)
    gx = LANES[2][0] - 40
    out.append((f"M{x1:g} {y1:g}H{gx - 12:g}Q{gx:g} {y1:g} {gx:g} {y1 - 12:g}V{y2 + 12:g}Q{gx:g} {y2:g} "
                f"{gx + 12:g} {y2:g}H{x2 - 2:g}", "", 0, 0, "start"))
    d, _ = curve("vsm", "flow", 0, 0)
    out.append((d, "", 0, 0, "start"))
    d, (x1, y1, x2, y2) = curve("solve", "cp", 0, -12)
    out.append((d, "root cause fixed", x1 + 12, y1 - 9, "start"))
    (x1, y1), (_, y2) = side("cp", "b"), side("wi", "t")
    out.append((f"M{x1:g} {y1:g}V{y2 - 2:g}", "update", x1 + 10, (y1 + y2) / 2 + 5, "start"))
    d, (x1, y1, x2, y2) = curve("flow", "wi", 0, 10)
    out.append((d, "new standard work", x1 + 12, y1 + 20, "start"))
    return out


def status(skill):
    if skill in AVAILABLE:
        return "available"
    return "coming soon" if skill in SOON else "planned"


def node_svg(name):
    x, y, w, h = box(name)
    skills = NODES[name][2]
    live = any(s in AVAILABLE for s in skills)
    stroke = GREEN if live else LINE
    dash = "" if live or any(s in SOON for s in skills) else ' stroke-dasharray="5 4"'
    out = [f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#FFFFFF" stroke="{stroke}" '
           f'stroke-width="{2.5 if live else 1.5}"{dash}/>']
    for i, s in enumerate(skills):
        ty = y + 28 + 22 * i
        weight = "700" if s in AVAILABLE else "400"
        out.append(f'  <text x="{x + 14}" y="{ty}" font-family="{MONO}" font-size="15" font-weight="{weight}" '
                   f'fill="{GRAPHITE}">{s}</text>')
        tag = status(s)
        colour = GREEN if tag == "available" else MUTE
        out.append(f'  <text x="{x + w - 12}" y="{ty}" text-anchor="end" font-family="{FONT}" font-size="13" '
                   f'fill="{colour}">{tag}</text>')
    return "\n".join(out)


def edge_svg(d, label, lx, ly, anchor):
    out = [f'  <path d="{d}" fill="none" stroke="{LINE}" stroke-width="1.6" marker-end="url(#arrow)"/>']
    if label:
        out.append(f'  <text x="{lx:g}" y="{ly:g}" text-anchor="{anchor}" font-family="{FONT}" font-size="13" '
                   f'fill="{MUTE}">{label}</text>')
    return "\n".join(out)


def build():
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
        f'aria-labelledby="title desc">',
        '  <title id="title">The shopfloor-skills hand-off loop</title>',
        '  <desc id="desc">Skills that see a problem hand it to skills that fix the cause, which hand the result '
        'to the skills that hold the gain in the control plan and station instructions. lead-daily-routine is '
        'available; solve-8d is coming soon; the other skills are planned.</desc>',
        '  <defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        f'orient="auto"><path d="M0 0L10 5L0 10Z" fill="{LINE}"/></marker></defs>',
        f'  <rect width="{W}" height="{H}" rx="16" fill="{CHALK}"/>',
    ]
    for x, title in LANES:
        parts.append(f'  <text x="{x}" y="70" font-family="{FONT}" font-size="20" font-weight="600" '
                     f'fill="{GRAPHITE}">{title}</text>')
        parts.append(f'  <rect x="{x}" y="80" width="{NODE_W}" height="3" fill="{GREEN}"/>')
    parts += [edge_svg(*e) for e in edges()]
    parts += [node_svg(n) for n in NODES]
    parts.append("</svg>\n")
    return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default="docs-site/public/hand-off-loop.svg")
    args = parser.parse_args()
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(build())
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
