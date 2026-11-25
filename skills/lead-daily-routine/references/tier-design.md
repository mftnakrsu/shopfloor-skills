# Tier design

How to choose the tiers, times, timeboxes, agenda and escalation rules of a tier-meeting cascade (Regelkommunikation), and where the defaults in SKILL.md come from.

## Contents

- Tier models
- Times and timeboxes
- Standing agenda
- Escalation
- Leader standard work
- IATF 16949 pointers
- Introducing a routine
- Sources

## Tier models

Sources agree on the mechanics and disagree on the labels.

| Model | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Source |
|---|---|---|---|---|---|
| Four tiers, bottom-up | Front-line teams, first in the day | Supervisors; take what tier 1 could not solve | Department managers; cross-team issues and department KPIs | Plant leadership, last in the day; plant-wide problems and resources | Kaizen Institute |
| Three tiers | Team leader with the team (start-up meeting) | Supervisor with team leaders and support-group representatives | Value-stream manager with supervisors and support staff | — | Mann |
| Two tiers, for small sites | Line huddle | Site huddle | — | — | Fabrico |

- The meetings are short, held standing at the same time each day, and agree actions instead of solving problems (Kaizen Institute).
- Labels conflict. One trade source calls tier 1 the front-line supervisors and tier 2 the middle managers (Quality Magazine). Another says a value-stream leader often chairs tier 2 and the plant manager tier 3 (Quality Digest). So ask who chairs each level, number the tiers from the line upward, and map the local names to those numbers.
- Not every site runs every tier daily. In German expert interviews, the middle and upper levels met daily or weekly (BVL). Where an upper tier meets less often than daily, name a daily contact who can answer escalations the same day.
- Escalation is what links the tiers. Without it, a cascade is only a set of separate meetings (TeamGuru).

## Times and timeboxes

| Source | Tier 1 | Higher tiers |
|---|---|---|
| iFactory (vendor) | 10–12 min | tier 2 15 min; tier 3 15–20 min |
| Fabrico (vendor) | about 10 min | 15–30 min |
| IEOM 2024 (practitioners at a machine-tool maker) | stand-ups of 15–30 min at every level | same |
| TeamGuru (example) | 10 min standing huddle at 06:45 | — |

Together: tier 1 takes about 10–15 min, higher tiers 15–30 min.

- The cascade starts early in the morning at the first level and ends at plant-manager level (IEOM 2024).
- Example cascade observed in a German audit at a coatings manufacturer (ZielKom report):

| Time | Meeting |
|---|---|
| 06:00 | Team stand-up at shift start |
| 06:30 | Cross-functional daily planning |
| 10:30 | Segment-leader stand-up |
| 11:00 | Plant-manager stand-up |

- Its top tier meets later than the default below; answers can still return to the line in the same shift.
- The top tier reviews only the red items. In one automotive assembly plant, managers walk the gemba first and then meet at 09:00 in one place to go through the reds only (Womack, via LEI).

**Defaults used in SKILL.md** (rule of thumb, drawn from the ranges above):

| Tier | Start | Timebox |
|---|---|---|
| 1 | within the first hour of the shift | ≤15 min |
| 2 | 30–60 min after tier 1 | about 15 min |
| 3 | 30–60 min after tier 2 | 15–20 min |
| 4 | 30–60 min after tier 3, ending before late morning | 15–30 min |

A shift that starts after the cascade escalates to a named leader on shift, who can decide and answers within the shift. Only what needs a higher tier waits for the next morning's cascade, marked as an exception with an owner and a due date (rule of thumb).

Worked example (invented round numbers): the shift starts at 06:00. Tier 1 runs 06:05–06:15, tier 2 06:45–07:00, tier 3 07:30–07:50 and tier 4 08:30–09:00. A problem raised at 06:10 reaches tier 4 by 08:30, and its answer can be back at the line before 10:00, well inside the shift.

## Standing agenda

- Tier 1 covers yesterday's results against target, today's plan and new problems (Kaizen Institute).
- When a KPI is off target, the team agrees an action, an owner and a follow-up date, and checks progress at the next meeting (Kaizen Institute).
- Keep to current status, goals and tasks. Take technical detail, detailed problem solving and planning out of the meeting (IEOM 2024).
- Before go-live, agree fixed meeting rules (moderation, duration, content) and hold a trial meeting under them (ifaa).
- The order safety, quality, delivery, cost, people is a common convention, not a standard. Local boards often use the German order Qualität, Kosten, Logistik, Sicherheit, Personal (ifaa). Keep one order at every tier, so a topic is easy to follow up the cascade.

Worked example of a timed tier 2 agenda (invented round numbers; set the split by local policy):

