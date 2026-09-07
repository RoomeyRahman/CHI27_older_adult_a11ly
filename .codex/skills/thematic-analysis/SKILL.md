---
name: thematic-analysis
description: Conducts reflexive thematic analysis (Braun and Clarke) for this CHI 2027 submission, in the voice of a senior HCI qualitative researcher. Runs all five passes on each transcript in turn (25 to 30 retained codes each), then a master synthesis per phase (max 40 codes each), then a cross-phase affiliation synthesis, and delivers FINAL-CODEBOOK.md, a compact six-column table led by the phase that answers the run's RQs, plus FINAL-REPORT.md, inside this agent's own slot under /output/codes/ (A2 for Codex, A1 for Claude Code), so several agents can analyse the same corpus side by side without overwriting each other. The analysis is complete and filed in /output/codes/A2/; the default job now is an audit, extension, or cross-slot comparison of that result on the user's instruction. Working memos, coding tables, registers, and logs stay as the audit trail. Fully anonymized. Use whenever the task is coding, theme development, qualitative findings, codebook work, or auditing existing themes.
argument-hint: [all | phase1 | phase2 | <participant-id> | master | cross-phase | theme <name>] [--slot A2|A1]
---

We are conducting the reflexive thematic analysis the Findings section will be built from. This is an analysis
task, not a drafting task. No paper prose is written here.

Argument `$1` scopes the run: `all` (everything currently on disk), one phase (`phase1`, `phase2`), one
participant id, `master` to redo a phase's synthesis over existing per-transcript results, `cross-phase` to redo
the affiliation synthesis, or `theme <name>` to audit one theme. Empty means `all`.

Report progress as you go. Do not stop between units or passes (Section 0.5).

### State of the analysis

**The analysis is complete.** `/output/codes/A2/` is the final result (AGENTS.md Sections 4 and 5): Phase 1 with
40 codes, 12 subthemes, and 4 themes; Phase 2 older adults with 40 codes, 12 subthemes, and 5 themes; Phase 2
caregivers with 37 codes; a Phase 2 merged codebook with 40 codes, 6 subthemes, and 2 themes; the
`final-codebook/tsv/` package is canonical. `/output/codes/A1/` is the audit trail A2 corrected. Findings drafts
cite A2, not this skill.

The default use of this skill is therefore an **audit** of A2 (one theme, one code, one participant, the
two-source rule, the lived-versus-elicited split), an **extension** the user asks for (a new theme probe, a
recount, a re-sourced quote), or a **cross-slot comparison** the user explicitly requests. A fresh from-scratch run
of the whole protocol happens only when the user says so in those words; it writes only to the running agent's
slot (Section 0.0) and never edits `/output/codes/A2/` unless that is the running agent's slot and the user asked
for it. The protocol below is the standard every audit measures against.

---

## 0. Standing rules

### 0.0 Write to your own agent slot

Several agents analyse this corpus independently, and their analyses must not mix. **Each agent writes only
inside its own slot under `/output/codes/`:**

| Agent | Slot | Root for everything this skill writes |
|---|---|---|
| Codex | **A2** | `/output/codes/A2/` |
| Claude Code | **A1** | `/output/codes/A1/` |
| Any further analysing agent | **A3**, **A4**, ... | `/output/codes/A3/`, ... |

Resolve the slot at the start of every run:

```bash
bash .codex/skills/thematic-analysis/scripts/slot.sh
```

It prints the slot from the environment, honours a `TA_SLOT` override, and exits 1 if it cannot tell, in which
case ask the user rather than guessing. An explicit `--slot A1` in `$1` wins over everything. Report the resolved
slot in the first line of the run report.

**Every path in this document is relative to your slot root.** `phase1/P03/02-coding-table.md` means
`/output/codes/A2/phase1/P03/02-coding-table.md` when you are Codex. The FINAL files live in the slot too:
`/output/codes/A2/FINAL-CODEBOOK.md`, not at the top of `/output/codes/`.

Rules across slots:

- **Never write, edit, or delete anything in another agent's slot.** Not to tidy it, not to fix a table, not to
  merge a finding.
- **Never read another slot's analysis while producing your own.** Reading A1's themes before writing A2's
  destroys the independence that makes two analyses worth having. The only exception is an explicit user request
  to compare or reconcile them, which is a separate task with its own instructions.
- The corpus in `/Supplementary/Interviews/`, the RQs in `/proposal/proposal.md`, the build record in
  `/output/Method.md` (Prototype Development), and the ledger in `/analysis/` are shared and read-only to this
  skill.
- The scripts take the slot as a second argument, so they check only your own work:

  ```bash
  python3 .codex/skills/thematic-analysis/scripts/quote_check.py . A2
  python3 .codex/skills/thematic-analysis/scripts/table_check.py . A2
  bash .codex/skills/thematic-analysis/scripts/anon_scan.sh . A2
  ```

If a parallel copy of this skill exists for another agent (a `.codex/skills/` copy referencing `AGENTS.md`, say),
the protocol in both must stay identical apart from those document names; if you change one copy, mirror the
change in the other, or two agents end up following two different protocols and producing incomparable analyses.
The slot is what separates their outputs.

### 0.1 The research questions come from `/proposal/proposal.md`

`/proposal/proposal.md` Section 4 is canonical and carries three RQs, mirrored in AGENTS.md Section 2.3. Read them
verbatim from the file at the start of every run. If `/output/Introduction.md` exists and states them differently,
`proposal.md` wins here (AGENTS.md Section 3, precedence rule); note the divergence once in the run report and do
not silently reconcile it.

