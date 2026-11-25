---
description: The pfmea-chain-checker agent checks the chain station by station, asks for missing documents and reports without editing.
tags: [agent, pfmea-chain-checker]
timeout_seconds: 600
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---
Use the pfmea-chain-checker agent. We are about to release the documents for a bracket line with four stations: OP10 cutting, OP20 welding of a nut, OP30 leak test, OP40 packing. The PFMEA lists "nut missing" at OP20 with severity 9, and "burr on edge" at OP10 with severity 4. Our control plan has a row for the nut check at OP20 with a reaction of "inform supervisor". I do not have the station instructions at hand today. Please check that the chain is complete.
