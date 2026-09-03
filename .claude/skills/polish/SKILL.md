---
name: polish
description: Runs a style-calibration pass over an existing section draft, enforcing the complete CHI-tuned writing style in /Training/writing-style.md (rhythm, cohesion, contrast frames, paragraph shape, agency, certainty calibration, citation integration, hype removal) plus the measurable reference targets, without altering any fact, count, quote, or citation.
argument-hint: [section-name-or-path-to-draft]
---

We are polishing the prose of `$1` for our CHI 2027 submission. This is a style pass, not a content pass: the argument, evidence, and structure stay; the sentences change. The complete guideline is `/Training/writing-style.md`, and this task follows it in full, section by section, ending with its reference table and its "Before you send it" checklist.

Execute this protocol exactly and report progress per phase.

### Phase 0: Hard Invariants (violating any one of these fails the task)

1. **Facts frozen.** No participant count, demographic, date, tool name, session duration, or metric changes. Counts must still match CLAUDE.md Section 3 exactly after the pass.
2. **Quotes verbatim.** Participant quotations are untouchable: no rewording, no trimming without ellipsis already present in the source, no new quotes, and no gloss added after one. No unconfirmed real participant name may be introduced or left standing (CLAUDE.md Section 3.2 pseudonym rule).
3. **Citations preserved.** Every `[cite]`, `[MISSING DATA: ...]`, `[BLOCKED: ...]`, and verified filed-source citation (`[Author Year; filename.pdf]`) survives the pass attached to the same claim. Citations may move within a sentence (to clause end, per the guideline) but never between claims, and none may be added or dropped.
4. **Theory load preserved.** Theoretical framing sentences keep their function. If polishing reveals a citation that fails the CLAUDE.md Section 10 enforcement rule (deletable without changing the conclusion), flag it in the report; do not silently delete it.
5. **CLAUDE.md style law still binds.** No em-dashes or en-dashes anywhere (Section 7.2, the one rule stricter than the guideline). Terminology per Sections 2.5 and 7.8: the anchor terms *care network*, *allegiance*, *the agent*, *dignity*, *older adult*, and *caregiver* stay identical every time; the three roles are tool, coach, and advocate; the four dimensions are direction, visibility, revocability, and ceremony; the consent mechanism is the Affiliation Ledger; "older adult" never becomes "the elderly" as a noun; the word "polyadic" never appears; and no synonym stands in for any of these. The six framing commitments of Section 2.4 hold in every rewritten sentence, and no rewrite may introduce a priority claim ("the first", "the only", "no prior work has").
6. **Autonomy claims frozen.** A sentence stating what the agent decides on its own, what follows fixed rules, and what waits for human confirmation keeps its exact scope. Polishing may not let "agentic" or a compressed verb widen a claim past what `/system/` logs.

### Phase 1: Ingestion and Baseline

