# Coding guide

Read this before Phase 2. Contents:

1. Granularity — how big is a coding unit
2. Code naming conventions
3. Semantic and latent coding
4. The why → how → decision interrogation, with worked examples
5. Handling the awkward material
6. Codebook format
7. Recoding and code-vocabulary drift

---

## 1. Granularity

"Line by line" means *nothing goes unread and unconsidered*, not that every orthographic line
gets its own code. The coding unit is the smallest stretch of talk that carries a complete
idea — sometimes a clause, usually a sentence or two, occasionally a whole turn when the
participant is building one extended argument.

Practical rules:

- Code the participant's talk. Code the interviewer's turns only when they shape what follows
  (a leading question, an interruption, a reframing) — then note it as an interactional artifact
  rather than as participant meaning.
- Overlapping and nested codes are fine. A single extract routinely carries a descriptive code
  and an interpretive one.
- Backchannels, false starts, and repairs are codeable when they mark difficulty ("I mean —
  well, not exactly, it's more that…" is hesitation doing analytic work).
- If a stretch of talk genuinely carries nothing relevant to the research question, mark it
  `[no code — off-topic]` rather than silently skipping it. The gap should be visible in the
  audit trail.

## 2. Code naming

Good codes are short verb-ish phrases that capture an action, orientation, or condition rather
than a noun-topic.

| Weak (topic label) | Stronger (analytic) |
|---|---|
| Trust | Extending provisional trust to reduce cognitive load |
| Privacy | Trading disclosure for convenience, then regretting it |
| Frustration | Blaming self for system failure |
| Notifications | Pre-emptively muting to protect attention |
| Onboarding | Learning by breaking things deliberately |

Mark in-vivo codes with quotes: `"it just does its thing"` — reserve these for participant
phrases that are doing conceptual work you could not phrase better yourself.

Keep code names under about ten words. If a code needs a paragraph to be intelligible, it is
probably a candidate theme in disguise; note it and move on.

## 3. Semantic and latent

- **Semantic**: what the participant explicitly said. `Reports switching off location sharing
  after a false alert.`
- **Latent**: what underlies or organizes it. `Positions the system as an unreliable witness to
  her own routine.`

Tag every code as one or the other. A dataset coded almost entirely at the semantic level
produces topic summaries at Phase 3, and you will feel it — if the codebook is drifting that
way, go back and add the latent layer before proceeding.

## 4. The why → how → decision interrogation

Apply this to any code that recurs, that surprises you, or that you feel tempted to leave as a
bare label. Write the result in the analytic-note column. Keep each to two or three sentences.

**Worked example 1**

> P4: "I always check the log afterwards. Not because I don't trust it exactly, it's just… I
> like to see it did what it said."

- Codes: `Post-hoc verification of automated action` (semantic); `Disavowing distrust while
  enacting it` (latent).
- **Why**: The denial ("not because I don't trust it") does more work than the assertion. P4 is
  managing a social identity — the competent user who is neither paranoid nor naive — while
  describing a routine that is straightforwardly a distrust practice.
- **How**: Verification is possible only because the system produces an inspectable log; the
  disavowal is possible only because "checking" is culturally readable as diligence rather than
  suspicion. The mechanism is that legibility affordances let users perform oversight without
  having to claim distrust.
- **Decision**: Promote `Disavowing distrust while enacting it` to a candidate cluster with
  `Blaming self for system failure` and `Explaining away anomalies`; search corpus for other
  disavowal constructions ("it's not that…", "I'm not one of those people who…").

**Worked example 2**

> P9: "Everyone at work uses it, so."

- Code: `Adoption as social non-decision` (latent).
- **Why**: The sentence ends on "so" — the reason is treated as too obvious to complete. The
  participant does not present adoption as a choice at all, which quietly contradicts the
  study's framing of use as individual decision-making.
- **How**: Works through the cost of non-use rather than the benefit of use; the mechanism is
  coordination lock-in, and it should appear elsewhere as complaints about being unreachable,
  or about colleagues assuming visibility.
- **Decision**: Hold as context for now — it may be a boundary condition on a theme about
  agency rather than a theme in itself. Revisit at Phase 4 Level 2.

**Worked example 3 — a decision to discard**

- Code: `Mentions cost` appears in six transcripts.
- **Why**: In each case it is a one-line answer to a direct interviewer question about price.
  It is elicited, not volunteered.
- **How**: No mechanism visible; participants do not connect cost to anything else in their
  accounts.
- **Decision**: Retain in codebook, exclude from theme development, and say so in the
  theme-development log. Frequency without conceptual traction is not a theme. This is exactly
  the case that a counting approach would over-promote.

## 5. Handling the awkward material

- **Contradiction within a transcript**: code both positions, then code the contradiction
  itself. Inconsistency is usually the most analytically productive material in the corpus.
- **The eloquent participant**: guard against letting one articulate speaker supply the
  analysis. Check at Phase 4 whether a theme rests disproportionately on them.
- **Silence and refusal**: "I'd rather not say" is codeable.
- **Interviewer contamination**: where the participant is clearly echoing the interviewer's
  vocabulary, code it as such and discount it in theme development.
- **Distress or sensitive disclosure**: handle in the report with care; consider whether the
  extract is necessary to the argument or whether paraphrase suffices. Note the choice in the
  reflexivity statement.

## 6. Codebook format

| Code | Definition | Include | Exclude | Extracts (n) | Anchor extract | Type |
|---|---|---|---|---|---|---|

The `n` column is bookkeeping only. Add a standing note under the table: *counts indicate
coding coverage, not analytic importance.*

Group the codebook by working cluster once clusters appear; keep orphan codes in a final
"unclustered" block rather than deleting them — they are where the next reading often starts.

## 7. Recoding and drift

Your coding vocabulary at transcript 8 is not the vocabulary you had at transcript 1. Return to
the early transcripts once, recode with the developed vocabulary, and record the pass in the
audit trail with a line on what changed. This single step is what separates a coded dataset from
a coded first transcript plus seven skimmed ones.
