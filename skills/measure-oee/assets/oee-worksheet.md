# OEE worksheet

Asset or line: ______ · Bottleneck: yes / no · Period: ______ · Prepared by: ______ · Date: ______

## Time model

- Convention: all stops except planned breaks and unscheduled time are losses / ISO 22400-2 (planned downtime outside) / other: ______
- Stop threshold (logged stop versus short stop): ______ min, set by local policy
- Ideal cycle time source (best demonstrated rate, design rate): ______

| Bucket | Formula | Minutes |
|---|---|---|
| All time | calendar time of the period | |
| Unscheduled time | not staffed or not planned | |
| Planned breaks | | |
| Planned production time (PPT) | scheduled time − planned breaks | |
| Logged stops | sum of stop log | |
| Run time (RT) | PPT − logged stops | |
| Net run time (NRT) | Σ total count × ideal cycle time | |
| Fully productive time (FPT) | Σ good count × ideal cycle time | |

## Counts per product

| Product | Ideal cycle (s) | Total | Scrap | Rework | Good | NRT (min) | FPT (min) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Factors

| Factor | Formula | Result |
|---|---|---|
| Availability | RT / PPT | |
| Performance | NRT / RT | |
| Quality | FPT / NRT | |
| OEE | A × P × Q = FPT / PPT | |
| Utilisation | PPT / all time | |
| TEEP | OEE × utilisation = FPT / all time | |

Check: A × P × Q = FPT / PPT (within rounding): ______

## Loss tree (minutes, ranked)

| Rank | Factor | Big loss | Reason | Minutes | Parts lost | Route | Owner | Due |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| | | | | | | | | |
| | | | | **Total = PPT − FPT** | | | | |

Schedule loss for TEEP (all time − PPT): ______ min

## Gaming and aggregation checks

| Check | Found? | Corrected figure |
|---|---|---|
| Changeover or planned maintenance moved out of PPT | | |
| Ideal cycle time slower than best demonstrated | | |
| Rework or sorted parts counted as good | | |
| Stop threshold changed | | |
| Percentages averaged across machines, shifts or days | | |
| Headline OEE hides a falling factor | | |

## Open questions

- ______
