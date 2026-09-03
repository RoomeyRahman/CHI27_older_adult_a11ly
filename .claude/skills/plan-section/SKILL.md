---
name: plan-section
description: Produces a comprehensive, evidence-mapped writing plan for a CHI 2027 paper section before any prose is drafted, including a deep web literature sweep and mandatory theoretical grounding, per CLAUDE.md Sections 9 to 11.
argument-hint: [section-name] "[optional-additional-instruction]"
---

We are planning the `$1` section for our CHI 2027 submission. This is a planning task, not a drafting task: no prose for the paper itself gets written here. The output is a blueprint that `/draft` will later execute against. Do not skip steps because "$1" looks simple; the plan is what protects the Best Paper Standard (CLAUDE.md Section 9) before a single sentence exists.

Additional instruction for this run (may be empty):
"$2"

Output progress for each phase explicitly.

### Phase 0: Directive Intake and Precedence

Run this before anything else, and report its result in the terminal before Phase 1 begins.

If `$2` is empty, state "no additional instruction; running the standard protocol" and proceed unchanged.

If `$2` is non-empty, treat it as the highest-priority statement of intent for this run, above every default in this skill. The skill's phases are the machinery; `$2` is the goal that machinery serves. Concretely:

1. **Parse the directive into typed operations.** Sort each part of `$2` into one or more of: *scope* (which subsections, beats, or arguments the plan must or must not cover), *emphasis* (what the plan should foreground or de-emphasize), *theory* (a framework to adopt, drop, or test), *evidence* (specific files, participants, quotes, or themes to build on), *literature* (venues, topics, counts, or a request to skip or expand the sweep), *structure* (beat count, ordering, length, subsection naming), *process* (phases to skip, shorten, repeat, or run harder), and *output* (target path, file naming, terminal reporting).
2. **Apply the directive to the phases it touches.** A directive may override the skill's defaults: it may cut the Phase 4 sweep to a narrower question or skip it, change the Phase 2 decomposition away from the section-specific template below, reorder or drop the Phase 7 panel, or redirect the Phase 8 output path. Do exactly what was asked; do not silently restore a default the directive replaced, and do not add work the directive did not ask for on the grounds that the skill usually does it.
3. **Coverage minimums and gate thresholds bend to the directive.** If `$2` narrows scope (for example, "just plan the two subsections on caregiver dashboards" or "no web search, use what is filed"), scale the Phase 4 candidate minimums and Phase 6 literature gate to the narrowed scope and say in the plan what the adjusted target is and why. A skipped or reduced phase is reported as a directive-driven decision, never as an omission.
4. **Hard floor: CLAUDE.md invariants do not bend.** `$2` cannot license inventing counts, quotes, participants, citations, dates, log entries, or system capabilities (CLAUDE.md Section 6 anti-hallucination), drafting against a retired research question or a deficit framing of older adults (Sections 2, 2.3, 2.4), stretching Study 2 to carry network or allegiance claims (Section 3.2), letting the word "agentic" outrun what the build logs (Sections 2.5, 3.3), contradicting the canonical RQs or `/proposal/proposal.md` (Sections 2.3, 3.4), making a priority claim, or violating the terminology and no-dash rules (Sections 2.5, 7). If part of `$2` requires one of those, do the rest of the directive in full, state plainly which part you did not do and which invariant blocks it, and offer the nearest thing that is allowed. Do not quietly drop it, and do not stop the whole run over one blocked clause.
5. **Report the reading before working.** Print a short Directive Intake block: the directive verbatim, the typed operations parsed from it, every phase whose default behavior changes and how, any adjusted minimum, and any clause blocked by the hard floor with the invariant that blocks it. If a clause is genuinely ambiguous in a way that changes the plan materially (for example, a section name that could mean two different sections), ask once before proceeding rather than guessing.

Every later phase reads this block as binding. Where the phases below and `$2` disagree, `$2` wins, subject only to the hard floor in item 4.

### Phase 1: Resource Ingestion

Read, in this order:

