---
description: Runs a changeover study from a filmed element list and decides between capacity and smaller lots with EPEI.
tags: [skill, improve-smed]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
We filmed a mould change on injection press 4, from the last good part of the old product to the first good part of the new one, both at full speed. One setter did it alone. The press was stopped for every element:

| Video time (min) | Element |
|---|---|
| 0-14 | Walk to the store, find and fetch the next mould |
| 14-23 | Fetch tools, crane and cart |
| 23-35 | Disconnect water lines, undo 8 clamp bolts, lift out the old mould |
| 35-50 | Lift in and align the new mould, bolt it up |
| 50-55 | Connect the water lines |
| 55-70 | Heat the mould to process temperature |
| 70-90 | Adjust settings, trial shots, wait for quality to approve the first part |

The press runs 4 products. Available time is 7,200 min per week. Weekly demand and cycle times: product A 3,000 pieces at 0.5 min, B 3,000 at 0.5 min, C 2,000 at 0.75 min, D 1,500 at 1.0 min. Each changeover takes about the same 90 minutes. Today we run each product once every two weeks. We need no overtime, deliveries are on time, and finished-goods stock is high.

Do the changeover study: classify the elements, propose the improvements in order, and tell us whether to use the time saved for more capacity or for smaller lots, with the numbers.
