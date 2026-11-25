# Throughput time study

Line or value stream: ______ · Product family: ______ · Date: ______ · Prepared by: ______

## 1. Terms

| Term the user uses | Meaning here | Mapped to (TPT, TH, WIP, station cycle time, order lead time) |
|---|---|---|
| | | |

## 2. Boundary

- Start point: ______ · End point: ______
- Flow unit (piece, job, lot, order): ______
- Clock (working hours per day, or calendar days): ______
- Counted inside the boundary (queues, in process, transit, rework, quarantine): ______

## 3. Measurement

| Item | Value | Unit | Source (count, report, sample) |
|---|---|---|---|
| WIP, mean of counts (number of days: __) | | units | |
| Good output over the same window | | units per day | |
| TPT = WIP ÷ TH | | working days / hours | computed |
| Tagged sample: number of units, mean, slowest, 85th or 95th percentile | | | |
| Difference Little against sample | | % | consistent if about 10% or less (rule of thumb) |

Data problems found and fixed: ______

## 4. Reference points

| Step | Effective process time t_i | Machines m_i | Rate m_i ÷ t_i |
|---|---|---|---|
| | | | |

- Raw process time T0 = Σ t_i = ______
- Bottleneck: ______ · r_b = ______
- Critical WIP W0 = r_b × T0 = ______
- Bottleneck utilisation u = TH ÷ r_b = ______
- X-factor = TPT ÷ T0 = ______

## 5. Practical-worst-case comparison

| At today's WIP w = ____ | Measured | Best case | Practical worst case |
|---|---|---|---|
| TPT | | | T0 + (w − 1) ÷ r_b = |
| TH | | | r_b × w ÷ (W0 + w − 1) = |

- WIP the PWC needs for today's output: TH × (W0 − 1) ÷ (r_b − TH) = ______
- Verdict (between best case and PWC, or worse than PWC): ______

## 6. Levers

| Finding | Lever (WIP cap, bottleneck capacity, variability, batch size, release rule, T0) | Target in numbers | Owner | Due |
|---|---|---|---|---|
| | | | | |

WIP cap: mechanism ______ · start cap ______ · target cap = TH × target TPT = ______ · output check at the cap: r_b × w ÷ (W0 + w − 1) = ______ · step-down rule ______ · owner of the cap ______

## 7. Tracking

| KPI | Today | Target | Frequency | Owner |
|---|---|---|---|---|
| TPT, mean | | | weekly | |
| TPT, slowest or percentile | | | weekly | |
| WIP | | | daily | |
| Good output | | | daily | |
| Bottleneck utilisation | | | weekly | |
| On-time delivery | | | weekly | |

## Open questions and assumptions

- ______
