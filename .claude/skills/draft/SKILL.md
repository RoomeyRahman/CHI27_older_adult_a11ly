---
name: draft
description: Executes a rigorous plan-following, theory-anchoring, grilling, drafting, and style-pass loop for a CHI 2027 paper section, verifying every citation against the filed literature and writing to the canonical style guide in /Training/writing-style.md, targeting Best Paper quality as defined in CLAUDE.md Sections 9 to 11.
argument-hint: [section-name] "[optional-story-arc, used only if no plan exists]"
---

We are drafting the `$1` section for our CHI 2027 submission. If a writing plan for this section exists in `/analysis/plans/`, that plan is the structural skeleton and the optional narrative arc below only supplements it. Optional arc:
"$2"

You must execute this exact multi-stage protocol. Output your progress for each step explicitly. The bar for this draft is the Best Paper Standard in CLAUDE.md Section 9; do not ship text that fails its gates.

### Phase 1: Contextual & Narrative Ingestion

1. **Guidance Alignment:** Read `/Training/writing-style.md` in full; it is the canonical style guide (CLAUDE.md Section 7) and every sentence you draft is answerable to it. Then scan the PDF guidelines in `/Training/` to calibrate your baseline for CHI structure and rigor. Per the guideline's own warning, apply its rules while drafting but check its metrics only afterward; mid-draft metric-chasing produces prose written to satisfy a number.
2. **Writing Plan Ingestion (the plan is the skeleton):** Look in `/analysis/plans/` for this section's plan, files named `<Section>*.md` (e.g. `Introduction.md`); when several versions exist, the highest version number is current unless its header says otherwise. If a plan exists, read it in full and obey it:
   - Follow its **beat and paragraph decomposition** exactly: paragraph order, each paragraph's job, and the stated handoffs. Deviate only for cause, and report every deviation with its reason in the final output.
   - Draw every empirical claim from its **Evidence-Mapped Outline** and argument chain; do not introduce claims the plan does not license without flagging them as additions.
   - Adopt its **Theory Alignment block** as the starting point for Phase 2 (the plan proposes; this task commits the ledger rows).
   - Honor its gate-check and grilling resolutions; do not silently reopen questions the plan already settled.
   - If the provided arc ("$2") conflicts with the plan, **the plan wins**; surface the conflict rather than blending them.
     If no plan exists, state that explicitly, recommend running `/plan-section $1` first, and only then fall back to "$2" as the skeleton. If neither a plan nor an arc exists, stop and ask the user rather than inventing a structure.
