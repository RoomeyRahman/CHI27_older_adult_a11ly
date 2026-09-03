# Quality control, reflexivity, and pitfalls

Read this before Phase 4 and again before writing up. Contents:

1. The theme-development log
2. Quality checklist
3. Reflexivity statement structure
4. Standing reflexive prompts for this corpus
5. Common failure modes
6. What to say if asked about validity, saturation, or inter-rater reliability
7. Project gates this analysis must also clear

---

## 1. The theme-development log

Every structural change gets one row in the unit's development log: `04-themes.md` for a transcript unit,
`study<N>/master/02-themes.md` for a study synthesis, `cross-study/02-themes.md` for the affiliation synthesis.
This is the audit trail, and it is what makes a single-analyst reflexive analysis defensible.

| Phase | Action | What changed | Reason | Evidence consulted |
|---|---|---|---|---|
The rows below are shape examples; the wording is illustrative and none of it is a real finding.

| Phase | Action | What changed | Reason | Evidence consulted |
|---|---|---|---|---|
| 4 | Split | "Family involvement" became "Standing rights to be consulted" and "Episodic help with a specific task" | Two distinct central concepts had been collapsed; extracts under the first were about position in the household, under the second about a task | OA02, OA04, CG02, CG06 coding tables |
| 4 | Discard | "Device inventory" | Elicited by direct questioning only; no conceptual traction; no mechanism linking device to any other code | Full study re-read |
| 3 to 2 | Recode | Added a latent layer to semantic-only codes in the first three transcripts | Codebook was drifting descriptive; Phase 3 clustering produced topic groups rather than themes | OA01 to OA03 |
| 4 | Demote | "Prescription hard to read" from theme to sub-theme | Real and corroborated, but it is a condition under which consultation happens rather than a separate claim about meaning | OA01, OA05, CG03 |

Backward loops between passes get a row too, naming the pass the loop started in and the pass it returned to:

| Phase | Action | What changed | Reason | Evidence consulted |
|---|---|---|---|---|
| C to A | Recode loop | Split `Checks the box daily` into a monitoring code and a reassurance code | Pass C could not place the code under either sub-theme without deciding which half of it was meant; the ambiguity was in the code, not the grouping | OA04, CG02 coding tables |

When a loop resets downstream columns to pending, say so here as well, so a reader can see why a matrix column
was rebuilt.

The log is written as the decisions happen, not reconstructed at the end. A log written afterwards records what
you can remember, which is the decisions that turned out well.

## 2. Quality checklist

Run before finalizing and write it into `master/04-review.md`, each item pass, fail, or pending, with a one-line
reason for anything not passing.

**Sequence**
- [ ] Each transcript was analysed in full, on its own, through all five passes, before the next one started
- [ ] Each study's master synthesis ran only after that study's transcripts were complete, and reads their registers and matrices
- [ ] Studies were never merged into one pooled corpus; the cross-study synthesis compares the study masters
- [ ] The Study 3 non-interview streams were analysed separately from its interviews
- [ ] The run did not stop after a transcript or a pass; both FINAL files exist

**Counts**
- [ ] Candidates per transcript recorded, near the 40 to 80 calibration range
- [ ] 25 to 30 retained per transcript, or a justified number outside it
- [ ] At most 40 master codes per study; 3 to 5 master themes over 6 to 12 sub-themes; at most 25 cross-study codes
- [ ] No code was trimmed by frequency; every retained code carries its five criterion answers
- [ ] Every register accounts for every candidate as RETAINED or PARKED with a reason

**Chain of derivation**
- [ ] Every sub-theme lists constituent codes by exact name, all from the retained set
- [ ] Every theme lists constituent sub-themes by exact name
- [ ] No theme was built directly from codes, bypassing sub-themes
- [ ] The chain theme to sub-theme to code to extract walks in both directions
- [ ] Master themes trace back to the per-transcript themes they draw on

**Coding**
- [ ] Every code name is six words or fewer, nuance in the definition
- [ ] No interviewer or facilitator turn is quoted anywhere
- [ ] Elliptical answers coded with recovered content and tagged `[elicited]` where the question was closed
- [ ] Codes carry a latent layer, not only semantic labels
- [ ] Disconfirming material coded and retained through the trim

**Themes**
- [ ] Each theme has one central organizing concept statable in a sentence
- [ ] Theme names are descriptive research English: no subtitle, no quoted phrase, no metaphor
- [ ] No theme is a topic bucket, an interview module, or a research question restated
- [ ] Every master theme clears the two-source rule or carries `[single-instance]`
- [ ] No theme rests disproportionately on a single articulate participant

