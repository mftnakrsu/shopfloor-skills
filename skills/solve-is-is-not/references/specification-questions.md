# Specification questions

The question pairs for each dimension of the Is/Is-Not, how to pick a good Is-Not, and how to write distinctions and changes. Question set after the Kepner-Tregoe process cards, in our own words.

## Deviation statement

- Object: the thing or group of things with the problem (part number, variant, assembly, machine).
- Defect: what is wrong with it, against which requirement (drawing, specification, standard).
- One line, as found. "Front-face scratches on powder-coated panels" is a deviation; "scratches caused by the racks" already holds a cause.

## Question pairs

| Dimension | Is | Is-Not: could be, but is not |
|---|---|---|
| What: object | Which object, part number or variant has the defect? | Which similar object, variant or part number could have it, but does not? |
| What: defect | What exactly is wrong with it? | What other defect could it have, but does not? |
| Where: place | On which machine, tool, cavity, line, station or location is the object when the defect is seen, and where is it made? | On which comparable machine, tool, cavity, line or station could it be seen, but is not? |
| Where: on the object | Where on the object is the defect? | Where else on the object could it be, but is not? |
| When: first | When was it first seen (date, shift, lot)? | When could it have been seen first, but was not? |
| When: pattern | When since then? Every shift, start-up only, after set-up, one day of the week? | When could it have been seen since, but was not? |
| When: life cycle | At which step of the flow or life of the object is it first seen (after moulding, after machining, at test, in the field)? | At which earlier or later step could it be seen, but is not? |
| Extent: units | How many objects have it, out of how many? | How many could have it, but do not? |
| Extent: size | How big is one defect; how many defects per unit? | What other size or count could it be, but is not? |
| Extent: trend | Is it growing, steady, falling or cyclic? | What could the trend be, but is not? |

Ask the "when" questions also in relation to other events: during start-up, after a tool change, after a maintenance stop. A date alone often hides the pattern (Kepner-Tregoe blog).

Who is involved (shift, crew) is recorded as a place or time fact, never to assign blame (AHRQ).

## Choosing the Is-Not

1. Take the closest comparable item: the sister machine, the other cavity, the related variant, the same line before the start date, the other side of the part.
2. It must be free of the defect, or show it at the normal base rate. Write that rate.
3. It is not the negation of the Is. "Not defective" or "good parts" gives nothing to compare (Kepner-Tregoe blog).
4. The more closely the Is-Not resembles the Is, the fewer distinctions remain, and the sharper the test.
5. Rule of thumb: start testing only with at least one real Is-Not pair in each dimension; list the empty ones as open questions.

## Writing distinctions

- A distinction is true only of the Is side. Write it as something measurable or nameable, for example (invented): tool 7C, programme rev. 4, lot 1120, 2 mm from the gate, first shift after a weekend stop.
- "Is different", "behaves differently" or a bare measurement is not a distinction; it gives no change to search for (Kepner-Tregoe blog).
- Ask also what is odd or unusual about the Is side, even if it seems unrelated.

## Finding changes

For each distinction ask what changed in, on, around or about it, and write the date and the scope (which machines, lines or lots it applies to).

Typical changes to ask about:

- Material: new lot, supplier, grade, storage or drying.
- Machine and tool: repair, replacement part, regrind, new tool, moved equipment, new programme or parameter.
- Method: revised instruction, new sequence, new fixture, changed check.
- Measurement: new gauge, recalibration, new limit or new inspector.
- People and organisation: new crew, shift pattern, overtime.
- Environment: season, temperature, humidity, new building section.

A change whose date comes after the first defect cannot have started it. A change that applies equally to the Is and the Is-Not side cannot explain the difference between them on its own.

## Sources

- Kepner-Tregoe: [Analytic troubleshooting process cards, 2025](https://kepner-tregoe.com/wp-content/uploads/2025/08/Updated-ATS-Process-Cards.pdf)
- Kepner-Tregoe: [8D: is or is not, that is the question](https://kepner-tregoe.com/blogs/8d-is-or-is-not-that-is-the-question/)
- AHRQ: [Kepner-Tregoe matrix, workflow assessment toolkit](https://digital.ahrq.gov/health-it-tools-and-resources/evaluation-resources/workflow-assessment-health-it-toolkit/all-workflow-tools/kepner-tregoe-matrix)
- Virginia Tech, Schaffer and McQuain: [Kepner-Tregoe course notes](https://courses.cs.vt.edu/cs2104/Fall13/notes/KTNotes3.pdf)
