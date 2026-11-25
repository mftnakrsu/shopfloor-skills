---
name: improve-smed
description: >-
  Runs a changeover reduction (SMED) study on machines and lines: films or
  reads a changeover, builds the element sheet, separates internal from
  external work, converts and streamlines it, decides with EPEI whether the
  time saved becomes more capacity or smaller lots, and keeps set-up
  verification and first-piece approval in place. Use when a changeover,
  set-up, die change, mould change or tool change is too long, when
  changeover time must be cut to a target, when a changeover-reduction
  plan or target risks cutting set-up verification, or when deciding how
  to use freed changeover time (Rüstzeitreduzierung, Rüstzeit,
  Rüstwechsel, inneres und äußeres Rüsten, Losgröße, Erstteilfreigabe).
license: MIT
metadata:
  version: "1.0.0"
  category: improve
  standards: "IATF 16949 8.5.1.1, 8.5.1.3"
---
# Changeover reduction (SMED)

## Conventions

- Changeover time (Rüstzeit) runs from the last good part of the old run to the first good part of the new run, both at normal speed. Trial parts, adjustment and the wait for first-piece approval are inside it. Times are in minutes. Elapsed time is the machine-stopped time; labour time is the sum over all people.
- Internal work (inneres Rüsten) can only be done with the machine stopped. External work (äußeres Rüsten) can be done while it runs.
- SMED (single-minute exchange of die) aims for a changeover under 10 minutes, a single-digit number of minutes, not one minute.
- EPEI (every part every interval; German texts usually keep the acronym) is how often every product on a machine is made once. Lot size is Losgröße.
- Set-up verification is the check that the new set-up makes good parts before the run continues, including first-piece approval (Erstteilfreigabe).

## Inputs

- Mode: study (analyse a changeover), decide (use the time saved) or review (check a changeover plan or claim). Infer it from the request.
- Study: a video, or an element list taken from one, with start and end times, who did each element and whether the machine was stopped. Also the product pair (from and to).
- Decide: available time per period, demand and cycle time per product, the number of products, the changeover time per product before and after, the current lot sizes or interval, and whether the machine limits output (overtime, backlog, late deliveries).
- The current set-up verification: who approves the first part, what is checked, and the records kept.

Ask for every missing input; never invent one. Copy the user's times and quantities exactly.

- A study without element times: ask for a video or an element list with times and machine state, add the blank `assets/element-sheet.md`, and stop.
- A decision without available time, demand, cycle times or the number of products: ask for them in one short list and stop. At most show the formula. Do not decide on invented numbers.
- A missing verification description does not block a study; list it as an open question.

## Procedure

### A. Changeover study

1. **Choose the machine.** Start where set-up loss hurts most: the bottleneck, or the largest set-up loss in the OEE loss tree.
2. **Film a normal changeover** from the last good part to the first good part, one camera per person. Explain the purpose to the team first; being watched can change the times. Film more than one changeover if times differ by product pair.
3. **Element sheet.** Split the video into elements of a few minutes or less. For each record start, end, duration, person, machine stopped or running, and type: prepare, remove and mount, connect, adjust and trial, verify, wait or search. Fill `assets/element-sheet.md`.
4. **Separate.** For each element done while stopped, ask: must the machine be stopped for this? If not, it is external work done internally. Move it before or after the stop with a checklist and a staged cart (fetching the next tool, gauges, material, paperwork; returning the old tool).
5. **Convert.** Change internal work into external: preheat moulds or dies, preset tools offline, pre-assemble on an intermediate jig, prepare the first-piece gauge and drawing before the stop.
6. **Streamline the internal work**, in this order:
   - Clamping: functional or quick clamps, fewer bolts, quarter-turn fasteners.
   - Standardise function: same clamp height, locating points and connections on every tool.
   - Eliminate adjustments: fixed stops, locating pins, stored settings, gauges instead of trial and error. Trial parts are time and scrap.
   - Parallel work: a second person cuts elapsed time but not labour time.
   - Mechanise last.
   Then shorten the external work so it fits inside the previous run.
7. **Cheap before costly.** Take the procedural gains first (steps 4 and 5, checklists, staging); buy hardware only for what remains.
8. **Calculate.** Internal time before and after; saving = before − after in minutes, and saving % = (before − after) / before × 100. A pass typically saves about 45–50% (rule of thumb from practitioner sources); repeat passes toward the target. Worked example in [changeover study](references/changeover-study.md) (a deliberately large example; typical first-pass saving is about 45%).
9. **Standardise.** Write the new method as a changeover standard with its checklist (`assets/changeover-standard.md`), train the setters, and re-time the next changeovers against it (number set by local policy). Update the set-up instruction.

### B. Use the time saved (EPEI)

1. **Formulas**, per period (for example a week):
   - A = available time; R = Σ demandᵢ × cycle timeᵢ; C = Σ changeover times for one cycle through all products.
   - If A ≤ R, the machine is over capacity before any changeover: say so and escalate; SMED alone cannot fix it.
   - Minimum EPEI = C / (A − R) periods. The chosen interval must be at least this, with a buffer for losses.
   - Lot sizeᵢ = demandᵢ × interval. Changeover time per period = C / interval.
   - Derivation and worked example in [EPEI decision](references/epei-decision.md).
