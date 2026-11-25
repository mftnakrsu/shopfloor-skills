---
title: improve-tpt
description: Calculates, checks and reduces the throughput time of a production line or shop, with a Little's Law cross-check, the practical worst case and a WIP cap.
---

<span class="status available">available</span>

Calculates, checks and reduces throughput time (Durchlaufzeit, lead time): the average time one unit spends between two named inventory points.

## What you give and what you get

| You give | You get |
|---|---|
| The boundary and flow unit, WIP counts at the same points on several days, good output over the same window, process times and parallel machines per step, working time and demand | The throughput time from Little's Law with a cross-check, the raw process time, bottleneck rate and critical WIP, a comparison with the practical worst case, the lever to pull first, a WIP cap checked against output, and a tracking plan |

If WIP or output is missing, the skill asks for the boundary, flow unit, WIP counts, output and working time in one short list and stops. It never presents a throughput time from an assumed output rate. Missing process times block only the reference points and the cap check; the throughput time is measured first.

## Rules it applies

- Every term is mapped first. "Cycle time" alone is ambiguous and is never used unqualified.
- Throughput time comes from measured WIP and output, never from summed station cycle times or ERP standard times.
- The Little's Law result is cross-checked against tagged units; a large gap means broken data.
- A faster station that is not the bottleneck does not raise output, and shortens throughput time only when WIP is already near its critical level.
- When the bottleneck is highly loaded, WIP is not cut first, because that costs output. Variability at the bottleneck is attacked instead.
- Every WIP cap is checked against the required output and stepped down while output holds.

## Where the work goes next

Long set-ups at the bottleneck go to [`improve-smed`](/skills/improve-smed/), unplanned stops there go to [`improve-tpm`](/skills/improve-tpm/), bottleneck losses that need a loss tree go to [`measure-oee`](/skills/measure-oee/), and station imbalance on a manual line goes to [`improve-line-balancing`](/skills/improve-line-balancing/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: terms and measurement, the flow formulas, and the WIP and variability levers, each with its sources.
- `assets/`: a throughput-time study and a WIP count sheet.
- `scripts/tpt_calc.py`: an optional standard-library calculator. Every result can be computed by hand.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/improve-tpt).
