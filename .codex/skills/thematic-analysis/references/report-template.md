# Report template and writing conventions

Read this before Phase 6. Contents:

1. Deliverable structure
2. The claim, extract, interpretation, implication rhythm
3. Quote selection and formatting
4. Answering "so what?"
5. Worked example of analytic prose
6. Variants: the report, the Findings feed, an applied summary

---

## 1. Deliverable structure

`<slot>/FINAL-REPORT.md` follows this order of argument, where `<slot>` is this agent's folder under
`/output/codes/`, `A2/` for Codex, `A1/` for Claude Code, and `A3/` and beyond for other analysing agents (SKILL.md Section 0.0). It sits at the top of the
slot alongside `FINAL-CODEBOOK.md`, because those two files are the deliverable and everything in the folders is
the audit trail that produced them.

```
# Reflexive thematic analysis: care networks and an agent's allegiance

## 1. Analytic approach
Reflexive TA; critical realist position; inductive weighting with a deductive second pass using the
affiliation codebook; dataset description, one line per study, with exact counts from AGENTS.md
Section 3 and their filed sources; single-analyst rationale; translation from Bangla; conventions for
quotes, participant ids, and anonymization. State the analytic sequence plainly: each transcript
analysed in full on its own, then a master synthesis per study, then the cross-study affiliation
synthesis. State the coding trajectory in one sentence per study with real numbers: candidates per
transcript, retained per transcript, master retained, sub-themes, themes.

## 2. Reflexivity and positionality
Pointer to 07-reflexivity-statement.md plus a two-paragraph summary that a reader of this file alone
can use.

## 3. Overview of the thematic structure
Thematic map, plus one paragraph stating the overall argument the themes make together. A reader
should be able to stop here and know what the analysis claims.

## 4. Theme 1, [Name] (from the study master synthesis, one block of themes per study)
   Definition paragraph
   Sub-theme 1.1, analysis with extracts
   Sub-theme 1.2, analysis with extracts
   Boundary and variation, including the disconfirming cases
   So what: theoretical and design significance
   RQ served, contribution served, corroboration status

## 5. Theme 2, [Name]
   ...

## 6. Relations between themes
Where they reinforce, where they pull against each other, what the tension means.

## 6a. Cross-study affiliation synthesis
For each of the five practices, assignment, contestation, gifting, revocation, and ceremony, what it
looked like among humans in Study 1 and what it looked like directed at the agent in Studies 2 and 3,
and what changed in the move. A practice with no agent-directed instance is reported as such. This
section is the analytic payoff and the paper's conceptual contribution is built from it. Studies are
never merged into one pooled corpus; where two disagree, both readings stand and the disagreement is
stated.

## 7. Discussion
Connection to the theory ledger and to prior HCI literature where the fit is real; what this extends,
complicates, or contradicts; implications for AI speech editing design; limitations and boundary
conditions.

## Appendix A, pointer to the per-transcript registers in <slot>/P*/03-code-register.md
## Appendix B, pointer to the development logs in <slot>/*/04-themes.md and <slot>/master/02-themes.md
## Appendix C, pointer to the memos in <slot>/P*/01-memo.md
## Appendix D, pointer to FINAL-CODEBOOK.md
```

Do not duplicate the codebook or the matrix into the report. They are separate inspectable artifacts and the
report points at them.

## 2. The rhythm

Every analytic paragraph follows the same movement:

1. **Claim**, the analytic point, stated in your voice, not the participant's.
2. **Extract**, the data that earns it.
3. **Interpretation**, what in the extract supports the claim, attending to the specific words and to what the
   participant is doing with the utterance.
4. **Implication**, what follows for the theme, for design, or for theory.

The failure mode to avoid is the quote sandwich with no filling: a topic sentence, three quotes in a row, and a
sentence saying that participants had varied views. If two extracts sit adjacent, there must be a reason,
contrast, escalation, or range, and you must state it.

## 3. Quotes

- Short extracts, under about 25 words, run inline in quotation marks. Longer ones are block quotes with the
  participant id and, where the transcript carries one, the timestamp.
- Attribute every extract: `(OA07, 26:33)`, or `(D2)` where no timestamp exists, or `(H3-CG1)` for a Study 3
  household member.
- **Never quote the interviewer or facilitator.** Where an answer needs its question to be readable, put the
  recovered content inside the participant's quote in square brackets, or state it in your own sentence
  introducing the extract. A two-speaker dialogue block is not an extract.
- Choose for **vividness** and **coverage**. Across a theme's extracts the reader should see its range, including
  at least one extract that sits near its boundary or complicates it.
- Do not use a quote merely because it restates the theme name. The best extracts are slightly in excess of the
  claim; they carry something the claim does not fully capture, and you comment on that surplus.
