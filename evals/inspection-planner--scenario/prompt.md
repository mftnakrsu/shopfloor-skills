---
description: The inspection-planner agent asks for the missing inputs and stops at its gate before deriving station documents.
tags: [agent, inspection-planner]
timeout_seconds: 600
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---
Use the inspection-planner agent. We are launching a stamped bracket on line 4 for a new customer. Operations are 10 stamping, 20 weld nut welding, 30 final inspection. I need the control plan and the station instructions for operation 20. The weld nut presence is the critical point. I have the drawing, but no PFMEA yet. Start now.