**Interpretation**
- [ ] Frequency never used as a proxy for importance
- [ ] Every theme answers "so what?"
- [ ] Analytic claims distinguished from participant claims
- [ ] Alternative readings considered, and the choice among them stated
- [ ] Seeded tensions survive in the report, not only in the working files

**Deliverables**
- [ ] Everything this run wrote is inside this agent's slot; no file in another slot was created or edited
- [ ] `README.md` names the agent that produced the slot
- [ ] `FINAL-CODEBOOK.md` generated from the study `master/03-matrix.md` files and `cross-study/03-matrix.md`, not hand-written
- [ ] One section per study that ran, cross-study last; a study that has not run is omitted, not stubbed
- [ ] Cell caps respected: definition 20 words, one quote of 25 words, reflexivity note 20 words
- [ ] `table_check.py`, `quote_check.py`, and `anon_scan.sh` all pass, scoped to this slot
- [ ] `README.md` states what is final, what is working, and the date of the last run

## 3. Reflexivity statement structure

Write 250 to 500 words in each `<slot>/study<N>/master/05-reflexivity.md` and in
`<slot>/cross-study/05-reflexivity.md`, first person, past tense, covering:

1. **Positionality.** Disciplinary background, relationship to the domain, relationship to participants, and
   what in that background makes certain readings easy and others hard to reach. For this study the specifics
   that matter: the research team comes from computing rather than gerontology or nursing; the interviews were
   conducted in Bangla by team members and reach the analysis in English translation; Study 1 interviews happened
   mostly in participants' homes, where a family member's presence shapes what an older adult will say about that
   family member; the team built the agent it is now evaluating, which makes a participant's politeness about it
   a plausible reading of any positive account; and the researchers are, in age and in role, closer to the adult
   children in these households than to the older adults, which makes the caregiver's account the easier one to
   find persuasive.
2. **Assumptions brought in.** The theoretical commitments held at the start, named plainly. Here that includes
   the expectation that families would treat monitoring as intrusion and that older adults would defend
   independence against it. Say that it was held before the coding started, since the data may not support it.
3. **Where the data resisted.** At least one concrete instance where the analysis went somewhere unexpected, or
   where a favoured reading had to be abandoned. A reflexivity statement with no such instance is decorative. The
   seeded tensions of CLAUDE.md Section 9.3 are where to look first: delegated dependence read as agency, memory
   restored rather than replaced, oversight read as intimacy, streak grief, trust built by self-verification.
4. **Decisions and their alternatives.** The two or three consequential analytic choices, the roads not taken,
   and why. Include the decision about how much weight hypothetical judgments carry, and, for Study 3, how a
   divergence between paired accounts was handled.
5. **Effects on the account.** What this analysis is therefore well-placed to see, and what it is likely to have
   missed. Translation, the pre-publication character of most of the sample, and the absence of any observation
   of actual editing sessions all belong here.

Where the analysis is produced with AI assistance, say so plainly and describe the division of labour, since
that is now a material part of the audit trail.

## 4. Standing reflexive prompts for this corpus

Ask these periodically during coding and theme development, and record answers that change something in the
unit's `01-memo.md`:

- Whose account am I finding most persuasive, and why that one?
- Which participant am I quietly arguing with?
- Am I reading a translated phrase as if the participant chose that English word?
- Am I treating advocacy talk as true because I am sympathetic to it?
- Is this a report of something done, something the participant believes the agent did, or something imagined?
  Have I marked which, and have I checked the believed capability against `/system/`?
- Whose account of this episode am I holding: the person who acted, or the person who was acted on?
- Am I reading a caregiver's account of an older adult's forgetting as evidence of forgetting, rather than as
  evidence of how caregivers account for their own work?
- Am I coding for the framing document's argument or for what answers the research question?
- What would a researcher from a different tradition see here that I am not seeing? A speech-language
  gerontologist would see something different from a care-ethics scholar; both would see something the design
  frame does not.
- If this theme is wrong, what in the data would show it? Have I looked?
- Am I reaching for a familiar HCI construct because it fits, or because it is nearby in the theory ledger?

## 5. Common failure modes

- **Topic summaries as themes.** Diagnosis: theme names are nouns; sub-themes reproduce the interview guide; the
  definition is a list of what participants said about the topic. Fix: ask what the extracts share *in meaning*
  and rename around that.
