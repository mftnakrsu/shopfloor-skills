---
name: improve-vsm
description: >-
  Draws and checks current-state and future-state value stream maps for one
  product family, door to door, and turns the future state into a loop plan.
  Use when a value stream map, current-state or future-state map, or a
  value stream design must be drawn, reviewed or turned into an
  implementation plan; when the takt, inventory days or lead-time ladder of
  a whole value stream must be computed; or when the supermarkets,
  pacemaker or FIFO lanes of a future-state map must be checked. Collects
  data-box fields, converts inventory to days of demand, answers the future-state questions in order,
  places kaizen bursts where a design needs a capability that does not yet
  exist, and plans loops with owners, targets and a 30/60/90-day review
  (Wertstromanalyse, Wertstromdesign, Wertstrom, Taktzeit, Schrittmacher,
  Supermarkt, Reichweite, Wertstrom-Durchlaufzeit).
license: MIT
metadata:
  version: "1.0.0"
  category: improve
  standards: ""
---
# Value stream mapping

## Conventions

- A value stream map (VSM, Wertstromanalyse) shows the material flow and the information flow of one product family from receiving to shipping on one page (LEI). The future-state map (Wertstromdesign) is the target design; the loop plan turns it into work.
- Product family: products that pass through similar steps and common equipment near the end of the stream. One map per family.
- Data-box fields use LEI's abbreviations: C/T cycle time (operator or machine time per unit before the work repeats), C/O changeover time, uptime %, %C/A (percent complete and accurate), available time per shift in seconds, plus operators, batch size and EPEI (every part every interval).
- Takt time (Taktzeit) = available working time ÷ customer demand, over the same period. Available working time = shift time − planned breaks. Other planned downtime (meetings, planned maintenance): state yes or no. In this skill unplanned downtime and changeovers are not subtracted from takt; they show up when effective C/T is compared with takt. State the convention every time, because some sources subtract planned downtime.
- The inventory ladder is the same rule as in `improve-tpt`: inventory days = units in stock ÷ daily customer demand. One flow unit (piece, set or box) throughout.

## Inputs

- Product family and its boundary (door to door, or a named start and end point), and the flow unit.
- Customer data: demand per day or month, working days per month, pack-out quantity, shipping frequency.
- Working pattern: shifts per day, shift length, planned breaks.
- Per process, walked from shipping back to receiving: C/T, C/O, uptime, %C/A, operators, batch size, part numbers run, and whether the equipment is shared with other families.
- Inventory at every point where flow stops: count and flow unit.
- Information flow: how orders and forecasts arrive, what the planning system sends to which process and how often, any expediting.
- Optional: the business goal (lead time, delivery, cost), the future-state horizon, the names or roles who can own loops.

Ask for every missing input; never invent one. Copy the user's numbers exactly.

- Without customer demand there is no takt, no pitch and no inventory days. Ask for demand (with its period) and the working time, in one short list, and stop. You may draw the process boxes and the information flow and give the formulas with the demand left open; never present a takt or a lead time in days from an assumed demand.
- Missing C/O, uptime or part-number counts block only the checks that use them (effective C/T, EPEI, supermarket (Supermarkt) size). Map what is known, mark the gap on the map and ask.
- If the user gives an existing map, rebuild the ladder from its numbers before judging the design.

## Procedure

1. **Set the scope.** Name the family, the boundary, the flow unit, the customer and the goal. If products differ in routing, build a product-by-process matrix and group by shared downstream steps; work content within a family should not differ by more than about 30% (Rother & Harris, rule of thumb). Details in [current state](references/current-state.md).
2. **Customer box, takt and pitch.**
   - Takt = available seconds per day ÷ demand per day. Pitch = takt × pack-out quantity.
   - Example (invented): 3 shifts × (480 − 20) min = 1,380 min = 82,800 s; demand 1,150 units a day → takt = 72 s. Pack of 10 → pitch = 720 s = 12 min.
3. **Walk the current state** from shipping back to receiving. Draw one process box per area of continuous flow; a box ends where the flow stops and inventory builds. Fill one data box per process. Record each inventory point with a triangle and its count. Draw the information flow on top: forecasts, orders, schedules, push arrows, and "go see" expediting. Prefer counts and timings taken on the floor over system data.
4. **Build the ladder.**
   - Inventory days at each point = count ÷ daily demand. Production lead time = sum of the inventory days.
   - Processing time = sum of the per-unit C/T of each process box. If a box has several operators, ask whether its C/T is the time on one unit or the output interval.
   - Example (invented): counts of 2,300, 1,150, 575 and 3,450 at 1,150 a day → 2 + 1 + 0.5 + 3 = 6.5 days; C/Ts of 40, 25, 65 and 50 s → 180 s.
   - Process cycle efficiency = processing time ÷ lead time, both in seconds of the same clock (here 180 ÷ (6.5 × 82,800) = 0.03% of working time).
   - The ladder uses demand as the rate. It equals throughput time only when output equals demand; if they differ, also measure TPT = WIP ÷ output with `improve-tpt`.
