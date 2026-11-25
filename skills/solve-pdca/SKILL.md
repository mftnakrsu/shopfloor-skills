---
name: solve-pdca
description: >-
  Runs one PDCA (plan, do, check, act) cycle on a defined production problem
  or improvement, written up on an A3 sheet: gap with measured baseline and
  target, cause analysis, countermeasure with a written prediction, a small
  test, a measured check against the prediction and the target, and the act
  decision to adopt and standardise, adapt and run the next cycle, or
  abandon. Use when an A3 must be written, reviewed or updated; when a
  trial or countermeasure must be checked before it is standardised, rolled
  out or closed; when the next PDCA cycle must be planned; or when SDCA and
  PDCA must be told apart (PDCA-Zyklus, Deming-Kreis, A3-Bericht,
  A3-Report, Problemlösungsblatt, Wirksamkeitsprüfung, Maßnahmenverfolgung,
  Standardisierung, SDCA).
license: MIT
metadata:
  version: "1.0.0"
  category: solve
  standards: "ISO 9001 0.3.2, 10.2.1, 10.3; IATF 16949 10.3.1"
---
# PDCA cycle on an A3

## Conventions

- One cycle (PDCA-Zyklus, Deming-Kreis) is one test of one countermeasure (Gegenmaßnahme): Plan, Do, Check, Act. A topic usually needs several cycles; each starts from what the last one taught. SDCA (standardise, do, check, act) holds a standard; PDCA raises it (Imai, via secondary sources). A cycle starts from a standard that is followed and ends in a new one.
- Plan holds the gap, the cause and a **prediction** (Vorhersage): the result the team expects, in the metric of the goal, written before Do. Check (also "Study") compares the measured result with that prediction and with the goal (Moen and Norman; Wikipedia).
- Act has three outcomes: **adopt** (goal met: standardise), **adapt** (partly met: change the countermeasure and run the next cycle), **abandon** (no effect or harm: back to the analysis) (Deming 1993, via Moen and Norman).
- The A3 (A3-Bericht) is one sheet, owner and date at the top, read left to right: background, current condition, goal, analysis on the left; countermeasures, plan, check, follow-up on the right (Shook). The layout is flexible; the logic is fixed.
- ISO 9001 0.3.2 describes processes and the management system run as a PDCA cycle; 10.2.1 asks that the effect of a corrective action is reviewed; 10.3 and IATF 16949 10.3.1 ask for continual improvement with a method and an effectiveness check. This skill gives one cycle its working steps. Choosing between point fix, event and kata is `improve-kaizen`; the 30/60/90 sustain plan stays there.

## Inputs

- The topic and its owner; who reviews the A3 (manager or mentor).
- The metric, its measured baseline (value, how counted, period, shifts) and the goal with a date, and who set it.
- The current standard (work instruction (Arbeitsanweisung), standard work (Standardarbeit), setting) and whether it is followed.
- What is known about the cause and how it was proven, or the data to analyse.
- The countermeasure, if chosen; for a check, the trial facts: where, how long, how many, the result measured with the baseline method, and what else changed.
- Limits the change must respect: safety, quality, output, cycle time against takt time (Taktzeit), cost.

Ask for every missing input; never invent one. Copy the user's numbers exactly.

- Without the baseline, the goal or what is known about the cause, ask for them in one short list (metric and how it is counted, current value over which period, goal and date and who sets it, what is known about the cause and what was tried, the current standard) and stop. At most give the blank `assets/a3-template.md`. Never write a baseline, goal, cause or countermeasure onto the A3 that the user did not give.
- A missing reviewer or limit does not block the Plan; write "to be confirmed" and list it as an open question.

## Procedure

1. **State the gap.** Background in one or two lines (why it matters). Current condition with the measured baseline. Goal with a value and a date. A solution is not a gap: if the topic starts from a solution, ask which metric it must move.
2. **Check the standard.** If no standard exists or it is not followed, first write down today's best method and get it followed (SDCA); then measure the baseline against it.
3. **Analyse the cause.** Use the simplest tool that shows cause and effect (Shook): a breakdown by type, place, shift or time, then a why-chain. A cause counts as proven only by an on/off test or a data comparison; otherwise it is a hypothesis and the first cycle tests it.
4. **Choose the countermeasure.** Each one acts on a named cause. Test one change per cycle where possible (rule of thumb), so the effect can be traced to it.
5. **Write the prediction and the test plan** before Do, with `assets/test-record.md`:
   - Prediction: the expected value of the goal metric, and any expected side effect.
   - Test: where, who, start and end, how many units, how the result is counted (the same method as the baseline). Start small (one line, one cell), preferably on a small scale (Deming, via Moen and Norman). Cover every shift and the normal product mix; the length is set by local policy.
   - The success criterion, in numbers, agreed with the reviewer.
6. **Do.** Run the test as planned. Record deviations from the plan, problems and unexpected observations as they happen. Change nothing else in the test area, or record it.
7. **Check.** Never skip it, and never fill it with opinions. Details in [plan, check, act](references/plan-check-act.md).
   - Was the test run as planned? Was the result counted with the baseline method over the planned period?
   - Rate = defects ÷ units × 100%. Change = (result − baseline) ÷ baseline × 100%. Gap closed = (baseline − result) ÷ (baseline − goal) × 100%.
   - Compare the result with the prediction and with the goal. A miss of the prediction means the cause or the countermeasure is not fully understood; say so.
   - Break down what is left (by type, place, shift): a cluster points at an uncovered cause.
   - Check the limits: safety, quality, cycle time against takt time, cost.
   - Whether the change is real or noise: compare with the normal spread of the baseline; for a measured characteristic, use a control chart.
