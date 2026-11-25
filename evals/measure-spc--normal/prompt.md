---
description: Sets X-bar and R limits for a turned bore, applies the run rules to today's subgroups and links the signal to the reaction plan.
tags: [skill, measure-spc]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
We want to put the bore diameter on our CNC lathe cell under SPC. Every hour the operator measures 5 consecutive parts. The tolerance is 12.000 ± 0.025 mm.

From 25 hourly subgroups taken last month while the process ran normally, the grand mean is 12.004 mm and the average range is 0.020 mm.

Today's 8 subgroups (mean / range, mm), in time order:

| Subgroup | Mean | Range |
|---|---|---|
| 1 | 12.003 | 0.018 |
| 2 | 12.005 | 0.022 |
| 3 | 12.009 | 0.015 |
| 4 | 12.012 | 0.025 |
| 5 | 12.010 | 0.019 |
| 6 | 12.013 | 0.021 |
| 7 | 12.009 | 0.017 |
| 8 | 12.014 | 0.023 |

The reaction plan in our control plan for this characteristic says: on any SPC signal the operator stops the cell, checks the tool offset and insert wear, measures the parts made since the last subgroup without a signal, and calls the shift lead. If the cause is not found and fixed within 30 minutes, it goes to the tier 2 meeting with quality and process engineering.

Which chart should we use, what are the control limits, and is there anything in today's data we must react to?
