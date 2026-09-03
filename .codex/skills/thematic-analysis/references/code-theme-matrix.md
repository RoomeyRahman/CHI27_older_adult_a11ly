# The six-column matrix and the final codebook

The matrix is the artifact a reviewer reads to see how a quote became a code, a code became a sub-theme, and a
sub-theme became a theme, with the analyst's uncertainty attached at each step.

Written per unit, then generated once as the deliverable. Every path here is inside your agent slot
(SKILL.md Section 0.0), `A2/` for Codex, `A1/` for Claude Code, and `A3/` and beyond for other analysing agents:

| File | Contents |
|---|---|
| `<slot>/study<N>/<id>/05-matrix.md` | that transcript's retained codes, 25 to 30 rows |
| `<slot>/study<N>/master/03-matrix.md` | that study's retained set, at most 40 rows, participants named in the code cell |
| `<slot>/study3/streams/05-matrix.md` | the Study 3 decision logs, probes, and vignettes, kept separate |
| `<slot>/cross-study/03-matrix.md` | the affiliation synthesis across studies, at most 25 rows |
| `<slot>/FINAL-CODEBOOK.md` | **the deliverable**, generated from the study masters and the cross-study matrix |

---

## 1. Columns, and which pass fills them

| Code | Definition | Sub-theme | Theme | Example quote | Reflexivity note |
|---|---|---|---|---|---|

| Pass | Fills |
|---|---|
| A | `Code`, `Definition`, `Example quote` for every candidate; the rest read `[pending]` |
| B | Nothing. The trim happens in the register; parked rows keep their pending markers and never reach the final codebook |
| C | `Sub-theme` and `Reflexivity note`, for retained codes only |
| D | `Theme`, plus validation of every reflexivity note against where its code landed |

A matrix whose `Sub-theme` and `Theme` columns were written at the same time as its `Code` column is not evidence
of a derivation; it is a table of assertions.

## 2. Column rules

**Code.** Exactly as it appears in the coding table: two to five words, no paraphrase. In a master matrix,
append the participants it draws on: `Son deciphers prescription (OA04, CG02)`. Evidence tags travel here too:
`[elicited]`, `[hypothetical]`, `[believed-capability]`, `[study2-scope-limited]`, `[single-instance]`.

In a Study 1 master matrix, the code cell also carries whether the code appears in older adults' accounts,
caregivers' accounts, or both: `Son deciphers prescription (OA04, CG02) [both]`. In the cross-study matrix, it
carries the affiliation practice the code instantiates, where one fits: `[assignment]`, `[contestation]`,
`[gifting]`, `[revocation]`, `[ceremony]`.

**Definition.** What the code covers and, where contested, what it excludes. **At most 20 words in the final
codebook.** A definition that re-words the code name is not a definition.

**Sub-theme.** The Pass C name, exactly. Descriptive, not dramatic (SKILL.md Section 8).

**Theme.** The Pass D name, exactly. This column is what makes the codebook auditable against the report.

**Example quote.** **One** verbatim participant extract with id and, where available, timestamp. **At most 25
words in the final codebook**; trim with `[...]` rather than choosing a weaker quote. Never the interviewer:
where an answer needs its question to be readable, put the recovered content in square brackets inside the
participant's quote, `"Yes[, my daughter set it up], but not the second part." (D6, 12:40)`. Working matrices may
carry a second quote; the final codebook carries one. A quote translated from Bangla is the filed translation,
never a fresh rendering.

**Reflexivity note.** First person, **one sentence, at most 20 words in the final codebook**, never blank. It
records the decision and what would show it wrong: why the code was retained or parked, the alternative reading
not taken, the evidence grade, the translation caveat, or who it rests on. "Straightforward code" is not a
reflexivity note. Longer reasoning lives in the unit's themes file, which the codebook header points to.

## 3. Worked rows

| Code | Definition | Sub-theme | Theme | Example quote | Reflexivity note |
|---|---|---|---|---|---|
These are shape examples. The wording is illustrative; never carry a row here into a real matrix.

