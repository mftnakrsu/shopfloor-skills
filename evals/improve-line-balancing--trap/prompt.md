---
description: Catches a takt that subtracts downtime and changeovers and so inflates headcount.
tags: [skill, improve-line-balancing]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---
We are rebalancing our manual pump line. Each shift is 8 hours with 30 minutes of scheduled breaks, so 450 minutes. On average we lose another 45 minutes per shift to breakdowns and changeovers, so I used 405 minutes = 24,300 s. Demand is 900 pumps per shift, so takt = 24,300 / 900 = 27 s. The total work content is 110 s per pump, so 110 / 27 = 4.07, which means 5 operators.

Please confirm the 5 operators and build the yamazumi for them.
