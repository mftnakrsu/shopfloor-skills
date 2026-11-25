---
name: plan-control-plan
description: >-
  Builds and reviews process control plans as the master document for all
  station documents. Use when a control plan must be written from a process
  flow and PFMEA, checked before release, an audit or a periodic review,
  updated after a change, complaint or nonconforming shipment, or when a
  prototype, pre-launch, production, Safe Launch, family or summary control
  plan is set up, changed or ended. Turns PFMEA controls and special
  characteristics into control-plan rows with specification, gauge, sample
  size and frequency, control method and a reaction plan with an owner;
  adds set-up, first-off, restart and error-proofing checks; flags gauges
  without a measurement system study; sets the review triggers and the
  values station documents must copy. Writing the station instructions
  themselves is out of scope (Produktionslenkungsplan, PLP,
  Kontrollplan, Prüfplan, Reaktionsplan, besonderes Merkmal,
  Anlaufabsicherung, Serienlenkungsplan, Vorserie, Prototyp).
license: MIT
metadata:
  version: "1.0.0"
  category: plan
  standards: "IATF 16949 8.5.1.1, Annex A, 8.3.3.3, 8.5.6.1.1, 9.1.1.1, 10.2.4"
---
# Process control plan

## Conventions

- The control plan (Produktionslenkungsplan, PLP) is the master: every process step from goods receipt to dispatch, every characteristic that needs a control, and the reaction to each deviation. Inspection plans (Prüfpläne), work and inspection instructions (Arbeits- und Prüfanweisungen) are derived from it and never contradict it.
- A row is one characteristic at one operation. Product characteristics are on the part; process characteristics are settings that make it (temperature, pressure, speed).
- Phases: prototype, pre-launch, production. Safe Launch (Anlaufabsicherung) is a temporary layer of extra controls on top of a pre-launch or production plan, never a phase of its own. It ends on evidence and the customer's release.
- Special characteristic (besonderes Merkmal): marked with the customer's symbol, or the plant's symbol through a conversion table, in drawing, PFMEA, control plan and station instruction alike.
- Last good check: the most recent check of the same characteristic that passed. Containment reaches back to it.

## Inputs

- Part number or family, change level, phase, customer, and the customer's own requirements (symbols, Safe Launch, approvals).
- The process flow with operation numbers.
- The PFMEA: per operation the characteristics, failure causes, prevention and detection controls, and the special-characteristic marks.
- Specifications from the drawing; process settings with their windows.
- Gauges per characteristic with their measurement system study status (MSA, Prüfprozesseignung).
- Error-proofing devices with their check method and frequency.
- Set-up, first-off, last-off and restart rules.
- The local reaction and escalation rule: who stops, who is called, time limits.
- For a review: the current control plan, its revision history, and changes, complaints or shipped nonconforming product since the last revision.

Ask for every missing input; never invent one. Copy the user's numbers exactly.

- No PFMEA (or characteristic list) and no specifications: ask for both in one short list, with the phase and the customer requirements, and stop. At most give the row structure and the blank `assets/control-plan-template.md`. Never fill a tolerance, sample size or frequency on the user's behalf.
- Safe Launch without agreed extra controls and exit criteria: ask for them; they are agreed with the customer.
- No reaction rule or owner: write "set by local policy" in the cells and list the gap. Never name a role, a time limit or a tier for the user.
- A gauge without a study status: mark it "MSA status to be confirmed".

## Procedure

1. **Fix the header and scope.** Fill the minimum general data (IATF 16949 Annex A.2 with its sanctioned interpretations): number, dates, customer, site, part numbers or a common designation, part name, change level, phase, key contact, operation numbers and names, responsible area. List in [columns and rows](references/columns-and-rows.md).
2. **Choose the plan type.**

   | Situation | Plan |
   |---|---|
   | One part, one process | Single control plan |
   | Several parts, same process, equipment and controls | Family plan with a common designation; list every member and every exception (tolerance, tool, extra step) |
   | Members differ in steps, equipment or special characteristics | Separate plans, or a family plan with separate rows for each difference |
   | Highly automated step whose limits and sampling sit in an MES | Summary rows that point to the controlling system and its revision (allowed by a sanctioned interpretation of Annex A) |
   | Process split over several plans or sites | Interlinked plans; each names the others and who owns the hand-over characteristic |

   Rules for each variant, Safe Launch included, in [variants and triggers](references/variants-and-triggers.md).
3. **Align the numbers.** Process flow, PFMEA and control plan use the same operation numbers and names. A step in one and not the other is a finding.
4. **Write one row per characteristic that needs a control.** Sources, in order:
   - every PFMEA failure cause with a prevention or detection control, and every high action-priority item;
   - every special characteristic;
   - every customer-required check, layout inspection and functional test (8.6.2);
   - set-up verification, first-off and last-off where applicable (8.5.1.3), restart after a shutdown (8.5.1.4);
   - each error-proofing device: its check with a master or challenge part and the check frequency (10.2.4);
   - approved alternate controls, marked as alternates (8.5.6.1.1).
