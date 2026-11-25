---
name: improve-line-balancing
description: >-
  Balances manual assembly lines and cells in a fixed order: volume, mix,
  takt, ergonomics, then a fill-up yamazumi. Merges or splits stations,
  quantifies operator, station and machine savings, and outputs the
  standard work for the new balance. Use when asked to balance or
  rebalance a line, build a yamazumi or operator balance chart, calculate
  a takt time or operator count, or review or audit a takt or headcount
  calculation; also for uneven operator loads, or when demand or mix
  changes (Taktzeit, Austaktung,
  Linienabstimmung, Bandabgleich, Yamazumi, Personalbedarf,
  Mitarbeiterbedarf, Arbeitsverteilung, Standardarbeit).
license: MIT
metadata:
  version: "1.0.0"
  category: improve
  standards: ""
---
# Line balancing

## Conventions

- Times are in seconds per unit. Takt (Taktzeit) is effective working time ÷ customer demand, over the same period.
- Work content is the sum of manual element times for one unit; for a mix, the demand-weighted sum.
- Planned cycle time is the load limit per operator, at or below takt (set by local policy).
- The yamazumi (operator balance chart) has one bar per operator, stacked elements and a takt line.
- Balancing (Austaktung) follows a fixed order: volume, mix, takt, ergonomics, fill-up. Never start with the yamazumi.

## Inputs

- Volume: customer demand per day or week, from actual shipments over about 12 months, and how stable it is.
- Working time: shifts per day, shift length, scheduled breaks, meetings and cleanup.
- Mix: the variants and their share of demand, and which elements differ by variant.
- Work elements in their possible order (precedence), each with an observed time: the lowest repeatable time of 10 or more timed cycles (rule of thumb), plus out-of-cycle work such as fetching material.
- Machines: automatic cycle time and load/unload time of each machine, and how many there are.
- Ergonomics: weights lifted, lift heights and frequency, awkward postures, and any NIOSH, RULA or REBA results.
- The current line: stations, operators per shift, planned cycle time policy.

Ask for every missing fact; never invent one.

- Without demand, working time or element times, ask for them in one short list and stop. At most add the blank `assets/balance-worksheet.md` and describe the method. Do not give a takt, an operator count or a saving on invented numbers.
- Missing ergonomic data does not block the calculation. Mark every lift or awkward posture "ergonomics not assessed" and list the assessment as an open action.
- A missing planned cycle time policy: balance to takt and say so.

## Procedure

1. **Volume.** Convert demand to demand per shift: daily demand ÷ shifts per day. Use long-term average shipments, not orders or a peak day. Cover spikes with a finished-goods buffer or overtime, never with a daily takt change (Rother & Harris).
2. **Mix.** List the variants and shares. Weighted work content = Σ (share × variant work content). If any variant's work content differs from another's by more than about 30%, consider a separate line or cell for it (Rother & Harris). Keep the variant-specific elements as their own rows; they are checked in step 5.
3. **Takt.**
   - Effective time = shift time − scheduled breaks, meetings and cleanup. Never subtract unplanned downtime, changeovers, scrap or other losses (Rother & Harris). Losses are fixed at their source, or covered by a buffer or overtime, not by headcount.
   - Takt = effective time per shift ÷ demand per shift.
   - Theoretical operators = weighted work content ÷ planned cycle time (or takt). Round with the fraction rule in [takt and operators](references/takt-and-operators.md): below 0.3 remove waste instead of adding a person; 0.3–0.5 start with the higher count and review after two weeks of kaizen; above 0.5 add the person and keep removing waste (rule of thumb).
   - Below about 10 s or above about 120 s takt, consider a second cell or more end items in the cell (Rother & Harris).
   - Example (invented): 2 shifts of 480 min, 2 × 10 min breaks per shift: 460 min = 27,600 s per shift. Demand 1,380 per day = 690 per shift. Takt = 27,600 ÷ 690 = 40 s. Work content 150 s ÷ 40 s = 3.75 → 4 operators.
4. **Ergonomics, before loading.** Screen each element with a public method: lifts with the revised NIOSH lifting equation (lifting index LI = load ÷ recommended weight limit), repetitive upper-limb work with RULA, whole-body postures with REBA. Details and thresholds in [ergonomics screening](references/ergonomics-screening.md).
   - LI above 1.0, RULA 5 or more, or REBA 8 or more: a high-risk element that must be redesigned (bring the load to waist height, a lift aid, a lift-assist table; for a posture, a tool support or a new work height). RULA 7 means change now. Each fix is an action with an owner and date; until it is in, plan job rotation (rule of thumb).
   - Never put two high-risk elements on one operator, and never fill an operator up with extra lifts or the same posture (rule of thumb).
