---
description: Chooses a pull system per part group, sizes the kanban loops with a cited formula and sets the pitch.
tags: [skill, improve-kanban-pull]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
We assemble electric drive units and want to replace the push schedule in front of final assembly with pull. Final assembly works 2 shifts of 7.5 hours, so 15 working hours a day, and builds 600 drive units a day. Each finished unit goes into a shipping crate that holds 10 units.

Two upstream areas feed assembly:

1. A machining cell makes the shafts. There are two shaft types, each drive unit uses one shaft. Shaft S1: 480 a day. Shaft S2: 120 a day. Daily usage of both stays within about ±5% of the monthly plan. Shafts move in bins of 20.
   - When assembly empties a bin, its card waits on average 1 hour at the kanban post before it is picked up.
   - At the machining cell the card then queues on average 4 hours (waiting for the change-over slot).
   - Machining and washing one bin take 2 hours; transport to the assembly line takes 30 minutes.
   - Our plant policy is a safety factor of 10% on all kanban loops.
2. A welding cell makes the motor housings, which go through the paint line and then to assembly. There are about 60 housing variants with customer-specific flanges; most variants are ordered 0 to 3 times a week, and the pattern changes every week. Housings are built to customer order today.

Tell us which pull system to use for the shafts and for the housings, how many kanban cards each shaft loop needs, and what the pitch at final assembly is.
