---
title: improve-vsm
description: Draws and checks current-state and future-state value stream maps for one product family, and turns the future state into a loop plan with owners, targets and 30/60/90-day reviews.
---

<span class="status available">available</span>

Draws and checks value stream maps (Wertstromanalyse, Wertstromdesign) for one product family, door to door: the current state with its data boxes and inventory ladder, the future state answered question by question, and a loop plan that turns the design into work.

## What you give and what you get

| You give | You get |
|---|---|
| The product family and its boundary, customer demand with its period, the working pattern, and per process the cycle time, changeover, uptime, operators and batch size, plus every inventory count | Takt and pitch, the inventory ladder in days with the production lead time and processing time, the current-state problems, the eight future-state answers, kaizen bursts, the future ladder and a loop plan |
| A future-state map to check | Each supermarket, FIFO lane and the pacemaker checked against takt and the run interval, every claimed saving checked against its cause |

Without customer demand there is no takt, no pitch and no inventory days. The skill asks for demand and working time and stops; it never presents a takt or a lead time from an assumed demand. Missing changeover or uptime data block only the checks that use them.

## Rules it applies

- One map per product family, walked from shipping back to receiving.
- Takt and the ladder use the same demand period, the same working time and one flow unit, and the takt convention is stated.
- Inventory days = count ÷ daily demand; the production lead time is their sum.
- The pacemaker is a scheduling point, never the bottleneck, and exactly one process gets the schedule.
- No inventory is removed from the future map while its cause stays: a supermarket after a shared batch process covers at least the run interval plus replenishment time, until a changeover burst shortens it.
- Every loop has an owner, a numeric target and dates; the pacemaker loop comes first, and 30/60/90-day reviews are set.

## Where the work goes next

Supermarket card counts and pitch go to [`improve-kanban-pull`](/skills/improve-kanban-pull/), and kaizen bursts that need an event to [`improve-kaizen`](/skills/improve-kaizen/). Changeover bursts go to [`improve-smed`](/skills/improve-smed/), uptime bursts to [`improve-tpm`](/skills/improve-tpm/), a process above takt with manual work to [`improve-line-balancing`](/skills/improve-line-balancing/), and measured throughput time to [`improve-tpt`](/skills/improve-tpt/). The current-state walk can be planned with [`lead-gemba-walk`](/skills/lead-gemba-walk/), and loop targets are tracked in [`lead-daily-routine`](/skills/lead-daily-routine/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: the current state, the future-state questions and the loop plan, each with its sources.
- `assets/`: a value stream study template.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/improve-vsm).
