---
title: solve-pdca
description: Runs one PDCA cycle on an A3 - gap with a measured baseline and goal, cause, countermeasure with a written prediction, a small test, a measured check and the act decision.
---

<span class="status available">available</span>

Runs one PDCA cycle (PDCA-Zyklus, Deming-Kreis) on a defined production problem or improvement, written up on an A3 sheet: the gap, the cause, a countermeasure with a written prediction, a small test, a measured check against the prediction and the goal, and the act decision. Choosing the format (point fix, kaizen event or kata) and the 30/60/90 sustain plan stay with [`improve-kaizen`](/skills/improve-kaizen/); this skill runs the cycle.

## Two modes

The skill picks the mode from your request.

| Mode | You give | You get |
|---|---|---|
| Run a cycle | The topic and owner, the metric with its measured baseline, the goal with a date, what is known about the cause, the countermeasure, and for a check the trial facts | A filled A3 and test record: the prediction, the result, the comparison with prediction and goal, a breakdown of what is left, and the act decision |
| Review | An A3, or a request to close, standardise or roll out | Whether each request can be done now, what must come first and in what order, and each failed item with its fix |

Without the baseline, the goal or what is known about the cause, the skill asks for them and stops. It never writes a baseline, goal, cause or countermeasure onto the A3 that you did not give.

## Rules it applies

- A prediction in the goal's metric is written before the test.
- The check counts the result with the baseline method and compares it with both the prediction and the goal; it is never skipped or filled with opinions.
- Act is one of three: adopt and standardise, adapt and run the next cycle, or abandon and go back to the analysis.
- Nothing is standardised, rolled out or closed on a result that was not measured.
- An adopted change gets a new standard, training of every shift and a check of its use with who, how and how often.

## Where the work goes next

Many candidate causes go to [`solve-fishbone`](/skills/solve-fishbone/), a problem not yet scoped to [`solve-is-is-not`](/skills/solve-is-is-not/), and a cause that must be proven first to [`solve-5why`](/skills/solve-5why/). A chronic problem that one cycle cannot crack goes to [`solve-dmaic`](/skills/solve-dmaic/), and a complaint or repeat problem to [`solve-8d`](/skills/solve-8d/). Whether a change is real is checked with [`measure-spc`](/skills/measure-spc/). An adopted change updates [`plan-workstation-instructions`](/skills/plan-workstation-instructions/) and [`plan-control-plan`](/skills/plan-control-plan/). Topics arrive from [`improve-kaizen`](/skills/improve-kaizen/), [`lead-daily-routine`](/skills/lead-daily-routine/), [`lead-gemba-walk`](/skills/lead-gemba-walk/), [`measure-oee`](/skills/measure-oee/) and [`audit-process`](/skills/audit-process/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: plan, check and act, and the A3 sheet, each with its sources.
- `assets/`: an A3 template and a test record.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/solve-pdca).