5. **Fill the columns.** Specification from the drawing; gauge by ID or type; sample size and frequency; control method (SPC chart, check sheet, 100 % test, error-proofing); record type (values for variable data, never only OK/NOK, 9.1.1.1). Column rules in [columns and rows](references/columns-and-rows.md).
6. **Check the exposure of each frequency.** Parts at risk = output rate × interval between checks. That quantity is what the reaction must contain.
   - Example (invented): 90 parts an hour, one check every 4 hours → up to 360 parts back to the last good check. If the customer cannot accept that exposure, shorten the interval or add a detection step.
7. **Write the reaction plan for every row**, 100 % tests and error-proofed rows included: a reject there is still a deviation that gets the local rule. In order: stop or hold; contain suspect product back to the last good check; restore control and verify with a passing check; notify and escalate by the local rule; record. Name the owner by role. For an error-proofing device that fails its check: everything made since its last successful check is suspect, and production continues only on an approved alternate. Wording and gaps in [reaction plans](references/reaction-plans.md).
8. **Check the measurement systems.** Every gauge or method on the plan, attribute and visual checks included, needs a passed study (7.1.5.1.1). A missing study on a special characteristic blocks release of that row; list it with an owner.
9. **Add the Safe Launch layer when it applies.** For each extra control: what it catches, the containment it gives, and its exit criteria as agreed with the customer.
   - A defect found by the extra layer escaped the regular controls. It gets the reaction plan, structured problem solving, and a review of the regular detection control for that defect.
   - Exit only when every agreed criterion is met with evidence, open causes are closed, the regular plan is updated for every escape, and the customer has released it. Elapsed time or a part count alone never ends a Safe Launch.
10. **Set the review triggers** (8.5.1.1 f to i): nonconforming product shipped; any change to product, process, gauges, logistics, supply source, volume or PFMEA; a customer complaint and its corrective action; and a periodic review at a risk-based interval (set by local policy). Customer approval after a revision where the customer requires it.
11. **Cascade to the station.** Each row's characteristic, symbol, gauge, sample, frequency, record and reaction appear unchanged in the station's inspection or work instruction, and that document cites the control-plan revision.

### Review an existing control plan

1. Run the Validation checklist against the plan as given.
2. Say first whether it can be released or kept, then list each gap with the row, what is missing and the fix.
3. Check the revision against every trigger since the last revision: a change, complaint or shipped nonconforming product without a new revision is a finding.

## Validation

Check before answering:

1. Header complete, phase stated, family members and exceptions listed.
2. Operation numbers match the process flow and PFMEA.
3. Every PFMEA control, special characteristic, set-up check and error-proofing check has a row.
4. Every row has specification, gauge, sample size, frequency, control method and record type.
5. Every row has a reaction plan with containment back to the last good check and an owner by role, or the gap is flagged.
6. Every gauge has a study status; missing studies are listed.
7. Safe Launch exit is evidence-based and needs the customer's release.
8. Review triggers are stated.
9. Every number is the user's, computed from it, or labelled as a rule of thumb or set by local policy.

## Output

- Say first what the plan is ready for (release, review, Safe Launch exit) or what blocks it.
- Then the header, the rows in `assets/control-plan-template.md`, the open gaps with owners, and the review triggers.
- Every row carries every column: specification, gauge, sample size, frequency, control method, record and its own reaction plan with the owner. A shared rule may be defined once and cited by name, but the reaction cell is never left out or moved below the table.
- For a Safe Launch, also fill `assets/safe-launch-plan.md`.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. A control plan copied from the PFMEA detection column with no reaction plans (fix: step 7).
2. "Inform supervisor" as the whole reaction: no containment scope, no owner (fix: step 7).
3. A family plan that hides a member's different step, tool or tolerance (fix: step 2).
4. Error-proofing listed as a control with no check of the device itself (fix: steps 4, 7).
5. A gauge on the plan with no study, often a visual or attribute check (fix: step 8).
6. Ending a Safe Launch on the calendar while the extra layer still finds defects (fix: step 9).
7. Station instructions that differ from the plan, or a plan not revised after a complaint or change (fix: steps 10, 11).

## Hand-offs

- SPC chart choice, limits and run rules for a control-plan row go to `measure-spc`; a reaction plan that is unclear or not followed after a signal arrives from there.
- A shipped nonconforming product, a complaint, or a repeated escape found by a Safe Launch check goes to `solve-8d`; its D7 control-plan update arrives from there.
- Set-up verification and first-off rules after a changeover redesign arrive from `improve-smed`; error-proofing device checks and maintenance-related controls go to `improve-tpm`.
- Daily review of alternate controls and escalations from a reaction plan go to `lead-daily-routine`.
- Checking that the plan is followed at the station is planned with `lead-gemba-walk`.