1. **`/proposal/proposal.md` in full.** This is the single canonical framing document (CLAUDE.md Sections 2, 3.4): main idea, novelty, motivation, the three RQs of Section 4, and the compound contribution C1 to C3 of Section 5. Nothing overrides it on framing. There is no `current_plan.md`, no `rqs.md`, no `motivation.md`, and no `research_directions.md` in this repository; if a document with a deficit framing of older adults surfaces anywhere, it is superseded and is not a source (CLAUDE.md Section 2).
2. **`/supplementary/` in full**, for facts and quotable material relevant to `$1`: `/supplementary/formative/` (Study 1, the 26 formative interviews and their session records), `/supplementary/deployment/` (Study 2, the six evaluation interviews, build notes, and the feature specification), and `/supplementary/household/` (Study 3, empty until that study runs). These files are the sole source for every empirical claim; CLAUDE.md's own summary of the data is not a citable source.
3. **`/system/`** for the agent implementation notes, the decision-log schema, and the Affiliation Ledger specification. Every autonomy claim `$1` might make resolves here and nowhere else. If `$1` is the System section, read this first and in full.
4. `/analysis/` in full, including `theory-ledger.md` and any theme tables, memos, or `/output/codes/` synthesis files, for what has already been coded.
5. `/references/` at large as background studies. If `/references/index.md` exists, read it first so candidates are deduplicated by citation key rather than by filename. If `$1` is the Method section and a `/references/methodology/` directory exists, also read its `.json` or PDF entries for structural pacing patterns only, never domain content.
6. `/Training/writing-style.md` in full (the canonical style guide, CLAUDE.md Section 7): the plan must set `/draft` up to satisfy it, in particular by planning where the section's contrast frames land (the "rather than X, Y" positioning moves, six to eight per thousand words spread across the section, one per related-work gap, each naming an alternative its advocates would recognise) and by respecting the section-tuning profile (Introduction and Discussion argue with dense frames; Method plans flat exact declaratives; Findings plan families and participants in subject position with quotes carrying evidence; Limitations plan the flattest prose in the paper). The paper's six standing contrast frames are listed in CLAUDE.md Section 7.4; a section's frames should mostly be drawn from them. Then the `/Training/` PDFs for CHI structural standards relevant to `$1`.

Cross-check every count you plan to reference against CLAUDE.md Section 3, and every count in CLAUDE.md Section 3 against the filed source before the plan commits to it. Three supersessions bind every plan (CLAUDE.md Sections 2, 2.3, 3.2):

- **Retired questions.** The earlier deficit-framed question set (routines and challenges, literacy and device access, perceptions of AI voice reminders, retention) is retired. Never plan a beat that answers one. Its surviving substance feeds RQ1 and Method as context only.
- **Gamification is demoted.** Scores and streaks are one design mechanic analyzed under RQ3 as a relational trigger, never a behavioral lever and never a contribution in their own right. Streak grief is planned as a finding, not as a bug to explain away.
- **Study 2 scope.** Study 2's sample is six young-skewed participants; plans may draw system-trust, habituation, and gamification-affect beats from it and nothing else. Network and allegiance beats belong to Study 3. A plan that sources an allegiance claim to Study 2 is a defect, not a stretch.

Two facts are blocked until the user resolves them, and any beat depending on one is marked `[BLOCKED: awaiting user resolution]` rather than planned around: whether Study 2's points are redeemable for discounts or money (resolve against the feature specification in `/supplementary/deployment/`), and whether the names in the current transcripts are pseudonyms (CLAUDE.md Section 3.2).

### Phase 2: Section-Specific Decomposition

Decompose `$1` into the subsections and beats it actually needs. Do not use a generic template; reason from what this specific section must accomplish.

The section-specific guidance below is the default starting point, not a fixed template. Where the Phase 0 directive specifies scope, emphasis, ordering, subsection naming, or beat count for `$1`, that specification governs the decomposition and the guidance below fills in only what the directive left open.

