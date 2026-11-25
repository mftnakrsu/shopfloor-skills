---
name: audit-process
description: >-
  Runs and reports manufacturing process audits (IATF 16949 9.2.2.3),
  scored VDA 6.3 process audits and self-assessments, whole layered
  process audit programmes (not a single walk segment) and
  shopfloor-management self-audits. Use when planning or doing an
  internal or customer-style process audit, scoring a VDA 6.3 element,
  writing audit notes up as findings, grading nonconformities (major,
  minor, observation) and mapping them to ISO 9001 and IATF 16949
  clauses, designing or reviewing an LPA programme
  and its metrics, or auditing tier meetings. Builds the checklist from
  the control plan and PFMEA, covers every shift and the handover,
  writes each finding as requirement, evidence and gap, and follows up
  until actions are verified (Prozessaudit, VDA 6.3, Selbstbewertung,
  Layered Process Audit, LPA, geschichtetes Prozessaudit, Selbstaudit,
  Auditbericht, Abweichung, Hauptabweichung, Nebenabweichung,
  Feststellung, Normkapitel).
license: MIT
metadata:
  version: "1.0.0"
  category: audit
  standards: "ISO 9001 9.2, 10.2; IATF 16949 7.2.3, 9.2.2.1, 9.2.2.3, 10.2.3; ISO 19011; VDA 6.3; AIAG CQI-8"
---
# Process audit

## Conventions

- Three audit types: the manufacturing process audit (Prozessaudit), which checks one process on every shift against its control plan (Produktionslenkungsplan), PFMEA (Prozess-FMEA) and instructions; the layered process audit (LPA, geschichtetes Prozessaudit) programme, short yes/no checks by several management layers; and the shopfloor-management self-audit (Selbstaudit) of tier meetings and boards.
- Scope split: this skill owns the LPA programme: its design, layers, checklists, schedule, metrics and review. `lead-gemba-walk` owns only the optional LPA segment done inside one walk. Fixing a weak tier routine is `lead-daily-routine`; this skill audits and scores it.
- A finding (Feststellung) compares objective evidence with the audit criteria; a nonconformity (Abweichung) is a finding that breaks a requirement. ISO 19011 terms and principles in [clause map](references/clause-map.md).
- Clause numbers are ISO 9001:2015 and IATF 16949:2016, summarised in our own words. Edition status in [clause map](references/clause-map.md).

## Inputs

- Mode: plan an audit, write up and grade an audit already done, score a rated questionnaire, design or review an LPA programme, or follow up findings. Infer it from the request.
- Scope: the process, line or areas, the product family, the shifts it runs.
- Criteria: control plan, PFMEA and work instructions with their revisions; the customer's audit method and requirements; local standards.
- Auditor: role, qualification, and any responsibility for the area audited.
- Evidence: the audit notes, with records, IDs, values, dates and shifts; for a scored method, the points per question with starred questions marked.
- LPA programme: areas, layers and roles, frequencies, checklists, and the results for the period.

Ask for every missing input; never invent one. Copy every number, ID and revision exactly.

- Writing findings needs the evidence. Without audit notes or records, ask for the scope, the criteria documents and the evidence in one short list, and stop. You may add the blank `assets/audit-checklist.md` or a list of the usual question areas, labelled as a checklist, never as results.
- Missing revisions, a missing customer method or missing response deadlines do not block a write-up: mark them "to be confirmed" and list them as open points.
- Never invent a clause's wording or a customer rule. Where a rule depends on the edition or the customer, say so.

## Procedure

### A. Plan the audit

