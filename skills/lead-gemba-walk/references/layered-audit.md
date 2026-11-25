# Layered audit

How to build and run the optional layered process audit (LPA) segment of a walk, and how it relates to IATF 16949.

## Contents

- What an LPA is
- Layers and frequency
- Building the checklist
- Running the audit
- LPA metrics
- IATF 16949 pointers
- Sources

## What an LPA is

- A short, scheduled check, done where the work is done, by several layers of management, each at its own frequency. The guideline most used in automotive is AIAG CQI-8 (2nd edition 2014, a paid document; summarised here from public secondary sources).
- It checks process inputs and controls, not finished-product characteristics, and not paperwork for its own sake (EASE).
- Questions are simple yes/no items a non-specialist can answer, and an audit takes about 10–15 minutes (EASE; Tervene).
- Leaders do their own audits. One supplier procedure accepts delegation only in extenuating circumstances (Nexteer).

## Layers and frequency

Frequency is set by local policy or by the customer's specific requirements. Published examples:

| Layer | EASE summary of CQI-8 | Nexteer supplier procedure (rev. 2023) |
|---|---|---|
| 1 | Supervisors, daily | Supervisor or team leader: one operation, line or cell per shift |
| 2 | Engineers and other departments, weekly | Middle management: one line, cell or department per week, chosen at random; checks that layer 1 completes its checklists and closes issues |
| 3 | Plant and site leaders, monthly | Plant or general manager: one line, cell or department per week; checks layer 2 the same way |

Each higher layer also checks that the layer below does its audits and closes its items (Nexteer). Rotating auditors keeps observations sharp (Tervene).

## Building the checklist

- Build it with a cross-functional team, from the control plan, the PFMEA and the quality issues of the area (Nexteer).
- Minimum content in one supplier procedure (Nexteer, paraphrased):
  1. Error-proofing verification records checked, and the devices work.
  2. First-time quality tracked, reported and reacted to.
  3. The operator follows standardized work.
  4. The operator is trained or certified for the job.
- Typical further items (Nexteer, paraphrased): material identified and traceable; nonconforming product segregated; changeover instructions followed; control-plan checks at the right frequency, sample size and form; reaction plans followed when a result is outside its limits; gauges available, numbered and calibrated; preventive maintenance done on schedule; rework done to instruction.
- Keep each checklist short: 10–15 items at most (Tervene); 5–10 inside a gemba walk (rule of thumb), so the walk keeps time for open observation.
- Write each item so that the answer is seen, not told: "the last check entry is within its interval", not "do you do the check?" (rule of thumb).
- After a customer complaint, some customers require an LPA with questions specific to that issue (EASE).

## Running the audit

1. Audit during real work, not when the line is empty (Tervene).
2. Review the records, watch the work, and ask the operator without stopping production (Nexteer).
3. Answer each item Yes or No. Mark what you could not check "not reviewed" (Nexteer).
4. Correct a No at once if it is within your authority, and write down the action and the date. Pass the others to the responsible person and note who was told (Nexteer).
5. If product quality is at risk, the area acts at once. What cannot be corrected at once goes into the corrective-action process and is escalated as needed (Nexteer).
6. Feed Nos back to the PFMEA owner where relevant (Nexteer).
7. A No stays a No in the record even when it was corrected during the audit. First-time conformance counts what was conforming when checked (Nexteer).

## LPA metrics

| Metric | Formula | Worked example (invented round numbers) |
|---|---|---|
| Schedule adherence % | audits done ÷ audits scheduled × 100 | 18 ÷ 20 × 100 = 90% |
| First-time conformance % | items conforming when checked ÷ items checked × 100 | 136 ÷ 160 × 100 = 85% |
| Repeat Nos | items answered No in 2 or more audits of the same area in the period | 3 items |
| Average days to close | sum of days from No to verified closure ÷ number of closed Nos | (2 + 4 + 9) ÷ 3 = 5 days |

"Not reviewed" items are left out of both the numerator and the denominator of first-time conformance.

The trap in the second formula: if the 24 Nos of the example were corrected during the audits and booked as Yes, the score would read 160 ÷ 160 = 100% and hide every problem.

Nexteer tracks schedule adherence and first-time conformance; Tervene adds findings per audit, repeat issues and days to close. Management reviews the results at planned intervals (Nexteer, referring to IATF 16949 9.3).

## IATF 16949 pointers

As of 2026-11-25: IATF 16949:2016 with its sanctioned interpretations. Summaries are in our own words; use the official text and the customer-specific requirements for the binding wording.

- **9.2.2.3 Manufacturing process audit.** Every manufacturing process is audited in each three-year period, on all shifts where it runs, including a sample of the shift handover, and the audit checks the PFMEA and the control plan in use. The standard does not name LPAs, but several automotive customers require them in their specific requirements for this clause (EASE). An LPA feeds the process audit; it does not replace it.
- **8.5.6.1.1 Temporary change of process controls.** Where an alternate control method is in use, its use is reviewed daily. An LPA item, or the tier meeting, can carry that daily review.

## Sources

- AIAG: [CQI-8 Layered Process Audit guideline, 2nd ed. 2014](https://webstore.ansi.org/Standards/AIAG/AIAGCQI2014) (store listing; text not accessed)
- EASE: [Core principles of the CQI-8 layered process audit guideline](https://www.ease.io/blog/core-principles-of-the-cqi-8-layered-process-audit-guideline/)
- EASE: [3 things to know about GM IATF 16949 layered process audit requirements](https://www.ease.io/blog/3-things-to-know-about-gm-iatf-16949-layered-process-audit-requirements/)
- Tervene: [CQI-8 layered process audit guideline](https://tervene.com/blog/cqi-8-layered-process-audit-guideline/)
- Nexteer: [Layered audit process, supplier procedure, rev. May 2023](https://www.nexteer.com/wp-content/uploads/layered_audit-May-2023.pdf)
- GlobalSuite Solutions: [summary of IATF 16949 internal audit types](https://www.globalsuitesolutions.com/?p=123974) (secondary)
- DNV: [IATF 16949:2016 comparison matrix](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf)