3. **The Core Story:** Whatever skeleton governs (plan or arc), verify it protects, rather than smooths, the seeded tensions listed in CLAUDE.md Section 9.3, each anchored to a named A2 theme: delegated dependence as agency, reminders strengthen felt timing without replacing memory, oversight as intimacy, streak grief, and trust through self-verification. Each tension appears with its counter-case or not at all.
4. **Fact-Finding:** Read `/proposal/proposal.md` in full for framing, the three RQs, and the C1 to C3 contribution structure, and for nothing else (CLAUDE.md Section 3 precedence); three paragraphs of its Section 1 still describe the retired three-study architecture and are superseded by `/output/Method.md`. Read `/output/Method.md` in full: it is canonical for the study as executed, every count, the deployed feature list, and procedures (CLAUDE.md Section 3). Read `/output/codes/A2/` for every finding and every quotable extract: `FINAL-CODEBOOK.md` and `FINAL-REPORT.md` for Phase 1, `final-codebook/phase-2/` for Phase 2, with `final-codebook/tsv/` as the canonical package; `/output/codes/A1/` is audit trail only and is never cited. Read `/output/Related-Work.md` for positioning and the definition of allegiance when `$1` is Introduction or Discussion. Go to `/Supplementary/Interviews/phase-1/` and `phase-2/` only to verify an A2 extract at its cited line. For any claim about what the agent does on its own, `/output/Method.md` Prototype Development is the ceiling; `/system/` does not exist and no logs exist. There is no `current_plan.md`, `rqs.md`, `motivation.md`, or `research_directions.md` in this repository.

   Cross-check every count against CLAUDE.md Section 3, and treat CLAUDE.md itself as a checksum, never as a source: a fact whose only home is CLAUDE.md's summary is `[MISSING DATA]` until the filed transcript or record is located. Five supersessions bind every draft (CLAUDE.md Sections 2, 2.3, 3, 3.3, 5):

   - Never draft a beat answering a retired question (routines and challenges, literacy and device access, perceptions of AI voice reminders, retention). Their substance survives only as RQ1 context and Method context.
   - Never write Study 1, Study 2, or Study 3. The study is one two-phase household study: Phase 1, the deployment, Phase 2.
   - Never draft gamification as a contribution or a behavioral lever; scores and streaks are relational triggers analyzed under RQ3, and streak grief is a finding. Symbolic streaks, a logbook, and a heat map are the only deployed reward mechanisms.
   - Never let an elicited Phase 2 judgment about an unbuilt mechanism (risk-graded weakening veto, silence as participation, probationary mode, shared family scores) carry a use claim. Every Phase 2 sentence carries the lived or elicited label its A2 code carries.
   - Never describe an agent capability beyond the deployed list in `/output/Method.md` Prototype Development, and never write "the agent decided" for anything but the request to notify a family member after an unconfirmed dose. Flag anything finer to the user instead of drafting around it.

   Two evidentiary limits bind every draft, and prose depending on either does not ship: no household pairing map is filed, so no sentence claims that an older adult and a caregiver described the same episode (CLAUDE.md Sections 3.5, 5.4); and caregiver transcripts are not de-identified (Section 3.4), so caregivers are quoted by ID only and no name, employer, or workplace enters `/output/`.
5. **Pedagogical Alignment:** `/references/` is background studies for every section: scan it for claims and citation support relevant to `$1`, reading `/analysis/literature/literature-map.md` first and citing by the numeric keys of `/references/reference.bib`. If `$1` is the Method section and a `/references/methodology/` directory exists, additionally read its entries to extract structural pacing and theoretical integration patterns from the award-winning papers there. Extract patterns only; never borrow domain content.
6. **Reference Evaluation (before any citing):** Build a working citation inventory for this section. For every literature source the plan's evidence map or your argument will lean on, verify it through one of two doors:
   - **A filed PDF in `/references/`**: open the PDF itself (Read the first page or two, or the parsed JSON where one exists) and confirm from the document, not from memory, (a) title, authors, venue, and year, and (b) that it actually supports the specific claim you will attach to it. A plan row marked with a filename is a pointer, not proof; spot-check every filed source before load-bearing use, and fully read any source carrying a pivotal claim. If the PDF does not support the claim, do not cite it; downgrade the claim to `[cite]` and flag the mismatch.
   - **`[cite]` placeholder**: everything else. A work not verifiably filed gets a `[cite]`, never a fabricated author-year reference.
     Record the inventory (source, file, claim it supports, verified yes/no) in your working notes; Phase 4 may only cite from this inventory.

### Phase 2: Theory Alignment (mandatory, before any prose)

Produce the **Theory Alignment block** required by CLAUDE.md Section 10:

- **Primary framework(s):** the theory that will carry load in this section, with its key constructs, drawn from or added to the candidate stack in CLAUDE.md Section 10.
- **Rival considered:** at least one plausible alternative framing and why the primary wins for this material.
- **The work the theory does here:** what it predicts, explains, or organizes in this specific section. Name the paragraphs or beats where it will surface.
- **Ledger update:** add or update the corresponding rows in `/analysis/theory-ledger.md` (create the file with the header `construct | source theory | citation | where used | load it bears` if absent) in this same task.

