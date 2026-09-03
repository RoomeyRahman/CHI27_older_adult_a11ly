---
name: revise
description: Integrates reviewer feedback into an existing draft while strictly preventing data hallucination, preserving theoretical load-bearing, and protecting narrative momentum. Revised text must still clear the Best Paper gates in CLAUDE.md Section 11.
argument-hint: [section-name] "[reviewer-feedback-or-critique]"
---

We need to revise the `$1` section based on the following reviewer feedback:
"$2"

You must execute this exact multi-stage revision protocol. Output your progress for each step explicitly. Revision may never lower the draft below the Best Paper Standard (CLAUDE.md Section 9); appeasing a reviewer at the cost of a quality gate is not an option.

### Phase 1: Draft & Context Ingestion

1. **Load Current Draft:** Read `/output/$1.md`. Analyze its narrative arc, its theoretical grounding, and which of C1 empirical, C2 conceptual, or C3 design (CLAUDE.md Section 9.1) it currently advances.
2. **Load the Ledger:** Read `/analysis/theory-ledger.md` and identify which frameworks currently carry load in this section.
3. **Feedback Ingestion:** Analyze the provided reviewer feedback ("$2").
4. **Fact-Checking:** If the reviewer asks for expanded data or justifications, immediately cross-reference `/proposal/proposal.md` (the single canonical framing document, CLAUDE.md Sections 2 and 3.4), the relevant study directory under `/supplementary/` (`formative/`, `deployment/`, or `household/`), and `/system/` for any claim about the agent's autonomy. There is no `current_plan.md`, `rqs.md`, `motivation.md`, or `research_directions.md` in this repository, and CLAUDE.md's own summary of the data is a checksum, not a source.

### Phase 2: Feedback Triaging & AC Validation

Output a brief **Triaging Report**:

- **Valid & Supported:** Which feedback is valid and supported by our actual data?
- **Unbacked/Dangerous Requests:** Does the reviewer ask for claims we cannot empirically support, or for framing that violates the six commitments in CLAUDE.md Section 2.4? Requests of this shape are answered with a limitation acknowledgment or a reasoned rebuttal, never compliance. The recurring ones to watch for: any drift toward older adults as a deficit technology should repair; a request to re-center the individual user in place of the care network; a request to report Study 3 household data before Study 3 has run (CLAUDE.md Section 3.3); a request to read a network or allegiance claim out of Study 2's six young-skewed participants (Section 3.2); a request to describe an agent capability `/system/` does not show implemented; a request to add a priority claim ("the first study to...", Section 2.5); a request to extend a claim from Bangladesh to the Global South at large; and a request to explain streak grief away as a usability bug.
- **Theory Impact:** Does the feedback demand a new framework, weaken an existing one, or reveal that a framework was decorative? Update the Theory Alignment for this section accordingly and record the change in `/analysis/theory-ledger.md`.
- **Tension Impact:** Does the requested change sand down a seeded tension (CLAUDE.md Section 9.3: delegated dependence as agency, memory restored rather than replaced, oversight as intimacy, streak grief, trust through self-verification)? If so, propose a revision that answers the reviewer while preserving the tension and its counter-case.
- **Flow Impact:** Where will changes be injected to prevent breaking narrative momentum?

### Phase 3: Hallucination Prevention & Targeted Integration

**[STRICT ANTI-HALLUCINATION PROTOCOL]**: If a reviewer requests a metric, detail, participant, date, log entry, or result that does not exist in our source files, you MUST NOT invent it to appease them. Instead, weave in a scientifically sound acknowledgment of a limitation, or insert a `[MISSING DATA: review needed for X]` placeholder and surface it to the user. Quotes remain verbatim from filed `/supplementary/` transcripts; never paraphrase into quotation marks and never compose an illustrative quote. No unconfirmed real participant name enters `/output/` (CLAUDE.md Section 3.2 pseudonym rule).

Modify the text of `/output/$1.md`.

- **Seamless Blending:** Weave revisions directly into relevant paragraphs.
- **Scientific Weight:** Ground new additions strictly in facts from the filed source files or literature `[cite]`. A new citation must be opened and verified before it is written as author-year; otherwise it is `[cite]`.
- **Theory continuity:** New text inherits the section's Theory Alignment; if it introduces a framework, that framework enters the ledger and must carry load under the enforcement rule (CLAUDE.md Section 10).

### Phase 4: The Style Pass (per `/Training/writing-style.md`, bound by CLAUDE.md Section 7)

Read `/Training/writing-style.md` in full if not already read this task, then subject the _entire_ revised section, not only the new text, to an editorial pass against it:

- **Rhythm and cohesion:** New sentences match the section's rhythm profile (long qualification then short landing, mean 18 to 21 words, spread 6 to 9, at most one sentence over 35 words); they link by reference to the previous idea, given-before-new; edited paragraphs still open with arguable claims; anchor terms and fixed names (CLAUDE.md 2.5 and 7.8: care network, allegiance, the agent, dignity, older adult, caregiver; tool, coach, advocate; direction, visibility, revocability, ceremony; Affiliation Ledger) stay identical.
- **Agency and certainty:** True actor in subject position, with families and participants doing the deciding and the agent announcing, requesting, escalating, or staying silent; observation flat, inference hedged once, verbs on the rung their evidence reaches; no causal language; the coarse-quantifier vocabulary stays consistent with the rest of the paper; no exact figure gets repeated where it was already stated once.
- **Contrast frames:** If the revision added or moved positioning claims, the frames stay honest (an alternative its advocates would recognise), stay drawn from the paper's six standing frames where possible, and the per-thousand-word density stays in the six-to-eight band, spread not bunched.
- **Banned words and constructions:** Purge the full CLAUDE.md 7.7 union list from all new and touched text (hype words, stacked connectors, empty intensifiers, rhetorical-question transitions).
- **The No-Dash Rule:** Remove all em-dashes and en-dashes (project rule, stricter than the guideline).
- **Quotations:** Any quote the revision touches stays verbatim, integrated, and unglossed.
- **Theory enforcement pass:** Re-test every theoretical citation in the revised section; delete or rework any that no longer changes a conclusion.
- **Flow Check:** The "scars" of the edit are invisible, and the section still ends on a consequence, not a summary.

If the revision was substantial (new paragraphs, restructured argument), recommend running `/polish $1` afterward for the measured enforcement pass against the guideline's reference table.

### Phase 5: Quality Gates, Final Output & Changelog

1. Re-run all eight Section Quality Gates from CLAUDE.md Section 11 on the revised section and report pass/fail per gate; revise until all pass.
2. Overwrite the existing file at `/output/$1.md` with the revised text.
3. Output a brief **Changelog** summarizing what was changed, listing any feedback rejected due to lack of evidence or framing violations (with the rebuttal rationale a reviewer response letter could reuse), noting any theory ledger updates, and highlighting any `[MISSING DATA]`, `[BLOCKED]`, or `[cite]` tags generated.
