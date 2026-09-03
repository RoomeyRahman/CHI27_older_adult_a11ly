# Theme construction: the five passes

Read before Phase 2. Governs how codes become sub-themes and sub-themes become themes, in every unit: each of
each transcript in a study, then that study's master synthesis, then the cross-study affiliation synthesis.

**The rule: candidate codes, then a trim, then sub-themes, then themes, then review, in that order, each written
to disk before the next begins. All five run in one invocation; an exit check is a checkpoint you report and
cross, never a place to stop and ask.**

---

## 1. Why one sweep fails

Abstraction performed in the same sweep as coding produces sub-themes that no code supports and theme names
chosen before the evidence was read, and a fabricated sub-theme is indistinguishable in the output from a derived
one. Three specific failures:

- **Anticipation contaminates the codes.** If you already know the theme, the code becomes a step toward it
  rather than a description of the extract.
- **Quotes drift.** Extracts recalled while writing a theme are extracts recalled, not extracts read.
- **Selection hides inside description.** When coding and filtering happen together, the codes that were never
  written are invisible, and so is the judgment that suppressed them. Splitting exhaustive coding from an argued
  trim turns that judgment into something a reader can disagree with.

## 2. The passes

### Pass A, candidate codes, exhaustive

**Input:** the transcript (or, at master level, the eight per-transcript registers and matrices).

**Deliberately over-inclusive.** Nothing is filtered for importance. If you catch yourself skipping a passage
because it will not survive, code it and let Pass B kill it on the record.

**Volume.** Roughly **40 to 80 candidate codes per interview transcript**, scaling with length. At master level,
pooling the eight retained sets gives **200 to 240 entries** before reconciliation. Calibration figures, not
quotas: far fewer means stretches went uncoded or the coding unit was too coarse.

**Output:** `02-coding-table.md` for a transcript unit; `master/01-code-synthesis.md` for the master unit, both
inside your agent slot (SKILL.md Section 0.0). Codes
are two to five words, definitions carry the nuance, extracts are participant-only and verbatim, and evidence
tags travel with the code: `[elicited]`, `[demonstration-grounded]`, `[in-vivo]`, `[tr]`.

**Must not:** name a sub-theme or theme anywhere, including in an analytic note; drop, merge, or rank codes for
importance; quote the interviewer; write a code longer than six words.

**Exit check:** the table is on disk; every code has a definition boundary, at least one attributed verbatim
participant extract, and a short name; the candidate count is recorded; no sub-theme or theme name appears.

### Pass B, the trim

**Output:** `03-code-register.md` (transcript units) or the retained-set section of `master/01-code-synthesis.md`,
holding **every** candidate marked `RETAINED` or `PARKED` with a reason. **Nothing is deleted.** The parked block
is where a later loop goes looking when a theme turns out thin.

**Targets: 25 to 30 retained per transcript; at most 40 at master level.** Those numbers are what the theme
counts below can carry. If the honest number is 23 or 33, take it and say why; do not pad or amputate.

1. **Reconcile before judging.** Merge synonyms, collapse near-duplicates that share a mechanism, split codes
   doing two jobs even though that raises the count. Most reduction happens here. Record the count after this
   step. At master level this is merging across transcripts: the same code under different names in OA02 and
   CG06 is one master code, and both original names are kept.
2. **Score each survivor** on five criteria, one word each in the register, a clause where contested:
   - **RQ traction** against the three RQs in `/output/Introduction.md`.
   - **Mechanism**: does it name something that happens, a condition, an action, a relation, rather than a topic
     that came up?
   - **Corroboration**: within a transcript, where else it appears; at master level, how many participants carry
     it, plus any `/supplementary/` artifact.
   - **Evidence grade**: volunteered, `[elicited]`, or `[demonstration-grounded]`.
   - **Conceptual load**: what the analysis specifically loses without it. This is the criterion that saves the
     rare load-bearing code with thin corroboration, and it must be argued in writing.
3. **Retain and park.** Park, in order of confidence: instrument codes that only ever answer a direct question;
   topic labels with no mechanism; elicited-only codes with no unprompted appearance; the redundant, naming which
   code absorbs them; the off-question. **Retain every code that cuts against the direction the analysis is
   heading**, even thin ones. Trimming is where an inconvenient case would quietly disappear, and the tensions in
   CLAUDE.md Section 9.3 are protected here specifically. At master level, check participant balance: if the
   retained set comes mostly from two articulate participants, the trim followed fluency rather than
   significance. For Study 1, check the balance between older adults and caregivers as well: a retained set drawn
   mostly from caregivers is an analysis of how the work is accounted for, not of how it is done.
4. **Write the trim rationale** at the head of the file: counts at each step, which criteria did most of the
   parking, the two or three hardest calls with both sides stated.

**Must not:** park without a reason; delete a code from the register; **trim by frequency**, since a code that
recurs but names no mechanism and answers no RQ is exactly what this pass exists to park; name a sub-theme or
theme; add a code that was not in Pass A; edit a definition to make a code survive.

**Exit check:** the register accounts for every candidate; the retained set is within target or justified outside
it; every retained code carries its five criterion answers; merges and splits are recorded with old names kept;
no sub-theme or theme name appears.

### Pass C, sub-themes and reflexivity notes

**Group only the retained codes.** A parked code is not clustered and not quietly reintroduced; if one is needed,
unpark it in the register with a reason and log it. Read the register and the codes before rereading any
transcript; return to a transcript only to check a specific extract when a decision turns on it.

Per sub-theme, in this order:

