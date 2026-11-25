# Chart formulas

## Contents

- Constants for subgroup charts
- Variable charts: X-bar/R, X-bar/S, individuals and moving range
- Attribute charts: p, np, c, u
- Assumptions and checks
- Capability, only after control
- Standard
- Sources

All limits are ±3 sigma. Sigma is always estimated within subgroups (or from consecutive moving ranges), so that a drifting mean does not widen the limits.

## Constants for subgroup charts

| n | A2 | D3 | D4 | d2 |
|---|---|---|---|---|
| 2 | 1.880 | 0 | 3.267 | 1.128 |
| 3 | 1.023 | 0 | 2.575 | 1.693 |
| 4 | 0.729 | 0 | 2.282 | 2.059 |
| 5 | 0.577 | 0 | 2.115 | 2.326 |
| 6 | 0.483 | 0 | 2.004 | 2.534 |
| 7 | 0.419 | 0.076 | 1.924 | 2.704 |
| 8 | 0.373 | 0.136 | 1.864 | 2.847 |
| 9 | 0.337 | 0.184 | 1.816 | 2.970 |
| 10 | 0.308 | 0.223 | 1.777 | 3.078 |

A2, D3 and D4 from NIST; d2 from the standard factor table (York). A2 = 3 ÷ (d2 √n), so the process sigma is R-bar ÷ d2 and the sigma of a subgroup mean is R-bar ÷ (d2 √n) = A2 × R-bar ÷ 3.

## Variable charts

**X-bar and R** (n from 2 to about 10)

- Centre = grand mean (mean of the subgroup means). UCL, LCL = grand mean ± A2 × R-bar.
- R chart: centre R-bar, UCL = D4 × R-bar, LCL = D3 × R-bar.
- Worked example (invented): n = 3, grand mean 8.00, R-bar 0.30. X-bar limits 8.00 ± 1.023 × 0.30 = 7.693 to 8.307. R chart UCL = 2.575 × 0.30 = 0.773, LCL = 0. Process sigma = 0.30 ÷ 1.693 = 0.177.

**X-bar and S** (n above about 10, or when n varies)

- S chart: centre s-bar; limits s-bar ± 3 (s-bar ÷ c4) √(1 − c4²).
- X-bar chart: grand mean ± 3 s-bar ÷ (c4 √n).
- c4 depends on n; take it from a standard factor table or the calculator in use. Do not reuse the R-chart constants.

**Individuals and moving range** (n = 1)

- MR_i = |x_i − x_(i−1)|; there is one MR fewer than values.
- Individuals: centre = mean of the values; limits = mean ± 3 × MR-bar ÷ 1.128 = mean ± 2.66 × MR-bar.
- MR chart: UCL = 3.267 × MR-bar (D4 for n = 2), LCL = 0.
- Worked example (invented): values 10, 12, 11, 13, 14. Mean 12.0. MRs 2, 1, 2, 1; MR-bar 1.5. Limits 12.0 ± 3.99 = 8.01 to 15.99. MR UCL = 4.90.
- Moving ranges are serially correlated: runs on the MR chart are weak evidence. If a few very large moving ranges inflate MR-bar, check the median moving range as well (Wikipedia, individuals chart).

## Attribute charts

**p chart** (fraction of defective units)

- p-bar = total defectives ÷ total inspected (never the mean of daily percentages when n varies).
- Limits per subgroup: p-bar ± 3 √(p-bar (1 − p-bar) ÷ n_i). Plot p_i = defectives_i ÷ n_i.
- LCL at or below zero: no lower limit.
- A lower limit above zero exists only when n > 9 (1 − p-bar) ÷ p-bar (Wikipedia, p-chart). Example (invented): p-bar 0.02 needs n > 441.
- Worked example (invented): 30 defectives in 1,500 inspected over 10 days, p-bar = 0.02. A day with 150 inspected: 3 √(0.02 × 0.98 ÷ 150) = 0.0343, UCL = 0.0543, no LCL.

**np chart** (count of defective units, constant n)

- Centre n × p-bar; limits n p-bar ± 3 √(n p-bar (1 − p-bar)). Use only when every subgroup has the same n.

**c chart** (defects per constant inspection unit)

- Centre c-bar; limits c-bar ± 3 √c-bar; negative LCL means no lower limit (NIST). With c-bar below 9 there is no lower limit.
- Worked example (invented): c-bar = 16 → UCL = 16 + 12 = 28, LCL = 4.

**u chart** (defects per unit, varying size)

- u_i = defects_i ÷ units_i; u-bar = total defects ÷ total units; limits u-bar ± 3 √(u-bar ÷ n_i).

## Assumptions and checks

- p and np charts assume each unit has the same chance to be defective, units are independent, and the inspection is the same every time (Wikipedia, p-chart). A change of gauge or inspector breaks the chart.
- c and u charts assume defects arrive independently (Poisson, NIST). Clustered defects give too many signals.
- The individuals chart does not need normal data to work as a signal tool (Wikipedia, individuals chart, after Wheeler), but strong skew raises false alarms on one side.
- Autocorrelated data (for example a slow temperature) give runs that are not special causes; sample less often or use a time-series chart.
- Parallel streams (cavities, spindles, nests) are separate processes: chart them separately or by stream.

## Capability, only after control

- Cp = (USL − LSL) ÷ (6 sigma); Cpk = the smaller of (USL − mean) ÷ (3 sigma) and (mean − LSL) ÷ (3 sigma) (NIST).
- Capability compares a process in control with the tolerance (NIST). With open signals, the result describes no single process; fix the signals first.
- Minimum Cpk values are set by the customer or local policy.

## Standard

- ISO 7870-2 (control charts, part 2: Shewhart control charts) covers the Shewhart charts above; its second edition dates from March 2023 (as of November 2026). Full text paywalled and not read; the formulas here follow NIST.

## Sources

- NIST/SEMATECH e-Handbook: [X-bar and R, S charts](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc321.htm); [Individuals charts](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc322.htm); [p charts](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc332.htm); [c charts](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc331.htm); [Process capability](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm)
- ISO: [ISO 7870-2 catalogue entry](https://www.iso.org/standard/78859.html)
- Lawson, J.: [Shewhart control charts in Phase I](https://bookdown.org/lawson/an_introduction_to_acceptance_sampling_and_spc_with_r26/shewhart-control-charts-in-phase-i.html) (25 or more subgroups for trial limits, rule of thumb)
- York: [Factors for control charts (d2)](https://www.york.ac.uk/depts/maths/histstat/tables/controlfactors.pdf)
- Wikipedia: [Shewhart individuals chart](https://en.wikipedia.org/wiki/Shewhart_individuals_control_chart); [p-chart](https://en.wikipedia.org/wiki/P-chart); [u-chart](https://en.wikipedia.org/wiki/U-chart)
