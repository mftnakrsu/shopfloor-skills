---
title: How it works
description: The shopfloor-skills hand-off loop - skills that see a problem hand it to skills that fix the cause, and those hand the result to the documents that hold the gain.
tableOfContents: false
---

Each skill does one job and then hands over. A skill's **Hand-offs** section names where the work goes next. Together they form one loop: see the problem, fix the cause, hold the gain.

<div class="figure"><a href="/hand-off-loop.svg" title="Open the diagram at full size"><img src="/hand-off-loop.svg" alt="Three columns. See the problem: lead-daily-routine, measure-spc, measure-oee, lead-gemba-walk, audit-process and improve-vsm. Fix the cause: the solve skills, improve-smed, improve-tpm, improve-kaizen and the flow skills. Hold the gain: plan-control-plan, then plan-workstation-instructions. Arrows show each hand-off." width="1550" height="850" /></a></div>

Today `lead-daily-routine` and `solve-8d` are available. The other boxes are planned skills, drawn with a dashed border.

## The hand-offs

| From | When | To |
|---|---|---|
| `lead-daily-routine` | A KPI is red and the cause is unknown | `solve-5why`, `solve-fishbone` or `solve-8d` |
| `measure-spc` | A process is out of control | Escalation in `lead-daily-routine` |
| `measure-oee` | The loss tree shows set-up loss | `improve-smed` |
| `measure-oee` | The loss tree shows breakdowns | `improve-tpm` |
| `measure-oee` | The loss tree shows defects | the solve skills |
| `lead-gemba-walk` | Observations | `improve-kaizen` or the solve skills |
| `audit-process` | Findings | the solve skills or `plan-control-plan` |
| `improve-vsm` | The future state needs one part fixed | `improve-tpt`, `improve-kanban-pull` or `improve-line-balancing` |
| the solve skills | The root cause is fixed | `plan-control-plan`, to update it |
| `plan-control-plan` | The control plan changed | `plan-workstation-instructions` |
| the flow skills | A new standard work exists | `plan-workstation-instructions` |

## Why a loop

A fix that never reaches the control plan and the station instruction is lost at the next shift change. So every path through the loop ends in the documents that the line works from. The daily routine then watches the new standard, and a new red starts the loop again.

## Rules that keep the loop honest

- A skill names only skills that already exist. The linter checks every name, so a hand-off to a planned skill is added in the same change that adds that skill.
- Until then, a skill describes the next step in words. For example, `lead-daily-routine` says to start an 8D outside the meeting and track it on the action list.
