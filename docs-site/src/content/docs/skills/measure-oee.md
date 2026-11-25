---
title: measure-oee
description: Calculates and checks OEE and TEEP for a machine, line or plant, builds a loss tree in minutes, and routes the top losses to the skill that fixes them.
---

<span class="status available">available</span>

Calculates and checks OEE (overall equipment effectiveness, Gesamtanlageneffektivität) and TEEP for a machine, line or plant, ranks the losses in minutes, and routes the largest ones to the right countermeasure.

## Two modes

The skill picks the mode from your request.

| Mode | You give | You get |
|---|---|---|
| Calculate | The shift calendar and planned breaks, the stop log with reasons and minutes, the counts per product (made, scrap, rework) and the ideal cycle time per product | The agreed time model, availability, performance, quality, OEE and TEEP with every formula shown, a loss tree in minutes ranked largest first, and a route for each top loss |
| Check a figure | An OEE figure or report and the data behind it | A plain "right" or "wrong" first, then the corrected figure with its calculation and the reason |

If the ideal cycle time, the counts or the planned production time are missing, the skill asks for them in one short list and stops. It may compute what the data allows, labelled as partial, but it never assumes a nameplate speed or a benchmark rate. A missing stop threshold does not block the calculation; it is marked "set by local policy" and listed as an open question.

## Rules it applies

- Changeovers, planned maintenance and waiting stay inside planned production time as losses, unless your convention says otherwise; then both figures are shown and labelled.
- Rework is a quality loss. Only first-pass good parts count as good.
- Losses are ranked in minutes, never by factor percentages.
- OEE across machines, shifts or days comes from summed minutes, never from averaged percentages.
- For a line, the bottleneck's OEE counts. A gain on a non-bottleneck adds stock, not output.
- Gaming is named and recomputed: excluded changeovers, a slow ideal cycle time, rework counted as good, a raised stop threshold.
- The 85% "world class" figure is a reference, not a standard. Compare an asset first with its own baseline.

## Where the work goes next

Set-up losses go to [`improve-smed`](/skills/improve-smed/), breakdowns, minor stops and speed losses go to [`improve-tpm`](/skills/improve-tpm/), and defects from a complaint or repeat problem go to [`solve-8d`](/skills/solve-8d/). A red OEE KPI on the board of [`lead-daily-routine`](/skills/lead-daily-routine/) comes here for its loss tree.

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: the time model across conventions and the loss tree with gaming effects, each with its sources.
- `assets/`: an OEE worksheet.
- `scripts/oee.py`: an optional standard-library calculator. Everything works by hand without it.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/measure-oee).
