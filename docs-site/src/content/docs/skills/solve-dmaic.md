---
title: solve-dmaic
description: Runs DMAIC projects on chronic problems with plenty of data - charter, measurement system check, baseline and capability, tested Xs, a verified pilot and the control handover - and reviews tollgates.
---

<span class="status available">available</span>

Runs DMAIC (Define, Measure, Analyze, Improve, Control) projects on chronic production problems that have plenty of data, and reviews the tollgate (Phasenreview) at the end of each phase. It first checks that DMAIC fits, and routes the problem elsewhere when it does not.

## Two modes

The skill picks the mode from your request.

| Mode | You give | You get |
|---|---|---|
| Run a phase | The problem with its Y and definition, data in time order with the number checked, specification limits, measurement system results, the sponsor, the goal and the cost basis | The phase deliverables: a project charter, a data collection plan, the measurement check, baseline and capability, tested Xs with their effect size, a verified pilot, or the control handover |
| Review a tollgate | The phase's deliverables | Whether the gate can pass, every failed item with its fix, and whether the team must loop back |

Without baseline data, the skill asks for it and stops; a charter may be offered with the problem statement, goal and savings left blank. Without specification limits it computes no capability, and without a measurement system result the Measure tollgate cannot pass.

## Rules it applies

- DMAIC fits a chronic problem with data where cause and solution are unknown; a complaint, a single event or a chart signal goes elsewhere first.
- The measurement system must pass before the baseline is used; a failed study is never back-calculated into a corrected baseline.
- Capability only on a stable baseline with specification limits, roughly normal data and enough values.
- Every claimed X has a test result and a practical size; historical data show association, so each vital X is confirmed with a trial.
- The more Xs are tested, the more likely one passes by chance.
- A gate never passes on a failed measurement system, an unstable baseline or an untested difference.

## Where the work goes next

Candidate Xs are listed with [`solve-fishbone`](/skills/solve-fishbone/), and a problem is stratified with [`solve-is-is-not`](/skills/solve-is-is-not/). Control charts and capability go to [`measure-spc`](/skills/measure-spc/). A single defect inside the project goes to [`solve-5why`](/skills/solve-5why/), and a complaint to [`solve-8d`](/skills/solve-8d/). Control-phase updates go to [`plan-control-plan`](/skills/plan-control-plan/) and [`plan-workstation-instructions`](/skills/plan-workstation-instructions/). Chronic problems arrive from [`lead-daily-routine`](/skills/lead-daily-routine/), [`measure-oee`](/skills/measure-oee/), [`measure-spc`](/skills/measure-spc/), [`solve-8d`](/skills/solve-8d/), [`solve-pdca`](/skills/solve-pdca/), [`improve-kaizen`](/skills/improve-kaizen/) and [`audit-process`](/skills/audit-process/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: tollgates, and statistics (measurement system study, capability, test choice and worked tests), each with its sources.
- `assets/`: a project charter and a tollgate review.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/solve-dmaic).
