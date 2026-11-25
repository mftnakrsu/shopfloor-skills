---
name: measure-spc
description: >-
  Sets up and reads statistical process control (SPC) charts for one
  product or process characteristic. Use when a control chart must be
  chosen, when control limits must be calculated or checked, when chart
  data must be checked for out-of-control signals, or when a signal needs
  a reaction and an escalation path. Chooses between X-bar/R, X-bar/S,
  individuals and moving range, p, np, c and u charts, computes the limits
  from the process data with the standard constants, applies the Western
  Electric or Nelson run rules, keeps tolerance limits apart from control
  limits, and links each signal to the reaction plan of the control plan
  and to tier escalation (Statistische Prozessregelung, SPR,
  Qualitätsregelkarte, QRK, Regelkarte, Eingriffsgrenzen, Mittelwertkarte,
  Spannweitenkarte, Urwertkarte, Reaktionsplan, Produktionslenkungsplan).
license: MIT
metadata:
  version: "1.0.0"
  category: measure
  standards: "IATF 16949 8.5.1.1 e, 9.1.1.1"
---
# SPC control charts

## Conventions

- Control limits (Eingriffsgrenzen) are computed from the process's own data at ±3 sigma; they show what the process does. Tolerance limits (Toleranzgrenzen, specification limits) come from the drawing; they show what the customer accepts. The two never replace each other.
- Sigma for limits is the within-subgroup sigma (R-bar / d2, s-bar / c4 or MR-bar / 1.128), never the standard deviation of all values pooled.
- A subgroup (Stichprobe) is a set of units measured together; n is its size. A rational subgroup holds units made close together, so that differences show up between subgroups, not within them.
- Phase I sets the limits from history; Phase II monitors new points against frozen limits.
- A signal is any point or pattern that breaks an agreed run rule. The reaction plan (Reaktionsplan) is the control plan's (Produktionslenkungsplan) instruction for that signal.

## Inputs

- The characteristic, its unit, and whether it is measured (variable data) or counted (attribute data).
- Subgroup size and frequency, and how units are picked.
- The data in time order: raw values, or per subgroup the mean and range. For attributes: per subgroup the count found and the number inspected.
- The baseline period, with known events (tool change, new material lot, repair).
- The tolerance, if one exists.
- The reaction plan and escalation path for this characteristic, and the run rules in force.

Ask for every missing input; never invent one.

- Attribute charts need the number inspected per subgroup. Without it, ask for it and stop: give no limits, only the formula with n left open. Never assume a constant n.
- Variable charts need time order and subgroup membership. Summary statistics without the subgroup size cannot be charted.
- Fewer than 25 subgroups: compute trial limits, label them as trial, and say when to recompute (rule of thumb, Lawson).
- No reaction plan or escalation path given: flag the gap, offer `assets/reaction-plan.md` with roles and time limits left blank as "set by local policy", and never name a role, a time limit or a tier on the user's behalf.

## Procedure

1. **Choose the chart.**

   | Data | Subgroup | Chart |
   |---|---|---|
   | Measured | n = 1 (slow output, every unit measured, homogeneous batch) | Individuals and moving range (I-MR, Urwertkarte) |
   | Measured | n = 2 to about 10 | X-bar and R (Mittelwert- und Spannweitenkarte) |
   | Measured | n above about 10, or varying n | X-bar and S |
   | Defective units, n varies | any | p chart (proportion), limits per subgroup |
   | Defective units, n constant | any | np chart or p chart |
   | Defects per unit area or unit, area constant | one inspection unit | c chart |
   | Defects, area or units vary | any | u chart |

   The n ≈ 10 break follows NIST. A defective unit fails as a whole; a defect is one flaw, and one unit can carry several. Formulas, constants and assumptions in [chart formulas](references/chart-formulas.md).