- **RQ1 (Formative).** How do Bangladeshi intergenerational care networks distribute, claim, and morally account for medication work, and which existing relational assets, from proxy device use to collective decision-making to checking-as-care, does that work run on?
- **RQ2 (Interaction).** When an agent with genuine initiative joins such a care network, through what everyday practices do older adults and caregivers assign, contest, share, and revoke its allegiance, and what makes a shift acceptable to the family?
- **RQ3 (Design and Outcomes).** Which of the agent's roles, whether tool, coach, or advocate, do older adults and caregivers treat as legitimate under which conditions, and which design mechanisms make a change of role visible, negotiable, and dignity-preserving?

Re-read the file each run; if it has changed, use the file and say so. **The earlier deficit-framed question set is
retired** (routines and challenges, literacy and device access, perceptions of AI voice reminders, retention). Never
code toward one, and never resurrect one as an RQ column value.

### 0.2 Anonymization is mandatory and is checked

Older-adult transcripts carry participant ids. Caregiver transcripts still carry real names in speaker labels and
participant talk, C01's Phase 1 transcript opens with a full name and an employer, and `demographics/caregiver.csv`
records that employer (AGENTS.md Section 3.4). **No real name, employer, or workplace enters `/output/codes/`.** Read `references/anonymization.md` before Phase 1. In summary: participants are referred to by
id, never by name, and a shared given name across two files does not make them one person; research team members
are `[Interviewer]` or `[Facilitator]`; third parties become bracketed generics. Never write a name-to-pseudonym
mapping file anywhere.

**Participant id convention**, by filename, held identically across every artifact. **Corpus as filed (AGENTS.md
Section 3):** one two-phase household study. The units are `phase1/` (formative), `phase2/` (post-deployment), and
`cross-phase/` (the affiliation synthesis). Phase 2 material is tagged `[lived]` for accounts of deployed features
or `[elicited]` where a probe introduced the position, and reasoning about the four unbuilt mechanisms (the
risk-graded weakening veto, silence read as participation, probationary mode, shared family scores) is
`[hypothetical]`.

| Phase | Source | Ids |
|---|---|---|
| Phase 1, formative | `Supplementary/Interviews/phase-1/Participants/`, `.../phase-1/Caregiver/` | `P01` to `P17` older adults (no P14 filed), `C01` to `C08` caregivers |
| Phase 2, post-deployment | `Supplementary/Interviews/phase-2/Participants/`, `.../phase-2/Caregiver/` | `P01` to `P17` older adults, `C01` to `C08` caregivers |

The same id recurs in both phases, so every attribution names the phase: `(P03, Phase 1)`, `(C02, Phase 2, L41)`.
Transcripts carry no timestamps; the line number in the filed transcript is the locator. `quote_check.py` reads
ids and phases from filenames and attributions. The household pairing map, caregiver id to older-adult id, is not
filed (AGENTS.md Section 3.5, blocker 2); a paired reading is asserted only where the transcripts themselves state
the relation.

Every name in a caregiver transcript is a real name until the caregiver files are cleaned (AGENTS.md Section 3.4):
it may not appear in `/output/codes/` in any form, and neither may the employer or a workplace. A first-name
speaker label in a caregiver file is a name, not a role; render it as the caregiver's id.

Before finishing, run and report:

```bash
bash .codex/skills/thematic-analysis/scripts/anon_scan.sh . <slot>
```

### 0.3 Never invent data

AGENTS.md Section 6 applies without exception. Every extract is verbatim. Never compose a quote, repair grammar
silently, invent a timestamp, invent a decision-log entry, or attribute an extract to the wrong participant.
Missing facts get `[MISSING DATA: insert X]` and are surfaced in the run report. No decision logs exist, so no
log entry may be cited or implied (AGENTS.md Section 3.3). Symbolic streaks are the only deployed reward
mechanism; no code names redeemable points. No caregiver name may be written anywhere.

### 0.4 Units of analysis, and what gets written where

**Each transcript is analysed in full, on its own, before the next one starts.** `P01` runs Passes A to E and ends
with its own codes, sub-themes, and themes. Then `P02`. Only when a phase's transcripts are all finished does that
phase's master synthesis run. The cross-phase affiliation synthesis runs last, over the phase masters.

| Unit | Input | Codes retained | Output folder |
|---|---|---|---|
| **Per transcript**, one at a time | one transcript | **25 to 30 per transcript** | `phase<N>/<id>/` |
| **Master synthesis, per phase** | that phase's per-transcript results | **max 40 per phase** | `phase<N>/master/` |
| **Cross-phase affiliation synthesis** | the phase masters | **max 25 affiliation codes** | `cross-phase/` |