- Elision `[...]`. Insertions for sense `[the editing app]`. Do not clean grammar further: these transcripts are
  already translated and lightly cleaned at source, and that fact is stated once in Section 1 and not repeated.
  A kinship term or honorific is left as the filed translation gives it, because the relation is the analysis.
- Where an extract is elicited by a leading question, or is a participant reasoning about a hypothetical
  scenario rather than reporting practice, say so in the sentence that introduces it. Do not bury it in a
  footnote and do not omit it. The same holds for an extract describing an agent capability `/system/` does not
  log: report it as what the participant believed.
- Balance across participants, and in Study 1 across older adults and caregivers. If one participant supplies
  more than roughly a third of the extracts in a theme, revisit the theme. If every extract in a Study 1 theme
  comes from one side of the network, that is a finding about whose account it is, and it is stated.
- For a Study 3 paired episode, quote both sides or say why only one is quoted. A one-sided quotation of a
  paired episode reads as agreement that was never established.
- Consent-based exclusions govern: material a participant or their family asked to be excluded is unusable even
  anonymized. Check before quoting.
- Re-read every extract for identifiability within a small community, not only for names. A combination of
  institution, neighbourhood, and role can identify a person even after names are removed. Generalize the
  specifics if it can.

## 4. Answering "so what?"

Each theme ends with a passage doing at least two of these:

- **Extends theory**: names a construct from the ledger and shows where the data push past it.
- **Complicates a design assumption**: identifies a belief embedded in current adherence and caregiver-monitoring
  systems that the data undercut.
- **Reframes the problem**: shows that what the field treats as an adherence or usability issue is better
  understood as something else, a question of whom the system serves, or of what the checking is for.
- **Specifies conditions**: states when and for whom the pattern holds, and when it breaks.

Weak: *This suggests control is important for older adults.*

Strong: *A missed dose in this corpus is usually treated as an individual failure, and the design response that
follows is a louder reminder. These accounts describe something a reminder cannot reach. The dose was missed at
a wedding, in a household where three people habitually track the regimen and none of them was present, so the
lapse belongs to a distribution of attention rather than to a memory. What follows is not a better notification
but a decision about whom the system tells when attention lapses, which is what makes the allegiance question
the relevant one here rather than salience.*

Cite real, checkable literature. If unsure a source exists, describe the position and mark it `[cite]` for the
user to verify rather than inventing a reference. Fabricated references are worse than an unreferenced claim.

## 5. Worked example of analytic prose

The passage below is a shape example, written to show the rhythm. The wording is illustrative and no extract in
it is real; never carry it into an artifact.

> Participants who described consulting a family member did not present it as help sought. They described a
> standing arrangement, which puts the relationship first and the difficulty second:
>
> > "I discuss with [my eldest son] during any difficulties." (OA04)
>
> The tense is the interesting part. The verb is habitual rather than episodic, and the difficulty is named in
> the plural and in the abstract, so the arrangement precedes any particular problem. What the son supplies is
> not a solution to this prescription but a standing right to be consulted about prescriptions, which is a
> position in the household rather than an act of assistance. Reading it as help sought would make the older
> adult the one with the deficit and the son the remedy, and the grammar of the account will not carry that.
>
> This matters for what an agent inherits. A system that escalates to a family member is not adding a helper to
> a household that lacked one; it is entering a position that is already occupied and already earned, and the
> question the family will ask it is the question they have already settled among themselves, which is [...]

Note what the passage does: names the analytic point first, uses the extract as evidence rather than
illustration, reads the specific wording, and identifies the mechanism that makes the stance available.

## 6. Variants

- **The analysis report** (`FINAL-REPORT.md`), the default above. Full structure, audit trail as appendix
  pointers, written for a reader who will test the derivation.
- **The Findings feed.** When the Findings section is drafted, `$plan-section` and `$draft` consume this report,
  not the transcripts. That means every claim the Findings will make must exist here first with its extract
  attached, and every theme heading here should be usable as a subsection heading there. Keep theme names
  analytically precise rather than elegant; `$polish` handles the prose, not the analysis. Findings prose is
  2500 to 4000 words and folds implications into the Discussion; this report may be longer and keeps its
  implications with each theme. Every theme carries the RQ it answers and which of C1, C2, or C3 it serves, so
  the Findings plan can map them without re-deriving the mapping.
- **An applied summary**, if ever asked for by a community partner: invert the order, lead with the thematic
  overview and what follows from it, keep quotes prominent, shorten the theory linkage, and add a short "what we
  are not claiming" section, which prevents over-reading. Anonymization rules are stricter, not looser, in
  anything that returns to the community the participants were recruited from.
