---
description: Computes OEE and TEEP for one press day and builds the loss tree in minutes.
tags: [skill, measure-oee]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
Please calculate OEE and TEEP for injection press 4 for yesterday and tell us where to focus.

- The press runs 2 shifts of 8 hours; the night shift is not staffed. Each shift has 30 minutes of planned breaks.
- Our stop rule: any stop of 5 minutes or longer is logged with a reason. Yesterday's log: changeover from product A to product B 60 min, hydraulic pump breakdown 45 min, waiting for material 15 min.
- Short stops under 5 minutes added up to 30 min, from the counter on the machine.
- Product A: ideal cycle time 30 s, 600 parts made, 20 scrapped.
- Product B: ideal cycle time 20 s, 1,200 parts made, 30 scrapped, and 30 more reworked at the bench and then passed.
