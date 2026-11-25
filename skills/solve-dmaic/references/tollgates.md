# DMAIC tollgates

What each phase must deliver before the sponsor signs its tollgate, and the questions to ask at the review. The deliverables follow the milestone lists published by iSixSigma and the phase descriptions in the DMAIC literature; the wording and the "fails if" column are this skill's own.

## How a tollgate runs

1. The team shows each deliverable with its evidence (data, study report, signed document), not a statement that it is done.
2. The sponsor checks each item: pass, or fail with what is missing.
3. Outcome: pass and go on; pass with named open items that do not affect the next phase (each with an owner and a date); or fail and redo or loop back.
4. Looping back is normal: Analyze can show that data are missing (back to Measure), or Improve can show a cause was wrong (back to Analyze).
5. Record the decision, the date and the open items on `assets/tollgate-review.md`.

## Define

| Deliverable | Fails if |
|---|---|
| Charter signed by the sponsor | No sponsor, or no process owner named |
| Problem statement | It contains a cause or a solution, or has no number, period or cost |
| Goal | No target value or no date; or the goal is a solution ("install …") |
| Scope | No in-scope and out-of-scope list |
| Customers and CTQ | The customer requirement behind Y is not stated |
| Process map (SIPOC, then a detailed map) | The map shows the process as written, not as walked |
| Team | No one from the process (operators, maintenance) on it |

Questions: Is this one problem or several? Is the goal reachable within the time set? Has the charter changed, and why?

## Measure

| Deliverable | Fails if |
|---|---|
| Operational definition of Y | Two inspectors could count the same unit differently |
| Data collection plan | No sampling method, or Xs not recorded with each value |
| Measurement system study | Not done, or outside the acceptance limits (gauge R&R %GRR over 30%, or distinct categories under 5, AIAG guideline; attribute agreement below the local limit) |
| Stability check | No control chart in time order, or special causes not handled |
| Baseline | Taken before the measurement study passed, or over too short a period to show the usual variation |
| Capability (measured Y) | Computed on an unstable process, without specification limits, or with the wrong sigma |
| Gap to goal | Not stated in units and money |

Questions: Does the data need stratification? Are there quick wins that can be taken now without hiding the baseline?

## Analyze

| Deliverable | Fails if |
|---|---|
| Candidate Xs | Only one X ever considered |
| Stratification and Pareto | Y not split by the recorded Xs |
| Tests | A difference claimed without a test, or with the wrong test for the data type |
| Practical size | A significant but tiny effect treated as a vital X |
| Confirmation | A vital X rests only on historical association, with no trial or experiment planned or done |
| Gain estimate | The expected Y after removing the vital Xs is not compared with the goal |
| Updated problem and goal | Not revised after what was learned |

Questions: What else changed at the same time as X (season, lot, product mix)? Is the process so broken that a redesign is needed instead?

## Improve

| Deliverable | Fails if |
|---|---|
| Solutions per vital X | A solution has no verified X behind it |
| Selection | No criteria (effect, cost, risk, time) |
| Risk check | No PFMEA review of the change |
| Pilot | Not run, or run without the same measurement system as the baseline |
| Verification | No before/after test, or Y did not move toward the goal |
| Implementation plan | No owners, dates or resources |

Questions: Did X really change in the pilot? Does the solution create a new failure mode?

## Control

| Deliverable | Fails if |
|---|---|
| Control plan | Vital Xs and Y are not in it, or have no method, frequency and reaction plan |
| Monitoring | No control chart or error-proofing check on the key X or Y |
| Standard work | Instructions not updated, or people not trained on the new method |
| Handover | Process owner has not signed |
| Sustain check | No result after the period set by local policy |
| Closure | Savings not confirmed where required, no read-across, no lessons learned |

Questions: Who reacts when the chart signals? Where else can the solution be applied?

## Sources

- iSixSigma: [Six Sigma DMAIC: milestone review deliverables and questions](https://www.isixsigma.com/methodology/six-sigma-dmaic/)
- ASQ: [DMAIC process](https://asq.org/quality-resources/dmaic)
- Wikipedia: [DMAIC](https://en.wikipedia.org/wiki/DMAIC)
- Minitab: [Is my measurement system acceptable?](https://support.minitab.com/en-us/minitab/help-and-how-to/quality-and-process-improvement/measurement-system-analysis/supporting-topics/gage-r-r-and-wheeler-s-emp-studies/is-my-measurement-system-acceptable/), summarising the AIAG guideline
- ASTM: [E2281 process capability and performance measurement](https://store.astm.org/e2281-15r20.html)