5. **Fill-up yamazumi.**
   - Take the elements in their precedence order. Load operator 1 up to the planned cycle time, then operator 2, and so on. The last operator holds the remainder: that gap is the visible kaizen target. Do not share the work out equally; equal shares hide the waste (LEI; rationale in [fill-up yamazumi](references/fill-up-yamazumi.md)).
   - Remove waste elements (walking, searching, waiting) before loading, then recompute step 3.
   - Mix check: for each variant, every operator's load must stay at or below the planned cycle time. If one variant overloads an operator, move the element or level the sequence and check the average over the repeating sequence.
   - No element may exceed the planned cycle time on its own; if one does, split it, add a parallel station, or shorten it.
6. **Stations and machines.**
   - Merge stations when operators can share one footprint and walking stays small; split a station when one element or variant overloads it.
   - Machine check: one cycle (load, unload and automatic time) must fit within takt. Machines needed = cycle per unit ÷ takt, rounded up. Free the surplus machines.
7. **Quantify the savings.**
   - Operators saved = (current − new) per shift × shifts. Stations, machines and floor space saved.
   - Units per labour hour = units per day ÷ (operators × shifts × effective hours). Gain % = new ÷ old − 1.
   - Line efficiency = weighted work content ÷ (operators × takt). Balance loss = 1 − efficiency.
   - Example (invented): 1,380 units ÷ (5 × 2 × 7.67 h, from 27,600 s ÷ 3,600) = 18.0; with 4 operators 22.5 units per labour hour, +25%.
8. **Standard work.** For each operator: the element sequence, the manual, walk and machine times against takt (combination table), the layout with walk path, standard WIP, and the quality and safety points (standardised work chart). Templates in `assets/standard-work-sheet.md`; document list and the training steps in [standard work](references/standard-work.md). Train with TWI Job Instruction, run a pilot, track hour-by-hour output, and re-time after 2–4 weeks (rule of thumb) or when takt changes.

Optional: `scripts/balance.py` runs steps 3, 5 and 7 from a JSON file. The procedure above gives the same result by hand.

## Validation

Check before answering:

1. Takt uses effective time with only scheduled stops removed; demand and time cover the same period.
2. Operator count = work content ÷ planned cycle time, with the fraction rule stated.
3. Every operator's load, for every variant, is at or below the planned cycle time.
4. The fill-up leaves the gap on the last operator, and the gap is named as a kaizen target.
5. Every lift and awkward posture has an assessment or is listed as open; every high-risk result has a fix with owner and date.
6. Every machine cycle fits within takt.
7. Savings are in numbers: operators, stations, machines and units per labour hour.
8. No input was invented.

## Output

- `assets/balance-worksheet.md`, filled in: volume, mix, takt, operator count, ergonomic screen, current and new yamazumi as a table (operator, elements, load per variant, gap to takt), machine check and savings.
- `assets/standard-work-sheet.md` filled in for each operator: the element sequence, the operator's cycle time against takt, and the standard WIP as a number of parts and where they sit (e.g. one unit in a machine or buffer). In a chat answer, one compact table per operator is enough; a description of what the sheet should contain is not.
- Then the open actions: ergonomic fixes, kaizen on the last operator's gap, pilot and re-timing.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. Downtime or changeovers subtracted from takt, inflating headcount (fix: step 3).
2. Takt from a peak day or orders instead of average shipments (fix: step 1).
3. Equal-share balancing that spreads the waste across everyone (fix: step 5).
4. Balancing on the average variant while one variant overloads an operator (fix: steps 2, 5).
5. Filling an operator up with lifts or awkward postures (fix: step 4).
6. Ignoring machine cycle time and out-of-cycle work (fix: steps 5, 6).
7. Posting new standard work without training or re-timing (fix: step 8).

## Hand-offs

- Track hour-by-hour output and the open ergonomic and kaizen actions in the tier meetings of `lead-daily-routine`.
- A safety incident or a repeat output or quality problem with an unknown cause on the new balance goes to `solve-8d`.
