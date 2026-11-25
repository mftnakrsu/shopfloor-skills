# Control plan to station instruction

Editions and clause numbers as checked in November 2026.

How each field of a station instruction traces back to the control plan and the PFMEA, and which clause drives it. Clause content is summarised in plain words, not quoted.

## Document hierarchy

| Level | Document | Answers | Owner (typical, set by local policy) |
|---|---|---|---|
| 1 | Control plan (Produktionslenkungsplan, PLP) | every process and inspection step, goods receipt to goods issue | quality planning |
| 2 | Inspection plan (Prüfplan) | what, how often, how many, with what, against which limits | quality planning; inside or integrated into level 1 |
| 3 | Inspection instruction (Prüfanweisung) | how one station carries out its checks | quality planning with production |
| 3 | Work instruction (Arbeitsanweisung, standardized work sheet) | the operator's work steps with embedded checks | production engineering |
| 4 | Method sheet ("Prüfmethodenblatt", Messanweisung; meaning set locally) | how one characteristic is measured | metrology or quality |

A lower level never contradicts a higher one. An inspection plan that differs from the control plan is a finding by definition, because it must be part of it (VDA RPP checklist).

## Field map

| Instruction field | Control-plan source | PFMEA source | Driver |
|---|---|---|---|
| Header: part or family designation, change level, operation number and name, line | general data | process item, process step | IATF 16949 Annex A |
| Source line: control-plan number, revision, date; PFMEA revision | revision data | revision | VDA 2: reference by number, revision and date |
| Work step, machine, fixture, tool | process step, machine or device | process work element | 8.5.1.2 |
| Characteristic number and name, product or process | characteristic number, product, process | product and process characteristic, failure cause | 8.5.1.1 |
| Special-characteristic symbol | special-characteristic class | special-characteristic column; customer conversion table | 8.3.3.3 (SI 6) |
| Specification, or attribute criterion plus limit-sample ID | specification or tolerance | requirement from the drawing | 8.6.6 zero defects for attribute sampling |
| Gauge ID or type, capability study reference | evaluation or measurement technique | detection control | 7.1.5.1.1 |
| Sample size and frequency, including set-up, tool change, after a stop | sample size, frequency | occurrence and detection rating | 9.1.1.1, 8.5.1.3, 8.5.1.4 |
| Control method: chart, check sheet, error-proofing check, 100 % | control method | prevention and detection control | 8.5.1.1, 10.2.4 |
| Error-proofing check: device, challenge part, frequency | control method, test frequency | error-proofing method detail | 10.2.4 |
| Reaction: stop, segregate, contain, call, record; owner | reaction plan and its owner | severity drives the escalation level | 8.5.1.1, 9.1.1.1 |
| Recording: values for variable data | control method, records | — | 9.1.1.1 |
| Alternate method | list of approved alternates | alternate controls | 8.5.6.1.1 |
| Safety rules and PPE | — | safety effects where in scope | 8.5.1.2 |
| Limit samples, appearance masters, lighting | measurement technique | detection control | 8.6.3 |
| Languages, approval, training level, change history | — | — | 8.5.1.2, 7.2.2 |

## Worked example (invented)

Control-plan row: 60.3, flange thickness, product, no special class, 9.50 ± 0.20 mm, micrometer M-31, 2 parts at set-up and 2 parts every 4 hours, values on a check sheet, reaction "stop, check parts since last good check, call quality inspector".

Check row in the instruction:

| No. | Check | Gauge and method | How many, how often | OK if | Record | If NOK |
|---|---|---|---|---|---|---|
| 60.3 | Flange thickness | Micrometer M-31, at the three marked points, take the lowest | 2 parts at set-up, then 2 parts every 4 hours | 9.30 to 9.70 mm | Both values on the check sheet | Stop. Mark and set aside all parts since the last good check. Call the quality inspector. Write the event on the sheet |

Every value in the row is copied from the control plan; only the "how to measure" detail is added, and it must match the method used in the capability study for M-31.

## Sources

- VDA QMC: [Checklisten Robuster Produktionsprozess](https://vda-qmc.de/wp-content/uploads/2023/04/Checklisten-RPP.pdf) (PLP content; inspection plans part of the PLP)
- VDA QMC: [VDA 2, 7th revised edition (English)](https://vda-qmc.de/wp-content/uploads/2026/01/VDA-2_Yellow-Volume_7th-edition-2025-1.pdf) (control plan referenced by number, revision, date; reference parts)
- DNV: [IATF 16949:2016 comparison matrix](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf) (clauses 7.1.5.1.1, 8.5.1.1 to 8.5.1.4, 8.5.6.1.1, 8.6.3, 8.6.6, 9.1.1.1, 10.2.4)
- IATF: [Sanctioned Interpretations, Nov 2024](https://www.iatfglobaloversight.org/wp/wp-content/uploads/2024/11/IATF-16949-SIs-Nov-2024.pdf) (SI 6 special characteristics, SI 11 alternates, SI 25 Annex A)
- tacto: [Prüfanweisung](https://www.tacto.ai/de/einkaufer-lexikon/pruefanweisung) (inspection plan against inspection instruction)
