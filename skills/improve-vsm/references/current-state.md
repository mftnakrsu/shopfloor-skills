# Current state

How to scope the family, walk the stream, fill the data boxes, draw the information flow and build the inventory ladder.

## Contents

- Scope and product family
- Walking the stream
- Data-box fields
- Map layout and icons
- Information flow
- Inventory ladder
- Effective cycle time
- Worked example
- Sources

## Scope and product family

- LEI's starting steps: pick one product family, have one person lead the mapping, start at the door-to-door level, and draw material and information flow together (LEI lexicon).
- A family is a product and its variants that pass through similar steps and common equipment close to shipping. Define it from the most downstream steps (LEI eBook glossary).
- With many variants, build a matrix: products as rows, process steps as columns, a mark where a product uses a step. Group rows with the same downstream steps. In high-mix plants group by routing rather than by product type, then rank the groups by volume or revenue (LEI eBook, Hunt).
- Work content inside one family or cell should not differ by more than about 30% between products (Rother & Harris; rule of thumb). Products that skip or add many steps belong to another family.
- Write a short charter: family, boundary, customer, business goal, team, the date the future state is due. Do not widen the scope while mapping (LEI eBook, Worth).

## Walking the stream

1. Start at shipping and walk upstream to receiving, so each process is seen from its customer's side (Rother & Shook, as summarised by Think Insights).
2. Time C/T on the floor with a stopwatch; ask the operators for C/O times; count every inventory point. A quick first walk can take about 20 minutes (LEI eBook, LaHote).
3. Check system data against what you see: spreadsheets miss what happens on the floor (LEI eBook, Worth).
4. A perfect map is not the goal; seeing and agreeing on the flow is (LEI lexicon).

## Data-box fields

One data box per process box (LEI eBook):

| Field | Meaning | Unit |
|---|---|---|
| C/T (or P/T) | Time an operator or machine needs for all work on one unit before the work repeats | s per unit |
| C/O | Time to switch from the last good part of one part number to the first good part of the next | min |
| Uptime | Share of the time the machine is available to produce | % |
| D/T | Time lost to planned or unplanned stops | min or % |
| %C/A | Share of units completed right first time, with nothing to correct downstream | % |
| Available time | Time the process works per shift, net of planned breaks | s per shift |

Add where they matter: operators, shifts, batch or lot size, number of part numbers run, EPEI, scrap, and whether the equipment is shared with other families.

EPEI (every part every interval) is the time in which a machine runs every part number once; it rises with C/O time and with the number of part numbers (LEI lexicon, EPEx).

## Map layout and icons

- Three rows (LEI eBook): information flow at the top; process boxes in the middle with data boxes below; the timeline (ladder) and summary figures at the bottom. Customer at top right, suppliers at top left.
- A process box covers one area of continuous flow and stops where the flow stops and inventory builds (LEI eBook).
- Common icons: process box, data box, inventory triangle, push arrow, supermarket, withdrawal and production kanban, signal kanban, kanban post, levelling (heijunka) box, FIFO lane, kaizen burst, "go see" scheduling, manual and electronic information arrows, truck shipment (Lucid; names vary by tool).
- In text, write the map as three lines: information flow; process boxes with data in brackets, linked by the inventory between them; the ladder.

## Information flow

Record for each signal: who sends it, to whom, what (forecast, firm order, schedule), how (system, paper, verbal) and how often. Mark every process that gets its own schedule from the planning system with a push arrow, and every expediting walk as "go see" scheduling. Several schedules in one stream are a current-state problem: each process then works to its own plan and inventory builds between them.

## Inventory ladder

- Inventory days = count ÷ daily customer demand. This is Little's Law with demand as the rate; it is the same rule `improve-tpt` uses for days of demand (Rother & Harris).
- Production lead time = sum of the inventory days along the stream, including raw material and finished goods.
- Processing time = sum of the per-unit C/T of the process boxes. It is the time a unit is being worked on.
- Process cycle efficiency = processing time ÷ lead time, both in the same clock. State whether the days are working days or calendar days.
- The ladder equals the measured throughput time only when output equals demand. When output runs above or below demand, measure TPT = WIP ÷ output as well and say which number you report.

## Effective cycle time

Compare each process with takt twice: nominal C/T, and C/T ÷ uptime. A shared machine also loses time to C/O; its capacity check needs the run time and C/O of all families it serves. A process above takt on either check needs capacity, moved work, more uptime or shorter C/O in the future state.

## Worked example

Invented stream, one flow unit = one piece, demand 350 pieces a day.

| Point | Count | Daily demand | Days |
|---|---|---|---|
| Raw material | 1,400 | 350 | 4.0 |
| Before forming | 700 | 350 | 2.0 |
| Before joining | 350 | 350 | 1.0 |
| Before final test | 175 | 350 | 0.5 |
| Finished goods | 1,050 | 350 | 3.0 |
| Lead time | | | 10.5 |

C/Ts 20, 70, 55 and 35 s → processing time 180 s. Working day of one shift, 7 h net = 25,200 s → takt = 25,200 ÷ 350 = 72 s. Forming at 70 s is below takt nominally, but at 85% uptime its effective C/T is 82 s, above takt: a kaizen burst for uptime, or a second shift at forming.

## Sources

- LEI: [Lexicon, value-stream mapping](https://www.lean.org/lexicon-terms/value-stream-mapping/)
- LEI: [eBook, Why, When and How Value-Stream Mapping is a Vital Part of Continuous Improvement](https://email.lean.org/hubfs/ebook%20files/eBook-Top5-VSM-final.pdf)
- LEI: [Lexicon, every product every interval](https://www.lean.org/lexicon-terms/every-product-every-interval/)
- Rother, M. and Harris, R.: [Creating Continuous Flow, LEI excerpt with the Apex example](https://www.lean.org/wp-content/uploads/2021/01/Creating-continuous-flow-part1.pdf)
- Think Insights: [Value stream mapping](https://thinkinsights.net/consulting/value-stream-mapping)
- Lucid: [Value stream mapping symbols](https://www.lucidchart.com/pages/value-stream-mapping/value-stream-mapping-symbols)
