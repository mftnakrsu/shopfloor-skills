---
title: solve-is-is-not
description: Scopes a problem with an Is/Is-Not specification, draws out the distinctions and dated changes, tests every possible cause against both columns, and names the most probable cause with its verification test.
---

<span class="status available">available</span>

Scopes a production or quality problem with an Is/Is-Not specification (Ist/Ist-nicht-Analyse) of what, where, when and extent. It draws out what is true only of the Is side and what changed there, tests every possible cause against each pair, and names the most probable cause with the test that will verify it. This skill narrows a known list of causes; [`solve-fishbone`](/skills/solve-fishbone/) builds a broad one.

## Two modes

The skill picks the mode from your request.

| Mode | You give | You get |
|---|---|---|
| Build | The deviation, Is and Is-Not facts as numbers, identifiers and dates, the changes with dates, and any causes the team has named | An Is/Is-Not worksheet with distinctions and changes, the cause test matrix, the most probable cause and its verification plan, and the open questions |
| Check | An existing Is/Is-Not and the cause the team chose | Whether that cause explains every fact, the change that does fit, and whether the analysis can be closed |

Without the Is-Not side, the start date or the extent, the skill asks for them, names the comparisons that would matter most, and stops. It does not confirm or reject a named cause on missing facts.

## Rules it applies

- Every Is-Not is the closest real comparison where the defect could be but is not, never the negation of the Is.
- Distinctions are concrete (a tool number, a lot, a date), and every change has a date and a scope.
- One fact that a cause cannot explain eliminates it, however popular it is.
- The most probable cause is the one that explains every pair with the fewest and most reasonable assumptions (rule of thumb).
- No cause is called the root cause before a test has verified it; containment can start at once, permanent action waits.

## Where the work goes next

When one or two ideas or none fit the facts, the list is widened with [`solve-fishbone`](/skills/solve-fishbone/) and tested here. A verified cause goes to [`solve-5why`](/skills/solve-5why/) for its occurrence, detection and system roots, and a cause to test with a countermeasure to [`solve-pdca`](/skills/solve-pdca/). This analysis serves the D2 and D4 steps of [`solve-8d`](/skills/solve-8d/). Problems arrive from [`measure-spc`](/skills/measure-spc/), [`lead-daily-routine`](/skills/lead-daily-routine/), [`measure-oee`](/skills/measure-oee/), [`improve-kaizen`](/skills/improve-kaizen/), [`solve-dmaic`](/skills/solve-dmaic/) and [`audit-process`](/skills/audit-process/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: specification questions, and testing causes, each with its sources.
- `assets/`: an Is/Is-Not worksheet.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/solve-is-is-not).
