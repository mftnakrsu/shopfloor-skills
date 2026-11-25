---
description: The skill-reviewer agent finds the planted problems in a weak draft skill without editing anything.
tags: [agent, skill-reviewer]
timeout_seconds: 600
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---
Use the skill-reviewer agent to review the draft skill below. Treat it as the file skills/measure-oee/SKILL.md. Do not change any files; I only want the review.

```markdown
---
name: measure-oee
description: >-
  This skill is about OEE.
license: MIT
metadata:
  version: "1.0.0"
  category: measure
  standards: ""
---
# OEE

## Conventions
OEE stands for Overall Equipment Effectiveness. It was introduced as part of TPM and is one of the most popular KPIs in manufacturing. It combines availability, performance and quality into a single number that shows how well equipment is used compared with its full potential.

## Inputs
- Planned production time, downtime, ideal cycle time, total count, good count.

## Procedure
1. Compute OEE = availability × performance × quality.
2. World-class OEE is 85%, so compare the result against that.
3. At Werk Musterstadt we report OEE every Monday.

## Validation
- Check that the result looks plausible.

## Output
- A number.

## Pitfalls
- Wrong data.

## Hand-offs
- Losses → `improve-smed`
```
