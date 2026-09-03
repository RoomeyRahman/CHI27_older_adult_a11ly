# Coding guide

Read this before Phase 2. Contents:

**Standing frame for this phase: Pass A is exhaustive, not selective.** Code everything relevant and let the
Pass B trim decide what carries the analysis (`theme-construction.md`, Pass B). Expect roughly 40 to 80 candidate
codes per interview transcript here. Do not skip a passage because it looks unlikely to survive, and do not merge
two codes because you suspect they will end up together; both judgments belong to a later pass, made on the
record.


1. Granularity, how big is a coding unit
2. Coding a question-and-answer pair, and why the interviewer is never quoted
3. Code naming conventions, and the brevity rule
4. Semantic and latent coding
5. The why to how to decision interrogation, with worked examples from this corpus
6. Handling the awkward material in these transcripts
7. Codebook format
8. Recoding and code-vocabulary drift

---

## 1. Granularity

"Line by line" means *nothing goes unread and unconsidered*, not that every orthographic line gets its own code.
The coding unit is the smallest stretch of talk that carries a complete idea: sometimes a clause, usually a
sentence or two, occasionally a whole turn when the participant is building one extended argument. In this corpus
turns are often long, because participants were asked open questions and given room; a single turn can carry
three distinct positions and should carry three codes.

Practical rules:

- **The coding unit is the question-and-answer pair, not the answer alone.** Read the interviewer's turn to
  establish what the participant's turn is about, then code the participant's position. This matters constantly
  in this corpus, because many answers are elliptical: "Yes", "No, not that one", "Only sometimes". An answer
  coded without its question is uninterpretable, and an answer coded *as* its question is the interviewer's
  meaning wearing the participant's turn. See Section 2a for how to do this without letting the question become
  the finding.
- **Never quote the interviewer.** The interviewer's words supply context for the code and can be paraphrased in
  the analytic note or the code definition. They never appear as an extract, never in the matrix, and never in
  the report.
- Overlapping and nested codes are fine. A single extract routinely carries a descriptive code and an
  interpretive one.
- Backchannels, false starts, and repairs are codeable when they mark difficulty.
- If a stretch of talk genuinely carries nothing relevant to the three research questions, mark it
  `[no code, off-topic]` rather than silently skipping it. The gap should be visible in the audit trail.
- **Code the third party.** When a participant describes what a son, a daughter, or a pharmacist did, that is
  network data and it gets its own code. The analytic note names whose account it is, because we have the older
  adult's version of the son's action and not the son's, except in Study 3 where both may exist.
- **Silence and non-use are moves, not gaps.** An ignored reminder, a declined offer of help, or a refusal to
  answer is coded as participation, never marked as missing data. See SKILL.md Section 0.6.

## 2. Coding a question-and-answer pair

Elliptical answers carry real content, and that content lives partly in the question. The rule is to recover the
content, credit it to the participant, and keep the interviewer out of the evidence.

**Worked example.** The interviewer asks whether the participant uses a captioning tool and whether they then
correct the captions by hand. The participant answers: "Yes, but not the second part."

