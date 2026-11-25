# Seven consistency checks

Run all seven on every draft and every review. Each check compares the station document with the control plan (and, for check 5, the PFMEA) for one operation and one revision.

## How to run a check

1. Put the control-plan rows for the operation next to the document's check rows.
2. Compare field by field; do not judge whether the control plan is right, only whether the document matches it. A control plan that looks wrong is a separate finding for its owner.
3. For each check write: pass or fail, the finding in one sentence, the clause, the fix, an owner and a date.
4. One failed check means the document is not ready for release.

## The checks

| # | Check | Fails when | Clause | Fix |
|---|---|---|---|---|
| 1 | Coverage both ways | a control-plan row for the operation is missing from the document, or the document has a check with no row | 8.5.1.1, VDA 6.3 P6.2.1 | add the missing row; for an orphan check, add it to the control plan or remove it |
| 2 | Special characteristics | a symbol is missing, or differs from the control plan or the customer's symbol | 8.3.3.3 (SI 6) | copy the symbol from the control plan |
| 3 | Sample, frequency, reaction | sample size, frequency, set-up or restart checks, or the reaction text differ from the control plan in any way, looser or tighter | 9.1.1.1, 8.5.1.1 | copy the control-plan text; if the station needs a different value, raise a control-plan change first |
| 4 | Gauge capability | a gauge has no calibration status, no capability study, or a study that failed or used another method; an attribute or visual check has no attribute study | 7.1.5.1.1, 7.1.5.2.1 | add the reference, or start the study; limits in the measurement capability reference |
| 5 | PFMEA trace | a control-plan detection control has no PFMEA detection control, or a high action-priority PFMEA item has no control-plan control | 8.5.1.1 (linkage to PFMEA) | send the gap to the control-plan and PFMEA owners |
| 6 | Error-proofing | a device has no verification step, no challenge-part ID, no frequency, or no reaction if it fails | 10.2.4 | add the check from the control-plan test frequency |
| 7 | Revision | the document is based on an older control-plan or PFMEA revision than the current one | 8.5.1.1 review triggers, 7.5.3 | re-derive from the current revision, then retrain |

## Why a station may not deviate

- The control plan is the basis for release of product (8.6.1) and the auditor checks that the plan is followed at the station (9.1.1.1, VDA 6.3 P6.2.1). A station document that differs from it fails both.
- Lowering a frequency is a change to the process controls. It goes through the control-plan review: PFMEA check, the evidence (for example capability and defect history), customer approval where the customer requires it, then the control-plan revision, then the station document.
- Until the control plan is changed, the station follows the control plan. A tighter local check is allowed only when the control plan or local policy allows it, and is written in the control plan too, so that both stay identical.

## Other flags while reviewing

- "Inform the supervisor" as the whole reaction: no containment scope, no named role, no record (8.5.1.1, 9.1.1.1).
- Variable characteristic recorded only as OK/NOK (9.1.1.1).
- No set-up or first-off release, no restart rule after a stop (8.5.1.3, 8.5.1.4).
- Attribute sampling that accepts any defect (8.6.6).
- Alternate method in use without its own instruction (8.5.6.1.1).
- One language only, worn or illegible copies, handwritten uncontrolled changes (8.5.1.2, 7.5.3).
- No safety rules or PPE (8.5.1.2).
- Appearance check without an approved limit sample, lighting or a qualified evaluator (8.6.3).

## Worked example (invented)

Control plan row 15.1: torque 8 ± 1 N·m, special characteristic, 100 % by the nutrunner, values stored. Instruction rev. 2 shows the torque check without the symbol and says "check the green lamp".

- Check 1 pass. Check 2 fail: the symbol is missing. Check 3 pass for frequency. Recording: fail, the instruction reduces a stored value to a lamp; add "value stored in the nutrunner controller, read the shift report". Check 4: nutrunner capability study not referenced, to be confirmed. Result: not ready for release.

## Sources

- DNV: [IATF 16949:2016 comparison matrix](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf) (clauses 7.1.5, 8.5.1.1 to 8.5.1.4, 8.5.6.1.1, 8.6, 9.1.1.1, 10.2.4)
- IATF: [Sanctioned Interpretations, Nov 2024](https://www.iatfglobaloversight.org/wp/wp-content/uploads/2024/11/IATF-16949-SIs-Nov-2024.pdf) (SI 6)
- vdiversify: [VDA 6.3 guide](https://www.vdiversify.com/vda-6-3/) (P6.2.1 documents based on the control plan; P6.2.2 restart)
- CIS, University of Tennessee: [Top findings during IATF 16949 transition audits](https://cis.tennessee.edu/top-findings-during-iatf169492016-transition-audits) (MSA also for attribute and visual methods)
- VDA QMC: [Checklisten Robuster Produktionsprozess](https://vda-qmc.de/wp-content/uploads/2023/04/Checklisten-RPP.pdf) (incomplete also means wrongly executed)
