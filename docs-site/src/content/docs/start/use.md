---
title: Use
description: Ask your agent in your own words. It picks the skill whose description matches your request.
---

You do not call a skill by name. Ask your agent in your own words, and it loads the skill whose description matches the request.

Examples for `lead-daily-routine`, the skill available today:

- *"Design a tier meeting cascade for our plant: three levels, two shifts, the early shift starts at 06:00."*
- *"Here are today's board values and open actions. Build the agenda for the tier 1 meeting."*
- *"Our tier 2 meeting runs 40 minutes and people stop coming. Audit the routine."*

The skill works in three modes, design, run and audit, and picks the mode from your request. When something it needs is missing, it asks for it. It does not invent board values or shift times.

## Start a skill by name

In Claude Code you can also start a skill directly:

```
/shopfloor-skills:lead-daily-routine
```

## Give it real data

The skills work best with the facts of your line: shift times, KPIs and targets, today's board, the actions that are open. Remove the names of people, customers and products before you paste data in, if your rules ask for that.

## What the skills do not do

- They do not connect to your MES, ERP or board software. You bring the data.
- They do not reproduce the text of any standard. They point to clause numbers and summarize in their own words. Use the official documents for the binding text.
