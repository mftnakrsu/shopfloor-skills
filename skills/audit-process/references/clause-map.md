# Clause map

How to write, grade and map an audit finding, and a map from common shopfloor findings to ISO 9001 and IATF 16949 clauses.

## Contents

- Audit principles
- Writing a finding
- Grading
- Clause map
- Editions
- Sources

## Audit principles

ISO 19011:2018 sets seven principles (summarised in our own words):

1. **Integrity:** work honestly, only within your competence, and stay impartial.
2. **Fair presentation:** report what the audit found, truthfully and completely, including obstacles met and opinions the auditee does not share.
3. **Due professional care:** judge with diligence, in proportion to what is at stake.
4. **Confidentiality:** protect what you learn in the audit.
5. **Independence:** do not audit your own work; for an internal audit, independence means no responsibility for the activity audited and no conflict of interest.
6. **Evidence-based approach:** conclusions rest on verifiable evidence, drawn from a sample that is fit for the purpose.
7. **Risk-based approach:** plan, run and report with the risks and opportunities of the process in mind.

## Writing a finding

ISO 19011 terms: the **audit criteria** are the requirements you audit against; **objective evidence** is what you saw, measured, read or were told and can verify; a **finding** is the result of comparing the two, and shows conformity or nonconformity. Findings can also point to risks, opportunities for improvement or good practice.

Every nonconformity has three parts:

| Part | Content | Example (invented) |
|---|---|---|
| Requirement | the document and its revision, plus the clause | Control plan rev. B, row 12: torque check of 5 parts every hour (IATF 16949 9.1.1.1) |
| Evidence | what was seen, where, when, with IDs | Torque record of station 30, night shift: entries at 22:00 and 02:00 only |
| Gap | what is not met, in one sentence | The torque check was done every 4 hours instead of every hour on the night shift |

Rules:

- One requirement per finding. Several lapses against one requirement go into one finding with each piece of evidence listed.
- State the process gap, never a person's fault. Write stations and roles, not names.
- No cause and no solution in the finding; those belong to the area's response.
- A conforming point that is well done is recorded too (good practice), so the report is fair.

## Grading

The grading scheme for internal audits is set by local policy. Many organisations reuse the certification grades. In the IATF certification rules (summarised from a secondary source):

| Grade | When |
|---|---|
| Major nonconformity | A requirement is not addressed at all, or the system for it has broken down; several minors against one requirement can add up to a major |
| Minor nonconformity | A lapse against a requirement that, on judgement and experience, is not likely to make the system fail; often one observed lapse |
| Observation or opportunity for improvement | No requirement broken, but a risk or a better way is seen |

Rules of thumb for internal grading:

- Raise the grade when nonconforming product may have reached or may reach the customer, or when a special characteristic is involved.
- A repeat of a finding from the last audit is graded at least one level higher.
- State the reason for the grade in one line.

## Clause map

Map each finding to the most specific IATF 16949 clause and to the ISO 9001 clause it supplements. Summaries in our own words; numbering is ISO 9001:2015 and IATF 16949:2016 (DNV matrix for IATF clause titles).

| Finding pattern | ISO 9001 | IATF 16949 | What the clause asks (summary) |
|---|---|---|---|
| Control-plan check skipped, late, wrong sample or not recorded | 8.5.1 | 8.5.1.1, 9.1.1.1 | Checks run as the control plan says, with records, and the reaction plan is used when a result is out |
| PFMEA control missing from the control plan, or the reverse | 8.5.1 | 8.5.1.1, 9.2.2.3 | The control plan is linked to and takes in the PFMEA outputs |
| Setting outside the work instruction, no approved deviation | 8.5.1 | 8.5.1.2, 8.5.6.1.1 | Work is done to the standard; a temporary alternate control needs approval, its own instruction and daily review |
| Instruction missing, outdated or not at the station | 7.5.3, 8.5.1 | 8.5.1.2 | Current, legible instructions at the work station, in the operators' language |
| Set-up or first-off release missing | 8.5.1 | 8.5.1.3 | Set-ups are verified and released, with records |
| No restart check after a stop | 8.5.1 | 8.5.1.4 | Product is verified after a planned or unplanned shutdown |
| Maintenance or tool change not done as planned | 7.1.3 | 8.5.1.5, 8.5.1.6 | Planned maintenance and tool management run as defined |
| Gauge overdue for calibration, or no capability study | 7.1.5.1, 7.1.5.2 | 7.1.5.1.1, 7.1.5.2.1 | Gauges are calibrated and capable; when one is found out of calibration, its earlier results and the product checked with it are assessed |
| Operator not qualified on the matrix | 7.2 | 7.2.2 | People are competent for the job, with on-the-job training |
| Parts or containers not identified, traceability broken | 8.5.2 | 8.5.2.1 | Product is identified and traceable as defined |
| Suspect or nonconforming parts not segregated | 8.7 | 8.7.1.3, 8.7.1.7 | Unidentified or suspect product is treated as nonconforming and segregated; disposition is controlled |
| Rework without instruction | 8.7 | 8.7.1.4 | Rework follows an approved instruction, with records |
| Error-proofing not tested at the stated frequency, challenge part uncontrolled | 8.5.1 | 10.2.4 | Error-proofing devices are tested for failure at the control-plan frequency; challenge parts are identified and controlled |
| Storage, FIFO or packaging not as defined | 8.5.4 | 8.5.4.1 | Product is preserved; stock is rotated and its condition checked |
| Disorder or dirt that affects the product | 7.1.4 | 7.1.4.1 | The plant is kept in order, clean and in repair |
| Shift handover does not pass on process changes or problems | local requirement | local requirement | No clause sets the handover's content; 9.2.2.3 only makes the audit sample it. State the local handover standard (document and revision) as the criterion |
| Corrective action closed without effect, or problem recurs | 10.2 | 10.2.3 | Problems are solved with root cause, containment, verified actions and updated documents |
| Auditor audits own area, or is not qualified | 9.2.2 | 7.2.3 | Auditors are objective and impartial, and on the list of qualified auditors |

When no clause fits, state the local requirement (document and revision) as the criterion. Never stretch a clause to cover a finding.

## Editions

As checked in November 2026:

- IATF 16949:2016 with its sanctioned interpretations is the auditable edition; a second edition is planned for about mid-2027 (Smithers).
- ISO 9001:2026 was published in September 2026, with a three-year transition (DNV). IATF 16949:2016 is built on ISO 9001:2015, so this map uses the 2015 numbers. Check the 2026 numbering before citing it.
- The IATF certification rules are in their 6th edition, in force since 1 January 2025 (LRQA).

## Sources

- ISO: [ISO 19011:2018 public preview](https://cdn.standards.iteh.ai/samples/70017/7df30d6d9f6243f9888896f5926931cb/ISO-19011-2018.pdf)
- Wikipedia: [ISO 19011](https://en.wikipedia.org/wiki/ISO_19011)
- DNV: [IATF 16949:2016 comparison matrix](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf)
- Advisera: [Definitions of the audit findings (expert answer citing IATF Rules, 5th ed.)](https://community.advisera.com/topic/definitions-of-the-audit-findings/)
- LRQA: [Understanding the IATF 16949 Rules 6th edition](https://www.lrqa.com/en-gb/latest-news/understanding-iatf-16949-6th-edition/)
- Smithers: [IATF 16949 second edition update](https://www.smithers.com/resources/2026/august/iatf-16949-second-edition-update)
- DNV: [New edition of ISO 9001 released](https://www.dnv.com/news/2026/new-edition-of-the-quality-management-system-standard-iso-9001-released/)
