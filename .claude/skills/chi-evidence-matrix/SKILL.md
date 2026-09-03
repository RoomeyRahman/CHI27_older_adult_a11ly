---
name: chi-evidence-matrix
description: Extract findings from a corpus of HCI/CHI papers (10 to 200+ PDFs) and consolidate them into a small final table of what the field already knows, with citation keys drawn from the user's .bib file and an empty column reserved for the author's own contribution. Use this whenever the user points at a folder of papers, a literature review, or a .bib file and wants key-findings extraction, an evidence matrix, a synthesis or comparison table, theme grouping across many papers, agreement/conflict analysis, or research-gap identification — including phrasings like "summarize my literature," "organize my related work," "what is already known," "build a table from these papers," or "what can my work extend." Trigger even when the user does not say "evidence matrix," and trigger for HCI-adjacent venues (CHI, CSCW, UIST, DIS, IMWUT/UbiComp, TOCHI, IUI, MobileHCI, CHI PLAY, ASSETS).
---

# CHI Evidence Matrix

Turn a corpus of papers into a **short** final table of established knowledge — typically 8–12 knowledge statements from 100 papers — with a column deliberately left empty for the author's own contribution.

The deliverable is a table, not an essay. The user writes their own Results and Discussion; this skill builds the scaffolding they write into.

## Invocation arguments

Accept these from the user's request. Ask once for anything missing that is required, then proceed without further check-ins.

| Argument | Required | Meaning |
|---|---|---|
| `papers` | yes | Path to the corpus (folder of PDFs, or a single file). Default `/references/` in this repository. |
| `bib` | recommended | Path to the `.bib` file for the literature review. Supplies the ground-truth citation keys used in every table cell. Default `/output/reference.bib` if it exists; otherwise run without one and report every key as unresolved. |
| `focus` | recommended | Free-text instruction steering the whole analysis — the lens, construct, population, or angle that matters. See below. |
| `year_range` | no | What counts as "recent" for this literature, e.g. `2019-2026`. |
| `max_knowledge` | no | Cap on rows in the final table. Default 12. |
| `out` | no | Output directory. Default `/analysis/` in this repository. |

Example invocation, using this project's defaults:

```
papers: references/
bib: output/reference.bib
focus: "Center on agents that serve more than one principal inside a household.
        Treat the single-principal assumption in alignment work, the passive
        posture of caregiver dashboards, and intermediated use in the Global
        South as the three literatures to position between. Ignore adherence
        intervention trials unless they report how family members were involved."
year_range: 2015-2026
max_knowledge: 12
```

**Standing use in this repository.** CLAUDE.md Section 2.6 names three literatures the paper must occupy the
intersection of: alignment and agentic AI under the single-principal assumption; CSCW caregiver dashboards and
shared health monitoring; Bangladesh and Global South HCI on proxy use and family mediation. Run this skill with
a focus naming whichever of the three is being written, and report the per-literature paper count, because
`/references/` currently leans toward caregiving and aging reviews and the other two are thin. This skill also
produces the `/references/` index that `/plan-section` and `/draft` deduplicate candidates against; Table 2 is
that index.

### How `focus` is applied

The focus argument is not a filter applied at the end — it changes every stage, which is what makes a 100-paper run tractable:

- **Screening**: papers irrelevant to the focus are logged in `excluded.md` with a one-line reason, not extracted. Never delete them silently; the user needs to defend the corpus.
- **Extraction**: findings that speak to the focus get full treatment (effect direction, statistics, page anchors); off-focus findings get one line.
- **Consolidation**: the focus supplies the axis along which knowledge statements are grouped. A focus on "explanation modality as moderator" produces different, better-aligned knowledge statements than a generic topical grouping.
- **Gaps**: ranked by relevance to the focus first, general originality second.

If no focus is given, ask for one before extracting — for a large corpus, working without it produces generic themes that are hard to write against. If the user declines, derive a provisional focus from the `.bib` file's contents and state it explicitly for confirmation in one line.

## Non-negotiable rules

These matter because a fabricated citation or an invented sample size will survive into a submitted paper and damage the author.

1. **Three provenance markers, always distinguishable.**
   - unmarked = read from the paper file;
   - `[inferred]` = your reasoning over what the paper says (e.g. a limitation the authors did not state);
   - `[background]` = your own knowledge of the field, used for framing only.
   `[background]` is allowed and useful — for naming a theory correctly, situating a paper in a research lineage, or noting that a construct is measured inconsistently across HCI. It is **never** allowed to carry a citation, a number, a finding, or a sample size. Those come from the file.
