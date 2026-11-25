#!/usr/bin/env python3
"""OEE and TEEP calculator for the measure-oee skill (standard library only).

Usage: python3 oee.py input.json

Input JSON for one machine (all times in minutes, cycle times in seconds):
{
  "all_time": 1440,
  "planned_production_time": 900,
  "stops": [{"reason": "changeover A to B", "loss": "setup", "minutes": 60}],
  "minor_stop_minutes": 30,
  "products": [{"name": "A", "ideal_cycle_s": 30, "total": 600, "scrap": 20, "rework": 0}]
}
Give a list of such objects under "machines" to aggregate several machines,
shifts or days. Aggregation sums the time buckets; it never averages percentages.
"""
import json
import sys


def compute(data):
    ppt = float(data["planned_production_time"])
    stops = [dict(s) for s in data.get("stops", [])]
    stop_minutes = sum(float(s["minutes"]) for s in stops)
    run_time = ppt - stop_minutes
    if run_time <= 0:
        raise ValueError("stops are as long as or longer than planned production time")
    net_run = 0.0
    fully_productive = 0.0
    quality_losses = []
    for p in data["products"]:
        ict_min = float(p["ideal_cycle_s"]) / 60
        bad = float(p.get("scrap", 0)) + float(p.get("rework", 0))
        if bad > float(p["total"]):
            raise ValueError(f"product {p.get('name', '?')}: scrap plus rework exceeds total")
        net_run += float(p["total"]) * ict_min
        fully_productive += (float(p["total"]) - bad) * ict_min
        for kind in ("scrap", "rework"):
            if float(p.get(kind, 0)):
                quality_losses.append({"reason": f"{kind} {p.get('name', '')}".strip(),
                                       "loss": kind, "minutes": float(p[kind]) * ict_min})
    performance_loss = run_time - net_run
    minor = float(data.get("minor_stop_minutes", 0))
    result = {
        "planned_production_time": ppt,
        "run_time": run_time,
        "net_run_time": net_run,
        "fully_productive_time": fully_productive,
        "availability": run_time / ppt,
        "performance": net_run / run_time,
        "quality": fully_productive / net_run if net_run else 0.0,
        "oee": fully_productive / ppt,
        "losses": stops + [
            {"reason": "short stops", "loss": "minor stops", "minutes": minor},
            {"reason": "speed loss (remainder)", "loss": "reduced speed", "minutes": performance_loss - minor},
        ] + quality_losses,
        "warnings": [],
    }
    if net_run > run_time:
        result["warnings"].append("performance above 100%: the ideal cycle time is set too slow")
    if minor > performance_loss:
        result["warnings"].append("logged short stops exceed the performance loss: check counts and cycle times")
    if "all_time" in data:
        all_time = float(data["all_time"])
        result["all_time"] = all_time
        result["utilisation"] = ppt / all_time
        result["teep"] = fully_productive / all_time
    result["losses"].sort(key=lambda item: -item["minutes"])
    return result


def aggregate(machines):
    parts = [compute(m) for m in machines]
    total = {key: sum(p[key] for p in parts) for key in
             ("planned_production_time", "run_time", "net_run_time", "fully_productive_time")}
    total["availability"] = total["run_time"] / total["planned_production_time"]
    total["performance"] = total["net_run_time"] / total["run_time"]
    total["quality"] = total["fully_productive_time"] / total["net_run_time"]
    total["oee"] = total["fully_productive_time"] / total["planned_production_time"]
    total["machines"] = parts
    return total


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print(__doc__)
        return 2
    with open(argv[0], encoding="utf-8") as handle:
        data = json.load(handle)
    result = aggregate(data["machines"]) if "machines" in data else compute(data)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