- **Analysis of the instrument.** If the themes map one to one onto the four interview modules, or onto the
  three research questions, the instrument has been summarized rather than the data. The RQs are what the themes
  must answer, not what they must be.
- **The bucket theme.** Everything that did not fit elsewhere. Fix: dissolve and redistribute, or admit it is
  unanalyzed residue and say so.
- **Frequency creep.** "Most participants", "the majority felt". With samples this size it also invites a reader
  to read a rate into a count. Fix: replace with an interpretive claim, or state the count and explicitly
  disclaim importance.
- **Lone-user drift.** A theme that describes one person's practice with the household edited out. Fix: re-read
  against the commitment that the care network is the unit of analysis, and restore who else was in the episode.
- **Settling the checking question by assumption.** Coding a check as surveillance, or as care, because of what
  monitoring usually means rather than because of what this episode shows. Fix: let the code carry the ambiguity
  and let the extract decide.
- **Scope stretch.** Reading a network or allegiance claim out of Study 2. Fix: tag it `[study2-scope-limited]`
  and let Study 3 carry it.
- **Quote dumping.** Fix: apply the claim, extract, interpretation, implication rhythm.
- **Theme count inflation.** Nine themes usually means codes were renamed rather than clustered.
- **Merging evidence grades.** Building a theme from one participant's lived workaround and another's reaction
  to a demonstration, without saying which is which.
- **Positivist creep.** Validation, saturation, reliability, and bias-elimination imported into a reflexive
  framework where those concepts do different work.
- **Over-claiming from thin data.** One transcript cannot evidence patterning across a dataset.
- **Deficit drift.** A theme that ends up describing what older adults cannot do. Every such theme should be
  re-read against the framing commitment that this is a design gap, not a memory problem.
- **Non-use read as missing data.** A refusal, a silence, or an ignored reminder recorded as absence rather than
  as a move. Fix: code it as participation and say what it accomplished.

## 6. If asked about validity, saturation, or inter-rater reliability

- **Inter-rater reliability**: not appropriate here. Coding consensus measures the extent to which two people can
  be trained to apply a fixed frame; reflexive TA treats interpretation as situated and generative, so agreement
  is neither achievable nor desirable as a quality criterion. Offer instead: audit trail, analytic memos,
  reflexive journaling, critical-friend challenge, member reflection, and transparency about alternative
  readings.
- **Saturation**: developed within grounded theory around theoretical sampling, and it presumes meaning can be
  exhausted. Reflexive TA prefers *information power*: sample adequacy judged against study aim, specificity of
  the sample, quality of dialogue, and analytic strategy. For this work, say what makes each study's sample
  adequate for the questions it actually answers, and say where it is not: Study 1 speaks to RQ1, Study 2 to
  system trust and habituation only, and RQ2 and RQ3 wait on Study 3.
- **Validity**: reframe as trustworthiness and quality of interpretation. The claim is not that another analyst
  would produce the same themes, but that these themes are well-evidenced, coherent, transparently derived, and
  useful.

State these positions matter-of-factly rather than defensively. If a reviewer expects a codebook or
coding-reliability approach, explain the difference and help them read the audit trail instead.

## 7. Project gates this analysis must also clear

Beyond the checklist above, the analysis artifacts are the evidentiary base for the Findings section and must not
create work the drafting skills then have to undo:

- **Contribution.** Every master theme states which of C1 empirical, C2 conceptual, or C3 design it serves
  (CLAUDE.md Section 9.1).
- **RQ mapping.** Every final theme maps to RQ1, RQ2, or RQ3 from `/proposal/proposal.md`. Unmapped material is
  context and is labeled as such. No theme answers a retired question.
- **Evidence.** Every extract carries a participant id and, where the transcript has one, a timestamp. Counts
  match CLAUDE.md Section 3 exactly where they touch study facts.
- **Theory.** The Theory Alignment block exists in `cross-study/05-reflexivity.md`, the ledger is updated in the same
  run, and the enforcement rule holds: if a theoretical citation could be deleted without changing a paragraph's
  conclusion, either the paragraph is rewritten so the theory works or the citation goes.
- **Framing.** No artifact frames an older adult as a deficit technology should repair, re-centers the lone user
  in place of the care network, or lets a described agent capability outrun what `/system/` logs.
- **Anonymity.** No unconfirmed participant name appears anywhere in the slot; `anon_scan.sh` passes.
- **Tension.** Disconfirming cases appear in `FINAL-REPORT.md`, not only in the coding tables.
