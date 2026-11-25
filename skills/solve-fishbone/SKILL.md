---
name: solve-fishbone
description: >-
  Turns a fishbone (Ishikawa, cause-and-effect) brainstorm into cause
  hypotheses that can be tested. Use when a team has a 6M brainstorm or
  fishbone diagram and needs to know which causes to test first and how,
  when a fishbone must be built for a production problem, or when a cause
  from a fishbone or a vote is called the root cause without a test. Writes
  a measurable effect, sorts causes by man, machine, method, material,
  measurement and environment, rewrites them as checkable conditions,
  screens them against Is/Is-Not facts and recent changes, and gives each
  hypothesis a test with its expected result (Ishikawa-Diagramm,
  Fischgrätendiagramm, Ursache-Wirkungs-Diagramm, 6M, Mensch, Maschine,
  Methode, Material, Messung, Mitwelt, Ursachenanalyse).
license: MIT
metadata:
  version: "1.0.0"
  category: solve
  standards: "IATF 16949 10.2.3"
---
# Fishbone to testable hypotheses

## Conventions

- The effect (Wirkung) is the head of the fish: one measurable deviation, stated without a cause. One effect per diagram.
- The bones are cause categories. The default is 6M: man (people, Mensch), machine (Maschine), method (Methode), material (Material), measurement (Messung) and environment (Mitwelt, also called mother nature or milieu). Rename or add bones to fit the process (ASQ).
- Every item on a fishbone is a hypothesis, not a finding, until a test confirms it (UF Health QPSI). A vote at most breaks ties in the test order; it never verifies a cause.
- A testable cause is a condition someone can check or switch: a thing plus how it deviates from its standard, for example "clamp pressure below set value", not "clamp".
- Is/Is-Not: where, when and on what the effect occurs, compared with where it could occur but does not (Kepner-Tregoe).
- IATF 16949 10.2.3 asks for a documented problem-solving process that includes root cause analysis; the screened sheet and the test records are that evidence.

## Inputs

- The effect: the defect or deviation, its measure (rate or count of checked), its level before and now, since when, and where it is found.
- Is/Is-Not facts by product, machine or tool, line, station, shift, lot and time.
- Changes around the start: people, material lots, settings, repairs, tools, programs, methods, gauges.
- The brainstorm list or the existing diagram, and who took part.
- The process flow and any data already collected (counts per stratum, settings, logs).

Ask for every missing input; never invent one. Copy the user's numbers exactly.

- Without a measurable effect, ask in one short list (which defect or deviation, how many out of how many checked, where found, since when, where and when it does not occur, what changed) and stop. At most add the blank `assets/fishbone-worksheet.md` and the prompt questions from [6M categories](references/6m-categories.md). Never present causes for the user's problem as findings.
- Without a brainstorm, offer prompt questions per bone and mark any cause you suggest as a candidate for the team to confirm on the floor.
- Without Is/Is-Not facts, build the hypotheses, mark the screening as open, and ask for the facts before ordering the tests.

## Procedure

1. **Write the effect.** What, where, when, how much, measured as rate = defects ÷ checked × 100 against the level before. Example (invented): 60 of 2,000 brackets with burrs this week, against 10 of 2,000 before, is 3.0% against 0.5%. Remove any cause or solution from the head.
2. **Collect the facts.** Fill the Is/Is-Not table and list the changes with dates. Ask for data by stratum (machine, tool, shift, lot) before the brainstorm is judged.
3. **Set the bones.** Start with 6M and adapt: split a large bone (machine into tool and machine), or add one (maintenance, management) where the team needs it. Prompt questions per bone in [6M categories](references/6m-categories.md).
4. **Clean each entry.**
   - Single word or vague: make it a condition (thing plus deviation).
   - Solution ("new machine", "more inspection"): move it to a parking list until a cause is confirmed.
   - Blame or attitude of a person: rewrite as the process condition that allows the error (no error-proofing, unclear instruction, training gap, workload), or reject it as untestable.
   - Restated effect or symptom: drop it. Duplicates: merge them under one bone.
