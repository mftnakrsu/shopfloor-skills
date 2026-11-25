---
title: solve-5why
description: Builds and reviews 5-Why chains for occurrence, detection and system causes, with an evidence check on every link, stop rules and one action per root cause.
---

<span class="status available">available</span>

Builds and reviews 5-Why chains (5-Why-Methode, Warum-Warum-Analyse) for a defined production or quality problem: one chain for why it occurred, one for why it was not detected, and one for why the system allowed it.

## Two modes

The skill picks the mode from your request.

| Mode | You give | You get |
|---|---|---|
| Build | The problem facts (what, where, when, how many, how found), the process flow with its controls, and what has been checked so far | A problem statement, the three legs as tables with the evidence and status of every link, the root causes, one action per root cause, the open checks and the documents to update |
| Review | An existing 5-Why | Whether it can be accepted, then every failed item with what is missing and the fix |

Without the problem facts, the skill asks for them in one short list and stops. A broad problem (a trend with no defect type) is broken down first. With facts but no evidence, the first whys are given only as hypotheses, each with the check that would confirm it.

## Rules it applies

- The problem statement is factual and quantified, and holds no cause and no solution.
- Every link is marked verified, hypothesis or rejected; a root cause rests only on verified links, and for the occurrence leg preferably on an on/off test.
- A chain stops only at a changeable condition that passes the counterfactual and the "therefore" test. It never stops at a person, at "no time" or at a supplier without its own chain.
- The number of whys is not fixed.
- Each root cause gets its own action, from the strongest level that is feasible; retraining or a reminder is never the action on its own.

## Where the work goes next

Many candidate causes go to [`solve-fishbone`](/skills/solve-fishbone/), and a problem whose where and when are unclear to [`solve-is-is-not`](/skills/solve-is-is-not/). A customer complaint, safety topic or repeat problem goes to [`solve-8d`](/skills/solve-8d/). Document updates go to [`plan-control-plan`](/skills/plan-control-plan/) and [`plan-workstation-instructions`](/skills/plan-workstation-instructions/), and checking an action's effect over a cycle to [`solve-pdca`](/skills/solve-pdca/). A chronic problem with plenty of data goes to [`solve-dmaic`](/skills/solve-dmaic/). Problems arrive from [`lead-daily-routine`](/skills/lead-daily-routine/), [`measure-spc`](/skills/measure-spc/), [`measure-oee`](/skills/measure-oee/), [`lead-gemba-walk`](/skills/lead-gemba-walk/) and [`audit-process`](/skills/audit-process/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: the three legs, and evidence and stop rules, each with its sources.
- `assets/`: a 5-Why worksheet.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/solve-5why).