5. **Mark the current-state problems.** Compare every C/T with takt, and the effective C/T = C/T ÷ uptime as well. Example (invented): 60 s at 80% uptime → 75 s, above a 72 s takt. Flag each process above takt, each long C/O at a shared machine, each schedule sent to more than one process, and each large inventory. Agree the problems with the team before designing.
6. **Design the future state by answering the questions in order.** Each answer limits the next; full questions and decision rules in [future-state questions](references/future-state-questions.md).
   1. What is the takt time?
   2. Build to a finished-goods supermarket, or straight to shipping?
   3. Where can continuous flow run?
   4. Where are supermarket pull or FIFO lanes needed to control the processes upstream of flow?
   5. Which single process gets the customer schedule (the pacemaker, Schrittmacher)?
   6. How is the mix levelled at the pacemaker?
   7. What increment of work (pitch) is released to and withdrawn from the pacemaker?
   8. Which process improvements does the design need to work?
   - Any answer that depends on a capability that does not exist yet (a C/T above takt, a C/O too long for the run interval, low uptime, poor %C/A) gets a kaizen burst. Never remove inventory from the map while its cause stays.
7. **Check the future state.**
   - Every process in continuous flow has C/T at or below takt, or a kaizen burst that gets it there.
   - The pacemaker is a scheduling point, not the bottleneck: a bottleneck is fixed, never allowed to set the pace (Shook).
   - Exactly one process receives the schedule; every other process is linked by a supermarket, a FIFO lane with a maximum, or flow.
   - A supermarket after a shared batch process holds at least the demand over its run interval (EPEI) plus the replenishment time, plus safety stock set by local policy. Example (invented): EPEI 4 days at 300 units a day → at least 1,200 units before safety. A smaller supermarket needs a shorter EPEI first, which means a C/O kaizen burst.
   - Rebuild the future ladder from the designed inventory days and state the new lead time only as the target once the bursts are done.
8. **Plan the loops.** Split the future state into loops: the pacemaker loop first, then one loop per upstream supermarket or FIFO lane, then the supplier loop. For each loop: the kaizen bursts in it, an owner by role, a target in numbers (lead time, inventory days, C/O, uptime, pitch hits), a start and an end date. Every loop gets a number, also when data is missing: give a provisional target labelled as an assumption, with the date by which the missing data confirms or replaces it. Start the first loop within 2 to 3 weeks of mapping, plan 30-, 60- and 90-day reviews inside the future-state horizon (LEI, Worth), and never launch all loops at once. Details in [loop plan](references/loop-plan.md).
9. **Review and re-map.** At each 30/60/90-day review compare the loop targets with measured values, re-count the inventory points and redraw the current state when a loop is finished. Redraw the future state when demand or mix moves takt.

## Validation

Check before answering:

1. Takt and the ladder use the same demand period, the same working time and one flow unit; the takt convention is stated.
2. Every inventory in days is count ÷ daily demand, and the lead time is their sum.
3. Every C/T above takt, nominal or effective, is flagged with a fix.
4. Exactly one pacemaker gets the schedule, and it is not chosen because it is the bottleneck.
5. No inventory is removed or shrunk on the future map without its cause removed or a kaizen burst for it; supermarkets cover at least EPEI plus replenishment time.
6. Every loop has an owner, a numeric target and dates, the pacemaker loop is first, and 30/60/90-day reviews are set.
7. Every number is the user's, computed from it, or labelled as an assumption, a rule of thumb or set by local policy.

## Output

- `assets/vsm-study.md`, filled in: scope, customer box with takt and pitch, data boxes, inventory ladder, current-state problems, the eight answers, kaizen bursts, future ladder, loop plan and review dates.
- A text sketch of each map is enough: information flow on top, process boxes with data boxes in the middle, the ladder at the bottom. Drawing by hand on the floor stays the real method.
- Show every formula with the user's numbers and units.
- Put open questions and assumptions before the plan, and end the answer with the loop plan and the review dates. Data still missing becomes a dated task in the plan, not a closing list.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. Mapping several families on one map, or a single process instead of the stream (fix: step 1).
2. Takt computed from calendar time, or with an unstated downtime deduction (fix: step 2, Conventions).
3. Inventory removed on the future map while the changeover or uptime problem that caused it stays (fix: steps 6, 7).
4. The bottleneck made the pacemaker, or schedules still sent to every process (fix: step 7).
5. Ladder days mixing pieces with sets or boxes, or cycle efficiency with mixed clocks (fix: steps 4, Validation 1).
6. Jumping from the current state to point kaizen, or launching every loop at once (fix: steps 5, 8).
7. A future state with no owners, dates or reviews (fix: step 8).

## Hand-offs

- Measured throughput time, WIP caps and the Little's Law cross-check go to `improve-tpt`; a stream-level lead-time problem found there comes back here.
- A process above takt with manual work goes to `improve-line-balancing`.
- A C/O kaizen burst (EPEI too long, supermarket too large) goes to `improve-smed`; an uptime burst goes to `improve-tpm`; a machine whose losses need a loss tree goes to `measure-oee`.
- A low %C/A from a complaint or a repeat defect goes to `solve-8d`.
- Loop targets are tracked on the board in `lead-daily-routine`; a red lead-time or delivery KPI there that spans several processes comes here.
