---
description: Catches a kanban loop sized with the processing time instead of the full replenishment lead time.
tags: [skill, improve-kanban-pull]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---
Our paint line refills a supermarket of painted covers for the packing line. Packing uses 40 covers an hour, and a bin holds 25 covers. We sized the loop with the Toyota formula: painting one bin takes 30 minutes, so cards = 40 × 0.5 h × 1.1 ÷ 25 = 0.88, rounded up to 1, and we run 2 cards to be safe.

The supermarket keeps running empty. Here is what happens to a card: it waits on average 1 hour at the post before pickup, then the order waits about 5 hours in the paint line's order queue, painting takes 30 minutes, curing 1.5 hours, and the forklift run back takes 30 minutes. The paint line paints only these covers, and it can paint 50 an hour including all stops.

Please confirm the 2 cards and tell us whether the empty supermarket means we need a second paint booth.
