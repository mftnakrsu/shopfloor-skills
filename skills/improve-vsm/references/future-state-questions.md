# Future-state questions

The question sequence for the future-state design, with decision rules, supermarket sizing and pitch. Answer the questions in order: each answer limits the ones after it.

## Contents

- Where the sequence comes from
- The eight questions
- Kaizen bursts
- Supermarket sizing after a shared process
- Pitch and paced withdrawal
- Pacemaker and bottleneck
- Checks before the design is agreed
- Sources

## Where the sequence comes from

Paraphrased from Rother & Shook via LEI's six guidelines (LEI Lean Post); some summaries merge two questions into seven (Teamguru; MyEducator).

## The eight questions

| # | Question | Decision rules |
|---|---|---|
| 1 | What is the takt time? | Available working time of the processes closest to the customer ÷ customer demand. Planned breaks are always deducted; state whether other planned downtime is too. |
| 2 | Finished-goods supermarket, or build to shipping? | Build to shipping when the time from pacemaker to dock is short and reliable against what the customer accepts; otherwise a finished-goods supermarket the customer pulls from. |
| 3 | Where can continuous flow run? | Join processes whose C/T are close to takt, whose equipment is dedicated and reliable, and whose C/O is short. Combine or move work so each C/T approaches but does not exceed takt (MyEducator). Look for flow in today's layout before moving equipment (Shook). |
| 4 | Where are supermarket pull or FIFO lanes needed upstream? | A supermarket where a process serves several streams, has long C/O or is far away. A FIFO lane with a maximum quantity where variety is too high to stock every part number. Each inventory left on the map needs a named cause. |
| 5 | Which single process gets the customer schedule? | The pacemaker: usually the most downstream pull point, often final assembly; everything after it flows. It may sit further upstream if units flow FIFO from there to the end (LEI eBook glossary). |
| 6 | How is the mix levelled at the pacemaker? | Spread part numbers evenly over the day or shift instead of long runs. Levelling needs short C/O at the pacemaker and enough supermarket stock upstream. |
| 7 | What increment of work is released and withdrawn? | Pitch = takt × pack-out quantity (or a multiple). Release one pitch of work at the pacemaker while taking away the same amount of finished goods, typically every 5 to 60 minutes (LEI lexicon). |
| 8 | Which process improvements are needed? | Every gap between the design and today's capability: C/T above takt, C/O too long for the needed EPEI, low uptime, low %C/A. Each becomes a kaizen burst. |

## Kaizen bursts

- Draw a burst wherever an answer assumes something not yet true. Write on it the gap in numbers: from what to what, at which process.
- Typical bursts: C/O reduction at a shared machine, uptime at a process in flow, %C/A at a process feeding the pacemaker, work moved between stations to get under takt, a supplier delivery frequency.
- Removing inventory on the map without removing its cause is the classic error: the stock comes back, or the pacemaker starves (Teamguru).

## Supermarket sizing after a shared process

A supermarket after a batch process must cover consumption until that part number is made again.

- Minimum stock ≈ daily demand × (EPEI + replenishment time) + safety stock. The first term follows from EPEI; the safety stock is set by local policy.
- EPEI estimate (practitioner calculation; rule of thumb): EPEI in days = (number of part numbers × C/O per change) ÷ time left each day for changeovers, where time left = available time − run time needed for the day's demand of all part numbers.
- Example (invented): 6 part numbers, 40 min per C/O = 240 min; available 900 min a day, run time needed 840 min → 60 min a day for changeovers → EPEI = 4 days. At 300 units a day the supermarket needs at least 1,200 units before safety.
- To shrink the supermarket, shorten EPEI first: cut C/O, or free capacity. Put that on the map as a kaizen burst and size the supermarket for today's EPEI until the burst is done.
- Detailed kanban loop sizing belongs to a pull-system study; here the check is only that the designed stock is not below the run interval.

## Pitch and paced withdrawal

- Pitch = takt × pack-out quantity. Example (invented): takt 48 s × 25 units = 1,200 s = 20 min.
- A material handler releases one pitch of work to the pacemaker and withdraws one pitch of finished goods on a fixed route. A missed pitch is seen within one interval, not at the end of the shift (LEI eBook).

## Pacemaker and bottleneck

The pacemaker is chosen as a scheduling point, close to the customer. It is not the bottleneck: TPS does not let a bottleneck set the pace of the stream; bottlenecks from downtime, quality or long C/O are fixed (Shook; LEI eBook glossary).

## Checks before the design is agreed

1. Takt, pitch and the ladder use the same demand and working time.
2. One schedule point only; every other link is flow, a supermarket or a FIFO lane with a maximum.
3. Every process in flow is at or under takt, or has a burst.
4. Every supermarket covers at least EPEI plus replenishment time, or has a C/O burst and is sized for today until the burst is done.
5. The future ladder adds up to the stated target lead time.
6. The design does not bend to today's planning-system settings; the settings change to fit the design (Teamguru).

## Sources

- LEI: [6 guidelines for moving toward a lean value stream](https://www.lean.org/the-lean-post/articles/6-guidelines-for-moving-toward-a-lean-value-stream/)
- LEI: [eBook, Why, When and How Value-Stream Mapping is a Vital Part of Continuous Improvement](https://email.lean.org/hubfs/ebook%20files/eBook-Top5-VSM-final.pdf)
- LEI: [Lexicon, value-stream mapping](https://www.lean.org/lexicon-terms/value-stream-mapping/)
- LEI: [Lexicon, every product every interval](https://www.lean.org/lexicon-terms/every-product-every-interval/)
- Shook, J.: [Misunderstandings about value-stream mapping, flow analysis and takt time](https://www.lean.org/the-lean-post/articles/misunderstandings-about-value-stream-mapping-flow-analysis-and-takt-time/)
- Teamguru: [Future state value stream mapping](https://www.teamguru.com/guides/future-state-value-stream-mapping)
- MyEducator: [Tools, future state](https://app.myeducator.com/reader/web/1716c/chapter06/wg1v6)
- Rother, M. and Shook, J.: *Learning to See*, Lean Enterprise Institute, 1999
