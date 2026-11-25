# Variants and review triggers

Rules for the phases, Safe Launch, family, summary, interlinked and alternate-control plans, and for when a plan must be reviewed. Clause summaries are in our own words.

As of November 2026: IATF 16949:2016 with its sanctioned interpretations; AIAG Control Plan manual, 1st edition (2024), known only through public secondary summaries because the manual is paid; VDA 2, 7th revised edition. Re-check when a new edition appears.

## Phases (IATF 16949 8.5.1.1, Annex A)

| Phase | Purpose | Typical content |
|---|---|---|
| Prototype | Controls while making prototypes | Dimensional checks, material and performance tests the customer requires |
| Pre-launch | Controls after prototype and before production | Extra checks and higher frequencies until the process is proven |
| Production | Controls for series production | The settled rows, frequencies and reaction plans |

IATF 16949 asks for a pre-launch and a production plan. The AIAG manual (2024) adds Safe Launch and treats the plan as a living document. Existing plans need not be reworked to the new manual (DQS).

## Safe Launch

- A temporary layer of extra controls or containment on top of a pre-launch or production plan, to keep defects away from the customer in early production. It is not a phase that follows another (Umbrex).
- For each extra control, record: what it checks, why (which risk or open PFMEA item), its frequency, its reaction, and its exit criteria.
- Exit criteria are agreed with the customer, including who authorises the exit. Elapsed time is not proof of readiness (Umbrex). Typical evidence: a run with no defects found by the extra layer, capability on special characteristics, closed problem-solving items. The numbers are set by the customer or local policy.
- A defect found by the extra layer is an escape from the regular controls. It gets the reaction plan, a cause search, and a change to the regular plan (stronger detection, higher frequency or a new prevention control) before exit.
- At exit, the regular plan carries every change the Safe Launch taught; then the status changes and the extra rows are removed in one revision.

## Family control plans

- Allowed for bulk materials and for similar parts made by a common process (8.5.1.1). Use a common designation and keep the member list (SI 25).
- Use one only where process steps, equipment and controls are really the same; document every exception (Umbrex). Audit findings often name per-part plans that are hard to keep current, so family plans are recommended where they fit (CIS, University of Tennessee).
- A member with an extra step, other tool, other tolerance or other special characteristic gets its own rows or its own plan.

## Summary plans for automated processes (SI 24)

- Where a manufacturing execution system controls the limits, sample size and frequency, summary rows with a direct reference to that system are acceptable.
- The row names the system, the recipe or program and its revision. The reaction plan stays in the control plan.
- For bulk materials, most production detail sits in the batch recipe.

## Interlinked plans

- One product's process may be split across several plans, sites or suppliers. Each plan names the linked plans (AIAG 2024, vendor reading).
- A characteristic made in one plan and only checked in another (pass-through) has its control in the plan where it is made (bhavyamangla.com summary).

## Alternate controls (8.5.6.1.1, SI 11)

- Keep a list of process controls with their approved alternates. Not every control needs one.
- Each alternate has its own instruction, approval based on risk, customer approval where required, daily review while in use, traceability of the parts made under it, and a restart check when the primary control returns.

## Review triggers (8.5.1.1 f to i)

| Trigger | Action |
|---|---|
| Nonconforming product shipped | Review the rows that should have caught it |
| Change to product, process, measurement, logistics, supply source, volume or PFMEA | Review before the change goes live |
| Customer complaint with corrective action | Update with the corrective action (SI 20) |
| Periodic | At a risk-based interval set by local policy |

After a revision, get customer approval where the customer requires it, and update every station document that cites the plan.

## Sources

- DNV: [IATF 16949:2016 vs ISO/TS 16949:2009 comparison matrix (8.5.1.1, 8.5.6.1.1)](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf)
- IATF: [IATF 16949 Sanctioned Interpretations, November 2024 (SI 11, SI 20, SI 24, SI 25)](https://www.iatfglobaloversight.org/wp/wp-content/uploads/2024/11/IATF-16949-SIs-Nov-2024.pdf)
- DQS: [Publication of APQP 3rd edition and Control Plan 1st edition](https://www.dqsglobal.com/en/explore/blog/hk/coming-publication-of-apqp-ed3-and-control-plan-ed1)
- Umbrex: [AIAG control plan framework](https://umbrex.com/resources/frameworks/automotive-mobility-frameworks/aiag-control-plan/)
- PeakAvenue: [New AIAG control plan requirements](https://www.peakavenue.com/news-events/news/detail/new-aiag-control-plan-requirements)
- bhavyamangla.com: [Control Plan 1st Edition 2024](https://bhavyamangla.com/control-plan-1st-edition-2024/)
- CIS, University of Tennessee: [Top findings during IATF 16949:2016 transition audits](https://cis.tennessee.edu/top-findings-during-iatf169492016-transition-audits)
