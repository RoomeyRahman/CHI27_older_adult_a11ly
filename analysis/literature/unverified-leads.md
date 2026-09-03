# Unverified Leads

**⚠ NOT VERIFIED — do not cite anything in section A without checking it first.** Nothing in section A is in `references/reference.bib`. Sections B onward describe entries that *are* filed, and what about each of them still needs a human check.

Compiled 2026-09-02 alongside `literature-map.md`; revised the same day across three reductions, to 150 entries, then 146, then 122.

Numbers in brackets are citation keys in `references/reference.bib`, which runs `1`–`122`.

---

## A. Papers expected to exist that this session could not verify

Searched by title, author, and topic through Crossref and OpenAlex without a confident match. They are almost certainly real; the failure is in the search, not the paper. Resolve each in the ACM Digital Library or Google Scholar before citing.

| Expected work | Why it matters here | What went wrong | Follow-up search |
|---|---|---|---|
| Ahmed, Jackson, Ahmed et al., *Protibadi: A Platform for Fighting Sexual Harassment in Urban Bangladesh*, CHI 2014 | The most-cited Bangladeshi HCI system paper; useful for establishing the country's HCI record | Four separate query formulations returned unrelated papers; the DOI was never surfaced | ACM DL search for "Protibadi" restricted to CHI 2014 proceedings |
| Sultana, Ahmed, Bardzell, *Shifting Sands of Labor* (patriarchy and labor in Bangladesh) | Would strengthen the structural-power reading of allegiance shifts | No match in either service under any tried phrasing; the exact title may differ | ACM DL author search on Sharifa Sultana, list all CHI and CSCW entries |
| Vines et al., *An Age-Old Problem: Examining the Discourses of Ageing in HCI*, TOCHI (c. 2015) | The founding critique of deficit framing in aging HCI; [66] partially substitutes | Searches returned other Vines and Lazar papers; the title may be misremembered | ACM DL author search on John Vines, filter TOCHI |
| Berridge, *Active Subjects of Passive Monitoring* (older adults and monitoring, *Ageing and Society* or similar) | The strongest sociological account of monitoring from the monitored person's side | Query returned unrelated gerontology and robotics papers. The related Berridge and Grigorovich paper on digital ageism was verified, but it was cut in the reduction to 150 | Author search on Clara Berridge in a gerontology database, then match by year |
| Sabie and Ahmed, refugee and displacement HCI work in Bangladesh | Would extend the Bangladesh corpus beyond the papers filed | Searches returned refugee-studies work by other authors | ACM DL author search on Dina Sabie |
| Chalmers and Galani (or Chalmers and MacColl), seamful design in ubiquitous computing | The named rival to a smooth ceremony in the theory ledger; [28] is filed as the modern statement | Only a 2003 IEE wearable-computing paper and unrelated 2022 work surfaced | Search "seamful design" restricted to UbiComp 2003–2005 |
| Caine, Fisk, Rogers, older adults' privacy attitudes toward in-home visual sensing (HFES or *Gerontechnology*, c. 2006) | Early empirical baseline for monitoring acceptance | Only a PsycEXTRA stub and an HFES proceedings abstract surfaced, neither a citable full record | HFES proceedings search on Kelly Caine, 2005–2010 |
| WHO, *Adherence to Long-Term Therapies: Evidence for Action* (2003) | The standard global adherence statistic source | Crossref and OpenAlex return journal summaries and reviews of the report, not the report itself | Cite the WHO report directly from the WHO publications page as a `@techreport`, with the ISBN |
| Kittay, *Love's Labor: Essays on Women, Equality, and Dependency* (1999) | Dependency-work theory that would complement Tronto [112] and Mol [80] | Searches returned commentary and related feminist work only | Publisher page (Routledge) for the ISBN and edition |
| Puig de la Bellacasa, *Matters of Care: Speculative Ethics in More Than Human Worlds* (2017) | Care theory now common in DIS and CHI care work | Only *Hypatia* and *Configurations* reviews carry DOIs | University of Minnesota Press page for the ISBN |
| Hristova et al., *Snapchat Streaks: How Adolescents Metagame Gamification in Social Media* (2019) | Would strengthen the streak-grief evidence base | Exists only as an OSF preprint (`10.31234/osf.io/nszex`); no peer-reviewed venue found | Check whether it appeared in a venue; otherwise cite the peer-reviewed [46], which is filed |
| Russell, *Human Compatible: Artificial Intelligence and the Problem of Control* (2019) | General-audience statement of the control problem | Verified via OpenAlex and filed in the 313-entry bibliography, then cut in the reduction to 150 because no paragraph depended on it | Restore from `references/reference.bib.bak-313` if the Discussion needs it |
| Sambasivan et al., *"Privacy is not for me, it's for those rich women"* (SOUPS 2018) | Performative privacy practices among women in South Asia | Verified via OpenAlex and the USENIX listing, filed, then cut in the reduction to 150. USENIX papers carry no DOI | Restore from `reference.bib.bak-313`; check the page range against the SOUPS 2018 proceedings |
| Toyama, *Geek Heresy*, and Sen-style capability critiques of ICTD | Background for the asset-based stance | Not searched systematically; out of scope for this pass | Deliberate follow-up pass if the Discussion needs a development-theory anchor |

