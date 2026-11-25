#!/usr/bin/env python3
"""Render the raster files of the brand kit from the SVG sources.

- fallback/: GIF and PNG versions of the animated SVGs, for places that do not animate SVG.
  The frames are computed from the same timing constants as the CSS animation.
- icons/: favicon PNGs, favicon.ico, the Apple touch icon and the web-app icons.
- social-preview.png and .claude-plugin/icon.png.

Needs cairosvg (with the Cairo library), Pillow and fontTools; see ../README.md.
"""
import argparse
import io
import os
import sys

import cairosvg
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_brand as bb  # noqa: E402

FPS = 12.5
BACKGROUNDS = {"light": "#FFFFFF", "dark": bb.GH_DARK}


def png(svg_text, width, height=None):
    data = cairosvg.svg2png(bytestring=svg_text.encode("utf-8"), output_width=width,
                            output_height=height or width)
    return Image.open(io.BytesIO(data)).convert("RGBA")


def save_gif(frames, path):
    """frames: list of RGB images; one loop of the animation."""
    palette = frames[len(frames) // 2].quantize(colors=64, method=Image.Quantize.MEDIANCUT)
    quantized = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frames]
    quantized[0].save(path, save_all=True, append_images=quantized[1:], loop=0,
                      duration=round(1000 / FPS), optimize=True, disposal=1)


def loop_fractions():
    n = round(bb.ANIM_SECONDS * FPS)
    return [(bb.START_AT + i / n) % 1 for i in range(n)]


def flatten(img, colour):
    bg = Image.new("RGBA", img.size, colour)
    bg.alpha_composite(img)
    return bg.convert("RGB")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--semibold", required=True)
    parser.add_argument("--medium", required=True)
    parser.add_argument("--assets", default="assets/brand")
    parser.add_argument("--plugin-icon", default=".claude-plugin/icon.png")
    parser.add_argument("--site", default="docs-site")
    args = parser.parse_args()
    a = args.assets
    brand = bb.Brand(args.semibold, args.medium)
    fb = os.path.join(a, "fallback")
    icons = os.path.join(a, "icons")
    os.makedirs(fb, exist_ok=True)

    # Animated hero banners: GIF loop plus the resting frame as an opaque PNG.
    for theme in ("light", "dark"):
        frames = [flatten(png(brand.hero_frame(theme, f, BACKGROUNDS[theme]), 1280, 360), BACKGROUNDS[theme])
                  for f in loop_fractions()]
        save_gif([f.resize((640, 180), Image.LANCZOS) for f in frames], os.path.join(fb, f"hero-{theme}.gif"))
        rest = png(brand.hero_frame(theme, bb.HOLD_END, BACKGROUNDS[theme]), 1280, 360)
        flatten(rest, BACKGROUNDS[theme]).save(os.path.join(fb, f"hero-{theme}.png"), optimize=True)

    # Animated icon tile: opaque graphite, so the GIF uses white outside the rounded corners.
    frames = [flatten(png(bb.icon_tile_animated_svg(f), 192), "#FFFFFF") for f in loop_fractions()]
    save_gif(frames, os.path.join(fb, "icon-tile-animated.gif"))
    png(bb.icon_tile_animated_svg(bb.HOLD_END), 512).save(os.path.join(fb, "icon-tile-animated.png"), optimize=True)

    # Favicons: the 16-unit tile renders pixel-exact at 16, 32 and 48 px.
    fav = bb.favicon_svg()
    sizes = (16, 32, 48)
    fav_imgs = {s: png(fav, s) for s in sizes}
    for s, img in fav_imgs.items():
        img.save(os.path.join(icons, f"favicon-{s}.png"), optimize=True)
    fav_imgs[48].save(os.path.join(icons, "favicon.ico"), sizes=[(s, s) for s in sizes],
                      append_images=[fav_imgs[16], fav_imgs[32]])
    tile = open(os.path.join(a, "logo/icon-tile.svg"), encoding="utf-8").read()
    for s in (192, 512):
        png(tile, s).save(os.path.join(icons, f"icon-{s}.png"), optimize=True)
    png(open(os.path.join(icons, "app-icon-full-bleed.svg"), encoding="utf-8").read(), 180).convert("RGB").save(
        os.path.join(icons, "apple-touch-icon.png"), optimize=True)
    png(open(os.path.join(icons, "maskable.svg"), encoding="utf-8").read(), 512).convert("RGB").save(
        os.path.join(icons, "maskable-512.png"), optimize=True)

    # Social preview and the plugin directory icon.
    social = open(os.path.join(a, "social-preview.svg"), encoding="utf-8").read()
    png(social, 1280, 640).convert("RGB").save(os.path.join(a, "social-preview.png"), optimize=True)
    if args.plugin_icon:
        os.makedirs(os.path.dirname(args.plugin_icon), exist_ok=True)
        png(tile, 1024).save(args.plugin_icon, optimize=True)

    if args.site and os.path.isdir(os.path.join(args.site, "public")):
        pub = os.path.join(args.site, "public")
        for name in ("favicon.ico", "apple-touch-icon.png", "icon-192.png", "icon-512.png", "maskable-512.png"):
            with open(os.path.join(icons, name), "rb") as src, open(os.path.join(pub, name), "wb") as dst:
                dst.write(src.read())
    print("rendered fallbacks, icons, social preview and plugin icon")


if __name__ == "__main__":
    main()
