---
name: improve-tpm
description: >-
  Runs total productive maintenance (TPM) on machines and lines: computes
  and interprets MTBF and MTTR from breakdown data, audits
  autonomous-maintenance steps against exit criteria, sets up
  planned-maintenance basics, and turns breakdown, minor-stop and speed
  losses from an OEE loss tree into maintenance actions. Use whenever a
  request mentions MTBF, MTTR, breakdowns, machine downtime, repeat
  failures, a preventive maintenance plan, autonomous maintenance or an
  AM step audit, also when the data is already given: when asked to
  compute MTBF or MTTR, asked to sign off, pass or confirm an AM step
  audit, or asked whether the next AM step can start (TPM, autonome Instandhaltung, Jishu Hozen, geplante
  Instandhaltung, Wartungsplan, Störungen, Stillstände).
license: MIT
metadata:
  version: "1.0.0"
  category: improve
  standards: "IATF 16949 8.5.1.5"
---
# Total productive maintenance

## Conventions

- Autonomous maintenance (AM, autonome Instandhaltung, Jishu Hozen) is done by the operators; planned maintenance (PM, geplante Instandhaltung) by the maintenance team.
- AM is one pillar of total productive maintenance (TPM). Its steps follow the order of the Japan Institute of Plant Maintenance (JIPM): 1 initial cleaning, 2 contamination sources and hard-to-access areas, 3 provisional cleaning, lubrication and inspection standards, 4 general inspection, 5 autonomous inspection, 6 standardisation, 7 autonomous management. Some sites add a step 0 for safety and equipment functions.
- A failure (Störung) is an unplanned stop longer than the breakdown threshold, which is set by local policy. Shorter stops are minor stops. Planned maintenance stops are never failures.
- MTBF = operating time ÷ number of failures. MTTR = total breakdown downtime, stop to restart, ÷ number of failures. Times in hours, over one stated period.

## Inputs

- Mode: audit an AM step, diagnose breakdowns, set up planned maintenance, or route loss items from an OEE loss tree. Infer it from the request.
- Diagnose: the machine, the period, the planned production time, every failure with its downtime and failure mode, planned maintenance stops in the period, and earlier MTBF and MTTR if known. A split of downtime into response, diagnosis, waiting for parts, repair and test helps. Ask whether the site's MTTR counts stop to restart or hands-on repair only, and state the definition used.
- AM audit: the step claimed, the tag list (hung, closed, open, by type), the contamination sources and hard-to-access areas found and fixed, the cleaning time per shift, and the posted standards.
- Planned maintenance: the equipment list with criticality, the failure history, the current maintenance tasks and the spare-parts list.

Ask for missing inputs; never invent them.

- Without the failure count, the operating or planned production time for the period, and the downtime of each failure, do not give MTBF or MTTR values. Ask for them in one short list and stop. At most give the formulas and the blank `assets/breakdown-log.md`.
- Missing earlier MTBF and MTTR do not block a diagnosis; say that the trend cannot be judged yet.
- An AM audit without the tag counts or the contamination-source status cannot pass. Ask for them.

## Procedure

### A. Route loss items from an OEE loss tree

1. Take each loss item in minutes with its machine. Route it:

| Loss | Route |
|---|---|
| Breakdowns | Part B, then the planned-maintenance tasks in part D; AM steps 1–3 to restore basic conditions |
| Minor stops, reduced speed | AM steps 1–2 on that machine: clean, find and remove contamination and deterioration; then focused improvement on the top stop reason |
| Defects, start-up scrap | Hold the machine conditions that make good parts (quality maintenance), and structured problem solving; `solve-8d` for a customer complaint or a repeat problem |
| Set-up and adjustment | A changeover study in `improve-smed`, not this skill |
| Waiting for material or people, starved or blocked | Not an equipment loss; escalate in the tier meeting |

2. Start with the largest loss on the bottleneck machine. Check that the breakdown minutes match the maintenance log for the same period; if not, reconcile the data first.

### B. Diagnose breakdowns with MTBF and MTTR

1. Operating time = planned production time − breakdown downtime − planned stops inside that time.
2. MTBF = operating time ÷ failures. MTTR = breakdown downtime ÷ failures. Availability from MTBF and MTTR ≈ MTBF ÷ (MTBF + MTTR): operational, since MTTR includes waiting; inherent only when MTTR is hands-on repair.
3. Worked example (invented): planned 432 h, 8 failures with 24 h downtime, 2 planned stops of 4 h. Operating time = 432 − 24 − 8 = 400 h. MTBF = 400 ÷ 8 = 50 h. MTTR = 24 ÷ 8 = 3 h. Availability (operational) ≈ 50 ÷ 53 = 94.3%. Details and pooling rules in [MTBF and MTTR](references/mtbf-mttr.md).
4. Compare with the earlier period and decide:

| MTBF | MTTR | Meaning | Action |
|---|---|---|---|
| Falling | Stable | Failures more often: deterioration or a new failure mode | Restore basic conditions (AM steps 1–3), check the PM interval, root-cause the top failure mode |
| Stable | Rising | Repairs take longer: maintainability | Split downtime into response, diagnosis, waiting for parts, repair and test; act on the largest part (spares, skills, tools, access) |
| Falling | Rising | Both | Do both, worst failure mode first |