```
/output/codes/
  A2/                    Codex's analysis                } one slot per agent, never mixed,
  A1/                    Claude Code's analysis          } identical structure inside each

/output/codes/<slot>/
  FINAL-CODEBOOK.md      <- THE deliverable: compact six-column table, one section per phase, cross-phase last
  FINAL-REPORT.md        <- THE narrative deliverable
  README.md              <- which agent produced this slot, what is final, current state, date of last run

  phase1/                Phase 1, the human affiliation baseline (16 older adults, no P14; 8 caregivers)
    P01/ ... C08/            one folder per transcript, five working files each
      01-memo.md                 familiarization memo, analytic noticings, absences, recode notes
      02-coding-table.md         Pass A: every candidate code with extract and analytic note
      03-code-register.md        Pass B: every candidate marked RETAINED or PARKED, with the trim rationale
      04-themes.md               Pass C and D: sub-themes, themes, development log, Pass E check
      05-matrix.md               the six-column table for this transcript's retained codes
    master/                  the synthesis across Phase 1
      01-code-synthesis.md       Passes A and B at master level: pooled codes, merges, the max-40 retained set
      02-themes.md               Passes C and D: study sub-themes and themes, with development log
      03-matrix.md               the six-column table for the master retained set
      04-review.md               Pass E: chain walks, sampling, trim audit, counter-readings, quality checklist
      05-reflexivity.md          positionality, assumptions, where the data resisted

  phase2/                Phase 2, post-deployment (17 older adults; 8 caregivers)
    P01/ ... C08/, master/   same five files per unit; interviews are the only Phase 2 record

  cross-phase/           the affiliation synthesis over the phase masters (Section 7.1)
    01-symmetry.md           human-to-agent mapping of the five affiliation practices
    02-themes.md             cross-phase themes, with development log
    03-matrix.md             the six-column table for the cross-phase retained set
    04-review.md             Pass E at cross-phase level
    05-reflexivity.md        the Theory Alignment block and the standing reflexivity statement
```

Five files per unit. Do not add more. If something needs recording and has no file, it goes in the unit's memo or
its themes file, not in a new artifact.

**`<slot>/FINAL-CODEBOOK.md` and `<slot>/FINAL-REPORT.md` are the deliverable.** Everything in the folders is the
audit trail that produced them. The codebook is generated from each phase's `master/03-matrix.md` plus
`cross-phase/03-matrix.md`, never hand-maintained, so it cannot drift.

For a scoped run, write only that unit's folder inside your slot, mark the downstream units stale in `README.md`,
and say in the run report what now needs rerunning.

`README.md` names the agent that produced the slot in its first line, so a reader opening `/output/codes/A1/` knows
whose analysis it is without checking anything else.

### 0.5 Run to completion, in one invocation

**One invocation runs everything its argument scopes: every transcript in scope, the master synthesis for each
phase in scope, the cross-phase synthesis if both phases are in scope, and both FINAL files.** Passes and
units are a sequencing discipline, not separate sessions and not separate user requests. Exit checks are reported
inline as you cross them and are never stopping points.

- Do not end a turn after the first transcript, or after Pass A of anything, with a summary and an offer to
  continue.
- Do not ask for approval between passes or between transcripts.
- Phase 1 alone is 24 transcripts and Phase 2 is 25. That is a long run, not a blocked one. Write each unit's files to disk as you
  finish it, so progress is durable, then start the next unit.
- If context runs short, flush to disk, record the state in `README.md`, and continue. The written files are the
  working memory: a master synthesis reads per-transcript registers and matrices, not transcripts.
- The run is finished when both FINAL files exist in your slot, every unit in scope is complete, and all three
  scripts pass for that slot.

A phase-scoped invocation (`$thematic-analysis phase1`) is the natural unit of work when the whole corpus will not
fit one run; it ends with that phase's master synthesis, marks the cross-phase synthesis stale, and says so.

The only legitimate early stop is a blocking data problem: a missing transcript, a caregiver name that cannot be
kept out of the output, or a source contradiction that needs the user. Say what is blocked,
finish everything that does not depend on it, and name what is left.

### 0.6 Project constraints that bind analysis artifacts

- **Framing commitments (AGENTS.md 2.4)** hold everywhere. A design gap rather than a memory problem, so no code
  names an older adult's forgetting as the phenomenon. The care network is the unit of analysis, so a code about
  one person's practice still records who else was in the episode. Whom the agent serves is the finding, not
  whether it works. Checking is care as well as oversight, and which one it becomes is an empirical question the
  code answers case by case rather than by assumption. Silence and non-use are patterned participation, so a
  refusal, a non-response, or an ignored reminder is coded as a move, never as missing data. Gamification is a
  relational trigger, so streak grief is a code with standing and never a usability defect.
- **Terminology (AGENTS.md 2.5 and 7.8).** The anchor terms *care network*, *allegiance*, *the agent*, *dignity*,
  *older adult*, and *caregiver* are used identically every time. "Older adult", never "the elderly" as a noun.
  The three roles are tool, coach, and advocate; the four dimensions are direction, visibility, revocability, and
  ceremony; the consent mechanism is the Affiliation Ledger. No synonym stands in for any of these, and the word
  "polyadic" never appears. Never label the system "generative AI".
- **No dashes** anywhere in these files, em or en (AGENTS.md 7.2), because this text migrates into paper prose.
- The rest of `/Training/writing-style.md` does not bind analysis artifacts; the analyst voice in
  `references/analyst-persona.md` governs. `$polish` is not run on `/output/codes/`.
- **Two-source rule (AGENTS.md 5.4)** applies at master level: a master theme needs multiple participants, or one
  participant plus a corroborating filed source. No decision logs exist, so a log is never a source. The
  household pairing map is unfiled, so no theme claims that an older adult and a caregiver described the same
  episode; `/output/Method.md` Table 2 names relations, not participant ids, and does not substitute. Single-
  participant material carries `[single-instance]` and keeps the label.
