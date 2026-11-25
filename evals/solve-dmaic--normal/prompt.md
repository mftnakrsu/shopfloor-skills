---
description: Reviews an Analyze tollgate on a chronic paint defect, tests the stratified rates and finds what is still missing before Improve.
tags: [skill, solve-dmaic]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
We run a DMAIC project on paint runs (sags) on the topcoat line for washing-machine side panels. The defect has been with us for over a year.

Define: charter signed by the plant manager. Goal: bring the run rate below 2.0% of panels painted within six months.

Measure: an attribute agreement study with 3 inspectors and 50 reference panels gave 96% agreement with the standard, which passes our 90% acceptance limit. Over the last 26 weeks we painted 25,000 panels and found 1,200 with runs. The weekly p chart of the run rate shows all points inside the control limits and no run-rule signals.

Analyze: we split the 26 weeks of data two ways.

By shift:
| Shift | Panels | With runs |
|---|---|---|
| Early | 8,400 | 410 |
| Late | 8,300 | 400 |
| Night | 8,300 | 390 |

By relative humidity in the spray booth at the time of painting:
| Booth humidity | Panels | With runs |
|---|---|---|
| Above 65% RH | 9,000 | 720 |
| 65% RH or below | 16,000 | 480 |

The team says humidity is the root cause and wants to pass the Analyze tollgate today and start Improve by installing booth air conditioning. Is that right? What does the data show, and what is missing?