2. **Compute before and after** with the user's numbers.
3. **Decide the goal:**
   - Capacity: the machine limits output (overtime, backlog, late deliveries, lost sales). Keep the lot sizes and turn the freed minutes into output: freed minutes = (C_before − C_after) × cycles per period; extra pieces = freed minutes / cycle time.
   - Smaller lots: the machine has spare capacity. Shorten the interval, cut lot sizes and stock.
   - Both: first secure demand plus a buffer, then use the rest for smaller lots.
   Ask when the goal is unclear; otherwise state the reason in numbers.
4. **Choose the interval** as a practical one (shift, day, week) that is not below the minimum EPEI. Keep the changeover time per period near the allowance: about 10% of available time is a typical target (rule of thumb cited by LEI); the rest is set by local policy.
5. **Change the schedule.** The saving counts only when lot sizes or the plan change; otherwise it is lost as idle time.

### C. Keep set-up verification

1. Never remove the first-piece approval or set-up verification to hit a time target. In short, IATF 16949 8.5.1.3 expects every set-up to be checked and recorded before the run continues, with written guidance for the setters and, where it fits, first-off and last-off part comparison.
2. Make it faster instead: call the inspector at the last good part, stage gauges and drawings at the machine, check the last-off part of the old run as external work, use fixed criteria and go/no-go gauges, or let a trained, released person at the machine approve where local rules allow.
3. Until the first part is approved, everything made since the set-up is suspect. Producing on before approval puts a whole box or more at risk.
4. When the method changes (new clamps, removed adjustments), update the set-up instruction, the control-plan row (IATF 16949 8.5.1.1) and the PFMEA if the risk changes. Details in [set-up verification](references/setup-verification.md).

### D. Review a plan or claim

1. Check it against Validation and Pitfalls.
2. Name each gap with its fix and the minutes it saves; add them up against the target. Where the split inside an element is not known, give an estimate per fix, labelled as an estimate to confirm by re-timing, so the total can still be checked against the target.
3. Reject any saving that comes from dropping verification, and show a path to the target that keeps it.

## Validation

Check before answering:

1. The changeover is timed from last good part to first good part, with trial parts and approval inside.
2. Every element is marked internal or external, and external work is moved out of the stop.
3. Procedural steps come before hardware spending.
4. Set-up verification and first-piece approval are still in place.
5. EPEI is computed with A > R, before and after, and the interval is not below the minimum.
6. The capacity-or-lots choice has a stated reason in numbers, and the schedule or lot sizes change.
7. A study ends with the new changeover standard and its re-timing plan.
8. No input was invented; open questions are listed.

## Output

- Study: the filled `assets/element-sheet.md`, the improvements in order with minutes saved, the before and after totals, and always the new standard: `assets/changeover-standard.md` filled in, with the re-timing plan. Include it in the answer; do not only offer it.
- Decide: the EPEI before and after, the chosen interval, lot sizes per product, the capacity-or-lots recommendation with its reason, and the schedule change.
- Review: each gap with its fix, the minutes added up against the target, and the verification kept.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. Timing only the mechanical swap, without run-up, trial parts and approval (fix: step A3).
2. Buying clamps before taking the free separation gains (fix: steps A4, A7).
3. Cutting the time by skipping first-piece approval (fix: part C).
4. Pocketing the saving without changing lot sizes or the schedule (fix: step B5).
5. Claiming capacity on a machine that does not limit output (fix: step B3).
6. Studying one changeover when times differ by product pair (fix: step A2).
7. No standard, so times drift back (fix: step A9).

## Hand-offs

- Escalations about changeover losses or over-capacity machines go to the tier meeting in `lead-daily-routine`.
- A set-up that produced defects reaching the customer goes to `solve-8d`.
- The set-up loss arrives from the loss tree in `measure-oee`, from `improve-tpm` or from long set-ups at the bottleneck in `improve-tpt`; after the change, re-measure availability in `measure-oee`.
- Breakdowns or machine-condition problems seen during changeovers go to `improve-tpm`.
- New machine cycle times or freed capacity on a manual line go to `improve-line-balancing`.
- A changeover kaizen burst (EPEI too long, supermarket too large) arrives from `improve-vsm`; long supplier change-overs that stretch a kanban loop's lead time arrive from `improve-kanban-pull`.
- After the change, re-check the stability of the critical characteristics with `measure-spc`; signals that start after changeovers arrive from there.
- Improvement topics that need a workshop or a sustain plan go to `improve-kaizen`.
- Long set-ups seen on a gemba walk arrive from `lead-gemba-walk`.
- New set-up verification and first-off rules go to `plan-control-plan`; the new set-up and first-off steps go to `plan-workstation-instructions`.
- A root cause in set-up or changeover arrives from `solve-5why`, `solve-pdca` and `solve-dmaic`.