| Clock time | Item | Minutes |
|---|---|---|
| 06:45 | Safety | 1 |
| 06:46 | Quality | 3 |
| 06:49 | Delivery | 3 |
| 06:52 | Cost and productivity | 2 |
| 06:54 | People | 1 |
| 06:55 | Actions due today | 2 |
| 06:57 | New problems | 1 |
| 06:58 | Escalations up and answers down | 2 |
| 07:00 | End | 15 in total |

## Escalation

1. A problem a tier cannot solve goes up the same day with a named owner, and the answer goes back to the team that raised it (Kaizen Institute).
2. An escalation is a request for support (Peters 2009, as cited in the BVL report). Use this framing in the meeting, so nobody hides a red to avoid blame.
3. Triggers: tier 1 escalates when a problem recurs or cannot be fixed the same day. Tier 2 escalates when its support staff cannot resolve the problem, which usually means deeper root-cause work is needed (SafetyChain deck).
4. Escalate to someone who can decide. An alert to a person without decision authority loses the time it was meant to save (BVL).
5. Keep one written escalation list per board. In German interviews, escalation was often verbal or a card moved to the next board, and actions were copied between board, spreadsheet and notes, so nobody could trace them across levels (BVL).
6. If no action can be agreed because the cause is unclear, start structured problem solving (for example an A3, a one-page problem-solving report) or escalate. The action stays on the board until the improvement is achieved (BVL).

Deviation management (Abweichungsmanagement), step by step:

1. See the deviation: a red on the board, or an andon call (a signal from the line that asks for help).
2. Contain it at once (Sofortmaßnahme).
3. Cause known: a simple action with owner and date. Cause unknown: structured problem solving outside the meeting.
4. Escalate when the problem is outside the tier's authority or resources.
5. Verify the effect and update the standard.

(IEOM 2024; Peters 2009, as cited in the BVL report.)

### Andon time ladder (illustrative)

Scale response times to takt: the faster the work cycle and the more a minute of downtime costs, the faster each level must respond (Gemba Academy). Example for a 60-second cycle:

| Who responds | Within |
|---|---|
| Team leader | seconds |
| Group leader | 1 min |
| Area engineer or manager | 5 min |
| Plant manager | 10 min |

Contain at once, and aim for a root-cause countermeasure within 24 hours, depending on process stability, severity and the skills of the support staff (Gemba Academy). These values illustrate the principle; they are not a standard. Set your own ladder by local policy.

## Leader standard work

- Each level checks the level below: team leaders confirm that operators follow standard work, supervisors confirm the team leaders' routines, and value-stream managers confirm the supervisors' routines (Mann).
- Diagnostic question: does the leader's own supervisor review the leader's standard work every day? (Mann)
- The share of working time spent in fixed routine falls with each level up. Reported values, a gradient and not targets (Mann, via Business901):

| Level | Share of time in standard work |
|---|---|
| Operator | about 95% |
| Team leader | about 80% |
| Supervisor | about 50% |
| Value-stream manager | about 25% |
| Executive | about 10% |

- Other sources report other values, for example about 70% for a team leader and about half for an area manager (TeamGuru). Use the shape of the gradient, not the numbers.
- Five elements of leader standard work (Murli, LEI): a daily team reflection; gemba walks on a fixed route at a fixed time; fast response to abnormalities; mentoring at every level; strategy deployment with monthly progress reviews.
- Confirm that countermeasures and standards still hold, for example with a T-card board (IEOM 2024).

## IATF 16949 pointers

As of 2026-11-25: IATF 16949:2016, with the sanctioned interpretations of November 2024 and the FAQs of May 2022. The summaries below are in our own words; use the official documents for the binding text.

- **8.5.6.1.1 Temporary change of process controls.**
  - Keep a list of the process controls (inspection, measuring, test and error-proofing) that have approved backup or alternate methods.
  - Write standard work for each alternate method.
  - Review the use of alternates at least once a day, for example in a tier meeting or a layered process audit.
  - Verify the process before going back to the primary control, and keep product made under an alternate traceable, for example by the first and last piece of each shift.
  - The interpretations add: not every control needs an alternate, but every alternate must be on the list and in the process flow, PFMEA, control plan and standard work. If a primary control fails and no alternate exists, assess the risk in the FMEA first; if an alternate is approved, write its standard work, verify it through daily management, and revalidate when the primary control is back (SI 11; FAQ 17).
- **9.1.1.1 Monitoring and measurement of manufacturing processes.**
  - Verify that the process flow, PFMEA and control plan are followed in practice: measurement methods, sampling, acceptance criteria and records of measured values.
  - When acceptance criteria are not met, a reaction plan and an escalation process apply.
  - Record significant process events, such as a tool change or a machine repair.

How the skill uses them: alternates in use are listed and reviewed daily at tier 1 or tier 2; a result that triggers a reaction plan appears as a quality red with an escalation path.