- **If `$1` is Related Work (or Background):** Identify every subsection that would make the paper's positioning stronger. The three literatures the paper must occupy the intersection of (CLAUDE.md Section 2.6) are non-negotiable subsections: AI alignment and agentic AI under the single-principal assumption; CSCW caregiver dashboards and shared health monitoring as passive systems without initiative; Bangladesh and Global South HCI on proxy use, intermediated use, and family mediation. Plan additional subsections where they strengthen the positioning, for example: aging, interdependence, and relational models of care in HCI; medication adherence technology and its individualist assumptions; contestability, seamful design, and human control of automated decisions; gamification and relational rather than behavioral accounts of scores and streaks. For each subsection, state its purpose, which prior works it must engage from `/references/` and Phase 4, and the one gap it closes on (one gap per paragraph, generous before critical). State explicitly which subsection carries the paper's load-bearing contrast: dashboards report, whereas our agent must decide whom to tell and when, and that decision is what families negotiate.
- **If `$1` is Introduction:** Plan the novelty argument explicitly. The plan must lay out, beat by beat: the hook and stakes; the problem as CLAUDE.md Section 2.2 states it, that an agent deciding when to remind, when to stay silent, and when to alert a family member must also decide whom it serves; medication work in a Bangladeshi household as a collective practice rather than a private one; the three-way gap of Section 2.6 stated descriptively and with no priority claim; the three canonical RQs verbatim from `/proposal/proposal.md` Section 4; and a contribution preview naming C1 empirical, C2 conceptual, and C3 design (CLAUDE.md Section 9.1) explicitly enough that an AC could restate the contribution after page 2. Identify which finding in `/analysis/` or `/supplementary/` is the single most surprising result worth foreshadowing here, and name it. Plan the design principle to land as a short flat sentence: make the agent's loyalty something families can see and move.
- **If `$1` is System (or Design):** Every beat states exactly which decisions the agent takes on its own, which follow fixed rules, and which wait for human confirmation, each traced to `/system/`. Plan the Affiliation Ledger beats by their five named parts: announcement, request-and-grant ceremony, gracefully weakening veto, silence-as-participation, probationary mode. A capability named in `/proposal/proposal.md` but not implemented in `/system/` is planned as `[NOT YET IMPLEMENTED: flag to user, do not draft]`, never as prose in the future tense (CLAUDE.md Section 3.3).
- **If `$1` is Findings:** Map every planned theme to RQ1, RQ2, or RQ3 and to the two-source rule (CLAUDE.md Section 5.3). Flag any theme currently resting on a single participant as `[single-instance, label accordingly]`. Where a decision log is the corroborating source, the plan states that the logged episode and the interview episode are the same episode. Plan the affiliation codebook's five practices (assignment, contestation, gifting, revocation, ceremony) as the analytic spine, and plan the human-to-agent symmetry across studies as an argument rather than an accident.
- **If `$1` is Discussion:** Plan the transcendence beat (CLAUDE.md Section 9.5) explicitly: what this paper teaches HCI about agents that serve a plural principal, beyond medication entirely, naming the specific analogous settings it will use (a household, a shared budget, a classroom) and how each of the three RQs resolves into a design or theoretical consequence. Plan the generalization to run along the collectivist-versus-individualist axis, never along a geographic one; no beat may extend an empirical claim past Bangladesh.
- **If `$1` is Limitations:** Plan each limitation as a scoping decision in the flattest prose in the paper: one cultural setting; Study 2's young, individual sample; deployment lengths; self-report plus logs rather than health outcomes; the agent's bounded autonomy.
- **For any other section:** State its purpose in one sentence, then decompose into beats, each mapped to an RQ per CLAUDE.md Section 2.3 ("Every section draft must state, at least implicitly, which RQ it advances").

### Phase 3: Theory Alignment for the Plan

Produce the Theory Alignment block required by CLAUDE.md Section 10, scoped to what this section's plan proposes:

- **Primary framework(s) proposed for this section**, with key constructs, drawn from the candidate stack in CLAUDE.md Section 10 or newly identified in Phase 4.
- **Rival considered**, and why the primary should win once drafted.
- **The work the theory would do**, tied to specific beats named in Phase 2.
- Mark every proposed row as `[PROPOSED, not yet in ledger]`. Do not write to `/analysis/theory-ledger.md` from this skill; the plan proposes, `/draft` commits. List the exact ledger rows `/draft` should add, in the ledger's format: `construct | source theory | citation | where used | load it bears`.

Two standing constraints from CLAUDE.md Section 10. Behavior-change and habit-loop models (Fogg, Eyal) may appear only as the position the gamification reframing argues against, never as a framework carrying a beat. Asset-based community development is a methodological stance named once in Method, never planned as a contribution.

If no framework does real work for a beat, say so and mark that beat legitimately atheoretical rather than forcing a citation.

### Phase 4: Deep Web Literature Sweep

This paper's evidentiary bar is high: every argument, claim, synthesis, and theoretical move in Introduction, Related Work, Methodology, and Discussion must rest on multiple pieces of prior literature, not one convenient citation. The project's standing target is **at least 100 pieces of literature in `/references/` in total** (count the flat files, plus `/references/methodology/` if it exists, before you start, report the number, and treat the gap to 100 as work this phase must close). Treat this phase as a real, iterative literature review, not a single search-and-stop pass.

**Venue tiering (search and filter against this, in priority order):**