1. Choose the type from the purpose: process audit for one process against its documents; LPA programme for daily discipline on critical controls; SFM self-audit for the leadership routine.
2. Check the auditor: qualified for this audit type (IATF 16949 7.2.3) and with no responsibility for the area audited (ISO 19011; ISO 9001 9.2.2 asks for objectivity and impartiality). If not, name another auditor.
3. Fix scope and criteria in `assets/audit-plan.md`: every document with its revision, every shift the process runs, and a shift handover to observe (9.2.2.3). Use the customer's method where one is required, for example VDA 6.3 element P6.
4. Build the checklist (`assets/audit-checklist.md`) from the control plan's special characteristics and high-risk rows, the PFMEA's highest-priority causes, set-up and restart, nonconforming product, gauges, qualification, and the complaints and open findings of the area. Details in [process audit](references/process-audit.md).
5. Audit frequency follows risk (9.2.2.1): raise it after process changes, nonconformities or customer complaints; every process is covered within three calendar years.

### B. Collect the evidence

1. Audit during real production, on every shift in scope.
2. Trace both ways: one control-plan row to the station (instruction, gauge, record, reaction), and one station record back to its control-plan row and PFMEA line.
3. Look at the records of several recent days and every shift, not only today's (rule of thumb).
4. Record evidence with IDs: document and revision, record date and shift, gauge ID, setting value, station. A statement that cannot be checked is not evidence.
5. When evidence shows product may be nonconforming, tell the area owner at once so the product is contained, and record it. The auditor does not fix the process.

### C. Write, grade and map the findings

1. Write each nonconformity in three parts: requirement (document, revision, clause), evidence, and the gap in one sentence. One requirement per finding. Name stations and roles, never people. No cause or solution in the finding.
2. Grade each finding and give the reason in one line. The internal scheme is set by local policy. The usual grades follow the IATF certification rules:
   - Major nonconformity (Hauptabweichung): the requirement is not addressed, or the system for it has broken down, or several minors hit one requirement.
   - Minor nonconformity (Nebenabweichung): a single lapse that is not likely to make the system fail.
   - Observation or opportunity for improvement (Verbesserungspotenzial): no requirement is broken.
   - Rules of thumb: grade up when product may reach the customer, when a special characteristic is involved, and for a repeat finding.
3. Map each finding to the most specific IATF 16949 clause and its ISO 9001 base clause with the table in [clause map](references/clause-map.md). If no clause fits, cite the local document as the criterion; never stretch a clause.
4. For every nonconformity, state which product is affected (since the last known-good check) and what must happen to it: hold, re-check or a risk assessment. Any measuring result found invalid needs a review of the results and product since it became invalid, for example an overdue gauge (7.1.5.2.1).
5. Record conforming points of good practice as well (fair presentation).
6. Closing meeting: present the findings, note any the area does not accept, and agree the response deadlines (set by local policy or the customer).

### D. Score a rated questionnaire (VDA 6.3 style)

1. Each rated question has 10, 8, 6, 4 or 0 points. Apply the 2/3 rule: an element, sub-element or process step with fewer than 2/3 of its questions rated is left out of the result.
2. Fulfilment % = points achieved ÷ (questions rated × 10) × 100. Worked example (invented round numbers): 20 questions, 18 at 10, 1 at 8, 1 starred question at 4 → 192 ÷ 200 × 100 = 96%.
3. Classify by the percentage, then apply the downgrading rules. A question at 0, or a starred (*) question with low points, lowers the class whatever the percentage; in the example a starred question scored 4 or less rules out an A under one OEM supplement. The exact triggers and bands depend on the edition and the customer: confirm them ([process audit](references/process-audit.md)).
4. Every question below 10 points becomes a finding with an action, zeros and starred questions first (rule of thumb).

### E. LPA programme and SFM self-audit

1. LPA programme: set layers, roles, frequency, checklist rules and the schedule in `assets/lpa-programme.md`; compute schedule adherence, first-time conformance, repeat Nos and days to close; review the programme itself (who audits, Nos booked as Yes, repeat Nos without problem solving). Details in [layered audit programme](references/layered-audit-programme.md).
2. SFM self-audit: observe real meetings with `assets/sfm-audit-sheet.md`, score each of the five areas as Yes ÷ (Yes + No) × 100, and report each area on its own. Details in [SFM self-audit](references/sfm-self-audit.md).

