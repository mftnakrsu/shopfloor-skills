---
name: measure-oee
description: >-
  Calculates and checks OEE (overall equipment effectiveness) and TEEP for
  a machine, line or plant. Use when anyone asks what an OEE, TEEP,
  availability, performance or quality rate was, even with partial data;
  when an OEE figure or report must be checked before it is shared, for
  example a plant OEE averaged across machines; or when OEE losses must
  be ranked and fixed. Builds an agreed time model, a loss tree in minutes
  (six big losses, Pareto), catches gaming such as excluded changeovers,
  slow ideal cycle times or rework counted as good, and routes the top
  losses to changeover reduction, maintenance or problem solving
  (Gesamtanlageneffektivität, GAE, OEE-Kennzahl, Verfügbarkeit,
  Leistungsgrad, Qualitätsrate, Verlustbaum, Kurzstillstände).
license: MIT
metadata:
  version: "1.0.0"
  category: measure
  standards: "ISO 22400-2 (availability, effectiveness, quality ratio, OEE index)"
---
# OEE and TEEP

## Conventions

- Times are in minutes; ideal cycle times are in seconds per part and are converted to minutes before use.
- Time model, from the top down: all time (Kalenderzeit), then planned production time (Planbelegungszeit), then run time (Laufzeit), then net run time, then fully productive time. Each level is part of the one above, and each loss is the gap between two levels.
- Ideal cycle time (ideale Zykluszeit) is the fastest sustainable cycle per product, not the routing standard or the takt time.
- Good means first-pass good: scrap (Ausschuss) and rework (Nacharbeit) are both quality losses.
- OEE (Gesamtanlageneffektivität) has three factors: availability (Verfügbarkeit), performance (Leistungsgrad) and quality (Qualitätsrate).

## Inputs

- Scope and period: machine, line or plant; which station is the bottleneck; the dates or shifts.
- Time model: shift calendar, planned breaks, unstaffed or unscheduled time, and how planned maintenance, meetings and trials are treated.
- Stop log: each stop with reason and minutes, and the threshold that separates a logged stop from a short stop (minor stop, Kurzstillstand).
- Counts per product: total made, scrap, rework.
- Ideal cycle time per product, and where it comes from.

Ask for every missing input; never invent one.

- Without an ideal cycle time, counts or planned production time, OEE cannot be computed. Ask for the missing item in one short list and stop. You may compute what the data allows (for example availability or quality by count), labelled as partial, and give the formula with the missing value left open. Never assume a nameplate speed, a typical cycle or a benchmark rate.
- A missing stop threshold or reason codes does not block the calculation. Treat every logged stop as an availability loss, write "threshold set by local policy" and list it as an open question.
- If the user gives OEE percentages only, ask for planned production time and fully productive time (or the counts and cycle times) before aggregating.

## Procedure

1. **Agree the time model.** Default convention: only planned breaks and unscheduled time are outside planned production time. Changeovers, planned maintenance, cleaning, trials, waiting for material or operators all stay inside as losses. If the user works to ISO 22400-2, which leaves planned downtime outside planned busy time but keeps setup inside, compute both figures and label each. Mapping of the conventions in [time model](references/time-model.md). Write the convention down and keep it fixed across shifts, machines and months.
2. **Classify every stop.** At or above the threshold: availability loss, split into breakdown, setup and changeover (Rüsten), and other stops (material, operator, starved or blocked). Below the threshold: minor stop, a performance loss. Flag organisational stops (material, staffing, starved or blocked) separately; they are real losses but are fixed outside the machine.
3. **Compute the buckets and factors.**
   - Planned production time (PPT) = scheduled shift time − planned breaks.
   - Run time (RT) = PPT − logged stops.
   - Net run time (NRT) = Σ (total count_i × ideal cycle time_i).
   - Fully productive time (FPT) = Σ (good count_i × ideal cycle time_i), where good = total − scrap − rework.
   - Availability = RT / PPT; performance = NRT / RT; quality = FPT / NRT; OEE = A × P × Q = FPT / PPT.
   - Utilisation = PPT / all time; TEEP = OEE × utilisation = FPT / all time.
   - With several products, use the time-based quality FPT / NRT; good count / total count is close but not exact.
