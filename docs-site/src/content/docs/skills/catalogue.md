---
title: Skills catalogue
description: All 20 planned skills of shopfloor-skills, grouped by stage, with what each one does and whether it is available yet.
---

The design plans 20 skills in six stages. The prefix of a skill's name is its stage. Skills arrive in batches; this page shows the state of each one.

- <span class="status available">available</span>: in the repository and installed with the plugin.
- <span class="status soon">coming soon</span>: being written and tested now.
- <span class="status planned">planned</span>: designed, not written yet. The description says what the skill will do.

## lead: daily shopfloor leadership

| Skill | Status | What it does |
|---|---|---|
| [`lead-daily-routine`](/skills/lead-daily-routine/) | <span class="status available">available</span> | Designs, runs and audits tier meetings: the cascade, the SQDCP board, same-day escalation with a reply path, action follow-up and routine adherence |
| `lead-gemba-walk` | <span class="status planned">planned</span> | Plans, runs and follows up gemba walks, with an observation log and an optional layered-audit segment |

## measure: see the losses

| Skill | Status | What it does |
|---|---|---|
| [`measure-oee`](/skills/measure-oee/) | <span class="status available">available</span> | Computes OEE and TEEP from an agreed time model, builds a loss tree in minutes, and catches averaging errors |
| `measure-spc` | <span class="status planned">planned</span> | Chooses the control chart, computes limits, applies out-of-control rules, and links each signal to the reaction plan and tier escalation |

## improve: productivity and flow

| Skill | Status | What it does |
|---|---|---|
| [`improve-tpt`](/skills/improve-tpt/) | <span class="status available">available</span> | Reduces throughput time (Durchlaufzeit): measures it with a Little's Law cross-check, finds critical WIP, and caps it |
| `improve-vsm` | <span class="status planned">planned</span> | Draws current and future-state value streams and ends in a loop plan with owners and a 30/60/90 review |
| `improve-kanban-pull` | <span class="status planned">planned</span> | Chooses a supermarket, FIFO lane or CONWIP, sizes the loops with a cited formula, and sets the pitch |
| [`improve-line-balancing`](/skills/improve-line-balancing/) | <span class="status available">available</span> | Balances manual lines in a fixed order, from volume and mix to takt, ergonomics and a fill-up yamazumi, and outputs standard work |
| [`improve-smed`](/skills/improve-smed/) | <span class="status available">available</span> | Runs a changeover study from video, separates internal from external work, and decides between more capacity and smaller lots |
| [`improve-tpm`](/skills/improve-tpm/) | <span class="status available">available</span> | Audits autonomous-maintenance steps, covers planned-maintenance basics, and diagnoses with MTBF and MTTR |
| `improve-kaizen` | <span class="status planned">planned</span> | Picks the improvement format, from a point fix to a kaizen event or an A3, and ends every result in a new standard |

## plan: the documents that keep a line stable

| Skill | Status | What it does |
|---|---|---|
| `plan-control-plan` | <span class="status planned">planned</span> | Builds or reviews a process control plan as the master for all station documents, with reaction plans and review triggers |
| `plan-workstation-instructions` | <span class="status planned">planned</span> | Drafts and reviews station inspection and work instructions from control-plan rows, and runs consistency checks |

## solve: root cause and problem solving

| Skill | Status | What it does |
|---|---|---|
| [`solve-8d`](/skills/solve-8d/) | <span class="status available">available</span> | Runs an 8D from D0 to D8: containment, occurrence and escape root causes, verification, and the PFMEA and control-plan updates |
| `solve-5why` | <span class="status planned">planned</span> | Builds 5-Why chains for occurrence, detection and system causes, with an evidence check on every link |
| `solve-fishbone` | <span class="status planned">planned</span> | Turns a 6M brainstorm into cause hypotheses that can be tested |
| `solve-is-is-not` | <span class="status planned">planned</span> | Scopes a problem with Is/Is-Not, distinctions and changes, then eliminates hypotheses |
| `solve-pdca` | <span class="status planned">planned</span> | Runs one PDCA or A3 cycle on a defined problem or improvement |
| `solve-dmaic` | <span class="status planned">planned</span> | Runs DMAIC on chronic problems that have plenty of data |

## audit: check the system

| Skill | Status | What it does |
|---|---|---|
| `audit-process` | <span class="status planned">planned</span> | Runs process audits, layered process audits and shopfloor-management self-audits, and maps findings to ISO 9001 and IATF 16949 clauses |

For the order in which the skills arrive, see the [CHANGELOG](https://github.com/mftnakrsu/shopfloor-skills/blob/main/CHANGELOG.md). For how they hand work to each other, see [How it works](/guides/how-it-works/).
