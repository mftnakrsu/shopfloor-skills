---
name: solve-is-is-not
description: >-
  Scopes a production or quality problem with an Is/Is-Not specification
  (what, where, when, extent), draws out the distinctions between the Is
  and the Is-Not side and the dated changes behind them, tests every
  possible cause against both columns to eliminate those that do not fit,
  and names the most probable cause with the test that will verify it.
  Use when the cause of a deviation is unknown and the team disagrees or
  jumps to a favourite cause, when an 8D D2 or D4 needs an Is/Is-Not, or
  when an existing Is/Is-Not or its chosen cause must be checked
  (Kepner-Tregoe problem analysis, Ist/Ist-nicht-Analyse, Ist-Ist-nicht,
  Problemeingrenzung, Unterschiede und Änderungen, wahrscheinlichste
  Ursache, Ursachennachweis).
license: MIT
metadata:
  version: "1.0.0"
  category: solve
  standards: "IATF 16949 10.2.3"
---
# Is/Is-Not problem analysis

## Conventions

- Deviation (Abweichung): the gap between what should happen and what happens. The method fits when the cause is unknown and must be known to act (Kepner-Tregoe).
- Object and defect: the thing, or group of things, that has the problem, and what is wrong with it.
- Is: where, when and how much the defect is seen. Is-Not (Ist-nicht): the closest comparable object, place, time or amount where the defect could be but is not. It is a real comparison, not the negation of the Is.
- Distinction (Unterschied): what is true only of the Is side compared with its Is-Not. Change (Änderung): something new or different in, on or around a distinction, with its date.
- Possible cause: a statement "change or distinction X causes the defect by mechanism Y". Most probable cause: the possible cause that explains every Is and Is-Not with the fewest and most reasonable assumptions. True cause: a most probable cause that a test has verified.
- This skill narrows: it tests a known list of causes against the full specification. Building a broad list of causes is `solve-fishbone`.
- Cause status: **eliminated** (contradicts a fact), **fits only if** (needs an assumption), **fits** (explains every pair), **verified** (proved by a test).

## Inputs

- The deviation: object, defect, the requirement it misses, and how it is found.
- Is facts and Is-Not facts for what, where, when and extent, as numbers, identifiers and dates (product, variant, machine, tool, cavity, line, station, shift, lot, location on the part, first seen, pattern since, count out of count, trend).
- Changes before and around the start, each with its date and where it applies.
- Possible causes already named by the team, if any, and any tests already run.
- Mode: build a new analysis, or check an existing one. Infer it from the request.

Ask for every missing fact; never invent one. Copy the user's numbers, dates and identifiers exactly.

- Without the Is-Not side, the start date or the extent, ask for them in one short list and stop. Name the Is-Not comparisons that would matter most for this object (other machines, tools, lines, variants, shifts, positions on the part, earlier periods) and ask for the changes with dates. At most add the blank `assets/is-is-not-worksheet.md`.
- Do not confirm or reject a named cause on missing facts; say which facts would decide it.
- A broad problem ("scrap is up") is not specific enough yet. Ask for the breakdown by defect and take the largest single defect on one object.

## Procedure

1. **State the deviation.** One line: object and defect, as found. No cause and no solution in it. If the user's statement carries a cause, move it to the list of possible causes.
2. **Specify Is and Is-Not.** Fill each dimension with the question pairs in [specification questions](references/specification-questions.md):
   - **What:** which object has the defect, and which similar object could have it but does not; which defect, and which other defect could occur but does not.
   - **Where:** where the object is when the defect is seen (machine, line, station, cavity), and where on the object the defect sits, each against the closest place where it could be but is not.
   - **When:** first seen (date, shift); pattern since (every shift, start-up only, after a set-up); when in the life cycle or process flow; and when it could have been seen first but was not.
   - **Extent:** how many out of how many, size of a single defect, defects per unit, and the trend (growing, steady, falling), each against the Is-Not count.
   - Pick the Is-Not as the closest comparable item that is free of the defect. Mark every empty cell as an open question; a pair with no Is-Not cannot eliminate anything.
