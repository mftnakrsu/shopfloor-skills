---
name: lead-gemba-walk
description: >-
  Plans, runs and follows up gemba walks on the shop floor in three modes:
  process walk (standard work, waste, flow), management-system walk
  (boards, reds, escalations, leader standard work) and value-stream walk
  (end-to-end current state). Sets the purpose, route, timebox and open
  questions, keeps a blame-free observation log with owners and due dates,
  adds an optional layered process audit (LPA) segment, and closes the
  loop with the team. Use when planning, doing, writing up or following up
  a gemba walk, go-and-see, leader or management walk, shopfloor round or
  layered process audit, or turning walk notes into findings and actions
  (Gemba Walk, Gemba-Rundgang, Shopfloor-Rundgang, Prozessbegehung,
  Vor-Ort-Begehung, Layered Process Audit).
license: MIT
metadata:
  version: "1.0.0"
  category: lead
  standards: "IATF 16949 8.5.6.1.1, 9.2.2.3; AIAG CQI-8"
---
# Gemba walk

## Conventions

- The gemba (Ort der Wertschöpfung) is where the work is done. A walk is a prepared visit with a purpose, a route and follow-up; walking around without them is not a gemba walk.
- Walk types: the value-stream and management-system walks follow Womack; the process walk is a common practitioner form (Shook, KaiNexus).
- An observation is a fact seen at the gemba: where, what, how often. An interpretation is labelled as one. A finding is an observation that needs action.
- Observations describe the process, never a person. The log names stations and roles, not people.
- A layered process audit (LPA, geschichtetes Prozessaudit) is a short yes/no check of critical process controls by several management layers. Layer 1 is closest to the work.
- Durations are in minutes.

## Inputs

- Phase: plan, run (record or write up a walk) or follow up. Infer it from the request.
- Purpose: the problem, KPI (Kennzahl) concern or standard the walk looks at.
- Area: the process steps or the route, and for a value-stream walk the product family and its start and end points.
- Walkers: who walks, their level, who from the area guides, and the time available.
- Management-system walk: which boards and tier meetings exist (see `lead-daily-routine`).
- LPA segment: the control points to verify (control plan, error-proofing list, standard work), the walker's layer, and the audit frequency (set by local policy or customer requirement).
- Run phase: the raw observations. Follow-up phase: the observation log with status, and the open items of the previous walk.

Ask only for what is missing:

- A plan needs the purpose, the area and who walks. If any is missing, ask for them in a short list and stop. You may show the empty structure of a plan, but never a route, stations, problems or KPI values made up for the user's area.
- Missing time available or cadence does not block a plan: use the rules of thumb below, labelled.
- Never invent LPA control points. Ask for the control plan items; you may list the usual categories (step A7) as prompts to confirm.
- A write-up needs the observations. Never add one that was not reported.

## Procedure

### A. Plan the walk

1. Choose the walk type from the purpose (details in [walk design](references/walk-design.md)):

   | Type | Purpose | Route | Output |
   |---|---|---|---|
   | Process | see the work against its standard, find waste and obstacles | along the material flow of one process | observation log, kaizen candidates |
   | Management system | test whether the daily system keeps the process stable | board to board, then to the source of a red | gaps in boards, reds, escalations, leader standard work |
   | Value stream | see the whole flow, dock to dock | end to end, material and information flow | current-state facts: steps, inventory, times |

2. Write the purpose in one sentence tied to the problem or KPI. Tell the area leader and the team beforehand what the walk looks at, and that it is about the process and its obstacles, not about checking people.
3. Route: follow the product through the process steps in order, including the hand-offs between steps. For a kaizen view, start near the customer end and work back (Shook). Plan where to stand at each step.
4. Timebox: split the available time into a short opening with the area leader, one segment per stop on the route, the LPA segment if any, and a reflection at the end. Rule of thumb: about 5 minutes opening, 5–10 minutes reflection, the rest on the route. The segments must not exceed the time available. Worked example (invented round numbers): 60 minutes = 5 opening + 4 stops × 9 + 10 LPA + 9 reflection = 60.
5. Questions: prepare open questions and ask them in the order what → why → what if → why not (Shook, crediting Verble). Core set (Mann): What is the process here? How can you tell it is working? What do you do when it is not? Is there work going on to improve it? Ask the people doing the work, not only their leader. Question bank in [walk design](references/walk-design.md).
6. What to look for, by type: the checklists in [walk design](references/walk-design.md). Always include the gap between the written standard and the actual work, and what stops people from working to the standard.
7. LPA segment (optional): 5–10 yes/no items (rule of thumb), each answered on evidence seen at the station. When the user gives control points, make each one an item, keeping its wording and interval, and name the evidence to look at; mark any item you add as a proposal. Otherwise draw them from the control plan (Produktionslenkungsplan): error-proofing verification, standard work followed, operator qualified, control-plan checks at the right frequency and sample, reaction plans followed when a check fails. Give it its own timed row on the route, not items spread over the stops: the LPA asks "is the standard followed?"; the walk also asks "is the standard adequate, and what is in the way?". Details in [layered audit](references/layered-audit.md).
8. Cadence: make the walk part of leader standard work, with a fixed slot. Vary shift and time of day now and then to see other conditions. Sources disagree on frequency (ranges in [walk design](references/walk-design.md)); a walk whose findings are closed beats a frequent walk without follow-up.

