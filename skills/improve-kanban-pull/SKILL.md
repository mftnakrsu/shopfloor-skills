---
name: improve-kanban-pull
description: >-
  Designs and sizes pull systems on the shop floor. Use when a schedule
  should be replaced by pull, when choosing between a supermarket with
  kanban, a FIFO lane or CONWIP, when a kanban card count, supermarket
  stock or loop size must be calculated or checked, when a loop has
  stock-outs or overflow, or when the pitch or paced withdrawal at the
  pacemaker must be set. Chooses the system from product variety and
  demand variability, sizes each loop with Monden's kanban formula and the
  full replenishment lead time, checks supplier capacity, and sets
  pitch from takt and pack-out quantity (Kanban, Kanbankarten,
  Kanbanregelkreis, Supermarkt, FIFO-Bahn, Ziehsystem, Pull-System,
  Wiederbeschaffungszeit, Behältermenge, Taktzeit, Schrittmacherprozess).
license: MIT
metadata:
  version: "1.0.0"
  category: improve
  standards: ""
---
# Kanban and pull systems

## Conventions

- A pull loop (Regelkreis) links a customer process and a supplying process. The supplier makes or moves only what the customer has used, and the cards cap the stock in the loop.
- Supermarket (Supermarkt): a fixed stock of each part number near the supplier, refilled by kanban cards or empty bins (replenishment pull). FIFO lane (FIFO-Bahn): a lane with a maximum quantity between two processes; the supplier stops when it is full (sequential pull). CONWIP: a fixed number of cards for a whole line segment; a card is tied to the line, not to a part number.
- Replenishment lead time L (Wiederbeschaffungszeit) is the full time from the moment a container is emptied until it is back, full, at the customer: card wait at the post, transport of the card, queue at the supplier (including the wait for the part's change-over slot), processing, curing or inspection, and transport back. It is never the processing time alone.
- Demand D, lead time L and container quantity a use one unit (pieces) and one clock (working hours or working days), stated every time.

## Inputs

- Per part number or group: demand per working day and its day-to-day swing against the plan; number of part numbers; made to stock or to order.
- Per loop: each component of the replenishment lead time; container quantity; how the supplier batches cards into lots; supplier capacity and change-over time.
- The safety factor (set by local policy).
- For pitch: available working time per day at the pacemaker (breaks out), customer demand per day, pack-out quantity.
- Optional: target throughput time for a CONWIP segment, the longest stop a FIFO lane must cover, floor space limits.

Ask for every missing input; never invent one. Copy the user's numbers exactly.

- A card count needs D, every component of L, a and the safety factor. If any is missing, ask for it in one short list and stop. At most give the formula and the blank `assets/kanban-loop-sheet.md`. Never present a card count for the user's loop from an assumed lead time.
- Ask for the safety factor; do not pick one silently. When the user has no policy, give the result at 0% and at a value they choose.

## Procedure

1. **Map the flow.** List the processes from the pacemaker back to raw material. Name the pacemaker (Schrittmacherprozess): the one process that gets the customer schedule, usually final assembly or the last step of continuous flow. Every process upstream is controlled by a pull loop, not a separate schedule.
2. **Choose the system per part group** with this table (first matching row wins; details in [system choice](references/system-choice.md)):

   | Situation | System |
   |---|---|
   | One-off, built to order, short shelf life, or rare and costly parts | FIFO lane with a maximum, or CONWIP over several steps |
   | Many part numbers with no dominant high runners, too many to stock each one at the supplier | FIFO lane or CONWIP (sequential pull) |
   | Many part numbers, a few of them carrying most of the volume (an 80/20 pattern, LEI), the tail not stockable | Mixed: supermarket for the high runners, FIFO lane or CONWIP for the rest |
   | Repeating parts, each stockable, daily demand within about ±10% of the plan (Monden) | Supermarket with kanban |
   | Demand swings wider than that | Level the mix at the pacemaker first and recalculate cards each plan period; else CONWIP with a finished-goods buffer |

   CONWIP fits better than kanban when the mix shifts the bottleneck, because one card set covers the whole segment (Marek et al.).
3. **Check supplier capacity.** Supplier capacity per hour, after change-overs, must exceed the demand of all parts it serves. If it does not, no card count fixes the loop: raise capacity first (hand-offs).
4. **Build the replenishment lead time.** Sum the components from the Conventions, each in working hours. Example (invented): card wait 0.5 h + queue 3 h + processing 1.5 h + transport 1 h → L = 6 h.
5. **Size each kanban loop** with the kanban formula Monden gives for Toyota (as cited by Akturk & Erhun and Marek et al.):
   - Cards n = D × L × (1 + s) ÷ a, rounded up to a whole card.
   - Example (invented): D = 50 pcs/h, L = 6 h, s = 10% (set by local policy), a = 40 → 50 × 6 × 1.1 = 330 pcs ÷ 40 = 8.25 → 9 cards. Maximum stock in the loop = 9 × 40 = 360 pcs.
   - If the supplier waits for k cards before starting a lot, or the customer withdraws k containers at once, add k − 1 cards (Roser). Example: lots of 3 cards → 9 + 2 = 11 cards.
   - Two-card systems: size the withdrawal loop and the production loop separately, each with its own L.
   - Formula details, variants and a statistical safety stock in [kanban formula](references/kanban-formula.md).
6. **Size FIFO lanes and CONWIP loops.**
   - FIFO lane maximum = customer usage per hour × the longest supplier stop or change-over the lane must cover (rule of thumb; Roser recommends an expert estimate, then adjust). Example (invented): 20 units/h × 1.5 h = 30 units.
   - CONWIP cards w = output needed × target throughput time (Little's Law). Example (invented): 25 jobs/day × 2 days = 50 cards.
   - Check output at w with the practical-worst-case formula (Hopp & Spearman, used by Marek et al.): TH = r_b × w ÷ (W0 + w − 1), with r_b the bottleneck rate and W0 = r_b × raw process time. Example (invented): r_b = 30 jobs/day, W0 = 12 → TH = 30 × 50 ÷ 61 = 24.6 jobs/day, below the 25 needed, so start with more cards.
7. **Set the pitch at the pacemaker.**
   - Takt = available working time per day ÷ customer demand per day. Pitch = takt × pack-out quantity (LEI).
   - Example (invented): 25,200 s ÷ 420 units = 60 s takt; 12 units a box → pitch = 720 s = 12 min.
   - Release one pitch of work to the pacemaker and withdraw one pitch of finished goods at each interval (paced withdrawal); a levelling box (Heijunka-Box) has one slot per pitch. Practitioners start with intervals of about 5 to 60 minutes (rule of thumb, LEI).
8. **Run and tighten.** Write the card count, the maximum and an owner on each loop. Track stock-outs, overflow and pitch misses per shift. Lower the safety factor or remove cards one at a time while the customer never waits; when it does, add one back and fix the cause (Marek et al. heuristic; Monden: keep the number of kanbans to a minimum). Recalculate when demand, L or a change.

## Validation

Check before answering:

1. L is the full loop time with every component named, not the processing time.
2. D, L and a use the same unit and clock; the card count is rounded up.
3. The safety factor is the user's policy or labelled as an assumption.
4. Supplier capacity exceeds total demand; otherwise capacity comes before cards.
5. The system choice follows part variety and demand swing, and no supermarket is planned for parts that cannot be stocked.
6. Pitch uses takt from available time and real demand, and the pack-out quantity.
7. Every number is the user's, computed from it, or labelled as an assumption or a rule of thumb.

## Output

- `assets/kanban-loop-sheet.md`, filled in: flow and pacemaker, system per part group with the reason, each loop's lead-time build-up and card count, FIFO and CONWIP maxima, pitch, owners and the tracking plan.
- Show every formula with the user's numbers and units. Optional calculator: `scripts/kanban_calc.py` (standard library); every result can be computed by hand from the formulas above. Its `conwip` option gives the card count only; check the output at that count by hand with the practical-worst-case formula.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. Processing time used as the lead time, so the loop starves its customer (fix: step 4).
2. A fractional card count rounded down (fix: step 5).
3. A supermarket for every variant of a high-variety, built-to-order family (fix: step 2).
4. More cards or a bigger safety factor to hide a supplier that lacks capacity (fix: step 3).
5. Long change-overs leaving the part's slot days away, which inflates L (fix: steps 4, 8; hand-offs).
6. A schedule sent to several processes as well as the pacemaker (fix: step 1).
7. Cards set once and never recalculated after demand or lot size changes (fix: step 8).

## Hand-offs

- Long change-overs at the supplier that stretch the queue part of L go to `improve-smed`; breakdowns there go to `improve-tpm`; supplier losses that need a loss tree go to `measure-oee`.
- A supplier or pacemaker that cannot meet takt on a manual line goes to `improve-line-balancing`.
- Throughput time and WIP-cap checks for a CONWIP segment go to `improve-tpt`.
- Supermarket stock-outs and pitch misses are reported at the tier meeting run with `lead-daily-routine`.
- A future state that calls for supermarkets, FIFO lanes or a pacemaker arrives from `improve-vsm`; when the problem is the whole stream, not one loop, go there.
- A CONWIP or kanban loop chosen as a WIP cap arrives from `improve-tpt`; a line balanced to takt that needs a pacemaker and pitch arrives from `improve-line-balancing`.
- Card-reduction and loop-tightening events go to `improve-kaizen`.
- Demand swing or lead-time variation for a statistical safety stock is analysed with `measure-spc`.
- Card discipline at the kanban posts is checked on walks planned with `lead-gemba-walk`.
