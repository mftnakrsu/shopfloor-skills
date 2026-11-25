#!/usr/bin/env python3
"""Control limits and run-rule check for the measure-spc skill (standard library only).

Usage: python3 spc_limits.py input.json

Input JSON, one of:
  {"chart": "xbar_r", "subgroups": [[x, x, x], ...]}
  {"chart": "xbar_r", "n": 4, "means": [...], "ranges": [...]}
  {"chart": "imr", "values": [...]}
  {"chart": "p", "defectives": [...], "inspected": [...]}
Optional for Phase II on X-bar/R and I-MR: "baseline": {"centre": c, "spread": r_bar_or_mr_bar}
to judge the points against frozen limits instead of limits from the same data.
Run rules are Western Electric 1 to 4; a point exactly on a zone line counts as inside.
"""
import json
import math
import sys

# n: (A2, D3, D4, d2), NIST/SEMATECH e-Handbook 6.3.2.1; d2 from the standard factor table.
CONSTANTS = {
    2: (1.880, 0.0, 3.267, 1.128),
    3: (1.023, 0.0, 2.575, 1.693),
    4: (0.729, 0.0, 2.282, 2.059),
    5: (0.577, 0.0, 2.115, 2.326),
    6: (0.483, 0.0, 2.004, 2.534),
    7: (0.419, 0.076, 1.924, 2.704),
    8: (0.373, 0.136, 1.864, 2.847),
    9: (0.337, 0.184, 1.816, 2.970),
    10: (0.308, 0.223, 1.777, 3.078),
}


def mean(values):
    values = list(values)
    if not values:
        raise ValueError("no data")
    return sum(values) / len(values)


def run_rules(points, centre, sigma):
    """Western Electric rules 1-4. Returns signals as dicts with 1-based 'at'.

    Every point beyond a limit (rule 1) is its own signal; a lasting pattern (rules 2-4)
    is reported once, where it first fires.
    """
    if sigma <= 0:
        raise ValueError("sigma must be greater than zero")
    z = [round((p - centre) / sigma, 9) for p in points]
    hits = []
    for i in range(len(z)):
        for side, sign in (("high", 1), ("low", -1)):
            s = [sign * v for v in z[: i + 1]]
            if s[-1] > 3:
                hits.append((1, side, i))
            if len(s) >= 3 and sum(v > 2 for v in s[-3:]) >= 2 and s[-1] > 2:
                hits.append((2, side, i))
            if len(s) >= 5 and sum(v > 1 for v in s[-5:]) >= 4 and s[-1] > 1:
                hits.append((3, side, i))
            if len(s) >= 8 and all(v > 0 for v in s[-8:]):
                hits.append((4, side, i))
    signals, last = [], {}
    for rule, side, i in sorted(hits, key=lambda h: (h[2], h[0])):
        key = (rule, side)
        if rule == 1 or last.get(key) != i - 1:
            signals.append({"rule": rule, "side": side, "at": i + 1})
        last[key] = i
    return signals


def beyond(points, ucl, lcl):
    return [i + 1 for i, p in enumerate(points) if p > ucl or (lcl is not None and p < lcl)]


def xbar_r(data):
    if "subgroups" in data:
        groups = [list(map(float, g)) for g in data["subgroups"]]
        sizes = {len(g) for g in groups}
        if len(sizes) != 1:
            raise ValueError("all subgroups must have the same size for X-bar/R; use X-bar/S")
        n = sizes.pop()
        means = [mean(g) for g in groups]
        ranges = [max(g) - min(g) for g in groups]
    else:
        n = int(data["n"])
        means = list(map(float, data["means"]))
        ranges = list(map(float, data["ranges"]))
        if len(means) != len(ranges):
            raise ValueError("means and ranges must have the same length")
    if n not in CONSTANTS:
        raise ValueError("X-bar/R constants cover n = 2 to 10; use X-bar/S above 10")
    a2, d3, d4, d2 = CONSTANTS[n]
    base = data.get("baseline")
    centre = float(base["centre"]) if base else mean(means)
    r_bar = float(base["spread"]) if base else mean(ranges)
    sigma_mean = a2 * r_bar / 3
    result = {
        "chart": "xbar_r", "n": n, "subgroups": len(means),
        "centre": centre, "ucl": centre + a2 * r_bar, "lcl": centre - a2 * r_bar,
        "r_bar": r_bar, "r_ucl": d4 * r_bar, "r_lcl": d3 * r_bar,
        "process_sigma": r_bar / d2, "sigma_of_mean": sigma_mean,
    }
    result["range_beyond"] = beyond(ranges, result["r_ucl"], result["r_lcl"] if d3 else None)
    result["signals"] = run_rules(means, centre, sigma_mean)
    return result


def imr(data):
    values = list(map(float, data["values"]))
    if len(values) < 2:
        raise ValueError("need at least two values")
    mrs = [abs(b - a) for a, b in zip(values, values[1:])]
    base = data.get("baseline")
    centre = float(base["centre"]) if base else mean(values)
    mr_bar = float(base["spread"]) if base else mean(mrs)
    sigma = mr_bar / 1.128
    result = {
        "chart": "imr", "points": len(values),
        "centre": centre, "ucl": centre + 3 * sigma, "lcl": centre - 3 * sigma,
        "mr_bar": mr_bar, "mr_ucl": 3.267 * mr_bar, "sigma": sigma,
    }
    # Reported as the number of the later value in each pair whose moving range is beyond the limit.
    result["mr_beyond_at_value"] = [i + 1 for i in beyond(mrs, result["mr_ucl"], None)]
    result["signals"] = run_rules(values, centre, sigma)
    return result


def p_chart(data):
    defectives = list(map(float, data["defectives"]))
    inspected = list(map(float, data["inspected"]))
    if len(defectives) != len(inspected):
        raise ValueError("defectives and inspected must have the same length")
    if any(n <= 0 for n in inspected):
        raise ValueError("every subgroup needs a number inspected greater than zero")
    if any(d > n for d, n in zip(defectives, inspected)):
        raise ValueError("defectives cannot exceed the number inspected")
    p_bar = sum(defectives) / sum(inspected)
    rows = []
    for i, (d, n) in enumerate(zip(defectives, inspected), 1):
        half = 3 * math.sqrt(p_bar * (1 - p_bar) / n)
        lcl = p_bar - half
        p = d / n
        ucl = p_bar + half
        rows.append({"subgroup": i, "p": p, "ucl": ucl, "lcl": lcl if lcl > 0 else None,
                     "beyond": p > ucl or (lcl > 0 and p < lcl)})
    above = [r["p"] > p_bar for r in rows]
    below = [r["p"] < p_bar for r in rows]
    runs = []
    for side, flags in (("high", above), ("low", below)):
        for i in range(7, len(flags)):
            if all(flags[i - 7: i + 1]) and not (i > 7 and all(flags[i - 8: i])):
                runs.append({"rule": 4, "side": side, "at": i + 1})
    return {"chart": "p", "p_bar": p_bar, "subgroups": rows,
            "signals": [{"rule": 1, "side": "high" if r["p"] > p_bar else "low", "at": r["subgroup"]}
                        for r in rows if r["beyond"]] + runs}


CHARTS = {"xbar_r": xbar_r, "imr": imr, "p": p_chart}


def compute(data):
    chart = data.get("chart")
    if chart not in CHARTS:
        raise ValueError("chart must be one of: " + ", ".join(CHARTS))
    return CHARTS[chart](data)


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as handle:
        data = json.load(handle)
    try:
        result = compute(data)
    except (ValueError, KeyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
