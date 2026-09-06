# Plan for Section: Method

**Status:** live plan for the Method section. Supersedes `analysis/plans/Methodology.md`, which was written against a smaller filed corpus (nine transcripts, no Phase-2 data) and against a three-study architecture the user has since corrected.

**Revision 2, 2026-09-05.** Revision 1 was accepted with one structural objection: the architecture split the study's own logic across four subsections and never gave the prototype a home. This revision rebuilds the hierarchy to the user's specification. Study Design now carries the whole study, with formative interviews, prototype development, and post-deployment interviews as its three subsections; Participants and Recruitment carries sampling, eligibility, recruitment, and a demographics analysis; Data Collection carries the session procedures and absorbs corpus preparation; Data Analysis follows; ethics, consent, data handling, positionality, and scope close as one section.

---

## Directive Intake

**Directive verbatim (run 1):** "Method Organize this methodology for CHI. Do not make any claim or discussion to backup the motivation and novelty or justification of theoritical gap because these will cover in the Introduction and literarture review. Ask me one by one question where you need more justification before start writing."

**Directive verbatim (run 2, structural):** the Study Design section must cover the full study design context including the Formative Home Interviews, Prototype development, and post deployment Interviews, all three as subsections under Study Design; Participants and Recruitment must cover sampling strategy, recruitment, eligibility criteria, and participants with demographics analysis; Data Collection comes next and organizes corpus preparation under it; then Data Analysis; then Ethics, Consent, and Data Handling, Positionality and Scope as a section.

**Typed operations:**

- *Scope.* Method only, covering executed work. No motivation, novelty, or theory-gap justification anywhere in the section.
- *Structure.* Five sections in the order the user gave, with the three named subsections under Study Design and corpus preparation nested under Data Collection. This ordering is binding, not advisory.
- *Emphasis.* Organization and replicability. A reader reruns the study from this section alone. Demographics reported as analysis, not as a raw table dump.
- *Process.* Question the user one at a time before planning. Executed: ten questions asked and answered.
- *Output.* This plan file. No prose enters `/output/`.

**Phases changed by the directive:**

- **Phase 2 decomposition.** Rebuilt to the user's hierarchy. The template's own ordering is discarded.
- **Phase 3 theory.** Frameworks admitted only where they change a methodological decision. No framework may argue the paper's gap here.
- **Phase 4 literature sweep.** Reduced. The full 22-candidate Method sweep was run in a prior session and is filed in `analysis/plans/Methodology.md`; carried forward by reference. Adjusted target: zero new candidates, four rows retired, three promoted to required.
- **Phase 7 grilling.** Re-run against the new architecture.

**Blocked by the hard floor:** nothing.

**Standing prohibition that binds `/draft`:** no sentence in Method may argue that the approach is new, that prior work lacks it, or that a theoretical gap motivates it. Where a limit needs stating, state it as a scoping decision, never as a contrast against the literature.

---

## What the Question Round Established

Ten facts from the user, each correcting the repository or filling a gap it could not fill. They are the working record and must be filed as records before `/draft` runs.

| # | Question | Answer | Consequence |
|---|---|---|---|
| 1 | What did Phase-2 participants encounter? | Mixed: part lived, part elicited | Every Phase-2 domain splits into lived use and elicited judgment |
| 2 | Which behaviors ran on their phones? | Reminders, CRUD, streaks and heat map; family missed-dose notification; spoken allegiance announcement; request-and-grant with veto prompt | The filed feature report is stale; a current build record must be filed |
| 3 | Which were scenario probes only? | Risk-graded weakening veto; silence-as-participation; probationary mode; shared family scores | Four design propositions tested by elicitation, never deployed |
| 4 | Which roster is real? | 25: 17 medicine takers, 8 caregivers | CLAUDE.md Section 3.1's "26, with 9 caregivers" is wrong |
| 5 | Age eligibility | All medicine takers are older adults; four ages were wrong in the data | Corrected to 65, 71, 66, 66; range is 64 to 80 |
| 6 | Deployment length | Two weeks, uniform | Stated exactly, unhedged |
| 7 | Devices where there is no personal smartphone | Household smartphone counts as theirs | Device access reported at household level |
| 8 | Is Phase 2 the household study? | Yes | One study, two phases. Household is the unit; P and C records pair |
| 9 | Corpus preparation | Machine-drafted Bangla transcription and English translation, each fully verified by two Bangla-fluent researchers | Automation as drafting aid; tools to be named once filed |
| 10 | Team, guides, analysis | Three researchers (two researchers, one supervisor); filed guides are the real instruments; reflexive thematic analysis complete but artifacts unfiled | Executed analysis described; artifacts must be filed before Findings cite them |

---

## Data Corrections Applied

Made with the user's explicit instruction, each with a backup beside the original.

1. **Ages.** P11 60 to 65, P12 41 to 71, P13 46 to 66, P14 56 to 66. Applied in `participant.csv`, `demographsi.csv`, the Phase-2 headers, and the spoken Phase-1 lines. Backups `*.bak-age`.
2. **De-identification.** Every personal name in all 48 transcripts and in `demographsi.csv` replaced by its participant ID, including honorific forms and first-name address. Backups `*.bak-names`. Residual sweep clean.
3. **Device access.** New `Deployment_Device` column in `participant.csv`: own smartphone (9), household smartphone shared or proxy-operated (5), not specified (3). Backup `participant.csv.bak-device`. Phase-1 transcript statements about phone ownership left untouched, so the field records access rather than overwriting what participants said.