1. **Read the guideline in full.** Read `/Training/writing-style.md` top to bottom before touching the draft. It is the single source of truth for this pass; the rules restated below are its operational summary, and where they compress it, the file wins.
2. **Locate the draft.** If `$1` is a path, use it; otherwise use `/output/$1.md`. If the file does not exist, stop and ask.
3. **Measure the baseline.** Run the repository benchmark on the draft as it stands:

   ```
   .venv/bin/python benchmark.py <path-to-draft>
   ```

   `benchmark.py` sits at the repository root and needs `spacy`, `textstat`, `tabulate`, and the `en_core_web_sm` model; `requirements.txt` carries the setup commands. If the virtual environment is missing, create it before measuring rather than hand-estimating any metric.

   `benchmark.py` computes the full reference table of Phase 3, including the readability and lexical bands (Flesch Reading Ease, Flesch-Kincaid grade, Gunning Fog, polysyllabic percentage, MATTR-100, adjacent-sentence content-word overlap, connective density), and prints a per-metric pass or fail verdict. Report the baseline table before editing so improvement is demonstrable. Supplement it with a scratchpad script only for the checks it does not cover: em/en-dash count, "it is important to note", the full CLAUDE.md 7.7 hype list (the benchmark's hype set is narrower), and lexical contrast frames of the "rather than X, Y" / "instead of" / "not X but Y" / "unlike" shape, which the benchmark's connective-based contrast count does not see. Never hand-estimate a metric `benchmark.py` already reports.

### Phase 2: The Style Pass (apply every section of the guideline)

Work paragraph by paragraph. For each, apply the full rule set:

**Rhythm.**
- Pair long qualification sentences with short landing sentences. The long one carries conditions, scope, caveats; the short one tells the reader what to take.
- Target mean sentence length 18 to 21 words with a standard deviation of 6 to 9. Per ten sentences: one or two under twelve words, six or seven in the middle, two past twenty-five.
- Split anything over 35 words unless it is a genuine parallel list. At most one over-35 sentence per section.
- Spend short flat sentences on the claims a reviewer must remember.
- Keep density in vocabulary (a precise term saves a clause), never in syntax (no triple-embedded subordination; international reviewers pay the cost).

**Holding the thread.**
- Link sentences by pointing back at the previous idea ("this suggests", "because of that", "the same pattern held for", "which is why") rather than repeating the carrying noun. Roughly half of adjacent sentence pairs should share no content word.
- Order given-before-new: open each sentence with what the previous sentence established, close with the addition. Choppiness usually means new information arrived in subject position; fix it there.
- Hold three to five anchor terms for the paper, used identically every time (align with CLAUDE.md 7.8 terminology); vary everything around them. No synonym ever stands in for a defined construct.
- Kill nominalizations: keep actor and action in the sentence ("participants used colour to express tone", not "the utilisation of colour for the facilitation of expression"). Nominalize only when the process itself is the topic.

**Defining by contrast.**
- Frame key claims as "rather than X, Y". Six to eight contrast frames per 1,000 words, spread across the section rather than bunched on page one.
- Each frame names an alternative its advocates would recognise; no straw men. In this paper the natural frames are the six standing ones (CLAUDE.md Section 7.4): design gap rather than memory problem, care network rather than lone user, agent that negotiates rather than system that notifies, checking as care rather than surveillance, relational trigger rather than behavioral lever, collectivist interdependence rather than individualist autonomy.

**Paragraphs.**
- Every paragraph opens with an arguable claim, never an announcement ("This section describes..." is an announcement; rewrite it).
- Two to four sentences of support follow: a mechanism, a citation, a number, a quotation, or a worked case. Restatement is not support; where two sentences say the same thing at different vagueness, cut one.
- Close about half the substantive paragraphs with a synthesis sentence ("together, these themes show", "the upshot is", "what this leaves is"); never all of them.
- Vary paragraph length three to six sentences, with the occasional two-sentence paragraph for emphasis.

**Describing what already exists** (related-work and positioning passages).
- Shape: what the established line achieved, a sentence or two on how it plays out, the turn ("however", "yet", or nothing), what it does not handle, why that matters here, what we do.
- One gap per paragraph. Be generous before critical.

**Who acts.**
- The true actor takes subject position. Older adults, caregivers, and families decide, grant, contest, refuse, hand over, and work around; the agent announces, requests, escalates, and stays silent. "The daughter granted the agent the advocate role", never "the system was granted permission by the daughter". Never write a sentence that makes our software the protagonist of a family's decision. At CHI this is substance, not style: grammar assigns control, and control is the finding.
- First person for research acts (we recruited, we analysed, we argue), around six mentions per 1,000 words. Passive is permitted where the actor is irrelevant or obvious, but a method passage entirely in passive hides the decisions transparency requires; name who did what.

**Calibrating certainty.**
- Flat about procedure and observation; hedged about inference; the two always distinguishable.
- Verb ladder: *shows/demonstrates* need a controlled comparison; *indicates/points toward* need a strong consistent pattern; *suggests/is consistent with* need an observed regularity; *appears/may* mark genuine uncertainty. Put every claim verb on the rung its evidence reaches, and fix over-hedged measured results as firmly as overclaims.
- One hedge per claim, never stacked.
- No causal language anywhere: this is interview and observational work, so it yields association and description only.
- Coarse quantifiers, one vocabulary held for the whole paper (most, roughly half, several, a few, one participant). No percentages on our sample sizes. No "many" where a count exists.
- Exact figures stated once, where they belong, not repeated across sections.
- Somewhere, plainly, what the work does not cover; limitations in the flattest prose in the paper, each framed as a scoping decision (CLAUDE.md 6.2 and 6.3): one cultural setting, Study 2's young and individual sample, deployment lengths, self-report plus logs rather than health outcomes, the agent's bounded autonomy. Never extend a claim from Bangladesh to the Global South at large.

**Citations as prose.**
- Citations sit at clause end attached to the specific claim they support; multi-reference brackets point at something those papers actually share. Eleven to fourteen brackets per 1,000 words is the CHI norm; integration matters more than the number. Organise by idea, never one-paper-per-sentence summaries.
- Never a citation on our own findings.

**Being interesting without hype.**
- Engagement comes from stakes and tension. Surface the seeded tensions (CLAUDE.md 9.3); the sentence beginning "but this held only when" is the strongest kind. Never sand a complication smooth.
- Quotations integrated and left unglossed; no paraphrase immediately after a quote.
- Replace every evaluative adjective with the evidence it was gesturing at.

**Tuning by section.**
- Introduction and Discussion: densest contrast frames, longest sentences. Method: flat short declaratives, exact figures, minimal hedging, agency fully explicit. Findings: participants in subject position, quotations carrying evidence, coarse quantifiers generalising. Related Work: gap structure and citation integration hardest at work. Limitations: flattest prose in the paper.

**What to avoid (zero tolerance).**
- Hype words, none survive: leverage, robust, novel, seamless, state-of-the-art, cutting-edge, comprehensive, powerful, crucial, pivotal, delve, landscape, realm, underscore, unlock, harness (plus CLAUDE.md 7.7: testament, tapestry, robustly, seamlessly).
- Stacked connectors, all cut: moreover, furthermore, additionally, "it is important to note that". If the connection is real, the content carries it.
- Also out: intensifiers that measure nothing, "ever-evolving landscape" openers, rhetorical questions as section transitions, and em-dashes for asides (a comma, semicolon, or new sentence does the work).
- The section ends on the last real point or its consequence, never on a restating summary.

### Phase 3: Verification Against the Reference Table

Re-run `benchmark.py` (plus the scratchpad supplement) on the polished text and check every measurable target from the guideline's reference table:

| Metric | Target | Source |
|---|---|---|
| Flesch Reading Ease | 20–35 | `benchmark.py` |
| Flesch–Kincaid grade | 13–16 | `benchmark.py` |
| Gunning Fog | 17–19 | `benchmark.py` |
| Polysyllabic words | 25–30 % | `benchmark.py` |
| Vocabulary diversity (MATTR-100) | 0.75–0.80 | `benchmark.py` |
| Adjacent sentences sharing no content word | 40–55 % | `benchmark.py` |
| Connective tokens | 75–90 per 1,000 words | `benchmark.py` |
| Mean sentence length | 18–21 words | `benchmark.py` |
| Sentence-length spread (SD) | 6–9 | `benchmark.py` |
| Sentences over 35 words | ≤ 1 per section | `benchmark.py` |
| Contrast frames | 6–8 per 1,000 words | `benchmark.py` (connectives) plus scratchpad (lexical frames) |
| Citation brackets | 11–14 per 1,000 words | `benchmark.py` |
| First-person mentions | 5–8 per 1,000 words | `benchmark.py` |
| Passive constructions | 20–28 % of sentences | `benchmark.py` |
| Moreover / Furthermore / Additionally | 0 | `benchmark.py` |
| Hype words | 0 | `benchmark.py` (partial) plus scratchpad (full CLAUDE.md 7.7 list) |
| Em/en-dashes | 0 (CLAUDE.md rule, stricter than the guideline) | scratchpad |

Every row above is now computed, so no row may be reported as a judgment call or left blank. If a metric misses its band, fix the prose the metric is a proxy for, never the metric directly:

- **Sentence-length spread under six:** split one long sentence into a long plus a short, rather than padding the short ones.
- **Flesch Reading Ease above 35, or Flesch-Kincaid / Gunning Fog below band:** the prose has gone thin, not clear. Restore density in vocabulary, a precise term replacing a vague clause, per the guideline's rule that density lives in words and not in syntax.
- **Flesch Reading Ease below 20, or Flesch-Kincaid / Gunning Fog above band:** syntax is carrying load that vocabulary should carry. Cut embedded subordination and split the longest sentences; do not swap in shorter, less precise terms.
- **Polysyllabic words under 25 %:** technical constructs have been paraphrased into common words; restore the anchor terms of CLAUDE.md 2.5 and 7.8. Over 30 %: nominalizations have stacked up, so return the actor and the action to the sentence.
- **MATTR-100 under 0.75:** phrasing repeats around the anchor terms; vary everything except the anchors. Over 0.80: a defined construct has picked up synonyms, which the guideline and CLAUDE.md Section 2.5 both forbid. Check the anchor terms first, because this is the one band where the fix and the terminology invariant can pull against each other.
- **Adjacent sentences sharing no content word, outside 40 to 55 %:** the benchmark reports the share of adjacent pairs with *no* content word in common, so a low number means heavy repetition and a high number means a broken thread. Below 40 %, sentences are chaining by repeating the carrying noun, so link by pointing back at the previous idea instead. Above 55 %, the thread is broken and new information is arriving in subject position, so reorder given before new.
- **Connective tokens outside 75 to 90 per 1,000 words:** below band, the argument's joints are implicit and the reader reconstructs them, so name the relation with a precise conjunction. Above band, connectives are doing work the content should do; the fix is cutting stacked connectors, never adding a banned one to hit the number.

Report the benchmark's own verdict column verbatim alongside these notes. Do not fabricate a score for any metric, and do not declare a band met without a benchmark run on the final text.

Then walk the guideline's full "Before you send it" checklist, item by item, and mark each pass or fail:

1. No banned word survives anywhere.
2. Six to eight contrast frames per 1,000 words, spread not bunched, each naming a recognisable alternative.
3. No three consecutive sentences share a length; at least one short flat sentence in every long paragraph.
4. Sentences link by reference to the previous idea; given information opens, new information closes.
5. Anchor terms and fixed names used consistently; no synonym for a defined construct, and no "polyadic".
6. Every paragraph opens with an arguable claim, not an announcement.
7. Every paragraph survives "what is the evidence here".
8. Synthesis closers in about half the paragraphs, not all.
9. Families, participants, and researchers, not the agent, occupy subject position in findings.
10. Observation flat, inference hedged once, the two distinguishable.
11. Every verb on the rung of the evidence ladder its evidence reaches.
12. No causal language (no controlled comparison exists in this work).
13. Coarse quantifiers consistent; no percentages on small samples.
14. Citations attach to claims about the literature, never to our own findings.
15. At least one finding complicates the framing rather than confirming it, and every seeded tension present in this section (CLAUDE.md Section 9.3) still stands with its counter-case.
16. What the work does not cover is stated plainly somewhere.
17. The ending is a consequence, not a summary.

A failed item means revise and re-verify, not ship with a caveat. Fix violations after the drafting judgment is made, per the guideline's own warning: measuring mid-sentence produces prose written to satisfy a metric.

### Phase 4: Invariant Audit and Output

1. **Diff-audit the invariants.** Compare polished text against the original for Phase 0 violations: every count, quote, citation, `[cite]`, `[MISSING DATA]`, and `[BLOCKED]` present and attached to the same claim, and every autonomy claim still scoped exactly as it was. Run the CLAUDE.md Section 11 style gate (gate 6) and framing gate (gate 5) as final confirmation.
2. **Write the polished text back to the same file** (`/output/$1.md` or the given path). Do not create a new file.
3. **Report:** before/after metrics table, the 17-item checklist results, the invariant audit result, any theory citations flagged under the Section 10 enforcement rule, and any sentence where a style target and a hard invariant conflicted (the invariant always wins; list what was left unpolished because of it).