3. **Find the distinctions.** For each pair, write what is true only of the Is side, as a concrete difference: a tool number, a material lot, a programme, a date, a setting, a supplier. "Is different" or a bare reading is not a distinction.
4. **Find the changes.** For each distinction, list what changed in, on or around it, with the date and where it applies. A change that applies to both sides is still listed; the test in step 6 will deal with it.
5. **Develop possible causes.** Turn each relevant distinction or change into a statement: "If X, then the defect appears on the Is side and not on the Is-Not side, because Y." Add the team's own candidates and causes from experience. List them all before judging any.
6. **Test each cause against every pair.** For each pair ask: if this is the cause, how does it explain both the Is and the Is-Not? Mark each cell:
   - **Explains**: it accounts for both sides.
   - **Only if**: it explains the pair only with an assumption; write the assumption.
   - **Does not explain**: a fact contradicts it, for example the condition is equally present on the Is-Not side, or it started after the defect. One such cell eliminates the cause.
   - A cause is not eliminated by being unlikely, and not kept by being popular. Details and the elimination patterns in [testing causes](references/testing-causes.md).
7. **Pick the most probable cause.** Among causes with no "does not explain" cell, rank by the number of assumptions, then by how reasonable they are (rule of thumb). If none survives, the specification or the change list is incomplete: go back to steps 2 to 4. If several survive, check whether they act together.
8. **Plan the verification.** Before any permanent action, verify the most probable cause, starting with its assumptions:
   - check the facts behind each assumption (records, measurements);
   - observe the condition at the station or on the parts;
   - run an on/off test: create the condition and see the defect appear, remove it and see it stop;
   - try the fix on a trial basis and watch the result.
   Give the test, the result that confirms, the result that refutes, an owner and a date. Containment can start at once; permanent action waits for the result.
9. Run the Validation checks.

Example (invented): powder-coated panels show scratches on the front face, found at packing. Is: line B, 30 of 600 since Monday's early shift, steady. Is-Not: line A, same panel, 0 of 600; back face. Changes: new powder lot on both lines from the previous Friday; new hanging racks on line B from Monday.

| Possible cause | Line B, not A | Front, not back | From Monday | Result |
|---|---|---|---|---|
| New powder lot | Does not explain: same lot on line A | Does not explain: the lot coats both faces | Only if the lot sat unused over the weekend | Eliminated |
| New racks on line B | Explains | Only if the rack hooks touch the front face | Explains | Most probable; verify |

Verification: hang 50 panels on old racks and 50 on new racks on line B. Confirms if scratches appear only on the new racks; refutes if both sets scratch alike.

### Check an existing Is/Is-Not

1. Check the deviation statement, then each pair: is there a real Is-Not, a concrete distinction and a dated change?
2. Test the chosen cause against every pair as in step 6. If one fact contradicts it, say plainly that the cause does not explain the facts and must not be accepted, whatever the team believes.
3. Name the change or distinction that does fit and the test to verify it. Say whether the analysis can be closed: only with a verified cause.

## Validation

Check before answering:

1. The deviation statement names object and defect and contains no cause.
2. Every dimension has Is and Is-Not facts, or the gap is listed as an open question.
3. Every Is-Not is a real comparable item, not a negation.
4. Every distinction is concrete, and every change has a date and a scope.
5. Every possible cause is tested against every pair, with its assumptions written.
6. No cause with a "does not explain" cell is kept, and no cause is called the root or true cause before a test has verified it.
7. The verification has a test, confirming and refuting results, an owner and a date.
8. Every number and fact is the user's, or labelled as invented, a rule of thumb or set by local policy.

## Output

- `assets/is-is-not-worksheet.md`, filled in: deviation, Is/Is-Not table with distinctions and changes, the cause test matrix, the most probable cause and its verification plan, open questions.
- Say first which causes are eliminated and why, and which cause to verify first. In a check, say first whether the chosen cause explains the facts and whether the analysis can be closed.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. An empty or token Is-Not column, so nothing can be eliminated (fix: step 2).
2. An Is-Not that only negates the Is ("not defective parts") (fix: step 2).
3. A vague distinction with no change to look for (fix: steps 3, 4).
4. Keeping a cause that is equally present on the Is-Not side or started after the defect (fix: step 6).
5. Judging causes by vote, seniority or habit instead of the facts (fix: step 6).
6. Calling the most probable cause the root cause without a verification test (fix: step 8).
7. Starting a permanent fix before the cause is verified (fix: step 8).

## Hand-offs

- A customer complaint, field failure or repeat problem runs in `solve-8d`; this analysis serves its problem description and root-cause steps.
- A verified cause that needs its occurrence, detection and system roots goes to `solve-5why`.
- When no change or distinction explains the facts, widen the list of possible causes with `solve-fishbone`, then test them here.
- A process signal with an unknown cause arrives from `measure-spc`; checking that a fix holds on a measured characteristic goes back there.
- A red KPI with an unknown cause arrives from `lead-daily-routine`; report the verified cause back to that tier meeting.