1. **Constituent codes** by exact name. Written first, because they are the evidence. A code not in the retained
   set cannot be in a sub-theme.
2. **Name**, descriptive and analytic, per SKILL.md Section 8.
3. **One-line definition**, derived from the constituent list, not from memory of the interviews.
4. **What it excludes**, and which codes you considered and did not include.
5. **The RQ it speaks to.**

**Reflexivity notes are written in this pass**, per code, while the grouping decision is being made, because
their content is the decision and the alternative not taken. A note written after the theme is settled records a
rationalization.

**Targets: 4 to 8 sub-themes per transcript; 6 to 12 at master level.**

**Must not:** name a theme; cluster a parked code; create an empty sub-theme, or a single-code sub-theme without
a written defence; add a new code; alter a quote, since the extract set is fixed at Pass A.

**Exit check:** every sub-theme lists constituent codes matching retained codes exactly; every retained code sits
in exactly one sub-theme or was reparked on the record; every retained row has a reflexivity note naming a
decision; no theme name appears; the sub-theme count is within target.

### Pass D, themes and reflexivity validation

**Group sub-themes, never codes directly.**

1. State the **central organizing concept in one sentence, before naming the theme**. If you cannot state it
   without listing the sub-themes, there is no theme yet, only a bin.
2. Name the theme from that sentence, descriptively (SKILL.md Section 8).
3. **List the constituent sub-themes by exact name.** The chain theme to sub-theme to code to extract must be
   walkable in both directions.
4. Then write the definition, the boundary and variation, and select extracts from those already in the matrix.

Run the two-level review as you go: Level 1, do the extracts under each theme cohere when read as a set, ignoring
which transcript they came from; Level 2, does the structure represent the whole unit, or has a compelling
minority account been over-weighted. Every split, merge, promotion, demotion, or discard gets a log row in the
unit's themes file: what changed, why, and what evidence was consulted.

**Then validate every reflexivity note** against the theme its code ended up in. A note saying "I promoted this
over X" when the code was later demoted is now false, and a false audit trail is worse than a thin one. Keep the
original claim and append the correction, so the trail shows the movement.

**Targets: 2 to 4 themes per transcript; 3 to 5 at master level.**

**Must not:** build a theme from codes directly; introduce a sub-theme that did not exist at the end of Pass C
unless by a logged split; introduce a code that is not in the retained set; alter a quote.

**Exit check:** every theme has a one-sentence organizing concept and a constituent sub-theme list; every
sub-theme sits in exactly one theme; theme count is within target; every reflexivity note is validated or
corrected; at master level, every theme clears the two-source rule or carries `[single-instance]` and maps to
RQ1, RQ2, or RQ3.

### Pass E, review

Writes no new analysis. Tries to break what exists. For a transcript unit this is short, appended to
`04-themes.md`; at master level it is the whole of `master/04-review.md`.

1. **Walk the chain downward.** Theme to sub-themes to codes to extracts. A link that will not walk is a defect:
   demote or rebuild, do not patch with a sentence.
2. **Walk it upward.** Sample five extracts at random in a transcript unit, fifteen to twenty across transcripts
   at master level. For each, does its code still fit, is its sub-theme where a reader would put it, is the theme
   a claim it supports? Record the sample and the hit rate. A master-level miss rate above roughly one in five
   means Pass C is redone, not tidied.
3. **Verify mechanically.** `quote_check.py` and, once the final files exist, `table_check.py`, both scoped to
   your slot.
4. **Attack each theme** with its strongest counter-reading; either say why it loses or concede it. Name the two
   or three extracts that fit worst and say what was done with them.
5. **Audit the trim.** Reread the parked block with the finished themes in hand and name the parked codes closest
   to the line. Either unpark one and rebuild, or say why the parking holds. A trim nobody rechecks after the
   themes exist is a filter applied before the evidence was understood.
6. **At master level only:** check instrument capture (do the themes reproduce the four interview modules or the
   three RQs?), participant concentration per theme (more than about a third from one participant gets flagged),
   and evidence grades per theme (an all-elicited or all-demonstration-grounded theme is a theme about the
   instrument). Then run the quality checklist and the anonymization scan.

If Pass E forces no change at all, say whether you believe the analysis is that clean or the pass was not
adversarial enough.

## 3. Unit state, recorded in every file

Every file opens with:

```
<!-- slot: A1 | unit: study1/OA03 | pass: A complete | B complete | C pending -->
```

Update as each pass finishes. Never write a downstream column while its upstream pass is pending. On a resumed
run, read these lines first and restart from the earliest incomplete unit and pass.

## 4. Loops are allowed, silence is not

Pass B routinely reveals that a code was named wrong or was two codes; Pass C, that a retained code does not
cluster and should have been parked; Pass D, that a sub-theme was two; Pass E, that a parked code was needed.
Going back is correct practice.

Every backward loop gets a log row naming the pass it started in, the pass it returned to, what changed, and why.
When a loop invalidates downstream work, reset those columns to pending and rebuild them rather than editing in
place around the change. A theme resting on a code that was quietly redefined underneath it is not detectable
later.

## 5. Units and scope

The units run in order: each transcript of a study in full, then that study's master synthesis over their
results, then the next study, then the cross-study affiliation synthesis over the study masters. A scoped run on
one participant runs all five passes for that transcript only, then stops, marks the master and final files
stale, and says what needs rerunning. A master synthesis cannot be simulated from one transcript, studies are
never merged into one pooled corpus, and the Study 3 non-interview streams are never folded into its interview
synthesis.
