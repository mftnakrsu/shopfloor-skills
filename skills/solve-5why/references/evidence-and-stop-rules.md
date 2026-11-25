# Evidence and stop rules

How to verify each link, when a chain may stop, what to ask when the answer is a person, and how strong an action is.

## Verifying a link

A link "B because C" is verified when facts show that C is present and that C produces B. Record the method, counts, date and who checked it.

| Method | How | Notes |
|---|---|---|
| On/off test | Create C under control and show B appears; remove C and show B does not | The strongest proof for the occurrence root (Nexteer supplier training). Repeat enough to rule out chance (number set by local policy) |
| Challenge test | Run known bad parts or a challenge part through the control, with the suspected condition present and then removed | Proves a detection link |
| Data comparison | B appears where C is present and not where C is absent, by lot, shift, machine, cavity, time | Use when reproduction is destructive, unsafe or too costly |
| Direct observation | C is seen at the station and recorded with a photo, measurement or log entry | Proves C is present, not yet that it causes B |
| Record | A drawing, plan, checklist or log shows C | Proves C exists in the system |

Status rules:

1. Verified: the evidence is recorded.
2. Hypothesis: plausible but not checked. Write the check, the owner and the date. Anything said with "probably", "maybe", "usually" or "I think" starts here.
3. Rejected: facts contradict it. Keep it in the record with the evidence, close its branch and look for another answer.
4. Whys below a hypothesis are hypotheses too. A root cause needs a verified chain from the problem down to it.
5. Where links rest on group opinion, a second team may build a different chain for the same problem (Card). Evidence on each link is what makes the chain repeatable.

## Stop rules

Stop a chain only when all three hold:

1. **Changeable condition.** The answer is a condition of the process, design or management system that the team or a named function can change.
2. **Counterfactual test.** Ask: "If we corrected this, is it likely the problem would still recur?" If yes, it is a contributing factor; keep asking (University of Arizona QA guide). Similar test: "Will correcting this cause prevent recurrence? If not, what is the next level?" (Nexteer supplier training).
3. **Therefore test.** Read the chain from the root back to the problem with "therefore" between the links. Each step must follow from the one below; a step that needs an unstated link is a jump: insert the missing why.

Do not stop at:

- a person ("operator error", or a person's attention, care or memory);
- "no time", "bad luck", "it just happened";
- a restated symptom ("the part was wrong");
- a supplier, another department or the customer, without asking for that party's own chain;
- five whys because the form has five rows. The count is not fixed (LEI); 3 to 7 links are common (University of Arizona QA guide).

Go further only while the answer stays within reach of an action. A root like "the economy" or "physics" has gone too far; step back to the last changeable condition.

## When the answer is a person

The person is where the error showed; the cause is what made the error possible or likely. Ask:

1. Could the step be done wrong without anything stopping or signalling it? (no error-proofing)
2. Is the instruction present, current, clear, in the person's language, and does it name this check?
3. Can the person see and reach the parts easily? (layout, lighting, ergonomics)
4. Was the person interrupted, rushed or doing several tasks? (workload, distraction)
5. Was the person trained and released for this station and variant, and how is that checked?
6. Was anything different that day: new person, new variant, changed material, shift change, instruction revised?
7. Why did the next control not catch it? (this opens or continues the detection leg)

Keep asking until the answer is a condition of the process, not of the person. Several of these deeper causes (confusing procedures, distractions, poor layout, missed steps through poor error-proofing, the need for a better fixture or vision system) are listed in public supplier training as better roots than human error (Nexteer supplier training).

## Action strength

Rule of thumb, adapted from the action hierarchy used in patient safety (IHI RCA2; CMPA) and supplier guidance. Stronger actions depend less on people remembering.

| Strength | Action type | Example (invented) |
|---|---|---|
| Strongest | Make the error impossible | A fixture that cannot close with a part missing |
| Strong | Detect at the source and stop | A sensor that stops the cycle when the condition is present |
| Medium | Detect later, automatically | An automatic check with a challenge part tested every shift |
| Weak | Standardise | A revised instruction, a checklist, a visual aid |
| Weakest | Train, remind or inspect by hand | Retraining, a reminder or awareness notice, an added visual check |

- Supplier worked examples rate retraining and alerts to the operator as almost no benefit and mistake-proofing as highly effective (Keysight). Training and new procedures are weaker actions in RCA2.
- Training is part of rolling out a stronger action, never the action on its own.
- An error-proofing device needs a test frequency (IATF 16949 10.2.4), a challenge part and a reaction plan for its failure (IATF 16949 8.5.1.1 or local practice).
- Verify the effect of each action with evidence (data, records, observation) over a period set by local policy.

## Sources

- LEI: [Lexicon, 5 Whys](https://www.lean.org/lexicon-terms/5-whys/)
- Nexteer Automotive: [3-legged 5 Why supplier training, 2018](https://www.nexteer.com/wp-content/uploads/5-Why-Training-Nexteer-Supplier-Version-17-Sept-18.pdf)
- University of Arizona, Office of Research and Partnerships: [5 Whys root cause analysis guide](https://research.arizona.edu/sites/default/files/2026-07/5-Whys-Procedure.pdf)
- Keysight: [Root cause and corrective action guideline for suppliers](https://about.keysight.com/en/supplier/KeysightRCCA_Guideline.pdf)
- Card, A. J.: [The problem with "5 whys", BMJ Quality & Safety 26(8), 2017](https://qualitysafety.bmj.com/content/early/2016/09/02/bmjqs-2016-005849.full)
- Wikipedia: [Five whys](https://en.wikipedia.org/wiki/Five_whys)
- IHI: [RCA2: Improving root cause analyses and actions to prevent harm](https://www.ihi.org/resources/tools/rca2-improving-root-cause-analyses-and-actions-prevent-harm)
- CMPA: [Action hierarchy tool](https://www.cmpa-acpm.ca/static-assets/pdf/education-and-events/workshops/action-hierarchy-tool.pdf)
- DNV: [IATF 16949:2016 comparison matrix](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf)
