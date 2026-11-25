---
description: Builds production control-plan rows from a process flow and PFMEA extract, with reaction plans, error-proofing checks and a gauge-study gap.
tags: [skill, plan-control-plan]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
Please build the production control plan for our machined aluminium pump cover (one part number, phase: production), including the reaction plans. Here is what we have.

Process flow: 10 receive castings, 20 mill sealing face (CNC-2), 30 drill and tap 4 × M6 (CNC-3), 40 wash, 50 leak test (LT-1), 60 pack.

PFMEA extract (the rows that need a control):

| Op | Characteristic | Specification | Class | Prevention control | Detection control |
|---|---|---|---|---|---|
| 20 | Sealing face flatness (product) | ≤ 0.04 mm | SC (customer special characteristic) | Tool-life counter, insert change every 400 parts | Flatness gauge FG-07, 1 part every 2 hours, value recorded |
| 20 | Coolant concentration (process) | 6 to 8 % | – | – | Refractometer, once per shift |
| 30 | Thread present and full depth, 4 × M6 (product) | Go/no-go thread gauge | – | Tap breakage monitor on the spindle stops the machine; checked at shift start with a master part that has one untapped hole | Thread gauge, 5 parts per shift |
| 40 | Bath temperature (process) | 60 ± 5 °C | – | – | Thermometer reading every 4 hours |
| 40 | Residual dirt (product) | ≤ 3 mg per part | – | – | Gravimetric lab test, 1 part per week |
| 50 | Leak rate (product) | ≤ 2.0 cm³/min at 1.5 bar | SC | – | Leak tester 100 %; NOK parts are locked into a red box automatically; checked at shift start with leak master LM-2 |

Set-up: after every set-up and every insert change, the first part is measured on the CMM and released before production continues.

Gauges: the thread gauges, LT-1 and the lab method have passed their gauge studies. No gauge study has been done for FG-07 yet.

Our plant reaction rule: stop the machine, block all parts back to the last good check, call the shift lead; if it is not fixed within 1 hour, escalate to the quality engineer. If an error-proofing device fails its shift-start check: stop, block all parts made since its last successful check, and use an alternative check only with quality approval.
