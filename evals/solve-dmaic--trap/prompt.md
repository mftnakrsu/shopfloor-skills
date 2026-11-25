---
description: Refuses to pass a Measure tollgate when the gauge study shows the measurement system is not adequate.
tags: [skill, solve-dmaic]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---
We are at the Measure tollgate of our DMAIC project on seal-groove depth on machined pump housings. About 3.5% of housings are reworked because the groove depth is out of tolerance (2.40 ± 0.05 mm), and that has been the case for a long time.

What we did in Measure:
- Gauge R&R on the depth gauge at the station: 3 operators, 10 parts, 3 repeats each. Result: %GRR = 34% of study variation, number of distinct categories = 3.
- Baseline: 30 subgroups of 5 housings from the last six weeks. The X-bar and R chart shows no signals. Cpk = 0.62.

The team says Measure is complete: Cpk 0.62 is the baseline and we move to Analyze to find the X's. As the sponsor, can I sign off the Measure tollgate today?
