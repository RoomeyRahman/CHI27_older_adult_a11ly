---
name: chi-introduction
description: Write, draft, restructure, or critique the introduction section of a CHI or HCI paper using the six-part structure (The Drop, World Building, The Players, Player One, The Deal, The Loot) and CHI-calibrated prose style. Use this skill whenever the user asks to write or improve an introduction for a CHI, CSCW, UIST, DIS, or other HCI venue paper, asks for help with a paper's opening, hook, research questions, gap statement, or contribution framing, or shares a draft introduction for feedback — even if they don't say "introduction" explicitly (e.g., "help me frame this paper", "my reviewers said the motivation is unclear").
---

# CHI Introduction Writer

Write introductions for CHI/HCI papers that make the rest of the paper feel inevitable. By the time a reviewer reaches the research questions, they should understand why those are the questions; by the contributions, why they matter. The reviewer should stop wondering what the paper is about and feel they are in good hands.

## Workflow

1. **Gather the raw material.** An introduction is written last for a reason: it ties together things that must already exist. Before drafting, you need to know (ask the user, or extract from any draft/notes they share):
   - The problem and why it hurts (stakes, who is affected)
   - Key concepts the reader must understand
   - The prior work landscape and the specific gap
   - The approach/methods and what makes them necessary
   - The research questions (or enough to derive them)
   - The findings and concrete contributions, and who each contribution serves
   If pieces are missing, ask targeted questions rather than inventing findings or citations. Never fabricate citations — use bracketed placeholders like `[CITE: prior work on X]` where the user must supply references.

2. **Read `references/structure.md`** for the full six-part recipe with examples and the reasoning behind each part.

3. **Read `references/style.md`** for CHI-calibrated prose mechanics (rhythm, contrast frames, hedging ladder, banned words, quantitative targets). Read this BEFORE drafting, not during — checking mid-draft produces sentences written to satisfy metrics.

4. **Draft the introduction** following the six parts in order. Typical length: 600–1,000 words (roughly 0.75–1.25 pages in CHI format), though this flexes with paper type.

5. **Self-check against the checklists** at the end of both reference files. Fix violations, especially: banned hype words, stacked hedges, announcements instead of claims, vague contribution statements, and a first sentence that wastes its position.

## The six parts (summary)

| Part | Question it answers | Core move |
|---|---|---|
| 1. The Drop | Why does this matter? | Drop the reader into a world where the problem already exists and already hurts — a scene, story, or striking statistic. Never open with a definition. |
| 2. World Building | What is the problem, exactly? | Now that they care, explain concepts, causes, stakeholders, constraints. |
| 3. The Players | What has been done? | Give prior work its flowers, then name what remains unresolved. One gap per paragraph; never trash prior work. |
| 4. Player One | What are you doing differently? | Stop hiding. State the gap, approach, and novelty confidently. "We argue/propose/demonstrate", not a timid "we explore" (unless explore is truly the right verb). |
| 5. The Deal | What do you promise to answer? | Research questions that feel inevitable given everything above, ordered so they tell a story. |
| 6. The Loot | What did you find and who gains? | Concrete findings and contributions. Name the insight, name the audience, name the implication. |

The recipe is a scaffold, not a template. Parts can merge or expand; RQs occasionally move after related work. What must survive is the logic: matter → world → known → unresolved → your move → promise → payoff.

## Critiquing an existing draft

When the user shares a draft, map each paragraph onto the six parts and diagnose:
- Missing or out-of-order parts (most common: opening with definitions instead of a Drop; a shy or absent Player One; vague Loot)
- RQs that don't feel inevitable — the fix is usually upstream in World Building or the gap, not in the RQ wording
- Prior work framed as failure rather than foundation
- Style violations from `references/style.md` (hype words, stacked connectors, nominalization, miscalibrated verbs)

Give the diagnosis by part, then offer a revision. Quote the specific sentences that fail and show the rewrite.

## Reference files

- `references/structure.md` — Full six-part recipe: purpose, techniques, worked examples, failure modes for each part.
- `references/style.md` — CHI prose style: rhythm targets, contrast frames, hedging ladder, citation integration, banned words, quantitative reference table, pre-send checklist.
