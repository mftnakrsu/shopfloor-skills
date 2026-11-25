---
name: improve-tpt
description: >-
  Calculates, checks and reduces the throughput time (lead time) of
  production lines and shops. Use when throughput time, lead time or WIP
  is too high, when a throughput-time figure must be calculated, checked
  or confirmed (for example one built from summed station cycle times),
  when choosing between faster machines, WIP caps or CONWIP to cut it, or
  when sizing a WIP cap. Maps the user's terms to one definition, measures
  throughput time with a Little's Law cross-check, computes raw process
  time, bottleneck rate and critical WIP, compares the line with the
  practical worst case, and applies WIP-cap and variability rules
  (Durchlaufzeit, DLZ, Lieferzeit, Bestand, Umlaufbestand, Engpass,
  Durchsatz).
license: MIT
metadata:
  version: "1.0.0"
  category: improve
  standards: ""
---
# Throughput time reduction

## Conventions

- Throughput time (TPT, Durchlaufzeit) is the average time one flow unit spends between two named inventory points. Lean "production lead time" and Factory Physics "cycle time" mean the same thing.
- Throughput (TH, Durchsatz) is good output per time unit, a rate. WIP (work in process, Umlaufbestand) is the count of flow units between the same two points.
- "Cycle time" alone is ambiguous: a station's repeat interval, a time through the routing, or processing only. Never use it unqualified; map it first.
- WIP, TH and TPT use one flow unit (piece, job, lot or order) and one clock (working hours or calendar days), stated every time.

## Inputs

- The boundary: start and end inventory points, and the flow unit.
- WIP counts at the same points on several days.
- Good output over the same window.
- Per step: average effective process time (including set-ups and stops), number of parallel machines or workplaces.
- Working time per day and the required output (customer demand).
- Optional: start and finish stamps of 20 to 30 tagged units (rule of thumb from practitioner use), the release rule, downtime, set-up and lot-size data, rework rate, the TPT target.

Ask for every missing input; never invent one. Copy the user's numbers exactly.

- TPT needs WIP and TH for the same boundary and window. If either is missing, ask for it in one short list (boundary, flow unit, WIP counts, good output over the same days, working time) and stop. At most give the formulas and the blank `assets/tpt-study.md`. Never present a TPT for the user's line from an assumed output rate. A WIP target holds only at unchanged output; say so, and leave the cap until output is known.
- Missing process times block only the reference points, the PWC comparison and the cap check. Measure TPT first, then ask for them.

## Procedure

1. **Map the terms.** Write each term the user uses next to its meaning here, using the table in [terms and measurement](references/terms-and-measurement.md). Order lead time (what the customer waits) is TPT plus order processing and backlog; if the customer waits longer than TPT, the gap is off the shop floor.
2. **Fix the boundary and unit.** Name the start and end points and the flow unit. Count everything between them: queues, units in process, in transit, in rework.
3. **Measure TPT with Little's Law.** TPT = WIP ÷ TH, with WIP the mean of the counts and TH the good output over the same window.
   - Example (invented): WIP counts average 40 jobs; output 4 jobs a day → TPT = 40 ÷ 4 = 10 working days; at 10 working hours a day, 100 working hours.
   - Little's Law gives the mean only. Customers feel the slow jobs: report the tail from the tagged sample when there is one.
4. **Cross-check.** Compare Little's TPT with the tagged-unit mean. Within about 10% (rule of thumb): consistent. A larger gap means broken data; check, in order: mixed units (pieces against lots), WIP and TH from different windows, scrap counted as output, rework or side stocks missed, calendar against working days, a window too short against the TPT. Never use ERP standard lead times as the measurement.
5. **Compute the reference points** (Hopp & Spearman, via Gallego).
   - Raw process time T0 = sum of the average process times along the routing, one unit through an empty line.
   - Station rate = machines ÷ process time. Bottleneck rate r_b = the lowest station rate.
   - Critical WIP W0 = r_b × T0: the least WIP that reaches full output in an ideal line.
   - Bottleneck utilisation u = TH ÷ r_b. X-factor = TPT ÷ T0.
   - Example (invented): steps of 2 h (1 machine), 3 h (2 machines), 1 h (1) and 2 h (1) → T0 = 8 h; station rates 0.5, 0.67, 1 and 0.5 jobs/h, so r_b = 0.5 jobs/h; W0 = 0.5 × 8 = 4 jobs; TH = 4 ÷ 10 = 0.4 jobs/h, so u = 80%; x-factor = 100 ÷ 8 = 12.5.
