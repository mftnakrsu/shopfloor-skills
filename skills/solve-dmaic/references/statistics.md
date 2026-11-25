# DMAIC statistics

## Contents

- Measurement system study
- Baseline and capability
- Choosing a test
- Test formulas with examples
- Reading a result

All examples use invented round numbers. α (the risk of calling a difference real when it is not) is set by local policy; 0.05 is the usual default (rule of thumb).

## Measurement system study

Run it on the gauge, method and people that will collect the project data, before the baseline.

- %GRR (study variation) = 100 × sigma of the measurement system ÷ total sigma of the study. %GRR of tolerance uses 6 × sigma of the measurement system ÷ (USL − LSL); 6 sigma is the current convention, and older studies use 5.15 sigma.
- Number of distinct categories (ndc) = 1.41 × sigma of the parts ÷ sigma of the measurement system, rounded down (Minitab).
- Acceptance (AIAG guideline, via Minitab): %GRR under 10% acceptable; 10–30% marginal, accepted or not by local policy according to the use and the cost of a better gauge; over 30% not acceptable. ndc at least 5.
- Example: sigma of the measurement system 0.02 mm, total sigma 0.10 mm. %GRR = 20%, marginal. Sigma of the parts = √(0.10² − 0.02²) = 0.098 mm; ndc = 1.41 × 0.098 ÷ 0.02 = 6.9, so 6.
- A failed study makes every later number doubtful: measurement error adds to the observed spread, so capability looks worse than the process is, and good parts are rejected while bad parts are accepted near the limits. Fix the gauge (resolution, fixture, method, training, environment) and repeat the study. A correction computed from the failed study is only an estimate, since the study holds few parts and repeats; it never replaces a new baseline.
- Pass/fail inspection: an agreement study with known good, bad and borderline reference units, each judged more than once by each inspector. Acceptance limit set by local policy.

## Baseline and capability

- Rate for counted Y: defects ÷ units checked over the baseline period, with both counts stated.
- Within sigma from subgroups: R-bar ÷ d2 (d2 = 2.326 for n = 5) or MR-bar ÷ 1.128 for individual values. Overall sigma: the standard deviation of all values.
- Cp = (USL − LSL) ÷ 6σ within. Cpk = min(USL − mean, mean − LSL) ÷ 3σ within. Pp and Ppk use the overall sigma (NIST; JMP).
- On a stable process Cpk and Ppk are close. Ppk well below Cpk suggests the mean moves between subgroups: look at the control chart again.
- Example: tolerance 50 ± 3, mean 50.5, within sigma 0.5, overall sigma 0.8. Cpk = min(2.5, 3.5) ÷ 1.5 = 1.67; Ppk = 2.5 ÷ 2.4 = 1.04. The gap points to drift between subgroups.
- Capability needs a stable process, roughly normal data, and enough values: about 50 or more (NIST). On non-normal data, transform or use a non-normal method before quoting an index.
- Required Cpk levels are set by the customer or by local policy.

## Choosing a test

| Y | X | Question | Test |
|---|---|---|---|
| Pass/fail | Two groups | Do the defect rates differ? | Two-proportion z test; Fisher's exact test when any expected count is under about 5 (rule of thumb) |
| Pass/fail or category counts | Three or more groups | Does the rate or the mix depend on the group? | Chi-square test of independence |
| Measured | Two independent groups | Do the means differ? | Two-sample t test, Welch form |
| Measured | Same units before and after | Did each unit change? | Paired t test on the differences |
| Measured | Three or more groups | Do the means differ? | One-way ANOVA, then compare pairs |
| Measured | Continuous X | Does Y move with X? | Scatter plot and regression |

Small counts: the z test needs reasonably large samples (NIST). If any expected count is under about 5, use Fisher's exact test (rule of thumb).

## Test formulas with examples

**Two proportions.** Pooled p = (x1 + x2) ÷ (n1 + n2). z = (p1 − p2) ÷ √(p (1 − p) (1/n1 + 1/n2)). Significant at α = 0.05 two-sided when |z| > 1.96 (NIST).

Example: supplier A 45 defective of 1,500 (3.0%), supplier B 15 of 1,500 (1.0%). Pooled p = 60 ÷ 3,000 = 0.02. z = 0.02 ÷ √(0.02 × 0.98 × 2 ÷ 1,500) = 0.02 ÷ 0.00511 = 3.9. Significant.

