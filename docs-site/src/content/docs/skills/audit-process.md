---
title: audit-process
description: Plans, runs and reports manufacturing process audits, scored VDA 6.3 audits, layered process audit programmes and shopfloor-management self-audits, and follows findings up until they are verified.
---

<span class="status available">available</span>

Plans, runs and reports manufacturing process audits (Prozessaudit, IATF 16949 9.2.2.3), scored VDA 6.3 audits and self-assessments, layered process audit (LPA) programmes and shopfloor-management self-audits (Selbstaudit). This skill owns the LPA programme: its design, layers, checklists, schedule, metrics and review. [`lead-gemba-walk`](/skills/lead-gemba-walk/) owns only the LPA segment done inside one walk.

## Five modes

The skill picks the mode from your request.

| Mode | You give | You get |
|---|---|---|
| Plan | The process and shifts, the control plan, PFMEA and instructions with revisions, the customer's method, and the auditor | An audit plan and a checklist built from the control plan and PFMEA, covering every shift and a handover |
| Write up | The audit notes with records, IDs, values, dates and shifts | A report: summary first, findings as requirement, evidence and gap, each graded and mapped to a clause, the product affected, good practice and a response table |
| Score | The points per question, with starred questions marked | The percentage, the class after the 2/3 and downgrading rules, and the findings |
| LPA programme | Areas, layers, roles, frequencies, checklists and the period's results | The programme, its metrics (schedule adherence, first-time conformance, repeat Nos, days to close) and a review of the programme itself |
| SFM self-audit | Observations of real tier meetings | A score per area and the top gaps |

Writing findings needs the evidence; without audit notes or records, the skill asks for the scope, the criteria and the evidence and stops. It never invents a clause's wording or a customer rule.

## Rules it applies

- The auditor is qualified and does not audit their own area; the audit covers every shift in scope and a handover.
- Each finding holds one requirement, the evidence with IDs and the gap; it names stations and roles, never people, and holds no cause or solution.
- Every nonconformity says which product is affected and what must happen to it.
- A VDA 6.3 class is never read from the percentage alone.
- A finding closes only when its effectiveness is verified on evidence, not when the action is reported done.

## Where the work goes next

Root causes go to [`solve-8d`](/skills/solve-8d/), [`solve-5why`](/skills/solve-5why/), [`solve-fishbone`](/skills/solve-fishbone/), [`solve-is-is-not`](/skills/solve-is-is-not/), [`solve-pdca`](/skills/solve-pdca/) or [`solve-dmaic`](/skills/solve-dmaic/), by the kind of finding. Control-plan gaps go to [`plan-control-plan`](/skills/plan-control-plan/), station documents to [`plan-workstation-instructions`](/skills/plan-workstation-instructions/), reaction plans not followed to [`measure-spc`](/skills/measure-spc/), maintenance not done to [`improve-tpm`](/skills/improve-tpm/), and a weak tier routine to [`lead-daily-routine`](/skills/lead-daily-routine/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: the process audit with VDA 6.3 scoring, the layered audit programme, the SFM self-audit and the clause map, each with its sources.
- `assets/`: an audit plan, a checklist, a report, an LPA programme and an SFM audit sheet.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/audit-process).