- Wrong: quoting the interviewer's question as the extract, or writing a code like `Asked about caption
  correction`. That codes the instrument.
- Wrong: coding only `Says yes`. That records the turn and loses the content.
- Right: two codes, `Daughter sets the schedule` and `Takes doses unprompted`, with the answer as the extract:
  `"Yes, but not the second part." (D6, 12:40)`, and an analytic note recording that the content of "the second
  part" is recovered from the preceding question, paraphrased.

Three rules follow:

1. **Recover, then attribute to the participant.** The code states the participant's position in plain terms, as
   if they had said it in full. The recovery itself, what the question supplied, goes in the analytic note, in
   one clause.
2. **Quote only the participant.** Where the bare answer is unreadable alone, add the recovered content as a
   bracketed insertion inside the participant's quote: `"Yes[, I use auto-captions], but not the second part."`
   Square brackets mark it as the analyst's insertion, which is exactly what it is. Never build a two-speaker
   dialogue block as an extract.
3. **Grade the evidence.** A position recovered from a closed or leading question is `[elicited]` and carries
   less weight than the same position volunteered. Tag it, and check whether it appears unprompted elsewhere
   before it supports a sub-theme.

The boundary case is the interviewer turn that does more than ask: an explanation of the study's premise, a
reframing, a suggestion of what the participant might mean. Code that as an interactional artifact, name it in
the analytic note, and discount whatever follows it. Do not quote it there either; describe it.

## 3. Code naming

**Codes are short. Two to five words, six at the outside.** A code is a handle, not a sentence: it is what you
say to yourself when you find the same thing again in transcript six, and it has to be short enough to scan a
hundred of them in one column. The nuance belongs in the definition, the reasoning belongs in the analytic note,
and the interpretation belongs in the sub-theme. A code carrying all three is doing three jobs badly.

Diagnostic: if the code will not fit comfortably in a narrow table column, or if it contains "because", "rather
than", "while", or a clause after a comma, it is a definition that has been pasted into the name field. Cut it
back and move the remainder down.

Good codes are gerund-led where an action is going on, and noun-plus-qualifier where a condition is:

The rows below are shape examples; the wording is illustrative and none of it is a real finding.

| Too vague (topic) | Too long (definition in the name) | Code |
|---|---|---|
| Family | Consulting one named child about difficulties as a standing arrangement | `Standing right to consult` |
| Memory | Asserting unaided recall when an external aid is offered | `Memory as competence claim` |
| Reminders | Waking to the internal cue slightly before the notification fires | `Anticipates the reminder` |
| Trust | Setting a test timer to check the app fires before relying on it | `Verifies before relying` |
| Gamification | Describing the loss of an accumulated streak as a personal loss | `Streak break as loss` |
| Monitoring | Reading a daughter's comment on the score as attention rather than checking | `Score as contact` |
| Escalation | Naming which family member the agent should tell, over others present | `Routes alert to one child` |
| Prescriptions | Taking an unclear prescription to a pharmacist rather than back to the doctor | `Pharmacist as interpreter` |

Each of those short codes still needs its definition to be usable, which is the point: the definition column is
where "what counts as a framing pause" gets settled, and the codebook is where a reader goes to find out.

Keep the vocabulary consistent across transcripts. `Pharmacist as interpreter` in OA04 and `Asks the chemist` in
OA09 are one code with two names, and Pass B will treat them as two. Reuse the existing name or rename both.

Mark in-vivo codes with quotation marks, and reserve them for short participant phrases doing conceptual work you
could not phrase better yourself. The brevity rule applies to them too: `"a blessing"`, not a quoted sentence. Because most of this corpus is translated, mark a translated in-vivo code `[tr]`:
`"my memory is very sharp" [tr]`. That tag is a standing reminder that the phrasing is partly the translator's
and that the code should not be defended on its exact wording. Kinship terms are the case where this matters
most: an English "brother" may render several distinct Bangla terms carrying different seniority, so note the
uncertainty rather than reading the English word.

Terminology binds code names as it binds prose (AGENTS.md 2.5 and 7.8): *care network*, *allegiance*, *the
agent*, *dignity*, *older adult*, *caregiver*, used identically every time; "older adult", never "the elderly" as
a noun; the roles are tool, coach, and advocate; the dimensions are direction, visibility, revocability, and
ceremony; the mechanism is the Affiliation Ledger. Never call the system "generative AI", and never write
"polyadic".

## 4. Semantic and latent

- **Semantic**: what the participant explicitly said. `Reports asking a son about every unclear prescription.`
- **Latent**: what underlies or organizes it. `Treats consultation as a position the son holds rather than help
  the older adult requests.`

Tag every code as one or the other. A dataset coded almost entirely at the semantic level produces topic
summaries at Phase 3, and you will feel it. If the codebook is drifting that way, go back and add the latent
layer before proceeding.

## 5. The why to how to decision interrogation

Apply this to any code that recurs, that surprises you, or that you feel tempted to leave as a bare label. Write
the result in the analytic-note column. Two or three sentences each.

**Worked example 1, the reconstructive shape**

The examples in this section are shape illustrations. The extracts are invented to show the reasoning; never
carry one into an artifact.

> OA04: "I discuss with [my eldest son] during any difficulties." (OA04)

- Codes: `Standing right to consult` (semantic); `Consultation as position, not help` (latent).
- **Why**: The verb is habitual and the difficulty is plural and abstract, so the arrangement precedes any
  particular problem. He is not reporting that he needed help this time; he is reporting who holds the right to
  be asked. What is being managed is the difference between a person who requires assistance and a household
  with a settled division of authority.
- **How**: This is available to him because the son's position is already established and already earned. The
  mechanism is that a standing consultative right converts an episode of not knowing into an ordinary use of the
  household's structure, which protects dignity in a way an ad hoc request would not. Look for the same mechanism
  wherever a participant names one specific family member rather than "my children".
- **Decision**: Promote to a candidate cluster with codes about who is entitled to be told; search the study for
  other habitual-tense constructions naming one member, which mark the same move.

**Worked example 2, the unweighed acceptance**

> A participant describes her daughter setting up the app, choosing the reminder times, and later commenting on
> her score, and says she was glad of it. (D6)

- Codes: `Daughter as onboarder` (semantic); `Setup handed over without qualification` (latent);
  `Score as contact` (latent).
- **Why**: The handover is described without any weighing of independence against convenience, which is what the
  monitoring-as-intrusion expectation predicts she would do. The absence of that weighing is the datum.
- **How**: The mechanism is that the setup work and the taking of the medication are separable for her. The
  daughter configured; she takes. That separation is what makes the handover cost nothing to her standing, and it
  appears here in a participant who is not making an argument about autonomy.
- **Decision**: Hold as a boundary case against any sub-theme about monitoring as intrusion, code the separation
  itself, and look for it elsewhere. Tag `[study2-scope-limited]`, because a single Study 2 account cannot carry
  an allegiance claim.

**Worked example 3, the interviewer's vocabulary**

> Interviewer explains that many older adults find it hard to remember doses, that the team is building a
> reminder, and asks what difficulties the participant has. The participant then reports forgetting when the
> routine is disrupted.

- Codes: `Forgetting under disruption` (semantic, `[elicited]`); `[interactional artifact: premise supplied by
  interviewer]`. The interviewer's turn is paraphrased in the note above and is not quoted anywhere.
- **Why**: The difficulty frame was handed to the participant a moment earlier, and it is a deficit frame. The
  specific content, disruption of routine, is hers and is not in the interviewer's turn, so the report is not
  simply an echo. But that a difficulty was reported at all is partly the question's doing, and coding this as
  evidence of memory trouble would import the interviewer's premise into the analysis.
- **How**: The mechanism to check is whether disruption-linked lapses appear unprompted elsewhere. If they do,
  this corroborates; if only after prompting, the claim is weaker and is reported as elicited.
- **Decision**: Code both layers, discount the extract's weight, record the discount. Do not discard it:
  elicited material is still evidence, at a lower grade.

**Worked example 4, a decision to discard**

- Code: `Names a phone model` appears across most transcripts.
- **Why**: In nearly every case it answers a direct question about the device. It is elicited, not volunteered,
  and participants do not connect the device to anything else in their accounts.
- **How**: No mechanism visible. The model does no analytic work; what does work is who operates the device and
  on whose behalf, which is a different code.
- **Decision**: Retain in the codebook as inventory, exclude from theme development, record the exclusion in the
  theme-development log. Frequency without conceptual traction is not a theme. This is exactly the case a counting
  approach would over-promote.

## 6. Handling the awkward material in these transcripts

- **Contradiction within a transcript**: code both positions, then code the contradiction itself. Inconsistency
  is usually the most analytically productive material in the corpus, and this corpus has a lot of it, because
  participants were asked both how they manage medication and how their family is involved, and the two answers
  frequently describe different households.
- **The stated ideal versus the actual practice**: when a participant describes a settled routine and then
  describes a dose missed at a wedding, do not code the routine as a plan and the lapse as a failure. Code the
  gap. Ask what the ideal account is for, and to whom it is addressed.
- **Contradiction across a pair**: in Study 3, an older adult and a caregiver narrating the same episode
  differently is the study's central kind of evidence. Code both accounts on their own terms, code the divergence
  as its own code, and never resolve it toward the more plausible version.
- **The articulate participant**: some speakers are notably more fluent about the household's arrangements than
  the rest, and caregivers are systematically more fluent about them than older adults, because accounting for
  the work is part of the work. Guard against letting them supply the analysis. Check at Phase 4 whether a theme
  rests disproportionately on them or on one side of the network.
- **Echoed vocabulary**: where the participant is plainly reusing a term the interviewer introduced a turn
  earlier, code it, tag it `[elicited]`, and discount it. Describe what the interviewer said in the analytic
  note; never quote it.
- **Translation seams**: where the English reads oddly literal, or where a term seems to shift meaning across a
  transcript, flag it in the analytic note rather than reading the oddity as significant word choice.
- **Hypothetical judgment**: where a participant evaluates a scenario they were asked to imagine rather than one
  they have lived, tag the code `[hypothetical]`. This is not a defect; the affiliation probes and the co-design
  vignettes are built on it. But a preference about a described escalation and a report of one that happened are
  different evidence and must not be merged in a theme without comment.
- **Believed capability**: where a participant describes the agent doing something, check `/system/`. If the
  capability is not implemented and logged, tag `[believed-capability]` and code what they believed, never what
  the agent did.
- **Silence and refusal**: "I would rather not say" is codeable, and so is a participant who answers a question
  about their own medication with an account of a relative's. In a household interview, what an older adult
  declines to say while a caregiver is present is data about the household, not a gap.
- **Distress or sensitive disclosure**: several transcripts contain accounts of ridicule, anticipated ridicule,
  social anxiety, and clinical contact. Handle these in the report with care. Ask whether the extract is
  necessary to the argument or whether a paraphrase suffices, and note the choice in the reflexivity statement.
  Anonymization is not sufficient protection on its own for a small population; consider whether the combination
  of details in an extract makes a person identifiable within their own household or neighbourhood, and
  generalize identifying specifics if it does. In Study 3 the risk runs inside the family: a caregiver may
  recognise the older adult's account of an episode they both lived.
- **Talk about a retired study phase**: where a participant refers to an earlier, deficit-framed protocol, that is
  historical protocol talk. Code it as an interactional artifact if it shapes the turn, never as data about the
  present study.

## 7. Codebook format

| Code | Definition | Include | Exclude | Extracts (n) | Anchor extract | Type |
|---|---|---|---|---|---|---|

Standing note under the table: *counts indicate coding coverage, not analytic importance.*

Group the codebook by working cluster once clusters appear. Keep orphan codes in a final "unclustered" block
rather than deleting them; they are where the next reading often starts.

Add a `Grade` note in the definition cell where an extract set is mostly elicited or mostly hypothetical, so the
discount travels with the code into Phase 3 instead of being remembered.

## 8. Recoding and drift

Vocabulary drifts twice in this design, and each drift is handled in a different place.

**Within a transcript.** Your codes at the end of a long interview are sharper than your codes at its start.
Reread the transcript once with the settled vocabulary before Pass B, recode what needs it, and record the pass
in `01-memo.md` with a line on what changed. This is what separates a coded transcript from a coded first half.

**Across transcripts.** Do not go back and rewrite the first transcript after coding the sixth. Each transcript
unit is finished on its own terms, and reconciling vocabulary between transcripts is the master synthesis's job
(SKILL.md Section 6), where `Pharmacist as interpreter` in OA04 and `Asks the chemist` in OA09 become one master
code with both original names recorded. Rewriting earlier units instead would erase the record of how each
account actually read. The same holds across studies: Study 1's codes are not renamed to match Study 2's, because
the difference in vocabulary between the human baseline and the agent-directed case is what the cross-study
synthesis reads.
