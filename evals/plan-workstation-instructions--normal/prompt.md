---
description: Drafts the work and inspection instruction for one station from three control-plan rows.
tags: [skill, plan-workstation-instructions]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
Please draft the work and inspection instruction for station 40 on our water pump cover line. Source is control plan CP-2210, revision D, dated 3 November, part 77-410, operation 40 "press bushing and fit retaining clip". These are all the control-plan rows for operation 40:

| No. | Characteristic | Class | Specification | Gauge / method | Sample and frequency | Control method | Reaction plan |
|---|---|---|---|---|---|---|---|
| 40.1 | Bushing press depth (product) | SC | 3.20 ± 0.08 mm | Digital depth gauge DG-117 (MSA study MS-55, QMP 17 %, calibration due next 30 June) | 5 parts every 2 hours, and the first 5 parts after every set-up | X-bar/R chart | Stop the press, hold all parts made since the last good subgroup, measure them 100 %, call the shift leader |
| 40.2 | Press force at end position (process) | — | 1.8 to 2.6 kN | Force monitor on the press | Every part | Automatic NOK reject into the locked red bin | More than 3 rejects in one hour: stop and call the process engineer |
| 40.3 | Retaining clip present (product) | — | Clip present | Inductive sensor with press interlock (error-proofing) | Check the sensor with challenge part RP-40 at the start of every shift | Error-proofing check sheet | Sensor misses RP-40: stop, quarantine all parts since the last successful check, call maintenance and the shift leader |

Operators wear safety glasses and cut-resistant gloves at this press. The team on this line speaks German and Romanian.