## B. Filed entries with verification caveats

These **are** in `references/reference.bib`. Each carries a `note` field stating its caveat. Read the note before citing a page number or a venue.

| Key | Caveat | What to check |
|---|---|---|
| [80] Mol, *The Logic of Care* | Book with no publisher DOI. Existence, title, year, and publisher verified through the review record `10.3384/cu.2000.1525.124533` and two further reviews | Edition and page numbers against the Routledge print edition before any page-level citation |
| [34] Goffman, *The Presentation of Self in Everyday Life* | Book, no publisher DOI, many editions in circulation | Which edition the project cites; pagination differs between the Doubleday 1959 printing and later ones |
| [112] Tronto, *Moral Boundaries* | Book, verified via OpenAlex only (no DOI) | Publisher and year against the Routledge record; the four phases of care are usually cited to specific pages |
| [60] Kretzmann and McKnight, *Building Communities from the Inside Out* | Book, verified via OpenAlex (no DOI); review record `10.2190/PD41-GKWW-RU7X-M7Y4` corroborates | Publisher (ACTA Publications) and year. Per CLAUDE.md this is named once in Method and never claimed as a contribution |
| [72] Mackenzie and Stoljar (eds.), *Relational Autonomy* | Crossref deposits no author or editor names for this Oxford record; the editors were entered from the publisher page | Whether the project cites the collection or an individual chapter in it |
| [38] Hadfield-Menell et al., *Cooperative Inverse Reinforcement Learning* | Not in Crossref (NIPS proceedings of that era were not deposited). Verified via the OpenAlex record for arXiv:1606.03137 | Whether to cite the NIPS 2016 proceedings version or the preprint, and the page range if the former |
| [105] Sorensen et al., *A Roadmap to Pluralistic Alignment* | Not in Crossref. Verified via the OpenAlex record for arXiv:2402.05070. The ICML 2024 attribution comes from the paper's own venue claim, not from a publisher record | The PMLR volume and page numbers before citing it as a conference paper |
| [37] Gupta and Pillai, *Elder Caregiving in South-Asian Families* | No DOI is registered. Metadata carried over from the pre-existing bibliography and corroborated by the PDF filed in `/references/`. No abstract exists in either service, so the literature map claims no finding for it | Volume, number, and page range against the filed PDF |
| Ryan and Deci, *Self-Determination Theory* | Verified against the Crossref record for `10.1521/978.14625/28806`, which deposits no author names; the authors were entered from the Guilford Press page. A generated author-less duplicate of this record was removed before renumbering | That the DOI resolves to the book, not a review, at submission time |

## C. Filed entries whose metadata is thin

- **No abstract in either service** for [43] (feminist care ethics toolkit), [63] (TRIO framework), [67] (Lee and See on trust in automation), [106] (Star and Strauss), and [37] (Gupta and Pillai). The literature map marks [43] and [37] as *title-level relevance only* and claims no finding for them. The other three are well-known works whose content is not in doubt, but no sentence in the map is sourced to an abstract that does not exist.
- **CHI 2026, DIS 2026, and FAccT 2026 entries** were deposited recently. Page numbers may be absent or provisional; check them at submission time.
- **Citation counts are not a quality signal for recent work.** Any count quoted in the literature map for a 2025 or 2026 paper is an artifact of recency.
- **One entry is a doctoral-consortium research statement**, not a full paper: Zakreuskaya, 2025, on collaborative medication reconciliation. Cite it as a position piece or drop it.

## D. What was done to `reference.bib`

Five passes, each backed up before it ran.

