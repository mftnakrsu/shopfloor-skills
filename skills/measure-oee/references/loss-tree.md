# Loss tree

The six big losses and their factors, how much each gaming error moves OEE, where to route each loss, and what benchmarks are worth.

## Six big losses

| Factor | Loss | Typical content | Other names |
|---|---|---|---|
| Availability | Breakdowns | Equipment and tooling failure, unplanned maintenance | Equipment failure |
| Availability | Setup and adjustment | Changeovers, major adjustments, warm-up, cleaning, planned maintenance inside PPT | Rüsten und Einrichten |
| Performance | Minor stops and idling | Jams, misfeeds, blocked sensors, short clearing; usually a minute or two, fixed by the operator | Kurzstillstände, Leerlauf |
| Performance | Reduced speed | Running slower than the ideal cycle: wear, dirt, material, inexperience | Geschwindigkeitsverlust |
| Quality | Process defects | Scrap and rework in steady production | Running rejects |
| Quality | Start-up rejects | Defects from start-up or changeover until stable running | Reduced yield, Anlaufverluste |

- Mapping after Vorne and Wikipedia (total productive maintenance, TPM). Both name sets describe the same six losses; accept either.
- One practitioner source also puts lack of material or operators and starved or blocked time under equipment failure (Vorne). This skill keeps them as availability losses but flags them as organisational, because the fix lies outside the machine.
- Minor stops are usually under-recorded and become invisible to operators (Vorne). If none are logged, the performance loss cannot be split; propose a short tally study or cycle-level data.
- Lost parts = loss minutes ÷ ideal cycle time in minutes. Use it to state a loss in parts the line could have made.

## Gaming and calculation errors, with their effect

All figures are this project's own calculations on the invented shift used in the skill: PPT 450, run time 400, net run time 340, fully productive time 330, OEE 73.3%.

| Error | What changes | Reported OEE | Effect |
|---|---|---|---|
| Ideal cycle 66 s instead of the true 60 s | Net run time 374, FPT 363, performance 93.5% | 80.7% | +7.3 points, no real gain |
| 30-min changeover moved out of PPT | PPT 420, availability 95.2% | 78.6% | +5.2 points |
| Assumes 10 additional reworked parts (the example has none), counted as good (true FPT 320) | Quality 97.1% instead of 94.1% | 73.3% instead of 71.1% | +2.2 points |
| Threshold raised so the 20-min breakdown, made of 4-min stops, becomes minor stops | Availability 93.3%, performance 81.0% | 73.3% | OEE unchanged, but the breakdown vanishes from the stop list |
| Plant OEE as the mean of machine percentages | Small machines weigh as much as large ones | Can be high or low | Always sum minutes first |
| Mean availability × mean performance × mean quality | Not equal to the summed-bucket result | Wrong | Compute factors from summed buckets |
| Nameplate rate that the process never reaches | Performance looks too low | Too low | Use the best demonstrated sustained rate per product |

- Performance above 100% means the ideal cycle time is set too slow (Vorne).
- A headline OEE can rise while a factor falls: in one practitioner example, OEE rose from 85.1% to 85.7% while quality fell from 99.5% to 95.0% (Vorne). Always report the three factors with the OEE.
- Definitions must be the same across shifts and departments, and should be cross-checked against shop-floor records (Genium).

## Routing

| Loss | First countermeasure | Why |
|---|---|---|
| Setup and changeover | Changeover study: separate internal from external work, then shorten internal work (single-minute exchange of die, SMED) | Changeovers are typically the largest setup loss (Vorne) |
| Start-up rejects | The same changeover study, plus fixed settings for the first good part | They follow changeovers (Vorne) |
| Breakdowns | Planned maintenance, review of mean time between failures (MTBF) and mean time to repair (MTTR), why-why analysis on repeats | TPM planned-maintenance pillar (Wikipedia, TPM) |
| Minor stops, reduced speed | Autonomous maintenance: clean, inspect, lubricate, remove contamination sources; focused improvement | TPM autonomous-maintenance and focused-improvement pillars (Wikipedia, TPM) |
| Process defects | Root-cause analysis; quality maintenance for chronic defects | TPM quality-maintenance pillar (Wikipedia, TPM) |
| Material, staffing, starved, blocked | Owner in logistics, planning or the upstream station, tracked on the tier board | Not a machine loss |

Re-measure after a change over the same window length and with the same time model.

## Benchmarks

- The 85% "world class" figure is attributed to the TPM originator (Vorne), presented as a practical level seen among award-winning Japanese plants; it is often split as availability 90%, performance 95%, quality 99% (Vorne).
- The same source says most manufacturers run closer to 60%, without a disclosed method, and warns against comparing dissimilar processes or product mixes (Vorne).
- Literature reviews note that OEE definitions differ in loss definition and in scope, from a single machine to a plant (Ahmed, University of Groningen).
- Compare an asset first with its own baseline, then with similar assets and mix. Treat 85% as a reference only.

## Sources

- Vorne: [Six big losses](https://www.oee.com/oee-six-big-losses/); [Calculating OEE](https://www.oee.com/calculating-oee/); [World-class OEE](https://www.oee.com/world-class-oee/)
- Wikipedia: [Total productive maintenance](https://en.wikipedia.org/wiki/Total_productive_maintenance)
- Genium: [Calculate OEE correctly](https://genium.vn/en/insights/tinh-oee-dung-cach)
- Ahmed: [OEE thesis, University of Groningen](https://fse.studenttheses.ub.rug.nl/22111/1/MAhmed_IPFinal.pdf)