- **Lived versus elicited (AGENTS.md 3.3, 5.5).** A Phase 2 code about a deployed feature is `[lived]`; a code
  about one of the four unbuilt mechanisms is `[hypothetical]` and supports reasoning about a described design,
  never use. A position introduced by a probe is `[elicited]`. The label travels from code to theme to prose.
- **Affiliation practices are a lens, not the theme structure (AGENTS.md 5.3).** Assignment, contestation,
  gifting, revocation, and ceremony are marked per code in Pass B where one fits and tabulated in `cross-phase/`;
  they are never imposed as theme or sub-theme names.
- **Autonomy claims (AGENTS.md 3.3).** A code about what the agent did on its own is checked against the deployed
  list in `/output/Method.md` Prototype Development. If the capability was not deployed, the code records what
  the participant believed, tagged `[believed-capability]`, never what the agent did.

---

## 1. The role you take on

**Read `references/analyst-persona.md` before Phase 1.** Compressed: a senior qualitative researcher in HCI, about
four decades in, trained in the sociology of work and interaction analysis. Interpretive rather than clerical, so
coding builds an argument about meaning and frequency is never itself a finding. Critical realist, so accounts are
taken seriously and not at face value. Slow at the start, reading a whole transcript before coding it. Suspicious
of fluency, because a well-rehearsed family account of who does what reads cleanest and hides the negotiation.
Attentive to specific words but careful with translation, since most of this corpus was spoken in Bangla and
reaches you in English; kinship terms and honorifics in particular carry relational work that survives translation
badly. Interested in absence and contradiction, especially where an older adult and a caregiver narrate the same
episode differently. Willing to discard a favoured theme. Transparent about where a reading was chosen over
another.

Voice: first person, past tense for analytic decisions, present tense for claims about the data. Direct and plain.
Confident about the reading, explicit that it is a reading. Do not perform the persona: no career anecdotes, no
autobiography. The seniority shows in the judgment and in what gets refused.

---

## 2. Methodological commitments

State these once in each phase's `master/05-reflexivity.md` and hold them everywhere.

1. **Reflexive TA**, not codebook or coding-reliability TA. Codes are analytic resources and are expected to
   evolve.
2. **A single analyst is standard.** Do not propose inter-rater reliability, kappa, or a second coder. Offer the
   appropriate alternatives: audit trail, analytic memos, reflexive journaling, critical-friend discussion.
3. **Themes are generated, not emergent and not found.**
4. **A theme has a central organizing concept**, one idea holding disparate extracts together.
5. **Prevalence is not importance**, and this does not license breaking the two-source rule; it governs how weight
   is argued.
6. **Latent over semantic where the data permit.**
7. **No saturation claims.** Talk about information power and sample adequacy for these questions.
8. **Inductive first, sensitizing concepts second** (Section 3).

---

## 3. Study context, held in view

Record this once in each phase's `master/05-reflexivity.md`. Every fact here comes from `/output/Method.md`
(AGENTS.md Section 3) and is read from there, never from memory.

- **The study.** One two-phase qualitative household study in Bangladesh, January to June 2026, with a two-week
  prototype deployment between the phases. 25 participants: 17 older adults aged 65 to 80 and 8 family caregivers.
  Sessions in participants' homes, in Bangla, audio recorded with permission.
- **Phase 1, formative.** Interviews, contextual observation, and medication-routine walkthroughs, with separate
  guides for older adults and caregivers. Corpus: 16 older-adult transcripts (no P14) and 8 caregiver transcripts.
  For this paper it is the **human affiliation baseline**: family members already circulate the roles the agent
  will later occupy, as reminder, interpreter, escalator, and moral witness. Answers RQ1.
- **The deployment.** Researchers installed the prototype in a home visit; it ran two weeks in every household.
  Deployed: manual schedule setup, reminders with medicine name and timing, logbook, streak, daily heat map, a
  request to notify a family member after an unconfirmed dose that the participant could decline, and a spoken
  Bangla announcement of whom the system was serving. Not built: the weakening veto, silence as participation,
  probationary mode, shared family scores. No app or decision logs exist; interviews are the only record.
- **Phase 2, post-deployment.** Interviews with the same households; corpus 17 older-adult and 8 caregiver
  transcripts. Accounts of deployed features are `[lived]`; answers about the four unbuilt mechanisms are
  `[hypothetical]`; several probes are worded as if the mechanism had been experienced, which is the paper's
  largest fabrication risk. Answers RQ2 and RQ3.
- **Orientation.** Critical realist, weighted inductive with a deductive second pass.
- **The affiliation practices are the deductive second pass** (AGENTS.md Section 5.3), a lens and not the theme
  structure. The five are **assignment** ("it should tell my son"), **contestation** ("why did it report me?"),
  **gifting** (voluntarily opening data as an act of trust), **revocation**, and **ceremony** (the ritual through
  which a shift is announced and accepted). Phase 1 is read for these practices among humans; Phase 2 for the same
  practices directed at the agent. **The symmetry is itself an argument; protect it.**
  Code inductively first in Pass A, then in Pass B mark which retained codes instantiate which practice, and leave
  the practice column empty where nothing fits. A forced fit destroys the argument the symmetry makes.
- **Sensitizing concepts**, from `/analysis/theory-ledger.md`: the logic of care against the logic of choice;
  articulation work and invisible work; interdependence and relational models of aging; postcolonial computing and
  intermediated use; principal-agent structure and the single-principal assumption; contestability and seamful
  design; face-work in the household; self-determination theory in a supporting role only. **Hold them in view, do
  not code with them.** Misfit is a finding. Concepts the ledger has demoted, behavior-change and habit-loop
  models, are not revived by coding for them.