**Still to clean:** C01's transcript names an employer, a re-identifying detail; Phase-2 P08 and P14 originally carried the same personal name, so one is a copy error.

---

## Section Purpose

Let a reader reconstruct the study: how it was designed, who took part in what households, what they used for how long, how the data was produced, and how interpretations were made. The section establishes the evidentiary warrant for C1 and for the deployed half of C3, and it draws the line, once and clearly, between what participants lived and what they judged from description.

**Title:** *Method*.

**Design name, used consistently:** a two-phase qualitative household study with a prototype deployment between the phases.

**Target length:** 2,000 to 2,400 words excluding tables and any study-flow figure. Flat prose, short declaratives, exact figures, first person for research actions. At most two contrast frames in the section, both methodological, neither positional.

**Division-of-labour rule, binding on `/draft` so the two front sections do not duplicate each other.** Study Design states what each phase *is*, why it follows the one before, and what it can support. Data Collection states how the data was *produced*: session sequence, instruments in use, recording, deployment logistics, and the path from Bangla speech to analyzable English. If a sentence answers "what kind of evidence is this", it belongs in 4.1. If it answers "what did you do that day", it belongs in 4.3.

---

## Recommended Section Architecture

Five sections, thirty-six beats. Paragraph titles are working titles for `/draft`, not headings for the paper.

### 4.1 Study Design

**Purpose:** carry the whole study in one place, so no later section has to re-explain the arc.

1. **M1, "A two-phase household study with a deployment between the phases."** One sentence naming the design, then the arc in order: formative home interviews, analysis, prototype development, a two-week deployment, post-deployment interviews with the same households. Give the phase-to-RQ mapping compactly: Phase 1 answers RQ1; the deployment and Phase 2 answer RQ2 and RQ3. Not an experiment; no experimental vocabulary anywhere in the section.
2. **M2, "The household is the unit."** Both an older adult and, where a caregiver was enrolled, a family caregiver were interviewed about the same household across both phases. Name the paired subset by ID; claims about how a family negotiates the agent rest on it.
3. **M3, "Setting and language."** Sites in Bangladesh, urban and rural, sessions in Bangla in participants' homes. Bound every empirical claim to Bangladesh. Flat, one paragraph.

#### 4.1.1 Phase 1: Formative Home Interviews

4. **M4, "Aim and interview domains."** What the phase was for, then the domains from the filed guides: daily medication routine, artifacts and storage, disruptions and missed doses, device use and who operates it, reading and interaction conditions, the care network and handover, closing design reflection. Report domains; do not reproduce the guide's deficit-framed wording as the section's rationale.
5. **M5, "The caregiver branch."** The caregiver guide treats the caregiver as the participant rather than as a reporter on someone else, and records each answer's referent: the caregiver's own experience, their account of the older adult's, or a joint household account. A real methodological choice; it belongs in the design, not in a procedure footnote.
6. **M6, "What Phase 1 supports."** Current practices and expressed design concerns, and the requirements the prototype was built against. It establishes nothing about how the system behaved.

#### 4.1.2 Prototype Development

7. **M7, "From Phase-1 interpretations to design requirements."** How analysis of Phase 1 became a requirement set, and who made that conversion. Point to the traceability table rather than restating findings inside Method. Source: `Supplementary/Interviews/medical_app_feature_report(1).md`, which records recurring interview requirements and the features built against them.
8. **M8, "What was built."** The build participants used for two weeks: medicine setup and editing, scheduled reminders carrying medicine name and timing, streaks, logbook, daily heat map, missed-dose notification to a family member, a spoken announcement in Bangla of whom the agent was currently serving, and a request-and-grant prompt before involving a family member, which the older adult could decline. Each item traces to the current build record, which must be filed. State the agent's autonomy exactly: which decisions it took on its own, which followed fixed rules, which waited for human confirmation.
9. **M9, "What was not built."** Four mechanisms named in the design did not reach the deployed build: the risk-graded weakening veto, silence read as patterned participation, probationary mode as an onboarding feature, and shared family scores. State this here, in the flattest sentence in the subsection, before any Phase-2 material appears anywhere in the paper.
10. **M10, "Design decisions and what was deferred."** Who decided, how competing interpretations were resolved, which requirements were deferred or rejected and why, and how the care-network framing constrained the build. A requested feature does not become a finding because the prototype implemented it.

**Required design-traceability table.** Columns: Phase-1 evidence, analytic interpretation, design requirement, built element, deployment status, Phase-2 probe. Every row cites a Phase-1 transcript or an analysis artifact. Rows for the four unbuilt mechanisms carry deployment status "not built, elicited only".

#### 4.1.3 Phase 2: Post-Deployment Interviews