4. **Worked example (invented round numbers).** One 480-min shift, 30 min of breaks, so PPT = 450. Stops: changeover 30, breakdown 20, so RT = 400. One product, ideal cycle 60 s = 1 min, 340 made, so NRT = 340. 10 scrapped, so FPT = 330. Availability = 400/450 = 88.9%; performance = 340/400 = 85.0%; quality = 330/340 = 97.1%; OEE = 330/450 = 73.3%. All time 1,440 min for the day: utilisation = 31.3%, TEEP = 330/1,440 = 22.9%.
5. **Sanity checks.** Performance above 100% means the ideal cycle time is too slow; ask for the real one. Every factor lies between 0 and 100%. The loss minutes add up to PPT − FPT.
6. **Build the loss tree in minutes.**
   - Level 1: availability loss = PPT − RT; performance loss = RT − NRT; quality loss = NRT − FPT; for TEEP, schedule loss = all time − PPT.
   - Level 2, the six big losses: breakdowns; setup and adjustment; minor stops; reduced speed; process defects; start-up rejects (reduced yield). Performance loss splits into minor stops (logged short-stop minutes) and speed loss (the remainder). Quality loss per product = (scrap_i + rework_i) × ideal cycle time_i; keep start-up rejects after a changeover separate where known.
   - Level 3: reason codes, for example "changeover A to B" or "hydraulic pump".
   - Rank all level-3 items by minutes (Pareto) and name the top three. Rank by minutes, never by factor percentages, because a factor's percentage hides how many minutes it costs. Fill in `assets/oee-worksheet.md`.
7. **Aggregate correctly.** Across machines, shifts or days, sum PPT, RT, NRT and FPT first, then compute the factors. Never average OEE percentages, and never multiply averaged factors. Example (invented round numbers): machine 1 has PPT 400 and FPT 360 (90%); machine 2 has PPT 100 and FPT 30 (30%). The mean of 60% is wrong; the plant OEE is (360 + 30) / (400 + 100) = 78.0%. For a line, report the bottleneck's OEE and the line output; a non-bottleneck's OEE gain adds stock, not output.
8. **Check for gaming.** Name each distortion found and recompute without it: changeovers or planned maintenance moved outside PPT; an ideal cycle time slower than the best demonstrated rate; rework or sorted parts counted as good; the stop threshold raised so breakdowns become minor stops; percentages averaged; a headline OEE that hides a falling factor. Effect sizes in [loss tree](references/loss-tree.md).
9. **Route the top losses.**

   | Loss | Route |
   |---|---|
   | Setup, changeover, start-up rejects | Changeover reduction study (SMED) |
   | Breakdowns | Planned maintenance and TPM (MTBF and MTTR review) |
   | Minor stops, reduced speed | Autonomous maintenance (restore basic conditions) and focused improvement |
   | Process defects, rework | Structured root-cause work; an 8D for complaints or repeat defects |
   | Material, staffing, starved or blocked | The owning area, through the daily tier meeting |

   Work on the bottleneck first.
10. **Benchmark with care.** Compare first with the asset's own baseline, then with similar assets and product mix. The often-quoted 85% "world class" is an aspirational reference, not a standard (source in [loss tree](references/loss-tree.md)).

The optional calculator `scripts/oee.py` (standard library) computes steps 3, 6 and 7 from a JSON file. Everything above works by hand without it.

## Validation

Check before answering:

1. The time model and its convention are stated, and changeovers sit inside PPT unless the user's convention says otherwise (labelled).
2. Every ideal cycle time came from the user; none was assumed.
3. Rework is counted as a loss.
4. A × P × Q equals FPT / PPT, within rounding.
5. Loss minutes add up to PPT − FPT.
6. Any aggregate is built from summed minutes, not averaged percentages.
7. Each top loss has a route and an owner to be named.

## Output

- `assets/oee-worksheet.md`, filled in: time model, buckets, factors, OEE and TEEP, the loss tree in minutes ranked, gaming checks, routes, and open questions.
- For a check of an existing figure: say first whether it is right, then the corrected figure with its calculation, then the reason.
- Show each formula with the user's numbers. Round factors to one decimal place only at the end.
- Write for the user in plain words; never cite this skill's step numbers or file names.

## Pitfalls

1. OEE averaged across machines, shifts or days (fix: step 7).
2. Changeover or planned maintenance moved out of PPT to lift availability (fix: steps 1, 8).
3. Routing standard or a slow cycle used as ideal cycle time (fix: steps 5, 8).
4. Rework counted as good (fix: step 3).
5. Losses ranked by factor percentages instead of minutes (fix: step 6).
6. OEE chased on a non-bottleneck (fix: steps 7, 9).
7. An ideal cycle time or rate invented when it is missing (fix: Inputs).

## Hand-offs

- Process defects that come from a customer complaint, or repeat, go to `solve-8d`.
- Losses owned by other areas (material, staffing) and red OEE results go to the board in `lead-daily-routine`.