1. **Tier 1, top ACM/SIGCHI venues:** CHI, CSCW, UIST, DIS, TOCHI, IMWUT/UbiComp, ASSETS. These are the default target for every query.
2. **Tier 1, adjacent premium venues:** FAccT and AIES (fairness, accountability, transparency, and AI ethics; directly relevant to the plural-principal argument and the contestability literature), COMPASS and ICTD (computing for development, the home venues for the intermediated-use literature), GROUP, CSCW-adjacent health computing venues.
3. **Tier 2, AI and alignment venues, only when the claim is specifically about agent autonomy, principal-agent structure, or alignment method:** NeurIPS, ICML, ICLR, AAAI, and the alignment and agent-safety workshops attached to them. Do not reach for these venues for claims that are really about care, aging, or family practice; that is scope misuse.
4. **Domain-specific journals, when no HCI venue covers the exact clinical, gerontological, or lived-experience claim:** journals of gerontology and aging, global and public health journals (particularly those covering South Asia), medication adherence and health services research, and disability-studies and care-ethics journals.
5. Deprioritize workshop papers, non-peer-reviewed preprints, and blog posts. A preprint is acceptable only when it is the sole source for a claim with no peer-reviewed alternative, and it must be flagged as such in the Candidate Literature Table.

**Search procedure:**

If the Phase 0 directive constrains this sweep (narrower topics, named venues, a fixed number of sources, filed references only, or no web search at all), follow that constraint and record the adjusted target in the Candidate Literature Table header. Otherwise run the full procedure below.

1. Derive an initial batch of 8 to 12 search queries from the section's beats and the theoretical framework(s) proposed in Phase 3. Cover the theory constructs (logic of care versus logic of choice, articulation work and invisible work, interdependence and relational models of aging, postcolonial computing and intermediated use, principal-agent framing, contestable AI and seamful design, face-work, self-determination theory), the setting and population (intergenerational care networks, family caregivers, older adults in South Asia, Bangladesh, collectivist care arrangements, proxy and shared device use), and the technology (autonomous and agentic assistants, multi-stakeholder and multi-principal AI, caregiver dashboards and shared health monitoring, medication adherence systems, gamification in health).
2. Run every query with WebSearch. For each promising hit, use WebFetch to confirm it is a real, findable publication (title, full author list, venue, year) before it enters the candidate table. Never fabricate a citation, an author, or a venue.
3. **Snowball, do not stop at one pass.** For the 3 to 5 strongest hits, pull their reference lists or "cited by" trails (via WebFetch on the paper page or a scholar index) and run follow-up queries against the most relevant of those. Keep expanding queries until you hit the minimums below or you can show the search is genuinely exhausted for this section's beats.
4. Cross-check every candidate against `/references/index.md` if it exists, against filenames already in `/references/`, and against candidates already proposed in other `/analysis/plans/*.md` files, so the same paper is not proposed twice under different keys.
5. Log every query you actually ran, even ones that returned nothing usable; a thin result set with no query log is not evidence the literature does not exist.

**Standing coverage debt.** `/references/` currently leans toward caregiving and aging reviews. The alignment and principal-agent literature, the CSCW caregiver-dashboard literature, and the postcolonial-computing and intermediated-use literature are the three the positioning of CLAUDE.md Section 2.6 depends on, and they are the thinnest on disk. Weight the sweep toward whichever of the three `$1` actually needs, and report the per-literature count in the Phase 8 summary.

**Coverage minimums (do not settle for fewer without explicitly justifying why the search was exhausted):**

- If `$1` is Introduction, Related Work, Methodology, or Discussion: propose **at least 20 new candidate works**, dedup'd against existing references and other plans, weighted toward Tier 1 venues.
- For any other section: propose at least 6 to 10 new candidate works.
- Across the paper as a whole, the running total of `/references/` plus all proposed-but-unfiled candidates across `/analysis/plans/` should be tracked toward the 100-work target. Report the current count and the remaining gap in the Phase 8 summary every time.

**Candidate Literature Table.** For every candidate, record: title, full author list, venue and year, venue tier (from the list above), which of the three positioning literatures it serves if any, one-sentence relevance to a specific beat from Phase 2, and a suggested citation key. Mark every entry `[cite - not yet in /references/, verify and add PDF before citing in draft]`. These are proposals for the user to accept and file into `/references/`, not citations `/draft` may use yet.

### Phase 5: Evidence-Mapped Outline

Assemble the actual writing plan as a paragraph-level or beat-level outline. For every beat, state:

