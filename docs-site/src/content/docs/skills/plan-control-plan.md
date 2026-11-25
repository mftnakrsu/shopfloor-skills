---
title: plan-control-plan
description: Builds and reviews process control plans as the master for all station documents - rows from the PFMEA, reaction plans with containment and an owner, error-proofing and gauge-study checks, Safe Launch and review triggers.
---

<span class="status available">available</span>

Builds and reviews process control plans (Produktionslenkungsplan, PLP) as the master document for every station document. It turns PFMEA controls and special characteristics into rows, gives every row a reaction plan, and sets the triggers for the next review.

## Two modes

The skill picks the mode from your request.

| Mode | You give | You get |
|---|---|---|
| Build | The part or family, phase and customer requirements, the process flow, the PFMEA extract, the specifications, gauges with their study status, error-proofing devices, set-up rules and your reaction rule | A header and one row per characteristic and operation, with specification, gauge, sample size, frequency, control method, record and its own reaction plan, the open gaps with owners, and the review triggers |
| Review | The current plan with its revision history and the changes, complaints or shipped nonconforming product since the last revision | Whether the plan can be released or kept, then each gap with the row, what is missing and the fix |

Without a PFMEA (or a characteristic list) and the specifications, the skill asks for both and stops. It never fills a tolerance, sample size or frequency for you, and without a local reaction rule it writes "set by local policy" instead of naming a role or a time limit.

## Rules it applies

- One row per characteristic at one operation; product and process characteristics are kept apart.
- Every row has a reaction plan: stop or hold, contain back to the last good check, restore and verify, escalate, record, with an owner by role.
- The parts at risk are the output rate times the interval between checks; that is what the reaction must contain.
- Each error-proofing device has its own check with a master or challenge part and a frequency; a failed device makes its output since the last good check suspect.
- Every gauge, attribute and visual checks included, needs a passed measurement system study; a missing study on a special characteristic blocks that row.
- Safe Launch is a temporary layer on top of the plan and ends only on evidence and the customer's release, never on the calendar.
- A change, a complaint or shipped nonconforming product without a new revision is a finding.

## Where the work goes next

Station inspection and work instructions are derived from the rows with [`plan-workstation-instructions`](/skills/plan-workstation-instructions/). Chart choice and limits for a row go to [`measure-spc`](/skills/measure-spc/). A complaint or shipped nonconforming product goes to [`solve-8d`](/skills/solve-8d/); a Safe Launch escape that needs no full 8D goes to [`solve-5why`](/skills/solve-5why/) or [`solve-fishbone`](/skills/solve-fishbone/). Error-proofing and maintenance-related controls go to [`improve-tpm`](/skills/improve-tpm/), the daily review of alternate controls to [`lead-daily-routine`](/skills/lead-daily-routine/), and an effectiveness check by process audit to [`audit-process`](/skills/audit-process/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: columns and rows, reaction plans, and plan variants with review triggers, each with its sources.
- `assets/`: a control-plan template and a Safe Launch plan.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/plan-control-plan).