11. **M11, "Aim, window, and who was interviewed."** Interviews with the same households after a two-week deployment, in the same homes, in Bangla, following the filed Phase-2 guides. Both the older adult and the enrolled caregiver were interviewed about the same period. Two weeks for every household, exact and unhedged.
12. **M12, "Two kinds of question, kept apart."** The load-bearing beat of the section. Some questions asked participants to recount what the agent did: its announcements, its request to involve a family member, their refusals, the alerts their family received. Others described a mechanism that was not in the build and asked what participants would make of it. State the split, point to the table, and commit to labeling every Phase-2 claim accordingly. Carries contrast frame 1: accounts of use rather than reactions to a description.
13. **M13, "What Phase 2 supports."** Lived questions support claims about how households handled the agent's declarations, requests, refusals, and alerts over two weeks. Elicited questions support claims about how families reasoned about proposed mechanisms. Neither supports claims about health outcomes or about use beyond two weeks.

**Required lived-versus-elicited table.** Columns: Phase-2 guide section, mechanism, status in the deployed build, evidential status of participants' answers. Eight rows minimum, one per mechanism named in intake answers 2 and 3. `/draft` may not omit it.

### 4.2 Participants and Recruitment

**Purpose:** one auditable account of who took part, and what the sample's composition means for the claims.

14. **M14, "Sampling strategy."** The strategy as executed, named plainly, with the logic that households rather than individuals were the sampling target and that a caregiver was sought alongside the older adult wherever one did the medication work.
15. **M15, "Eligibility criteria."** Inclusion: adults 64 and over managing a daily long-term medication regimen at home; family members doing medication work for a co-resident older adult. State exclusions. State how age and regimen were established.
16. **M16, "Recruitment and household enrolment."** How households were reached, who approached them, how the older adult and the caregiver in one household were enrolled together, how prior relationships between team and participants were handled, and how many households were approached relative to those enrolled.
17. **M17, "Who took part."** Exact figures once: 25 participants, 17 medicine takers and 8 family caregivers, across N households. Point to the participant table. State phase participation, including any incomplete records.
18. **M18, "What the sample looks like."** The demographics analysis the directive asks for: not a table restated in sentences, but the composition that matters for the claims. Draw on the corrected demographics files. Age 64 to 80, mean 69.4, median 68. Gender near-even among medicine takers, 9 women and 8 men, and even among caregivers, 4 and 4. Caregivers skew young, six of the eight in their twenties or early thirties, and stand in varied kin positions: adult daughters and sons, a daughter-in-law, grandchildren. Regimen complexity spans a single daily medicine for five participants to eight or more for five others, with one participant taking thirteen across three dose times. Fourteen of the 17 report family caregiver support and three report only minimal support. Only one participant used a phone alarm before the deployment. Most report missing or delaying doses, two report missing only when stock runs out. Reading and interaction conditions are consequential: several cannot read handwritten prescriptions or small text, and most prefer voice with large text. Device access before deployment ranges from a laptop and smartphone to a calls-only handset, and nine ran the app on a personal smartphone while five used a household one. **Each figure is cited from `participant.csv` and `caregiver.csv` as corrected in this session, never from memory, and the coarse-quantifier vocabulary of CLAUDE.md Section 5.6 applies outside the exact counts.**
19. **M19, "Compensation and participation burden."** Compensation, travel, scheduling, accommodations. If there was none, one plain sentence saying so.

**Required participant table.** Columns: ID, role, household ID, age, gender, daily medicines and dose times, device access during deployment, phase participation. No diagnoses beyond what the analysis uses.

**Required household pairing table.** Columns: household ID, medicine-taker ID, caregiver ID, relationship. The user holds this mapping; it is not in the repository. Every paired-account claim depends on it, so it blocks M2 and M17.

### 4.3 Data Collection

**Purpose:** how the data was produced. Procedures only; the design logic stays in 4.1.

#### 4.3.1 Phase 1 Sessions

20. **M20, "The formative session, in order."** Consent, environment observation, interview, artifact walkthrough where the participant demonstrates the routine rather than describing it, closing reflection. Facilitator count, recording, field notes, language, location, and session duration.
21. **M21, "What was observed rather than asked."** The guides direct observation of storage locations, lighting and noise, analog aids in use and analog aids abandoned, and device handling during a live demonstration. Report what the team actually recorded, and distinguish it from what the protocol invited.

#### 4.3.2 Deployment

22. **M22, "Installation and onboarding."** Who installed the app, on whose device, what setup involved, what participants were told about the agent's role announcements, and how long onboarding took.
23. **M23, "Devices and household operation."** Nine participants used a personal smartphone and five used a household one, with a relative operating parts of the setup. Report proxy and shared-device operation as the deployment condition it was, not as noise or as an accommodation for deficit.
24. **M24, "What the deployment produced."** State exactly which records exist from the two weeks. If the only Phase-2 evidence is the interviews, say so plainly here, because the design promised decision logs and a reader will look for them.

#### 4.3.3 Phase 2 Sessions

25. **M25, "The post-deployment session, in order."** Session sequence, who was present, whether the older adult and caregiver were interviewed separately or together, recording, language, and duration.
26. **M26, "How the questions were asked."** The guides ask for the last actual occurrence rather than the general case, which is why the transcripts carry episodes. Disclose that several probes name an interpretation before requesting a response, and state the commitment to separate spontaneous accounts from prompted agreement in analysis.

