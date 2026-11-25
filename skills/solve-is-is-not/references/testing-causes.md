# Testing causes

How to test each possible cause against the specification, how to rank the survivors and how to verify the most probable cause.

## Writing a possible cause

Write each cause so it can be tested: "If [condition], then the defect appears on [Is side] and not on [Is-Not side], because [mechanism]."

- One condition per cause. If two conditions act only together, write the combination as its own cause.
- Keep the team's favourite causes on the list; the test, not the debate, decides (Edinburgh ITIL blog).

## The test matrix

Rows are the possible causes; columns are the Is/Is-Not pairs. In each cell ask: if this is the cause, how does it explain both the Is and the Is-Not? (Kepner-Tregoe process cards)

| Mark | Meaning | Write |
|---|---|---|
| Explains | Accounts for both sides of the pair | The short reason |
| Only if | Explains the pair only with an extra condition | The assumption, as a checkable fact |
| Does not explain | A fact contradicts it | The fact |

## Elimination patterns

A single "does not explain" cell eliminates the cause. Common patterns:

1. **Present on both sides.** The condition applies to the Is-Not side as well (same fixture, same supplier), yet the Is-Not has no defect.
2. **Wrong time.** The change happened after the first defect, or long before it with no reason for the delay.
3. **Wrong place on the part.** The mechanism would act on the whole part, but the defect sits in one spot only.
4. **Wrong extent.** The mechanism would affect every unit, but only some are affected, or the trend does not match.
5. **Wrong pattern.** The condition is present on one shift only, but the defect appears on all shifts.

Do not rescue an eliminated cause with a chain of assumptions. If several assumptions are needed to make it fit, treat it as eliminated unless new facts appear (Rework summary of the method).

## Ranking the survivors

1. Keep only causes with no "does not explain" cell.
2. Rank by the number of "only if" assumptions, fewest first; then by how reasonable and how easy to check each one is (rule of thumb).
3. The top one is the most probable cause: the one to verify first, not yet the true cause (Kepner-Tregoe process cards).
4. If none survives, a fact, an Is-Not or a change is missing or wrong. Re-check the specification and the change list before inventing new causes.
5. If two survive with no assumptions, check whether they interact, and verify both.

## Verifying the true cause

Verify before spending on a permanent fix, to avoid fixes that do not work (Kepner-Tregoe process cards). Start with the assumptions of the most probable cause.

| Method | How | Confirms when |
|---|---|---|
| Check the facts | Read the records, measure the condition, check the dates and scope of the change | Each assumption is true |
| Observe | Look at the condition at the station or on the parts (photo, measurement, section) | The condition is present where the defect is and absent where it is not |
| On/off test | Create the condition under control, then remove it | The defect appears with it and stops without it (Siemens) |
| Swap | Exchange the suspected item between the Is and the Is-Not side | The defect moves with the item |
| Trial fix | Apply the fix on a trial basis and watch the result | The defect stops, and returns if the fix is removed |

- Write, before testing, the result that confirms and the result that refutes, with an owner and a date.
- The sample size and the time to watch are set by local policy.
- A refuted cause is a useful result: mark it eliminated with the evidence and test the next one (Edinburgh ITIL blog).
- A verified true cause feeds the root-cause record of the problem-solving process (IATF 16949 10.2.3 asks for a documented problem-solving process including root cause analysis and its results).

## Sources

- Kepner-Tregoe: [Analytic troubleshooting process cards, 2025](https://kepner-tregoe.com/wp-content/uploads/2025/08/Updated-ATS-Process-Cards.pdf)
- AHRQ: [Kepner-Tregoe matrix, workflow assessment toolkit](https://digital.ahrq.gov/health-it-tools-and-resources/evaluation-resources/workflow-assessment-health-it-toolkit/all-workflow-tools/kepner-tregoe-matrix)
- University of Edinburgh, ITIL Tattle blog: [Problem analysis, 2019](https://blogs.ed.ac.uk/itiltattle/2019/05/17/problem-analysis-insensibly-one-begins-to-twist-facts/)
- Rework: [Kepner-Tregoe method](https://resources.rework.com/libraries/process-management/kepner-tregoe-method)
- Siemens: [8D report](https://www.siemens.com/en-us/technology/8d-report/)
- DNV: [IATF 16949:2016 comparison matrix](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf)
