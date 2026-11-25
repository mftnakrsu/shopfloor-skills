---
name: solve-dmaic
description: >-
  Runs and reviews DMAIC projects (Define, Measure, Analyze, Improve,
  Control) on chronic production or quality problems that have, or can
  collect, plenty of data: project charter with a factual problem statement
  and goal, measurement system analysis before the baseline, stability and
  capability of the baseline, stratification and hypothesis tests to find
  and verify the vital few causes, piloted and verified improvements, and a
  control plan with handover. Use when a long-standing problem needs a
  data-driven Six Sigma project, when a charter, baseline or capability
  must be set up, when a gauge study, test result or before/after
  comparison must be read, or when a phase tollgate must be signed off
  (DMAIC-Projekt, Six Sigma, Projektauftrag, Projektcharta, Phasenreview,
  Messsystemanalyse, MSA, Prozessfähigkeit, Hypothesentest, chronisches
  Problem, Verbesserungsprojekt).
license: MIT
metadata:
  version: "1.0.0"
  category: solve
  standards: "IATF 16949 9.1.1.1, 10.3.1"
---
# DMAIC project

## Conventions

- Y is the project output measure (defect rate, scrap, a dimension); X is a candidate cause or input that may drive Y. The vital few are the Xs that explain most of the gap.
- A tollgate (Phasenreview) is the sponsor's review at the end of each phase. It passes only when every deliverable of that phase exists; otherwise it fails and the open items are listed.
- A chronic problem is common-cause variation of a stable process: it has been there a long time and the control chart shows no signals. A sporadic problem is a special cause: a signal, a sudden step.
- Baseline is Y before any change, from a measurement system proven adequate.
- Within sigma (short-term, from subgroups) gives Cp and Cpk; overall sigma (standard deviation of all values) gives Pp and Ppk (JMP).

## Inputs

- The problem: Y, its unit and operational definition (what counts as a defect), the process and scope, how long it has existed.
- Data in time order: values or counts with the number checked, over a period long enough to show the variation, plus process records for candidate Xs (machine, shift, material lot, settings, environment).
- The specification limits, if Y is a measured characteristic.
- Measurement system results: gauge R&R (Messsystemanalyse) for measured Y, an agreement study for pass/fail inspection.
- The sponsor, the process owner, the team, and the goal if the sponsor has set one.
- Cost basis for the business case: cost per defect, scrap unit or hour.
- Mode: run a phase, or review a tollgate. Infer it from the request.

Ask for every missing input; never invent one. Copy the user's numbers exactly.

- Without baseline data (Y over a defined period and the volume), ask for it and stop. A project charter (Projektcharta) may be offered from `assets/project-charter.md` with the problem statement, goal and savings left blank; never fill them with assumed figures.
- Without specification limits, compute no capability (Prozessfähigkeit); report the mean and sigma and ask for the limits.
- Without a measurement system result, the Measure tollgate cannot pass; ask for the study or plan one.
- The significance level α and the acceptance limits for measurement studies are set by local policy; if none is given, use α = 0.05 and say so (rule of thumb).

## Procedure

1. **Check that DMAIC fits.** DMAIC improves an existing process that falls short of its requirements (ASQ). Use it when the problem is chronic, data are available or can be collected, and the cause and the solution are unknown (rule of thumb). Route elsewhere:

   | Situation | Use instead |
   |---|---|
   | Customer complaint, field failure, safety topic | `solve-8d` (a DMAIC can follow for a chronic remainder) |
   | One event or a single clear defect, cause findable at the station | `solve-5why` |
   | Control chart signal, sudden step | reaction plan and `measure-spc` first |
   | Cause and solution already known | just do it, or `improve-kaizen` |

2. **Define.** Fill `assets/project-charter.md`.
   - Problem statement: Y, where, since when, how much, out of how many, with the cost. No cause and no solution in it.
   - Goal: one Y, a target value, a date; set by the sponsor. Scope in and out, team, sponsor, process owner, and a high-level process map (SIPOC: suppliers, inputs, process, outputs, customers).
   - CTQ (critical to quality): the customer requirement Y is measured against.
   - Gate questions in [tollgates](references/tollgates.md).
3. **Measure.**
   - Write the operational definition and a data collection plan: what, how, how often, sample, who, which Xs are recorded with each value.
   - Check the measurement system before trusting any data. Gauge R&R, as %GRR of study variation or of tolerance: under 10% acceptable, 10–30% marginal, over 30% not acceptable; number of distinct categories at least 5 (AIAG guideline, via Minitab). The marginal band is decided by local policy. Attribute inspection: agreement with a reference standard, limit set by local policy. A failed study means the baseline, its capability and every reject decision made with that gauge are not yet trustworthy: fix the gauge or method, repeat the study, then take the baseline. Do not back-calculate a corrected baseline from the failed study and present it as the baseline.
   - Plot Y in time order on a control chart (`measure-spc`). Signals are special causes: react and remove them first; they are not the chronic problem.
   - Baseline: rate = defects ÷ units checked; for measured Y the mean, within sigma and overall sigma.
   - Capability only on a stable process with specification limits, roughly normal data and about 50 or more values (NIST; non-normal data in [statistics](references/statistics.md)). IATF 16949 9.1.1.1 asks for statistical studies of manufacturing processes, and for reaction plans where a characteristic is unstable or not capable. Cp = (USL − LSL) ÷ 6σ; Cpk = min[(USL − mean), (mean − LSL)] ÷ 3σ, with the within sigma.
   - Example (invented): tolerance 10.0 ± 0.3 mm, mean 10.1 mm, within sigma 0.05 mm. Cp = 0.6 ÷ 0.30 = 2.00; Cpk = min(0.2, 0.4) ÷ 0.15 = 1.33. Centring, not spread, limits this process.
   - State the gap: baseline against goal, in units and money.