#### 4.3.4 Corpus Preparation

27. **M27, "The Bangla recording is the source."** Sessions ran in Bangla; the verified Bangla transcript is the canonical record. State which language coding was done in and how code-switching was handled.
28. **M28, "Machine drafting with full human verification."** Automatic speech recognition produced a Bangla draft and machine translation an English draft. Two Bangla-fluent researchers checked each complete transcript against the audio and each English rendering against the Bangla, correcting errors and omissions. Name tools and versions. Report how disagreements and inaudible passages were resolved.
29. **M29, "Automation drafted; researchers decided."** One flat landing sentence: no automated system participated in coding or interpretation. Carries contrast frame 2, drafting aid rather than analytic authority, and it is the section's last frame.
30. **M30, "Kinship terms, honorifics, and idiom."** How address forms and culturally specific expressions were preserved or annotated, since the paper's argument runs on relational language.

### 4.4 Data Analysis

31. **M31, "Reflexive thematic analysis and its stance."** Name Braun and Clarke's approach, the epistemological position, the semantic and latent balance, and inductive-first then RQ-aligned coding. Themes are constructed by the analysts; never write that themes emerged.
32. **M32, "Familiarization and coding."** Repeated reading, memoing, independent initial engagement by the two researchers, then iterative coding with the supervisor. State plainly that discussion deepened interpretation and was not used to compute agreement, and give the reason from the approach rather than from convenience.
33. **M33, "Building and naming themes."** How candidate themes were built, checked against transcripts, revised, bounded, and named, and when the Bangla source was revisited.
34. **M34, "Analysis across phases and within households."** Whether Phase 1 was analyzed before the prototype was built, how Phase-2 material was coded, and how the older adult's and the caregiver's accounts of the same household were read against each other. Phase-1 findings, design decisions, and Phase-2 responses stay separable rather than merged into one corpus.
35. **M35, "Negative cases and analytic records."** How disconfirming cases were retained, and which artifacts exist: memos, codebook, theme map, decision trail. Give the stopping rationale without claiming saturation.

### 4.5 Ethics, Consent, Data Handling, Positionality, and Scope

**Purpose:** the conditions under which the data was produced and interpreted, and the limits of what it supports. The flattest prose in the paper.

36. **M36, "Approval and consent in a shared home."** The approving body and protocol identifier, consent mode, recording consent, withdrawal, and how consent was handled with other family members present. Consent in a shared household is itself a design; report it as one.
37. **M37, "Automated processing, anonymization, and storage."** What participants were told about automated transcription and translation, where processing happened and under what retention terms, how identifiers were removed, how the identity key is held, storage and retention.
38. **M38, "The research team and its position."** Three researchers: two who conducted interviews, verification, and coding, and one supervisor. Their relationships to Bangladesh, to Bangla, to caregiving, and to the participants, reported only where each changed recruitment, interviewing, translation, or interpretation. No demographic inventory detached from consequences.
39. **M39, "Scope."** One setting; households reached through the team's recruitment route; a two-week window; self-report interviews rather than logged system data or health outcomes; four designed mechanisms tested by description rather than by use. End on the last real limit, with no summary sentence.

---

## Theory Alignment

Per CLAUDE.md Section 10, and constrained by the directive: theory appears only where it changes a methodological decision, and never to argue the paper's gap.

### Primary 1: Reflexive thematic analysis (Braun and Clarke)

**Ledger status:** committed, row exists. **Carries:** M31 to M35.

Constructs: researcher subjectivity as resource, recursive coding, themes as constructed patterns, methodological coherence. **Work it does:** it decides M32. Under this approach, two analysts reading independently and then arguing is analytic depth; under the rival it is an untested reliability claim. Delete the framework and M32 has no principled answer to a reviewer asking for an agreement statistic.

**Rival:** coding-reliability thematic analysis. Loses because the executed process sought interpretation rather than stable code application; importing agreement metrics after the fact would misdescribe the work.

### Primary 2: Prototype as filter and elicitation object

**Ledger status:** `[PROPOSED, not yet in ledger]`. **Carries:** M7 to M10, M12, M13.

Constructs: prototype filtering, manifestation, scope, experienced qualities. **Work it does:** it produces the lived-versus-elicited table and the traceability table. Without it, M12 collapses into a generic sentence about semi-structured interviews, and four unbuilt mechanisms quietly acquire the evidential status of deployed ones.

**Rival:** usability evaluation framing. Loses because no tasks, success measures, or performance protocol were used, and the guides ask for meaning and legitimacy rather than performance.

### Primary 3: Translation as interpretive work

**Ledger status:** `[PROPOSED, not yet in ledger]`. **Carries:** M27 to M30.

Constructs: visibility of translation, source-language meaning chain, translator positionality, documented decisions for non-equivalent terms. **Work it does:** it makes the verified Bangla transcript the analytic source rather than the English rendering, and it requires M30 to exist at all. Delete it and machine-drafted English silently becomes the data.