Two standing constraints. Behavior-change and habit-loop models (Fogg, Eyal) appear only as the position the gamification reframing argues against, never as a framework carrying a beat. Asset-based community development is named once in Method as a stance and never claimed as a contribution.

If no framework can do real work for this section, say so explicitly and explain why the section is legitimately atheoretical (rare; Method subsections describing logistics may qualify).

### Phase 3: The AC Grilling Session

Adopt the persona of a highly critical SIGCHI Associate Chair (AC) evaluating a Best Paper candidate and output a brief **Grilling Report**:

- **Plan Fidelity:** Does the intended draft follow the writing plan's beat decomposition and evidence map? List any planned deviation and its justification; an unjustified deviation fails this check.
- **Narrative vs. Evidence:** Does the story over-promise compared to the actual data in `/output/codes/A2/` and `/output/Method.md`? Does any sentence let the word "agentic" carry a claim `/output/Method.md` Prototype Development cannot back, or let an elicited judgment read as use?
- **Citation Integrity:** Is every literature source either in the verified Phase 1 inventory or marked `[cite]`? Any citation resting on memory rather than an opened document fails this check. Does any sentence make a priority claim ("the first", "the only", "no prior work has")? Priority claims fail this check outright (CLAUDE.md Section 2.5).
- **Theoretical Anchor:** Does the chosen framework genuinely explain the material, or is it decoration? Apply the enforcement rule from CLAUDE.md Section 10.
- **Contribution Check:** Which of C1 empirical, C2 conceptual, or C3 design (CLAUDE.md Section 9.1) does this section advance, and does the arc make that visible?
- **Epistemic Gaps:** Are there unbacked claims that need methodological justification, and does the section respect the six framing commitments (CLAUDE.md Section 2.4)? In particular: does any sentence quietly re-center the lone user in place of the care network, or treat checking as settled surveillance or settled benignity rather than as the empirical question it is?
- **Transcendence (Introduction and Discussion only):** Does the arc articulate what the paper teaches HCI about agents serving a plural principal, beyond medication entirely, while keeping every empirical claim inside Bangladesh?

### Phase 4: Hallucination Prevention & Drafting

**[STRICT ANTI-HALLUCINATION PROTOCOL]**: You are explicitly forbidden from inventing participant counts, demographics, dates, statistical significance (p-values), interview quotes, log entries, or system capabilities. If the source files lack specific data needed to fulfill the narrative, use a precise `[MISSING DATA: insert X]` placeholder and surface it to the user. Do NOT guess or interpolate. Quotes come verbatim from A2 extracts in `/output/codes/A2/` or the transcript lines they cite in `/Supplementary/Interviews/`, attributed by ID, phase, and line: never paraphrase into quotation marks, never compose an illustrative quote, and present Bangla quotes in translation with the original filed.

**[REFERENCE VERIFICATION PROTOCOL]**: Citations obey the Phase 1 inventory. Only two forms may appear in the draft: (a) a verified filed source, cited as author-year plus its filename so the user can resolve BibTeX later, e.g. `[Sultana et al. 2018; 2910674.2935855.pdf]`; (b) `[cite]` for everything else. Never write an author-year reference for a work you have not opened in this task or a prior verified inventory. Never attribute a finding to a filed paper beyond what its text supports; when in doubt, reopen the PDF or downgrade to `[cite]`. Never attach a citation to one of our own findings.

Write the first draft of the `$1` section.

- **Narrative Drive:** Follow the governing skeleton from Phase 1 (the writing plan, or "$2" only when no plan exists): paragraph order, jobs, and handoffs as planned.
- **Theory in the prose:** Weave the Phase 2 framework into the argument so it carries load at the beats you named; theory appears where it explains, never as a citation list.
- **Scientific Weight:** Ground every beat in the filed data and explicit HCI theory. Apply structural rules from `/Training/`.
- **Formatting:** Cite per the Reference Verification Protocol above, and name the `/output/codes/A2/`, `/output/Method.md`, or `/Supplementary/Interviews/` file behind each empirical claim in your working notes so the terminal report can list it.

