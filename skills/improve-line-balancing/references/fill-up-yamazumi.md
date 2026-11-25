# Fill-up yamazumi

How to load operators, merge or split stations, check machines and quantify the savings, with one worked example.

## Element data

1. Break the job into work elements: the smallest steps that could move to another operator.
2. Time each element at the line with a stopwatch over 10 or more cycles; use the lowest repeatable time and record the spread separately (rule of thumb from practitioner research).
3. Separate manual, walking and machine time. Machine time an operator does not wait for is not operator load.
4. Record out-of-cycle work (material fetch, checks every n parts) as time per unit: e.g. 180 s every 25 parts = 7.2 s per unit.
5. Mark each element as value-adding, necessary non-value-adding or waste. Remove the waste first.
6. Balance on observed times, not on standard or planned times.

## Fill-up rule

The operator balance chart aims to minimise operators by loading each to very nearly, but slightly less than, takt (LEI).

1. Take the elements in precedence order.
2. Add elements to operator 1 while the load stays at or below the planned cycle time; for a mix, while every variant's load stays at or below it.
3. Continue with operator 2, and so on.
4. The last operator holds the remainder. Show the gap to takt on the chart as the kaizen target: removing that much work content removes one operator.

Why not equal shares: spreading the remainder evenly makes every operator look busy and hides the waste. Classical line-balancing scores (efficiency against the longest station, smoothness) prefer equal loading; the lean goal prefers fewer operators, each close to takt. This skill follows the lean goal.

## Mix check

- Check each operator's load for each variant, not only the weighted load.
- If one variant overloads an operator on a paced line, move the variant element to an operator with spare time, or level the sequence (for example never two long variants in a row) and check that the average over the repeating sequence fits. The sequence rule is set by local policy.

## Merge or split stations

| Situation | Action |
|---|---|
| Two neighbouring operators together carry less than one planned cycle time | Merge into one station and footprint |
| An operator walks more than they work between stations | Bring stations together (U-shape or shorter line) |
| One element exceeds the planned cycle time on its own | Split the element, add a parallel station, or shorten it |
| One variant overloads a station | Move the variant element, or level the sequence |
| Two high-risk ergonomic elements meet on one operator | Split them across operators |

## Machine check

- Machine cycle per unit = load + unload + automatic time, unless the machine is loaded while it runs.
- Machines needed = machine cycle per unit ÷ takt, rounded up. Every single cycle must fit within takt.
- The process capacity sheet records this per machine, including tool changes (LEI).

## Savings

- Operators saved = (current − new operators per shift) × shifts.
- Units per labour hour = units per day ÷ (operators × shifts × effective hours per shift).
- Also count stations, machines and floor space freed.

## Worked example (invented)

Takt 40 s, planned cycle time 38 s (set by local policy), 2 shifts of 27,600 s effective, 1,380 units per day, one variant. Ten elements in precedence order, walking waste already removed: 9, 12, 10, 7, 11, 15, 12, 14, 6, 8 s = 104 s. Today: 4 operators.

- Operators = 104 ÷ 38 = 2.74 → 3 (fraction above 0.5).
- Fill-up: operator 1 = 9 + 12 + 10 + 7 = 38 s; operator 2 = 11 + 15 + 12 = 38 s; operator 3 = 14 + 6 + 8 = 28 s.
- Gap on operator 3: 38 − 28 = 10 s to the planned cycle time. It is the kaizen target, and it shows where a future takt change can be absorbed.
- Equal shares (35 / 35 / 34 s) would give the same headcount but hide the gap inside every bar.
- Line efficiency = 104 ÷ (3 × 40) = 86.7%; balance loss 13.3%.
- Saved: 1 operator per shift, 2 in total. Units per labour hour: 1,380 ÷ (4 × 2 × 7.67, from 27,600 s ÷ 3,600) = 22.5 → 1,380 ÷ (3 × 2 × 7.67) = 30.0, +33%.

## Sources

- LEI: [Lexicon, operator balance chart](https://www.lean.org/lexicon-terms/operator-balance-chart/)
- LEI: [Lexicon, yamazumi board](https://www.lean.org/lexicon-terms/yamazumi-board/)
- LEI: [Lexicon, standardized work](https://www.lean.org/lexicon-terms/standardized-work/)
- Rother, M., Harris, R.: [Creating Continuous Flow, excerpt (LEI)](https://www.lean.org/wp-content/uploads/2021/01/Creating-continuous-flow-part1.pdf)
- Lecture slides: [Assembly line balancing](https://www.slideshare.net/slideshow/assembly-line-balancing-170054174/170054174)
