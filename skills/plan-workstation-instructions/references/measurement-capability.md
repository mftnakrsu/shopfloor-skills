# Measurement capability for station gauges

Editions and limits as checked in November 2026.

What evidence a gauge named in a station document needs, and the default limits. The customer's requirements and local policy override every default here; ask for them.

## What is required

- Every type of measurement and inspection system named in the control plan needs a statistical study of its variation, attribute and visual methods included (IATF 16949 7.1.5.1.1). Gauges of one family with the same range, resolution and repeatability may share a representative study (IATF FAQ 6).
- Every gauge needs a calibration record and ID (7.1.5.2.1).
- The study must use the measuring method of the station: same fixture, points, sequence and conditions. If the method sheet changes the method, the study must be repeated.
- For critical characteristics (safety or approval relevant), VDA 5 (3rd edition, 2021) expects continuing proof of suitability, not only a one-off study; calibration alone does not show it.

## VDA 5 ratios

- Resolution first: %RE = resolution ÷ tolerance × 100 %. Default limit 5 % (VDA 5, 2010 revision; check the current customer requirement).
- Measurement system: Q_MS = 2 × U_MS ÷ T × 100 %, with U_MS the expanded uncertainty of the measuring system and T the tolerance width. Default limit 15 % (VDA recommendation, 2010 revision); company limits between 15 % and 20 % are seen (Dietrich).
- Measurement process: Q_MP = 2 × U_MP ÷ T × 100 %, with U_MP the expanded uncertainty of the whole process at the station (operators, part, temperature, stability). Default limit 30 %; 20 % for high requirements (VDA 5, 2021, as shown in the VDA QMC article).
- Smallest testable tolerance: T_min = 2 × U_MP ÷ Q_MP,max.

## AIAG MSA ratio

- %GRR against tolerance or process variation: below 10 % capable, 10 % to 30 % conditionally capable, 30 % or more not capable (common guideline values, via Dietrich). Which method applies is set by the customer.

## Worked example (invented)

Tolerance 20.00 ± 0.20 mm, so T = 0.40 mm. Gauge resolution 0.001 mm; U_MS = 0.025 mm; U_MP = 0.05 mm.

- %RE = 0.001 ÷ 0.40 = 0.25 %: below 5 %, pass.
- Q_MS = 2 × 0.025 ÷ 0.40 = 12.5 %: below 15 %, pass.
- Q_MP = 2 × 0.05 ÷ 0.40 = 25 %: below 30 %, suitable; above 20 %, so not suitable where high requirements apply.
- T_min = 2 × 0.05 ÷ 0.30 = 0.33 mm: the process cannot verify a tolerance narrower than this.

## Attribute checks

- Attribute and visual checks need an attribute study (agreement between inspectors and with the reference), limit samples with IDs, and for appearance items defined lighting and qualified evaluators (8.6.3).
- Attribute sampling accepts zero defects (8.6.6).

## In the station document

Write next to each gauge: ID, calibration due status, study reference, the ratio and its result. If any is missing, mark it "to be confirmed" and fail consistency check 4.

## Sources

- VDA QMC: [White Paper VDA 5 (2024)](https://vda-qmc.de/wp-content/uploads/2024/03/White-Paper-Standard-VDA-5-24.pdf) (3rd edition, July 2021)
- VDA QMC: [Press report 2011, revised VDA 5](https://vda-qmc.de/wp-content/uploads/2024/02/Pressebericht-2011-QZ-Messsystem-und-Messprozess-sind-zweierlei-Ueberarbeiteter-VDA-Band-5-–-Pruefprozesseignung.pdf) (resolution below 5 %, Q_MS 15 %, Q_MP 30 %)
- VDA QMC: [QZ 2024, Regelmäßig und geeignet](https://vda-qmc.de/wp-content/uploads/2024/06/2024-QZ-VDA-QMC-Regelmaessig-und-geeignet.pdf) (Q_MP below 30 % suitable, below 20 % for high requirements; continuing suitability)
- Dietrich, E.: [Eignungsnachweis von Mess- und Prüfprozessen, 6th ed., excerpt](https://www.beam-shop.de/media/pdf/9f/3c/d0/9783446478886_01003daa-fb55-454f-8c4a-0bfa4426d8d7.pdf) (Q = 2U/T; company ranges; %GRR guideline values)
- IATF: [FAQs, May 2022](https://www.iatfglobaloversight.org/wp/wp-content/uploads/2022/05/IATF-16949-FAQs_May-2022.pdf) (FAQ 6 gauge families)
- DNV: [IATF 16949:2016 comparison matrix](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf) (7.1.5.1.1, 7.1.5.2.1, 8.6.3, 8.6.6)