### Phase 5: The Style Pass (per `/Training/writing-style.md`, bound by CLAUDE.md Section 7)

- **Rhythm:** Pair long qualification sentences with short landing sentences; target mean length 18 to 21 words with spread (SD) 6 to 9; at most one sentence over 35 words per section; spend the short flat sentences on the claims a reviewer must remember, such as "Families move the agent between these roles."
- **Cohesion:** Link sentences by reference to the previous idea, given-before-new; every paragraph opens with an arguable claim, not an announcement; synthesis closers on about half the substantive paragraphs; anchor terms (CLAUDE.md 7.8 and 2.5) identical every time; kill nominalizations.
- **Fixed names:** the three roles are tool, coach, and advocate; the four dimensions are direction, visibility, revocability, and ceremony; the consent mechanism is the Affiliation Ledger. No synonyms, and the word "polyadic" never appears.
- **Contrast frames:** Six to eight per thousand words, spread not bunched, each naming an alternative its advocates would recognise; use the paper's six standing frames (design gap rather than memory problem; care network rather than lone user; agent that negotiates rather than system that notifies; checking as care rather than surveillance; relational trigger rather than behavioral lever; collectivist interdependence rather than individualist autonomy).
- **Agency:** True actor in subject position. Older adults, caregivers, and families decide, grant, contest, refuse, and hand over; the agent announces, requests, escalates, and stays silent; we recruited, built, analysed, and argue, around six first-person mentions per thousand words. Never write a sentence that makes our software the protagonist of a family's decision. Passive only where the actor is irrelevant or obvious, never wall-to-wall in method prose.
- **Certainty:** Flat observation, inference hedged exactly once, verbs on the rung of the evidence ladder their evidence reaches; no causal language anywhere (no controlled comparison exists in this work); one consistent coarse-quantifier vocabulary, exact figures once, no percentages on our sample sizes.
- **Banned words and constructions:** Purge the full CLAUDE.md 7.7 union list (hype words, stacked connectors, empty intensifiers, rhetorical-question transitions; the title's question is the one granted exception). Replace evaluative adjectives with the evidence they gesture at. Write "older adult", never "the elderly" as a noun.
- **The No-Dash Rule:** Remove all em-dashes and en-dashes (stricter than the guideline; project rule wins).
- **Quotations:** Integrated and left unglossed; never paraphrase a quote immediately after it appears.
- **Theory enforcement pass:** For every theoretical citation, test whether deleting it would change the paragraph's conclusion. Rewrite or delete accordingly (CLAUDE.md Section 10).
- **Ending:** The section ends on its last real point or its consequence, never on a restating summary.

This pass applies the guideline by judgment; `/polish` is the measured enforcement pass and should be run on the shipped draft before `/grill`.

### Phase 6: Quality Gates & Final Output

1. Run all eight Section Quality Gates from CLAUDE.md Section 11 and report pass/fail per gate. A failed gate means you revise before shipping, not ship with a caveat.
2. Ensure the `/output/` directory exists.
3. Write the finalized text to `/output/$1.md`.
4. Output a confirmation in the terminal that lists: the gate results, plan adherence (which plan file governed, plus every deviation and its reason, or "no plan existed"), the Theory Alignment summary (one line per framework used), the citation report (each verified filed source with its filename), the source file behind each empirical claim, any `[MISSING DATA]`, `[BLOCKED]`, or `[NOT YET IMPLEMENTED]` placeholders needing manual resolution, all `[cite]` placeholders needing literature resolution, and any contradiction found among `/proposal/proposal.md`, `/output/Method.md`, `/output/codes/A2/`, and `/Supplementary/Interviews/` (surfaced, never resolved silently, per CLAUDE.md Section 3).
