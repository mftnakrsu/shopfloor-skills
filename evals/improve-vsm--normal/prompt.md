---
description: Builds the current-state ladder, answers the future-state questions in order and ends in a loop plan with a 30/60/90 review.
tags: [skill, improve-vsm]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---
I want a value stream map (Wertstromanalyse) for our mounting-bracket family, door to door, and then a future state and an implementation plan.

Customer: 600 brackets a day, packed 20 to a box, one truck a day. We work 2 shifts of 8 hours with 30 minutes of planned breaks per shift.

Processes in order (one piece = one bracket). The family is one part number at every process; assembly only changes the label for three customers, with no changeover.
- Laser cutting: C/T 30 s, C/O 15 min, uptime 95%, dedicated to this family.
- Press-brake bending: C/T 45 s, C/O 30 min, uptime 90%.
- Robot welding: C/T 100 s, C/O 10 min, uptime 85%, one cell.
- Assembly and pack: 1 operator, C/T 60 s, no changeover, 98% complete and accurate.

Inventory counted this morning: sheet stock enough for 3,000 brackets before cutting; 1,800 cut blanks before bending; 1,200 bent parts before welding; 900 welded parts before assembly; 2,400 finished brackets in the shipping area.

Information flow: the customer sends a 30-day forecast monthly and firm orders daily. Our ERP plans weekly and prints a separate weekly schedule for each of the four processes. The supervisor walks the floor every day to expedite late orders.
