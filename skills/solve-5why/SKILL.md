---
name: solve-5why
description: >-
  Builds and reviews 5-Why chains for a defined production or quality
  problem: one chain for why the problem occurred, one for why it was not
  detected and one for why the system allowed it, with an evidence check on
  every link, stop rules, and one action per root cause. Use when a root
  cause must be found with 5 Why or why-why analysis, when an existing
  5-Why must be checked before it is accepted, or when occurrence,
  detection and systemic causes must be separated (5-Why-Methode,
  5-Mal-Warum, Warum-Warum-Analyse, Ursachenanalyse, Fehlerursache,
  Auftretensursache, Nichtentdeckung, Systemursache).
license: MIT
metadata:
  version: "1.0.0"
  category: solve
  standards: "IATF 16949 10.2.3, 10.2.4"
---
# 5-Why analysis

## Conventions

- A link is one "why?" and its answer (because …). A chain (Warum-Kette) runs from the problem statement to a root cause; a leg is one of three chains.
- Occurrence leg (Auftretensursache): why the defect or problem was made. Detection leg (Nichtentdeckung): why no control caught it before it went on. System leg (Systemursache): why the management system let both happen.
- Evidence status of each link: **verified** (proved by a test, data or observation), **hypothesis** (plausible, not yet checked), **rejected** (contradicted by facts).
- The escape point is the first control after the cause that should have caught the problem.

## Inputs

- The problem facts: what (part, defect or deviation from standard), where found, when (date, shift, lot), how many out of how many, how it was found.
- The process flow around the problem, and every check or control after the step where it arises.
- What has been checked so far: measurements, trial results, records, observations, and what changed recently (material, tool, setting, person, method).
- Optional: the PFMEA (Prozess-FMEA) and control-plan (Produktionslenkungsplan) rows, maintenance plan, standard work.
- Mode: build a new analysis, or review an existing one. Infer it from the request.

Ask for every missing fact; never invent one. Copy the user's numbers, dates and lots exactly.

- Without the problem facts, ask for them in one short list and stop: what the defect is, how many out of how many, where it is found (station or check), when it is found and since when, how it is found, what has been checked and what data exists. At most add the blank `assets/5why-worksheet.md`. Never write a chain or name a root cause from assumed facts.
- A broad problem (a trend or general complaint with no defect type) is not a 5-Why problem yet. Ask for the breakdown (by defect type, location, shift, machine) and run the chain on the largest single item.
- With facts but no evidence, give the first whys only as hypotheses, each with the check that would confirm it. Never call a hypothesis a root cause.

## Procedure

1. **State the problem.** One factual sentence with what, where, when and how many, as found. No cause, no suspected cause and no solution in it; keep changes and findings in a separate list of facts. If the user's statement contains a cause ("because the gauge was not used …"), move that into the occurrence leg as a hypothesis.
2. **Go and see.** Base each answer on parts, the station, records and the people who do the work, not on desk opinions. List what changed before the problem started.
3. **Build the occurrence leg.** Ask "why was it made?" Each answer is a physical or process condition that directly causes the answer above it. One cause per link; if two causes each contribute, branch and follow each branch to its own root. Start points per leg in [three legs](references/three-legs.md).
4. **Build the detection leg.** List the controls after the cause in flow order. Start at the escape point: should it have detected the problem? If yes, ask why it did not; if no control could, that absence is the first answer. Continue to the condition that let the control fail (device, setting, method, frequency).
5. **Build the system leg.** Its first whys are the root of the occurrence leg and, where a control existed and failed, the root of the detection leg. Ask why the system allowed each: risk analysis, planning, change control, maintenance planning, standard work, design rules. These roots usually sit with support functions (engineering, quality, maintenance, management).
6. **Check the evidence on every link.**

   | Evidence | Verifies the link when |
   |---|---|
   | On/off test | Creating the condition brings the problem back; removing it stops the problem |
   | Data comparison | The problem appears where the condition is present and not where it is absent (by lot, shift, machine, time) |
   | Direct observation | The condition is seen and recorded at the station (photo, measurement, log) |
   | Record or document | A record shows the condition (drawing, plan, log, change record) |

   - Mark each link verified, hypothesis or rejected, with its evidence or the check to run, an owner and a date.
   - Opinions, "probably" and "usually" are hypotheses. Whys below a hypothesis stay hypotheses; drop a rejected link and its branch, and look for another answer.
   - A root cause is accepted only when its link is verified, and for the occurrence leg preferably by an on/off test. Methods in [evidence and stop rules](references/evidence-and-stop-rules.md).