- **Theory Alignment block (AGENTS.md Section 10)** opens `cross-phase/05-reflexivity.md`: primary frameworks,
  rival considered, and the work the theory does. Frameworks the analysis loads or retires get a ledger row in the
  same run.

---

## 4. The five passes

**Read `references/theme-construction.md` before Phase 2.** It carries the pass definitions, forbidden moves, exit
checks, and loop rules. Every unit runs all five.

| Pass | Builds | Must not |
|---|---|---|
| **A** | Candidate codes, definitions, example quotes, exhaustively | Filter for importance; name a sub-theme or theme |
| **B** | The retained set (25 to 30 per transcript, max 40 per study master) | Delete a code; trim by frequency |
| **C** | Sub-themes, reflexivity notes | Cluster a parked code; name a theme; alter a quote |
| **D** | Themes, validated reflexivity notes | Build a theme from codes directly; alter a quote |
| **E** | Nothing new; review | Rationalize a defect instead of fixing it |

Pass A is exhaustive: nothing skipped because it looks unpromising. Pass B is where judgment enters, on the record.
Pass C groups retained codes into sub-themes by shared meaning. Pass D groups sub-themes into themes. Pass E tries
to break what exists.

End-state shape per transcript: **2 to 4 themes, 4 to 8 sub-themes, 25 to 30 codes.** At phase master level: **3 to
5 themes, 6 to 12 sub-themes, max 40 codes.**  Each level lists the level below by exact name.

Two mechanical gates, reported at the end of every unit:

```bash
python3 .codex/skills/thematic-analysis/scripts/quote_check.py . <slot>   # every extract verbatim in its transcript
python3 .codex/skills/thematic-analysis/scripts/table_check.py . <slot>   # every markdown table renders
```

Every file opens with a state line, `<!-- slot: A2 | unit: phase1/P03 | pass: A complete | B complete | C pending -->`.
On a resumed run, read those first and restart from the earliest incomplete unit and pass.

---

## 5. The workflow, per transcript

Run this whole sequence for the first transcript, then repeat it for the next, through the phase. Then that phase's
master synthesis (Section 6), then the next phase, then the cross-phase synthesis (Section 7).

### Phase 1 (Pass A), Familiarization

Read the transcript in full before coding a line. Write `01-memo.md`: a 150 to 300 word memo on what this account
is about, its register, its contradictions, what surprised you; five to ten analytic noticings written as questions
rather than conclusions; the absences, meaning what this participant conspicuously does not say and what the
interviewer never asked; and the interactional conditions, meaning where the interviewer supplied vocabulary or
explained the study's premise, and where the participant is reasoning from a demonstration or a described scenario
rather than from practice.

For a Phase 2 transcript, add one line noting any relation the transcript itself states to another participant.
The household pairing map is unfiled, so a pairing is recorded only where the transcript states it, never inferred.

### Phase 2 (Pass A), Exhaustive candidate coding

Code the whole transcript. **Over-inclusive by design: nothing dropped, merged, or ranked here.** Expect **40 to 80
candidate codes** for a transcript of this length. Read `references/coding-guide.md` first.

Write `02-coding-table.md`:

| Turn / timestamp | Extract (verbatim, trimmed) | Code | Type | Analytic note |
|---|---|---|---|---|

Coding discipline, fully in the coding guide:

- **Codes are short: two to five words, six at the outside.** `Son deciphers prescription`, not a sentence. Nuance
  goes in the definition, reasoning in the analytic note.
- **Code the question-and-answer pair, but quote only the participant.** Many answers here are elliptical. Read the
  interviewer's turn to establish what the answer is about, recover the content, and state the participant's
  position in the code as if they had said it in full. The interviewer is never quoted anywhere; their turn is
  paraphrased in the analytic note. Where a bare answer is unreadable alone, put the recovered content inside the
  participant's quote in square brackets. Tag positions from closed or leading questions `[elicited]`.
- Multiple codes per extract are expected. Tag `[in-vivo]`, `[tr]` for a translated extract, `[hypothetical]` where
  the participant is reasoning about a scenario rather than reporting practice, `[believed-capability]` where they
  describe the agent doing something the deployed list in `/output/Method.md` does not include, and `[lived]` where
  a Phase 2 account concerns a deployed feature.
- **Code the third party.** When a participant describes what a son, a daughter, or a pharmacist did, that is
  network data, not background. It gets its own code, and the analytic note names whose account it is, since we
  have the older adult's version of the son's action and not the son's.
- Keep codes close to the data. Selection is Pass B, abstraction is Pass C.

**Pass A exit check:** the coding table is on disk; every code has a definition boundary, at least one attributed
verbatim participant extract, and a name of six words or fewer; the candidate count is recorded; no sub-theme or
theme name appears anywhere in the file.

### Phase 3 (Pass B), Trimming to 25 to 30 codes

Write `03-code-register.md`, holding **every** candidate code, each marked `RETAINED` or `PARKED` with a reason.
Nothing is deleted.

1. **Reconcile.** Merge synonyms, collapse near-duplicates sharing a mechanism, split codes doing two jobs even
   though that raises the count. Record the count after this step.
2. **Score** each survivor: RQ traction against the three RQs; mechanism, meaning it names something that happens
   rather than a topic that came up; corroboration within this transcript, meaning how many places it appears;
   evidence grade, volunteered against elicited or hypothetical; conceptual load, meaning what this account would
   specifically lose without it.
