# Root-cause verification

The three root causes an 8D needs, how to prove each one, what to ask when the answer is "human error", and how to judge the strength of an action.

## Three root causes

| Cause | Question | Example (invented) |
|---|---|---|
| Occurrence (why made) | Why was the defect produced? | The nut feeder jams and the welder runs without a nut. |
| Escape (why not detected) | Why did no control catch it before the customer? The escape point is the first control after the cause that should have caught it. | The presence sensor at the next station was bypassed after a fault. |
| Systemic (why the system allowed it) | Which design, planning or management system let both happen? | The PFMEA rated detection as good although the sensor had no daily check in the control plan. |

Each level needs its own action (Creation Technologies; Wikipedia; Siemens). A restated defect ("the nut was missing") is not a cause.

## On/off verification

A cause is verified when you can make the defect appear with the cause present and disappear with it removed (Siemens; Creation Technologies).

1. State the cause as a testable condition, for example "feeder jam with welder running".
2. On: create the condition under control, on a trial or with sample parts, and show the defect occurs.
3. Off: remove the condition and show the defect does not occur.
4. Repeat enough times to rule out chance (number set by local policy).
5. For the escape cause, run the same test on the control with known bad parts or a challenge part: with the suspected condition present, the check misses a known bad part; with the condition removed or restored, it catches it. Showing that the fixed check catches it belongs to D5.
6. Where a destructive or safety-relevant reproduction is not allowed, use data instead: the defect appears only in the lots, times or stations where the cause was present (Is/Is-Not).

Record the test conditions, counts and dates as evidence.

## When the answer is "human error"

Operator error is not accepted as a root cause (Creation Technologies). The person is where the error showed; the cause is what made the error possible or likely. Ask:

1. Could the step be done wrong without anything stopping it? (no error-proofing)
2. Is the instruction clear, current, at the station and in the operator's language?
3. Can the operator see and reach the part and the component easily? (ergonomics, lighting, layout)
4. Was the operator interrupted, rushed or doing several tasks? (distraction, workload, takt)
5. Was the operator trained and released for this station, and how is that checked?
6. Was anything different that day: new person, new variant, changed material, shift change?
7. Why did the next check not catch it? (this is the escape cause)

Keep asking why until the answer is a condition of the process, not of a person.

## Action strength

Rule of thumb, adapted to the line from the action hierarchy used in patient safety (VA National Center for Patient Safety, used in IHI RCA2) and from supplier guidance. Stronger actions depend less on people remembering.

| Strength | Action type | Example on the line |
|---|---|---|
| Strongest | Make the error impossible | A fixture that will not close without the component; a design change that removes the step |
| Strong | Detect at the source and stop | A sensor that stops the cycle when the component is missing (error-proofing, IATF 16949 10.2.4) |
| Medium | Detect later, automatically | An automated end-of-line check with a challenge part tested every shift |
| Weak | Standardise and remind | A revised instruction, a checklist, visual aids |
| Weakest | Train, warn or inspect by hand | Retraining, an awareness notice, an extra visual inspection |

- Retraining, reminders to follow the procedure or disciplinary action alone are not accepted as corrective actions (Creation Technologies). Supplier worked examples rate retraining as almost no benefit and error-proofing as highly effective (Keysight). RCA2 treats training and new procedures as weaker actions.
- Training is still part of rolling out a stronger action, never the action on its own.
- An error-proofing device needs a test frequency in the control plan, a challenge part and a reaction plan for failure (IATF 16949 10.2.4).

## Sources

- Wikipedia: [Eight disciplines problem solving](https://en.wikipedia.org/wiki/Eight_disciplines_problem_solving)
- Siemens: [8D report](https://www.siemens.com/en-us/technology/8d-report/)
- Creation Technologies: [8D supplier training, 2022](https://www.creationtech.com/wp-content/uploads/2022/09/8D-Supplier-Training-9-22-22.pdf)
- Keysight: [Root cause and corrective action guideline for suppliers](https://about.keysight.com/en/supplier/KeysightRCCA_Guideline.pdf)
- CMPA: [Action hierarchy tool](https://www.cmpa-acpm.ca/static-assets/pdf/education-and-events/workshops/action-hierarchy-tool.pdf), based on VA National Center for Patient Safety root cause analysis tools
- IHI: [RCA2: Improving root cause analyses and actions to prevent harm](https://www.ihi.org/resources/tools/rca2-improving-root-cause-analyses-and-actions-prevent-harm)
- DNV: [IATF 16949:2016 comparison matrix](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf)
