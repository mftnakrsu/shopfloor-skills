#!/usr/bin/env python3
"""Build the hand-off loop diagram (design spec, section 4.2) as a static SVG.

Standard library only. The diagram brings its own Chalk card, so it reads on light and dark
pages. Update AVAILABLE and SOON when a skill ships, then run this script again.
"""
import argparse
import os

GRAPHITE, GREEN, CHALK, MUTE, LINE = "#1F2428", "#2E8A55", "#F1F4F2", "#5B6368", "#6B7479"
AVAILABLE = {
    "lead-daily-routine", "solve-8d", "measure-oee", "improve-line-balancing", "improve-smed", "improve-tpt",
    "improve-tpm", "improve-vsm", "improve-kanban-pull", "improve-kaizen", "lead-gemba-walk", "measure-spc",
}
SOON = set()
FONT = "'Barlow Semi Condensed', 'Segoe UI', system-ui, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

W, H = 1550, 850
# (x, width, heading) per lane. The gaps between lanes (210 units) carry the arrows and their labels.
LANES = [(40, 300, "See the problem"), (550, 350, "Fix the cause"), (1110, 400, "Hold the gain")]
NODE_H, ROW = 56, 26

# name -> (lane, top y, skills shown in the box, height or None for the default)
NODES = {
    "oee": (0, 154, ["measure-oee"], None),
    "ldr": (0, 326, ["lead-daily-routine"], None),
    "spc": (0, 422, ["measure-spc"], None),
    "gemba": (0, 518, ["lead-gemba-walk"], None),
    "audit": (0, 614, ["audit-process"], None),
    "vsm": (0, 724, ["improve-vsm"], None),
    "smed": (1, 112, ["improve-smed"], None),
    "tpm": (1, 196, ["improve-tpm"], None),
    "solve": (1, 300, ["solve-5why", "solve-fishbone", "solve-8d"], 136),
    "kaizen": (1, 518, ["improve-kaizen"], None),
    "flow": (1, 698, ["improve-tpt", "improve-kanban-pull", "improve-line-balancing"], None),
    "cp": (2, 340, ["plan-control-plan"], None),
    "wi": (2, 724, ["plan-workstation-instructions"], None),
}


def box(name):
    lane, y, skills, h = NODES[name]
    x, w, _ = LANES[lane]
    return x, y, w, h or NODE_H + ROW * (len(skills) - 1)


def left(name):
    return box(name)[0]


def right(name):
    x, _, w, _ = box(name)
    return x + w


def path(*pts, r=10):
    """An orthogonal path through the points, with rounded corners and the end pulled back for the arrowhead."""
    pts = list(pts)
    (ex, ey), (px, py) = pts[-1], pts[-2]
    pts[-1] = (ex - 2 if ex > px else ex + 2 if ex < px else ex, ey - 2 if ey > py else ey + 2 if ey < py else ey)
    d = f"M{pts[0][0]:g} {pts[0][1]:g}"
    for (x0, y0), (x1, y1), (x2, y2) in zip(pts, pts[1:], pts[2:]):
        sx = (x1 > x0) - (x1 < x0)
        sy = (y1 > y0) - (y1 < y0)
        tx = (x2 > x1) - (x2 < x1)
        ty = (y2 > y1) - (y2 < y1)
        d += f"L{x1 - sx * r:g} {y1 - sy * r:g}Q{x1:g} {y1:g} {x1 + tx * r:g} {y1 + ty * r:g}"
    return d + f"L{pts[-1][0]:g} {pts[-1][1]:g}"


