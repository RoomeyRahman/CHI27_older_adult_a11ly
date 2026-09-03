# Extraction fields and CHI vocabulary

## Contents
1. JSON record schema
2. CHI/HCI controlled vocabulary (contribution types, study types, instruments, analyses)
3. Where to find each field in a typical CHI paper
4. Worked example
5. Missing-value conventions

---

## 1. JSON record schema

One file per paper at `extractions/<paper_id>.json`.

`paper_id` = first author surname + year + short slug, e.g. `rahman2023glucose`. Set `bib_key` to the matching key from `bib_index.json` — prefer the real BibTeX key over your own `paper_id` so cells paste straight into LaTeX. If a paper has no bib entry, set `bib_key` to `null` and note it; the user needs to add it to their `.bib` before citing it.

`knowledge_ids` stays empty during Stage 2 and is filled in during Stage 5, once consolidation has decided which final statement each paper supports.

```json
{
  "paper_id": "rahman2023glucose",
  "bib_key": "rahman2023glucose",
  "filename": "rahman_chi2023.pdf",
  "citation": {
    "authors": "Rahman, S., Lee, J., & Okafor, A.",
    "year": 2023,
    "title": "Exact title from the title page",
    "venue": "CHI '23",
    "doi": "10.1145/... or Not reported",
    "verified_from_file": true
  },
  "contribution_type": ["empirical", "artifact"],
  "research_question": "As stated by the authors, quoted structure not quoted words",
  "theory": "Name of framework, or Not reported",
  "study_type": "lab study",
  "sample": {
    "n": 24,
    "population": "university students, 19-27, no prior VR experience",
    "country": "South Korea",
    "recruitment": "campus mailing list",
    "compensation": "Not reported"
  },
  "apparatus_or_system": "What was built or used; note if it is the paper's own artifact",
  "tasks": "What participants actually did",
  "measures": ["NASA-TLX", "task completion time", "custom trust scale (7-pt)"],
  "analysis": "repeated-measures ANOVA; thematic analysis of exit interviews",
  "key_findings": [
    {
      "claim": "Paraphrased finding in one sentence",
      "evidence": "F(2,46)=8.21, p<.01, partial eta2=.26",
      "direction": "condition B reduced workload vs baseline",
      "page": "p. 6"
    }
  ],
  "design_implications": ["As stated by authors", "..."],
  "author_limitations": ["Short exposure (single session)", "..."],
  "unstated_limitations": ["[inferred] No comparison against the commercial baseline"],
  "quote": {"text": "under 15 words, only if wording matters", "page": "p. 7"},
  "candidate_themes": ["trust calibration", "workload"],
  "knowledge_ids": ["K3"],
  "focus_relevance": "core | peripheral | background — against the focus argument",
  "relevance_to_topic": "One sentence tying it to the user's stated topic and focus",
  "evidence_strength": "Moderate — adequate N and preregistered analysis, but single-session lab only",
  "flags": []
}
```

Put `"⚠ unverified: venue"` style strings in `flags` for anything Stage 3 could not confirm.

---

## 2. CHI/HCI controlled vocabulary

Use these values so grouping and counting stay consistent across the corpus.

**Contribution type** (after Wobbrock & Kientz's taxonomy of HCI contributions): `empirical`, `artifact`, `methodological`, `theoretical`, `dataset`, `survey/review`, `opinion`. Papers often carry two — a system plus its evaluation is `artifact` + `empirical`.

**Study type**: `controlled lab study`, `within-subjects experiment`, `between-subjects experiment`, `field deployment`, `diary study`, `semi-structured interview`, `focus group`, `survey`, `log/trace analysis`, `co-design workshop`, `technology probe`, `Wizard-of-Oz`, `autoethnography`, `heuristic/expert evaluation`, `secondary analysis`, `simulation`.

**Standard instruments** worth recording verbatim when present, because they enable cross-paper comparison: NASA-TLX, SUS, UEQ/UEQ-S, AttrakDiff, IMI, PANAS, SUM/UMUX-LITE, Trust in Automation (Jian et al.), Godspeed, PSSUQ, System Causability Scale, TAM/UTAUT items, presence questionnaires (IPQ, SUS-presence), CSI (Creativity Support Index).

**Analysis**: `ANOVA`, `mixed-effects / LMM`, `regression`, `non-parametric (Friedman/Wilcoxon)`, `Bayesian`, `descriptive only`, `thematic analysis`, `grounded theory`, `content analysis`, `affinity diagramming`, `discourse analysis`, `mixed methods`.

**Recurring CHI limitations** — check whether each applies, because these are what the field's reviewers already know to look for: WEIRD/convenience sample, small N, single session, novelty effect, lab ecological validity, self-report bias, no longitudinal follow-up, single cultural context, prototype fidelity, no accessibility coverage, English-only, researcher-built baseline, no preregistration.

---

## 3. Where to find each field

| Field | Usual location |
|---|---|
| Citation, venue, year | Title page header, ACM strip at the foot of page 1 |
| Contribution claim | Last paragraph of the introduction ("we contribute…") |
| Research question | End of intro or start of method |
| Theory | Related work, or a named subsection |
| Sample, apparatus, tasks, measures | Method / Study Design |
| Findings with statistics | Results, figures and their captions |
| Interpretation, design implications | Discussion |
| Stated limitations | "Limitations" subsection near the end, sometimes folded into Discussion |

Figure captions in HCI papers often carry the cleanest statement of an effect. Read them.

---

## 4. Worked example (Column-2 style)

**Bad (stapled summaries):** "Smith et al. (2021) found A. Lee et al. (2022) found B. Chen (2023) found similar."

**Good (synthesis):** "Interruptibility models built on phone-sensor features predict receptivity well within a session but degrade over weeks as routines shift, an effect reported across three deployments (Smith et al., 2021; Lee et al., 2022; Chen, 2023); none retrained the model in situ."

The good version states one claim, cites the support, and names the shared blind spot — which is what makes the gap column writable.

---

## 5. Missing-value conventions

- `Not reported` — the paper genuinely does not state it. Common for compensation, ethics approval, sample demographics.
- `Not verifiable from file` — the file is scanned/corrupt/truncated, so the information may exist but could not be read.
- `Not applicable` — e.g. sample size for a purely theoretical contribution.

Never leave a cell blank, and never write `unknown` — a reader cannot tell which of the three situations produced it.
