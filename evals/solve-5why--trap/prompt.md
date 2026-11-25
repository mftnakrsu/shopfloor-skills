---
description: Catches a 5-Why chain that stops at operator error and ends in retraining.
tags: [skill, solve-5why]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---
Our team did a 5 Why for the swapped coolant hoses on the heater assembly line. Last week 9 units left station 7 with the inlet and outlet hoses fitted the wrong way round.

- Why 1: Why were the hoses swapped? The operator fitted them the wrong way round.
- Why 2: Why did the operator fit them wrongly? He was not paying attention.
- Why 3: Why was he not paying attention? He is careless.
- Root cause: operator error.
- Action: retrain the operator and send a reminder to all shifts.

Please check our 5 Why. If it is fine, we will mark it as done on the tier board.
