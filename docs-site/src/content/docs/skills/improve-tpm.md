---
title: improve-tpm
description: Runs total productive maintenance on machines and lines - MTBF and MTTR diagnosis, autonomous-maintenance step audits, planned-maintenance basics and OEE loss routing.
---

<span class="status available">available</span>

Runs total productive maintenance (TPM) on machines and lines: computes and interprets MTBF and MTTR, audits autonomous-maintenance (autonome Instandhaltung, Jishu Hozen) steps against exit criteria, sets up planned-maintenance basics, and turns OEE losses into maintenance actions.

## Four modes

The skill picks the mode from your request.

| Mode | You give | You get |
|---|---|---|
| Diagnose breakdowns | The period, planned production time, every failure with its downtime and failure mode, planned maintenance stops, and earlier MTBF and MTTR if known | MTBF, MTTR and availability with the calculation, the trend decision, the downtime split, the top failure modes and an action list |
| Audit an AM step | The step claimed, the tag list, the contamination sources and hard-to-access areas, cleaning time per shift, and the posted standards | Pass or fail in the first lines, each gap with its fix, owner and date, what maintenance must provide, and a re-audit date |
| Set up planned maintenance | The equipment list with criticality, the failure history, the current tasks and spare parts | A maintenance plan with a strategy per item, tasks split between operators and maintenance, and intervals labelled by source |
| Route OEE losses | Loss items in minutes from an OEE loss tree | A table of loss item, minutes, route and next action |

Without the failure count, the time for the period and the downtime of each failure, the skill gives no MTBF or MTTR; it asks for them in one short list and stops. Missing earlier figures do not block a diagnosis, but the trend cannot be judged yet. An AM audit without tag counts or the contamination-source status cannot pass.

## Rules it applies

- Planned maintenance stops are never failures, and MTBF uses operating time, not calendar or planned time.
- MTBF across machines is pooled, never averaged.
- Availability from MTBF and MTTR is operational when MTTR includes waiting; it is inherent only when MTTR is hands-on repair.
- A repeat failure mode needs a root cause and a lasting fix, not only faster repair.
- No AM step passes with an earlier step skipped, and no pass is confirmed that the evidence does not show, even on request.
- AM is not maintenance work handed to production: maintenance support and every task have an owner.

## Where the work goes next

Breakdown, minor-stop and speed losses arrive from [`measure-oee`](/skills/measure-oee/), and OEE is re-measured there after the change. Set-up and adjustment loss goes to [`improve-smed`](/skills/improve-smed/). A failure that caused a complaint or a safety issue goes to [`solve-8d`](/skills/solve-8d/), and missing resources and overdue tags are escalated through [`lead-daily-routine`](/skills/lead-daily-routine/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: MTBF and MTTR, the AM step exit criteria and planned maintenance, each with its sources.
- `assets/`: an AM step audit, a breakdown log and a planned-maintenance plan.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/improve-tpm).
