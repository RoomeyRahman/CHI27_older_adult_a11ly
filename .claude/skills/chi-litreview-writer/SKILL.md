---
name: chi-litreview-writer
description: Write or revise a Related Work / literature review section targeted at CHI (or CSCW, DIS, and similar HCI venues) in a specific calibrated academic prose style. Use this skill whenever the user asks to write, draft, restructure, or polish a related work section, literature review, background section, or "positioning" text for an HCI paper or proposal — including when they provide a references.bib file, a literature map, or a set of papers to synthesize. Also trigger when the user asks to make academic prose "sound like CHI", check it against the CHI style targets, or turn a list of papers into a narrative review.
---

# CHI Literature Review Writer

Write a Related Work section that does three jobs at once: teaches the reader the field, positions the paper's contribution against it, and reads as calibrated CHI prose rather than a laundry list or a template.

**Before writing anything, read both reference files in full:**
1. `references/chi-writing-style.md` — the sentence-level style contract (rhythm, contrast frames, hedging ladder, banned words, quantitative targets). Every paragraph you write is bound by it.
2. `references/litreview-structure.md` — how to structure the section, characterize prior work fairly, and use the gap pattern.

Read them at the start of every session that uses this skill; do not write from memory of them.

## Inputs

Expect some combination of: the paper/proposal itself, a `references.bib`, a literature map or notes on the papers, and possibly the papers' abstracts. If a bibliography exists but no analytical notes do, ask whether the user wants you to (a) work from titles/abstracts you can fetch, or (b) have them supply notes — and say plainly that anything written from title-level knowledge will be shallow and flagged as such.

**Never cite a paper that is not in the provided bibliography or otherwise verified in-session.** If the argument needs a citation you don't have, write `[CITATION NEEDED: <what kind of paper>]` and list these gaps at the end. Inventing a reference, or attributing a claim to a real paper you have not actually checked, is the worst possible failure of this skill.

## Workflow

### 1. Extract the positioning logic
From the paper's contribution claims, work out what the related work must accomplish: which streams the reader needs, in what order they build, and what gap each stream must open that the paper then fills. The gap statements are the skeleton; write them first, one per stream, before any prose.

### 2. Structure: 3–5 thematic subsections that tell a story
Organize by topic, not chronology and not paper-by-paper. Order subsections so each builds on the last, foundations first, and so the final subsection lands closest to the paper's contribution. Each subsection follows the shape: what this line of work achieved (generous, accurate) → how it plays out (a sentence or two, citing several papers per claim) → the turn → the one gap, and why it matters here. One gap per subsection; stacking complaints reads as axe-grinding.

Optionally end the section with a short synthesis ("Summary of Related Work" or an unlabeled closing paragraph) that names the intersection gap the paper occupies — the CHI-standard move when the contribution sits where multiple literatures fail to meet.

### 3. Draft under the style contract
Apply `chi-writing-style.md` while drafting, not after. The non-negotiables:
- Long-then-short sentence rhythm; mean ~19 words, SD 6–9; spend short flat sentences on the claims that matter
- Contrast frames ("rather than X, Y") carry the positioning — 6–8 per 1,000 words, spread out, each naming an alternative its advocates would recognize
- Given-before-new information order; link by reference to the previous idea, not noun repetition
- 3–5 anchor terms used with total consistency; no synonym variation on defined constructs
- Hedging ladder: flat for what prior work reported, one hedge for inference; no causal verbs without controlled designs behind them
- Citations attach to claims at clause end, several papers per claim where they genuinely share the claim; never cite the user's own findings
- Zero banned words (novel, leverage, robust, seamless, moreover, furthermore, delve, landscape...), zero em-dash asides, no rhetorical-question transitions

### 4. Fairness pass
Reread every sentence that characterizes prior work and ask: could I say this to the paper's authors' faces? A reviewer is likely among the cited authors. Criticism must be specific, accurate, and preceded by a fair account of what the work accomplished. Paraphrase, never copy — including never copying from other papers' related-work sections, which is plagiarism even when it describes third-party work.

### 5. Verify against the checklist
Run the "Before you send it" checklist and the reference table in `chi-writing-style.md` against the finished draft — after drafting, not during. Where feasible, compute the measurable targets (sentence length mean/SD, banned-word count, contrast-frame count per 1,000 words) with a quick script rather than estimating. Report the numbers to the user alongside the draft, and note any target missed and why (sometimes the honest sentence beats the metric; say so rather than padding).

### 6. Deliver
Output the section as a markdown file (or LaTeX if the user's project is LaTeX — match `\cite{key}` commands to the .bib keys exactly). Include at the end, outside the section text: the metric report, any `[CITATION NEEDED]` items, and 1–3 sentences on structural choices a co-author should sanity-check.

## Failure modes to refuse
- **The laundry list**: one paper per sentence, summaries in reading order. Restructure by idea.
- **The strawman contrast**: a "rather than" frame against a position nobody holds. Name the real alternative.
- **The overclaimed gap**: "no work has examined X" when work plausibly has. Write "we are aware of no work that..." only if the bibliography was actually searched for it, otherwise soften to "little work".
- **Uniform prose**: every sentence 19 words, every paragraph closed with "together, these show". Vary or it reads as machine output.
