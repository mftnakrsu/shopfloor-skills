---
description: Runs the Check and Act of one PDCA cycle on an A3, compares the result with the prediction and target, and plans the next cycle.
tags: [skill, solve-pdca]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
I own the A3 on leak-test failures for the gearbox cover line and the first trial is finished. Please write up the A3 with the check of the trial and tell me what we do next. My manager reviews it on Thursday.

Background: leak-test failures go to rework, which costs us about one operator per shift.

Current condition: over the last 4 weeks, both shifts, 5,000 covers built, 160 failed the leak test (3.2%). Counted from the leak-tester log.

Current standard: the work instruction for hand sealing; the last layered audit found it followed on both shifts.

Goal: 1.0% or less by the end of March, set by the plant manager. My manager and I agreed the trial passes at 1.0% or less.

Analysis: the hand-applied sealant bead breaks where the operator lifts the gun at the corners. We proved it: 30 covers with a deliberately broken bead at a corner all failed; 30 with a continuous bead all passed.

Countermeasure tested: a guide template that the gun nozzle runs along, so the bead stays continuous around the corners. Our prediction before the trial was that failures would drop below 1.0%.

Trial: 2 weeks on line A, both shifts, same leak tester and the same counting method. 2,000 covers built, 26 failed. Of the 26, 18 had the bead break at corner 3 next to the bolt boss, where the template does not reach. The other 8 were spread around the cover with no pattern. Cycle time went from 52 to 56 seconds per cover; the takt time is 60 seconds. Sealant use per cover did not change.
