# Changelog

All notable changes to this project are documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-11-25

First release: 20 Agent Skills and 6 subagents for production lines, as a Claude Code plugin and for OpenCode, Qwen Code and Cursor through `scripts/install.py`.

### Added
- Lead skills: `lead-daily-routine` (tier meetings, SQDCP board, same-day escalation, routine audit), `lead-gemba-walk` (process, management-system and value-stream walks, optional LPA segment).
- Measure skills: `measure-oee` (OEE and TEEP, loss tree, calculator), `measure-spc` (chart choice, limits, run rules, reaction links, calculator).
- Improve skills: `improve-tpt` (throughput time, Little's Law, critical WIP, calculator), `improve-vsm` (current and future state, loop plan), `improve-kanban-pull` (supermarket, FIFO or CONWIP, kanban sizing, calculator), `improve-line-balancing` (takt, ergonomics, yamazumi, calculator), `improve-smed` (changeover study, EPEI), `improve-tpm` (MTBF and MTTR, AM step audits, planned maintenance), `improve-kaizen` (format choice, 30/60/90 sustain plan).
- Plan skills: `plan-control-plan` (control plan with reaction plans, Safe Launch and family variants), `plan-workstation-instructions` (station instructions from control-plan rows, seven consistency checks).
- Solve skills: `solve-8d`, `solve-5why`, `solve-fishbone`, `solve-is-is-not`, `solve-pdca`, `solve-dmaic`.
- Audit skill: `audit-process` (process audits, VDA 6.3-style scoring, LPA programme, SFM self-audit, clause mapping).
- Agents: `8d-moderator`, `problem-solving-coach`, `inspection-planner`, `pfmea-chain-checker` (read-only), `process-auditor`, and the maintainer tool `skill-reviewer` (read-only).
- Hand-off loop across all skills and agents, checked by the linter.
- `claude plugin eval` cases: 3 per skill, 1 per agent.
- Linter, installer with agent conversion, pre-commit hook, CI (tests on Ubuntu and Windows, lint, `claude plugin validate --strict --profile directory`, `agentskills validate`).
- Brand kit, plugin icon, and the documentation site with a Türkçe page.

### Notes
- Smaller models such as Haiku may not load a skill on their own; name it in the prompt.

[1.0.0]: https://github.com/mftnakrsu/shopfloor-skills/releases/tag/v1.0.0
