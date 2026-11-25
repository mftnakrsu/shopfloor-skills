# Flow formulas

The exact formulas for throughput time, critical WIP, the three reference cases and queue time, with a worked example.

## Contents

- Symbols
- Little's Law
- Reference points
- Best case, worst case and practical worst case
- WIP the practical worst case needs
- Queue time at one station (Kingman)
- Effective process time
- Worked example
- Status of the formulas
- Sources

## Symbols

| Symbol | Meaning | Unit |
|---|---|---|
| WIP, w | Mean count of units between the start and end point | units |
| TH | Good output rate | units per time |
| TPT | Mean time a unit spends between the two points (Factory Physics: CT) | time |
| t_i, m_i | Average effective process time and number of parallel machines of step i | time; count |
| T0 | Raw process time | time |
| r_b | Bottleneck rate | units per time |
| W0 | Critical WIP | units |
| u | Utilisation | share |
| ca, ce | Coefficients of variation (standard deviation ÷ mean) of interarrival times and of effective process times | — |

## Little's Law

WIP = TH × TPT, so TPT = WIP ÷ TH and WIP = TH × TPT (Little 2011; Gallego). At constant output, WIP and TPT move in proportion: TPT cannot fall without WIP falling, and the other way round (FabTime).

## Reference points

- T0 = Σ t_i: the time one unit takes through an empty line, with no waiting (Gallego).
- Station rate = m_i ÷ t_i. r_b = the lowest station rate, the station with the least long-term capacity (Gallego).
- W0 = r_b × T0: the WIP at which an ideal line just reaches full output with no waiting (Gallego).
- Bottleneck utilisation u = TH ÷ r_b.
- X-factor = TPT ÷ T0: how many times longer a unit takes than its raw process time (FabTime).

## Best case, worst case and practical worst case

For a line holding w units (Hopp & Spearman, as presented by Gallego):

| Case | TPT | TH |
|---|---|---|
| Best (no variability) | T0 if w ≤ W0, else w ÷ r_b | w ÷ T0 if w ≤ W0, else r_b |
| Practical worst case (PWC) | T0 + (w − 1) ÷ r_b | r_b × w ÷ (W0 + w − 1) |
| Worst | w × T0 | 1 ÷ T0 |

- A line between best case and PWC is managed effectively. A line between PWC and worst case has large improvement potential (Gallego).
- Raising r_b helps TPT and TH when WIP is above W0. Cutting T0 helps only when WIP is below W0 (Gallego).
- The PWC is the line with the same T0 and r_b, balanced, with highly variable (exponential) process times (Gallego). It is a benchmark, not a forecast.

## WIP the practical worst case needs

Rearranging the PWC throughput formula for a required output TH below r_b gives the WIP a PWC line would need for it (our derivation from the formula above):

w_PWC = TH × (W0 − 1) ÷ (r_b − TH)

A line holding much more than w_PWC for its output carries WIP that only adds waiting. As TH approaches r_b, w_PWC grows without limit: near the bottleneck rate, small output gains cost a lot of WIP.

## Queue time at one station (Kingman)

Mean queue time ≈ [(ca² + ce²) ÷ 2] × [u ÷ (1 − u)] × t_e, written V × U × t (Kingman 1961; Factory Physics notation via MetricGate). The station's time = queue time + t_e.

- The formula is a G/G/1 approximation, accurate especially near saturation (Wikipedia); it is weaker at very low or very high load and for very high variability (WSC 2014).
- Sensitivity at V = 0.625 and t_e = 1: queue time 1.46 at u = 0.70, 2.50 at 0.80, 5.63 at 0.90, 11.9 at 0.95 (MetricGate). Above about 85% loading, TPT rises steeply (FabTime).

Example (invented): t_e = 1 h, u = 0.90, ca = ce = 1 → V = 1, U = 9, queue 9 h. Halving ce → V = 0.625, queue 5.6 h. Utilisation 0.80 instead → U = 4, queue 4 h. Both → 2.5 h, 72% less.

## Effective process time

- With availability A, t_e = t0 ÷ A (Hopp & Spearman, ch. 8, as summarised in public course material). Example (invented): t0 = 9 min, A = 90% → t_e = 10 min.
- At equal availability, long and rare stops raise ce more than short and frequent ones; set-ups raise both the mean and ce (Hopp & Spearman, ch. 8; rule of thumb here, because it was not checked against the book).
- Use effective times, including set-ups and stops, for T0 and r_b.

## Worked example

Invented line: four steps, working day of 10 hours.

| Step | t_i | m_i | Rate (jobs/h) |
|---|---|---|---|
| A | 2 h | 1 | 0.50 |
| B | 3 h | 2 | 0.67 |
| C | 1 h | 1 | 1.00 |
| D | 2 h | 1 | 0.50 |

1. T0 = 2 + 3 + 1 + 2 = 8 h. r_b = 0.5 jobs/h (A and D). W0 = 0.5 × 8 = 4 jobs.
2. Measured: WIP 40 jobs, output 4 jobs a day = 0.4 jobs/h. TPT = 40 ÷ 0.4 = 100 working hours = 10 working days. u = 0.4 ÷ 0.5 = 80%. X-factor = 100 ÷ 8 = 12.5.
3. PWC at 40 jobs: TPT = 8 + 39 ÷ 0.5 = 86 h; TH = 0.5 × 40 ÷ 43 = 0.47 jobs/h. The line is worse than PWC on both.
4. w_PWC for 0.4 jobs/h = 0.4 × 3 ÷ 0.1 = 12 jobs.
5. Target: halve TPT to 50 h → WIP = 0.4 × 50 = 20 jobs. PWC TH at 20 = 0.5 × 20 ÷ 23 = 0.43 jobs/h ≥ 0.4, so a cap of 20 keeps output if the line performs at least as well as PWC.
6. Making step C faster changes nothing at this WIP: it is not the bottleneck, and T0 matters only near W0.

## Status of the formulas

As of 2026-11-25: Little's Law, T0, r_b, W0 and the best, worst and practical-worst-case formulas were checked against Gallego's lecture notes, which present Hopp & Spearman. The Kingman formula was checked against Wikipedia. The availability and stop-pattern rules come from secondary summaries of Hopp & Spearman, ch. 8; treat them as rules of thumb until checked against the book.

## Sources

- Hopp, W. J. and Spearman, M. L.: *Factory Physics*, 3rd ed., Waveland Press, 2008
- Gallego: [IEOR 4000 notes, throughput, WIP and cycle time](https://www.columbia.edu/~gmg2/4000/pdfold/throughput.pdf)
- Little, J. D. C.: [Little's Law as viewed on its 50th anniversary, Operations Research 59(3), 2011](https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf)
- FabTime: [Cycle time tutorial and queueing formulas](https://inficon.com/media/11486/download/FabTimeCycleTimeTutorialAndQueueingFormulasfromFabTimeWebsite.pdf)
- Wikipedia: [Kingman's formula](https://en.wikipedia.org/wiki/Kingman%27s_formula)
- MetricGate: [Factory Physics calculator documentation](https://metricgate.com/docs/hopp-spearman-factory-physics/)
- WSC 2014: [Winter Simulation Conference paper on queueing approximations](https://informs-sim.org/wsc14papers/includes/files/215.pdf)
