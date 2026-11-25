# D0–D8 gates

What each discipline must achieve, the steps, the exit gate and the evidence to attach before the 8D moves on.

## Contents

- How the disciplines are named
- D0 Plan and emergency response
- D1 Team
- D2 Problem description
- D3 Containment
- D4 Root cause
- D5 Choose and verify permanent actions
- D6 Implement and validate
- D7 Prevent recurrence
- D8 Close and recognise the team
- IATF 16949 pointers
- Sources

## How the disciplines are named

Sources agree on the content and differ on the labels.

| Step | Global 8D, as summarised publicly | VDA 8D reporting |
|---|---|---|
| D0 | Prepare, emergency response actions, decide whether a full 8D is needed | — |
| D1 | Use a team | Team |
| D2 | Describe the problem | Problem description |
| D3 | Interim containment | Immediate measures (Sofortmaßnahmen) |
| D4 | Root causes and escape point | Failure causes (Fehlerursachen) |
| D5 | Verify permanent corrections | Planned corrective measures |
| D6 | Implement and validate | Implemented corrective measures |
| D7 | Prevent recurrence | Prevent a repeat of the failure |
| D8 | Congratulate the team | Acknowledge the team's success |

(Wikipedia; VDA QMC 2017.) The customer's own format wins where it prescribes one (IATF 16949 10.2.3).

## D0 Plan and emergency response

- **Purpose:** protect the customer and people before the analysis starts, and decide whether an 8D is the right tool. The gateway step comes from Global 8D (Wikipedia).
- **Steps:**
  1. Record the symptom as reported.
  2. If safety or the customer is at risk, act at once: stop shipment, hold stock, inform the customer as their requirements say.
  3. Decide: an 8D is needed for a customer complaint, a field failure, a safety or legal topic, a repeat problem, or a local criterion (set by local policy or customer requirement).
  4. Note the customer's response times and report format.
- **Gate:** emergency actions are in place or not needed, and the decision to run an 8D is recorded.
- **Evidence:** the complaint record, the hold or stop instruction, the customer notification.

## D1 Team

- **Purpose:** a small cross-functional team that knows the product and process. "Not a team of one" (Creation Technologies).
- **Steps:** name a leader who runs the 8D and a champion with authority over resources. Add people from the process: production, quality, engineering, maintenance, and the operators of the stations involved.
- **Gate:** leader, champion and members are named, with roles.
- **Evidence:** the team list.

## D2 Problem description

- **Purpose:** a factual, quantified statement that the whole team agrees on (Wikipedia: 5W2H).
- **Steps:**
  1. What: part number, defect, requirement broken (drawing, specification, boundary sample).
  2. Where: on the part, and where it was found (customer line, incoming, field).
  3. When: date found, production date or lot, delivery date.
  4. How many: quantity found defective out of quantity checked or delivered.
  5. How detected: who found it and with which check.
  6. Is/Is-Not: compare where the defect is and is not seen, by part, lot, line, shift and time.
  7. If the customer's description differs from yours, record both (Creation Technologies).
- **Gate:** the statement is quantified and contains no cause and no solution.
- **Evidence:** photos or the returned sample, the customer's report, the Is/Is-Not table.

Example (invented round numbers): "Customer found 10 of 1,000 brackets (part X-1) from lot 100, delivered on 1 March, with a missing weld nut on the left flange; found at the customer's assembly line by a fit check." The sentence names no cause.

## D3 Containment

- **Purpose:** stop suspect product reaching the customer until the permanent fix works. Containment is visible and temporary (Quality Magazine).
- **Steps:**
  1. List every suspect location: customer stock, in transit, finished goods, work in process, incoming or supplier stock, service parts. Sources list the same scope: customer, in transit and in-house (Siemens); production, finished goods, customer on hand, incoming and warehouse (Keysight).
  2. Sort backwards from the shipping dock to the station where the defect arises (Creation Technologies).
  3. Choose a sort method proven able to detect the defect: test it on known bad parts first. Never sort with the check that already missed it.
  4. Mark the defective and the certified parts differently, and set the clean point: the first good part, lot, serial number or date code (Creation Technologies).
  5. Give each action an owner, a due date, the evidence it needs and its end condition (a blog post on supplier quality).
  6. Report found counts per location to the customer.
- **Gate:** every location is sorted or blocked, the customer is protected, and containment is verified.
- **How to verify containment:** the sort method found the known bad parts; no new defect is reported from shipments after the clean point; an extra audit on certified parts finds none (audit size set by local policy).
- **Evidence:** the filled containment plan with counts per location, the sort instruction, the marking, the clean-point record.

## D4 Root cause

- **Purpose:** find and verify why the defect was made and why it was not detected (Siemens; Wikipedia: escape point).
- **Steps:**
  1. Occurrence: why the defect was made. Ask what changed: machine, material, method, people, supplier, instruction, shift, drawing, gauge (Creation Technologies).
  2. Escape: why it was not detected. Find the escape point, the first control after the cause that should have caught it (Wikipedia).
  3. Systemic: why the system allowed both, for example a PFMEA that rated the risk low or a control plan without an error-proofing check.
  4. Verify each cause on and off (see the root-cause verification reference).