1. **Literature pass.** 215 verified entries appended to the pre-existing 99, and one pre-existing duplicate key (`10.1145/3517428.3544830`, entered twice with identical content) removed. State before this pass: `references/reference.bib.bak-20260902`.
2. **Renumbering.** All keys replaced with sequential integers, assigned in the alphabetical order (first author family name, then year, then title) that ACM-Reference-Format prints the bibliography in, so a bracketed number in a draft compiles to a `\cite` of the same number and prints as that number. This is what `.claude/skills/latex/scripts/md2tex.py` expects, since it converts a bracketed list of numbers directly into a `\cite` of the same keys. State before this pass: `references/reference.bib.bak-prenumber`.
3. **Cut to 150.** An entry was kept only if it carries analytic load somewhere in the project: a full key-paper row in `literature-map.md` (objective, method, sample, finding, limitation, and relevance all written out), a row in `analysis/theory-ledger.md`, or a named place in the ranked research gaps. That rule kept 150 and cut 163. State before this pass: `references/reference.bib.bak-313`.
4. **Cut to 146.** The rule was tightened to a single auditable test: an entry stays only if it has a full key-paper row in `literature-map.md`. Four entries failed it and were removed, listed below. A duplicate check was run at the same time and found no duplicate DOI and no duplicate title in the file. State before this pass: `references/reference.bib.bak-150`.

**The four entries the tightened rule removed.**

| Entry | Why it had no row | Consequence |
|---|---|---|
| Khanuja 2025, DIS, *Designing Aging Reflection Probes to Elicit Self-Perception of Aging Beliefs of Older Adults in India* | A research statement about the author's own programme rather than a study with reportable findings | None. It and the entry below were the clearest near-duplicate pair in the file, two outputs of one project |
| Khanuja 2026, DIS, *Designing Culturally Grounded Reflection Cards That Explore Self-Perception of Aging* | A pictorial from the same project as the entry above | Ranked gap 4, on the thinness of South Asian ageing HCI, now points to [86] and to the three promoted reviews outside HCI instead |
| Paris et al. 2026, FAccT, *Don't Trust the Process: When Verifiability Undermines AI Accountability* | Cited only in the Stream 3 conflicts paragraph and the pipeline notes, never given a row | **This is the one loss worth reconsidering.** It was the named counter-evidence to the assumption that decision logs settle accountability. The caution survives in the map as a plain statement, but without a citation behind it |
| Srinivasan et al. 2026, IUI, *Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance* | Cited only in the Stream 3 theories paragraph and the theory ledger, never given a row | The trust-calibration ledger row now rests on [67] Lee and See alone, which still carries it |

5. **Cut to 122.** A stronger test replaced the row rule, because a row was not evidence of anything: I had written one for every paper I selected. The test became **used in at least one sentence of the map's prose, a theory-ledger row, or a ranked gap**. Thirty-four entries failed it, existing only as a table row. Ten of those were kept anyway and given real prose work, because the failure was the map's and not the paper's: [89] Pradhan et al. 2020 on voice assistants among older adults with low technology use, [21] Coghlan et al. 2021 on dignity, autonomy, and style of company, [63] the TRIO framework, [56] Kim et al. 2026 on patient agency in home-based care, [74] Mathur et al. 2022 on conversational medication check-ins, [114] Wang et al. 2021 *Brilliant AI Doctor*, [77] Merrell et al. 2005 and [37] Gupta and Pillai 2013 on South Asian family caregiving, [117] Yang et al. 2024 Talk2Care, and [12] the WHO World Report on Ageing. The other 24 were removed. State before this pass: `references/reference.bib.bak-146`.

**The 24 the prose test removed**, by reason.

- **Method gestures with no analytic work in the paper:** Gaver et al. 2004 on cultural probes (a one-page essay), Light and Akama 2012 on facilitation, Vines et al. 2013 on configuring participation, Hsu et al. 2025 *Research as Care* (no abstract exists in either service). Dropping these means the Method section no longer gestures at a participatory-design lineage, which some Associate Chairs read for. That was a deliberate call and it is reversible.
- **Adjacent monitoring and privacy:** Read et al. 2022's scoping review, Zou et al. 2024 on privacy across contexts, Berridge and Grigorovich 2022 on digital ageism in nursing homes, Pel-Littel et al. 2021 on shared decision-making.
- **Adjacent family-communication probes:** Brereton et al. 2015 *The Messaging Kettle*, Vutborg et al. 2010 on grandparent storytelling, Soubutts et al. 2021 on stairlifts, Cuadra et al. 2026 on Privacy Cards.
- **Reviews the argument does not lean on:** McHugh et al. 2025, Lucchini et al. 2026.
- **Off-domain or off-question:** Rao Gadahad et al. 2026 (walking adherence, not medication), Schroeder et al. 2019 on goal-directed tracking, Fazelpour and Suresh 2025 on disagreement, Yu et al. 2024 on help-seeking urban robots, Bhat et al. 2023 on telemedicine, Chen 2022 on left-behind caregivers in China, Sultana et al. 2020 *Parareligious-HCI* (a CHI extended abstract).
- **Cluster redundancy in the voice-assistant group:** Harrington et al. 2022 on code-switching, Lazar et al. 2016 on robotic pets, Upadhyay et al. 2023 on long-term voice-assistant use. [90] and [117] carry that cluster now.

