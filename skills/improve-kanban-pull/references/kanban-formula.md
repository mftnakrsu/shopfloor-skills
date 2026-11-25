# Kanban formula

The Toyota formula for the number of kanbans, what goes into each term, variants, and the pitch formula, with worked examples.

## Contents

- Symbols
- The Toyota formula
- Building the replenishment lead time
- Lot and withdrawal batching
- Safety factor and statistical safety stock
- Two-card systems
- Pitch and paced withdrawal
- Worked example
- Status of the formulas
- Sources

## Symbols

| Symbol | Meaning | Unit |
|---|---|---|
| D | Average demand of the customer process for this part number | pieces per working hour or day |
| L | Replenishment lead time of the loop | working hours or days, same clock as D |
| a | Container quantity (pieces per kanban) | pieces |
| s | Safety factor | share |
| n | Number of kanbans in the loop | cards |
| k | Containers the supplier collects before it starts a lot, or the customer withdraws at once | containers |

## The Toyota formula

n × a = D × L × (1 + s), so n = D × L × (1 + s) ÷ a, rounded up to a whole card.

- Akturk & Erhun state it in this form as "the Toyota formula" for the maximum inventory of a loop, n × a. They take s = 0.05 in their study and note that the lead time is a property of the shop floor (load, mix, batch sizes), not of the part.
- Marek et al. state Monden's formula as cards = (D × L + w) ÷ a, with a buffer w of 10% of D × L in their example. This is the same formula with w = s × D × L.
- Co & Moosa describe Toyota's practice as average demand over the order cycle inflated by a constant overplanning factor.
- n × a is the most stock the loop can hold. Average stock is lower, because part of it is always on the way.

## Building the replenishment lead time

L runs from "container emptied" to "full container back at the customer". Sum, in one clock:

| Component | What to measure | Often missed |
|---|---|---|
| Card wait | Time from emptying until the card is collected from the post | Yes: collection runs, end-of-shift batching |
| Card transport | Time until the card reaches the supplier's board | |
| Queue at the supplier | Time until the order starts, including the wait for the part's slot in the change-over cycle | Yes: the largest part in most loops |
| Processing | Set-up share and run time for one container or lot | |
| Curing, cooling, inspection | Any fixed delay after processing | Yes |
| Transport back | Time until the full container is at the point of use | |

- The queue grows with change-over time and the number of part numbers on the machine: if each part runs once every EPEI interval (every part every interval), a card can wait up to that interval (LEI). Smartsheet lists a variant that adds D × EPEI ÷ a cards for this.
- Measure L on the floor by tagging 10 to 20 cards (rule of thumb), not from ERP lead times.

## Lot and withdrawal batching

If the supplier waits until k cards are on the board before it starts a lot, or the customer withdraws k containers in one trip, add k − 1 cards (Roser). Peak demand above the average during L also needs extra cards.

## Safety factor and statistical safety stock

- s is set by local policy. Akturk & Erhun use 0.05; Marek et al. use 0.10. Roser treats it as an optional margin added last, "until people feel comfortable".
- When daily demand varies, a statistical form (Smartsheet) is n = (D × L + z × σ_L) ÷ a, with σ_L the standard deviation of demand over L and z = 1.645 for a 95% service level.
- Monden expected the kanban system to absorb daily swings within about 10% of the monthly plan; larger swings are handled by recalculating the cards with each plan (cited by Akturk & Erhun).

## Two-card systems

Monden's classic system uses withdrawal (conveyance) and production kanbans. Size each loop with its own L. Marek et al. double the count when one card authorises both production and movement.

## Pitch and paced withdrawal

- Takt = available working time per day ÷ customer demand per day (LEI).
- Pitch = takt × pack-out quantity: the time the pacemaker needs to make one pack-out container (LEI).
- At each pitch interval one pitch of work is released and one pitch of finished goods is withdrawn. LEI suggests starting with increments of about 5 to 60 minutes of work.

## Worked example

Invented numbers. A supplying cell feeds a customer line that uses D = 50 pieces per working hour.

- L = card wait 0.5 h + card transport 0 h + queue 3 h + processing 1.5 h + transport back 1 h = 6 h.
- a = 40 pieces; s = 10% (set by local policy).
- n = 50 × 6 × 1.1 ÷ 40 = 330 ÷ 40 = 8.25 → 9 cards; maximum loop stock 360 pieces.
- The supplier starts a lot only when 3 cards are waiting: n = 9 + 2 = 11 cards.
- If set-up reduction halves the queue to 1.5 h: L = 4.5 h, n = 50 × 4.5 × 1.1 ÷ 40 = 6.19 → 7 cards (+ 2 = 9).

Pitch: 25,200 s ÷ 420 units = 60 s takt; 12 units per box → 720 s = 12 min.

## Status of the formulas

The Toyota formula and the pitch formula are sourced as cited. The k − 1 batching rule follows Roser. The 10 to 20 tagged cards are a rule of thumb. The formula is an estimate; Roser and Marek et al. both tune the count in operation. Gershwin's lecture notes list Monden's rule that the number of kanbans should be minimised.

## Sources

- Akturk, M. S. and Erhun, F.: [An overview of design and operational issues of kanban systems, International Journal of Production Research 37(17), 1999](https://repository.bilkent.edu.tr/bitstream/11693/25185/1/Overview%20of%20design%20and%20operational%20issues%20of%20kanban%20systems.pdf)
- Marek, R. P., Elkins, D. A. and Smith, D. R.: [Understanding the fundamentals of kanban and CONWIP pull systems using simulation, Winter Simulation Conference 2001](https://www.informs-sim.org/wsc01papers/122.PDF)
- Co, H. C. and Moosa, S.: [Overplanning factor in Toyota's formula for computing the number of kanban, IIE Transactions 29(5), 1997](https://ink.library.smu.edu.sg/lkcsb_research/892)
- Monden, Y.: *Toyota Production System: An Integrated Approach to Just-In-Time*, 4th ed., CRC Press, 2011
- Roser, C.: [How many kanbans? The kanban formula, part 2](https://www.allaboutlean.com/kanban-formula-part2/)
- Gershwin, S. B.: [Toyota Production System, MIT 2.854 lecture notes, 2016](https://ocw.iti.hr/courses/mechanical-engineering/2-854-introduction-to-manufacturing-systems-fall-2016/lecture-notes/MIT2_854F16_ToyotaProdSys.pdf)
- Smartsheet: [Simplified kanban formulas](https://www.smartsheet.com/simplified-kanban-formulas-project-managers)
- LEI: [Lexicon, pitch](https://www.lean.org/lexicon-terms/pitch/)
- LEI: [Top 5 value-stream mapping eBook, glossary and future-state guidelines](https://email.lean.org/hubfs/ebook%20files/eBook-Top5-VSM-final.pdf)
- LEI: [Lexicon, every product every interval](https://www.lean.org/lexicon-terms/every-product-every-interval/)
