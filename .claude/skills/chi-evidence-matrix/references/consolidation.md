# Consolidation: from candidate themes to final knowledge

The purpose of this stage is reduction. A corpus of 100 papers does not contain 100 pieces of knowledge; it contains roughly 8–12, each built up by many studies that replicate, refine, extend, or bound one another. Producing 40 rows means the work of synthesis was skipped and handed to the user.

## 1. The unit of a knowledge statement

A final row is a **claim the field would collectively endorse**, written so a reader could agree or disagree with it.

| Not a knowledge statement | Knowledge statement |
|---|---|
| Trust in AI systems | Users over-rely on confidently phrased explanations even when system accuracy is unchanged |
| Notification management | Interruptibility models trained on in-lab data lose precision within three weeks of field deployment |
| Older adults and voice interfaces | Voice interfaces reduce task time for older adults but only when error recovery is single-turn |

Test: could this row appear as a topic sentence in a related-work paragraph, with citations after it? If yes, it is a knowledge statement. If it reads like a section heading, it is a topic — rewrite or merge it.

## 2. Merge rules

Work through the candidate themes pairwise. Merge when **any** of these holds:

- **Same construct, same direction.** Two candidates assert the same relationship between the same variables. Merge unconditionally.
- **Extension.** One paper's contribution is the other's claim applied to a new population, modality, task, or scale. This is the most common case in HCI and the one most often missed: an extension is not new knowledge, it is *widened* knowledge. Merge, and record the widening dimension in the lineage.
- **Replication.** A later study confirms an earlier one. Merge; the replication raises the evidence grade rather than creating a row.
- **Refinement / boundary condition.** A study shows the earlier claim holds only under some condition. Merge, and state the condition inside the knowledge statement itself — this usually produces a *better*, more precise claim than either paper alone.
- **Same claim, different vocabulary.** HCI renames constructs constantly (reliance / over-trust / compliance; interruptibility / receptivity / opportune moments). Merge on meaning, not on the authors' terminology, and note the vocabulary drift — it is often a contribution in itself.
- **Co-citation test.** If a competent author would cite both candidates in the same sentence, they are one row.

Do **not** merge when:

- The claims point in **opposite directions**. That stays one row, graded `Contested`, with the divergence explained in Table 3. Opposing findings about the same construct are still one piece of knowledge — a disputed one.
- The constructs only sound similar. "Trust in the system" and "trust in the operator" are different objects.
- Merging would require a claim so abstract it loses testability ("interfaces affect behaviour"). Over-merging is as bad as under-merging; if the merged statement can't be disagreed with, back it out.

## 3. Procedure

1. Sort candidate themes by number of supporting papers, descending.
2. Take the largest as a seed. Walk the remaining candidates and pull in every one that satisfies a merge rule. The seed's statement usually needs rewriting after absorption — the merged claim is rarely the seed's original wording.
3. Repeat with the largest remaining unmerged candidate. Stop when everything is assigned.
4. If the count still exceeds `max_knowledge`, look for a **higher-order** merge: two knowledge statements that are both instances of one mechanism. Merge only if the parent claim stays testable.
5. If the count is far below `max_knowledge` (say 4 from 100 papers), the statements are probably too abstract. Split on the boundary conditions.
6. Anything left with a single supporting paper: fold into the nearest neighbour, or keep and label `Singleton — thin evidence`. Say so honestly. Thin areas are frequently where the user's contribution sits, so flag them rather than hiding them.

Record every decision in `consolidation_map.json`:

```json
{
  "consolidation": [
    {
      "knowledge_id": "K3",
      "candidate_themes": ["explanation confidence and reliance",
                            "verbosity effects on trust",
                            "confidence displays in clinical DSS"],
      "paper_ids": ["smith2021", "lee2022", "okafor2023", "chen2024"],
      "reason": "Same construct (expressed confidence -> reliance); Lee extends Smith to clinicians; Chen finds the boundary at low-stakes tasks."
    }
  ]
}
```

## 4. Writing the lineage column

The lineage tells the reader how the knowledge was built. Name the role each study played, not just its key.

**Weak:** `\cite{smith2021,lee2022,okafor2023,chen2024}`

**Strong:** `Established in lab settings \cite{smith2021}; replicated with clinicians \cite{lee2022}; extended to voice-only delivery \cite{okafor2023}; bounded to high-stakes tasks \cite{chen2024}.`

Useful roles: *established*, *replicated*, *extended to [population/modality/scale]*, *refined*, *bounded*, *contradicted*, *operationalized*, *formalized as a model*, *surveyed*. Chronological order works best — it shows the field moving.

Where the corpus contains only one study for a role, do not imply more. Three papers is `three studies`, not `a body of work`.

## 5. Ordering the final table

Order K1…Kn as an argument, not by paper count:

1. Foundational claims the reader must accept first.
2. Claims that build on those.
3. Contested claims.
4. The thinnest / most recent areas — which is usually where the user's own contribution will land, so ending there sets up their Discussion.

State this rationale in the closing 150 words.
