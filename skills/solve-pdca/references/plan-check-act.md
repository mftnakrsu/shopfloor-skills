# Plan, check, act

Working rules for the three steps where most cycles go wrong.

## Writing the prediction

- State it in the goal's metric and unit: "at most 10 per 10,000 picks", not "fewer errors".
- Write why the team expects it (the theory): which cause the countermeasure removes and how much of the problem that cause explains. A prediction without a reason teaches nothing when it misses.
- Add the side effects the team expects or fears, each with how it will be watched (cycle time, scrap of another kind, operator load, cost).
- Write it before the test starts and date it. A prediction written after the result is not a prediction.
- Prediction, theory and comparison of data to prediction come from the PDSA form of the cycle (Moen, Nolan and Provost, via Moen and Norman).

## Designing the test

| Decision | Rule |
|---|---|
| Scale | Smallest area where the cause occurs: one station, one line, one cell (preferably small scale: Deming, via Moen and Norman) |
| Changes | One per test where possible, or changes that can be switched on and off one at a time (rule of thumb) |
| Method | Count the result exactly as the baseline was counted: same source, same definition, same unit |
| Length | Long enough to cover every shift, the normal product mix and enough units to see the predicted change; set by local policy |
| Controls | Record anything else that changed in the area during the test (material lot, people, settings, volume) |
| Criterion | Agreed in numbers with the reviewer before the start |

## Running the check

Answer these in order and write the answers on the sheet.

1. Was the test run as planned? List the deviations. A test that was not run as planned is checked, but its result is marked as weaker evidence.
2. Was the result counted with the baseline method, over the planned period, on every shift?
3. What is the result, the change and the share of the gap closed (formulas in the procedure)?
4. How does it compare with the prediction? With the goal?
5. Is the change larger than the normal week-to-week spread of the baseline? If it is not, it may be noise; for a measured characteristic, read it on a control chart.
6. What is left? Break it down by type, place, shift and time. A cluster points at a cause the countermeasure does not reach.
7. Did any limit move: safety, another defect, cycle time against takt time, cost?
8. What did the team learn about the cause?

Opinions ("it feels better", "the operators are happy") are worth recording as observations, but they are not a check. If the measured data exists, read it; if it does not, collect it before the act decision.

## Reading prediction against result

| Result | What it says | Next |
|---|---|---|
| As predicted, goal met | Cause and countermeasure understood | Adopt |
| Better than baseline, short of prediction | Part of the cause is covered, or another cause exists | Adapt: break down what is left |
| Better than prediction | The theory is incomplete; check the controls for another change | Confirm before adopting |
| No change | The countermeasure does not act on the cause, or the cause is wrong | Abandon; go back to the analysis |
| Worse | Harmful effect | Undo now; abandon |

## Act and SDCA

- Adopt means the change becomes the standard: release the document, withdraw the old one, train every shift, set the check that it is used.
- From then on the standard is held by SDCA: standardise, do, check that it is followed, act on any drift (Imai, via secondary sources). The SDCA check asks "is the standard used?"; the PDCA check asks "did the change work?". Do not mix the two.
- When the SDCA check finds the standard not used, ask first whether the standard works, before retraining.
- Roll-out to similar areas is a small cycle of its own: predict the same effect, confirm it on the first area, then extend.

## Sources

- Moen, R., Norman, C.: [Circling back, Quality Progress, November 2010](https://qi.elft.nhs.uk/wp-content/uploads/2026/02/ron-cliff-circling-back.pdf)
- Lean Enterprise Institute: [Lexicon: PDCA](https://www.lean.org/lexicon-terms/pdca/)
- Wikipedia: [PDCA](https://en.wikipedia.org/wiki/PDCA)
- Institute for Healthcare Improvement: [How to improve: Model for Improvement](https://www.ihi.org/resources/how-to-improve)
- Martin, K.: [Words matter: why I prefer PDSA over PDCA (Lean Blog)](https://www.leanblog.org/2013/01/guest-post-words-matter-why-i-prefer-pdsa-over-pdca/)
- Roser, C.: [The many flavors of the PDCA (AllAboutLean)](https://www.allaboutlean.com/pdca-variants/)
- Commons-OS: [Gemba Kaizen pattern summary, a secondary summary of Imai used for SDCA](https://commons-os.github.io/patterns/gemba-kaizen/)
