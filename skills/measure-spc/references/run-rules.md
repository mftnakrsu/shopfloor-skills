# Run rules

Which patterns count as signals, what they usually mean on the shop floor, and what each extra rule costs in false alarms.

## Zones

- Zone A: between 2 and 3 sigma from the centre line. Zone B: between 1 and 2 sigma. Zone C: within 1 sigma. Each side is counted separately.
- Sigma here is the sigma of the plotted statistic: A2 × R-bar ÷ 3 for subgroup means, MR-bar ÷ 1.128 for individuals.
- A point exactly on a zone line counts as inside the zone nearer the centre (rule of thumb; agree it locally and keep it fixed).

## Western Electric rules (NIST)

NIST lists the four zone rules (1 to 4) together with two pattern rules for trends and alternation. The skill's default set is rules 1 to 4; the two pattern rules are optional, set by local policy.

| Rule | Pattern | Typical shop-floor meaning |
|---|---|---|
| 1 | One point beyond 3 sigma | A single upset: wrong setting, damaged tool, measuring error, mixed material |
| 2 | Two of three consecutive points beyond 2 sigma, same side | A sizeable shift in the mean |
| 3 | Four of five consecutive points beyond 1 sigma, same side | A smaller, lasting shift |
| 4 | Eight consecutive points on one side of the centre line | A lasting shift: new lot, offset change, a different operator method |
| Trend | Six points in a row rising or falling | Tool wear, heating up, a slowly loading filter |
| Alternating | Fourteen points in a row alternating up and down | Two streams mixed (two machines, two gauges) or over-adjustment |

## Nelson rules (Nelson 1984)

Nelson's eight rules also contain rules 1 to 3 and the trend and alternating rules (as his rules 3 and 4), and differ in three places:

- Nine points in a row on one side (instead of eight).
- Fifteen points in a row within 1 sigma, either side: spread smaller than the limits imply. Check for limits computed from mixed streams, or a gauge with too coarse a resolution.
- Eight points in a row with none within 1 sigma, both sides: mixture of two levels.

Use one named set and write it on the chart. Do not switch sets after looking at the data (Wikipedia, control chart).

## False alarms

- With rule 1 only, a process in control gives a false signal about once every 371 points on average (NIST).
- With the Western Electric rules added, about once every 92 points (NIST).
- More rules find small shifts sooner but cost more stops for nothing. Some plants react to rule 1 at once and treat the other rules as a call to watch and check first (NIST). Which rules trigger which reaction is set by local policy and written in the reaction plan.

## Reading order

1. Spread chart first (R, S or MR). An out-of-control spread makes the location limits invalid.
2. Location chart (X-bar or individuals): rule 1, then the zone rules, then runs and trends.
3. For each signal, record the rule, the chart, the first subgroup where it fires, and the side.
4. Count a lasting pattern once, from the subgroup where it first fires; points after it belong to the same signal until the cause is fixed. Each point beyond a limit is its own signal.

## Worked example (invented)

X-bar chart with centre 30.0 and 1 sigma 0.2, so zone lines at 30.2, 30.4 and 30.6 above the centre. Means in order: 30.1, 30.3, 30.5, 30.2, 30.5, 30.3.

- Rule 1: no point above 30.6.
- Rule 2: points 3 and 5 are above 30.4, within the three points 3 to 5: signal at point 5, high side.
- Rule 3: points 2 to 6 are all above 30.2 except point 4, which is on the line and counts as inside: four of five above, signal at point 6, high side.
- Rule 4: only six points on one side: no signal yet.

## Sources

- NIST/SEMATECH e-Handbook: [What are variables control charts? (Western Electric rules, false alarm rates)](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc32.htm); [What are control charts?](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm)
- Wikipedia: [Nelson rules](https://en.wikipedia.org/wiki/Nelson_rules) (Nelson, L. S., Journal of Quality Technology 16(4), 1984); [Control chart](https://en.wikipedia.org/wiki/Control_chart)