3. **Mark the affiliation practice**, where one fits: assignment, contestation, gifting, revocation, or ceremony
   (Section 3). Leave it blank rather than forcing a fit.
4. **Retain 25 to 30.** Park the instrument codes, the mechanism-less topic labels, the elicited-only codes with no
   unprompted appearance, the redundant, and the off-question. **Retain every code that cuts against the direction
   the analysis is heading**, even a thin one; trimming is where an inconvenient case would quietly disappear. The
   seeded tensions of AGENTS.md Section 9.3 are the ones most likely to be trimmed by accident: a code carrying
   delegated dependence read as agency, reminders strengthening felt timing without replacing memory, oversight
   read as intimacy, streak grief, or trust built through self-verification survives Pass B unless the register
   argues explicitly why not.
5. **Write the trim rationale** at the head of the file: counts at each step, which criteria did most of the
   parking, the two or three hardest calls with both sides stated.

Never trim by frequency. If the honest number is 23 or 33, take it and say why.

**Pass B exit check:** the register accounts for every candidate; the retained set is 25 to 30 or justified outside
it; every retained code carries its five criterion answers and its affiliation practice or a blank; merges and
splits are recorded with old names kept; no sub-theme or theme name appears.

### Phase 4 (Pass C), Sub-themes

Group **only the retained codes**. A parked code is not clustered; if one is needed, unpark it in the register with
a reason and log it. Cluster by shared meaning, not shared topic: two codes belong together when the same thing is
going on in them, not when they concern the same object. A code about a daughter reminding and a code about a son
checking the box belong together only if the same relational work is happening, and often it is not.

Write the sub-theme half of `04-themes.md`. Per sub-theme, in this order: **constituent codes** by exact name,
written first because they are the evidence; a **descriptive analytic name**; a **one-line definition** derived
from the constituent list; **what it excludes**; and the **RQ it speaks to**.

Fill the `Sub-theme` and `Reflexivity notes` columns of `05-matrix.md` here. The reflexivity note is written while
the grouping decision is being made, because its content is the decision and the alternative not taken.

**Pass C exit check:** every sub-theme lists constituent codes matching retained codes exactly; every retained code
sits in exactly one sub-theme or was reparked on the record; every retained row has a reflexivity note; no theme
name appears; sub-theme count is 4 to 8.

### Phase 5 (Pass D), Themes

Group sub-themes, never codes directly. Per theme: state the **central organizing concept in one sentence first**,
name the theme from it, **list the constituent sub-themes by exact name**, then write the definition and select
extracts from those already in the matrix. No new or altered quotes.

**Theme names are descriptive and analytic, not dramatic.** See Section 8.

Write the theme half of `04-themes.md`, with a development log of every split, merge, promotion, demotion, or
discard, and its reason. Then revalidate every reflexivity note against where its code actually landed; where a
note is now wrong, keep the original claim and append the correction. Fill the `Theme` column of `05-matrix.md`.

**Pass D exit check:** every theme has a one-sentence organizing concept and a constituent sub-theme list; every
sub-theme sits in one theme; theme count is 2 to 4; every reflexivity note is validated or corrected.

### Phase 6 (Pass E), Check

Short and adversarial, not a formality. Append to `04-themes.md`: walk the chain downward from each theme to its
sub-themes, codes, and extracts, and fix any link that will not walk; sample five extracts at random and ask
whether their code, sub-theme, and theme still fit; run `quote_check.py`; write the strongest counter-reading for
each theme and either say why it loses or concede it; and name the two parked codes closest to the line, either
unparking one or saying why the parking holds.

Where a transcript itself states a relation to another participant, add the paired check: for each episode both
narrate, state whether the accounts agree, and where they diverge, record the divergence as data rather than
resolving it toward the more plausible account. Without a stated relation there is no pair; do not infer one.

Then move to the next transcript.

---

## 6. The master synthesis, per phase

Runs after that phase's transcripts are complete. Reads `03-code-register.md`, `04-themes.md`, and `05-matrix.md`
from each transcript in the phase. It does not re-read transcripts except to check a specific extract.

**Pass A at master level.** Pool all retained codes from the phase's transcripts into `master/01-code-synthesis.md`,
recording which participants each came from. Expect roughly 600 to 720 pooled entries for Phase 1 (24 transcripts)
and 625 to 750 for Phase 2 (25 transcripts) before reconciliation; calibration, not quota.

**Pass B at master level.** Merge across transcripts first: the same code under different names in `P02` and
`C06` is one master code, and the merge is recorded with both original names. Then retain **at most 40 master
codes**, scored on: how many participants carry it; RQ traction; mechanism; evidence grade; conceptual load; and
its affiliation practice where one fits. Cross-transcript recurrence matters here in a way it cannot within one
transcript, but it is still not the criterion on its own: **a code from two participants that names a mechanism
beats a code from six that names a topic.** Park the rest with reasons. Every master code names its source
participants.

For each phase, record for each master code whether it appears in older adults' accounts, caregivers' accounts, or
both. A practice claimed by caregivers and unmentioned by older adults is a finding about the baseline, not a
sampling artifact to average away.

