---
description: Writes graded, clause-mapped findings from complete manufacturing process audit notes.
tags: [skill, audit-process]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
I am an internal auditor in the quality department and on our list of qualified process auditors. Yesterday, 24 November 2026, I did the annual IATF 16949 manufacturing process audit of the robot welding cell that makes seat brackets. I audited the early shift and the late shift and sat in on the handover between them. The cell belongs to production; I have no role in it. Audit criteria: control plan CP-WB-14 rev. F, PFMEA rev. D and the cell's work instruction WI-WB-03 rev. C.

My notes:
1. The control plan asks for one cut-and-etch weld penetration test per shift. The early shift's tests are all recorded. On the late shift the last recorded test is from three days ago.
2. Robot 2's wire feed was set to 9.6 m/min. WI-WB-03 allows 8.0 to 9.0 m/min. There is no approved deviation. The setter said it "welds better" since the new wire batch.
3. The fillet weld gauge at the station is labelled "calibration due 31 August 2026". There is no other gauge at the cell.
4. The PFMEA lists weld spatter on the thread as a failure mode with "100% visual check at the cell" as its detection control. The control plan and the work instruction have no such check.
5. The handover sheet was blank on two of the last five days. During the handover I watched, the nozzle change on robot 1 was not passed on.
6. The part-presence sensor is checked at every shift start with the red challenge part. The records for the last month are complete.

Please write up the findings with the ISO 9001 and IATF 16949 clauses, grade them, and give me the follow-up.
