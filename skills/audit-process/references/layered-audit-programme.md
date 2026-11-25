# Layered audit programme

How to design, run and review a layered process audit (LPA) programme across an area or plant: layers, schedule, checklists, metrics and the review of the programme itself. A single LPA segment inside one gemba walk is planned with the gemba-walk skill.

As checked in November 2026: AIAG CQI-8 2nd edition (2014) and the supplier procedure revision cited below are the latest found.

## Contents

- Programme design
- Layers and frequency
- Checklists
- Schedule
- Results and metrics
- Reviewing the programme
- Sources

## Programme design

- An LPA is a short, scheduled yes/no check, done where the work is done, of the process inputs and controls that prevent defects. Several management layers do it, each at its own frequency. The guideline most used in automotive is AIAG CQI-8 (2nd edition 2014, a paid document; summarised here from public secondary sources).
- IATF 16949 does not name LPAs. Some customers require them in their customer-specific requirements for the manufacturing process audit (9.2.2.3) (EASE). An LPA programme feeds the process audit; it does not replace it.
- Define in one procedure: the areas covered, the layers and who sits in each, the frequency per layer, how checklists are built and changed, how Nos are handled, the metrics and who reviews them.

## Layers and frequency

Frequency is set by local policy or by the customer's requirements. Published examples:

| Layer | EASE summary of CQI-8 | Nexteer supplier procedure (rev. 2023) |
|---|---|---|
| 1 | Supervisors, daily | Supervisor or team leader: one operation, line or cell per shift |
| 2 | Engineers and other departments, weekly | Middle management: one line, cell or department per week, chosen at random; checks that layer 1 completes its checklists and closes its issues |
| 3 | Plant and site leaders, monthly | Plant or general manager: one line, cell or department per week; checks layer 2 the same way |

- Leaders do their own audits; one supplier procedure accepts delegation only in extenuating circumstances (Nexteer).
- Rotate auditors across areas so that observations stay sharp (Tervene).

## Checklists

- Build them with a cross-functional team from the control plan, the PFMEA and the quality issues of the area (Nexteer).
- Minimum content in one supplier procedure (Nexteer, paraphrased): error-proofing verified and working; first-time quality tracked and reacted to; standardised work followed; operator trained or certified for the job.
- Typical further items (Nexteer, paraphrased): material identified and traceable; nonconforming product segregated; set-up instructions followed; control-plan checks at the right frequency and sample; reaction plans followed; gauges calibrated; preventive maintenance on schedule; rework to instruction.
- 10–15 items at most per checklist (Tervene); an audit takes about 10 minutes (EASE).
- Write each item so the answer is seen, not told (rule of thumb): "the last check entry is within its interval", not "do you do the check?".
- After a customer complaint, add a question specific to that issue for a set period; some customers require it (EASE).
- Retire an item that has been Yes in every audit for a long period, and replace it with a current risk (rule of thumb; the period is set by local policy).

## Schedule

- Plan the audits per layer for the period ahead, by name and area, so that every area gets each layer at its frequency.
- Count capacity: audits per period = areas × audits per area per period. Worked example (invented round numbers): 6 areas, layer 1 daily on 20 working days = 6 × 20 = 120 layer-1 audits per month.
- Audit during real work, on every shift the area runs (Tervene).

## Results and metrics

| Metric | Formula | Worked example (invented round numbers) |
|---|---|---|
| Schedule adherence % | audits done ÷ audits scheduled × 100 | 54 ÷ 60 × 100 = 90% |
| First-time conformance % | items conforming when checked ÷ items checked × 100 | 360 ÷ 400 × 100 = 90% |
| Repeat Nos | items answered No in 2 or more audits of the same area in the period | 4 items |
| Average days to close | sum of days from No to verified closure ÷ closed Nos | (1 + 3 + 5 + 7) ÷ 4 = 4 days |
| Layer check | higher-layer audits that confirmed the lower layer's checklist was done and its Nos closed ÷ higher-layer audits × 100 | 9 ÷ 10 × 100 = 90% |

- "Not reviewed" items are left out of both parts of first-time conformance.
- A No stays a No even when it was corrected during the audit; first-time conformance counts what was conforming when checked (Nexteer).
- Nexteer tracks schedule adherence and first-time conformance; Tervene adds findings per audit, repeat issues and days to close.

## Reviewing the programme

Audit the programme itself, at a frequency set by local policy:

1. Are the audits done by the named leaders, at their layer and frequency, on all shifts?
2. Is every No either corrected at once or passed to an owner with a date, and are the Nos closed and verified?
3. Do repeat Nos go into structured problem solving instead of being corrected again and again?
4. Does a No feed back to the PFMEA or the control plan where it shows a missing control (Nexteer)?
5. Does a 100% first-time conformance over a long period mean the checklist is too easy, or that Nos were booked as Yes? Check a sample of audits against the station.
6. Are the results reviewed by management at planned intervals (Nexteer, referring to IATF 16949 9.3)?

## Sources

- AIAG: [CQI-8 Layered Process Audit guideline, 2nd ed. 2014](https://webstore.ansi.org/Standards/AIAG/AIAGCQI2014) (store listing; text not accessed)
- EASE: [Core principles of the CQI-8 layered process audit guideline](https://www.ease.io/blog/core-principles-of-the-cqi-8-layered-process-audit-guideline/)
- EASE: [blog post on a customer-specific IATF 16949 layered process audit requirement](https://www.ease.io/blog/3-things-to-know-about-gm-iatf-16949-layered-process-audit-requirements/)
- Tervene: [CQI-8 layered process audit guideline](https://tervene.com/blog/cqi-8-layered-process-audit-guideline/)
- Nexteer: [Layered audit process, supplier procedure, rev. May 2023](https://www.nexteer.com/wp-content/uploads/layered_audit-May-2023.pdf)