- The claim or narrative move it makes.
- The RQ(s) it advances (CLAUDE.md Section 2.3).
- Its source: a specific file and location in `/proposal/proposal.md`, `/supplementary/`, `/system/`, or `/analysis/`, a candidate from the Phase 4 table, or `[MISSING DATA: insert X]` if nothing supports it yet.
- The theoretical framework carrying it, if any, from Phase 3.
- Whether it protects a seeded tension (CLAUDE.md Section 9.3: delegated dependence as agency, memory restored rather than replaced, oversight as intimacy, streak grief, trust through self-verification) that must not be sanded smooth. Every tension beat also names the counter-case the tension requires before it may anchor a claim.
- Whether the beat exists because of the Phase 0 directive, and if the directive asked for it explicitly, mark it `[DIRECTIVE]` so `/draft` knows it is not optional.
- Whether it carries one of the section's planned contrast frames (`/Training/writing-style.md`, and CLAUDE.md Section 7.4 for the six standing frames), and if so, the alternative it names; the thesis, each defined construct, each related-work gap, and the close each get one.

Do not let any beat rest on a claim with no traceable source; convert it to `[MISSING DATA]` instead of writing around the gap. A beat whose only support is CLAUDE.md's own summary of the data is `[MISSING DATA]` until the filed source is located.

