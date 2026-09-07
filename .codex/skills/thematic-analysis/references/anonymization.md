# Anonymization

Read this before Phase 1. Older-adult transcripts under `/Supplementary/Interviews/` carry participant ids. The
sixteen caregiver transcripts still carry real names in speaker labels and inside participant talk, C01's Phase 1
transcript opens with a full name and an employer, and `demographics/caregiver.csv` records that employer
(AGENTS.md Section 3.4). **No real name, employer, or workplace ever enters `/output/codes/`, in any slot.** This
is not a formatting preference: the population is small, recruitment ran through the team's networks, and a first
name plus a workplace plus a neighbourhood is identifying inside a small recruitment network. The household design
raises the stake further: a household is identifiable from the combination of its members, so an older adult and a
caregiver who are both quoted can identify each other's account to anyone who knows them.

---

## 1. Identifier scheme

| Who | Identifier | How assigned |
|---|---|---|
| Older adults | `P01` to `P17` (no P14 in Phase 1) | By source filename. `/Supplementary/Interviews/phase-1/Participants/P03.md` is `P03`, Phase 1. Never by name, never by order of analysis. |
| Caregivers | `C01` to `C08` | By source filename under `phase-1/Caregiver/` and `phase-2/Caregiver/`. The same id recurs in both phases, so every attribution names the phase. |
| A caregiver's first-name speaker label | the caregiver's `C` id | A first name in a speaker-label position is a name, not a role. Never carry it forward. |
| Research team, interviewing | `[Interviewer]` | Names never appear, in any file, including analytic prose about the interview. |
| Research team, running a session | `[Facilitator]` | As above. |
| Family members named in talk | `[her eldest son]`, `[his daughter]`, `[a grandchild]` | Bracketed generic that preserves the **relation**, because the relation is the analysis, and drops the identity. |
| Other third parties named in talk | `[a pharmacist]`, `[a doctor]`, `[a neighbour]`, `[a hospital]` | Same rule. |
| Places below city level | `[a neighbourhood in Dhaka]` | Keep the city where it does analytic work, generalize below it. |
| Recruitment channels | May be named at the level `/output/Method.md` names them | Snowball through the team's networks and referrals; never a specific institution, employer, or group that identifies a household. |
| Tools, platforms, and medications | Named | These are study objects, not people. A medication name that is diagnostic of a rare condition is the exception; generalize it to the condition class. |

The file is the identity. **The same first name appearing in two transcripts does not make them one person.**
Never merge, never cross-reference by name, and never assert in an artifact that two participants are the same
person unless the transcripts state it.

**There is no household key in the ids.** The household pairing map, caregiver id to older-adult id, is unfiled
(AGENTS.md Section 3.5). A pairing is asserted only where a transcript itself states the relation, and then only as
"the caregiver's account names a parent" rather than as a `P` id. Never construct a pairing from a shared surname,
a shared address, or `/output/Method.md` Table 2, which names relations and not ids.

**Names and AGENTS.md.** AGENTS.md lists no participant names and never will. It records only that the caregiver
files are not de-identified. Every name in a caregiver transcript is real until those files are cleaned: none may
appear in `/output/codes/` in any form, and neither may C01's employer. Refer to caregivers by their `C` id only,
flag the standing de-identification blocker once in the run report, and never argue that a name is safe because
it appears elsewhere in the repository.

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
- Household composition itself: "a widow living with three sons, one abroad" identifies a family to anyone who
  knows them, even with no name attached.

Generalize the combination, keep whichever element the analysis actually needs, and note the generalization in
the reflexivity column of the matrix. `[an older adult managing several chronic conditions]` usually preserves
everything the analysis needs from a specific diagnosis list.

**Within-family identifiability is the case to watch in a household study.** A caregiver reading the paper may recognise the
older adult's account of an episode they both lived, and vice versa. That is not a reason to drop paired
episodes, which are the study's evidence, but it is a reason to strip incidental detail from both accounts of the
same episode rather than only from one, and to note in the reflexivity column where a pairing was quoted.

## 5. Consent-based exclusions

Consent in a collectivist household is familial as well as individual (AGENTS.md Section 9.4); `/output/Method.md`
records that consent was obtained individually and that caregivers consented independently of the older adults
they discussed. Check each transcript for any material a participant, or a family member on their behalf, asked to
be excluded. Excluded material is unusable even anonymized, and it is also unusable as an uncited basis for a
claim. Where such a request appears, note it in that participant's `01-memo.md` and honor it in every artifact.
No separate consent record is filed under `/Supplementary/Interviews/`; say so in the run report rather than
assuming there was nothing to exclude.

## 6. The scan

Before any run is reported as finished, run:

```bash
bash .codex/skills/thematic-analysis/scripts/anon_scan.sh . <slot>
```

The second argument restricts the scan to your own slot (SKILL.md Section 0.0). Omit it to scan every slot, which
is the right call only when the user asks for a repository-wide check.

It derives candidate personal names from name-bearing positions in `/Supplementary/Interviews/` at run time, so no
real name is stored in the skill, then greps the slot for each. Exit 0 is clean, exit 1 is a failure with the
offending lines printed, exit 2 means a path is missing.

The script also prints residual Title Case bigrams found in the output for eye review. Most will be legitimate
(theme names, tool names, framework names, place names, medication names). Read the list rather than skipping it;
it is what catches a name the derivation missed, for example a family member mentioned only in the middle of a
participant's turn.

**Report the command and its output in the run report.** A run that has not reported a clean scan is not
finished. If the scan flags a false positive, such as a theme name that collides with a stopword gap, extend the
stoplist inside the script rather than weakening the pattern, and say in the run report that you did.
