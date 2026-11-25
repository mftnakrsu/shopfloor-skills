---
description: Asks for the number of units inspected per day before building a chart for defective counts.
tags: [skill, measure-spc]
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill]
---
Can you set up a control chart with limits for our helium leak test on the heat-exchanger line? These are the leaking units we found on each of the last 20 working days:

7, 4, 9, 6, 5, 11, 3, 8, 6, 7, 10, 5, 4, 6, 9, 7, 5, 8, 12, 6

Output varies a lot from day to day because of the schedule. We want the chart on the board at the line from Monday.