## Introducing a routine

A six-phase introduction model, tested in small and medium-sized firms (ifaa):

1. Set the goals and choose a pilot area with known, recurring problems. Half a day, for management and the production head.
2. Inform everyone affected, including the works council (Betriebsrat), and make clear that the KPIs are not for watching people. Half a day.
3. Introduction workshop: two half days of at most 4 hours each, with 6–8 participants. Day 1: goals, KPI sources and a board draft. Day 2: review, the meeting rules, a trial meeting and a presentation to management, where each participant presents their own part.
4. Trial: start the daily meetings at once and plan for about 3 months.
5. Check-up: neutral observers attend real meetings and check rigour, rule adherence, punctuality, participation, how current and sound the KPIs are, and action tracking.
6. Validation workshop of 2–3 hours, then roll out the cascade.

Top management takes part in meetings on site, during and after the introduction (ifaa).

## Sources

- Kaizen Institute: [How should daily management be structured in a manufacturing plant?](https://kaizen.com/insights/daily-management-manufacturing-plant/)
- Mann, D.: *Creating a Lean Culture*, 3rd ed., Productivity Press, 2015, ISBN 9781482243239. [Publisher listing](https://www.routledge.com/Creating-a-Lean-Culture-Tools-to-Sustain-Lean-Conversions-Third-Edition/Mann/p/book/9781482243239). Secondary summaries: [SecurityInfoWatch](https://www.securityinfowatch.com/home/article/10537858/home), [LeanBlog](https://www.leanblog.org/9)
- Fabrico: [Tier meetings](https://www.fabrico.io/cs/blog/tier-meetings/)
- iFactory: [Daily management system: tier 1-2-3 meeting structure](https://ifactoryapp.com/industries/manufacturing-plant/daily-management-system-tier-1-2-3-meeting-structure)
- Dinkelmann, Weinmann: "Maturity Steps towards a Digitally Integrated Shop Floor Management", IEOM 2024, DOI 10.46254/EU07.20240100. [PDF](https://ieomsociety.org/proceedings/2024germany/100.pdf)
- TeamGuru: [Lean daily management](https://www.teamguru.com/guides/lean-daily-management); [Tier meetings](https://www.teamguru.com/guides/tier-meetings); [Leader standard work](https://www.teamguru.com/guides/leader-standard-work)
- TU Darmstadt PTW et al.: ZielKom final report, BMBF project 2014–2017. [PDF](https://tuprints.ulb.tu-darmstadt.de/server/api/core/bitstreams/a0b83c65-e75d-4392-90ab-4500cecf4bc8/content)
- Womack: [Value-stream walk, management walk, or just walking around?](https://www.lean.org/the-lean-post/articles/value-stream-walk-management-walk-or-just-walking-around/), The Lean Post, LEI
- Quality Magazine: [The role of lean daily management in sustaining a lean culture](https://www.qualitymag.com/articles/98482-the-role-of-lean-daily-management-in-sustaining-a-lean-culture)
- Quality Digest: [article on tier meetings](https://qualitydigest.com/node/18175)
- BVL/IGF 19372 N: ShopfloorPulse final report. [PDF](https://www.bvl.de/files/1951/2125/2131/2133/Abschlussbericht_ShopfloorPulse_19372_N.pdf)
- SafetyChain: [Avoiding risk: using a tiered management system to improve daily execution](https://www.slideshare.net/slideshow/avoiding-risk-using-a-tiered-management-system-to-improve-daily-execution/252685323) (slide deck)
- Gemba Academy: [Ask Gemba: nuts and bolts of the andon system](https://blog.gembaacademy.com/?p=11425)
- Business901: [Mann on leader standard work](https://business901.com/?p=12803)
- Murli: [Standard work for lean leaders: one of the keys to sustaining performance gains](https://www.lean.org/the-lean-post/articles/standard-work-for-lean-leaders-one-of-the-keys-to-sustaining-performance-gains/), The Lean Post, LEI, 2013
- Conrad, Eisele: *Shopfloor-Management*, ifaa Betriebspraxis & Arbeitsforschung 235, 2019. [PDF](https://www.arbeitswissenschaft.net/fileadmin/Downloads/Angebote_und_Produkte/Publikationen/ifaa_BA_235_Shopfloormanagement.pdf)
- DNV: [IATF 16949:2016 comparison matrix](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf)
- IATF: [Sanctioned interpretations, November 2024](https://www.iatfglobaloversight.org/wp/wp-content/uploads/2024/11/IATF-16949-SIs-Nov-2024.pdf); [FAQs, May 2022](https://www.iatfglobaloversight.org/wp/wp-content/uploads/2022/05/IATF-16949-FAQs_May-2022.pdf)
