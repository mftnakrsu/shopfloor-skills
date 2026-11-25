---
name: improve-kaizen
description: >-
  Chooses and runs the right continuous-improvement format for a shop-floor
  problem or improvement idea: point fix, kaizen event (workshop, blitz),
  system or flow kaizen across departments, or Toyota Kata and A3 when the
  path is unknown. Use when improvement topics must be sorted into formats;
  when a kaizen event must be chartered, planned or reported out; when
  someone wants to close a kaizen event or improvement, report its result
  or claim its gain; when gains from an earlier event have faded; or when a
  kata or A3 needs coaching questions. Starts from a measured baseline and
  a current standard, and ends every result in a new standard, a check
  that the standard is used, and a 30/60/90-day sustain plan with owners
  (KVP, Kaizen-Workshop, Kaizen-Event, Punkt-Kaizen, System-Kaizen,
  Verbesserungs-Kata, Standardarbeit, Nachhaltigkeit, Verbesserungsprozess).
license: MIT
metadata:
  version: "1.0.0"
  category: improve
  standards: "ISO 9001 10.3; IATF 16949 10.3.1"
---
# Kaizen: choose the format and sustain the gain

## Conventions

- Kaizen (KVP, kontinuierlicher Verbesserungsprozess) works from a standard and ends in a new one (Ohno, via LEI). SDCA (standardise, do, check, act) holds a standard; PDCA (plan, do, check, act) raises it (Imai, via secondary sources).
- The four formats:
  - **Point fix** (Punkt-Kaizen): a quick local fix by one team at one station.
  - **Kaizen event** (Kaizen-Workshop, blitz): a cross-functional team changes one bounded area in a focused week, commonly five days (LEI).
  - **System kaizen** (flow kaizen, System-Kaizen): improvement of the flow across processes or departments, owned by management.
  - **Kata or A3**: a target is set but the way there is unknown, so the learner runs experiments under a coach (kata) or one owner works a problem through on one sheet (A3).
- "Result" always means three things: the new standard, the check that the standard is used, and the measured gain against the baseline.
- ISO 9001 10.3 and IATF 16949 10.3.1 require the organisation to improve continually; IATF adds a documented improvement process with its method, objectives, measures and effectiveness check. This skill gives that process its working steps.

## Inputs

- The topic: what is wrong or should be better, where, and who raised it.
- The metric, its measured baseline (value, method, period, shifts covered) and the target with a date.
- Scope: stations, areas or departments touched; who owns the area.
- Whether a current standard exists (standard work (Standardarbeit), work instruction, layout, check sheet) and whether it is followed.
- What is known about cause and solution, and what was tried already.
- Constraints: output, quality, safety, budget, dates.
- For an event: sponsor, team members (including operators of the area), available days.

Ask for every missing input; never invent one. Copy the user's numbers exactly.

- Without the problem, the baseline or the target, ask for them in one short list (problem, metric, current value with how and when it was measured, target and date, scope, current standard, what was tried) and stop. At most give the blank `assets/kaizen-charter.md`. With several topics to sort, still give each its format, and list the missing baseline and target per topic as open questions; the stop applies to chartering or planning a topic. Never write a target, baseline or saving onto a charter that the user did not give.
- A missing team list or sponsor does not block the format choice; write "to be confirmed" and list it as an open question.

## Procedure

1. **State the gap.** Write the topic as metric, baseline, target and date, inside a named scope. A solution is not a problem statement: if the user starts from a solution (a new conveyor, a new machine), ask which metric it should move.
2. **Check the standard.** Ask whether a current standard exists and is followed.
   - None, or not followed: first write down today's best method and get it followed (SDCA), then measure the baseline against it. Improving from no standard gives gains nobody can hold.
