# Board design

How to lay out a tier board (Shopfloor-Board) and choose its KPIs (Kennzahlen).

## Contents

- Category mapping
- Board zones
- Six questions for choosing KPIs
- How many KPIs
- Red, green and trend
- The hour-by-hour board
- Analog first
- Sources

## Category mapping

| SQDCP | German QKLSP (ifaa) | QCDSM (Suzaki, via BVL) | Example KPIs, shortened (ifaa) |
|---|---|---|---|
| Safety | Sicherheit | Safety | accidents, first-aid book entries, hazard reports, risk assessments, 5S level |
| Quality | Qualität | Quality | customer complaints, scrap, first-pass yield, ppm, rework time, top quality problems |
| Delivery | Logistik | Delivery | output against plan, delivery-date adherence, throughput time, work in process, inventory coverage |
| Cost | Kosten | Cost | productivity, OEE, downtime, scrap cost, setup and maintenance cost |
| People | Personal | Morale | attendance, sickness rate, improvement suggestions, overtime, training hours, qualification matrix |

- In German expert interviews, quality and productivity KPIs were used in the shopfloor management of 94% of the companies. Quality, productivity and delivery were the most common categories, and explicit cost KPIs were rare (BVL).
- So the cost column is often empty. Productivity, OEE and downtime count as cost KPIs (ifaa), so a productivity measure can fill it.
- Map the user's local category names to SQDCP before checking for gaps.

## Board zones

A board has three zones (ifaa):

1. **KPIs:** target against actual for each category.
2. **Improvement actions:** current and planned actions with their status, so their effect can be followed in the KPIs.
3. **Order and capacity situation:** order priorities, production plan, machine availability, staffing and shift plan, capacity use and loss times.

The training plan and the cleaning plan are steering items too (ifaa). An audited board also shows the current production status, the agenda, the KPI profile and the problem solving in progress (ZielKom report).

## Six questions for choosing KPIs

Work through these in a workshop with the people who will use the board. Questions paraphrased (ifaa):

1. Which company goals does this area serve?
2. Which goals for the area follow from them?
3. Which measures can the area itself influence, and which of them decide whether the goals are met?
4. Which internal or external problems block the targets today?
5. Which of these measures can the team record and show on site simply, quickly and cheaply, and which of them really help?
6. What other area information does the team need every day?

A board is specific to its company and area. Review its design from time to time (ifaa).

## How many KPIs

- Keep the number of KPIs limited (Meißner et al. 2018, via IEOM 2024). Digital systems make it easy to add many automatic KPIs and lose focus (IEOM 2024).
- Use 5–8 KPIs per board as a rule of thumb.
- KPIs are consolidated on the way up the hierarchy (BVL), so a higher-tier board shows fewer, aggregated KPIs and the escalations from below.

## Red, green and trend

Red or green compares actual with target. Check the direction of the KPI first.

| KPI type | Red when | Worked example (invented round numbers) |
|---|---|---|
| Higher is better, e.g. first-pass yield | actual < target | target 98%, actual 96%: red |
| Lower is better, e.g. absenteeism | actual > target | target 4%, actual 3%: green |

Trend shows whether the actual is improving, flat or worsening over recent periods. How many periods to compare is set by local policy.

## The hour-by-hour board

- A board beside the process that compares planned and actual output for each hour. When an hour misses the plan, the team writes down the problem and looks for its cause (LEI lexicon).
- It is a tool for finding problems, not for scheduling (LEI lexicon).
- In a pull process it compares downstream requests with actual production (LEI lexicon).
- Other names: production analysis board, production control board, progress control board (LEI lexicon).

Cumulative gap = cumulative actual − cumulative plan.

Worked example (invented round numbers):

| Hour | Plan | Actual | Cumulative gap | Problem or cause |
|---|---|---|---|---|
| 06–07 | 50 | 50 | 0 | — |
| 07–08 | 50 | 40 | −10 | Parts missing at station 3 |
| 08–09 | 50 | 45 | −15 | Fixture change took longer than planned |
| 09–10 | 50 | 50 | −15 | — |

Check: (50 + 40 + 45 + 50) − (4 × 50) = 185 − 200 = −15.

## Analog first

- Start with a paper board. Board design takes many rounds, paper trials are faster and cheaper, and managers who build their own board understand it and own it (IEOM 2024).
- Keep the team level analog where people have little screen access or need flexibility. Department and plant levels can use standard digital KPIs plus manual entries such as accidents and attendance (IEOM 2024).
- Going digital exposes data-quality problems, so whoever presents a KPI checks its data before the meeting (IEOM 2024).

## Sources

- Conrad, Eisele: *Shopfloor-Management*, ifaa Betriebspraxis & Arbeitsforschung 235, 2019. [PDF](https://www.arbeitswissenschaft.net/fileadmin/Downloads/Angebote_und_Produkte/Publikationen/ifaa_BA_235_Shopfloormanagement.pdf)
- BVL/IGF 19372 N: ShopfloorPulse final report, which also cites Suzaki's categories. [PDF](https://www.bvl.de/files/1951/2125/2131/2133/Abschlussbericht_ShopfloorPulse_19372_N.pdf)
- Dinkelmann, Weinmann: "Maturity Steps towards a Digitally Integrated Shop Floor Management", IEOM 2024, which cites Meißner et al. 2018. [PDF](https://ieomsociety.org/proceedings/2024germany/100.pdf)
- Lean Enterprise Institute: [Lexicon: production analysis board](https://www.lean.org/lexicon-terms/production-analysis-board/)
- TU Darmstadt PTW et al.: ZielKom final report, BMBF project 2014–2017. [PDF](https://tuprints.ulb.tu-darmstadt.de/server/api/core/bitstreams/a0b83c65-e75d-4392-90ab-4500cecf4bc8/content)