### F. Follow up

1. For each nonconformity, propose three actions: a correction or containment, a root-cause step and a corrective action.
   - Give each an owner. Use a role when no name is known.
   - Give each a due date: the user's, one tied to a known deadline, or a proposed date marked as a proposal.
   - Leave no action blank. While the root cause is open, name a candidate corrective action on the process, marked "to be confirmed by the root cause".
   - The area confirms or replaces them.
2. The root-cause step asks why the process allowed the gap (no approval route, no reminder, no error-proofing, an unclear standard); a person is never the final cause.
3. Route the root cause: repeat, customer or safety-related findings to `solve-8d`; a single-cause gap to `solve-5why`; many possible causes to `solve-fishbone`.
4. Close a finding only after its effectiveness is verified on evidence: records of the next shifts, a follow-up audit, or a re-check at the station. "Action done" is not closed.
5. Raise the audit frequency for the area after major findings or complaints (9.2.2.1) and feed the results to management review.

## Validation

Check before answering:

1. The auditor is qualified and independent of the area, and the audit covered every shift in scope and a handover.
2. Every nonconformity has requirement, evidence and gap, names no person, and holds no cause or solution.
3. Every finding has a grade with a reason and a clause, or a local document as criterion.
4. Every nonconformity says which product is affected and what happens to it.
5. A score applies the 2/3 rule and the downgrading rules; the class is not taken from the percentage alone.
6. Every action has an owner and a due date, and closure needs verified effectiveness.
7. No finding, score or clause wording was invented; numbers are the user's, cited, or labelled as rule of thumb or set by local policy.

## Output

- Plan: `assets/audit-plan.md` and `assets/audit-checklist.md`, filled in.
- Write-up: `assets/audit-report.md`: the summary first (result, counts by grade, product contained), then the findings table, the good practice, and the response table with owners and dates.
- Scored audit: the points, percentage, class after downgrading and the reason, then the findings.
- LPA programme: `assets/lpa-programme.md`; SFM self-audit: `assets/sfm-audit-sheet.md` with the scores and the top gaps.
- Write for the user in plain words; never cite this skill's step numbers, section names or file names.

## Pitfalls

1. The auditor audits their own area, or only one shift (fix: steps A2, A3).
2. Findings with no evidence, or written as blame of a person (fix: steps B4, C1).
3. A gap is written up, but the product it may have affected is left alone (fix: step C4).
4. A clause is stretched to fit, or cited from memory with invented wording (fix: step C3).
5. A VDA 6.3 class read from the percentage alone, ignoring the downgrading rules (fix: step D3).
6. A programme whose first-time conformance counts corrected Nos as conforming, so the result reads 100% (fix: step E1).
7. Findings closed when the action is reported done, not verified (fix: step F4).

## Hand-offs

- Root causes of repeat, customer or safety-related findings go to `solve-8d`; single-cause gaps to `solve-5why`; unclear causes with many candidates to `solve-fishbone`.
- A control-plan row that is missing, wrong or not linked to the PFMEA goes to `plan-control-plan`; a station instruction that differs from the control plan goes to `plan-workstation-instructions`.
- A reaction plan not followed or a control chart not kept goes to `measure-spc`; maintenance not done as planned goes to `improve-tpm`.
- A weak tier routine found in an SFM self-audit goes to `lead-daily-routine`; an LPA segment inside one walk is planned with `lead-gemba-walk`, and an LPA programme or an audit beyond one walk segment arrives from there.
- Findings that appear on one shift or line only go to `solve-is-is-not`; single improvement cycles from opportunities for improvement go to `solve-pdca`; chronic variation findings go to `solve-dmaic`.
- Effectiveness checks by process audit after a control-plan change, an instruction release or an 8D D6 or D7 arrive from `plan-control-plan`, `plan-workstation-instructions` and `solve-8d`; an audit of reaction-plan use arrives from `measure-spc`; a formal SFM self-audit across areas arrives from `lead-daily-routine`.
