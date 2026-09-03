# Synthesis, evidence grading, and gap ranking

> This file covers **candidate theme induction (Stage 4)**, evidence grading, conflict analysis, and gap ranking. The reduction of candidate themes into the small set of final knowledge statements (Stage 5) is a separate procedure in `consolidation.md` — read that one too.

## 1. Candidate theme induction (Stage 4 — expand, don't reduce)

At this stage, over-granularity is correct. Do not try to reach the final count here; 25–50 candidates from a large corpus is expected, and premature merging loses the distinctions that make Stage 5's lineage column possible.

Work from the `key_findings` entries pooled across all records, not from the papers as units. Papers usually contribute to more than one theme, and forcing one paper into one theme is what makes literature reviews read as annotated bibliographies.

Procedure:
1. Pool every `claim` string with its `paper_id`.
2. Group claims that make the same kind of statement about the same construct. Two claims belong together when swapping their citations would not change what the sentence asserts.
3. Name each theme as a noun phrase describing the *knowledge*, not the *topic*. `Interruptibility models decay over time` is a theme; `Interruptibility` is a topic heading.
4. Keep singletons at this stage. A claim made by one paper may turn out to be the boundary condition that sharpens a major statement in Stage 5 — merging it away now discards that.
5. Record each candidate with its supporting `paper_id`s and a one-line description of what it asserts. Stage 5 merges on meaning, so vague labels there become bad merges here.

Write the result to `work/candidate_themes.json`, then proceed to `consolidation.md`.

Grading (below) applies to the **final** knowledge statements, not to candidates — grade after consolidation, since replications only raise a grade once they have been merged into the statement they support.

## 2. Evidence strength grading

Grade per final knowledge statement, not per paper.

| Grade | Criteria |
|---|---|
| **Strong** | ≥4 independent studies, at least one outside a lab, convergent findings, adequate samples or saturation, replication across populations |
| **Moderate** | 2–3 studies, or more studies sharing one method/population; convergent but narrow |
| **Weak** | Single study, very small N without qualitative depth, descriptive statistics only, or all evidence from one research group |
| **Contested** | ≥2 studies pointing in opposing directions with no methodological explanation yet |

Independence matters: five papers from the same lab reusing one dataset is closer to one study. Check author overlap before grading `Strong`.

For qualitative streams, size is the wrong axis — grade on method transparency, reported saturation, participant diversity, and whether analysis procedure and coder agreement are described.

## 3. Detecting and explaining conflict

For each pair of opposing claims, test these explanations in order, because the first one that fits is usually the real answer and it is the sentence reviewers most want to see:

1. **Measure** — different instruments for a "same" construct (self-reported trust vs. reliance behaviour).
2. **Population** — students vs. domain experts, novices vs. long-term users, one culture vs. another.
3. **Setting** — lab vs. field, single session vs. multi-week.
4. **System fidelity** — research prototype vs. deployed commercial product.
5. **Analysis** — significance threshold, dropped participants, different baselines.
6. **Genuine disagreement** — only after 1–5 fail.

State the explanation as a testable proposition, since that is what converts a conflict into the user's research question.

## 4. Gap types to scan for

Run through this list explicitly rather than waiting for gaps to suggest themselves:

- **Population** — who has never been studied here (older adults, non-Western users, disabled users, low-literacy users, shift workers, clinical populations)
- **Geographic/cultural** — the corpus's country distribution, and what a Global South or South Asian context would change
- **Methodological** — everything is lab-based, or self-report only, or single-session
- **Temporal** — datasets or platforms that predate a relevant technology shift (e.g. LLM-based interfaces, on-device sensing)
- **Contradiction** — the conflicts from §3 that no study has adjudicated
- **Overlooked variables** — moderators nobody measured
- **Missing comparison** — a condition or baseline the field has never run head-to-head
- **Construct** — a term used inconsistently across papers, so results cannot be pooled

Count the corpus on each axis before claiming a gap. "No study examined X" is a strong claim; state it as "within this corpus of N papers, none examined X."

## 5. Ranking gaps

Score each candidate 1–5 on:
- **Originality** — is it actually unaddressed, or just unaddressed in the papers downloaded?
- **Significance** — does closing it change design practice or theory, or only add a data point?
- **Feasibility** — can it be done with plausible access, recruitment, and time?
- **Fit to venue** — would CHI reviewers recognize it as a contribution, and of which type?

Rank by significance × feasibility, break ties on originality, and write one sentence per rank explaining the placement. Rank honestly: a highly original but infeasible gap ranked first wastes the author's planning.