**Rival:** back-translation as a validity check. Loses because semantic equivalence does not preserve relational and contextual meaning, and the executed process was bilingual side-by-side review.

### Supporting

- **Relational research ethics** [44]: carries M36 only, where familial presence during consent is reported as a designed practice rather than a form.
- **Asset-based community development** [60]: named once, in M14 or M15, as the sampling stance. Never claimed as a contribution.
- **Intermediated use** [98], [33], [1]: carries M23, where household and proxy operation is reported as the deployment condition. Cited because it changes how the beat is written.
- **Articulation work** [106]: available for M5, where recording each answer's referent treats the caregiver's coordination labour as the object of study. Use only if it changes the sentence; otherwise drop it.

### Legitimately atheoretical beats

M3, M11, M16, M17, M19, M20, M22, M24, M25, M37. Exact procedural reporting carries them. Attach no citation.

### Ledger rows for `/draft` to add

```text
Prototype filtering; manifestation; experienced qualities | Prototyping theory | LimStoltermanTenenberg2008, BuchenauSuri2000 | Method 4.1.2, 4.1.3 | Forces the lived-versus-elicited split and bars unbuilt mechanisms from carrying use claims
Translation as interpretive work; source-language meaning chain | Cross-language qualitative research | TempleYoung2004, Squires2009, VanNesEtAl2010, WongPoon2010 | Method 4.3.4 | Keeps the verified Bangla transcript analytically primary and requires a documented decision trail for English renderings
```

Both citation groups are unfiled candidates; verify and add to `references/reference.bib` before `/draft` cites them.

---

## Literature

**Adjusted target, directive-driven:** no new sweep. The full Method sweep was run in a prior session; its 22 verified candidates are filed in `analysis/plans/Methodology.md` and carried forward by reference. `references/` holds 122 verified entries, so the paper-wide 100-work target is met and the gap is zero.

*Promoted to required (the section cannot be written correctly without them):*

1. `LimStoltermanTenenberg2008Prototypes`, TOCHI 2008. Carries M8, M9, M12. Requires the draft to state fidelity, scope, and which qualities were available for judgment.
2. `Squires2009CrossLanguage`, International Journal of Nursing Studies 2009. Carries M27 to M30. Reporting requirements for a two-language corpus.
3. `SamuelWassenaar2025AITranscription`, JERHRE 2025. Carries M37. Consent and disclosure obligations created by machine processing of interview audio.

*Retired:* `VinesEtAl2013Participation`, `FrauenbergerEtAl2015Rigour`, `ZimmermanEtAl2007RtD` served a design-derivation narrative that would drift into the novelty argument the directive excludes; `LevittEtAl2018JARSQual` duplicates `OBrienEtAl2014SRQR`.

*Unchanged and still required:* the Braun and Clarke set for M31 to M35, `OBrienEtAl2014SRQR` as a completeness audit, `TempleYoung2004Translation`, `VanNesEtAl2010Language`, `WongPoon2010Translation`, `YunusEtAl2022TranslationReporting`, `KoeneckeEtAl2020ASR`, `BuchenauSuri2000Experience`.

Filed entries usable now: [15], [16], [93] reflexive thematic analysis; [75], [103] reflexivity and positionality; [44] relational ethics; [60] asset-based stance; [98], [33], [1] intermediated use; [106] articulation work; [61], [9] practice turn.

**Citation density.** Method is not a load-bearing synthesis section under the directive, which removes positioning argument from it. The two-source rule applies to M12, M28, and M31, the three beats that make a methodological argument rather than a report. Each has two or more sources above.

---

## Evidence-Mapped Outline