4. **Analyze.**
   - List candidate Xs from the process map, a cause-and-effect diagram and the team's knowledge of the process.
   - Stratify Y by each recorded X (machine, shift, lot, setting band) and draw a Pareto of the defect types.
   - Test each difference that matters with the test for its data type (choice table and formulas in [statistics](references/statistics.md)): two proportions, two means (Welch t), paired before/after, more than two groups (ANOVA), counts by category (chi-square), a continuous X (regression).
   - Example (invented): machine A 60 defective of 2,000 (3.0%), machine B 20 of 2,000 (1.0%). Pooled p = 80 ÷ 4,000 = 0.02. z = 0.02 ÷ √(0.02 × 0.98 × (1/2,000 + 1/2,000)) = 0.02 ÷ 0.00443 = 4.5, above 1.96, so the difference is significant at α = 0.05.
   - Read the result in four steps:
     1. p ≤ α means a real difference in this data. A difference too small to matter is not a vital X.
     2. p > α does not prove there is no effect; the sample may be too small (NIST).
     3. Historical data show association, not cause: check confounders (season, lot, product mix) and confirm each vital X with a trial that sets X on and off, or a designed experiment, while other conditions are held.
     4. Quantify the gain. If the vital X were removed, Y would be expected to fall to the rate of the group without it (rule of thumb). If that rate is still above the goal, more Xs must be found, or the goal must be renegotiated with the sponsor.
   - Update the problem and goal statements with what was learned.
5. **Improve.**
   - One solution per verified vital X. Prefer removing the cause or error-proofing over inspection or training.
   - Assess the risk of each change (process FMEA, PFMEA) and pilot it at a limited scope.
   - Verify with data from the same measurement system: before/after with the same test as in Analyze, and new capability if Y is measured.
   - Confirm that the pilot moved Y toward the goal, and that the X really changed.
6. **Control.** Use `plan-control-plan` and `plan-workstation-instructions`.
   - Update the control plan with the vital Xs and Y, each with a method, a frequency and a reaction plan.
   - Put SPC on the key X or Y (`measure-spc`), and error-proofing with check frequencies.
   - Update standard work, PFMEA and maintenance plans; hand over to the process owner with a signed record.
   - Check that the gain holds after a period set by local policy, then close the project: savings confirmed by finance where the plant requires it, read-across to similar lines, lessons learned. IATF 16949 10.3.1 asks for a documented improvement process with its method, objectives, measurement of effectiveness and risk analysis.

### Review a tollgate

1. Check the phase's deliverables against [tollgates](references/tollgates.md) and the Validation list.
2. Say plainly whether the gate can pass. If it cannot, list every failed item with what is missing and the fix, and say whether the team must loop back to an earlier phase.
3. Never pass a gate on a deliverable that rests on a failed measurement system, an unstable baseline, or an untested difference.

## Validation

Check before answering:

1. The problem statement is quantified, has a period and a cost, and contains no cause or solution; the goal is a number with a date.
2. The measurement system passed before the baseline was used.
3. Capability is computed only on a stable baseline with specification limits, roughly normal data and enough values, with the formula filled in.
4. Every claimed X has a test result with its p-value or test statistic, and the practical size of the effect.
5. No X is called a root cause on historical association alone; a confirmation trial is named.
6. The expected gain from the vital Xs is compared with the goal.
7. Improvements are verified with data; the control plan, reaction plan and owner exist before closure.
8. Every number is the user's, computed from it, or labelled as invented, a rule of thumb or set by local policy.

## Output

- Say first which phase the project is in and whether its tollgate can pass, then the reasons.
- Then the numbers: baseline, gap, test results with each formula filled in with the user's figures, and what they mean.
- Then the open items, each with an owner and a due date to be set by the team.
- Fill `assets/project-charter.md` in Define and `assets/tollgate-review.md` for any tollgate.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. A cause or solution in the charter, so the project only proves a fix chosen in advance (fix: step 2).
2. A baseline taken with a gauge that has not passed a measurement study (fix: step 3).
3. Capability on an unstable process, or Cpk computed with the overall sigma (fix: step 3).
4. A difference claimed without a test, or "not significant" read as "no effect" (fix: step 4).
5. Historical correlation taken as a verified root cause (fix: step 4).
6. One X fixed although it cannot close the gap to the goal (fix: step 4).
7. The project closed without a control plan, reaction plan and process-owner handover, so the gain fades (fix: step 6).

## Hand-offs

- A chronic red KPI with no single cause arrives from `lead-daily-routine`; a chronic loss from the loss tree arrives from `measure-oee`; report the tollgate status back to that tier meeting.
- Control charts, stability checks and capability on the baseline and after Improve go to `measure-spc`.
- A single defect or event inside the project, with its cause findable at the station, goes to `solve-5why`; a customer complaint or safety topic goes to `solve-8d`.
- A vital X in machine condition goes to `improve-tpm`; one in set-up or changeover goes to `improve-smed`.
- Control-phase updates go to `plan-control-plan` and `plan-workstation-instructions`; a known solution with no need for analysis goes to `improve-kaizen`.
