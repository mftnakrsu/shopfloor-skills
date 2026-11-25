---
name: solve-8d
description: >-
  Leads an 8D problem solving from D0 to D8 for customer complaints, field
  failures, repeat defects and serious internal problems: team, factual
  problem description, containment of all suspect stock, verified
  occurrence and escape root causes, permanent corrective actions, PFMEA
  and control-plan updates, and the 8D report. Use when a complaint or
  escalation needs an 8D, or when asked whether an 8D can be closed, e.g.
  "can we close it?" (8D-Bericht, Reklamation, Fehlerabstellung).
license: MIT
metadata:
  version: "1.0.0"
  category: solve
  standards: "IATF 16949 10.2.3, 10.2.4, 10.2.6"
---
# 8D problem solving

## Conventions

- D0 plan and emergency response; D1 team; D2 problem description; D3 containment; D4 root cause; D5 choose and verify permanent actions; D6 implement and validate; D7 prevent recurrence; D8 close and recognise the team.
- The occurrence root cause is why the defect was made. The escape root cause is why it was not detected before it reached the customer.
- Verification happens before implementation and proves an action works. Validation happens after implementation and proves it works in production.
- The clean point is the first part, lot or date from which product is certified good.

## Inputs

- The complaint (Reklamation) facts: customer, part number, defect with photo or sample, quantity affected and quantity checked, where and when it was found, lots or date codes, delivery dates.
- The customer's requirements: response times and report format.
- The process flow and the stations involved.
- The current PFMEA (process failure mode and effects analysis, Prozess-FMEA) and control-plan (Produktionslenkungsplan) rows.
- What has been done already.

Ask for every missing fact; never invent one. Copy the numbers, lots and dates the user gives exactly.

