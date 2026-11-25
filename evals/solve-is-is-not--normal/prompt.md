---
description: Builds an Is/Is-Not specification, links distinctions to dated changes and eliminates possible causes that do not explain the facts.
tags: [skill, solve-is-is-not]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
We have a leak problem on our die-cast aluminium gearbox covers and nobody agrees on the cause. Can you run an Is/Is-Not on it and tell us which cause to chase first?

Facts we have:
- The covers fail the helium leak test after machining. Sectioned rejects show porosity at the oil-gallery boss. No leaks at the flange or at the other bosses.
- All rejects come from die-casting cell 3 (die 3B). Cells 1 and 2 cast the same cover with dies 1A and 2A and their leak rate is unchanged at about 0.2%.
- First leak on cell 3 parts: 3 March, early shift. Since then cell 3 rejects on every shift, steady, not growing. Before 3 March cell 3 was also at about 0.2%.
- Since 3 March: 46 of 900 covers from cell 3 failed.

Changes we know of:
- 20 February: new aluminium ingot supplier, used on all three cells.
- 1 March: the leak tester was recalibrated. All cells' covers go through the same tester.
- 2 March: die 3B came back from repair. The vacuum valve was replaced with a different type.
- 10 March: a new operator started on cell 3 night shift.

The team's candidate causes: gas in the new ingots, the tester recalibration, the new operator, and the die 3B vacuum valve.
