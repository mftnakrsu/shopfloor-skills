---
title: improve-kanban-pull
description: Designs and sizes pull systems - chooses a supermarket with kanban, a FIFO lane or CONWIP, sizes each loop with the full replenishment lead time, checks supplier capacity and sets the pitch.
---

<span class="status available">available</span>

Designs and sizes pull systems (Ziehsystem) on the shop floor: chooses between a supermarket with kanban, a FIFO lane and CONWIP, sizes each loop with Monden's kanban formula, checks that the supplier has the capacity, and sets the pitch at the pacemaker.

## What you give and what you get

| You give | You get |
|---|---|
| Per part number or group: demand per day and its swing, the number of part numbers, made to stock or to order | The system per part group with the reason |
| Per loop: every component of the replenishment lead time, the container quantity, how the supplier batches cards, its capacity and change-over time, and the safety factor | The lead-time build-up, the card count rounded up, the maximum stock in the loop, FIFO and CONWIP maxima |
| Available time, demand and pack-out quantity at the pacemaker | Takt, pitch and the paced withdrawal |

A card count needs demand, every component of the lead time, the container quantity and the safety factor. If one is missing, the skill asks for it and stops; it never gives a card count from an assumed lead time. It asks for the safety factor instead of picking one.

## Rules it applies

- The replenishment lead time is the full loop, from an empty container back to a full one at the customer, never the processing time alone.
- Demand, lead time and container quantity use one unit and one clock; the card count is rounded up.
- Supplier capacity must exceed total demand; if it does not, capacity comes before cards.
- No supermarket for parts that cannot be stocked; high-variety, built-to-order parts get a FIFO lane or CONWIP.
- A CONWIP card count is checked for output with the practical-worst-case formula.
- Cards are recalculated when demand, lead time or the container change, and removed one at a time while the customer never waits.

## Where the work goes next

A future state that calls for supermarkets or a pacemaker arrives from [`improve-vsm`](/skills/improve-vsm/). Long supplier change-overs go to [`improve-smed`](/skills/improve-smed/), breakdowns to [`improve-tpm`](/skills/improve-tpm/), and CONWIP throughput checks to [`improve-tpt`](/skills/improve-tpt/). Card-reduction events go to [`improve-kaizen`](/skills/improve-kaizen/), demand-swing analysis to [`measure-spc`](/skills/measure-spc/), and stock-outs are reported in [`lead-daily-routine`](/skills/lead-daily-routine/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: system choice and the kanban formula, each with its sources.
- `assets/`: a kanban loop sheet.
- `scripts/kanban_calc.py`: an optional calculator for cards, pitch and CONWIP (Python standard library).

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/improve-kanban-pull).
