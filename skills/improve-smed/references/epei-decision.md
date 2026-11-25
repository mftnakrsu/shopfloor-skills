# EPEI decision

How to compute EPEI, choose the interval and lot sizes, and decide whether a changeover saving becomes capacity or smaller lots.

## Formulas

Per period (a week, for example):

- A = available time the machine is planned to produce.
- R = Σ demandᵢ × cycle timeᵢ, the run time demand needs.
- C = Σ changeover timeᵢ for one cycle through all products.
- A − R is the time left for changeovers. If A ≤ R, the machine is over capacity before any changeover.
- Cycles possible per period = (A − R) / C.
- Minimum EPEI = C / (A − R), in periods.
- Lot sizeᵢ = demandᵢ × chosen interval.
- Changeover time per period = C / chosen interval.

LEI describes the method as two questions: is there enough capacity to run the parts, and how much time is left for changeovers, which sets the lot size. The formula above follows from those two questions; it matches the Fabrico example (2,400 min per week, 8 products at 60 min, 1,920 min run time: EPEI one week).

## Choosing the interval

- Not below the minimum EPEI; that would use every spare minute and leave nothing for breakdowns or scrap.
- About 10% of available time for changeovers is a typical target (LEI); treat it as a rule of thumb and set your own by local policy.
- Round to an interval the schedule can use: a shift, a day, a week.

## Capacity or smaller lots

| Situation | Use the saving for | Why |
|---|---|---|
| Overtime, backlog, late deliveries, lost sales, or the machine is the bottleneck | Capacity: keep lot sizes, run more | Extra minutes on the constraint are extra output |
| Spare capacity, deliveries on time, high stock | Smaller lots: shorter interval | Extra minutes on a non-constraint are only idle time; smaller lots cut stock and lead time |
| Both apply | First demand plus buffer, then smaller lots | Protect delivery, then flow |

Either way, change the lot sizes or the schedule, or the saving disappears as idle time.

## Worked example

Invented round numbers. A = 2,400 min per week. Four products, each 500 pieces per week at 1 min, so R = 2,000 min and A − R = 400 min.

- Before: changeover 50 min each, C = 200 min. Minimum EPEI = 200 / 400 = 0.5 week. Lot size = 500 × 0.5 = 250 pieces.
- After SMED: changeover 20 min each, C = 80 min. Minimum EPEI = 80 / 400 = 0.2 week, one day in a 5-day week.
- Smaller lots with the 10% rule of thumb: allowance = 0.10 × 2,400 = 240 min per week; 240 / 80 = 3 cycles per week; interval 1/3 week; lot size = 500 / 3 ≈ 167 pieces, a third less than 250.
- Capacity instead: keep 2 cycles per week (lots of 250). Changeover time falls from 2 × 200 = 400 to 2 × 80 = 160 min per week. Freed: 240 min, about 240 extra pieces at 1 min, useful only if they can be sold.

## Sources

- LEI: [Every product every interval, lexicon](https://www.lean.org/lexicon-terms/every-product-every-interval/)
- LEI: [EPEI article with the two-question method](https://www.lean.org/common/display/?o=792)
- Fabrico: [Every part every interval guide](https://www.fabrico.io/blog/every-part-every-interval-epei-guide/)
- Wikipedia: [Single-minute exchange of die](https://en.wikipedia.org/wiki/Single-minute_exchange_of_die)