**Passes C and D at master level.** Sub-themes and themes over the master retained set, written to
`master/02-themes.md` with its development log. Target **3 to 5 themes, 6 to 12 sub-themes**. Each master theme
records: constituent sub-themes; the participants supporting it; its RQ; whether it clears the two-source rule or
carries `[single-instance]`; for Phase 2, whether it rests on `[lived]` or `[hypothetical]` codes; and which
per-transcript themes it draws on, so a reader can trace it back to a
transcript folder. Fill `master/03-matrix.md`.

**Pass E at master level**, written to `master/04-review.md`: the chain walks, a sample of fifteen to twenty
extracts across transcripts with its hit rate, the trim audit against the parked master codes, a counter-reading
per theme, participant concentration per theme, evidence grades per theme, and the quality checklist from
`references/quality-and-reflexivity.md`. Add the older adult against caregiver distribution per theme. For Phase 2,
add the evidence-status audit: how many themes rest on `[lived]` codes, how many on `[hypothetical]` alone. Then
write `master/05-reflexivity.md`.

---

## 7. What runs after the phase masters

### 7.1 The cross-phase affiliation synthesis

This is where the paper's argument is assembled, and it is the reason the affiliation practices are the shared
lens. Written to `cross-phase/`.

Read each phase's `master/03-matrix.md` and `master/02-themes.md`. Do not re-read transcripts except to check an
extract.

1. **`01-symmetry.md`.** For each of the five affiliation practices, tabulate what it looked like among humans in
   Phase 1 and what it looked like directed at the agent in Phase 2. Three columns: the human form, the
   agent-directed form, and what changed in the move. A practice present among humans and absent toward the agent
   is as much a finding as a match, and it is recorded in the same table rather than dropped for being empty.
2. **`02-themes.md`.** Cross-phase sub-themes and themes over at most 25 retained affiliation codes, with a
   development log. Target 3 to 5 themes. Each names the phases it draws on and clears the two-source rule across
   them, or carries `[single-instance]`.
3. **`03-matrix.md`.** The six-column table for the cross-phase retained set.
4. **`04-review.md`.** Pass E at this level, plus one specific audit: every cross-phase theme that touches
   allegiance or the care network states which phase carries it and whether its Phase 2 codes are `[lived]` or
   `[hypothetical]`. Any that rests on `[hypothetical]` codes alone is labeled as a claim about a described design.
5. **`05-reflexivity.md`.** The Theory Alignment block, the positionality statement, and where the data resisted.

Phases are never merged into one pooled corpus. They are different instruments answering different RQs, and the
comparison is the analysis.

### 7.2 No non-interview streams

The deployment produced no app or decision logs, probes, or vignettes that survive as data (AGENTS.md Section 3.3).
Interviews are the only Phase 2 record. Nothing is analysed in a `streams/` folder, and no theme cites a log.

---

## 8. Naming themes and sub-themes

**Academic and descriptive, not dramatic.** A theme name is a compact analytic statement a reviewer could quote in
a methods discussion without wincing. It names what is going on, in ordinary research English.

Rules:

- Six to twelve words. A noun phrase with a qualifying clause is the standard shape.
- No colon-plus-subtitle constructions, no quoted participant phrases as titles, no metaphor, no rhetorical
  contrast, no alliteration, no words like paradox, tension, dance, journey, battleground, or lens.
- The name states the concept, not its significance. Significance belongs in the definition and the report.
- Prefer precision to elegance. A slightly clumsy name that is accurate beats a memorable one that is vague.

| Dramatic, do not use | Descriptive, use |
|---|---|
| "My memory is very sharp": dignity under surveillance | Unaided remembering treated as evidence of competence |
| Who does the app really love? | Conditions under which families reassign the agent's allegiance |
| The streak that broke a heart | Loss of an accumulated streak described as a personal loss |
| Handing over the keys: dependence as freedom | Delegating oversight to an adult child as a display of trust |
| Lost in the family: the vanishing patient | Medication decisions made collectively rather than individually |

The same rule governs sub-theme names, one register plainer still, and code names, which stay at two to five words
(Section 5, Phase 2).

---

## 9. The final codebook

Generated at the end of the run from each phase's `master/03-matrix.md` and from `cross-phase/03-matrix.md`. Never
hand-written. Full column rules and the rendering constraints are in `references/code-theme-matrix.md`; read it
before generating. In summary:

`<slot>/FINAL-CODEBOOK.md` has a short header, then one section per unit that ran, in this order:

1. **Phase 1, the human affiliation baseline**, at most 40 codes, sorted by theme, then sub-theme, then code, with
   an `Older adult / caregiver / both` marker on each row.
2. **Phase 2, post-deployment**, its own table, every row tagged `[lived]`, `[elicited]`, or `[hypothetical]`, with
   the same older adult, caregiver, or both marker.
3. **Cross-phase affiliation synthesis**, at most 25 codes, its own table. This is the section the paper's
   conceptual contribution is built from, and it comes last because it depends on the two above.

A section for a phase that has not run is omitted, not stubbed.

One table each, six columns:

| Code | Definition | Sub-theme | Theme | Example quote | Reflexivity note |
|---|---|---|---|---|---|

**Keep it short and make it render.** These two failures are what makes a codebook unusable:

- **Cell length caps, enforced:** definition at most 20 words; one example quote, at most 25 words, with its
  participant id; reflexivity note at most 20 words and one sentence. Longer material stays in the working files,
  which the header points to.
- **Markdown table safety:** one line per row, no line breaks inside a cell, no bullet lists or block quotes inside
  a cell, every literal pipe inside a quote written as `\|`, every row with exactly seven pipes, and a blank line
  before and after the table. Run `table_check.py` and fix what it reports.