8. **Act.** Choose one:

   | Check shows | Act |
   |---|---|
   | Goal met, result close to the prediction, no harmful side effect | Adopt (einführen): write the new standard, train every shift, set the check that it is used, then roll out to similar areas |
   | Goal met, but far better than predicted | Confirm first: look for another change in the area, then repeat or extend the test before adopting; the theory is incomplete |
   | Better than baseline, goal not met (whether or not the prediction was met), no harmful side effect | Adapt (anpassen): keep the countermeasure running as an interim measure under the test controls; aim the next cycle at the remaining cause, with a new prediction and test plan (step 5) |
   | No effect, or a harmful side effect | Abandon (verwerfen): undo the change; go back to the analysis, because the cause was probably wrong |

   - Goal met but the result fell short of the prediction: adopt, and record that the theory is incomplete.
   - Never standardise, roll out or close on a result that was not measured.
   - Roll-out is its own small check: confirm the result on the first similar area before the rest.
9. **Hold the gain and close.** The new standard names the document, its owner and its release date; the old version is withdrawn. The check that it is used names the role, the method (leader standard work, a layered process audit (Prozessaudit) item or a gemba-walk item) and a frequency to confirm against local policy. Close the A3 only when the goal is met in a measured check and the standard is released and checked. Record the learning in the follow-up box and share it.

Example (invented): mispicks at a kitting rack. Baseline 40 per 10,000 picks over 4 weeks, both shifts; goal 10 per 10,000. Cause: two look-alike bins (hypothesis, backed by 70% of mispicks between two look-alike bins). Countermeasure: a light that shows the bin to pick. Prediction: at most 10 per 10,000. Trial: 5,000 picks, 15 mispicks.

| Check | Value |
|---|---|
| Rate | 15 ÷ 5,000 = 30 per 10,000 |
| Change | (30 − 40) ÷ 40 = −25% |
| Gap closed | (40 − 30) ÷ (40 − 10) = 33% |
| Against prediction and goal | Missed both |
| What is left | 12 of 15 on the late shift, where the record shows the light was off for part of the test |
| Act | Adapt: keep the light running as an interim measure under the test controls; aim the next cycle at why it was off on the late shift, with a new prediction and test plan |

### Review an A3, or a request to close, standardise or roll out

1. Run the Validation checks against the A3 as given.
2. Say plainly whether each thing the user asks to do (close, standardise, roll out) can be done now. If not, say what must come first and in what order: measure, compare with the prediction and the goal, decide, then standardise, then roll out area by area.
3. List each failed item with the fix. Never write a check result or an act decision the data does not support.

## Validation

Check before answering:

1. The gap has a measured baseline and a goal with a date, or they are asked for.
2. The cause is proven, or the cycle is planned as a test of a hypothesis.
3. A written prediction exists for every test, in the goal's metric.
4. The check uses the baseline method and compares with both the prediction and the goal.
5. What is left is broken down, and the limits (safety, quality, cycle time, cost) are checked.
6. The act decision follows the table; nothing is standardised, rolled out or closed without a measured check.
7. An adopted change has a new standard, training of all shifts and a check with who, how and how often.
8. Every number is the user's, computed from it, or labelled as invented, a rule of thumb or set by local policy.

## Output

- `assets/a3-template.md`, filled in: every section, and for each cycle the prediction, the result and the act decision.
- `assets/test-record.md` for each cycle.
- Say first where the cycle stands: what the check shows against the prediction and the goal, and the act decision. Writing rules for the sheet are in [the A3 sheet](references/a3-sheet.md).
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. A solution written as the problem, or a goal with no measured baseline (fix: step 1).
2. Countermeasures that do not name the cause they act on (fix: steps 3, 4).
3. No prediction before the test, so the check has nothing to test against (fix: step 5).
4. Several changes in one test, so nobody knows which one worked (fix: step 4).
5. Plan, do, plan, do: the check is skipped or filled with opinions (fix: step 7).
6. Standardising or rolling out after a partial result as if the goal were met (fix: step 8).
7. Closing the A3 without a new standard and a check that it is used (fix: step 9).

## Hand-offs

- Topics that need one owner to test a way to a target arrive from `improve-kaizen`, which chose the format and keeps the 30/60/90 sustain plan; this skill runs one cycle. Report the result and the act decision back to the topic owner there.
- Red KPIs and escalations arrive from `lead-daily-routine`; report each cycle's check and act decision at that tier meeting. Findings from a walk arrive from `lead-gemba-walk`.
- When a cause must be proven before the countermeasure, build the chain with `solve-5why`; a customer complaint, field failure or repeat problem goes to `solve-8d`.
- Whether a change on a measured characteristic is real or noise is checked on a control chart with `measure-spc`; a loss item from the loss tree arrives from `measure-oee`.
- An adopted change updates station documents with `plan-workstation-instructions` and the control plan with `plan-control-plan`.
- A cause in set-up goes to `improve-smed`; one in machine condition or maintenance goes to `improve-tpm`.
- Many candidate causes go to `solve-fishbone`; a problem that is not scoped (where and when unclear) goes to `solve-is-is-not`. A surviving hypothesis from either, or a root-cause action from `solve-5why` whose effect needs a check over a cycle, arrives here.
- A chronic problem with plenty of data that one cycle cannot crack goes to `solve-dmaic`.
- The D5 verification of a permanent action can arrive from `solve-8d`; single improvement cycles from audit opportunities arrive from `audit-process`.
