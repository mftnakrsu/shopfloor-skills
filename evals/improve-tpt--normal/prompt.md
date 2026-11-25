---
description: Measures throughput time with a Little's Law cross-check, finds critical WIP and sets a WIP cap.
tags: [skill, improve-tpt]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
We machine and assemble valve bodies. Customers say our throughput time (Durchlaufzeit) is too long, and I have to halve it without losing output.

Boundary: from job release at turning to the finished-goods rack. One job is one valve body; all counts below are jobs.

- Routing and average process times per job, including set-ups and stops: turning 30 min, milling 40 min, deburring 20 min, assembly 30 min. One machine or workplace per step.
- We work 2 shifts of 8 hours, 5 days a week, so 16 working hours a day.
- WIP counted at 07:00 on 10 working days between release and the rack: 58, 62, 61, 59, 60, 63, 57, 60, 61, 59 jobs.
- Good output over the same 10 days: 200 jobs, so 20 jobs a day. Customer demand is also 20 jobs a day.
- 30 tagged jobs had release and finish stamps: mean 3.1 working days, slowest 5.4 working days.
- Jobs are released every morning from the ERP plan whenever material is available.
- Milling has unplanned stops of 30 to 90 minutes about twice a week.

Analyse our throughput time and tell me what to change.
