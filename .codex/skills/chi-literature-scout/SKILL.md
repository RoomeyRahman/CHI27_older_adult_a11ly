---
name: chi-literature-scout
description: Find, verify, and organize academic literature for an HCI/CHI-style paper or proposal, and write the results into a references.bib file. Use this skill whenever the user asks to find related work, build or update a bibliography or .bib file, identify papers for a literature review, map research streams, find research gaps, or asks "what has been published on X". Also trigger when the user shares a research proposal or draft and wants supporting citations. Prioritizes recent work from top venues (CHI, CSCW, DIS, TOCHI, FAccT, ASSETS, UIST, UbiComp/IMWUT, ACL, IEEE, Nature/Science family) and never invents citations — every entry must be verified by web search before it enters the .bib file.
---

# CHI Literature Scout

Build a verified, prioritized bibliography for an HCI research project, and hand off a structured literature map that the `chi-litreview-writer` skill (or a human) can write from.

**The one hard rule: never invent a citation.** Every BibTeX entry must be verified against a real source (ACM DL, publisher page, arXiv, Google Scholar result, Semantic Scholar, DBLP) via web search or web fetch *in this session*. If a paper cannot be verified, it does not go in the .bib file — it goes in a clearly-marked "unverified leads" list instead. A fabricated reference is the single worst possible output of this skill.

## Workflow

### Step 1 — Decompose the topic before searching

Read the user's proposal/topic and extract 3–6 **research streams** — the distinct bodies of literature the work sits at the intersection of. For a multi-stakeholder eldercare-AI proposal, for example, the streams might be: (a) medication adherence technology, (b) multi-stakeholder / caregiver-mediated health tech, (c) AI alignment with multiple principals, (d) HCI4D / technology use in the Global South / intermediated use, (e) aging, autonomy, and dignity in design.

For each stream, write down:
- 2–4 search query variants (include venue names in some: e.g. `"proxy use" older adults CHI`, `multi-stakeholder alignment agents`)
- The 1–2 canonical/foundational papers you expect to exist (to verify, not to assume)
- What the stream needs to *do* for the paper (background, gap, method precedent, contrast target)

Confirm the streams with the user if the topic is ambiguous; otherwise proceed.

### Step 2 — Search, wide then deep

For each stream, run web searches. Useful patterns:
- `<topic keywords> CHI 2024` / `CSCW 2025` / `site-free venue mentions` (do NOT use the `site:` operator)
- `<topic> ACM Digital Library`
- `<seminal author name> <topic>` once a key author surfaces
- Follow citation trails: fetch the landing page of a strong hit and mine its abstract and, where visible, its references for further leads

Prioritization order when deciding what makes the cut:
1. **Relevance to the specific research questions** — a mediocre-venue paper that is exactly on point beats a CHI best paper that is adjacent
2. **Venue tier** — CHI, CSCW, TOCHI, DIS, UIST, IMWUT/UbiComp, ASSETS, FAccT, ACL, top IEEE venues, high-impact journals
3. **Recency** — last 5 years preferred for the empirical front; older is fine (and expected) for foundational theory
4. **Influence** — highly cited or clearly field-shaping papers, even if older

Target roughly 25–50 papers for a full paper's bibliography, fewer if the user asks for a focused subtopic. Balance across streams; a review with 30 papers in one stream and 2 in another signals a hole.

### Step 3 — Verify every candidate

For each paper that will enter the .bib file, confirm via search result or fetched page: exact title, authors, year, venue, and ideally DOI. Small metadata details (page numbers) may be omitted rather than guessed. If two sources disagree on a detail, prefer the publisher/ACM DL version.

Anything you could not confirm goes into `unverified-leads.md` with a note on what's uncertain — never into the .bib.

### Step 4 — Write the outputs

Produce three files (in the working directory, then present them):

**1. `references.bib`** — verified entries only. Use consistent citation keys: `firstauthorYEARkeyword` (e.g. `sultana2019parareligious`). Group entries with `% ==== Stream name ====` comment headers. Use correct entry types (`@inproceedings` for CHI/CSCW/DIS papers, `@article` for journals including PACM HCI — note CSCW papers since 2018 are `@article` in *Proc. ACM Hum.-Comput. Interact.*). Include `doi` whenever found.

**2. `literature-map.md`** — the analytical layer, organized per stream:
- **Stream overview**: what this body of work has established (2–3 sentences)
- **Key papers table**: citation key | authors + year | objective | method | sample/data | main finding | limitation | relevance to this project
- **Agreements**: what multiple studies converge on
- **Conflicts**: where findings disagree, and what sample/method differences might explain it
- **Theories/models in play** (e.g., intermediated use, relational autonomy, principal-agent framing)
- **Recurring limitations** the literature itself admits
- **The gap this stream leaves open** — one gap per stream, stated as: what is known / what is unknown / why it matters / a possible RQ

End the map with a ranked list of the top research gaps across streams (strongest first) with a one-line justification each.

**3. `unverified-leads.md`** — papers that looked promising but could not be verified, clearly labeled `⚠ NOT VERIFIED — do not cite without checking`, plus suggested follow-up searches.

### Step 5 — Report honestly

In the chat summary, state: how many papers were verified, which streams are thin (and why — genuinely sparse literature vs. search limitations), and which canonical papers you expected but could not verify. Recommend the user spot-check 2–3 entries in the ACM DL before submission, since even verified web metadata occasionally drifts.

## Guardrails

- No `site:` operators, no quotes-heavy queries; keep queries 2–6 words.
- Do not summarize a paper beyond what its abstract/landing page supports. If you only saw the title, say so in the map ("title-level relevance only").
- Do not copy abstract text into the map — paraphrase in one or two sentences.
- If the user names a specific paper you cannot find, tell them plainly rather than substituting a similar-sounding one.
- When updating an existing references.bib, preserve existing entries and keys; append and de-duplicate (check by DOI and title, not key).