5. **Ask why down each bone** until the cause is a condition that can be checked or switched, usually two to three levels below the bone (rule of thumb).
6. **Screen against the facts.** For each cause, ask: does it explain where the effect is, and also where it is not? Does it line up with a change in time?
   - A cause present in both the affected and the unaffected group cannot by itself explain the difference: mark it "contradicts", give the fact, and move it down.
   - A cause that touches only the affected group and lines up with a change: mark it "fits" and move it up.
   - Keep contradicted causes on the sheet with the reason; a fact may turn out wrong.
7. **Write each hypothesis.** "If [condition], then [effect], because [mechanism]." Add the test, the result expected if true and if false, the data needed, an owner and a date. Format and test types in [hypothesis tests](references/hypothesis-tests.md).
8. **Choose the test.**

   | Test | Use when |
   |---|---|
   | Check against standard | The condition can be measured now: setting, wear, dimension, temperature |
   | Stratify data | Counts can be split by the factor (machine, tool, lot, shift) |
   | Swap test | A part, tool or unit can be moved between a good and a bad position |
   | On/off trial | The condition can be switched safely: on, the effect appears; off, it goes |
   | Measurement check | The count comes from a new or changed check, or detection is in doubt |

9. **Order the tests.** Causes marked "fits" and linked to a change take the first places. Put a measurement check ahead of them only when the count comes from a new or changed check. Among equals, quick and cheap tests go before slow and costly ones (rule of thumb). Quick readings on contradicted causes may run in parallel, each as a row of the test plan with its expected results, but never take the first places. Use votes only to break ties. Missing facts to collect are listed as questions, not as tests.
10. **Run, record, decide.** Mark each hypothesis confirmed, refuted or open, with the evidence. Only a confirmed cause gets a permanent action; more than one cause can be confirmed. If all are refuted, recheck the effect, the facts and the bones.

### Check a claimed root cause

1. Ask what evidence confirmed it. A vote, a majority, a diagram or experience is not evidence; say plainly that the cause is not verified yet.
2. Screen it against the Is/Is-Not facts. Name every fact that contradicts it.
3. Give the test that would confirm or refute it, with the expected results.
4. Keep the other candidates open, especially those that fit the facts.
5. Advise holding costly permanent actions until a test confirms the cause. Containment of suspect product goes ahead regardless.

## Validation

Check before answering:

1. The effect is measurable and contains no cause and no solution.
2. Every entry is a condition, a parked solution, or rejected with a reason.
3. Every cause is screened against the Is/Is-Not facts and changes, or the screening is marked open.
4. Every hypothesis to be tested, including quick parallel readings, has a test, the expected result if true and if false, and an owner and a date or is marked "to be assigned".
5. No cause is called confirmed without test evidence; votes only set test order.
6. Every number is the user's, computed from it, or labelled as invented, a rule of thumb or set by local policy.

## Output

- Answer in the structure of `assets/fishbone-worksheet.md`, filled in: the effect statement as one sentence with its numbers, Is/Is-Not, changes, the causes grouped bone by bone (one heading or block per bone, not grouped by screening result), each with its screening result, and the parking list.
- `assets/hypothesis-test-plan.md`: hypotheses in test order with tests, expected results, owners, dates and status.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. A vague effect, or a cause written into the head (fix: step 1).
2. Single-word bones that cannot be tested (fix: steps 4, 5).
3. Solutions and blame on the cause list (fix: step 4).
4. Ranking by votes instead of by fit with the facts (fix: steps 6, 9).
5. Keeping a cause that the unaffected group shares (fix: step 6).
6. Declaring the top cause the root cause without a test (fix: steps 7, 10).
7. Spending on a fix before the cause is confirmed (fix: step 10).

## Hand-offs

- A D4 root-cause search arrives from `solve-8d`; confirmed occurrence and escape causes go back to it for actions and verification.
- A control-chart signal with an unknown cause arrives from `measure-spc`; use the chart to stratify and to verify the cause.
- A confirmed machine condition (wear, a missing maintenance task) goes to `improve-tpm`.
- A loss with an unknown cause arrives from `measure-oee`.
- A red quality KPI arrives from `lead-daily-routine`; report the test status back to that tier meeting.
- A confirmed cause that needs a team workshop and a sustain plan goes to `improve-kaizen`.
