# Reaction plans

How to word the reaction plan of a control-plan row, and the gaps to flag. Clause summaries are in our own words.

As of November 2026: IATF 16949:2016 with its sanctioned interpretations; the reaction-plan owner column of the AIAG Control Plan manual, 1st edition (2024), is known from a software vendor's reading. Re-check when a new edition appears.

## What a reaction plan covers

IATF 16949 8.5.1.1 e asks for a reaction plan when nonconforming product is found or the process becomes unstable or not capable; 9.1.1.1 adds an escalation process. A complete plan covers four things and names who is responsible (Umbrex, summarising the AIAG manual):

1. **Stop or hold** suspect production. State who may stop; the operator's authority comes first.
2. **Contain** suspect product: back to the last good check, at every location it may have reached (station, buffer, finished goods, shipped).
3. **Restore** control: find and fix the cause, then restart only after a passing check, recorded.
4. **Notify and escalate** by role and time limit, both set by local policy.

Escalation alone does not contain any parts (Umbrex).

## Wording pattern

"[Stop / hold] → block and check all parts back to the last good check of this characteristic → correct [setting, tool, gauge] → restart after a passing check, recorded (one passing check is a rule of thumb; the plan may ask for more) → call [role] at once; escalate to [role] if not restored within [time, set by local policy] → record on [sheet or system]."

## Special cases

| Row type | Reaction to add |
|---|---|
| Special characteristic | Quality role informed every time; customer notified if suspect product may have shipped |
| Error-proofing device fails its check | Everything since the last successful device check is suspect; continue only on an approved alternate control (10.2.4, 8.5.6.1.1) |
| Gauge found out of calibration | Assess earlier results made with it; contain if they may be wrong (7.1.5.2.1) |
| SPC signal | Contain back to the last in-control subgroup; reaction per run rule |
| Unit outside tolerance | Nonconforming-product handling, whatever the chart shows |
| Repeat of the same reaction | Structured problem solving and a control-plan review |

## Gaps to flag

- "Inform supervisor" or "adjust machine" with no containment scope.
- No owner by role, or a person's name instead of a role.
- No time limit before escalation.
- No restart check.
- The same generic text in every row, whatever the characteristic.
- Variable data recorded only as OK or not OK.

## Sources

- DNV: [IATF 16949:2016 vs ISO/TS 16949:2009 comparison matrix (8.5.1.1 e, 9.1.1.1, 10.2.4, 7.1.5.2.1)](https://www.dnv.com/siteassets/images/pdf-documents/iatf-2009-to-2016-comparison-matrix.pdf)
- Umbrex: [AIAG control plan framework](https://umbrex.com/resources/frameworks/automotive-mobility-frameworks/aiag-control-plan/)
- PeakAvenue: [New AIAG control plan requirements (reaction-plan owner)](https://www.peakavenue.com/news-events/news/detail/new-aiag-control-plan-requirements)
- CIS, University of Tennessee: [Top findings during IATF 16949:2016 transition audits](https://cis.tennessee.edu/top-findings-during-iatf169492016-transition-audits)