**On duplicates.** No literal duplicate exists: every DOI and every title in the file is unique, checked after each pass. Two remaining pairs are two papers about one system rather than duplicate records, and both were kept deliberately because the map gives each a distinct job: [82] Mynatt et al. 2001 introduces the digital family portrait and [94] Rowan and Mynatt 2005 reports its year-long field trial, the first standing as the founding awareness system and the second as our deployment-length precedent. Say the word and one of them goes.

State before this pass: `references/reference.bib.bak-150`.

**How the cut was decided.** An entry was kept only if it carries analytic load somewhere in the project: a full key-paper row in `literature-map.md` (objective, method, sample, finding, limitation, and relevance all written out), a row in `analysis/theory-ledger.md`, or a named place in the ranked research gaps. **What the first cut removed, in three groups.**

- **67 tail entries** that appeared in the map only inside an "Additional verified entries in this stream" list with a one-line relevance note. Those lists are gone from the map. The papers are verified and recoverable; they were adjacent rather than load-bearing.
- **95 pre-existing entries** that the literature pass never cited. Most are generic technology-acceptance and technology-for-older-adults papers whose framing CLAUDE.md Section 2 supersedes: reviews of eHealth acceptance, medication-reminder usability studies, social-robot reviews, and similar. Cutting them is a framing decision as much as a length decision, and it is reversible.
- **7 entries with full map rows** whose work a kept neighbour already carries: Adelman et al. 2000 on triadic physician communication (covered by [63], the TRIO framework), Caraban et al. 2020 *The Nudge Deck* (covered by the 23-Ways-to-Nudge review), Cherian et al. 2021 on medication activity recognition (which the map labelled a contrast case), Ho 2020 on readiness for AI health monitoring (a debate article), Neustaedter and Greenberg 2012 on video chat in long-distance relationships (the intergenerational case is covered by the grandparent storytelling entry), Read et al. 2022 in *JMIR Aging* (covered by the same authors' scoping review), and Snow et al. 2021 *Neighbourhood Wattch* (covered by the same authors' *Household Wattch*).

**Six pre-existing entries were promoted into the kept set** and given full map rows, because the new corpus had no substitute for them: [5] Akter et al. 2025 on ageing in Bangladesh, [90] Rahman et al. 2025 on caregiving in the Indian subcontinent, [51] Jahangir et al. 2025 on intergenerational support in South Asia, [37] Gupta and Pillai 2013 on South Asian family caregiving, [74] Mathur et al. 2022 on conversational medication management with mild cognitive impairment, and McHugh et al. 2025 on caregiver-intervention outcomes. The last of those was cut again in the third pass; the other five stand, and without the first four the paper would have had no citable Bangladeshi or South Asian ageing source.

**Restoring anything.** `reference.bib.bak-146`, `.bak-150`, and `.bak-313` hold the earlier states under their own numbering. Find a paper in one of them, copy its entry, and append it to the live file as `123`. Do not renumber the live file; the literature map, the theory ledger, and any draft all depend on the current numbers.

## E. Searches still worth running

1. **ACM DL author sweeps** for Syed Ishtiaque Ahmed, Sharifa Sultana, Nova Ahmed, and Dina Sabie, to close the Bangladesh gap in section A properly rather than by topic query.
2. **CSCW 2026 and DIS 2026 late deposits.** This search ran on 2026-09-02; papers accepted for late-2026 venues may not yet be in Crossref.
3. **A dedicated pass on triadic clinical communication.** Only [63], the TRIO framework, survives the cuts; the Adelman review of older patient and physician communication and the Pel-Littel review of shared decision-making with multimorbidity were both removed. This literature has studied the three-party decision problem for decades and is now the thinnest part of the bibliography relative to its usefulness for RQ2; look in *Patient Education and Counseling* and *Social Science and Medicine*.
4. **Multi-user smart home and shared-account conflict** (Zeng, Geeng and Roesner, and successors). Topic queries surfaced adjacent work but no clean set; this is the closest technical analogue to a household agent with divided loyalty.
5. **Bangladeshi and South Asian gerontology outside HCI**, in *Ageing and Society*, *BMC Geriatrics*, and *Journal of Cross-Cultural Gerontology*. The promoted entries [5], [90], [51], and [37], plus [77] on Bangladeshi carers in Wales, cover the minimum; a targeted pass would give the Motivation section better population and caregiving-structure facts.
6. **Commercial agent-permission models**, if the system section needs to position the Affiliation Ledger against published technical reports on agent permissions and delegation. None were searched in this pass.
