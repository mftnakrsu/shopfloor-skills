# MTBF and MTTR

Exact definitions, a worked example, how to combine machines, and how to read the trend.

## Definitions

| Term | Formula | Notes |
|---|---|---|
| Operating time | Planned production time − breakdown downtime − planned stops inside that time | Up time only. Never calendar time |
| Failure | An unplanned stop longer than the breakdown threshold | Threshold set by local policy, for example 2 minutes (Vorne). Planned maintenance is not a failure (Wikipedia, MTBF) |
| MTBF (mean time between failures) | Operating time ÷ number of failures | Sum of up periods ÷ failures (Wikipedia, MTBF) |
| MTTR (mean time to repair) | Breakdown downtime ÷ number of failures | This skill uses stop to restart. Some sites count hands-on repair only (Wikipedia, MTTR); ask which, and state it |
| Availability from MTBF and MTTR | MTBF ÷ (MTBF + MTTR) | Operational, since MTTR from stop to restart includes waiting for parts and people; inherent only when MTTR is hands-on repair |
| Inherent availability | MTBF ÷ (MTBF + mean hands-on repair time) | Excludes planned maintenance and logistic delays (Wikipedia, Availability) |

Use the same period, the same machine and the same failure threshold in every comparison. MTTR is most meaningful between machines of the same type (SMRP).

## Worked example (invented numbers)

A press, one month.

- Planned production time 432 h. 8 failures, 24 h downtime from stop to restart. 2 planned maintenance stops of 4 h.
- Operating time = 432 − 24 − 8 = 400 h.
- MTBF = 400 ÷ 8 = 50 h.
- MTTR = 24 ÷ 8 = 3 h.
- Availability from MTBF and MTTR ≈ 50 ÷ (50 + 3) = 94.3% (operational, since MTTR includes waiting).
- Breakdown loss in the OEE loss tree = 24 h = 1,440 min; on 432 h planned it costs 24 ÷ 432 = 5.6 availability points.
- The two bases differ: operating time ÷ planned production time = 400 ÷ 432 = 92.6%, because the planned stops count against it, while MTBF ÷ (MTBF + MTTR) = 94.3% leaves them out. State which basis is used.

Wrong: counting the 2 planned stops as failures gives 400 ÷ 10 = 40 h; using planned production time gives 432 ÷ 8 = 54 h. Both mislead.

Downtime split, same example: 12 h repair, 9 h waiting for parts, 3 h waiting for a technician. Half the downtime is waiting, so the first actions are spares and response, not repair skill.

## Several machines

Pool, never average:

- Machine A: 400 h, 8 failures (MTBF 50 h). Machine B: 100 h, 1 failure (MTBF 100 h).
- Average of MTBFs = 75 h (wrong).
- Pooled MTBF = (400 + 100) ÷ (8 + 1) = 55.6 h (right).
- Pooled MTTR = total downtime ÷ total failures.

## Reading the trend

- MTBF falling: the machine fails more often. Look for deterioration (dirt, missing lubrication, loose parts), a new failure mode, or a PM interval that is too long.
- MTTR rising: repairs take longer. Split downtime into response, diagnosis, waiting for parts, repair and test, and act on the largest part.
- A single long repair can move MTTR a lot when there are few failures; with fewer than about five failures in the period, show the failure list rather than a trend (rule of thumb).
- Sort failures by mode. Repeats of the same mode need a root cause, not only faster repair.

## Data to log per failure

Machine, date, stop time, restart time, failure mode, part, cause found, response time, waiting for parts, repair time, test time, who repaired, spare parts used. Template: the breakdown log asset.

## Sources

- Wikipedia: [Mean time between failures](https://en.wikipedia.org/wiki/Mean_time_between_failures)
- Wikipedia: [Mean time to repair](https://en.wikipedia.org/wiki/Mean_time_to_repair)
- Wikipedia: [Availability](https://en.wikipedia.org/wiki/Availability)
- SMRP: [Best practices metrics guidelines](https://smrp.org/Resources/SMRP-Library/Best-Practices-Metrics-Guidelines) (MTTR metric; copyrighted, summarised only)
- Tractian: [Reliability performance indicators](https://tractian.com/en/glossary/reliability-performance-indicators)
- Vorne: [The six big losses](https://www.oee.com/oee-six-big-losses/)