5. Sort failures by mode. A mode that repeats in the period (three or more times is a rule of thumb) needs a root-cause analysis and a lasting fix, not only faster repair. Use `solve-8d` when it caused a customer complaint or a safety issue.
6. Report MTBF, MTTR, availability, the trend, the downtime split and the top failure modes, each with an action, owner and date.

### C. Audit an autonomous-maintenance step

1. Audit at the machine, not from the report. The team audits itself first, then the area manager, then the TPM coordinator (rule of thumb from practitioner sources).
2. Check the step's exit criteria in [AM steps](references/am-step-criteria.md). Also check that every earlier step still meets its criteria.
3. A step passes only when every criterion is met. Never pass a step whose earlier step was skipped. Never confirm a pass the evidence does not show, even when asked to.
4. Typical stops:
   - Step 1: open tags without an owner and date; close tags within eight weeks (rule of thumb from Industry Forum).
   - Step 2 skipped: the same dirt comes back every shift, and cleaning time does not fall. Fix each contamination source at the source (seal, cover, guard, collection) and each hard-to-access area with the ECRS questions: eliminate, combine, rearrange, simplify. Then measure cleaning time against a target set by local policy.
   - Step 3: a standard nobody can complete within its time budget, or without visual controls.
5. For a fail, say plainly in the first lines that the step is not passed and that the next step (name the next step, e.g. step 4 general inspection) must not start yet. Then list each gap with its fix, owner and date, name what maintenance must provide, escalate missing resources to management, and set a re-audit date. Fill `assets/am-step-audit.md`.

### D. Set up planned-maintenance basics

1. Rank the equipment by criticality (safety, quality, bottleneck, no back-up, repair cost).
2. Choose a strategy per item with the table in [planned maintenance](references/planned-maintenance.md): breakdown maintenance only for non-critical items; time-based or condition-based maintenance for critical ones; improvement maintenance for repeat failure modes.
3. For each task: what, method, interval, who (operator or maintenance), time, and the spare parts. Set the interval from failure history or the maker's manual; otherwise mark it "set by local policy" and review it after the first failures or inspections.
4. Split the work: cleaning, lubrication and simple checks go to the operators' AM standard; technical tasks stay with maintenance. Leave no task without an owner.
5. Keep a breakdown log (`assets/breakdown-log.md`) for every failure, and a critical spare-parts list with minimum stock.
6. Track MTBF, MTTR and PM compliance (planned tasks done on time ÷ planned tasks due), and review them monthly (IATF 16949 8.5.1.5 asks for measurable maintenance objectives).

## Validation

Check before answering:

1. Planned maintenance stops are not counted as failures, and their time is not in the operating time.
2. MTBF uses operating time, not calendar or planned production time.
3. MTBF across machines is pooled (total operating time ÷ total failures), never averaged.
4. Every number was given by the user, derived from their data, or labelled.
5. No AM step passes with an earlier step skipped, or with open tags lacking an owner and date.
6. Every action has an owner and a date.

## Output

- Diagnose: MTBF, MTTR and availability with the calculation shown, the trend decision, the downtime split, the top failure modes and the action list.
- AM audit: `assets/am-step-audit.md` filled in, with pass or fail, the gaps, the fixes and the re-audit date.
- Planned maintenance: `assets/pm-plan-template.md` filled in, with intervals labelled by source.
- Loss routing: a table of loss item, minutes, route and next action.
- Write for the user in plain words; never cite this skill's step numbers, section names or file names.

## Pitfalls

1. Planned maintenance counted as failures, or downtime left in the operating time (fix: step B1).
2. MTBF averaged across machines (fix: [MTBF and MTTR](references/mtbf-mttr.md)).
3. Only faster repair for a repeat failure mode (fix: step B5).
4. AM reduced to a cleaning campaign, with step 2 skipped (fix: step C4).
5. Passing a step on paper or on request (fix: steps C1, C3).
6. AM treated as maintenance work handed to production, with no maintenance support (fix: steps C5, D4).
7. Intervals invented without failure data or a source (fix: step D3).

## Hand-offs

- A breakdown or repeat failure that caused a customer complaint or a safety issue goes to `solve-8d`.
- Missing maintenance resources and overdue tags are escalated through `lead-daily-routine`; a red breakdown KPI or overdue AM tags from that board arrive here.
- Breakdown, minor-stop and speed loss items arrive from `measure-oee`; report the MTBF and MTTR results back and re-measure OEE there with the same time model.
- Set-up and adjustment loss goes to `improve-smed`.
- Unplanned stops at the bottleneck arrive from `improve-tpt`; breakdowns seen during changeovers arrive from `improve-smed`.
- A maintenance-plan update from the prevent-recurrence step of `solve-8d` arrives here.
- An uptime kaizen burst arrives from `improve-vsm`; breakdowns at a kanban supplier arrive from `improve-kanban-pull`.
- After a repair, re-check the stability of the critical characteristics with `measure-spc`; signals traced to tool wear or machine condition arrive from there.
- Improvement topics that need a workshop or a sustain plan go to `improve-kaizen`.
- Breakdowns and minor stops seen on a gemba walk arrive from `lead-gemba-walk`.
- A breakdown root cause is drilled with `solve-5why`; a root cause in machine condition or maintenance arrives from `solve-5why`, `solve-fishbone`, `solve-pdca` and `solve-dmaic`; maintenance not done as planned arrives from `audit-process`.
- Error-proofing device checks and maintenance-related controls arrive from `plan-control-plan` and go back there as control-plan rows; operator cleaning and inspection standards go to `plan-workstation-instructions`.
