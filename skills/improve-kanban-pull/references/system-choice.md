# Choosing the pull system

When to use a supermarket, a FIFO lane, CONWIP or a mix, and how each one caps stock.

## Contents

- The three systems
- Selection rules
- When a supermarket is needed between two steps
- Demand variability
- The pacemaker
- Sizing FIFO lanes and CONWIP loops
- Source disagreements
- Sources

## The three systems

| System | What the card or signal stands for | Stock it holds | Fits |
|---|---|---|---|
| Supermarket with kanban (replenishment pull) | One container of one part number | A fixed stock of every part number | Repeating parts, each one stockable, steady demand |
| FIFO lane (sequential pull) | A place in a lane with a maximum | Only what is in the lane, in sequence | Too many variants to stock, built to order, short shelf life, rare and costly parts; two decoupled processes |
| CONWIP | Capacity of a line segment; the part number is chosen from the backlog when the card returns | A fixed total WIP across several steps | Made to order, many variants sharing one routing, mix that shifts the bottleneck |

## Selection rules

1. Default between two linked steps: a FIFO lane, unless a reason for a supermarket applies (Roser).
2. Supermarket pull works best when each process can stock every part it makes; it may not be feasible with many part numbers (LEI).
3. Sequential pull is used when there are too many part numbers to stock; it needs short, predictable lead times and a well-understood order pattern, or a finished-goods store (LEI).
4. When an 80/20 rule applies (a few part numbers carry most of the volume), segment by volume (high, medium, low, infrequent) and mix the systems; infrequent parts can use a kanban that stands for an amount of capacity, not a part number (LEI).
5. CONWIP is suited to parts that are not stocked (custom, rare) because the card stands for a quantity, not a part type (Roser).
6. CONWIP is a little more resilient than kanban to mix changes, because the bottleneck can shift without re-sizing several card sets (Marek et al.). It can reach the same output with less WIP than kanban (Wikipedia: CONWIP).

## When a supermarket is needed between two steps

Roser's reasons to place a supermarket instead of a FIFO lane: the two steps need different lot sizes (the one mandatory reason), the step faces the customer, the flow splits or merges, cycle times or shift patterns differ widely, the steps are far apart, the supplier makes several variants, or responsibility changes hands.

## Demand variability

- Both kanban and CONWIP need fairly steady volume; large swings in volume or mix undermine either (Marek et al.).
- Monden expected kanban to absorb daily swings within about 10% of the monthly plan, with larger changes set through the plan (Akturk & Erhun).
- Wider swings: level volume and mix at the pacemaker, recalculate cards each plan period, or hold a finished-goods buffer in front of the customer.

## The pacemaker

Send the customer schedule to one process only, level the mix there, and release and withdraw small, consistent increments of work (LEI future-state guidelines). Upstream processes follow their pull loops; the pacemaker is usually near the customer end.

## Sizing FIFO lanes and CONWIP loops

- FIFO lane: Roser gives no formula; the lane should cover the failures, change-overs and other stops of the processes without growing large, and he recommends an expert estimate adjusted in operation. A starting point is customer usage × the longest stop to cover (rule of thumb). When the lane is full, the supplier stops (LEI).
- CONWIP: cards = output × target throughput time (Little's Law). Check the output at that WIP with TH = r_b × w ÷ (W0 + w − 1), the Hopp and Spearman formula Marek et al. use to set CONWIP cards.

## Source disagreements

- Roser lists "the process makes several variants" as a reason for a supermarket; LEI warns that a supermarket may not be feasible with many part numbers. Both hold: a handful of variants fit a supermarket, a long tail does not.
- The CONWIP paper's authors are listed as Spearman, Woodruff and Hopp (Wikipedia) and as Hopp and Woodruff in a reprint.

## Sources

- LEI: [Lexicon, pull production](https://www.lean.org/lexicon-terms/pull-production/)
- LEI: [Lexicon, first in, first out](https://www.lean.org/lexicon-terms/first-in-first-out-fifo/)
- LEI: [Lexicon, supermarket](https://www.lean.org/lexicon-terms/supermarket/)
- LEI: [Six guidelines for moving toward a lean value stream](https://www.lean.org/the-lean-post/articles/6-guidelines-for-moving-toward-a-lean-value-stream/)
- Roser, C.: [Ten rules when to use a FIFO, when a supermarket](https://www.allaboutlean.com/FIFO-vs-supermarket-part1/)
- Roser, C.: [Determining the size of your FIFO lane](https://www.allaboutlean.com/fifo-size/)
- Roser, C.: [Basics of CONWIP systems](https://www.allaboutlean.com/conwip-basics/)
- Marek, R. P., Elkins, D. A. and Smith, D. R.: [Understanding the fundamentals of kanban and CONWIP pull systems using simulation, Winter Simulation Conference 2001](https://www.informs-sim.org/wsc01papers/122.PDF)
- Akturk, M. S. and Erhun, F.: [An overview of design and operational issues of kanban systems, International Journal of Production Research 37(17), 1999](https://repository.bilkent.edu.tr/bitstream/11693/25185/1/Overview%20of%20design%20and%20operational%20issues%20of%20kanban%20systems.pdf)
- Wikipedia: [CONWIP](https://en.wikipedia.org/wiki/CONWIP)
