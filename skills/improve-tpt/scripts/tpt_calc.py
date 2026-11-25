#!/usr/bin/env python3
"""Little's Law and WIP calculator for the improve-tpt skill (standard library only).

Examples:
  python3 tpt_calc.py line --wip 40 --throughput 0.4 --process-times 2,3,1,2 --machines 1,2,1,1 --hours-per-day 10 --target-tpt 50 --caps 12,20
  python3 tpt_calc.py kingman --u 0.9 --ca 1 --ce 1 --te 1

Rates are per hour. Process times are in hours unless --unit min is given.
"""
import argparse
import sys


def little_tpt(wip, throughput):
    """Throughput time = WIP / throughput (Little's Law)."""
    if throughput <= 0:
        raise ValueError("throughput must be positive")
    if wip < 0:
        raise ValueError("wip must not be negative")
    return wip / throughput


def raw_process_time(times):
    """T0 = sum of the average process times along the routing."""
    if not times or any(t <= 0 for t in times):
        raise ValueError("process times must be positive")
    return sum(times)


def bottleneck_rate(times, machines=None):
    """r_b = lowest station rate, machines / process time."""
    machines = machines or [1] * len(times)
    if len(machines) != len(times):
        raise ValueError("give one machine count per process time")
    if any(m <= 0 for m in machines):
        raise ValueError("machine counts must be positive")
    raw_process_time(times)
    return min(m / t for t, m in zip(times, machines))


def critical_wip(rb, t0):
    """W0 = r_b * T0."""
    return rb * t0


def best_case(w, t0, rb):
    """(TPT, TH) of the best case at WIP w."""
    w0 = critical_wip(rb, t0)
    if w <= w0:
        return t0, w / t0
    return w / rb, rb


def worst_case(w, t0):
    """(TPT, TH) of the worst case at WIP w."""
    return w * t0, 1 / t0


def practical_worst_case(w, t0, rb):
    """(TPT, TH) of the practical worst case at WIP w >= 1."""
    if w < 1:
        raise ValueError("wip must be at least 1")
    w0 = critical_wip(rb, t0)
    return t0 + (w - 1) / rb, rb * w / (w0 + w - 1)


def pwc_wip_needed(throughput, t0, rb):
    """WIP a practical-worst-case line needs for a throughput below r_b."""
    if not 0 < throughput < rb:
        raise ValueError("throughput must be positive and below the bottleneck rate")
    return throughput * (critical_wip(rb, t0) - 1) / (rb - throughput)


def kingman_queue(u, ca, ce, te):
    """Mean queue time ~ ((ca^2 + ce^2) / 2) * (u / (1 - u)) * te."""
    if not 0 <= u < 1:
        raise ValueError("utilisation must be at least 0 and below 1")
    if te <= 0 or ca < 0 or ce < 0:
        raise ValueError("te must be positive and the coefficients of variation not negative")
    return (ca ** 2 + ce ** 2) / 2 * (u / (1 - u)) * te


def numbers(text):
    return [float(part) for part in text.split(",") if part.strip()]


def line_report(args):
    times = numbers(args.process_times)
    if args.unit == "min":
        times = [t / 60 for t in times]
    machines = numbers(args.machines) if args.machines else None
    t0 = raw_process_time(times)
    rb = bottleneck_rate(times, machines)
    w0 = critical_wip(rb, t0)
    tpt = little_tpt(args.wip, args.throughput)
    lines = []
    days = f" = {tpt / args.hours_per_day:.2f} working days" if args.hours_per_day else ""
    lines.append(f"TPT (Little) = {args.wip:g} / {args.throughput:g} per h = {tpt:.2f} h{days}")
    if args.sample_tpt:
        gap = (tpt - args.sample_tpt) / args.sample_tpt * 100
        lines.append(f"Sample mean {args.sample_tpt:g} h; Little differs by {gap:+.1f}%")
    lines.append(f"T0 = {t0:.3f} h; r_b = {rb:.3f} per h; W0 = {w0:.2f}")
    lines.append(f"Bottleneck utilisation = {args.throughput / rb:.1%}; x-factor = {tpt / t0:.1f}")
    best = best_case(args.wip, t0, rb)
    pwc = practical_worst_case(args.wip, t0, rb)
    worst = worst_case(args.wip, t0)
    lines.append(f"At WIP {args.wip:g}: best TPT {best[0]:.2f} h, TH {best[1]:.3f}; "
                 f"PWC TPT {pwc[0]:.2f} h, TH {pwc[1]:.3f}; worst TPT {worst[0]:.2f} h, TH {worst[1]:.3f}")
    if tpt > pwc[0]:
        verdict = "worse than PWC"
    elif tpt < best[0]:
        verdict = "at or better than PWC, and below the best case: check the WIP and output data"
    else:
        verdict = "at or better than PWC (between best case and PWC)"
    lines.append(f"Measured TPT is {verdict}")
    if args.throughput < rb:
        lines.append(f"WIP the PWC needs for {args.throughput:g} per h = {pwc_wip_needed(args.throughput, t0, rb):.1f}")
    if args.target_tpt:
        lines.append(f"Target WIP for TPT {args.target_tpt:g} h = {args.throughput * args.target_tpt:.1f}")
    for cap in numbers(args.caps) if args.caps else []:
        c_tpt, c_th = practical_worst_case(cap, t0, rb)
        ok = "meets" if c_th >= args.throughput - 1e-9 else "misses"
        lines.append(f"Cap {cap:g}: PWC TH {c_th:.3f} per h ({ok} {args.throughput:g}), PWC TPT {c_tpt:.2f} h")
    return lines


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    line = sub.add_parser("line", help="Little's Law, critical WIP and PWC for a line")
    line.add_argument("--wip", type=float, required=True)
    line.add_argument("--throughput", type=float, required=True, help="good units per hour")
    line.add_argument("--process-times", required=True, help="comma list, one per step")
    line.add_argument("--machines", help="comma list, one per step (default 1 each)")
    line.add_argument("--unit", choices=("h", "min"), default="h", help="unit of the process times")
    line.add_argument("--hours-per-day", type=float, help="working hours per day, to print days")
    line.add_argument("--sample-tpt", type=float, help="tagged-sample mean TPT in hours")
    line.add_argument("--target-tpt", type=float, help="target TPT in hours")
    line.add_argument("--caps", help="comma list of WIP caps to check")
    king = sub.add_parser("kingman", help="queue time at one station")
    for name in ("u", "ca", "ce", "te"):
        king.add_argument(f"--{name}", type=float, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "line":
            out = line_report(args)
        else:
            q = kingman_queue(args.u, args.ca, args.ce, args.te)
            out = [f"Queue time = {q:.2f}; time at station = {q + args.te:.2f} (units of te)"]
    except ValueError as exc:
        parser.error(str(exc))
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
