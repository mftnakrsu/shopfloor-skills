# Pull system design sheet

Value stream or area: ______ · Product family: ______ · Date: ______ · Prepared by: ______

## 1. Flow and pacemaker

- Processes from the pacemaker back to raw material: ______
- Pacemaker (the only process that gets the customer schedule): ______
- Available working time per day at the pacemaker (breaks out): ______ · Customer demand per day: ______

## 2. System per part group

| Part group | Part numbers | Demand per day | Swing against plan (%) | Made to stock or to order | System chosen | Reason |
|---|---|---|---|---|---|---|
| | | | | | | |

## 3. Supplier capacity

| Supplier process | Capacity per hour after change-overs | Total demand per hour of all parts it serves | Capacity > demand? |
|---|---|---|---|
| | | | |

## 4. Kanban loops

| Item | Loop 1 | Loop 2 | Loop 3 |
|---|---|---|---|
| Part number | | | |
| Demand D (pieces per working hour) | | | |
| Card wait at the post (h) | | | |
| Card transport (h) | | | |
| Queue at the supplier, including change-over slot (h) | | | |
| Processing (h) | | | |
| Curing, cooling, inspection (h) | | | |
| Transport back (h) | | | |
| Replenishment lead time L (h) = sum | | | |
| Container quantity a | | | |
| Safety factor s (set by local policy) | | | |
| D × L × (1 + s) ÷ a | | | |
| Cards, rounded up | | | |
| Lot or withdrawal batch k; add k − 1 | | | |
| Total cards n | | | |
| Maximum loop stock n × a | | | |
| Owner | | | |

## 5. FIFO lanes and CONWIP loops

| Loop | From → to | Usage or output per hour | Longest stop to cover, or target throughput time | Maximum or cards | Output check | Owner |
|---|---|---|---|---|---|---|
| | | | | | | |

## 6. Pitch

- Takt = available time ÷ demand = ______ s
- Pack-out quantity: ______ · Pitch = takt × pack-out quantity = ______ min
- Withdrawal route interval: ______ · Levelling box slots per shift: ______

## 7. Tracking

| Measure | Target | Frequency | Owner |
|---|---|---|---|
| Stock-outs per loop | | per shift | |
| Overflow (more full containers than cards allow) | | per shift | |
| Pitch hits and misses at the pacemaker | | per shift | |
| Measured L against the L used for sizing | | monthly | |
| Card count review (demand, L, a changed?) | | each plan period | |
