---
title: measure-spc
description: Sets up and reads SPC control charts - chooses the chart, computes the limits with the standard constants, applies the run rules, and links each signal to the reaction plan and tier escalation.
---

<span class="status available">available</span>

Sets up and reads statistical process control (SPC, Statistische Prozessregelung) charts for one product or process characteristic: chooses between X-bar/R, X-bar/S, individuals and moving range, p, np, c and u charts, computes the limits from the process data, applies the Western Electric or Nelson run rules, and links each signal to the reaction plan of the control plan and to tier escalation.

## What you give and what you get

| You give | You get |
|---|---|
| The characteristic, whether it is measured or counted, the subgroup size and frequency, and the data in time order | The chart choice with its reason, the limits with every formula filled in, and the trial or frozen status |
| Chart data to read, with the run rules in force | Whether the process is in control first, then each signal with its rule, chart, subgroup and side |
| The reaction plan and escalation path | The reaction step and escalation route for each signal, or the gap flagged |

Attribute charts need the number inspected in every subgroup; without it the skill asks and stops, and gives no limits. It never names a role, a time limit or a tier for your reaction plan.

## Rules it applies

- Control limits come from the process data and the within-subgroup sigma; tolerance limits never replace them.
- The spread chart is read before the location chart.
- Fewer than 25 subgroups give trial limits, labelled as trial.
- Limits are frozen for monitoring and recomputed only after a confirmed process change.
- Every signal gets a reaction: containment back to the last in-control subgroup, cause, notification and escalation.
- Capability is computed only on a process in control.

## Where the work goes next

A signal not fixed in time, or one that repeats, goes to the board in [`lead-daily-routine`](/skills/lead-daily-routine/) as a quality red. A repeated signal with an unknown cause or a customer link goes to [`solve-8d`](/skills/solve-8d/). Signals from tool wear or machine condition go to [`improve-tpm`](/skills/improve-tpm/), signals after set-ups to [`improve-smed`](/skills/improve-smed/), and scrap from a characteristic out of control feeds the quality loss in [`measure-oee`](/skills/measure-oee/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: chart formulas, run rules, and reaction and escalation, each with its sources.
- `assets/`: an SPC set-up sheet and a reaction plan.
- `scripts/spc_limits.py`: an optional calculator for X-bar/R, I-MR and p-chart limits and the run rules (Python standard library).

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/measure-spc).