- **Gate:** the occurrence and escape causes are both verified with evidence. "Operator error" is not accepted as a final cause.
- **Evidence:** the 5-why or fishbone, the Is/Is-Not, the on/off test records.

## D5 Choose and verify permanent actions

- **Purpose:** one permanent action per root cause, proven before rollout (Wikipedia; Siemens).
- **Steps:**
  1. For each cause, list options and choose by strength: make the error impossible, then detect it at the source, and only then add training or inspection.
  2. Verify on a trial: the action removes the cause, and the defect cannot be reproduced.
  3. Check that it creates no new risk: review the PFMEA for the changed step (Siemens).
  4. Agree the actions with the customer where required.
- **Gate:** verification evidence for each action.
- **Evidence:** trial results, the PFMEA review, the customer's agreement where needed.

## D6 Implement and validate

- **Purpose:** put the actions into production and prove they work there (Wikipedia).
- **Steps:**
  1. Implement through change control, with owner and date per action.
  2. Validate against the D2 measure over a period or quantity set by local policy or the customer.
  3. Remove containment only after validation, and record when and on whose approval.
- **Gate:** validation evidence, and containment ended with a record.
- **Evidence:** production data after the change, the error-proofing check records, the containment-end record.

## D7 Prevent recurrence

- **Purpose:** change the system so this and similar problems do not recur (Wikipedia; IATF 16949 SI 20).
- **Steps:**
  1. Update the PFMEA, control plan, station instructions, maintenance plans and error-proofing check frequencies.
  2. Read across: check similar parts, lines and plants for the same cause and apply the action there.
  3. Record the lesson learned where future projects will find it.
- **Gate:** the document revisions are listed with numbers and dates.
- **Evidence:** the revised documents, the read-across list with results.

## D8 Close and recognise the team

- **Purpose:** formal closure and thanks.
- **Steps:** run the closure checklist; get the customer's closure confirmation where required, since some customers close only when they sign off (Creation Technologies); recognise the team; archive the 8D.
- **Gate:** checklist complete, closure confirmed where required.
- **Evidence:** the signed 8D report.

## IATF 16949 pointers

As of 2026-11-25: IATF 16949:2016 with the sanctioned interpretations of November 2024. The summaries are in our own words; use the official text for audits.

- **10.2.3 Problem solving:** the plant needs a written way of solving problems so that they do not come back (SI 20). In practice, for an 8D:
  - Define an approach for each type and scale of problem, for example new-product issues, current production, field failures and audit findings (item a).
  - Protect the customer first with containment (item b), then find and record the causes and how you found them (item c).
  - Fix the system, not only the part, and carry the fix over to similar products and processes (item d).
  - Prove that the actions work (item e) and bring the PFMEA, control plan and other documents up to date (item f).
  - If the customer prescribes its own method or form, use it.
- **10.2.4 Error-proofing:** decide and record where error-proofing is used (PFMEA); test each device at the control-plan frequency with a challenge part (verified and calibrated where feasible) and keep records; react when a device fails.
- **10.2.6 Customer complaints and field failures:** analyse complaints and returned parts, including how the product's embedded software works in the customer's system where the customer requests it; start problem solving and corrective action, and report the results to the customer and inside the organization.
- **SI 20:** reworded 10.2.3 so that prevention of recurrence is required, because corrective actions often skipped it.

## Sources

- Wikipedia: [Eight disciplines problem solving](https://en.wikipedia.org/wiki/Eight_disciplines_problem_solving)
- Siemens: [8D report](https://www.siemens.com/en-us/technology/8d-report/)
- VDA QMC: *Definition of Failure Cause Categories for 8D Reporting* V1.0, 2017, free download. [PDF](https://vda-qmc.de/wp-content/uploads/2023/01/VDA_Volume_8D__V1.0__EN__English.pdf). VDA QMC: *8D – Problem Solving in 8 Disciplines*, 1st ed., 2018. [Shop listing](https://webshop.vda.de/QMC/en/8d-problem-solving-in-8-disciplines)
- AIAG: CQI-20 *Effective Problem Solving*, 2nd ed., 2018. [Listing](https://aiag.org/quality/shop-floor-quality/problem-solving)
- Creation Technologies: [8D supplier training, 2022](https://www.creationtech.com/wp-content/uploads/2022/09/8D-Supplier-Training-9-22-22.pdf)
- Keysight: [Root cause and corrective action guideline for suppliers](https://about.keysight.com/en/supplier/KeysightRCCA_Guideline.pdf)
- Quality Magazine: [Key strategies for effective problem solving](https://www.qualitymag.com/blogs/14-quality-blog/post/88658-quality-observations-key-strategies-for-effective-problem-solving)
- A blog post on supplier quality: [Facilitating 8D and CAPA with suppliers](https://dev.to/beefedai/facilitating-8d-and-capa-with-suppliers-sqe-playbook-2god)
- DNV: [IATF 16949:2016 comparison matrix](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf)
- IATF: [Sanctioned interpretations, November 2024](https://www.iatfglobaloversight.org/wp/wp-content/uploads/2024/11/IATF-16949-SIs-Nov-2024.pdf)
