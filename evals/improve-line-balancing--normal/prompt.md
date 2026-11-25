---
description: Rebalances a manual assembly line with mix, ergonomics and a shared test rig from full data.
tags: [skill, improve-line-balancing]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
Please rebalance our manual assembly line for gearbox covers.

- Demand: shipments over the last 12 months averaged 1,800 units per day and are stable. We run 2 shifts of 8 hours, each with two 15-minute breaks.
- Mix: variant A is 80% of units, variant B 20%. B needs one extra element (fit heat shield, 10 s).
- Local policy: plan each operator to at most 28 s per unit.
- Work elements in the only possible order, with observed repeatable times (lowest of 10 cycles):
  1. Lift housing from pallet into fixture, 8 s
  2. Insert bearing, 10 s
  3. Press shaft, 10 s
  4. Fit seal, 12 s
  5. Fit cover, 9 s
  6. Place 4 screws, 7 s
  7. Drive 4 screws, 14 s
  8. Connect harness, 8 s
  9. Label, 6 s
  10. (B only) Fit heat shield, 10 s
  11. Load, unload and start the function test rig, 10 s (the rig then tests automatically for 15 s)
  12. Pack, 6 s
- Today: 5 stations, 5 operators per shift. Station 5 has two identical test rigs used alternately.
- Ergonomics: our ergonomist found a lifting index of 1.6 for element 1 (housings come on a floor-level pallet) and a RULA score of 5 for element 7.

Give the takt, the number of operators, the new yamazumi, the savings and the standard work we need.
