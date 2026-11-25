---
description: Catches a plant OEE averaged across machines with very different planned times.
tags: [skill, measure-oee]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---
For the monthly report, our plant OEE for last week is 76.7%. We take the average of our three presses:

| Press | OEE | Planned production time |
|---|---|---|
| Press 1 | 80% | 900 min |
| Press 2 | 60% | 900 min |
| Press 3 | 90% | 120 min |

Press 2 is our bottleneck. Can you check the number before it goes to management?
