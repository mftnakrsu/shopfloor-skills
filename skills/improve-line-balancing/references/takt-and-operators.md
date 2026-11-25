# Takt and operators

Formulas for volume, mix, takt and operator count, with the rounding rule for a fractional operator.

## Effective time

- Effective time per shift = start-to-stop shift time − scheduled operator breaks, meetings and cleanup (Rother & Harris).
- Do not subtract unplanned machine downtime, changeovers or other internal problems. Takt must represent the customer's demand rate; losses are a capacity problem to fix, not part of takt (Rother & Harris).
- A secondary teaching source subtracts maintenance, downtime and changeovers too. This skill follows Rother & Harris, because subtracting losses shortens takt and so adds operators to pay for the losses.

## Demand

- Use actual shipments, not orders, over about the past 12 months. Check the range of daily demand (Rother & Harris).
- Run a steady takt on long-term average demand. Cover occasional spikes with a finished-goods buffer or overtime. Changing takt from day to day is inefficient and disrupts the work pace (Rother & Harris).
- Demand per shift = demand per day ÷ shifts operated per day, or per week ÷ shifts per week.
- Uncertain future demand: add capacity in steps as demand appears (Rother & Harris).

## Takt

Takt = effective time per shift ÷ demand per shift, in seconds per unit (LEI; Rother & Harris).

Example (invented): 480 min − 20 min breaks = 460 min = 27,600 s. Weekly demand 6,900 over 10 shifts = 690 per shift. Takt = 27,600 ÷ 690 = 40 s.

- Takt is a choice: demand is fixed, but shifts, shift length, end items per cell and number of cells can change. A 40 s takt over two shifts equals a 20 s takt in one shift (Rother & Harris).
- Below about 10 s, jobs become highly repetitive and stressful: consider several cells. Above about 120 s, work becomes hard to standardise: consider adding similar end items (Rother & Harris).
- Three-shift operations need a cycle time slightly below takt, because there is no time to catch up. Cycling chronically much faster than takt risks overproduction and extra operators and hides problems (Rother & Harris).
- Planned cycle time: the load limit per operator below takt, for example to absorb small disturbances. Its value is set by local policy; no public primary source gives a standard ratio.

## Mix

- Weighted work content = Σ (share of variant × work content of variant).
- Example (invented): variant X 60% at 90 s, variant Y 40% at 110 s: 0.6 × 90 + 0.4 × 110 = 98 s.
- Work content should not vary by more than about 30% between end items in one cell, especially on a moving conveyor; otherwise split the cell or move rare items elsewhere (Rother & Harris).
- Mixed-model lines can use a compound takt (Shook).

## Operator count

Theoretical operators = weighted work content ÷ planned cycle time (or takt) (Gemba Academy; LEI).

Example (invented): 97 s ÷ 38.6 s = 2.5 → the fraction rule decides between 2 and 3.

### Fractional operator (rule of thumb)

The practitioner rule below assumes operators are loaded to about 90–95% (HashLLP). The rule is often attributed to Rother & Harris; that attribution could not be checked in a public text, so treat it as a rule of thumb.

| Fraction | Action |
|---|---|
| Below 0.3 | Do not add an operator. Remove waste and incidental work so the work fits the lower count. |
| 0.3 to 0.5 | Do not add an operator yet. Start with the higher count if output must be safe, load by fill-up, and review after about two weeks of operation and kaizen. |
| Above 0.5 | Add the operator if needed, and keep removing waste so the extra person is eventually not needed. |

## Line metrics

- Line efficiency = Σ element times ÷ (operators × takt). Balance loss (balance delay) = 1 − efficiency (classical line balancing).
- Example (invented): 150 s ÷ (4 × 40 s) = 93.75%; balance loss 6.25%.
- Classical metrics reward equal loading; the lean goal rewards fewer operators each loaded close to takt. Report both, decide by operator count.

## Sources

- Rother, M., Harris, R.: [Creating Continuous Flow, excerpt (LEI)](https://www.lean.org/wp-content/uploads/2021/01/Creating-continuous-flow-part1.pdf)
- LEI: [Lexicon, takt time](https://www.lean.org/lexicon-terms/takt-time/)
- LEI: [Lexicon, operator balance chart](https://www.lean.org/lexicon-terms/operator-balance-chart/)
- Shook, J.: [Misunderstandings about value stream mapping, flow analysis and takt time (LEI)](https://www.lean.org/the-lean-post/articles/misunderstandings-about-value-stream-mapping-flow-analysis-and-takt-time)
- Gemba Academy: [Crew size calculation](https://blog.gembaacademy.com/?p=541)
- HashLLP: [Steps to calculate the number of operators required for a cell](https://www.hashllp.com/steps-to-calculate-operators-required/)
- MyEducator: [Takt time chapter (secondary teaching source)](https://app.myeducator.com/reader/web/1716c/chapter06/wg1v6)
- Lecture slides: [Assembly line balancing](https://www.slideshare.net/slideshow/assembly-line-balancing-170054174/170054174)
