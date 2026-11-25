---
title: solve-8d
description: Leads an 8D problem solving from D0 to D8 for customer complaints, field failures and repeat defects, with an evidence gate at every discipline.
---

<span class="status available">available</span>

Leads an 8D from D0 to D8 for customer complaints (Reklamation), field failures, repeat defects and serious internal problems, and checks whether an open 8D can be closed.

## Two modes

The skill picks the mode from your request.

| Mode | You give | You get |
|---|---|---|
| Run an 8D | The complaint facts: part, defect, quantity affected and checked, where and when found, lots or date codes, delivery dates, the customer's deadlines, what has been done so far | Each discipline in order, with its gate: team, a quantified problem description, containment of all suspect stock, occurrence and escape root causes with a test for each, permanent actions, document updates and the 8D report |
| Check for closure | An existing 8D | A plain yes or no, then every failed item with what is missing and the fix, discipline by discipline |

If the complaint facts are missing, the skill asks for them in one short list and stops. It does not invent defects, numbers, dates or causes. A missing PFMEA, control plan or customer deadline does not block D0 to D3; it is marked "to be confirmed" and listed as an open question.

## Rules it applies

- Two root causes, always: why the defect was made (occurrence) and why it was not detected before the customer got it (escape). Each is verified with an on/off test.
- The problem description (D2) holds facts only, with no cause and no solution.
- Containment covers six locations: customer stock, in transit, finished goods, work in process, incoming or supplier stock, and service parts. The sort method must be able to find known bad parts, so it is never the check that already missed the defect.
- "Operator error" is never a final cause. The skill asks why the process allowed it.
- Retraining alone is a weak action. Error-proofing or detection at the source comes first.
- D7 closes the loop: PFMEA, control plan, station instructions, and a read-across to similar parts and lines.

## What is in the folder

- `SKILL.md`: the procedure and the closure checklist.
- `references/`: the gate for each discipline, root-cause verification and the 8D report layout, each with its sources.
- `assets/`: an 8D report template and a containment plan.

## The agent

The [`8d-moderator`](/skills/agents/) agent loads this skill and moderates the whole 8D with the team.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/solve-8d).