2. **Check the baseline (Phase I).** Time order known; at least 25 subgroups (rule of thumb, Lawson); rational subgroups; no mixed machines, cavities or spindles in one subgroup (each stream gets its own chart). Measurement system capable for this tolerance (set by local policy).
3. **Compute the limits.** Use the user's numbers exactly.
   - X-bar chart: centre = grand mean; UCL, LCL = grand mean ± A2 × R-bar. R chart: centre R-bar; UCL = D4 × R-bar; LCL = D3 × R-bar.

     | n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
     |---|---|---|---|---|---|---|---|---|---|
     | A2 | 1.880 | 1.023 | 0.729 | 0.577 | 0.483 | 0.419 | 0.373 | 0.337 | 0.308 |
     | D3 | 0 | 0 | 0 | 0 | 0 | 0.076 | 0.136 | 0.184 | 0.223 |
     | D4 | 3.267 | 2.575 | 2.282 | 2.115 | 2.004 | 1.924 | 1.864 | 1.816 | 1.777 |

     Constants from NIST; use them exactly as printed.
   - Example (invented): n = 4, grand mean 50.0, R-bar 2.0. A2 = 0.729, D4 = 2.282, D3 = 0. X-bar limits 50.0 ± 1.458 = 48.542 to 51.458. R chart UCL = 4.564, LCL = 0.
   - Individuals: centre = mean; limits = mean ± 2.66 × MR-bar (2.66 = 3 / 1.128); MR chart UCL = 3.267 × MR-bar, LCL = 0. MR is the absolute difference of consecutive values.
   - Example (invented): mean 20.0, MR-bar 0.5 → limits 18.67 to 21.33; MR UCL = 1.634.
   - p chart: p-bar = total defectives ÷ total inspected; limits = p-bar ± 3 √(p-bar (1 − p-bar) ÷ n_i), separately for each subgroup's n_i. A negative LCL means no lower limit.
   - Example (invented): 120 defectives in 3,000 inspected, p-bar = 0.04. A day with 200 inspected: UCL = 0.04 + 3 × √(0.04 × 0.96 ÷ 200) = 0.0816 (8.2%), no LCL. A day with 50 inspected: UCL = 0.123.
   - c and u charts and the S chart: see [chart formulas](references/chart-formulas.md).
4. **Clean the baseline.** Read the range, S or MR chart first: if spread is out of control, the X-bar or individuals limits are not valid yet. Remove only points whose cause was found and fixed, recompute once, and freeze the limits for Phase II. Unexplained signals stay in and are investigated. Never recompute limits on new data as routine; recompute only after a confirmed, deliberate process change, with the old and new limits recorded.
5. **Apply the run rules.** Default set (Western Electric, via NIST), each side separately:
   1. One point beyond 3 sigma.
   2. Two of three consecutive points beyond 2 sigma on the same side.
   3. Four of five consecutive points beyond 1 sigma on the same side.
   4. Eight consecutive points on the same side of the centre line.
   - Zone width on an X-bar chart: 1 sigma = A2 × R-bar ÷ 3; example above: 0.486, so zones at 50.486, 50.972 and 51.458. Individuals: 1 sigma = MR-bar ÷ 1.128.
   - Name each signal: rule, chart, subgroup number where the rule first fires, and side. Trend and alternating rules, Nelson's set and their false-alarm cost in [run rules](references/run-rules.md). Which rules are in force is set by local policy; agree them before reading the data.
   - On attribute charts with per-subgroup limits, apply rule 1 and the same-side run rule; zone rules need a constant n.
6. **Link each signal to the reaction.** For every signal, state the step from the user's reaction plan, in its order:
   - Stop or hold as the plan says; the operator's authority to stop comes first.
   - Contain: hold and check every unit back to the last in-control subgroup.
   - Find and fix the cause; record it on the chart as an event.
   - Notify the named role; escalate to the next tier when the plan's time limit passes or the signal repeats.
   - Restart only after a subgroup back in control, recorded.
   Use the signal-to-reaction table and the escalation ladder in [reaction and escalation](references/reaction-and-escalation.md).