**Two means, Welch.** t = (mean1 − mean2) ÷ √(s1²/n1 + s2²/n2). Degrees of freedom ν = (s1²/n1 + s2²/n2)² ÷ [(s1²/n1)²/(n1 − 1) + (s2²/n2)²/(n2 − 1)]. Significant when |t| > t(0.975, ν) (NIST).

Example: before n = 20, mean 12.0, s = 1.0; after n = 20, mean 11.0, s = 1.0. t = 1.0 ÷ √(0.05 + 0.05) = 3.16; ν = 38; critical value 2.024. Significant.

**Paired.** For each unit d = after − before. t = mean of d ÷ (s of d ÷ √n), with n − 1 degrees of freedom.

Example: 10 units, mean difference 0.5, s of d 0.5. t = 0.5 ÷ (0.5 ÷ 3.162) = 3.16; critical value for 9 degrees of freedom 2.262. Significant.

**Chi-square of independence.** Expected count of a cell = row total × column total ÷ grand total. χ² = Σ (observed − expected)² ÷ expected over all cells, with (rows − 1) × (columns − 1) degrees of freedom (NIST). The test needs expected counts of about 5 or more in each cell (rule of thumb); with smaller counts, merge groups or use an exact test.

Example: three lines with 1,000 units each and 30, 30 and 60 defective. Expected defective 40 per line, expected good 960. χ² = (100 + 100 + 400) ÷ 40 + (100 + 100 + 400) ÷ 960 = 15.0 + 0.63 = 15.6; 2 degrees of freedom, critical value 5.991. The rate depends on the line.

**ANOVA and regression.** Use statistics software; report the F test or the slope with its p-value, and R² for how much of the variation in Y the X explains.

## Reading a result

1. Significant (p ≤ α, or the statistic beyond its critical value): the difference is unlikely to be chance in this data.
2. Not significant: no difference was shown. That is not proof of no difference; the sample may be too small to see it (NIST).
3. Practical size: state the difference in the unit of Y and in money. A significant difference that is small against the gap is not a vital X.
4. Cause: data collected without control show association. Before calling an X a root cause, check what else changed with it and confirm it with an on/off trial or a designed experiment in which X is set deliberately and other factors are held or randomised.
5. Many Xs: the more Xs are tested, the more likely one passes by chance. Confirm a vital X with a trial before acting on it.
6. Assumptions: the t tests need roughly normal values or enough values in each group for the mean to behave normally.
7. Gain: if a vital X were removed, expect Y to move to the level of the group without it (rule of thumb). Compare that with the goal; if it still misses, look for further Xs.

## Sources

- NIST/SEMATECH e-Handbook: [Process capability](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm)
- NIST/SEMATECH e-Handbook: [Hypothesis tests](https://www.itl.nist.gov/div898/handbook/prc/section1/prc13.htm)
- NIST/SEMATECH e-Handbook: [Two-sample t test](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm)
- NIST/SEMATECH e-Handbook: [Critical values of the t distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3672.htm)
- NIST/SEMATECH e-Handbook: [Critical values of the chi-square distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3674.htm)
- NIST/SEMATECH e-Handbook: [Comparing two proportions](https://www.itl.nist.gov/div898/handbook/prc/section3/prc33.htm)
- NIST/SEMATECH e-Handbook: [One-way ANOVA](https://www.itl.nist.gov/div898/handbook/prc/section4/prc43.htm)
- NIST/SEMATECH e-Handbook: [Contingency tables](https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm)
- NIST/SEMATECH e-Handbook: [Gauge R&R studies](https://www.itl.nist.gov/div898/handbook/mpc/section4/mpc4.htm)
- Minitab: [Is my measurement system acceptable?](https://support.minitab.com/en-us/minitab/help-and-how-to/quality-and-process-improvement/measurement-system-analysis/supporting-topics/gage-r-r-and-wheeler-s-emp-studies/is-my-measurement-system-acceptable/)
- Minitab: [Number of distinct categories](https://support.minitab.com/en-us/minitab/help-and-how-to/quality-and-process-improvement/measurement-system-analysis/supporting-topics/gage-r-r-and-wheeler-s-emp-studies/using-the-number-of-distinct-categories-in-a-gage-r-r-study/)
- JMP: [Process capability](https://www.jmp.com/en/statistics-knowledge-portal/quality-and-reliability-methods/process-capability)
- University of York: [Control chart factors (d2)](https://www.york.ac.uk/depts/maths/histstat/tables/controlfactors.pdf)