| Beat | Move | RQ / contribution | Source or gate | Framework | Protection |
|---|---|---|---|---|---|
| M1 | Name the two-phase design and the arc | All; C1, C3 | Intake 8; `proposal/proposal.md` Section 1 `[DIRECTIVE]` | Atheoretical | No experimental vocabulary |
| M2 | Household as unit; name paired subset | RQ2; C1 | `[BLOCKED: pairing map not filed]` | Atheoretical | Care network rather than lone user |
| M3 | Setting and language | All | Transcripts; demographics (Dhaka, Bogra, village sites) | Atheoretical | Claims bounded to Bangladesh |
| M4 | Phase-1 aim and domains | RQ1; C1 | `phase-1/interview_questions.md`, `phase-1/caregiver_interview_question.md` | Practice turn [61], [9] | Report domains, not the guide's deficit wording |
| M5 | Caregiver as participant, referent recorded | RQ1; C1 | `phase-1/caregiver_interview_question.md` header | Articulation work [106], if it changes the sentence | Caregiver is not a proxy reporter |
| M6 | Delimit Phase 1 | RQ1 | Corpus | Atheoretical | Phase 1 says nothing about the agent |
| M7 | Findings to requirements, traceably | RQ1, RQ3; C1, C3 | `medical_app_feature_report(1).md`; `[MISSING DATA: design-decision record]` | Prototype filtering | Phase-1 evidence not retrofitted to the build |
| M8 | What was built, with autonomy stated exactly | RQ2, RQ3; C3 | Intake 2; `[BLOCKED: current build record; feature report is stale]` | Prototype filtering | No capability claim beyond the filed build; "agentic" never outruns the log |
| M9 | What was not built | RQ3; C3 | Intake 3 | Prototype filtering | Four mechanisms named as unbuilt before any result appears |
| M10 | Who decided; what was deferred | RQ3; C3 | `[MISSING DATA: design meeting record]` | Prototype filtering | A requested feature is not a finding |
| M11 | Phase-2 aim, window, participants | RQ2, RQ3 | Intake 6; `phase-2/` guides; 24 transcripts | Atheoretical | Two weeks, exact |
| M12 | Lived versus elicited, stated and tabled | RQ2, RQ3; C1, C3 | Intake 1, 2, 3 | Prototype as elicitation object | Contrast frame 1; bars unbuilt mechanisms from use claims |
| M13 | Delimit Phase 2 | RQ2, RQ3 | Intake 1, 3, 6 | Prototype theory | No health outcomes; no claims past two weeks |
| M14 | Sampling strategy | RQ1 | `[MISSING DATA: written strategy]` | Asset-based stance, named once | Households, not individuals |
| M15 | Eligibility criteria | RQ1 | `participant.csv`, `caregiver.csv` as corrected; `[MISSING DATA: written criteria]` | Atheoretical | Regimen and care role, not deficit |
| M16 | Recruitment and household enrolment | All | `[MISSING DATA: recruitment record]` | Atheoretical | Prior relationships disclosed |
| M17 | Exact sample, once | All | `participant.csv` (17), `caregiver.csv` (8); intake 4 | Atheoretical | 25, never 26; no quantifier inflation |
| M18 | Demographics analysis | RQ1, RQ2 | `participant.csv`, `caregiver.csv` as corrected `[DIRECTIVE]` | Atheoretical | Composition read for what it does to the claims, not restated as prose table |
| M19 | Compensation and burden | All | `[MISSING DATA]` | Atheoretical | Say plainly if none |
| M20 | Phase-1 session, in order | RQ1 | Guides; transcripts; `[MISSING DATA: durations, dates, facilitator count]` | Atheoretical | None |
| M21 | Observation as executed | RQ1 | Guides Phase 1, 3, 5, 7; `[MISSING DATA: field notes]` | Atheoretical | Protocol intent not passed off as execution |
| M22 | Install and onboarding | RQ2 | `[MISSING DATA: who installed, what was said]` | Atheoretical | Onboarding framing shapes later trust talk |
| M23 | Devices and household operation | RQ2 | `Deployment_Device` column, added this session | Intermediated use [98], [33], [1] | Proxy use as condition, not deficit |
| M24 | What the deployment produced | RQ2 | `[BLOCKED: confirm whether app logs exist]` | Atheoretical | Say plainly if interviews are the only record |
| M25 | Phase-2 session, in order | RQ2, RQ3 | 24 transcripts; `[MISSING DATA: durations, separate or joint]` | Atheoretical | None |
| M26 | Probe anchoring and leading probes | RQ2, RQ3 | `phase-2/interview_questions.md` Sections 1, 3, 4, 5 | Reflexive method | Spontaneous accounts separated from prompted agreement |
| M27 | Bangla source; coding language | All | Intake 9; `[MISSING DATA: written protocol]` | Translation as interpretive work | Participant meaning stays upstream |
| M28 | Machine drafting, full verification | All | Intake 9; `[MISSING DATA: tool names, versions]` | Translation theory; ASR bias precedent | Two verifiers, complete passes, not spot checks |
| M29 | Machines drafted, researchers decided | All | Intake 9, 10 | RTA coherence | Contrast frame 2 |
| M30 | Kinship terms, honorifics, idiom | All | `phase-1/caregiver_interview_question.md` header; `[MISSING DATA: decision log]` | Translation theory | Relational language preserved |
| M31 | RTA and its stance | All; C1 | [15], [16], [93]; intake 10 | Reflexive thematic analysis | Never "themes emerged" |
| M32 | Familiarization and coding by three | All | Intake 10; `[MISSING DATA: memos]` | RTA | No agreement statistic; reason given |
| M33 | Theme construction and naming | All | `[MISSING DATA: theme map, codebook]` | RTA; translation theory | Bangla revisited at theme stage |
| M34 | Across phases and within households | RQ1, RQ2 | `[MISSING DATA: analysis timeline]`; pairing map | RTA | Phases and parties kept separable |
| M35 | Negative cases and records | All | `[MISSING DATA: negative-case register]` | RTA | Tensions retained; no saturation claim |
| M36 | Approval and consent in a shared home | All | Intake IRB answer; `[MISSING DATA: body, protocol number]` | Relational ethics [44] | Individual consent inside collective care |
| M37 | Automated processing, anonymization, storage | All | This session's de-identification; `[MISSING DATA: vendor terms, retention]` | `SamuelWassenaar2025AITranscription` | Identity key never exposed |
| M38 | Team and positionality in practice | All | Intake 10; `[MISSING DATA: relationships to setting]`; [103], [75] | Reflexivity | Consequences, not an inventory |
| M39 | Scope | All | This plan's audit | Atheoretical | Flattest prose; ends on the last real limit |

