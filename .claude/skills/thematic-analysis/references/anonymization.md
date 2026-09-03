# Anonymization

Read this before Phase 1. The transcripts in `/supplementary/` carry real names in headers, in speaker labels,
and inside participant talk. **No real name ever enters `/output/codes/`, in any slot.** This is not a formatting preference:
the population is small, the recruitment channels are named and public, and a first name plus a university plus a
neighbourhood is identifying inside a small recruitment network. Study 3 raises the stake further: a household
is identifiable from the combination of its members, so an older adult and a caregiver who are both quoted can
identify each other's account to anyone who knows them.

---

## 1. Identifier scheme

| Who | Identifier | How assigned |
|---|---|---|
| Study 1 participants | `OA01` to `OA17` older adults, `CG01` to `CG09` caregivers | By source filename. `/supplementary/formative/OA03.md` is `OA03`. Never by name, never by order of analysis. |
| Study 2 participants | `D1` to `D6` | By source filename under `/supplementary/deployment/`. |
| Study 3 participants | `H1-OA`, `H1-CG1`, `H1-CG2`, `H2-OA`, ... | By source filename under `/supplementary/household/`. The household number is the pairing key. |
| Research team, interviewing | `[Interviewer]` | Names never appear, in any file, including analytic prose about the interview. |
| Research team, running a session | `[Facilitator]` | As above. |
| Family members named in talk | `[her eldest son]`, `[his daughter]`, `[a grandchild]` | Bracketed generic that preserves the **relation**, because the relation is the analysis, and drops the identity. |
| Other third parties named in talk | `[a pharmacist]`, `[a doctor]`, `[a neighbour]`, `[a hospital]` | Same rule. |
| Places below city level | `[a neighbourhood in Dhaka]` | Keep the city where it does analytic work, generalize below it. |
| Recruitment channels | May be named | Part of the reported method, if `/supplementary/` records them as such. |
| Tools, platforms, and medications | Named | These are study objects, not people. A medication name that is diagnostic of a rare condition is the exception; generalize it to the condition class. |

The file is the identity. **The same first name appearing in two transcripts does not make them one person.**
Never merge, never cross-reference by name, and never assert in an artifact that two participants are the same
person unless the transcripts state it.

**The one exception is the Study 3 household prefix, and it is deliberate.** `H2-OA` and `H2-CG1` are the same
household, and the analysis needs that link to read a paired episode. The prefix carries the relation and nothing
else: it says two accounts belong to one family, never who that family is.

**Names in CLAUDE.md.** CLAUDE.md Section 3.2 lists participant names appearing in the current Study 2
transcripts and records that they are not yet confirmed as pseudonyms. Until the user confirms, none of them may
appear in `/output/codes/` in any form. Refer to those participants by their `D` id only, flag the unresolved
question once in the run report, and do not propagate a name on the grounds that CLAUDE.md already contains it.

## 2. Never write a mapping file

Do not create a name-to-pseudonym key anywhere in the repository, including `/analysis/`, the scratchpad, or a
comment. The mapping stays in working memory for the run. A mapping file recreates exactly the disclosure risk
the pseudonyms exist to remove, and it is the artifact most likely to be shared accidentally with supplementary
material.

## 3. Substitution inside extracts

Anonymization applies inside quotation marks as well as around them, and a substitution inside a quote is an
insertion, so it takes square brackets:

- Source: "I discuss with my eldest son [name] during any difficulties."
- Output: `"I discuss with my eldest son [name removed] during any difficulties."` or, better,
  `"I discuss with my eldest son [...] during any difficulties."` where the removal costs nothing analytically.
- Where the relation matters, and in this corpus it almost always does, keep the relation:
  `"[my daughter] set it up for me."` Never flatten a kinship term into `[a family member]`; which family member
  it is carries the analysis.

Never silently delete a name and close the gap, because that misrepresents the extract as shorter than it was.
Mark every removal.

If an extract cannot be anonymized without destroying what makes it evidence, do not use it. Say in the report
that a supporting extract was withheld for identifiability and describe what it showed. A withheld extract that
is described honestly is stronger than a quoted one that identifies a participant.

## 4. Beyond names: identifiability by combination

Run this check on every extract that reaches the report or the matrix. A participant can be identifiable from a
combination of unremarkable details:

- A named clinic, doctor, or hospital plus a neighbourhood.
- An uncommon condition, an unusual regimen, or a distinctive surgery plus an age and a district.
- An occupation plus a household composition plus a city.
- Household composition itself in Study 3: "a widow living with three sons, one abroad" identifies a family to
  anyone who knows them, even with no name attached.

Generalize the combination, keep whichever element the analysis actually needs, and note the generalization in
the reflexivity column of the matrix. `[an older adult managing several chronic conditions]` usually preserves
everything the analysis needs from a specific diagnosis list.

**Within-family identifiability is the Study 3 case to watch.** A caregiver reading the paper may recognise the
older adult's account of an episode they both lived, and vice versa. That is not a reason to drop paired
episodes, which are the study's evidence, but it is a reason to strip incidental detail from both accounts of the
same episode rather than only from one, and to note in the reflexivity column where a pairing was quoted.

## 5. Consent-based exclusions

Consent in a collectivist household is familial as well as individual (CLAUDE.md Section 9.4). Check each
transcript and its consent record in `/supplementary/` for any material a participant, or a family member on
their behalf, asked to be excluded. Excluded material is unusable even anonymized, and it is also unusable as an
uncited basis for a claim. Where a record exists, note it in that participant's `01-memo.md` and honor it in
every artifact. Where no exclusion record exists for a study, say so in the run report rather than assuming
there was nothing to exclude.

## 6. The scan

Before any run is reported as finished, run:

```bash
bash .claude/skills/thematic-analysis/scripts/anon_scan.sh . <slot>
```

The second argument restricts the scan to your own slot (SKILL.md Section 0.0). Omit it to scan every slot, which
is the right call only when the user asks for a repository-wide check.

It derives candidate personal names from name-bearing positions in `/supplementary/` at run time, so no real name
is stored in the skill, then greps the slot for each. Exit 0 is clean, exit 1 is a failure with the
offending lines printed, exit 2 means a path is missing.

The script also prints residual Title Case bigrams found in the output for eye review. Most will be legitimate
(theme names, tool names, framework names, place names, medication names). Read the list rather than skipping it;
it is what catches a name the derivation missed, for example a family member mentioned only in the middle of a
participant's turn.

**Report the command and its output in the run report.** A run that has not reported a clean scan is not
finished. If the scan flags a false positive, such as a theme name that collides with a stopword gap, extend the
stoplist inside the script rather than weakening the pattern, and say in the run report that you did.
