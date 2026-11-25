# Terms and measurement

How to map the user's words to one definition, and how to measure throughput time on the floor.

## Term map

Sources use the same words for different things. Map every term before computing.

| User says | Usually means | Map to | Source |
|---|---|---|---|
| Throughput time, TPT, Durchlaufzeit (DLZ) | Time a unit spends between start and end point | TPT | Haufe; LEI |
| Lead time, production lead time, door-to-door time | The same, at plant level from raw-material receipt to shipping | TPT | LEI |
| Order lead time, Lieferzeit | What the customer waits: TPT plus order processing and backlog | Order lead time, not TPT | LEI |
| Cycle time (Factory Physics, semiconductor plants) | Release to completion through the routing | TPT | Hopp & Spearman via Gallego; FabTime |
| Cycle time (lean, line balancing) | Repeat interval at a station or at the end of the line, in s per unit | Station or line cycle time, not TPT | LEI; Rother & Harris |
| Cycle time (some Six Sigma texts) | Processing only, without waiting | Close to raw process time T0 | iSixSigma |
| Throughput, output, Durchsatz | Good units per time unit, a rate | TH | Gallego |
| WIP, Umlaufbestand, Ware in Arbeit | Units between the start and end point, excluding stores and finished goods unless inside the boundary | WIP | Gallego |

If the user's "cycle time" could be either a repeat interval or a time through the routing, ask which one.

Durchlaufzeit is usually broken down into set-up time (Rüstzeit), processing time (Bearbeitungszeit), transport time (Transportzeit) and waiting or storage time (Liegezeit); waiting is normally the largest share (Haufe).

## Measurement recipe

1. Boundary: name the start inventory point and the end inventory point.
2. Flow unit: piece, job, lot or order. Use the same unit for WIP and output. A lot of 50 counts as 50 pieces or as 1 lot, never both.
3. WIP: count at the same points and the same time of day on several days (at least 5 to 10 days, rule of thumb). Include queues, units on machines, in transit, in rework and in quarantine.
4. Output: good units leaving the end point over the same days, after scrap.
5. Clock: working hours or calendar days, stated. Convert once at the end.
6. TPT = mean WIP ÷ output rate (Little's Law).
7. Direct sample: stamp start and finish of 20 to 30 tagged units (rule of thumb); give mean, slowest and, with enough data, the 85th or 95th percentile.
8. Per step: average effective process time including set-ups and stops, parallel machines, set-up time and lot size, unplanned stops, rework rate, arrival pattern.

## Conditions for Little's Law

- It holds for averages over a window, whatever the queue order (FIFO, priority, random), and separately for each product class (Little 2011).
- It is a measurement identity, not a forecast: it checks that WIP, output and time fit together (Little 2011, citing Lovejoy).
- The window should be long against the TPT and start and end at similar WIP levels; otherwise units that start before or finish after the window distort it (Little 2011). Rule of thumb: a window of several TPTs.
- Rework loops raise the load at the loop: with a rework share p, the rate into the loop is TH ÷ (1 − p) (FabTime). Count rework units as WIP.

## Cross-check: when the numbers do not fit

A gap of more than about 10% between Little's TPT and the tagged sample (rule of thumb) points to data problems. Check:

1. Units: pieces against lots or orders.
2. Windows: WIP and output from different periods.
3. Output: scrap or rework counted as good output.
4. Boundary: side stocks, rework areas or outside processing left out of the count.
5. Clock: calendar days in one number and working days in the other.
6. Sample: tagged units chosen because they were urgent (expedited units are faster than the rest).

Never replace measured data with ERP standard lead times; they are planning values.

## Inventory in days of demand

Value stream maps show inventory as days of demand: days = units in stock ÷ daily customer demand. This is Little's Law with demand as the rate. When output equals demand, the days add up to the TPT.

Example (invented): 600 units in front of assembly, demand 200 units a day → 3 days.

## Flow ratio

Process cycle efficiency = value-added time ÷ TPT (iSixSigma). State the denominator's clock: the same processing time gives a different ratio against calendar days and against working days. Published benchmarks differ widely between consultants, so do not use one as a target without a source the user accepts.

## Sources

- LEI: [Lexicon, cycle time and lead time](https://www.lean.org/lexicon-terms/cycle-time/)
- Rother & Harris: [Creating Continuous Flow, LEI excerpt](https://www.lean.org/wp-content/uploads/2021/01/Creating-continuous-flow-part1.pdf)
- Haufe: [Durchlaufzeit](https://haufe.de/id/beitrag/durchlaufzeit-1-welche-bedeutung-hat-die-durchlaufzeit-HI1176855.html)
- Gallego: [IEOR 4000 notes, throughput, WIP and cycle time](https://www.columbia.edu/~gmg2/4000/pdfold/throughput.pdf), presenting Hopp & Spearman, *Factory Physics*
- Little, J. D. C.: [Little's Law as viewed on its 50th anniversary, Operations Research 59(3), 2011](https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf)
- FabTime: [Cycle time tutorial and queueing formulas](https://inficon.com/media/11486/download/FabTimeCycleTimeTutorialAndQueueingFormulasfromFabTimeWebsite.pdf)
- iSixSigma: [Process cycle efficiency](https://www.isixsigma.com/dictionary/process-cycle-efficiency-pce/)