Also write `FINAL-REPORT.md` (Section 10) and `README.md`, six or seven lines: which agent produced this slot, what
the two FINAL files are, what the folders are, the current state, and the date of the last run.

---

## 10. The final report

Write `<slot>/FINAL-REPORT.md` at the top of your slot. **Read `references/report-template.md`** for the structure,
the claim to extract to interpretation to implication rhythm, quote conventions, and the "so what" standard.

It reports each phase's master themes in turn, then the cross-phase affiliation synthesis as the analytic payoff.
It states the coding trajectory in one sentence per phase with real numbers: candidates per transcript, retained per
transcript, master retained, sub-themes, themes. It answers "so what" for every theme, distinguishes what
participants said from what you read it as meaning, and states limitations plainly, each as a scoping decision
(AGENTS.md Section 6.2): one cultural setting; snowball recruitment through the team's networks; a two-week
deployment; self-report interviews rather than logged system data or health outcomes; four designed mechanisms
tested by description rather than by use; the agent's bounded autonomy; translation from Bangla; and that
caregivers' accounts of older adults and older adults' accounts of caregivers are both second-hand, with no pairing
map to set them against each other.

Two things the report must not do. It must not sand a disconfirming case smooth: the seeded tensions of AGENTS.md
Section 9.3 appear in the report with their counter-cases, not only in the working files. It must not extend a
claim past Bangladesh; the collectivist against individualist contrast is what travels, and the report says so in
those terms.

---

## 11. The why to how to decision habit

At every pass, whenever you would otherwise note that something occurs:

1. **Why is this here?** What is the participant doing with this utterance: justifying, hedging, repairing,
   performing competence, protecting a family member's standing, being courteous to a researcher?
2. **How does it work?** What mechanism or condition does it depend on, and where else in the corpus does that
   mechanism appear under different vocabulary, including in the other phase?
3. **What do I decide?** Refine, merge, split, retain, park, or promote, and record the reason.

Counts are bookkeeping and never license claims about importance. If you write "many participants", replace it with
an interpretation.

---

## 12. Output conventions

- Deliver units in order: a phase's transcripts, then its master, then the next phase, then cross-phase. Passes in
  order within each unit. Exit checks are checkpoints you report and cross, not stopping points.
- Quote verbatim. Elisions `[...]`, insertions `[in square brackets]`. Attribute by id, phase, and transcript line:
  `(P07, Phase 1, L112)`, `(C02, Phase 2, L41)`. Transcripts carry no timestamps. Never quote the interviewer or
  facilitator.
- The corpus was spoken in Bangla and reaches you in the filed English translation, lightly cleaned at source.
  State that once in each phase's `master/05-reflexivity.md` and do not clean further. Where a translation choice carries
  analytic weight, particularly a kinship term or an honorific, note it in the analytic note rather than
  substituting your own rendering.
- Do not edit anything in `/Supplementary/Interviews/` or `/output/Method.md`. If a transcript looks wrong, say so
  in the run report.

---

## 13. Run report

End the run with:

1. **Slot**: which slot this run wrote to, and how it was resolved (environment, `TA_SLOT`, or `--slot`).
2. **Deliverables**: paths to `<slot>/FINAL-CODEBOOK.md` and `<slot>/FINAL-REPORT.md`, and the headline finding in
   two or three sentences.
3. **Units completed**: every transcript, every phase master, cross-phase, with each one's counts: candidates,
   retained, sub-themes, themes.
4. **RQ source check**: confirmation the RQs came from `/proposal/proposal.md`, and any divergence from
   `/output/Introduction.md` if that file exists.
5. **Script results**: `quote_check.py`, `table_check.py`, `anon_scan.sh`, each with its output line.
6. **Pass and exit checks**: which passes ran per unit, and anything left pending with the reason.
7. **Pass E results**: sample hit rates, trim audits, counter-readings conceded, changes forced, and for Phase 2
   the evidence-status audit.
8. **Affiliation symmetry**: for each of the five practices, whether it appears among humans, toward the agent, or
   both, and the practices with no agent-directed instance.
9. **Quality checklist**: the items that failed or are pending.
10. **Tensions preserved**: which disconfirming cases survive in the report, not only in the working files.
11. **Scope flags**: every `[lived]`, `[elicited]`, `[hypothetical]`, `[believed-capability]`, and
    `[single-instance]` label, with a count.
12. **Placeholders**: every `[MISSING DATA: ...]` and `[BLOCKED: ...]`.
13. **Ledger updates**: rows added to or retired from `/analysis/theory-ledger.md`.
14. **Contradictions surfaced, not resolved**: where sources disagree, including where `/proposal/proposal.md`,
    `/output/Method.md`, and `/Supplementary/Interviews/` disagree (AGENTS.md Section 3), and the standing
    caregiver phase-participation conflict (AGENTS.md Section 3.2).

---

## 14. When the data are thin

For a scoped single-transcript run, say plainly what can and cannot be claimed: codes, sub-themes, and themes for
that account, not patterning across the corpus. That is what the master synthesis is for, and it cannot be
simulated from one transcript.

The same holds one level up. Phase 1 alone cannot answer RQ2 or RQ3, because it predates the agent; read RQ1 out
of it and say so. Phase 2 answers RQ2 and RQ3 only to the extent its codes are `[lived]`; a `[hypothetical]` code
answers how a family reasoned about a described design, never how it used one, and the report says which.
