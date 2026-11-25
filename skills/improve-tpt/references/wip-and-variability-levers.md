# WIP and variability levers

How to cap WIP, how to set and lower the cap, and which variability to remove first.

## Ways to cap WIP

| Mechanism | How it caps | Fits | Source |
|---|---|---|---|
| CONWIP | A new unit is released at the start only when one leaves the end; the count in between stays constant | Many products, one routing or a few; easy to run with cards or a release board | Wikipedia: CONWIP; Gallego |
| FIFO lane with a maximum | Upstream stops when the lane is full; first in, first out | Between two steps that cannot be linked by a supermarket | LEI VSM lexicon |
| Kanban or supermarket loop | Production is triggered by consumption; the cards cap the stock | Repetitive parts, stable demand | LEI VSM lexicon |
| Release control | Release follows the bottleneck's actual output, not the plan or material availability | First step when nothing else exists | Gallego (pull controls WIP, push controls release) |

Simulation studies found CONWIP reaching the same output as kanban with less WIP (Wikipedia: CONWIP). For the same output, a push line in Gallego's example needs 25% more WIP than a line with constant WIP.

## Setting the cap

1. Target WIP = output needed × target TPT (Little's Law).
2. Check it with the practical-worst-case throughput: r_b × w ÷ (W0 + w − 1) must reach the output needed. If the line performs worse than PWC today, treat the result as optimistic.
3. Start the cap between today's WIP and the target, so the first week does not starve the bottleneck (rule of thumb).
4. Lower the cap in steps, weekly, while output holds and the bottleneck never waits for work (rule of thumb).
5. When output drops, raise the cap one step and remove the variability that caused the gap before lowering again.
6. Write the cap where the release happens: a card count, a board, or a maximum line on the floor. Name an owner who may change it.
7. Keep a small buffer in front of the bottleneck only; it buffers variability where lost time cannot be made up (Variability Buffering Law: inventory, capacity or time absorbs variability; Hopp & Spearman).

## Variability: what to remove first

Variability is buffered by inventory, capacity or time. If WIP is capped and variability stays, output or delivery time pays for it.

| Source | Raises | Lever | Source |
|---|---|---|---|
| Long unplanned stops at the bottleneck | ce, t_e | Shorter repairs, spare parts, prevention; at equal availability, many short stops hurt less than few long ones (rule of thumb) | Hopp & Spearman, ch. 8 |
| Long set-ups and large lots | t_e, ce, ca downstream | Set-up reduction, then smaller lots | FabTime; LEI VSM lexicon |
| Batch release and transfer batches | ca | Release single units or small batches; move small transfer batches | FabTime |
| Waiting for a full batch at a lightly loaded batch process | Queue time | Start with what is there up to about 80% loading (rule of thumb from a FabTime simulation) | FabTime |
| Expediting and priority classes | TPT of normal orders | One release point, FIFO; priorities raise the TPT of the rest sharply | FabTime |
| Rework loops | Load and ca | Fix the defect cause; load into the loop is TH ÷ (1 − p) | FabTime |
| Bottleneck loading above about 85% | U term | Add capacity, offload work, cut effective process time; keep about 15% catch-up capacity | FabTime |

Example (invented): a batch of 4 units arrives at a step that takes 15 min per unit. The units wait 0, 15, 30 and 45 min, a mean of 22.5 min, even with spare capacity (FabTime).

## Prioritising the stations

Most of the delay usually sits at a few stations (George's "second law": 80% of delay at fewer than 20% of stations, cited by Little 2011; a rule of thumb). Rank stations by queue time or by the V × U term, and start with the largest.

## Sources

- Wikipedia: [CONWIP](https://en.wikipedia.org/wiki/CONWIP)
- Gallego: [IEOR 4000 notes, throughput, WIP and cycle time](https://www.columbia.edu/~gmg2/4000/pdfold/throughput.pdf)
- LEI: [Lexicon, value-stream mapping](https://www.lean.org/lexicon-terms/value-stream-mapping/)
- FabTime: [Cycle time tutorial and queueing formulas](https://inficon.com/media/11486/download/FabTimeCycleTimeTutorialAndQueueingFormulasfromFabTimeWebsite.pdf)
- Hopp, W. J. and Spearman, M. L.: *Factory Physics*, 3rd ed., Waveland Press, 2008
- Little, J. D. C.: [Little's Law as viewed on its 50th anniversary, Operations Research 59(3), 2011](https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf)
