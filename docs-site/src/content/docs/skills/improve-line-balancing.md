---
title: improve-line-balancing
description: Balances manual assembly lines and cells in a fixed order - volume, mix, takt, ergonomics, then a fill-up yamazumi - and outputs the savings and the standard work.
---

<span class="status available">available</span>

Balances manual assembly lines and cells (Austaktung) in a fixed order: volume, mix, takt, ergonomics, then a fill-up yamazumi. It merges or splits stations, checks the machines against takt, and outputs the standard work for the new balance.

## What you give and what you get

| You give | You get |
|---|---|
| Customer demand from average shipments, the shift pattern and scheduled breaks, the variants and their shares, the work elements in order with observed times, the machine cycle times, any ergonomic results, and the current line | Takt, the operator count with its rounding rule, an ergonomic screen, the current and new yamazumi as tables, a machine check, the savings in operators, stations, machines and units per labour hour, and the standard work per operator |

If demand, working time or element times are missing, the skill asks for them in one short list and stops. It gives no takt, operator count or saving on invented numbers. Missing ergonomic data does not block the calculation; every lift or awkward posture is marked "ergonomics not assessed" and listed as an open action.

## Rules it applies

- Takt uses effective time with only scheduled stops removed. Downtime and changeovers are never subtracted; they are fixed at their source.
- Takt comes from average shipments, not from orders or a peak day.
- Fill-up, not equal shares: each operator is loaded up to the planned cycle time, and the gap on the last operator is the visible kaizen target.
- Every variant is checked: no operator may be overloaded by any variant.
- Ergonomics comes before loading. High-risk elements are screened with the revised NIOSH lifting equation, RULA or REBA, and get a redesign action with an owner and date.
- Every machine cycle must fit within takt.

## Where the work goes next

The downtime, minor-stop and changeover losses kept out of takt go to [`measure-oee`](/skills/measure-oee/), [`improve-tpm`](/skills/improve-tpm/) and [`improve-smed`](/skills/improve-smed/). WIP and throughput time after the rebalance go to [`improve-tpt`](/skills/improve-tpt/). Hour-by-hour output is tracked in [`lead-daily-routine`](/skills/lead-daily-routine/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: takt and operators, the fill-up yamazumi, ergonomics screening and standard work, each with its sources.
- `assets/`: a balance worksheet and a standard-work sheet.
- `scripts/balance.py`: an optional standard-library calculator. The procedure gives the same result by hand.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/improve-line-balancing).
