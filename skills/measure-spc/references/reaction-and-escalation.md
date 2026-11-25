# Reaction and escalation

How a chart signal becomes a reaction at the workstation and, when needed, an escalation through the tiers. What the standards ask, a signal-to-reaction table, and the gaps to flag.

## What the standards ask (own summary)

As of November 2026; IATF 16949:2016 with its sanctioned interpretations is the current edition. Re-check the clause numbers when a new edition appears.


- IATF 16949 8.5.1.1 e: the control plan carries a reaction plan for when nonconforming product is found or the process becomes statistically unstable or not capable.
- IATF 16949 9.1.1.1: keep the measured values for variable data, follow reaction plans with an escalation process when criteria are not met, record significant process events such as tool changes and repairs; unstable or not capable characteristics get containment, including 100% inspection where appropriate.
- A complete reaction plan covers containment of suspect product, stopping suspect production, restoring control, and who is responsible (secondary summary of the AIAG control plan manual, Umbrex).
- The workstation instruction should state who may stop the process and the exact escalation path (rule of thumb; this skill's own recommendation).

## Signal-to-reaction table

The user's control plan decides. This table is the order to check it against, not a replacement.

| Situation | Reaction at the workstation | Escalation |
|---|---|---|
| Spread chart signal (R, S, MR) | Stop or hold per plan; check gauge, clamping, tool, material lot | As for a location signal |
| Rule 1 on the location chart | Stop or hold; contain back to the last in-control subgroup; check setting, tool, material | Named role at once; next tier if not restored within the plan's time limit |
| Zone or run rule | Check and adjust per plan; contain back to where the pattern began | Named role; next tier if it repeats or is not restored in time |
| Trend | Check wear, temperature, consumables; correct before rule 1 fires | Maintenance if the cause is machine condition |
| Unit outside tolerance | Nonconforming product: segregate, mark, contain back to the last good check, whatever the chart shows | Quality role at once |
| Repeat of the same signal, or cause unknown | Keep containment | Structured problem solving; tier board item with owner and due date |

- Containment starts at the last subgroup that was in control, not at the signal: a run or zone rule means the shift began earlier.
- Every signal and its action is written on the chart or the event log: time, rule, cause found, action, who, restart check.
- Restart after one subgroup back in control, recorded (rule of thumb; the plan may ask more).
- Over-adjustment: adjusting a process on every point inside the limits adds variation. Adjust only on a signal, or on the plan's tolerance-based rule.

## Escalation ladder

| Level | Who (named in the plan) | When | Answer due |
|---|---|---|---|
| Workstation | Operator | Every signal | Immediately |
| Tier 1 | Team or shift lead | Every signal, per plan | Set by local policy |
| Tier 2 | Area with quality and engineering | Not restored within the plan's time limit, or repeat | Same day (rule of thumb from tier practice) |
| Higher | Plant | Shipped suspect product, customer risk, safety | Set by local policy |

Write the user's own roles and time limits into the ladder. Where the plan has none, leave the cells blank, marked "set by local policy", and list them as open questions.

## Gaps to flag in a reaction plan

- "Inform supervisor" with no containment scope, no named role and no recording.
- No time limit before escalation.
- Variable data recorded only as OK or not OK.
- No rule for which run rules trigger which reaction.
- No restart check.

## Sources

- DNV: [IATF 16949:2016 vs ISO/TS 16949:2009 comparison matrix (8.5.1.1, 9.1.1.1)](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf)
- Umbrex: [AIAG control plan framework](https://umbrex.com/resources/frameworks/automotive-mobility-frameworks/aiag-control-plan/)
- NIST/SEMATECH e-Handbook: [What are variables control charts?](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc32.htm)
