---
description: Builds occurrence, detection and system 5-Why chains with an evidence check on every link.
tags: [skill, solve-5why]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
Please build the 5-Why analysis for this one. I need it for the problem-solving board on Friday.

Problem: on Tuesday's night shift, 38 of 1,200 plastic housings had their brass threaded inserts standing proud by 0.3 to 0.5 mm. Final assembly (station 60) found them because the cover screws would not seat. Day shift and the other two press lines had no proud inserts that week.

Process: station 20 presses the inserts with a pneumatic press that stops on a mechanical hard stop. Station 40 checks insert height on every part with a go/no-go depth gauge; the required height is flush ±0.2 mm.

What we have checked so far:
- Maintenance found the set screw of the hard stop loose on Wednesday morning, moved about 0.4 mm. Trial: with the stop deliberately set 0.4 mm short, 10 of 10 parts were proud; after resetting and tightening it, 50 of 50 parts were in tolerance.
- The fixture drawing shows no lock nut or thread locker on that set screw, and the hard stop is not on the preventive maintenance plan.
- At station 40, the gauge was swapped on Monday. The gauge fitted is the one for another housing variant, set to ±0.6 mm. Five known proud parts all passed that gauge; the correct gauge rejected all five.
- The two gauges look identical and carry no variant marking. The setup checklist does not ask for a master-part check after a gauge change.
- The PFMEA lists "insert too shallow" with the station 40 gauge as detection, but does not list a moving hard stop as a cause.
- The setter thinks the new batch of inserts from the supplier may be slightly oversized. Nobody has measured them yet.