7. **Apply the stop rules.** Stop a chain only when all three hold:
   1. The answer is a condition of the process, design or management system that the team can change.
   2. Counterfactual test: if this condition were corrected, the problem would not be likely to recur.
   3. Therefore test: reading from the root back to the problem, each step follows with "therefore".

   Never stop at a person ("operator error", or a person's attention, care or memory), at "no time" or "bad luck", at a restated symptom, or at a supplier without its own chain; ask what in the process allowed the error, using the human-error questions in [evidence and stop rules](references/evidence-and-stop-rules.md). The number of whys is not fixed.
8. **Set one action per root cause.** Each verified root in each leg gets its own action, chosen from the strongest feasible level:
   1. Make the error impossible.
   2. Detect at the source and stop (error-proofing; IATF 16949 10.2.4 asks for a documented choice of error-proofing methods with test frequencies).
   3. Detect later, automatically.
   4. Standardise (instruction, checklist, visual aid).
   5. Train, remind or inspect by hand.

   - Training, a reminder or a manual check alone is the weakest level. It can support a stronger action but is never the action on its own.
   - Give each action an owner, a date and how its effect will be verified. The check period is set by local policy.
9. **Close the loop.** Name the PFMEA, control plan, instruction or maintenance-plan rows to update and the similar parts or lines to check for the same cause (IATF 16949 10.2.3 asks for systemic corrective action that considers similar processes and products, and for updated documents). Then run the Validation checks.

Example (invented): on the early shift, 14 of 600 brackets had a drilled hole 0.8 mm off position, found at the welding station when the bolt would not fit.

| Leg | Why? | Because | Evidence | Status |
|---|---|---|---|---|
| Occurrence | Hole off position | Bracket not seated against the locator | Chips found under 3 of 3 rejected parts at the fixture | Verified |
| Occurrence | Not seated | Chips build up on the locator | On/off: 20 parts with chips placed, 9 off; cleaned, 20 of 20 good | Verified |
| Occurrence | Chips build up | No chip blow-off in the cycle and no cleaning step in standard work | Cycle program and standard work read | Verified (root) |
| Detection | Not caught at the hole-position check | Check is 1 part per 200 | Control plan row | Verified |
| Detection | Frequency of 1 per 200 | Frequency set without a known cause that shifts position | Control-plan review record | Hypothesis: ask the planner, owner and date set |
| System | Chips not foreseen | PFMEA has no chip-on-locator cause for this fixture | PFMEA row | Verified (root) |

The system row for the detection leg (why the frequency was set that way) waits until the detection hypothesis is checked.

Therefore test: no blow-off, therefore chips build up, therefore the bracket does not seat, therefore the hole is off.

| Root cause | Action | Strength | Verified by |
|---|---|---|---|
| No chip blow-off or cleaning step | Blow-off added to the cycle, and a seat sensor that stops the drill if the part is not on the locator | Detect at the source and stop | Seat sensor stops on a challenge part with chips; no position fault over a period set by local policy |
| PFMEA without chip cause | Add the cause to the PFMEA and check the other drilling fixtures for it | Standardise | PFMEA revision and read-across record |

### Review an existing 5-Why

1. Check the problem statement, then each link against steps 6 and 7.
2. Say plainly whether the analysis can be accepted. If not, list every failed item with what is missing and the fix: a link without evidence, a jump that fails the therefore test, a chain that stops at a person or a symptom, a missing detection or system leg, an action that is only retraining or a reminder.
3. Where a chain stops at a person, list the next whys to ask about the process, and propose a stronger action with how its effect will be verified.

## Validation

Check before answering:

1. The problem statement is factual, quantified and contains no cause.
2. There is an occurrence leg and a detection leg; there is a system leg, or its absence is named as an open item.
3. Every link has an evidence status, and every hypothesis has a check with an owner.
4. No root cause rests on a hypothesis or a rejected link.
5. No chain ends at a person, a symptom, "no time" or an outside party without its own chain.
6. Every root passes the counterfactual and therefore tests.
7. Every root cause has its own action, and no action is retraining or a reminder alone.
8. Every number and fact is the user's or labelled as invented, a rule of thumb or set by local policy.

## Output

- `assets/5why-worksheet.md`, filled in: problem statement, the three legs as tables with evidence and status, root causes, actions, open checks and document updates.
- Say first what is verified and what is still a hypothesis. In a review, say first whether the analysis can be accepted.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. A cause or a solution already in the problem statement (fix: step 1).
2. Only the occurrence leg, so the gap in detection and the system stays open (fix: steps 4, 5).
3. Links built on opinion with no evidence, presented as facts (fix: step 6).
4. A jump of several steps in one link, which fails the therefore test (fix: steps 3, 7).
5. A chain that ends at "operator error" or at a person's care or attention (fix: step 7).
6. Forcing exactly five whys, or stopping at a symptom (fix: step 7).
7. Retraining or a reminder as the only action (fix: step 8).

## Hand-offs

- A red KPI with an unknown cause arrives from `lead-daily-routine`; report the verified roots and actions back to that tier meeting.
- A customer complaint, field failure, safety topic or repeat problem goes to `solve-8d`; a 5-Why from here can feed its root-cause step.
- A root cause in maintenance planning or machine condition goes to `improve-tpm`; one in set-up or changeover goes to `improve-smed`.
- Checking whether a fix holds on a measured characteristic goes to `measure-spc`; an SPC signal with an unknown cause arrives from there.
- Problems seen on a gemba walk arrive from `lead-gemba-walk`; a defect whose cause must be proven arrives from `improve-kaizen`; a quality loss from the loss tree arrives from `measure-oee`.
- Many candidate causes, or no clear first why, go to `solve-fishbone`; a problem that is not scoped (where and when unclear, or a first why disputed) goes to `solve-is-is-not` first. A surviving hypothesis from either arrives here to be drilled to its roots.
- Document updates from closing the loop go to `plan-control-plan` and `plan-workstation-instructions`; a Safe Launch escape that needs no full 8D arrives from `plan-control-plan`.
- Verifying an action's effect over a cycle goes to `solve-pdca`; a broad KPI or chronic problem with plenty of data goes to `solve-dmaic`, and a single defect inside a DMAIC project arrives from there.
- Single-cause audit findings arrive from `audit-process`.