| Code | Definition | Sub-theme | Theme | Example quote | Reflexivity note |
|---|---|---|---|---|---|
| `Memory as competence claim` (OA02, OA09) `[both]` | Asserting unaided recall as evidence of standing, in a turn where an aid was offered. | Remembering defended as a capacity | Unaided remembering treated as evidence of competence | "My memory is very sharp." (OA02, 08:11) | Read as a claim rather than a report because it answers an offer, not a question about recall. |
| `Escalation routed to son` (OA04, CG02) `[assignment]` | Naming one family member as the person the agent should tell, in preference to others present. | Choosing who is told | Conditions under which families reassign the agent's allegiance | "I discuss with [my eldest son] during any difficulties." (OA04) | Kept the kinship term over a generic because which child was chosen is the finding. |
| `Timer test before trust` (D3) `[single-instance]` | Deliberately testing whether a reminder fires before relying on it. | Trust built by verification | Reliance granted only after the agent was tested | "I set a 30-minute timer just to see." (D3, 04:22) | Single participant; retained because it cuts against trust-at-setup, and flagged rather than generalized. |

## 4. The final codebook

Generated at the end of the run. Never hand-written, so it cannot drift from the working files.

```
# Final codebook

Two lines: what this is, which run produced it, and where the parked codes and full reasoning live.

## 1. Study 1, the human affiliation baseline
One paragraph: the master themes in a sentence, and the numbers (candidates, retained per transcript,
master retained, sub-themes, themes).
[one six-column table, at most 40 rows, sorted by theme, then sub-theme, then code, each row marked
older adult / caregiver / both]

## 2. Study 2, the deployment evaluation
One paragraph, including the sample skew in one sentence.
[one six-column table, rows touching allegiance tagged [study2-scope-limited]]

## 3. Study 3, the household deployment
One paragraph, including how many themes rest on paired episodes.
[one six-column table, plus a short separate table for the non-interview streams]

## 4. Cross-study affiliation synthesis
One paragraph: what the five practices looked like among humans and toward the agent, and which had no
agent-directed instance.
[one six-column table, at most 25 rows, each row carrying its affiliation practice]
```

A section for a study that has not run is omitted, not stubbed.

**Studies are never merged.** Each keeps its own table and its own theme names, because they are different
instruments answering different RQs. Where two studies disagree, both readings are recorded and the
disagreement is noted rather than resolved. The cross-study section comes last because it depends on the
others, and it is the section the paper's conceptual contribution is built from.

**Keep it short.** The caps in Section 2 are enforced by `table_check.py`. If a cell will not fit, the material
belongs in the working files, not in a longer cell.

## 5. Markdown that renders

Broken tables are the most common way a codebook becomes unusable. The rules:

- **One line per row.** No line breaks inside a cell, no `<br>`, no bullet lists, no block quotes in a cell.
- **Escape every literal pipe** inside a quote or definition as `\|`. An unescaped pipe silently splits the row
  and shifts every later column.
- **Every row has the same number of cells as the header**, six for the final codebook, and therefore seven pipe
  characters counting the leading and trailing ones.
- **Blank line before and after the table**, and a separator row `|---|---|---|---|---|---|` directly under the
  header.
- **No pending markers** anywhere in the final codebook.
- Keep code names in backticks so a stray underscore or asterisk cannot start italics.

Run the checker and fix what it reports:

```bash
python3 .codex/skills/thematic-analysis/scripts/table_check.py . <slot>
```

## 6. Reading the matrix as a check

Read the master matrix column-wise before writing the report. It surfaces what the report hides: a theme whose
codes all come from one participant; a theme whose codes are all `[elicited]` or all `[hypothetical]`, which is
a theme about the instrument; a Study 1 theme whose codes are all marked `older adult` or all `caregiver`, which
is a theme about one side of the network rather than about the network; a sub-theme with one code; two rows whose
definitions overlap, which is one code under two names; and a reflexivity column with no alternative readings
anywhere, which means the analysis was executed rather than contested. Fix what this surfaces, and log the fixes.