def edges():
    """(path, label, label x, label y, text-anchor) for every hand-off in spec section 4.2.

    Each label sits on a straight run of its own arrow, clear of the other arrows.
    """
    l1, l2, l3 = right("ldr"), left("solve"), left("cp")
    mid1, mid2 = (l1 + l2) / 2, (right("solve") + l3) / 2
    out = []
    # measure-oee: three exits, routed so that no two of them cross.
    out.append((path((l1, 166), (400, 166), (400, 140), (l2, 140)), "set-up loss", (400 + l2) / 2, 132, "middle"))
    out.append((path((l1, 182), (420, 182), (420, 224), (l2, 224)), "breakdowns", (420 + l2) / 2, 216, "middle"))
    out.append((path((l1, 198), (380, 198), (380, 322), (l2, 322)), "defects", (380 + l2) / 2, 314, "middle"))
    out.append((path((l1, 354), (l2, 354)), "red KPI, cause unknown", mid1, 346, "middle"))
    x = 130
    out.append((path((x, box("ldr")[1]), (x, box("oee")[1] + NODE_H)), "red OEE KPI", x + 12, 272, "start"))
    out.append((path((x, box("spc")[1]), (x, box("ldr")[1] + NODE_H)), "out of control: escalate", x + 12, 407, "start"))
    out.append((path((l1, 530), (440, 530), (440, 386), (l2, 386)), "observations", (440 + l2) / 2, 378, "middle"))
    out.append((path((l1, 546), (l2, 546)), "observations", l1 + 12, 564, "start"))
    out.append((path((l1, 630), (480, 630), (480, 418), (l2, 418)), "findings", l1 + 12, 622, "start"))
    out.append((path((l1, 654), (1060, 654), (1060, 382), (l3, 382)), "findings", l2 + 10, 646, "start"))
    out.append((path((l1, 752), (l2, 752)), "future state", mid1, 772, "middle"))
    out.append((path((l1, 736), (500, 736), (500, 562), (l2, 562)), "kaizen bursts", l1 + 12, 728, "start"))
    out.append((path((right("solve"), 356), (l3, 356)), "root cause fixed", mid2, 348, "middle"))
    x = 820
    out.append((path((x, box("solve")[1]), (x, box("tpm")[1] + NODE_H)), "D7: maintenance plan", x - 12, 284, "end"))
    x = l3 + 200
    out.append((path((x, box("cp")[1] + NODE_H), (x, box("wi")[1])), "update", x + 12, 565, "start"))
    out.append((path((right("flow"), 752), (l3, 752)), "new standard work", mid2, 744, "middle"))
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
    first = y + h / 2 - ROW * (len(skills) - 1) / 2 + 6
    for i, s in enumerate(skills):
        ty = first + ROW * i
        weight = "700" if s in AVAILABLE else "400"
        out.append(f'  <text x="{x + 16}" y="{ty:g}" font-family="{MONO}" font-size="17" font-weight="{weight}" '
                   f'fill="{GRAPHITE}">{s}</text>')
        tag = status(s)
        colour = GREEN if tag == "available" else MUTE
        out.append(f'  <text x="{x + w - 14}" y="{ty:g}" text-anchor="end" font-family="{FONT}" font-size="16" '
                   f'fill="{colour}">{tag}</text>')
    return "\n".join(out)


def edge_svg(d, label, lx, ly, anchor):
    out = [f'  <path d="{d}" fill="none" stroke="{LINE}" stroke-width="1.75" marker-end="url(#arrow)"/>']
    if label:
        # A Chalk halo keeps the label readable where another arrow passes close by.
        out.append(f'  <text x="{lx:g}" y="{ly:g}" text-anchor="{anchor}" font-family="{FONT}" font-size="16" '
                   f'fill="{MUTE}" stroke="{CHALK}" stroke-width="5" stroke-linejoin="round" '
                   f'paint-order="stroke">{label}</text>')
    return "\n".join(out)


def build():
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
        f'aria-labelledby="title desc">',
        '  <title id="title">The shopfloor-skills hand-off loop</title>',
        '  <desc id="desc">Skills that see a problem hand it to skills that fix the cause, which hand the result '
        'to the skills that hold the gain in the control plan and station instructions. lead-daily-routine, '
        'solve-8d, lead-gemba-walk, measure-oee, measure-spc, improve-line-balancing, improve-smed, improve-tpt, '
        'improve-tpm, improve-vsm, improve-kanban-pull and improve-kaizen are available; '
        'the other skills are planned.</desc>',
        '  <defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        f'orient="auto"><path d="M0 0L10 5L0 10Z" fill="{LINE}"/></marker></defs>',
        f'  <rect width="{W}" height="{H}" rx="16" fill="{CHALK}"/>',
    ]
    for x, w, title in LANES:
        parts.append(f'  <text x="{x}" y="62" font-family="{FONT}" font-size="24" font-weight="600" '
                     f'fill="{GRAPHITE}">{title}</text>')
        parts.append(f'  <rect x="{x}" y="76" width="{w}" height="3" fill="{GREEN}"/>')
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
