#!/usr/bin/env python3
"""Kanban, CONWIP and pitch calculator for the improve-kanban-pull skill (standard library only).

Examples:
  python3 kanban_calc.py cards --demand 50 --lead-times 0.5,0,3,1.5,1 --container 40 --safety 0.1 --batch 3
  python3 kanban_calc.py pitch --available 25200 --demand 420 --pack 12
  python3 kanban_calc.py conwip --output 25 --target-tpt 2

Demand and lead times must use the same clock (for example pieces per hour and hours).
"""
import argparse
import math
import sys


def lead_time(components):
    """Replenishment lead time L = sum of the loop components."""
    if not components or any(c < 0 for c in components):
        raise ValueError("lead-time components must not be negative")
    total = sum(components)
    if total <= 0:
        raise ValueError("lead time must be positive")
    return total


def kanban_cards(demand, lead, container, safety=0.0, batch=1):
    """Toyota formula n = D x L x (1 + s) / a, rounded up, plus batch - 1 cards.

    Returns (raw value, cards).
    """
    if demand <= 0 or lead <= 0 or container <= 0:
        raise ValueError("demand, lead time and container quantity must be positive")
    if safety < 0:
        raise ValueError("safety factor must not be negative")
    if batch < 1 or int(batch) != batch:
        raise ValueError("batch must be a whole number of at least 1")
    raw = demand * lead * (1 + safety) / container
    # Guard against float noise such as 8.000000001 before rounding up.
    cards = math.ceil(round(raw, 9)) + int(batch) - 1
    return raw, cards


def takt(available, demand):
    """Takt = available working time / customer demand."""
    if available <= 0 or demand <= 0:
        raise ValueError("available time and demand must be positive")
    return available / demand


def pitch(available, demand, pack):
    """Pitch = takt x pack-out quantity."""
    if pack <= 0:
        raise ValueError("pack-out quantity must be positive")
    return takt(available, demand) * pack


def conwip_cards(output, target_tpt):
    """CONWIP cards = output x target throughput time (Little's Law), rounded up."""
    if output <= 0 or target_tpt <= 0:
        raise ValueError("output and target throughput time must be positive")
    return math.ceil(round(output * target_tpt, 9))


def floats(text):
    return [float(x) for x in text.split(",") if x.strip()]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    c = sub.add_parser("cards", help="kanban cards for one loop")
    c.add_argument("--demand", type=float, required=True, help="demand per time unit")
    c.add_argument("--lead-times", required=True, help="comma list of lead-time components")
    c.add_argument("--container", type=float, required=True, help="pieces per container")
    c.add_argument("--safety", type=float, default=0.0, help="safety factor as a share, set by local policy")
    c.add_argument("--batch", type=int, default=1, help="cards collected before a lot starts")
    p = sub.add_parser("pitch", help="takt and pitch at the pacemaker")
    p.add_argument("--available", type=float, required=True, help="available time per day in seconds")
    p.add_argument("--demand", type=float, required=True, help="customer demand per day")
    p.add_argument("--pack", type=float, required=True, help="pack-out quantity")
    w = sub.add_parser("conwip", help="CONWIP cards from Little's Law")
    w.add_argument("--output", type=float, required=True, help="output needed per time unit")
    w.add_argument("--target-tpt", type=float, required=True, help="target throughput time, same clock")
    args = parser.parse_args(argv)
    try:
        if args.command == "cards":
            lead = lead_time(floats(args.lead_times))
            raw, n = kanban_cards(args.demand, lead, args.container, args.safety, args.batch)
            out = [
                f"L = {lead:g}",
                f"D x L x (1 + s) / a = {args.demand:g} x {lead:g} x {1 + args.safety:g} / {args.container:g} = {raw:.2f}",
                f"Cards = {n} (rounded up, plus {args.batch - 1} for batching); maximum loop stock = {n * args.container:g}",
            ]
        elif args.command == "pitch":
            t = takt(args.available, args.demand)
            pt = pitch(args.available, args.demand, args.pack)
            out = [f"Takt = {t:.1f} s", f"Pitch = {pt:.0f} s = {pt / 60:.1f} min"]
        else:
            out = [f"CONWIP cards = {conwip_cards(args.output, args.target_tpt)}; check output with the practical-worst-case formula"]
    except ValueError as exc:
        parser.error(str(exc))
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