- Mode: start or run an 8D, or check an existing 8D for closure. Infer it from the request.
- To start an 8D without the complaint facts, ask for them in one short list (part and defect, quantity affected and checked, where and when found, lots or dates, delivery dates, what has been done so far, the customer's deadlines) and stop. At most add the blank `assets/8d-report-template.md`. Do not write D2 onwards with invented defects, numbers, dates or causes.
- A missing PFMEA, control plan or customer deadline does not block D0 to D3. Write "to be confirmed" in its place and list it as an open question.

## Procedure

1. **D0 Plan and emergency response.** If there is a risk to safety or the customer, take emergency actions (Notfallmaßnahmen) such as stopping shipment, blocking stock and informing the customer as required. Decide whether an 8D is needed: customer complaint, field failure, safety or legal topic, repeat problem, or a local criterion (set by local policy or customer requirement). Note the customer's deadlines. **Gate:** emergency actions in place or not needed, and the decision recorded.
2. **D1 Team.** Form a cross-functional team with process knowledge: production, quality, engineering, maintenance and the operators of the stations involved. Name a leader and a champion with authority. **Gate:** roles named.
3. **D2 Problem description.** Describe the problem with facts: what (part, defect), where (on the part and where found), when (found, produced, lot, delivered), how many (defective out of checked or delivered), how detected, plus an Is/Is-Not comparison (where the defect is seen and where it could be but is not, by part, lot, line, shift and time). Do not say in D2 which station made the defect or which check missed it; that belongs in D4. **Gate:** the statement is quantified and contains no cause and no solution.
4. **D3 Containment (Sofortmaßnahmen).**
   - Suspect locations: customer stock, in transit, finished goods, work in process, incoming or supplier stock, service parts. Give each a quantity, an action, an owner and a due date, or state why it is not suspect.
   - Suspect period: until D4 bounds it, treat all product made since the last known-good point as suspect, regardless of lot.
   - Sort method: proven able to detect the defect on known bad parts, for example a 100% check by hand or gauge. Never the check that already missed it.
   - Marking: propose how certified parts are marked, for example a coloured dot on each part and a "certified" label with the sort date on each box.
   - Clean point: set it as date, lot and serial. If the exact one is not yet known, state a provisional one, such as the first part sorted and marked or the first lot made after the 100% check started. Confirm it with the containment effectiveness check and the D4 findings.
   - Effectiveness: the sort finds the known bad parts, and no defect is reported after the clean point.
   - **Gate:** the customer is protected and containment is verified. Details in [the gates](references/d0-d8-gates.md).
5. **D4 Root cause.**
   - Find the occurrence and escape root causes separately. For each, list the causes to test and the on/off test that will verify it (`solve-is-is-not` to scope and eliminate, `solve-fishbone` to widen the list of causes, `solve-5why` for the occurrence, detection and system chains).
   - Occurrence test: recreate the suspected condition on a trial and show the defect appears; remove it and show it does not.
   - Escape test: with the suspected condition present, the check misses a known bad part; with the condition removed or restored, it catches it.
   - Escape point: the first control after the cause that should have caught the defect.
   - Systemic cause: ask why the system allowed both.
   - "Operator error" is never final: ask why the process allowed it (no error-proofing, an unclear instruction, ergonomics, distraction, a training gap). Question list in [root-cause verification](references/root-cause-verification.md).
   - **Gate:** both causes are verified with evidence.
6. **D5 Choose and verify permanent actions.** Choose one permanent action per root cause: the occurrence cause, the escape cause and, where found, the systemic cause. Prefer making the error impossible or detecting it at the source (error-proofing, IATF 16949 10.2.4) over training or extra inspection; retraining alone is a weak action (ladder in [root-cause verification](references/root-cause-verification.md)). Verify that it works, including that the fixed check catches a known bad part, and that it creates no new risk (PFMEA check). **Gate:** verification evidence.
7. **D6 Implement and validate.** Implement, then validate with production evidence over a period or quantity set by local policy or the customer. Remove containment only after validation. **Gate:** validation evidence, and containment ended with a record.
8. **D7 Prevent recurrence.** Update the PFMEA, control plan, station instructions, maintenance plans (`improve-tpm`) and error-proofing check frequencies. Check similar parts, lines and plants for the same risk and apply the fix there (read-across), and record the lesson learned (IATF 16949 10.2.3, SI 20). **Gate:** the document revisions are listed.
9. **D8 Close.** Run the Validation checklist. Confirm closure with the customer where required, recognise the team, and archive the 8D. **Gate:** the checklist is complete and closure is confirmed where required.

### Check an 8D for closure

1. Run the Validation checklist against the 8D as given.
2. If any item fails, say plainly that the 8D cannot be closed yet.
3. List every failed item with what is missing and the fix, discipline by discipline. Cover at least: containment scope (all six locations) and its effectiveness check; a missing escape cause, named as missing, with the question why the check after the station (for example a camera, sensor or end-of-line test) did not detect the defect; "operator error" as a final cause; retraining as the only action; missing verification and validation; D7 document updates and read-across.
4. For an operator-error cause, list the questions to ask and propose a stronger action for the occurrence and the escape cause, each with how its effectiveness will be verified.

## Validation

Closure checklist:

1. Both root causes are verified.
2. There is one action per root cause.
3. Verification and validation evidence exist.
4. Containment ended with evidence.
5. The PFMEA, control plan and instructions are revised.
6. The read-across to similar parts and lines is done.
7. Neither "operator error" nor "retrain only" is the final answer.
8. Every action has an owner and a date.

Before answering, also check: D2 has no cause, D3 names every suspect location, and no fact was invented.

## Output

- `assets/8d-report-template.md` for the report. When starting an 8D, fill D0 to D3 in full and give D4 to D8 as a plan with owners and due dates.
- `assets/containment-plan.md` for D3.
- The writing rules in [8D report](references/8d-report.md). Customer response times and report formats are customer-specific; ask for them.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. Solutions already in D2 (fix: step 3).
2. Containment only in-house (fix: step 4).
3. Sorting with the check that missed the defect (fix: step 4).
4. Only one root cause, with no escape cause (fix: step 5).
5. "Operator error, so retrain." (fix: steps 5, 6).
6. Closing before validation (fix: step 7).
7. No PFMEA or control-plan update, and no read-across (fix: step 8).

## Hand-offs

- Escalations arrive from `lead-daily-routine`; report the 8D status back to that tier meeting.
- A D7 maintenance-plan update goes to `improve-tpm`.
- Containment (D3) and the verification of permanent actions use a control chart: check stability with `measure-spc`; a repeated SPC signal with an unknown cause arrives from there.
- A low %C/A from a value stream map arrives from `improve-vsm`; a defect whose cause must be proven arrives from `improve-kaizen`.
- Customer, safety or repeat problems found on a gemba walk arrive from `lead-gemba-walk`.
- D4 uses `solve-is-is-not`, `solve-fishbone` and `solve-5why`; their verified causes come back to D4. The D5 verification of a permanent action can run as one test cycle in `solve-pdca`.
- The D7 control-plan update goes to `plan-control-plan` and the station-instruction update to `plan-workstation-instructions`; a shipped nonconforming product or a Safe Launch escape arrives from `plan-control-plan`.
- A chronic remainder after D7 goes to `solve-dmaic`; an effectiveness check by process audit after D6 or D7 goes to `audit-process`, and repeat, customer or safety-related audit findings arrive from there.
