---
title: solve-fishbone
description: Turns a fishbone (Ishikawa, 6M) brainstorm into cause hypotheses that can be tested, screens them against Is/Is-Not facts and changes, and orders the tests.
---

<span class="status available">available</span>

Turns a fishbone (Ishikawa-Diagramm, cause-and-effect) brainstorm into cause hypotheses that can be tested. It writes a measurable effect, sorts the causes by 6M, rewrites them as conditions someone can check, screens them against the facts, and gives each hypothesis a test with its expected result. This skill widens the list of causes; [`solve-is-is-not`](/skills/solve-is-is-not/) narrows it.

## Two modes

The skill picks the mode from your request.

| Mode | You give | You get |
|---|---|---|
| Build or screen | The effect with its rate, before and now, Is/Is-Not facts, the changes with dates, and the brainstorm or diagram | A fishbone worksheet with the causes bone by bone, each screened as fits or contradicts, a parking list for solutions, and a test plan in test order |
| Check a claimed root cause | A cause picked from a fishbone or a vote | Whether it is verified, the facts that contradict it, the test that would decide it, and the other candidates kept open |

Without a measurable effect, the skill asks for it and stops. Without a brainstorm, it offers prompt questions per bone and marks any cause it suggests as a candidate for the team to confirm.

## Rules it applies

- The effect is one measurable deviation with no cause in it.
- Every entry is a condition that can be checked or switched; solutions go to a parking list, and blame is rewritten as the process condition that allows the error.
- A cause that the unaffected group shares cannot explain the difference and moves down.
- Causes that fit the facts and line up with a change are tested first; a vote only breaks ties.
- No cause is called confirmed without a test, and costly permanent actions wait for the result.

## Where the work goes next

Screened causes are tested against the full specification in [`solve-is-is-not`](/skills/solve-is-is-not/). A confirmed cause is drilled down with [`solve-5why`](/skills/solve-5why/), and a hypothesis that needs a countermeasure test goes to [`solve-pdca`](/skills/solve-pdca/). Root-cause searches arrive from [`solve-8d`](/skills/solve-8d/) (D4), [`measure-spc`](/skills/measure-spc/), [`measure-oee`](/skills/measure-oee/), [`lead-daily-routine`](/skills/lead-daily-routine/), [`improve-kaizen`](/skills/improve-kaizen/), [`plan-control-plan`](/skills/plan-control-plan/), [`audit-process`](/skills/audit-process/) and the Analyze phase of [`solve-dmaic`](/skills/solve-dmaic/). A confirmed machine condition goes to [`improve-tpm`](/skills/improve-tpm/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: the 6M categories with prompt questions, and hypothesis tests, each with its sources.
- `assets/`: a fishbone worksheet and a hypothesis test plan.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/solve-fishbone).
