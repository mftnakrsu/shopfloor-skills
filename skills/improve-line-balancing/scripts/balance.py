#!/usr/bin/env python3
"""Takt, operator count and fill-up yamazumi calculator (standard library only).

Usage: python3 balance.py line.json

line.json:
{
  "shift_seconds": 28800,
  "scheduled_stops_seconds": 1800,
  "shifts_per_day": 2,
  "demand_per_day": 1800,
  "planned_cycle_seconds": 28,
  "mix": {"A": 0.8, "B": 0.2},
  "current_operators": 5,
  "elements": [
    {"name": "Insert bearing", "seconds": 10},
    {"name": "Fit heat shield", "seconds": 10, "variants": ["B"]}
  ]
}

scheduled_stops_seconds holds breaks, meetings and cleanup only.
planned_cycle_seconds (default: takt), mix (default: one variant) and
current_operators (per shift) are optional. Elements are loaded in the
given (precedence) order. The output is JSON.
"""
import json
import math
import sys

DEFAULT_VARIANT = "all"


def effective_seconds(shift_seconds, scheduled_stops_seconds):
    """Shift time minus scheduled stops. Unplanned losses are never subtracted."""
    value = shift_seconds - scheduled_stops_seconds
    if value <= 0:
        raise ValueError("effective time must be positive")
    return value


def takt(effective_per_shift, demand_per_shift):
    if demand_per_shift <= 0:
        raise ValueError("demand must be positive")
    return effective_per_shift / demand_per_shift


def element_time(element, variant):
    variants = element.get("variants")
    if variants is None or variant in variants:
        return element["seconds"]
    return 0.0


def variant_content(elements, variant):
    return sum(element_time(e, variant) for e in elements)


def weighted_content(elements, mix):
    return sum(share * variant_content(elements, v) for v, share in mix.items())


def fraction_advice(operators_exact):
    """Rule of thumb for the fractional operator."""
    whole = math.floor(operators_exact)
    fraction = operators_exact - whole
    if fraction < 1e-9:
        return whole, "exact: no fractional operator"
    if fraction < 0.3:
        return whole, "below 0.3: do not add an operator; remove waste so the work fits"
    if fraction <= 0.5:
        return whole + 1, "0.3 to 0.5: start with the higher count, review after about two weeks of kaizen"
    return whole + 1, "above 0.5: add the operator and keep removing waste"


def fill_up(elements, mix, cap):
    """Load operators in order up to cap for every variant; remainder on the last."""
    operators, current = [], []

    def loads(group):
        return {v: sum(element_time(e, v) for e in group) for v in mix}

    for element in elements:
        if max(element_time(element, v) for v in mix) > cap + 1e-9:
            raise ValueError(f"element '{element['name']}' exceeds the planned cycle time on its own")
        trial = current + [element]
        if current and max(loads(trial).values()) > cap + 1e-9:
            operators.append(current)
            current = [element]
        else:
            current = trial
    if current:
        operators.append(current)
    result = []
    for number, group in enumerate(operators, 1):
        per_variant = loads(group)
        weighted = sum(mix[v] * per_variant[v] for v in mix)
        result.append({
            "operator": number,
            "elements": [e["name"] for e in group],
            "load_by_variant": per_variant,
            "weighted_load": round(weighted, 2),
            "gap_to_cap": round(cap - max(per_variant.values()), 2),
        })
    return result


def analyse(line):
    mix = line.get("mix") or {DEFAULT_VARIANT: 1.0}
    if abs(sum(mix.values()) - 1.0) > 1e-6:
        raise ValueError("mix shares must add up to 1")
    elements = line["elements"]
    shifts = line["shifts_per_day"]
    effective = effective_seconds(line["shift_seconds"], line["scheduled_stops_seconds"])
    demand_shift = line["demand_per_day"] / shifts
    takt_s = takt(effective, demand_shift)
    cap = line.get("planned_cycle_seconds") or takt_s
    if cap > takt_s + 1e-9:
        raise ValueError("planned cycle time must not exceed takt")
    content = weighted_content(elements, mix)
    exact = content / cap
    suggested, advice = fraction_advice(exact)
    yamazumi = fill_up(elements, mix, cap)
    new_ops = len(yamazumi)
    hours = effective / 3600
    out = {
        "effective_seconds_per_shift": effective,
        "demand_per_shift": demand_shift,
        "takt_seconds": round(takt_s, 2),
        "planned_cycle_seconds": round(cap, 2),
        "content_by_variant": {v: variant_content(elements, v) for v in mix},
        "weighted_content_seconds": round(content, 2),
        "operators_exact": round(exact, 2),
        "operators_by_fraction_rule": suggested,
        "fraction_rule": advice,
        "yamazumi": yamazumi,
        "operators_after_fill_up": new_ops,
        "line_efficiency_vs_takt": round(content / (new_ops * takt_s), 4),
        "units_per_labour_hour": round(line["demand_per_day"] / (new_ops * shifts * hours), 2),
    }
    current = line.get("current_operators")
    if current:
        before = line["demand_per_day"] / (current * shifts * hours)
        out["operators_saved_all_shifts"] = (current - new_ops) * shifts
        out["units_per_labour_hour_before"] = round(before, 2)
        out["productivity_gain"] = round(out["units_per_labour_hour"] / before - 1, 4)
    return out


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print(__doc__)
        return 2
    with open(argv[0], encoding="utf-8") as handle:
        line = json.load(handle)
    try:
        print(json.dumps(analyse(line), indent=2))
    except (ValueError, KeyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