3. **Choose the format** with this table (first matching row wins; practitioner synthesis, not one source's rule):

   | Signal | Format |
   |---|---|
   | Cause unknown after real attempts, or target set but the way there unknown | Kata (one learner, daily experiments) or A3 (one owner, needs analysis and agreement across functions) |
   | Crosses departments or the whole value stream; time is lost between areas; needs management decisions | System kaizen, owned by the manager who owns the flow; split into events and point fixes |
   | One bounded area, several functions needed, a change to layout, flow or workplace that needs days of focused work | Kaizen event |
   | One station or team, fix known or quick to test, no other area affected | Point fix, done by the team within days |

   - Several topics: give each one its format and a one-line reason.
   - A point fix on a flow problem moves the problem elsewhere. An event on a problem with unknown cause ends in guesses. Do not run an event on a topic that belongs one row higher.
4. **Run the format.**
   - Point fix: make the change, try it, write it into the station standard, tell all shifts. Log it on the team board.
   - Kaizen event: charter, preparation, the five days, report-out, follow-up, as in [kaizen event](references/kaizen-event.md). The charter names the sponsor, scope, baseline, target and the limits the change must respect (for example output or quality must not drop). The team includes operators from the area, not only specialists (LEI).
   - System kaizen: the flow owner maps the current and future state, then splits the gap into events and point fixes, each with an owner and date, reviewed monthly (set by local policy).
   - Kata or A3: the coaching questions and the A3 sections are in [kata and A3](references/kata-and-a3.md). When a cause must be proven, use structured problem solving before the fix.
5. **Verify the gain.** Measure with the same metric and method as the baseline, over a period that covers every shift and the normal product mix. The length is set by local policy; as a rule of thumb, at least as long as the baseline period. A last-day result is a trial, not a gain.
   - Change = (after − baseline) ÷ baseline × 100%.
   - Example (invented): baseline 50 minutes per changeover over 20 changeovers; after, 35 minutes over 20 changeovers → (35 − 50) ÷ 50 = −30%.
6. **Write the new standard.** Name the document (standard work, work instruction, layout, visual standard, check sheet, maintenance plan), its owner and its release date. Withdraw the old version. Train every shift and every operator who runs the area, not only the team.
7. **Set the check that the standard is used.** For each new standard, propose a concrete check: the role that checks (for example team leader or supervisor), the method (a leader standard-work item, a layered process audit (Prozessaudit) question or a gemba-walk (Gemba-Rundgang) item) and a frequency, marked to confirm against local policy. "Someone checks it" is not a check.
8. **Write the 30/60/90 sustain plan** with `assets/sustain-plan.md`. At each checkpoint check three things: the standard is in use (check results), the metric against the target, and the open actions closed. Details in [sustaining gains](references/sustaining-gains.md).
   - The 30-day check and audit are common event practice (Manifest checklist); the 60- and 90-day checks are a rule of thumb.
   - Every open action gets one owner and a due date. Unowned actions are the usual way gains fade. When planning, list the follow-up actions already known (release of the standard, training of every shift, the checks, each checkpoint), each with its owner (a role is enough) and a due date, relative to the event if no calendar date is known.
   - When the metric slips, find out why before retraining: often the standard itself does not work and must change.
9. **Close.** Never report an event or fix as complete, or its gain as achieved, until the new standard is released and trained on every shift, the gain is verified as in step 5, the checks are running and every open action has an owner and a date. The report-out ends the event week, not the topic; the topic closes when the 90-day check passes. When asked to report completion earlier, report the trial result, what is still missing and the check dates instead.

## Validation

Check before answering:

1. Each topic has a gap with a measured baseline and a target, or the missing value is asked for.
2. A current standard exists, or writing one is the first step.
3. The format matches the table, with a one-line reason.
4. The gain is measured with the baseline method over every shift, not on one day.
5. Every result names the new standard, its owner and the training of all shifts.
6. Every new standard has a check with who, how and how often.
7. The 30/60/90 plan exists, and every open action has an owner and a date.
8. Every number is the user's, computed from it, or labelled as invented, a rule of thumb or set by local policy.

## Output

- `assets/kaizen-charter.md` for an event or an A3: gap, scope, limits, team, plan, open-action list.
- `assets/sustain-plan.md` for every result: new standard, its check, the 30/60/90 checkpoints and the closure criteria.
- Every plan for an event, fix, kata or A3 covers Validation items 5 to 7 in the answer itself, not only in a template.
- For several topics, a table: topic, format, reason, owner, next step.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. Improving without a standard to start from, or ending without a new one (fix: steps 2, 6).
2. A charter with a solution instead of a gap, or with invented baseline and target (fix: step 1).
3. A five-day event on a problem with an unknown cause, or a point fix on a cross-department flow problem (fix: step 3).
4. A team of specialists without the operators of the area (fix: step 4).
5. Declaring the gain on the last day of the event (fix: step 5).
6. Training only the team, not the other shifts (fix: step 6).
7. Disbanding the team with an open-action list that has no owners and no follow-up checks (fix: steps 8, 9).

## Hand-offs

- Topics arrive from `lead-daily-routine` boards and escalations; report the format, owner and sustain-check status back to that tier meeting, where the 30/60/90 checks are reviewed.
- A defect whose cause must be proven goes to `solve-8d` when it is a customer complaint, a repeat problem or a serious internal problem. A kata or A3 topic runs one cycle at a time in `solve-pdca`: this skill chooses the format and keeps the 30/60/90 sustain plan; that skill runs the cycle and reports its check and act decision back.
- Losses on a machine go to `measure-oee` for the loss tree; set-up losses go to `improve-smed`; breakdowns and minor stops to `improve-tpm`.
- A topic about WIP or throughput time goes to `improve-tpt`; a manual line with uneven station loads goes to `improve-line-balancing`.
- System kaizen across a stream starts from a current- and future-state map in `improve-vsm`; its loop plan and kaizen bursts arrive here.
- A flow topic that needs a supermarket, a FIFO lane or CONWIP goes to `improve-kanban-pull`; card-reduction events arrive from there.
- The check that the new standard is used can be a gemba-walk item planned with `lead-gemba-walk`; walk findings that need an improvement format arrive from there.
- Improvement topics that need a workshop or a sustain plan arrive from `measure-oee`, `improve-tpt`, `improve-line-balancing`, `improve-smed` and `improve-tpm`.
- Whether a gain on a measured characteristic is real or noise is checked on a control chart with `measure-spc`.
- Cause analysis in a workshop widens the list of causes with `solve-fishbone` and narrows it with `solve-is-is-not`; a defect whose cause must be proven goes to `solve-5why`; a problem whose cause needs data analysis goes to `solve-dmaic`, and a known solution with no need for analysis arrives from there. A confirmed cause that needs a workshop and a sustain plan arrives from `solve-fishbone`.
- New standard work after the event goes to `plan-workstation-instructions`.
