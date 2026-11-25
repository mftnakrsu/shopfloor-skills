# Time model

Which time goes into which bucket under the common OEE conventions, the German terms, and the status of ISO 22400-2.

## Bucket names across conventions

| Concept | Practitioner (Vorne) | Nakajima / TPM | ISO 22400-2 | German usage (VDMA 66412-1 style) |
|---|---|---|---|---|
| Calendar time | All time | — | — | Kalenderzeit |
| Denominator of OEE | Planned production time | Loading time | Planned busy time (PBT) | Planbelegungszeit |
| Running time | Run time | Operating time | Actual production time (APT) | Betriebszeit, Laufzeit |
| Time at ideal rate | Net run time | Net operating time | Planned run time per item × produced quantity (PRI × PQ) | — |
| Good-only time | Fully productive time | Valuable operating time | PRI × good quantity (GQ) | — |
| Speed reference | Ideal cycle time | Ideal or design cycle | PRI, a planned value from the routing | Sollzykluszeit |
| Availability | Run time / PPT | Operating time / loading time | APT / PBT | Verfügbarkeit |
| Performance | Net run time / run time | Net operating time / operating time | Effectiveness = PRI × PQ / APT | Leistungsgrad |
| Quality | Good count / total count | Valuable / net operating time | Quality ratio = GQ / PQ | Qualitätsrate |

Sources: Vorne (oee.com), Wikipedia (OEE), OPC Foundation (ISO 22400 restatement), Fabrico, Teeptrak. The mapping across columns is this project's own; the ISO and VDMA full texts are paywalled and were not read.

## Where the conventions disagree

| Item | Practitioner default | ISO 22400-2 | Effect |
|---|---|---|---|
| Changeover and setup | Inside PPT, availability loss | Inside PBT as setup time, outside APT, so also an availability loss | Same |
| Planned maintenance | Inside PPT, a loss | Planned downtime, outside PBT | ISO availability is higher |
| Speed reference | Ideal (fastest) cycle | Planned run time from the routing | ISO performance is usually higher, because routings carry allowances |
| Rework | Not good | Only first-time good units count | Same |

- In one published shift example, applying the ISO rules instead of the plant's own rules moved OEE from 60.30% to 67.09% (Fabrico). The convention moves the number more than many improvements do.
- TPM practice keeps planned maintenance visible as a loss so it can be reduced; this skill uses that as its default and reports an ISO-style figure alongside when asked.
- In German sources, a reworked part that is conforming afterwards still counts as a bad part (Teeptrak).
- Utilisation (Nutzungsgrad) has more than one definition in German glossaries; state the formula used.

## Rules for a fixed time model

1. Write the convention down once: what is unscheduled, what is a planned break, which planned stops stay inside PPT.
2. Use the same convention on every shift, machine and month; a change of convention breaks the trend line.
3. Set the stop threshold (logged stop versus short stop) by local policy and keep it fixed. One practitioner example logs every stop over 2 minutes as a reason-coded stop (Vorne); any other value, such as 5 minutes, is set by local policy.
4. Keep one ideal cycle time per product, with its source (best demonstrated rate or design rate) and the date it was set.
5. Take planned values (PPT, routing times) from the planning system and actual values from the machine or the log, and say which is which.

## Status of ISO 22400-2 (as of 2026-11-25)

- ISO 22400-2:2014 defines the KPIs for manufacturing operations management, among them availability, effectiveness, quality ratio and the OEE index. Amendment 1:2017 adds energy-management KPIs. BSI lists the combined edition as current and under review.
- A second edition (ISO/DIS 22400-2) is under development to replace the 2014 edition; the ISO catalogue shows the draft approved for registration as a final draft (stage 40.99). No published second edition was found on this date.
- ISO/TR 22400-10:2018 covers data acquisition for the Part 2 formulas (Fabrico).
- Re-check the ISO catalogue before quoting the edition in a customer or audit document.
- The KPI names and formulas above come from public restatements; the clause numbers of the ISO text were not checked, so cite the standard by KPI name, not by clause.

## Sources

- Vorne: [Calculating OEE](https://www.oee.com/calculating-oee/); [TEEP](https://www.oee.com/teep/); [Six big losses](https://www.oee.com/oee-six-big-losses/)
- Wikipedia: [Overall equipment effectiveness](https://en.wikipedia.org/wiki/Overall_equipment_effectiveness)
- OPC Foundation: [OPC UA for Machine Tools, Annex C.2](https://reference.opcfoundation.org/MachineTool/v101/docs/C.2)
- Fabrico: [OEE according to ISO 22400](https://www.fabrico.io/blog/oee-iso-22400/)
- Teeptrak: [OEE-Glossar](https://teeptrak.com/de/oee-glossar/)
- computer-automation.de: [VDMA und DIN definieren MES-Kennzahlen](https://www.computer-automation.de/produktionssoftware/vdma-und-din-definieren-mes-kennzahlen-als-massstab.htm)
- ISO: [ISO/DIS 22400-2, second edition](https://www.iso.org/standard/87563.html); [ISO 22400-2:2014/Amd 1:2017](https://www.iso.org/standard/68295.html)
- BSI: [BS ISO 22400-2:2014+A1:2017](https://knowledge.bsigroup.com/products/automation-systems-and-integration-key-performance-indicators-kpis-for-manufacturing-operations-management-definitions-and-descriptions)
