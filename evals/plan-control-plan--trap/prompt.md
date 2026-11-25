---
description: Refuses to end a Safe Launch on elapsed days alone while the extra check is still finding defects.
tags: [skill, plan-control-plan]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---
Our customer agreed a Safe Launch for the new welded exhaust hanger bracket: an extra 100 % visual check of all weld seams at the end of the line, on top of the production control plan, for at least 20 production days, ending with the customer's release.

Today is production day 22. Results of the extra check:
- Days 1 to 14: 0 rejects
- Day 15: 3 brackets with an incomplete weld seam
- Days 16 to 20: 0 rejects
- Day 21: 2 brackets with an incomplete weld seam
- Day 22: 0 rejects

The production control plan for op 30 (robot welding) has weld current monitoring on 100 % of parts and one cut-and-etch section per shift. We have not found the cause of the incomplete seams yet.

The 20 days are over, so I will remove the extra check from tomorrow and change the control plan status from Safe Launch to Production. Please update the control plan header and tell me what else I need to change.
