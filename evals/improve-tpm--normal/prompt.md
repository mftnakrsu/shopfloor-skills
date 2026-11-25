---
description: Diagnoses a breakdown loss with MTBF and MTTR and sets planned-maintenance actions.
tags: [skill, improve-tpm]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
Our OEE loss tree for October puts breakdowns on press P4 as the biggest availability loss. Data for October:

- Planned production time: 500 h.
- 10 breakdowns, total downtime 40 h from stop to restart. Of those 40 h: 20 h hands-on repair, 14 h waiting for spare parts, 6 h waiting for a technician.
- 6 of the 10 breakdowns were a leaking hydraulic hose at the same clamp; the other 4 were different electrical faults.
- 2 planned preventive-maintenance stops of 5 h each, also inside the planned production time.
- Last quarter's figures for P4, measured the same way: MTBF 46 h, MTTR 2 h.

Work out MTBF and MTTR for October, tell me what the change means, and tell me what maintenance actions to take.