**Tension protection.** Method reports no findings, so the seeded tensions of CLAUDE.md Section 9.3 appear here only as analytic commitments in M35, plus the design facts that decide whether each is claimable at all. *Trust through self-verification* is claimable, because probationary testing was participant-initiated during a real two-week deployment, but M9 must record that probationary mode was not a built feature. *Streak grief* is claimable, because streaks and the heat map were deployed. *Shared family scores* is elicited only and may carry no use claim. *Delegated dependence as agency* now has lived evidence available, because the request-and-grant prompt ran, so M8 and M12 must be exact enough for Findings to rest on it.

---

## Pre-Flight Gate Check

1. **Contribution gate: pass.** 4.1.1 and 4.2 warrant C1's formative half; 4.1.2, 4.1.3, and 4.3 warrant C1's negotiation half and the deployed part of C3. M9 and M12 keep the undeployed part of C3 out of the empirical column. C2 is Discussion work and is correctly absent.
2. **RQ gate: pass.** Every empirical beat maps to RQ1, RQ2, or RQ3. RQ2 is genuinely served, because the allegiance announcement, the request-and-grant prompt, the veto, and family notification all ran for two weeks. No beat answers a retired question.
3. **Evidence gate: conditional.** Every beat has a filed source, a recorded user fact, or an explicit gate. Counts corrected to 25 and no longer match CLAUDE.md Section 3.1, flagged for the user. Six blockers remain, listed below.
4. **Theory gate: pass.** Three frameworks, each changing a specific decision, each surviving the enforcement test. Two ledger rows named for `/draft`.
5. **Framing gate: pass.** No beat frames an older adult as a deficit to repair. Household is the unit throughout. M8 and M9 keep capability claims inside the build. No priority claim, and per the directive no positioning claim.
6. **Tension gate: pass.** M9, M12, and M35 carry the method-level protections; claimability of each tension is stated.
7. **Transcendence gate:** not applicable to Method, and excluded by the directive.
8. **Directive gate: pass.** Run-1 operations: organize-only scope, standing prohibition on motivation and novelty, paragraph hierarchy, ten sequential questions, reduced sweep with the adjustment recorded. Run-2 operations: Study Design carries all three phases as subsections (4.1.1, 4.1.2, 4.1.3); Participants and Recruitment carries sampling (M14), eligibility (M15), recruitment (M16), and demographics analysis (M18); Data Collection follows and nests corpus preparation (4.3.4); Data Analysis follows (4.4); ethics, consent, data handling, positionality, and scope close as one section (4.5). Section order is exactly as specified.
9. **Literature density gate: pass at the adjusted target.** Three rows promoted, four retired, the rest carried forward. The three argumentative beats each have two or more sources.

---

## Plan Grilling Session

### Directive compliance check

Both directives satisfied; no operation blocked. Run-2 ordering is reproduced beat for beat in the architecture above, and the division-of-labour rule in Section Purpose exists specifically to keep 4.1 and 4.3 from duplicating each other, which is the failure mode a design-plus-collection split invites.

### R1, domain expert in aging, care, and computing in the Global South

1. **Device access nearly read as a deficit.** An earlier version framed household smartphone use as an accommodation for participants who lacked phones. That inverts the paper's own framing: proxy operation is the care arrangement the agent joined. **Fixed:** M23 reports it as a deployment condition and carries the intermediated-use citation because the citation changes how the beat is written.
2. **The caregiver branch was invisible.** **Fixed:** M5 sits in Study Design, not in a procedural footnote, because treating the caregiver as a participant is a design choice.
3. **Demographics analysis risked becoming a deficit inventory.** Listing literacy, eyesight, and device limitations as a list of what participants cannot do would violate the framing commitments. **Fixed:** M18 reports reading and interaction conditions as conditions the design had to meet, and reports device access as household access, next to the caregiver support figures that show the assets the household already holds.
4. **Rejected as a false alarm.** A demand to drop the Phase-1 guide's accessibility and literacy domains. Those domains produced the conditions M18 and M23 depend on. The retired accessibility research question may not organize findings; the interview domain was really asked and is legitimately reported.

### R2, methods and evidence hawk

1. **The stale build record.** The only filed system document says family missed-dose notification is not implemented; the user confirms it ran. **Fixed:** M8 is gated `[BLOCKED]` until a current build record is filed. Top blocker on the section.
2. **Four unbuilt mechanisms appear throughout the Phase-2 transcripts as though used**, because the guide's wording presents them that way. Largest fabrication risk in the paper. **Fixed:** M9, M12, M13, M26, and the required lived-versus-elicited table.
3. **Paired-account claims had no mapping.** **Fixed:** M2 and M17 gated on the household pairing table.
4. **Count contradiction.** Resolved to 25 by the user; CLAUDE.md Section 3.1 flagged for correction rather than silently overridden.
5. **Analysis claimed complete with nothing filed.** **Fixed:** M32 to M35 gated on the artifacts being filed.
6. **New defect found in this revision: the deployment's own records were never audited.** The design promised decision logs, and a reader reaching 4.3.2 will look for them. Nothing in the repository shows they exist. **Fixed:** M24 added and gated, so the draft must state plainly whether interviews are the only Phase-2 record.
7. **New defect: M18 invites rounding.** A demographics paragraph is where exact figures usually decay into "most" and "the majority". **Fixed:** M18 carries an explicit instruction that every figure is cited from the corrected files and that the coarse-quantifier vocabulary applies only outside the exact counts.
8. **Rejected as a false alarm.** A demand for inter-rater reliability. Under the stated approach, agreement statistics would misdescribe what was done; M32 says so and gives the reason.

