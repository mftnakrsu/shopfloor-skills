# shopfloor-skills: logo guidelines

> Status: first version. The maintainer chose the logo, the colours and the typeface on 2026-11-25.

## 1. The logo

- **Idea:** a yamazumi chart of a balanced line. Three stations split their work into 1, 2 and 3 blocks, and every stack ends level just under one takt line. The green line is the takt time; the stacks are the work. Nothing sticks out above the line.
- **Versions:** horizontal lockup, stacked lockup, symbol only, small-size symbol, wordmark only, icon tile.
- **Built from rectangles only,** on an 8-unit grid of the 256-unit symbol. That keeps it sharp on screen and simple to embroider, paint or cut.

| File | Use |
|---|---|
| `logo/lockup-horizontal-ink.svg`, `-white.svg` | Headers, documents, the docs site |
| `logo/lockup-stacked-ink.svg`, `-white.svg` | Square and narrow formats |
| `logo/symbol-ink.svg`, `-white.svg` | Symbol alone, 32 px and larger |
| `logo/symbol-small-ink.svg`, `-white.svg` | Symbol below 32 px: a 16-unit grid where every edge lands on a whole pixel at 16 px |
| `logo/wordmark-ink.svg`, `-white.svg` | Name alone |
| `logo/icon-tile.svg` | Avatar and app icon: Chalk stacks and a green line on a Graphite tile |
| `icons/` | Favicon and web icon set, with `head-snippet.html` and `site.webmanifest` |
| `social-preview.png` | Repository social preview, 1280 x 640. Source: `social-preview.svg` |
| `../../.claude-plugin/icon.png` | Plugin directory icon: the icon tile at 1024 x 1024 |

"Ink" files are for light backgrounds: Graphite stacks and text with a Line Green takt line. "White" files are for dark backgrounds: Chalk stacks and text with the lighter Line Green.

## 2. Animated assets

| File | Where |
|---|---|
| `hero-light.svg`, `hero-dark.svg` | Header banner, 1280 x 360, on pages that set their own background colour. Transparent |
| `icon-tile-animated.svg` | The icon tile with the same motion. Opaque Graphite, so it reads on any page. The README's header and the docs site's home page |
| `fallback/*.gif` | One loop of each animation, for places that do not animate SVG |
| `fallback/*.png` | The resting frame. The hero PNGs have an opaque background (white or `#0D1117`) |

The motion tells one story: work blocks stack up on the three stations, one after the other, until every stack ends level just under the takt line. The line is dim while the line is unbalanced and turns full green when it is balanced. Then the stacks clear and the loop starts again. One loop is 8 seconds, and it opens in the finished state, so a first glance shows the whole logo.

Motion rules:

1. Only `transform` and `opacity` are animated, with CSS inside the SVG.
2. Under `prefers-reduced-motion: reduce` every animation stops and the finished logo stays.
3. The resting state of every element is the static logo. A renderer that ignores CSS animation shows the static logo.
4. Blocks grow from their own base. They never overshoot the takt line.

README usage: the animated icon tile above the name. Do not switch images with `<picture>` in the README: the browser picks the source by the computer's colour scheme, while GitHub draws the page in the GitHub theme, so the wrong version can land on the wrong page colour. The tile is opaque and reads on both.

```html
<p align="center">
  <img src="assets/brand/icon-tile-animated.svg" width="96" height="96" alt="">
</p>

<h1 align="center">shopfloor-skills</h1>
```

## 3. Clear space

Keep a clear zone of one column width on all sides. One column is 48 units of the 256-unit symbol, a little under a fifth of its height. The zone scales with the logo.

## 4. Minimum size

| Version | Screen | Print |
|---|---|---|
| Horizontal lockup | 160 px wide | 30 mm wide |
| Stacked lockup | 96 px wide | 20 mm wide |
| Symbol | 32 px | 8 mm |
| Small-size symbol and favicon | 16 px | 5 mm |

Below 32 px, use `symbol-small-*.svg` or the files in `icons/`. They are drawn on a 16-unit grid, so the three columns and the line stay sharp at 16, 32 and 48 px.

## 5. Colour

| Name | HEX | RGB | CMYK (naive conversion) | Use |
|---|---|---|---|---|
| Graphite | `#1F2428` | 31 36 40 | 23 10 0 84 | Stacks and text on light backgrounds; the icon tile |
| Line Green | `#2E8A55` | 46 138 85 | 67 0 38 46 | The takt line on light backgrounds. The one signal colour |
| Line Green on dark | `#3FA56A` | 63 165 106 | 62 0 36 35 | The takt line on dark backgrounds |
| Chalk | `#F1F4F2` | 241 244 242 | 1 0 1 4 | Stacks and text on dark backgrounds; the diagram card |
| Mute | `#5B6368` on light, `#A9B3AE` on dark | | | Secondary text, such as the tagline |

Contrast (WCAG 2 ratios):

| Pair | Ratio |
|---|---|
| Graphite on white | 15.7:1 |
| Chalk on Graphite | 14.1:1 |
| Chalk on GitHub dark `#0D1117` | 17.1:1 |
| Line Green on white | 4.3:1 |
| Line Green on Chalk | 3.9:1 |
| Line Green on dark, on Graphite | 5.1:1 |
| Line Green on dark, on `#0D1117` | 6.1:1 |
| Mute on white | 6.1:1 |
| Mute on dark, on Graphite | 7.3:1 |

- Line Green clears 3:1, the level for graphics and large text, on every approved background. It does not reach 4.5:1 on white, so never set body text in Line Green on white. The docs site uses a deeper green, `#236B42` (6.5:1 on white), for links and buttons.
- Approved pairs: Graphite and Line Green on white or Chalk; Chalk and Line Green on dark on Graphite or another dark background.
- The CMYK values are arithmetic conversions. Check them against a physical guide before any print job.
- Why green: a takt line that is met is a green status on any shopfloor board. Green also stays clear of the red and yellow that boards use for alarms.

## 6. Typography

- **Wordmark and tagline:** Barlow Semi Condensed SemiBold (600) and Medium (500), converted to outlines. The wordmark is set without extra letter spacing, with the font's own kerning. Its x-height is 80 units next to the 256-unit symbol, centred on the symbol's middle.
- **Why this face:** a plain signage face, close in spirit to the DIN lettering on machines and floor markings. Its tall, narrow stems echo the stacks.
- **Licence:** Barlow Semi Condensed is under the SIL Open Font License 1.1, copyright 2017 The Barlow Project Authors. The logo files contain outlines only, no font files. The docs site serves the font from its own build, through the `@fontsource/barlow-semi-condensed` package, and publishes the licence at `/fonts/OFL-BarlowSemiCondensed.txt`.
- **Docs headings:** Barlow Semi Condensed SemiBold. Body text uses the system font stack.
- Do not recreate the wordmark by typing it. Use the files.

## 7. Don'ts

- Do not use any employer's colours, logos, typefaces or styling with this logo, and do not place it next to an employer's mark in a way that suggests an official product. This is an independent open-source project.
- Do not change the number of blocks or let a stack cross the takt line. The balanced line is the idea.
- Do not stretch, squash, rotate or skew the logo.
- Do not recolour it outside the palette, and do not use red or yellow in it.
- Do not add shadows, outlines, gradients or bevels.
- Do not rearrange the parts of a lockup or change the space between them.
- Do not place it on a busy photo or pattern without the icon tile.
- Do not use the full symbol below 32 px; use the small-size cut.

## 8. Rebuilding and limits

- Every file here is generated. See `design/brand/README.md` for the commands.
- No trademark search has been done. Run one before the project is published widely.