7. **Check the tolerance separately.** A point inside tolerance can still be a signal, and the signal still gets the reaction. A unit outside tolerance is nonconforming product and goes to nonconforming-product handling whatever the chart says. Compute capability (Cp, Cpk) only on a process in control (NIST), never on a baseline with open signals.
8. **Write it up.** Fill `assets/spc-setup-sheet.md` for a new chart; log signals and reactions in `assets/reaction-plan.md`.

The optional calculator `scripts/spc_limits.py` (standard library) computes X-bar/R, I-MR and p-chart limits from a JSON file and lists rule 1 to 4 signals. Every result can be computed by hand from the formulas above.

## Validation

Check before answering:

1. The chart matches the data type and subgroup size; attribute charts know n for every subgroup.
2. Limits come from the process data and the within-subgroup sigma, with the constant for the user's n.
3. Tolerance limits are not drawn or used as control limits.
4. The spread chart is read before the location chart.
5. Every signal names its rule, chart, subgroup and side.
6. Every signal has a reaction step and an escalation route from the user's plan, or the gap is flagged.
7. Every number is the user's, computed from it, or labelled as a rule of thumb or set by local policy.

## Output

- Say first whether the process is in control, and which signals need a reaction now.
- Then the chart choice with its reason, the limits with each formula filled in with the user's numbers, the signal list, and the reaction and escalation for each signal.
- For a check of an existing chart: say first whether it is right, then the corrected limits, then the reason.
- Fill `assets/spc-setup-sheet.md` or `assets/reaction-plan.md` when asked for a set-up or a reaction plan.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. Tolerance limits drawn as control limits, so a shifted process looks "in control" (fix: Conventions, step 7).
2. Limits from the pooled standard deviation of all values, which widens them when the mean drifts (fix: Conventions, step 3).
3. Only rule 1 checked, so shifts inside the limits are missed (fix: step 5).
4. A c chart, or one fixed limit, for defectives from varying sample sizes (fix: steps 1, 3).
5. Limits recomputed every week, so the chart follows the drift (fix: step 4).
6. A signal answered with "inform supervisor" and no containment back to the last good subgroup (fix: step 6).
7. Capability reported for a process that is not in control (fix: step 7).

## Hand-offs

- A signal that is not fixed within the reaction plan's time limit, or that repeats, goes to the tier board in `lead-daily-routine` as a quality red with an owner and a due date.
- A repeated signal with an unknown cause, or a signal linked to a customer complaint or shipped nonconforming product, goes to `solve-8d`.
- Signals traced to tool wear, machine condition or after repairs go to `improve-tpm`; signals that start after changeovers or set-ups go to `improve-smed`.
- Scrap and rework minutes from a characteristic out of control feed the quality loss in `measure-oee`.
- A quality red caused by an SPC signal, or a reaction-plan result, arrives from `lead-daily-routine` for chart and limit checks.
- Stability checks for containment and for verifying permanent actions arrive from `solve-8d`.
- A re-check of a characteristic's stability after a repair or a set-up change arrives from `improve-tpm` and `improve-smed`; chronic quality loss on one characteristic arrives from `measure-oee`.
- Demand or lead-time variation for a statistical kanban safety stock arrives from `improve-kanban-pull`; whether a kaizen gain is real or noise arrives from `improve-kaizen`.
- A reaction plan that is not followed at the station is checked on walks planned with `lead-gemba-walk`.
- A signal with an unknown cause that is not a complaint goes to `solve-is-is-not` to scope it, `solve-fishbone` for many candidate causes or `solve-5why` for the chain; checks that a fix holds arrive from those skills and from `solve-pdca`.
- A stable process that is not capable (chronic common cause) goes to `solve-dmaic`; its baseline and Improve capability checks arrive from there.
- The control-plan line and reaction plan for a charted characteristic go to `plan-control-plan`; a reaction plan or chart that must appear in the station instruction goes to `plan-workstation-instructions`; an audit of reaction-plan use goes to `audit-process`, and a reaction plan not followed found there arrives here.