### AC, meta-reviewer against the Best Paper Standard

1. **The strongest methodological move risked staying implicit.** A study that deploys part of its design, elicits judgments about the rest, and says exactly which is which is more honest than most CHI deployments. **Fixed:** M12 is the load-bearing beat of 4.1.3 with a required table.
2. **The new hierarchy risked a redundant Data Collection section.** With all three phases described in 4.1, a reader could hit 4.3 and find the same content again. **Fixed:** the division-of-labour rule in Section Purpose, and the beats in 4.3 are written as procedures only.
3. **Prototype development risked drifting into the novelty argument.** A subsection about building a system is where a Method quietly starts justifying itself. **Fixed:** M7 to M10 report derivation, contents, and exclusions; the standing prohibition forbids the justification, and three literature rows were retired for pulling in that direction.
4. **Theory risked decoration.** Enforcement rule applied to all three frameworks before drafting; each changes a decision. [106] on M5 is marked conditional for exactly this reason.
5. **The scope paragraph risked a quality-claim ending.** **Fixed:** M39 ends on the last real limit, with no summary sentence.

### Post-grilling verdict

The revised architecture produces a CHI-standard Method once six records are filed. No structural defect with a known fix remains. The evidence defects are unresolved because the repository does not hold the facts, not because the plan works around them.

---

## Standing Deliverable Report

**RQs served.** RQ1 through Phase 1 and its analysis. RQ2 through the deployed allegiance mechanisms across two weeks in paired households. RQ3 through both phases, split by the lived-versus-elicited line.

**Source files.** `Supplementary/Interviews/phase-1/` (16 medicine-taker and 8 caregiver transcripts, two guides); `Supplementary/Interviews/phase-2/` (17 medicine-taker and 7 caregiver transcripts, two guides); `Supplementary/Interviews/demographics/participant.csv`, `caregiver.csv`, `demographsi.csv` as corrected this session; `Supplementary/Interviews/medical_app_feature_report(1).md`, stale and superseded by a build record still to be filed; `proposal/proposal.md` for design intent; `analysis/theory-ledger.md`.

**Blockers, in clearing order.**

1. `[BLOCKED]` Current build record for the deployed version, listing which of the eight mechanisms shipped and stating the agent's autonomy per decision type. The filed feature report contradicts the user's confirmation and cannot be cited.
2. `[BLOCKED]` Household pairing map, caregiver ID to medicine-taker ID with relationship. Best filed as a `Household_ID` column in both demographics files.
3. `[BLOCKED]` Whether the deployment produced app or decision logs, or whether interviews are the only Phase-2 record.
4. `[BLOCKED]` Analysis artifacts: codebook, memos, theme map, negative-case register. Confirmed to exist; not in the repository.
5. `[MISSING DATA]` IRB approving body and protocol number.
6. `[MISSING DATA]` Transcription and translation tool names, versions, deployment mode, retention terms.
7. `[MISSING DATA]` Sampling strategy and eligibility criteria as written; recruitment route; session dates and durations; facilitator count; compensation.
8. `[MISSING DATA]` Who installed the app and how onboarding ran; what participants were told about the role announcements; device for P14, P15, P16.
9. `[MISSING DATA]` Design-decision record for M10: who decided, what was deferred or rejected.
10. `[MISSING DATA]` Researcher relationships to the setting, for M38.
11. **Corpus gaps:** no Phase-1 transcript for P14; no Phase-2 transcript for C05. Confirm whether those sessions happened.
12. **Data checks:** Phase-2 P08 and P14 originally carried the same personal name; C01's transcript names an employer.

**Resolved.** The monetized-points flag from CLAUDE.md Section 3.2: the filed feature record lists streaks, logbook, and heat map only, with no redeemable points, and the user's account of the deployed build does not include them. Treat symbolic streaks as the only deployed reward mechanism; confirm when the build record is filed.

**Contradiction to surface, not resolve.** CLAUDE.md Section 3 describes three studies with 26 formative participants and a six-person Study 2. The filed corpus and the user's answers describe one study, two phases, 25 participants, and a two-week household deployment that is itself the household study. `proposal.md`'s empirical arc describes that household study as future work. CLAUDE.md Sections 3.1, 3.2, 3.3 and `proposal.md` need updating by the user.

**Unresolved `[cite]` placeholders.** The carried-forward candidate table in `analysis/plans/Methodology.md`, minus four retired rows. Three are promoted to required and must be verified and filed before drafting: `LimStoltermanTenenberg2008Prototypes`, `Squires2009CrossLanguage`, `SamuelWassenaar2025AITranscription`.

This plan does not touch `/output/`. Running `/draft Method` turns it into prose, and it should not run until blockers 1 to 4 are cleared.
