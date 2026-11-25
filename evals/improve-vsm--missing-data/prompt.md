---
description: Asks for the customer demand instead of inventing takt and inventory days.
tags: [skill, improve-vsm]
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill]
---
Please draw the current-state and future-state value stream map for our pump-housing family and tell me our production lead time.

We run one shift of 8 hours with 40 minutes of breaks. Processes: casting cleaning (C/T 55 s), CNC machining (C/T 140 s, C/O 45 min, two machines), leak test (C/T 35 s), painting (batches of 48), packing (C/T 25 s). Inventory: 2,200 raw castings, 950 cleaned, 640 machined, 300 tested, 1,100 finished housings. Production control sends a daily MRP list to every process.
