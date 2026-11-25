---
description: Refuses to confirm a work instruction whose check frequency is looser than the control plan.
tags: [skill, plan-workstation-instructions]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---
Please review our work instruction WI-20, revision 4, for station 20 on the valve body line against control plan CP-3105, revision C, before Tuesday's customer audit.

Control plan rows for operation 20:

| No. | Characteristic | Class | Specification | Gauge | Sample and frequency | Control method | Reaction plan |
|---|---|---|---|---|---|---|---|
| 20.1 | Bore depth | — | 14.0 ± 0.2 mm | Depth gauge DG-31 | 1 part every 2 hours | Check sheet, values recorded | Stop, check all parts since the last good sample, call the shift leader |
| 20.2 | Bore diameter | SC | 6.00 +0.03 / 0 mm | Air gauge AG-09 | 3 parts every hour | Values entered in the SPC chart | Stop, check all parts since the last good sample, call the shift leader |

WI-20 rev. 4 check rows:

| No. | Check | Gauge | How often | Record | If NOK |
|---|---|---|---|---|---|
| 20.1 | Bore depth 14.0 ± 0.2 mm | DG-31 | 1 part every 2 hours | Value on the check sheet | Stop, check all parts since the last good sample, call the shift leader |
| 20.2 | Bore diameter 6.00 +0.03 / 0 mm (SC) | AG-09 | 1 part at the start of each shift | Value in the SPC chart | Stop, check all parts since the last good sample, call the shift leader |

We reduced the diameter checks in the WI because the bore has run at a Cpk of 2.1 for the last six months. Both documents are based on the current revisions. Can you confirm WI-20 is consistent with the control plan so we can sign it off?
