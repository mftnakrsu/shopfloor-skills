---
name: plan-workstation-instructions
description: >-
  Drafts and reviews station inspection instructions, measurement method
  sheets and operator work instructions derived from the control plan.
  Use when writing a station instruction from control-plan rows, when
  checking whether an existing work or inspection instruction matches the
  control plan (characteristics, special-characteristic symbols, gauge,
  sample size, frequency, recording, reaction plan) before it is released
  or audited, or when a control-plan or PFMEA change must reach the
  station. Maps control-plan fields to the instruction, writes steps with
  key points and reasons, adds set-up, restart, error-proofing and
  reaction blocks, runs seven consistency checks (coverage, special
  characteristics, sample and reaction, gauge capability, PFMEA trace,
  error-proofing, revision) and asks what the user means by a method
  sheet, as that term has no public definition (Prüfanweisung,
  Prüfmethodenblatt, Messanweisung, Arbeitsanweisung,
  Werkerselbstprüfung, WSP, Produktionslenkungsplan, PLP).
license: MIT
metadata:
  version: "1.0.0"
  category: plan
  standards: "IATF 16949 7.1.5.1.1, 8.3.3.3, 8.5.1.1, 8.5.1.2, 8.5.1.3, 8.5.1.4, 8.5.6.1.1, 8.6.6, 9.1.1.1, 10.2.4"
---
# Workstation inspection and work instructions

## Conventions

- The control plan (Produktionslenkungsplan, PLP) is the master. Every station document is derived from it and may never be looser than it: not in characteristics, specification, gauge, sample size, frequency, recording or reaction.
- To change a station check, change the control plan first through its own change process, then the instruction. A capable process is a reason to request a control-plan change, never a licence for the station document to differ.
- Below the control plan sit the inspection plan (Prüfplan), the station inspection instruction (Prüfanweisung) and the work instruction (Arbeitsanweisung) with the operator's own checks (Werkerselbstprüfung, WSP). Hierarchy in [control-plan to instruction](references/control-plan-to-instruction.md).
- "Prüfmethodenblatt" (method sheet) has no public definition. Common local meanings: a per-characteristic measurement method sheet (measuring points, fixture, datum, sequence, repeats, conditions, the capability study it belongs to), or a general description of an inspection method. Always ask which one the user's company means.

## Inputs

- The control-plan rows for the operation, with control-plan number, revision and date: characteristic number and name, product or process, special-characteristic class, specification, gauge or method, sample size and frequency, control method, reaction plan with its owner.
- The PFMEA rows for the operation, with revision (needed for the trace check only).
- The gauge list: ID, type, calibration status, capability study reference and result.
- Error-proofing devices with their challenge parts (red rabbits) and check frequency.
- Safety rules and PPE, the operators' languages, limit samples with IDs, set-up and restart rules.
- For a review: the existing instruction with its revision.
- For a method sheet: what the user's company means by it.

Ask for every missing input; never invent one. Copy every number, ID and revision exactly.

- No control-plan rows: ask for them in one short list (operation, characteristics with specification, gauge, sample and frequency, control method, reaction plan, control-plan revision) and stop. At most add the blank `assets/station-instruction.md`. Never draft checks with invented limits, frequencies, test values or gauge IDs.
- The user asks for a "Prüfmethodenblatt": ask what it means locally, offer the two common readings above, and wait before writing it.
- Missing capability evidence, PFMEA, languages or safety rules do not block a draft. Mark the field "to be confirmed" and list it as an open point.

## Procedure

1. **Choose the mode.** Draft a new document, or review an existing one against the control plan. Infer it from the request.
2. **Fix the scope.** One operation, one control-plan revision. List every control-plan row for that operation; this list is the contract for the document.
3. **Map each row to the document.** Use the field map in [control-plan to instruction](references/control-plan-to-instruction.md). Every control-plan row becomes exactly one check row; no row is dropped and no check appears without a row.
4. **Write the work steps.** Verb first, one action per step. For each step give the key points (quality, safety, the knack) and a reason for each key point (TWI Job Instruction). Split a step with more than about five key points (rule of thumb). Put a photo or pictogram slot on every step and an OK/NOK picture pair on every visual check. Writing rules in [operator instruction writing](references/operator-instruction-writing.md).
5. **Write each check row.**
   - What: characteristic number and name, with the special-characteristic symbol from the control plan (customer symbol or conversion table, IATF 16949 8.3.3.3).
   - With what: gauge ID and how to use it (where to measure, fixture, sequence).
   - How many and how often: copied word for word from the control plan, including set-up, first-off, after tool change or after a stop.
   - Decision: the specification, or for attribute checks the criterion and the limit-sample ID. Attribute acceptance is zero defects (8.6.6).
   - Record: variable data are recorded as values, never only as OK/NOK (9.1.1.1); name the chart, sheet or system.