2. **Every citation key must resolve.** A key appears in a table cell only if it exists in the supplied `.bib` file or corresponds to a file in the corpus. Never write a citation from memory. Keys that cannot be resolved are listed in `unresolved_citations.md` rather than being quietly used.
3. **Never invent citations, DOIs, years, venues, participant counts, or effect sizes.** Read them off the title page and the method section.
4. **Do not analyze or speculate about the user's own results.** The final column is scaffolding. Fill it with the open question the literature leaves behind, phrased as `Gap: … → author to state contribution`. This pass deliberately precedes their own analysis so the prior-knowledge baseline stays uncontaminated.
5. **Quote sparingly.** Under 15 words, one quote per paper maximum, with a page number. Paraphrase everything else.
6. **Missing data is explicit.** `Not reported` (paper doesn't say), `Not verifiable from file` (unreadable/scanned), `Not applicable`. Never blank, never "unknown" — the reader can't tell those apart.

## Workflow

### Stage 0 — Setup and ledger

Resolve the arguments. Then:

```bash
python3 .claude/skills/chi-evidence-matrix/scripts/bib_index.py <bib> \
  --papers <papers> --out "$SCRATCH/work/bib_index.json"
```

Working files (`work/`) go in the scratchpad, not in the repository. Only the deliverables land in `<out>`.

This parses the `.bib` into a key→metadata index and matches entries to PDF filenames by title and author-year. Read its report: unmatched PDFs (in the folder, absent from the bib) and unmatched bib entries (cited but not downloaded) both matter, and the user usually wants to know about them before you spend an hour extracting.

Create `$SCRATCH/work/ledger.csv` with one row per paper: `paper_id, filename, bib_key, status (pending|extracted|excluded|unreadable), note`. Update it as you go. On a 100-paper corpus this ledger is the only thing standing between you and losing track of what has been done.

### Stage 1 — Screen against the focus

Read title + abstract only. Mark each paper `include` or `exclude` in the ledger with a reason. Report the counts (`104 found → 78 included, 26 excluded`) before extracting, and list the exclusion reasons grouped by kind. Screening 100 abstracts is cheap; extracting 100 papers is not.

### Stage 2 — Per-paper extraction

Process in batches of 10. Write one JSON record to `$SCRATCH/work/extractions/<paper_id>.json` **immediately after reading each paper**, then update the ledger. Incremental writes mean a failure at paper 63 doesn't cost the first 62.

Field list, CHI vocabulary, and worked examples: `references/extraction-fields.md`. Read it before the first extraction. For scanned or image-only PDFs, read the file with the Read tool's `pages` parameter rather than a text extractor, and mark anything still unreadable `Not verifiable from file`.

Note that many filenames in `/references/` are ACM DOI fragments (`3706598.3713582.pdf`) that carry no title, so the ledger's `filename` column is not a usable identifier on its own. Read the title page of each.

Read strategically: title page for metadata, the "we contribute" sentence at the end of the introduction, method for design/sample/measures, results (including figure captions, which in HCI papers often state effects most cleanly), discussion for interpretation and limitations.

After each batch of 10, report progress in one line. After the first batch, pause and show the user two complete records — if the granularity is wrong, fixing it at paper 10 is far cheaper than at paper 100.

### Stage 3 — Verification pass

Re-open every record and confirm four fields against the file: year, venue, participant count, and any numeric effect. These drift most easily. Confirm each `bib_key` against `bib_index.json`. Log failures to `$SCRATCH/work/verification_notes.md` and set `flags` in the record; flagged studies carry a ⚠ in the output.

### Stage 4 — Candidate themes (expansion)

Pool every `claim` across all records — a 78-paper corpus yields roughly 200–400 claims. Cluster them into candidate themes without worrying about the final count; expect 25–50. This stage is deliberately over-granular. Save to `$SCRATCH/work/candidate_themes.json`.

### Stage 5 — Consolidation (the reduction)

This is the stage that produces the deliverable, and the one most likely to be done badly. **Full procedure in `references/consolidation.md` — read it before starting.**

The core idea: candidate themes are not the answer. Papers in a healthy literature build on each other, so a claim first established in 2018, replicated in 2020, and extended to a new population in 2023 is **one** piece of knowledge with a lineage, not three themes. Collapse those. Target `max_knowledge` (default 12) final statements, each written as a *claim the field would endorse*, not a topic label.

Record every merge in `$SCRATCH/work/consolidation_map.json` so the reduction is auditable: the user must be able to see which of the 40 candidates became K3 and why. Reviewers ask.

Write the result to `$SCRATCH/work/synthesis.json` (schema: `python3 .claude/skills/chi-evidence-matrix/scripts/build_matrix.py --schema`).

### Stage 6 — Build and deliver

```bash
python3 .claude/skills/chi-evidence-matrix/scripts/build_matrix.py "$SCRATCH/work/" \
  --bib "$SCRATCH/work/bib_index.json" \
  --out <out>/chi_knowledge_table.xlsx --md <out>/chi_knowledge_table.md
```

The script validates every citation key against the bib index, refuses to silently drop unresolved ones, and emits the workbook plus a Markdown twin for Overleaf or Word. It performs no interpretation — all judgment lives in the JSON you wrote.

Report both paths in the terminal. Then write Table 2 a second time to `/references/index.md` as the repository's
citation index, one row per filed PDF: `filename | citation key | title | venue and year | which of the three
positioning literatures | which claim it supports`. That file is what `/plan-section` and `/draft` read to
deduplicate candidates and to resolve `[cite]` placeholders, and without it every literature run reopens the same
PDFs. Overwrite it on a rerun rather than appending.

## Output structure

Five tables. **Table 0 is the deliverable**; the rest are the audit trail that makes it defensible.

**Table 0 — Final knowledge table (primary, ≤ `max_knowledge` rows)**

| ID | Established knowledge (what the field knows) | How it was built (lineage across studies) | Evidence & consensus | Gap → extension for this work |
|---|---|---|---|---|

- **ID**: `K1…Kn`, ordered as they should appear in the write-up.
- **Established knowledge**: one declarative claim in the user's own voice, synthesized, no study named. If it reads like a topic ("trust in AI"), rewrite it as a claim ("users over-rely on confident explanations even when accuracy is unchanged").
- **How it was built**: the lineage — `Established \cite{a}; replicated \cite{b,c}; extended to older adults \cite{d}; boundary condition found \cite{e}`. This column is what turns 100 papers into a story.
- **Evidence & consensus**: `n studies; dominant methods; Strong / Moderate / Weak / Contested` plus a one-clause reason.
- **Gap → extension**: `Gap: … → author to state contribution`. Left open by design.

**Table 1 — Consolidation map**: `Candidate theme | Papers | Merged into | Reason for merge`. Shows 40 candidates reducing to 10 and why. Include unmerged singletons flagged `Thin evidence`.

**Table 2 — Evidence matrix (one row per paper)**: `Cite key | Study | Year | Venue | Country/Context | Research question | Theory | Sample | Method | Measures | Main finding | Stated limitation | Knowledge ID | Relevance`.

**Table 3 — Agreement and conflict**: `Claim | Supporting | Contradicting | Plausible reason for divergence (sample / method / measure / context) | Confidence`. The divergence column is the one reviewers reward — prefer a concrete methodological explanation over "results are mixed."

**Table 4 — Ranked gaps**: `Rank | Gap | Knowledge ID | What is known | What is unknown | Why it matters | Candidate research question | Feasible method | Originality | Feasibility`. Top 5, strongest first, one sentence per ranking.

## After the tables

Close with ≤150 words on the order in which K1…Kn should be presented in the write-up and why that order builds an argument. Then stop. Do not draft the user's Discussion.

## Common failure modes

- **Too many rows in Table 0.** Twenty-five "knowledge statements" from 100 papers means Stage 5 didn't happen. If two rows would be cited together in the same sentence of a related-work section, they are one row.
- **Topics instead of claims.** A row a reader cannot agree or disagree with is a heading, not knowledge.
- **Per-paper summaries pretending to be synthesis.** If the knowledge column names studies sequentially, rewrite it.
- **Lineage collapsed into a citation dump.** `\cite{a,b,c,d,e}` says nothing. Say who established, who replicated, who extended, and along what dimension.
- **Confidence inflation.** Three lab studies with N<20 on undergraduates is `Weak`, however consistent.
- **`[background]` doing work it shouldn't.** Framing, yes. Findings and citations, never.
- **Answering the last column.** Leaving it open is the point of this pass. In this repository it is also a rule:
  CLAUDE.md Section 6 forbids drafting our own findings into a literature artifact, and the last column stays
  `Gap: … → author to state contribution`.
- **A priority claim smuggled into a knowledge statement.** "No prior work has studied X" is unwriteable here
  (CLAUDE.md Section 2.5). State the gap descriptively so it survives a near-neighbour surfacing.
