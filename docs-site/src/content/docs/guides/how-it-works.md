---
title: How it works
description: The shopfloor-skills hand-off loop - skills that see a problem hand it to skills that fix the cause, and those hand the result to the documents that hold the gain.
tableOfContents: false
---

Each skill does one job and then hands over. A skill's **Hand-offs** section names where the work goes next. Together they form one loop: see the problem, fix the cause, hold the gain.

<div class="figure"><a href="/hand-off-loop.svg" title="Open the diagram at full size"><img src="/hand-off-loop.svg" alt="Three columns. See the problem: lead-daily-routine, measure-spc, measure-oee, lead-gemba-walk, audit-process and improve-vsm. Fix the cause: the solve skills, improve-smed, improve-tpm, improve-kaizen and the flow skills. Hold the gain: plan-control-plan, then plan-workstation-instructions. Arrows show each hand-off." width="1550" height="850" /></a></div>

All 20 skills are available today.

## The hand-offs

| From | When | To |
|---|---|---|
| `lead-daily-routine` | A KPI is red and the cause is unknown | `solve-5why`, `solve-is-is-not`, `solve-fishbone` or `solve-8d` |
| `lead-daily-routine` | A known gap with a cause partly known | `solve-pdca`, for one test cycle |
| `lead-daily-routine` | A chronic red KPI with plenty of data | `solve-dmaic` |
| `lead-daily-routine` | A formal SFM self-audit across areas | `audit-process` |
| `lead-daily-routine` | The OEE KPI is red | `measure-oee`, for the loss tree |
| `lead-daily-routine` | The breakdown KPI is red, or AM tags are overdue | `improve-tpm` |
| `lead-daily-routine` | A line keeps missing the hour-by-hour plan | `improve-line-balancing` |
| `lead-daily-routine` | A quality red comes from an SPC signal | `measure-spc` |
| `lead-daily-routine` | A leader walk or a go-and-see for a red | `lead-gemba-walk` |
| `lead-daily-routine` | A red lead-time KPI spans several processes | `improve-vsm` |
| `measure-spc` | A process is out of control | Escalation in `lead-daily-routine` |
| `measure-spc` | A repeated signal has an unknown cause | `solve-8d` |
| `measure-spc` | Signals from tool wear or after set-ups | `improve-tpm` or `improve-smed` |
| `measure-spc` | A signal with an unknown cause that is not a complaint | `solve-is-is-not`, `solve-fishbone` or `solve-5why` |
| `measure-spc` | The process is stable but not capable | `solve-dmaic` |
| `measure-spc` | A charted characteristic needs its control-plan line | `plan-control-plan` |
| `measure-oee` | The loss tree shows set-up loss | `improve-smed` |
| `measure-oee` | The loss tree shows breakdowns | `improve-tpm` |
| `measure-oee` | The loss tree shows defects | the solve skills |
| `measure-oee` | The bottleneck is known and the problem is the flow | `improve-tpt` |
| `improve-smed`, `improve-tpm` | The change is in | `measure-oee`, to re-measure with the same time model |
| `improve-tpt` | Long set-ups or breakdowns at the bottleneck | `improve-smed` or `improve-tpm` |
| `improve-line-balancing` | Losses were kept out of takt | `measure-oee`, `improve-tpm` or `improve-smed` |
| `solve-8d` | D7 needs a maintenance-plan update | `improve-tpm` |
| `solve-8d` | Containment or a permanent action needs a stability check | `measure-spc` |
| `solve-8d` | D4 needs the causes scoped, listed and drilled down | `solve-is-is-not`, `solve-fishbone`, `solve-5why` |
| `solve-8d` | D7 updates the documents | `plan-control-plan`, `plan-workstation-instructions` |
| `solve-8d` | A chronic remainder after D7 | `solve-dmaic` |
| `solve-fishbone` | The cause list is screened; fishbone widens it, Is/Is-Not narrows it | `solve-is-is-not` |
| `solve-is-is-not` | A verified cause needs its occurrence, detection and system roots | `solve-5why` |
| `solve-5why` | An action's effect must be checked over a cycle | `solve-pdca` |
| `solve-dmaic` | The Control phase | `plan-control-plan`, `plan-workstation-instructions` |
| `lead-gemba-walk` | Findings that need an improvement format | `improve-kaizen` |
| `lead-gemba-walk` | Customer, safety or repeat problems | `solve-8d` |
| `lead-gemba-walk` | Value-stream walk facts | `improve-vsm` |
| `lead-gemba-walk` | An LPA programme, beyond the segment inside one walk | `audit-process` |
| `audit-process` | Findings | the solve skills or `plan-control-plan` |
| `improve-vsm` | The future state needs one part fixed | `improve-tpt`, `improve-kanban-pull` or `improve-line-balancing` |
| `improve-vsm` | A kaizen burst needs an event | `improve-kaizen` |
| `improve-vsm` | A changeover or uptime burst | `improve-smed` or `improve-tpm` |
| `improve-kanban-pull` | Long supplier change-overs or breakdowns | `improve-smed` or `improve-tpm` |
| `improve-kaizen` | A defect's cause must be proven | `solve-8d` or `solve-5why` |
| `improve-kaizen` | A kata or A3 topic; kaizen chooses the format, PDCA runs one cycle | `solve-pdca` |
| `improve-kaizen` | The new standard needs a check | `lead-gemba-walk` |
| the solve skills | The root cause is fixed | `plan-control-plan`, to update it |
| `plan-control-plan` | The control plan changed | `plan-workstation-instructions` |
| `plan-workstation-instructions` | A station check needs a control-plan change | `plan-control-plan` |
| the flow skills | A new standard work exists | `plan-workstation-instructions` |

## Why a loop

A fix that never reaches the control plan and the station instruction is lost at the next shift change. So every path through the loop ends in the documents that the line works from. The daily routine then watches the new standard, and a new red starts the loop again.

## Rules that keep the loop honest

- A skill names only skills that already exist. The linter checks every name, so a hand-off to a planned skill is added in the same change that adds that skill.
- Until then, a skill describes the next step in words. For example, `lead-daily-routine` says to start an 8D outside the meeting and track it on the action list.