**Citation density for load-bearing sections.** If `$1` is Introduction, Related Work, Methodology, or Discussion, any beat that makes a synthesis claim, a theoretical generalization, or a positioning-against-prior-work claim (as opposed to a beat that only reports this study's own empirical fact) must list **at least two** independent supporting sources from Phase 1's existing literature or Phase 4's candidate table, not one. A single citation on a synthesis claim is a gap: either find a second corroborating source or mark the claim `[UNDER-SUPPORTED: only one source, strengthen before drafting]` so `/draft` does not silently ship it thin.

### Phase 6: Pre-Flight Gate Check

Before writing the plan file, verify it would let a subsequent `/draft` pass the Section Quality Gates (CLAUDE.md Section 11):

1. Contribution gate: which of C1, C2, or C3 does this plan serve, and where.
2. RQ gate: every empirical beat maps to RQ1, RQ2, or RQ3, and no beat answers a retired question.
3. Evidence gate: every beat has a filed source, a `[cite]`, a Phase 4 candidate, `[MISSING DATA]`, or `[BLOCKED]`. Counts match CLAUDE.md Section 3 exactly. No allegiance or network beat is sourced to Study 2.
4. Theory gate: the Phase 3 block exists and names ledger rows to add.
5. Framing gate: no planned beat frames an older adult as a deficit technology should repair, no beat re-centers the lone user in place of the care network, no beat lets "agentic" outrun what `/system/` logs, and no beat makes a priority claim.
6. Tension gate: seeded tensions relevant to this section are named, protected, and paired with their counter-cases.
7. Transcendence gate (Introduction and Discussion only): the beyond-medication argument is planned explicitly, generalized along the collectivist-versus-individualist axis and bounded to Bangladesh empirically.
8. Directive gate (only when `$2` is non-empty): every operation parsed in Phase 0 is either satisfied by the plan, or listed as blocked with the CLAUDE.md invariant that blocks it. A directive-driven reduction in scope or literature count is recorded as such, and the adjusted threshold is what gate 8 measures against.
9. Literature density gate (Introduction, Related Work, Methodology, Discussion only): the Phase 4 minimum candidate count is met or the shortfall is explicitly justified, venue tiers lean Tier 1, and no synthesis beat is left `[UNDER-SUPPORTED]` without a plan to fix it before drafting.

Report any gate the plan would fail and revise the plan before writing it out, rather than shipping a plan that sets up a failing draft.

### Phase 7: Plan Grilling Session

Before the plan is finalized, subject the Phase 1 to 6 draft (hold it in working memory, do not write it to disk yet) to an adversarial SIGCHI-style panel, exactly as `/grill` would do to a drafted section, except the object under review is the plan itself: would executing this plan produce a Best Paper draft, or does it set `/draft` up to fail?

Produce three independent reviews, each citing specific beats, subsections, or table rows from the working plan. Vague criticism ("could be stronger") is forbidden; every weakness names the plan location and the concrete fix.

- **R1, the domain expert** in aging, care, and computing in the Global South. Checks every planned beat against the six framing commitments (CLAUDE.md Section 2.4): does any beat, even implicitly, frame older adults as forgetful individuals technology should fix; does the plan hold the care network as the unit of analysis rather than sliding back to the lone user; does the plan treat checking as an open empirical question rather than assuming surveillance or assuming benignity; does it plan silence and non-use as patterned participation. Checks that the plan's engagement with the intermediated-use and proxy-use literature is honest positioning rather than a strawman, and that no beat extends a claim from Bangladesh to a region.
- **R2, the methods and evidence hawk.** Audits every count the plan proposes to reference against CLAUDE.md Section 3 and against the filed source behind it. Checks every beat in the Phase 5 outline actually has a traceable source, `[cite]`, Phase 4 candidate, `[MISSING DATA]`, or `[BLOCKED]` tag, and flags any beat that quietly assumes a fact with none of those. Flags any beat that cites CLAUDE.md rather than a filed file. Checks every synthesis-claim beat in a load-bearing section has the two required independent sources (Phase 5's citation-density rule) and is not silently shipped `[UNDER-SUPPORTED]`. Flags as a fabrication risk any beat that sources an allegiance or network claim to Study 2 (CLAUDE.md Section 3.2), any beat that reports Study 3 data before Study 3 has run (Section 3.3), any beat that describes an unimplemented capability as existing (Section 3.3), and any beat resting on the unresolved monetized-points or pseudonym questions. Flags any single-instance finding not explicitly labeled as such.
- **AC, the meta-reviewer** evaluating the plan against the Best Paper Standard (CLAUDE.md Section 9) and the Theoretical Grounding Mandate (Section 10): does the plan make the section's contribution nameable by the point a reader would hit it; for each proposed theory row, apply the Section 10 enforcement rule now, before drafting, rejecting any framework whose citation could be deleted without changing the beat's conclusion; does the plan protect earned surprise and the seeded tensions (Section 9.3) as explicit beats rather than letting them get planned away; for Introduction and Discussion plans, does the transcendence beat actually generalize to agents serving a plural principal with named analogous settings, not just gesture at it.
- **Directive compliance check** (only when `$2` is non-empty): before the three reviews, restate each parsed operation from Phase 0 and point to the plan location that satisfies it. Any operation the working plan drifted away from is the first defect to fix in the revision step, ranked above the reviewers' findings. A reviewer objection that would undo an explicit user directive is a false alarm unless it names a CLAUDE.md invariant; record it as such with the rebuttal, and keep the directive.

**Verdict and revision.** For each review, produce a ranked defect list (framing violations and evidence failures first, then theory decoration, then missing tension protection, then structure) with the plan location and a concrete fix. Note any reviewer complaint that is actually wrong given our data or scope, with the rebuttal. Then revise the working plan in place to resolve every defect that is not a false alarm: add or re-source beats, cut or replace decorative theory, tighten citation density, add explicit tension-protecting beats, re-flag single-instance findings. This may require looping back into Phase 4 for additional sources or Phase 3 for a different framework. Do not proceed to Phase 8 with an open defect that has a known fix.

### Phase 8: Output

1. Ensure `/analysis/plans/` exists.
2. Write the finalized, post-grilling plan to `/analysis/plans/$1.md`, or to the path the Phase 0 directive names if it names one, structured as: the Directive Intake block from Phase 0 verbatim if `$2` was non-empty, section purpose, subsection or beat decomposition (Phase 2), Theory Alignment block (Phase 3), Candidate Literature Table (Phase 4), Evidence-Mapped Outline (Phase 5), Pre-Flight Gate Check results (Phase 6), Plan Grilling Session summary (Phase 7: the three reviews' ranked defects, which were fixed and how, and any false alarms with rebuttal). If a plan already exists at that path, read it first and say whether this run replaces it or revises it under the directive.
3. In the terminal, output a summary: how the directive shaped this run and any clause blocked by the hard floor, the beat count, the contribution(s) served, every `[MISSING DATA]`, `[BLOCKED]`, `[NOT YET IMPLEMENTED]`, `[cite]`, and `[UNDER-SUPPORTED]` placeholder remaining after grilling, the ledger rows `/draft` should add, the top 5 to 10 candidate papers from Phase 4 ranked by venue tier and relevance the user should review and file into `/references/` before drafting, the literature coverage tally (current file count in `/references/`, count of new candidates proposed this run, per-literature counts across the three positioning literatures, running total against the 100-work target, remaining gap), any contradiction found between `/proposal/proposal.md` and `/supplementary/` (surfaced, never resolved silently, per CLAUDE.md Section 3.4), and the grilling verdict: would the pre-grilling plan have survived, what the grilling session changed, and whether any defect remains unresolved and why.
4. Note explicitly that this plan does not touch `/output/` and that running `/draft $1` next is what turns it into prose.