### B. Run and write up

1. Watch before you ask: stay at each stop for at least one full work cycle (rule of thumb).
2. Ask, listen, and record facts as you go: where, what, how often, and the person's own explanation.
3. Do not fix, order or redesign on the spot. Only an immediate safety risk or a risk to product quality is contained at once (stop, protect, segregate) and logged as contained. The one other exception is a No in the LPA segment, which the walker may correct at once within their own authority (step B6).
4. No blame. A standard not followed is a question about the process: is the standard known, clear and possible to follow, are the means there (material, tools, PPE, time), was the person trained? Idle people are a waiting observation (Wartezeit) until the cause upstream or downstream is found. Warnings and disciplinary notes never go into a walk log; if conduct really is the issue, it goes to the line manager through the normal HR route, outside the walk.
5. Recurring disturbances that people work around (missing parts, rework loops, manual restarts) are findings even when people deal with them themselves.
6. LPA segment: answer each item Yes, No or "not reviewed". Correct a No at once if it is within your authority, and note the action and date. Pass other Nos to the responsible person and note who was told. A No stays a No in the record even when it was corrected during the audit.
7. Reflect right after the walk with the area leader: what did we see, what did we learn, which findings matter most for the purpose.
8. Fill in the observation log (`assets/observation-log.md`): number, where, what was seen, type, containment, next step, owner, due date, status, verified. Every row gets an owner (a role when no name is known) and a due date; mark dates you propose as proposals.
9. Writing up a past walk: check that each safety or quality risk was really contained. If it was not, containment is the first action, due today.

### C. Follow up

1. Give every finding an owner, a due date and a route ([follow-up](references/follow-up.md)):
   - Simple fix with a known cause: an action on the area board (`lead-daily-routine`).
   - Unknown cause: structured problem solving outside the walk; customer, safety or repeat problems go to `solve-8d`.
   - Equipment losses: `measure-oee`, then `improve-tpm` or `improve-smed`. Flow and waiting: `improve-tpt` or `improve-line-balancing`.
2. Close the loop: tell the people at the gemba what was learned and what happens next, even when nothing happens at once. When is set by local policy; rule of thumb: before the next walk in that area.
3. Close a finding only when someone has seen at the gemba that the action works. "Action assigned" or "reported done" is not closed.
4. Start every walk with the open findings of the previous walk in that area.
5. Track the walk system with the metrics in [follow-up](references/follow-up.md): walks held, findings closed and verified on time, average open age; for the LPA, schedule adherence, first-time conformance and repeat Nos.

## Validation

Check before answering:

1. The walk has a one-sentence purpose tied to a problem, KPI or standard.
2. The route follows the process flow, and the timed segments add up to no more than the time available.
3. The questions are open, and the walkers talk to the people doing the work.
4. Nothing is fixed or ordered on the spot except contained safety or quality risks and LPA Nos within the walker's authority.
5. No observation blames, rates or disciplines a person; each is stated as a process fact.
6. Every finding has an owner, a due date, a route and a verification step; the team hears back.
7. LPA items cover every control point the user gave, are yes/no on evidence, sit in their own timed segment, and a No corrected during the audit still counts as a No.
8. Assumptions and rules of thumb are labelled.

## Output

- Plan: `assets/walk-plan.md` filled in (purpose, type, route, timed segments, questions, what to look for), with `assets/lpa-checklist.md` when an LPA segment is included.
- Run or write-up: `assets/observation-log.md` filled in, the contained risks first, then the top findings for the purpose, then who tells the team what and by when.
- Follow-up: the log with status and verification, the overdue findings, and the metrics.
- Write for the user in plain words; never cite this skill's step numbers, section names or file names.

## Pitfalls

1. A walk with no purpose or follow-up becomes walking around and collecting anecdotes (fix: steps A2, C1).
2. The walker fixes or gives orders on the spot (fix: step B3).
3. Findings blame or punish people, so the next walk sees a staged process (fix: step B4).
4. The walker talks only to supervisors, or reads screens instead of watching the work (fix: steps A5, B1).
5. The walk shrinks to a checklist; nobody asks whether the standard is adequate (fix: step A7).
6. Findings are closed when assigned, and the team never hears back (fix: steps C2, C3).
7. LPAs are delegated, or Nos corrected during the audit are booked as Yes (fix: step B6, [layered audit](references/layered-audit.md)).

## Hand-offs

- Actions with a known cause go onto the area board and its tier meeting in `lead-daily-routine`; a management-system walk that finds a broken routine also goes there for the routine audit.
- Customer, safety or repeat problems with an unknown cause go to `solve-8d`.
- Equipment losses go to `measure-oee` for the loss tree, then `improve-tpm` (breakdowns, minor stops) or `improve-smed` (long set-ups).
- Waiting, piles of work in process and long throughput times go to `improve-tpt`; an unbalanced manual line goes to `improve-line-balancing`.
