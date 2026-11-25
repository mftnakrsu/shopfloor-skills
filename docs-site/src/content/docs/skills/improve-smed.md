---
title: improve-smed
description: Runs a changeover reduction (SMED) study, decides with EPEI whether the time saved becomes capacity or smaller lots, and keeps set-up verification in place.
---

<span class="status available">available</span>

Runs a changeover reduction study (SMED, Rüstzeitreduzierung) on machines and lines, decides how to use the time saved, and keeps set-up verification and first-piece approval in place.

## Three modes

The skill picks the mode from your request.

| Mode | You give | You get |
|---|---|---|
| Study | A video of a changeover, or an element list with times, who did each element and whether the machine was stopped | The element sheet, internal and external work separated, the improvements in order with minutes saved, before and after totals, and a new changeover standard with a re-timing plan |
| Decide | Available time, demand and cycle time per product, the number of products, the changeover time before and after, and whether the machine limits output | The minimum EPEI, lot sizes, and a decision between more capacity and smaller lots, with the numbers |
| Review | A changeover plan or claim | Each gap with its fix and the minutes it saves against the target, and a path to the target that keeps the set-up verification |

If element times are missing, the skill asks for a video or an element list and stops. A decision without available time, demand, cycle times or the number of products stops at the questions and the formula. A missing description of the current set-up verification does not block a study; it is listed as an open question.

## Rules it applies

- Changeover time runs from the last good part of the old run to the first good part of the new one, with trial parts and approval inside.
- Separate first, then convert, then streamline. Cheap procedural gains come before hardware.
- Adjustments are removed with fixed stops, locating pins and stored settings, not done faster.
- The first-piece approval is never removed to hit a target. It is made faster instead (IATF 16949 8.5.1.3).
- The saving counts only when lot sizes or the plan change; otherwise it is lost as idle time.

## Where the work goes next

The set-up loss arrives from the loss tree in [`measure-oee`](/skills/measure-oee/), and availability is re-measured there after the change. Breakdowns seen during changeovers go to [`improve-tpm`](/skills/improve-tpm/). A set-up that sent defects to the customer goes to [`solve-8d`](/skills/solve-8d/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: the changeover study, the EPEI decision and set-up verification, each with its sources.
- `assets/`: an element sheet and a changeover standard.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/improve-smed).
