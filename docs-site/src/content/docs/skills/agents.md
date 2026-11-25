---
title: Agents
description: The six subagents of shopfloor-skills, what each one does, and the skills each one uses.
---

An agent takes a whole job, such as leading an 8D, and uses several skills to do it. Each agent loads at most three skills at the start and loads the others only when it needs them, which keeps its context small.

Two pairs split the work on purpose. `problem-solving-coach` handles everyday line problems and hands over to `8d-moderator` when a full 8D is needed. `inspection-planner` builds the documents, and `pfmea-chain-checker` reviews them on its own, as a second pair of eyes.

| Agent | Status | What it does | Edits files |
|---|---|---|---|
| `skill-reviewer` | <span class="status available">available</span> | A tool for maintainers. Reviews a skill or agent against the project's writing rules and the Agent Skills specification, and reports fixes with file and line | No |
| `8d-moderator` | <span class="status available">available</span> | Leads an 8D team from D0 to D8 for customer complaints, repeat defects and serious escalations, and closes the loop in the control plan and station instructions | Yes |
| `problem-solving-coach` | <span class="status available">available</span> | Takes everyday line problems, such as red KPIs, OEE losses and gemba findings, picks the root-cause method, and hands over to `8d-moderator` when an 8D is needed | Yes |
| `inspection-planner` | <span class="status available">available</span> | Builds the control plan, derives the station inspection and work instructions from it, and runs the consistency checks | Yes |
| `pfmea-chain-checker` | <span class="status available">available</span> | Checks, station by station, that every PFMEA failure mode that needs a control has one in the control plan, with a reaction plan and a matching instruction. Reports gaps and never edits | No |
| `process-auditor` | <span class="status available">available</span> | Runs process audits, layered process audits and shopfloor-management self-audits, backed by gemba evidence | Yes |

`skill-reviewer` is for people who write skills for this project. It reads and reports; it never changes a file.

## In other tools

Agents are written once, in Claude Code format. For OpenCode, Qwen Code and Cursor, the [installer](/start/install/) converts each agent. Read-only agents stay read-only in every tool. `npx skills` installs skills only, without agents.
