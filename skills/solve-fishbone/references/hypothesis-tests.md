# Hypothesis tests

How to write a fishbone cause as a hypothesis, screen it against the facts, and choose and read a test. Fishbone items are hypotheses, not confirmed causes, and each needs data or observation before corrective action (UF Health QPSI).

## Hypothesis format

"If [condition], then [effect], because [mechanism]."

| Field | Content |
|---|---|
| Condition | A thing plus its deviation from standard, checkable or switchable |
| Effect | The measured effect from the head of the fish |
| Mechanism | How the condition makes the effect, in one line |
| Fit with facts | Fits, contradicts or open, with the Is/Is-Not fact or change |
| Test | One test from the table below |
| Expected if true / if false | The result that confirms and the result that refutes, stated before testing |
| Owner, date | Who runs the test and by when |

Example (invented): "If the punch edge is worn beyond its regrind limit, then burrs form on the cut edge, because a blunt edge tears instead of shears. Test: measure the edge radius on die set B and on die set A. True: B is beyond the limit and A is not. False: both are inside the limit."

## Screening with Is/Is-Not

Use the Is/Is-Not table to sort the brainstorm, then pick the cause to test first (method after Kepner-Tregoe).

1. For each Is/Is-Not pair, write what is distinctive about the "is" side.
2. List the changes in or around that distinction, with dates.
3. For each cause, ask whether it explains both columns. A cause that is equally present on the "is not" side contradicts the facts.
4. Rank: fits and linked to a change; fits; open; contradicts.

Write each distinction as a measurable difference, such as a tool number, a lot or a date; "it is different" gives no change to look for.

## Test types

| Test | How | Reads as confirmed when |
|---|---|---|
| Check against standard | Measure the condition now against its drawing, setting or limit | The condition is out of standard where the effect is, and in standard where it is not |
| Stratify data | Split the defect counts by the factor and compare rates | The rate differs clearly between the levels of the factor and matches the Is/Is-Not |
| Swap test | Exchange a part, tool or unit between a good and a bad position | The effect moves with the swapped item |
| On/off trial | Create the condition under control, then remove it | The effect appears with it and goes without it (Siemens) |
| Measurement check | Run known good and known bad parts through the check; compare two checkers or gauges | The check misses known bad parts or rejects known good ones |

The number of parts, repeats and the threshold for "differs clearly" are set by local policy. A destructive or unsafe trial is replaced by data stratification.

## Worked example: stratified rates (invented)

Rate = defects ÷ checked × 100.

| Stratum | Defects | Checked | Rate |
|---|---|---|---|
| Die set A | 5 | 1,000 | 0.5% |
| Die set B | 55 | 1,000 | 5.5% |
| Early shift | 30 | 1,000 | 3.0% |
| Late shift | 30 | 1,000 | 3.0% |

The rate follows the die set, not the shift. Causes tied to die set B move up; causes that would act on both shifts alike, such as a shift-specific person or method, move down. The next test is a check against standard or a swap test on die set B.

## Reading the result

- Confirmed: the result matches "expected if true". Record the evidence, then plan the permanent action.
- Refuted: record why and keep it on the sheet; do not delete it.
- Open: the test was not clear; choose a sharper test.
- More than one cause can be confirmed. If all are refuted, recheck the effect statement, the facts and the bones.
- A vote, a majority or the length of a bone is never test evidence.

## Sources

- UF Health QPSI: [Using the fishbone diagram for root cause analysis](https://knowledge.qpsi.med.ufl.edu/qi-foundations/using-the-fishbone-diagram-for-root-cause-analysis/)
- Kepner-Tregoe: [Problem analysis application guide, 2024](https://kepner-tregoe.com/app/uploads/2024/07/PA-Application-Guide_22July2024.pdf)
- Kepner-Tregoe: [8D: is or is not, that is the question](https://kepner-tregoe.com/blogs/8d-is-or-is-not-that-is-the-question/)
- Siemens: [8D report](https://www.siemens.com/en-us/technology/8d-report/)
- iSixSigma: [Mistakes when using fishbone diagrams](https://isixsigma.com/ask-tools-techniques/mistakes-when-using-fishbone-ishikawa-diagrams)
