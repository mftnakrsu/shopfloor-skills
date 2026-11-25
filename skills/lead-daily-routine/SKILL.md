---
name: lead-daily-routine
description: >-
  Designs, runs and audits shopfloor management on production lines: tier
  meeting cascades, SQDCP boards, same-day escalation with a reply path,
  action tracking and routine adherence. Use when setting up or fixing
  daily leadership routines, tier meetings, huddles, stand-ups, KPI
  boards, escalation rules or leader standard work (Shopfloor-Management,
  Regelkommunikation, Shopfloor-Board).
license: MIT
metadata:
  version: "1.0.0"
  category: lead
  standards: "IATF 16949 8.5.6.1.1, 9.1.1.1"
---
# Daily leadership routine

## Conventions

- Tier 1 is the line or team at its board; higher numbers are higher levels, up to the plant.
- SQDCP means safety, quality, delivery, cost, people. Map local names to it, for example German QKLSP (Qualität, Kosten, Logistik, Sicherheit, Personal).
- Red or green is actual against target.
- Escalation means asking the next tier for support, never blame.
- Durations are in minutes.

## Inputs

- Mode: design (a new cascade), run (today's meeting) or audit (check or fix a running routine). Infer it from the request.
- The leadership levels and who attends.
- The shift pattern and start times.
- The KPIs (Kennzahlen) tracked, with their targets and how often the data refreshes.
- Run mode: today's board values and open actions.
- Audit mode: observations of real meetings.

Ask only for what is missing. If there is no answer, state assumptions as assumptions.

- A design needs the leadership levels, at least one shift start time and the KPIs tracked. If any of these is missing, ask for the missing ones in a short list and stop there. Do not draft a schedule on invented facts; at most name the tiers you expect, with every assumption labelled.
- Missing targets, later shift times or refresh rates do not block a design. Write "set by local policy" or "assumption" in their place and list them as open questions.
- Run mode needs today's board values and open actions. If they are missing, ask for them; never invent a value.

## Procedure

### A. Design a cascade (Regelkommunikation)

1. Choose the tier count: 2 for a small site, 3–4 for larger sites (rule of thumb). Number the tiers from the line upward and map the local level names to them.
2. Times: tier 1 within the first hour of the shift; each next tier 30–60 minutes after the one below, so issues travel up the same morning; the top tier ends before late morning (rule of thumb; example cascade in [tier design](references/tier-design.md)). A shift that starts after the cascade holds its own tier 1 and escalates to a named leader on shift, who can decide and answers within the shift. Only what needs a higher tier waits for the next morning's cascade, marked as an exception with an owner and a due date.
3. Timeboxes: tier 1 ≤15 min, tier 2 about 15 min, tier 3 15–20 min, tier 4 15–30 min (rule of thumb from practitioner sources). Meet standing at the board, at the same time and place every day, and start on time.
4. One fixed agenda order at every tier: safety, quality, delivery (output against plan, hour by hour at tier 1), cost and productivity, people, actions due today, new problems, escalations up and answers down. Discuss only the reds; a green needs no discussion.
5. Board: 5–8 KPIs per board (rule of thumb), each with target, actual, red or green, and trend; an action list (Maßnahmenplan) with problem, action, owner, due date and status; an escalation list; an hour-by-hour board at the line. Choose the KPIs with the six questions in [board design](references/board-design.md). Put each KPI the user already tracks, under its own name, into its SQDCP category. Name every empty category as a gap and propose a KPI for it, marked as a proposal. KPIs cut from a board move to a weekly or monthly review, or are dropped; a lower board takes one only within its own 5–8 limit.
6. Escalation rules: escalate when a problem is outside the tier's authority or resources, recurs, or cannot be fixed the same day. Every escalation gets an owner and a due date, and the answer returns to the raising team the same day. If a higher tier does not meet daily, name a daily contact who answers escalations the same day.
7. Problem solving stays outside the meeting, and every problem leaves the meeting with an owner and a due date:
   - Product or people at risk: contain at once (Sofortmaßnahme), without waiting for the meeting.
   - Cause known: a simple action with an owner and a date.
   - Cause unknown: give it an owner and a due date, and start structured problem solving outside the meeting; use `solve-8d` for customer complaints, safety issues and repeat problems. The meeting only starts, tracks and closes the work.
8. IATF 16949 hooks:
   - Where alternate process controls are in use, review them daily in the tier 1 or tier 2 meeting (8.5.6.1.1).
   - Results that trigger a reaction plan in the control plan (Produktionslenkungsplan) appear as quality reds with an escalation path (9.1.1.1).
9. Leader standard work: give each chair a written daily routine that checks the level below at the gemba (Ort der Wertschöpfung): the board, open actions, escalations and standard work. The chair's own manager reviews that routine daily. Lower levels spend more of their time in fixed routine than higher ones (gradient in [tier design](references/tier-design.md)).

### B. Run today's meeting

1. For every red KPI, give either a countermeasure with owner and date, or an escalation. A red OEE KPI gets its loss tree in `measure-oee`; a quality red from an SPC signal gets its chart check in `measure-spc`.
2. List the actions due today.
3. List the escalations going up and the answers coming down.
4. Output the agenda with clock times that fit the tier's start time and timebox (steps A2 and A3; worked example in [tier design](references/tier-design.md)).

### C. Audit the routine

1. Observe real meetings, not reports about them.
2. Score the checklist in `assets/routine-self-audit.md`.
3. Compute the adherence metrics defined in [routine audit](references/routine-audit.md): meetings held, started on time, within timebox, attendance, reds with a countermeasure or escalation, action closure and open age, and escalation answer time.
4. Name the three biggest gaps.
5. If the user only describes the routine, check the description against Validation and Pitfalls. Open with one short paragraph that names the main failures found and the standard each one breaks, in numbers. Then list every gap the description shows, each with its fix from part A; state each fix as the new setting in numbers. Low attendance, overruns and skipped meetings are gaps too. Say once that nothing was observed in a real meeting. End with the corrected agenda, with clock times and minutes that add up to the timebox, and the adherence metrics to track.

## Validation

Check before answering:

1. An issue raised at tier 1 can reach the top tier, and an answer can return, before the end of the shift. Shifts after the cascade follow the A2 exception.
2. Every tier has a time, a timebox, attendees and an agenda.
3. No board has more than 8 KPIs (the A5 rule of thumb), and every SQDCP category has a KPI or a named gap.
4. Every red has a countermeasure or an escalation, and every action has an owner and a date.
5. No problem-solving session is scheduled inside a tier meeting.
6. Assumptions are labelled.

## Output

- Design mode: `assets/tier-cascade-template.md` and `assets/tier-board-template.md`, filled in, followed by the escalation rules (step A6), the problem-solving rule (step A7), the KPI gaps (step A5) and the open questions.
- Run mode: the timed agenda, plus the action and escalation lists.
- Audit mode: `assets/routine-self-audit.md` with scores and the top three gaps. For a described routine: each gap with its fix, the corrected agenda and the adherence metrics to track.
- In every mode, write for the user: state each rule in plain words, and never cite this skill's step numbers, section names or file names.

## Pitfalls

1. The meeting turns into status reporting (fix: steps A4, B1).
2. Too many KPIs (fix: step A5).
3. Escalation waits until next week (fix: steps A2, A6).
4. Verbal escalation without an owner, date or reply (fix: steps A5, A6).
5. Red results are hidden or punished (fix: treat escalation as a request for support).
6. Leaders manage from screens instead of the gemba (fix: steps A3, A9).
7. Meetings overrun or get skipped, and nobody measures it (fix: step C3).

## Hand-offs

- A complaint, safety issue or repeat problem with an unknown cause goes to `solve-8d`.
- A red OEE KPI goes to `measure-oee` for the loss tree; a red breakdown KPI or overdue AM tags go to `improve-tpm`; a line that keeps missing the hour-by-hour plan goes to `improve-line-balancing`.
- Leader standard work walks and a go-and-see for a red KPI are planned with `lead-gemba-walk`; actions from walks arrive on the board from there.
- A quality red from an SPC signal goes to `measure-spc` for chart and limit checks; an unresolved or repeat signal arrives from there.
- A red lead-time or delivery KPI that spans several processes goes to `improve-vsm`; loop targets are tracked on the board.
- Improvement topics from the board go to `improve-kaizen`; supermarket stock-outs and pitch misses arrive from `improve-kanban-pull`.
