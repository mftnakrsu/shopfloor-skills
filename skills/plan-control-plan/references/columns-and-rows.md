# Columns and rows

What goes in the header, which rows a control plan needs, and the rule for each column. Clause summaries are in our own words.

As of November 2026: IATF 16949:2016 with its sanctioned interpretations (SI compilation of November 2024; the releases of November 2025 and June 2026, checked in their communiqués, do not touch 8.5.1.x) and the AIAG Control Plan manual, 1st edition (2024). Re-check when a new edition appears.

## Header (IATF 16949 Annex A.2 as amended by SI 25)

| Field | Note |
|---|---|
| Control plan number | Unique; station documents cite it with the revision |
| Issue date and revision date | Every revision gets a date and a reason (the trigger) |
| Customer information | As the customer requires |
| Organisation and site | |
| Part numbers or common control plan designation | A family plan uses the common designation and keeps the member list with it |
| Part name or description | |
| Engineering change level | Must match the drawing level in production |
| Phase | Prototype, pre-launch or production; Safe Launch shown as an added status, for example "production / Safe Launch" (AIAG 2024, vendor reading) |
| Key contact | |
| Part or process step number; process name or operation description | Same numbers as the process flow and PFMEA |
| Functional group or area responsible | |

## Where rows come from

| Source | Row it creates |
|---|---|
| PFMEA failure cause with a prevention control | Process-characteristic row (the setting that prevents the cause) |
| PFMEA failure mode with a detection control | Product-characteristic row (the check) |
| Special characteristic (8.3.3.3, SI 6) | Row with the symbol; usually a tighter method or frequency |
| Customer requirement, layout inspection, functional test (8.6.2) | Row at the operation where it is done, with the customer's frequency |
| Set-up, first-off and last-off (8.5.1.3) | Row per operation where set-ups happen, with the release record |
| Restart after planned or unplanned shutdown (8.5.1.4) | Row or a note on the affected rows |
| Error-proofing device (10.2.4) | Row for the device check with the master or challenge part and the frequency |
| Approved alternate control (8.5.6.1.1, SI 11) | Row marked "alternate", pointing to its own instruction |
| Planned rework | Its own operation with its controls (VDA RPP checklist) |

## Column rules

| Column | Rule |
|---|---|
| Characteristic number | Same number as the drawing balloon or PFMEA line |
| Product / process | One of the two; never mix them in one row |
| Class | Customer symbol, or the plant symbol through the conversion table |
| Specification | From the drawing or the process window; for attribute checks, the limit sample or master by ID |
| Measurement technique | Gauge ID or type; the same method that the gauge study used |
| Error-proofing | Device name and what it prevents or detects |
| Sample size and frequency | Number of parts and when: per hour, per lot, per set-up, after tool change, 100 % |
| Control method | SPC chart, check sheet, 100 % test, error-proofing, first-off release |
| Record | Where the result is kept; actual values for variable data (9.1.1.1) |
| Reaction plan | See the reaction-plan wording; with an owner by role (AIAG 2024 adds an owner column, vendor reading) |

## Trace map to the PFMEA and station documents

| Control-plan field | PFMEA field | Station document field |
|---|---|---|
| Operation number and name | Process step | Operation in the header |
| Characteristic and class | Product or process characteristic, special-characteristic mark | Step or inspection row with the symbol |
| Prevention or detection control | Prevention control, detection control | Work step or inspection step |
| Sample size and frequency | Occurrence and detection ratings justify it | Identical sample and frequency |
| Reaction plan | Severity sets how far it escalates | Boxed reaction with the role to call |
| Revision | PFMEA revision | Cites the control-plan revision |

## Sources

- IATF: [IATF 16949 Sanctioned Interpretations, November 2024 (SI 6, SI 11, SI 24, SI 25)](https://www.iatfglobaloversight.org/wp/wp-content/uploads/2024/11/IATF-16949-SIs-Nov-2024.pdf)
- DNV: [IATF 16949:2016 vs ISO/TS 16949:2009 comparison matrix (8.5.1.1, 8.5.1.3, 8.5.1.4, 8.6.2, 9.1.1.1, 10.2.4)](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf)
- IATF: [Stakeholder Communiqué SC-2025-003](https://www.iatfglobaloversight.org/wp/wp-content/uploads/2025/11/IATF-Stakeholder-Communique-SC-2025-003-Release-of-Sanctioned-Interpretations-SIs-and-Frequently-Asked-Questions-FAQs-related-to-Rules-6th-Edition-and-IATF-16949.pdf)
- IATF: [Stakeholder Communiqué SC-2026-004](https://www.iatfglobaloversight.org/wp/wp-content/uploads/2026/06/IATF-Stakeholder-Communique-SC-2026-004-Release-of-Sanctioned-Interpretations-SIs-related-to-Rules-6th-Edition-and-Frequently-Asked-Questions-FAQs-related-to-IATF-16949.pdf)
- PeakAvenue: [New AIAG control plan requirements](https://www.peakavenue.com/news-events/news/detail/new-aiag-control-plan-requirements)
- VDA QMC: [Checklisten Robuster Produktionsprozess](https://vda-qmc.de/wp-content/uploads/2023/04/Checklisten-RPP.pdf)
- Symestic: [Control Plan im Automotive](https://www.symestic.com/de-de/was-ist/control-plan-im-automotive)
