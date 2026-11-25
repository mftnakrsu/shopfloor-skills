# Planned-maintenance basics

Maintenance strategies, how to choose one, how to split work between operators and maintenance, and the IATF 16949 pointer.

## Strategies

Types as named in Japanese TPM practice (MONOist, part 4):

| Strategy | What it means | Use for |
|---|---|---|
| Breakdown maintenance | Repair after failure, planned in advance (spares, method ready) | Cheap, non-critical items with a back-up |
| Time-based maintenance (TBM) | Service or replace at a fixed interval of time, cycles or hours | Wear with a known life (filters, belts, hoses, seals) |
| Condition-based maintenance (CBM) | Measure a condition and act at a set limit | Critical items where wear can be measured (vibration, temperature, pressure, oil condition) |
| Inspection and repair | Inspect at intervals, repair what is found | Items with no clear life but visible deterioration |
| Improvement (corrective) maintenance | Change the design to extend life or shorten repair | Repeat failure modes |
| Maintenance prevention | Feed lessons into new equipment design | New machines and rebuilds |

## Choosing

1. Rank the equipment: safety risk, quality risk, bottleneck, no back-up, repair time and cost. Score scales are set by local policy.
2. For critical items: CBM where the condition can be measured, otherwise TBM.
3. For repeat failure modes: root cause first, then improvement maintenance; TBM only as containment.
4. For non-critical items: breakdown maintenance with spares ready.
5. Set intervals from the failure history (for example a little below the shortest observed life of a wear part, rule of thumb) or from the maker's manual. If neither exists, label the interval "set by local policy" and review it after the first inspections.

## Work split

- Operators (AM standard): cleaning, lubrication, tightening, simple visual and sense checks, tagging abnormalities.
- Maintenance: technical inspections, TBM and CBM tasks, repairs, spares, training operators, support for the AM steps.
- Operators run autonomous maintenance; maintenance runs the plans, schedules and spares (MONOist, part 4).
- Every task has one owner, and the operator and maintenance standards together leave no part of the machine unchecked (rule of thumb).

## Spare parts

- A critical spares list per machine: part, use per year, lead time, minimum stock, location.
- Parts whose lead time is longer than the acceptable downtime are held in stock (rule of thumb).

## PM compliance

PM compliance = planned tasks done on time ÷ planned tasks due in the period. Example (invented): 45 of 50 due tasks done on time = 90%. The target is set by local policy.

## IATF 16949 pointer

IATF 16949:2016 clause 8.5.1.5 Total productive maintenance, in summary (as of 2026-11-25): keep a documented maintenance system; identify the key equipment; provide resources and spare parts; use planned, predictive and periodic methods as relevant; set measurable maintenance objectives (for example OEE, MTBF, MTTR, PM compliance) and review them, with action when they are missed. Check the customer-specific requirements too.

## Sources

- MONOist: [いまさら聞けないTPM (4), 計画保全と品質保全](https://monoist.itmedia.co.jp/mn/articles/1604/18/news011_2.html), 2016
- Advisera expert community: [8.5.1.5 Total productive maintenance](https://community.advisera.com/topic/8-5-1-5-total-productive-maintenance/)
- Wikipedia: [Total productive maintenance](https://en.wikipedia.org/wiki/Total_productive_maintenance)
