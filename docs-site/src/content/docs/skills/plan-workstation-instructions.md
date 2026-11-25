---
title: plan-workstation-instructions
description: Drafts and reviews station inspection instructions, method sheets and operator work instructions derived from the control plan, and runs seven consistency checks against it.
---

<span class="status available">available</span>

Drafts and reviews station inspection instructions (Prüfanweisung), measurement method sheets and operator work instructions (Arbeitsanweisung) derived from the control plan. The control plan is the master: a station document may never be looser than it.

## Three outputs

The skill picks the mode from your request.

| Mode | You give | You get |
|---|---|---|
| Draft | The control-plan rows for one operation with their revision, the gauge list, error-proofing devices and challenge parts, safety rules and the operators' languages | A station instruction with work steps, key points and reasons, one check row per control-plan row, set-up, restart and error-proofing blocks, the reaction box, and the consistency-check result |
| Review | The existing instruction with its revision, and the control-plan rows | Whether it can be released as it stands, then one row per consistency check with pass or fail, the finding, the clause and the fix |
| Method sheet | What your company means by a method sheet (Prüfmethodenblatt) | The sheet, once its meaning is agreed |

Without the control-plan rows, the skill asks for them and stops. It never drafts a check with an invented limit, frequency or gauge ID. "Prüfmethodenblatt" has no public definition, so the skill always asks what you mean before it writes one.

## Rules it applies

- Every control-plan row becomes exactly one check row; no row is dropped and no check is added.
- Sample size, frequency, specification, gauge and reaction are copied word for word from the control plan. A capable process is a reason to request a control-plan change, never to loosen the station document.
- Special characteristics carry their symbol, and variable data are recorded as values, never only as OK/NOK.
- A weak reaction plan in the control plan is copied, listed as a gap and sent to the control-plan owner, not rewritten at the station.
- Seven consistency checks run on every draft and review: coverage both ways, special characteristics, sample and reaction, gauge capability, PFMEA trace, error-proofing and revision.

## Where the work goes next

Control-plan change requests and gaps from the checks go to [`plan-control-plan`](/skills/plan-control-plan/), and a new control-plan revision comes back from there. A control chart named as the control method goes to [`measure-spc`](/skills/measure-spc/). Updates arrive from [`solve-8d`](/skills/solve-8d/) (D7), [`improve-smed`](/skills/improve-smed/), [`improve-tpm`](/skills/improve-tpm/), [`improve-kaizen`](/skills/improve-kaizen/), [`improve-line-balancing`](/skills/improve-line-balancing/) and the solve skills. Instructions not followed at the station are checked with [`lead-gemba-walk`](/skills/lead-gemba-walk/), and findings on station documents arrive from [`audit-process`](/skills/audit-process/).

## What is in the folder

- `SKILL.md`: the procedure and the checks.
- `references/`: control plan to instruction, operator instruction writing, measurement capability and the consistency checks, each with its sources.
- `assets/`: a station instruction, a method sheet and a consistency-check report.

[Read the skill on GitHub](https://github.com/mftnakrsu/shopfloor-skills/tree/main/skills/plan-workstation-instructions).
