# Three legs

Where each leg starts, what to ask along it, and the typical roots it ends at. Sources name the legs differently (specific, occurrence or process; detection or escape; systemic or management); the questions are the same.

## Occurrence leg: why was it made?

Start at the problem statement. The first answer is the physical condition at the part or the station that produced the defect.

Questions along the chain:

1. Was the correct process, programme, parameter and sequence used?
2. Was the standard work followed, and does it exist for this variant?
3. Were the correct material, part and tool used, in good condition?
4. Is the tool change and maintenance plan followed for this equipment?
5. Has anything changed: material lot, supplier, tool, setting, fixture, person, shift, variant, layout?
6. Is the failure mode in the PFMEA, and do its causes match what was found?

Typical roots: tool wear or breakage, wrong or drifting set-up, processing parameters out of range, fixture or locating faults, handling and storage damage, a missing or unclear step in standard work, a change that created a new failure mode.

## Detection leg: why was it not caught?

1. List every control after the cause in flow order: self-check, sensor or error-proofing device, in-process gauge, final test, audit.
2. Find the escape point: the first control that should have caught the problem.
3. If no control could detect it, the first answer is that absence. Then ask why none was planned (this leads into the system leg).
4. If a control existed, ask how it failed:
   - device not working, bypassed or disabled after a fault;
   - gauge or master not calibrated or worn, or a detection setting or logic changed;
   - measurement system not able to see this defect;
   - sample size or frequency too low for how the cause behaves;
   - check criteria not in the instruction, or checking a label instead of the part;
   - the control not re-verified after a change or repair.
5. Prove the failure with known bad parts or a challenge part: with the condition present, the control misses it; with the condition removed, it catches it.

Typical roots: error-proofing not effective or bypassed, no quality gate, measurement system issues, a detection setting or logic changed, check frequency not linked to the risk.

## System leg: why did the system allow it?

The first whys are the roots of the occurrence leg and, where a control existed and failed, the root of the detection leg (Nexteer supplier training). Ask for each:

1. Was the failure mode and this cause in the PFMEA? If yes, were the occurrence and detection risks rated realistically?
2. Was the product and process planning process followed for this station, and was this change assessed before release?
3. Does the control plan set a check, a frequency and a reaction for this cause?
4. Is the equipment's condition covered by the maintenance plan?
5. Is the design robust against this cause, or does it rely on a person getting it right?
6. Does change management require a risk check and a verification before a changed process restarts?
7. Are lessons from similar parts, lines or past problems fed back into these documents?

Typical roots: failure mode or cause missing from the PFMEA; risk rated too low because it had never happened; a process change not assessed; no effective preventive maintenance; change rules without a verification step; lessons learned not transferred.

The roots of this leg usually sit with support functions (engineering, quality, maintenance, planning, management), so name the function that owns the action.

## Branches

When an answer has two contributing causes, record both and follow each in its own branch to its own root and action (University of Arizona QA guide). A branch is not a sign of a bad analysis. A branch whose first link is rejected is closed with the evidence that rejected it.

## Sources

- Nexteer Automotive: [3-legged 5 Why supplier training, 2018](https://www.nexteer.com/wp-content/uploads/5-Why-Training-Nexteer-Supplier-Version-17-Sept-18.pdf)
- Keysight: [Root cause and corrective action guideline for suppliers](https://about.keysight.com/en/supplier/KeysightRCCA_Guideline.pdf)
- Gangidi, P.: [A systematic approach to root cause analysis using 3 × 5 why's technique, International Journal of Lean Six Sigma 10(1), 2019](https://www.emerald.com/insight/content/doi/10.1108/IJLSS-10-2017-0114/full/html)
- University of Arizona, Office of Research and Partnerships: [5 Whys root cause analysis guide](https://research.arizona.edu/sites/default/files/2026-07/5-Whys-Procedure.pdf)