6. **Compare with the practical worst case (PWC).** At the line's WIP w:
   - Best case: TPT = T0 if w ≤ W0, else w ÷ r_b. PWC: TPT = T0 + (w − 1) ÷ r_b, and TH = r_b × w ÷ (W0 + w − 1).
   - WIP the PWC needs for the current output (rearranged from the PWC formula, valid for TH < r_b): w = TH × (W0 − 1) ÷ (r_b − TH).
   - Example (invented): PWC at 40 jobs gives TPT = 8 + 39 ÷ 0.5 = 86 h, below the measured 100 h; the PWC needs only 0.4 × 3 ÷ 0.1 = 12 jobs for 0.4 jobs/h. The line holds more than 3 times the WIP it needs.
   - Between best case and PWC: the line is managed well. Worse than PWC: large improvement potential. Details and formulas in [flow formulas](references/flow-formulas.md).
7. **Choose the lever** with this table (first matching row wins):

   | Finding | Lever |
   |---|---|
   | Bottleneck u above about 85% (FabTime) | Do not cut WIP first: it costs output. Raise bottleneck capacity or cut its effective process time and variability (step 9) |
   | WIP well above the PWC need, u below about 85% | Cap WIP (step 8); TPT falls roughly with WIP, TH barely moves |
   | Long waits in front of a batch process | Smaller transfer batches first; smaller process batches only with set-up reduction |
   | Expediting or priority classes | One release point and FIFO lanes with a maximum quantity |
   | WIP near W0 already | Cut T0: process time, transport, steps. Only here does a faster non-bottleneck step shorten TPT |

   A faster station that is not the only bottleneck does not raise r_b. Cutting T0 helps only when WIP is near or below W0.
8. **Set the WIP cap.** Cap the units between the two points: release a new unit only when one leaves (CONWIP), or set a maximum per FIFO lane or kanban loop. Levers and rules in [WIP and variability levers](references/wip-and-variability-levers.md).
   - Target WIP = TH × target TPT. Example (invented): halving 100 h at 0.4 jobs/h → 20 jobs.
   - Check output with the PWC TH formula: at 20 jobs, 0.5 × 20 ÷ 23 = 0.43 jobs/h ≥ 0.4 needed. If the line runs worse than PWC, the formula is optimistic.
   - Start between the current WIP and the target, then step the cap down weekly while output holds (rule of thumb). Stop lowering when output drops below demand; then fix variability first.
9. **Cut variability at the bottleneck.** Queue time ≈ V × U × t_e (Kingman), with V = (ca² + ce²) ÷ 2 and U = u ÷ (1 − u).
   - Example (invented): t_e = 1 h, u = 0.90, ca = ce = 1 → 9 h of queue. Halving ce → 5.6 h; u = 0.80 instead → 4 h; both → 2.5 h.
   - Attack ce: long unplanned stops, long set-ups, rework. Attack ca: batch releases, upstream batching, irregular arrivals.
10. **Plan and track.** Give each lever an owner, a date and a target in numbers. Track TPT (mean and tail), WIP, TH, bottleneck u and on-time delivery weekly, and re-run the Little cross-check after each change.

## Validation

Check before answering:

1. WIP, TH and TPT use the same flow unit, boundary, window and clock.
2. TPT comes from measured WIP and output, never from summed station cycle times or ERP standard times.
3. The Little's Law result is cross-checked against direct data, or the missing check is named.
4. r_b uses the slowest station rate, counting parallel machines; T0 is a sum of process times.
5. Every WIP cap is checked against the required output.
6. Every number is the user's, computed from it, or labelled as an assumption or a rule of thumb.

## Output

- `assets/tpt-study.md`, filled in: term map, boundary, measurement and cross-check, reference points, PWC comparison, chosen levers with owners, and the tracking plan.
- `assets/wip-count-sheet.md` when the user still has to collect the counts.
- Show every formula with the user's numbers and units. Optional calculator: `scripts/tpt_calc.py` (standard library); every result can be computed by hand from the formulas above.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. Summed station cycle times reported as throughput time (fix: steps 1, 3).
2. Throughput (a rate) mixed up with throughput time (a duration) (fix: step 1).
3. Pieces against lots, or working against calendar days, in one formula (fix: steps 2, 4).
4. Buying speed at a station that is not the only bottleneck, while units wait in queues (fix: steps 6, 7).
5. Cutting WIP at a bottleneck that runs above about 85% (fix: step 7).
6. Reporting only the mean when customers feel the slow orders (fix: step 3).
7. A WIP cap set without checking output, then dropped after one bad week (fix: step 8).

## Hand-offs

- A red delivery or lead-time KPI arrives from `lead-daily-routine`; report the TPT trend back to that tier meeting.
- A quality problem that drives rework loops or scrap with an unknown cause goes to `solve-8d` when it is a complaint or repeat problem.