6. **Add the blocks the clauses require**, where they apply:
   - Set-up and first-off/last-off release, with who releases (8.5.1.3).
   - Restart after a planned or unplanned stop (8.5.1.4).
   - Error-proofing check: device, challenge part ID, frequency from the control plan, what to do if the device fails (10.2.4).
   - Approved alternate method, with its own instruction (8.5.6.1.1).
   - Safety rules and PPE at the top (8.5.1.2).
7. **Write the reaction box.** For each check: stop or hold, mark and segregate, contain back to the last good check, the named role to call, what to record. Copy it from the control-plan reaction plan exactly. If that reaction lacks a containment scope or a named role (for example "inform the supervisor" alone), do not add your own text at the station: copy it, list the gap as an open point, and send it to the control-plan owner.
8. **Write the method sheet** only after the user has defined it. For the measurement reading, the method must be the one used in the capability study, or the study does not apply. Fields in `assets/method-sheet.md`; capability limits in [measurement capability](references/measurement-capability.md).
9. **Run the seven consistency checks** in [consistency checks](references/consistency-checks.md), on a draft and on every review:
   1. Coverage both ways: every control-plan row for the operation is in the document, and every check in the document has a row.
   2. Special-characteristic symbols match the control plan.
   3. Sample size, frequency and reaction match the control plan exactly.
   4. Every gauge has calibration status and capability evidence.
   5. Every control-plan detection control traces to the PFMEA, and every high-priority PFMEA item has a control.
   6. Every error-proofing device has a verification step and frequency.
   7. The document's revision is based on the latest control-plan and PFMEA revision.
   For a review, give each check pass or fail with the finding, the clause and the fix.
10. **Release.** Language versions for every language the operators understand, legible and at the station (8.5.1.2); approval; training of the operators before use, recorded.

## Validation

Check before answering:

1. Every control-plan row for the operation has exactly one check row, and no check is invented.
2. Every sample size, frequency, specification, gauge ID and reaction is the user's, copied exactly.
3. Special characteristics carry their symbol.
4. Variable characteristics record values.
5. Each reaction is copied from the control plan, and any missing containment scope or named role is listed as an open point.
6. All seven consistency checks were run, and each failure has a fix.
7. A "Prüfmethodenblatt" was written only after the user defined it.
8. Every number is the user's, from a cited source, or labelled as a rule of thumb or set by local policy.

## Output

- Draft: `assets/station-instruction.md`, filled in, then the consistency-check result and the open points.
- Review: say first whether the document can be released as it stands, then `assets/consistency-check-report.md` with one row per check.
- Method sheet: `assets/method-sheet.md`, once its meaning is agreed.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. A station check made looser than the control plan by a local decision, without a control-plan change (fix: Conventions, step 9).
2. A control-plan characteristic missing from the instruction, or an orphan check with no row (fix: steps 3, 9).
3. Variable data recorded only as OK/NOK (fix: step 5).
4. A reaction of "inform the supervisor" with no containment scope (fix: step 7).
5. An error-proofing device with no challenge-part check (fix: step 6).
6. A method sheet that measures differently from the capability study (fix: step 8).
7. One language only, or a revision older than the control plan (fix: steps 9, 10).

## Hand-offs

- A control-plan change request (for example a lower check frequency) and gaps found by the coverage, sample-and-reaction and PFMEA-trace checks go to `plan-control-plan`; a new or revised control plan arrives from there to be carried into the station documents.
- A control chart named as the control method is set up and read with `measure-spc`; its reaction plan feeds the reaction box.
- A D7 update to station instructions after a complaint arrives from `solve-8d`; report the new revision back to that 8D.
- New set-up and first-off steps after a changeover study arrive from `improve-smed`; operator cleaning and inspection standards arrive from `improve-tpm`.
- Instructions that are not followed or not understood at the station are checked on walks planned with `lead-gemba-walk`; a finding there comes back here for a fix.
- New standard work after a kaizen arrives from `improve-kaizen`; a rebalanced line's new station content arrives from `improve-line-balancing`.
- Document updates after a verified cause or an adopted change arrive from `solve-5why`, `solve-pdca` and `solve-dmaic`.
- Findings on station documents arrive from `audit-process`; an effectiveness check by process audit after an instruction release goes there.
