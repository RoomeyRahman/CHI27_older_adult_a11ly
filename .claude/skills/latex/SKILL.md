---
name: latex
description: Converts a finished markdown section in /output/ into ACM (acmart) LaTeX inside /output/latex/care_network_agent/, converting numeric markdown citations into \cite{} against reference.bib, writing the section to its sources/*.tex file, and updating main.tex accordingly. Use when a drafted section needs to enter the compiled submission.
argument-hint: [section-name | path-to-md | abstract | all]
---

We are moving `$1` from markdown into the compiled ACM submission. This is a **transcription task, not a writing task**: the prose is already final, and this pass changes markup only. The target project is `/output/latex/care_network_agent/`, built with `acmart` (`\documentclass[manuscript,review,anonymous]{acmart}`) and compiled from the repository root with `make pdf`.

Two helper scripts live beside this file and do the mechanical work:

- `.claude/skills/latex/scripts/md2tex.py` converts one markdown file to LaTeX and emits a JSON report of every citation, placeholder, dash, and table it found.
- `.claude/skills/latex/scripts/check_cites.py` verifies every `\cite` key in a `.tex` file resolves against the bib file(s).

Execute the protocol below in order and report per phase.

### Phase 0: Hard Invariants (violating any one of these fails the task)

1. **Prose frozen.** Not one word of the source markdown changes: no rewording, no reordering, no trimming, no "small fixes", no new sentences, no new headings. If the markdown reads badly, say so in the report and leave it alone; `/polish` and `/revise` own the prose.
2. **No content invented.** Never write a title, abstract, keyword, caption, CCS concept, author, or affiliation that does not exist in a repository source file. Anything missing stays a `\suggestion{[MISSING DATA: ...]}` marker, which is visible in the compiled PDF by design.
3. **Placeholders survive.** Every `[cite]`, `[cite: ...]`, `[MISSING DATA: ...]`, `[BLOCKED: ...]`, and `[NOT YET IMPLEMENTED: ...]` in the markdown becomes a visible `\suggestion{...}` marker in the LaTeX. Never silently drop one, and never resolve one by guessing a bib key.
4. **Citations never move between claims.** A bracket attaches to the same clause in LaTeX that it attached to in markdown.
5. **Anonymity preserved.** The class is `anonymous` for review. Do not add author names, affiliations, or acknowledgements, and do not remove the `anonymous` option.
6. **Preamble discipline.** Do not delete or reformat the acmart preamble, the `%TC:` TeXcount lines, or the `\ifx ... \fi` blocks that hold the disabled sample authors and rights commands. Add a package only when the converted section genuinely needs one, and say why in the report.
7. **Supplementary and system are read-only.** Never edit anything under `/supplementary/` or `/system/`.
8. **Participant names.** A real participant name may not enter the LaTeX. If the markdown carries a name that has not been confirmed as a pseudonym (CLAUDE.md Section 3.2), stop and report it rather than transcribing it.

### Phase 0.5: Project Bootstrap Check

Before resolving the target, confirm `/output/latex/care_network_agent/` exists and holds `main.tex`, `acmart.cls`, `ACM-Reference-Format.bst`, and a `sources/` directory.

If it does not, do not improvise a project. Report exactly what is missing and stop, telling the user the skeleton must be created first: the acmart class files come from the official ACM Primary Article Template, and `main.tex` needs the `\documentclass[manuscript,review,anonymous]{acmart}` preamble, an `itquote` environment, a `\suggestion` command, an empty `\title{}`, `abstract`, and `\keywords{}`, a commented CCS block, `\input{sources/...}` lines in the Phase 1 order, and `\bibliographystyle{ACM-Reference-Format}` plus `\bibliography{reference}`. Converting into a project that does not exist produces a file nobody compiles.

### Phase 1: Resolve the Target

Map the argument to a source markdown file and a destination `.tex` file. The skeleton order below is what `main.tex` inputs, in exactly this sequence:

| Argument (case-insensitive) | Source markdown | Destination | `\section{...}` |
|---|---|---|---|
| `intro`, `introduction` | `/output/Introduction.md` | `sources/1_intro.tex` | Introduction |
| `background`, `related`, `related work` | `/output/RelatedWork.md` or `/output/Background.md` | `sources/2_background.tex` | Related Work |
| `method`, `methods`, `methodology` | `/output/Methodology.md` | `sources/3_method.tex` | Method |
| `system`, `design` | `/output/System.md` | `sources/4_system.tex` | The Agent |
| `findings`, `results` | `/output/Findings.md` | `sources/5_findings.tex` | Findings |
| `discussion` | `/output/Discussion.md` | `sources/6_discussion.tex` | Discussion |
| `conclusion`, `limitations` | `/output/Conclusion.md` or `/output/Limitations.md` | `sources/7_conclusion.tex` | (see note) |
| `abstract` | `/output/Abstract.md` | `main.tex` abstract environment | n/a |
| `all` | every markdown in `/output/` with a mapping | each destination above | each |

Rules for resolution:

- A path argument (anything containing `/` or ending `.md`) is used directly; infer its destination from its H1 or filename, and confirm the choice in the report.
- If the mapped markdown does not exist, list what `/output/*.md` actually holds and stop. Do not invent a section.
- If two candidate markdown files exist for one destination (a `Introduction.md` alongside a `Introduction-2.md`, say), do not choose silently: report both, use the one the argument names, and default to the file the user last edited when the argument is ambiguous.
- `/output/codes/` holds analysis artifacts, never paper prose. Never convert a file from it.
- When converting a Conclusion into a file that already carries Limitations, keep Limitations and Conclusion as separate `\section`s in that one file, in the order the markdown gives them, and report that you did.
- A section with no slot in the table gets a new file `sources/N_slug.tex` numbered after the last existing one, plus a new `\input` line in `main.tex` at the position its argument implies. Ask the user where it belongs if the position is not obvious.

Read the destination `.tex` before writing it. If it holds hand-written LaTeX beyond a bare `\section{...}` line, quote what is there and ask before overwriting; the default is to preserve nothing but report exactly what was replaced.

### Phase 2: Convert

Run the converter into the scratchpad first, never straight over the destination:

```bash
python3 .claude/skills/latex/scripts/md2tex.py output/Methodology.md \
  --section-title "Method" \
  --out "$SCRATCH/3_method.tex" \
  --report "$SCRATCH/3_method.json"
```

Use `--no-section` only when appending into a file that already carries the `\section` line, and for the abstract.

The converter handles: headings (`##` to `\subsection`, `###` to `\subsubsection`, `####` to `\paragraph`), numeric citations (`[27, 34]` to `\cite{27,34}`), mixed brackets (`[64, 66; cite: X]` to `\cite{64,66}\suggestion{[cite: X]}`), bare and named `[cite]` placeholders, `[MISSING DATA: ...]`, bold and italic, inline code, block quotes to the `itquote` environment already defined in `main.tex`, bullet and numbered lists, smart quotes to `` `` '' ``, and LaTeX escaping of `% & # $ _ ~ ^ \`.

### Phase 3: Review the Conversion by Hand

The script is mechanical; these judgments are yours. Read the generated `.tex` against the markdown side by side and fix:

1. **Participant quotations.** A quotation the markdown sets as a block quote belongs in `itquote`. A short in-line quotation stays in-line with `` `` '' `` quotes. Attribution stays exactly as the markdown wrote it, including the older adult or caregiver role label where the markdown carries one. Verify every quotation is character-identical to the markdown, which is itself verbatim from a filed transcript in `/supplementary/`. A quotation translated from Bangla keeps its translation exactly as the markdown gives it; never re-translate, and never typeset the Bangla original in place of the filed translation.
2. **Emphasis that means something.** Bold used for a claim the reader must remember (`\textbf{}`) is correct; bold used as a list label (`\textbf{RQ1.}`) is correct; bold used decoratively should be reported, not restyled.
3. **RQ and contribution lists.** Keep them as `itemize` with a bold lead label, matching what the markdown had. The three RQs and the C1 to C3 contributions do not get renumbered, relabeled, or merged.
4. **Tables.** The script comments a markdown table out and leaves a `TODO(/latex)` line. Build a real `table`/`tabular` with `\caption`, `\label{tab:...}`, and `booktabs` rules (already loaded), place it near its first reference, and add a `\ref{}` if the prose refers to it. Report every table you built. A participant table keeps its pseudonyms exactly as filed.
5. **Figures.** Only insert a figure when the markdown references one, and only when the image file already exists in the project; caption text comes from the markdown, never from you. A decision-log schema or Affiliation Ledger diagram is a figure the markdown must call for first.
6. **Cross-references.** Prose naming another section ("Appendix A", "Section 3") may keep its literal text; introduce `\label`/`\ref` only where the markdown already names a numbered object, and report the change.
7. **Dashes.** The report lists every `--` or `---` the source contained. CLAUDE.md 7.2 forbids dashes in this paper's prose, so do not convert them into typeset dashes: flag each one for the user and leave the source markdown for `/polish` to fix.
8. **Escaping check.** Grep the output for stray `%`, `&`, or `_` outside a command, and for `$` that is not `\$`, since an unescaped one silently opens math mode.

### Phase 4: Bibliography

The markdown cites by number and `/output/reference.bib` uses those same numbers as its entry keys, so `[27, 34]` resolves to `\cite{27,34}` directly. Where the drafting skills emitted verified filed sources as `[Author Year; filename.pdf]` rather than numbers, those are not yet bib keys: report each one as needing a numbered entry in `/output/reference.bib` before it can compile, and leave it as a `\suggestion{}` marker rather than inventing a key.

1. Copy `/output/reference.bib` into the project as `reference.bib` whenever the project copy is missing or differs from it. Leave `sample-base.bib` on disk untouched.
2. Ensure `main.tex` ends with `\bibliographystyle{ACM-Reference-Format}` and `\bibliography{reference}`. Replace a `\bibliography{sample-base}` if that is still what it says, and report the switch.
3. Verify:

```bash
python3 .claude/skills/latex/scripts/check_cites.py \
  output/latex/care_network_agent/sources/3_method.tex \
  output/latex/care_network_agent/reference.bib
```

4. Any key that fails to resolve is reported as unresolved and left as `\cite{key}` so the compiled PDF shows it as a missing reference. Never invent a bib entry, and never repoint a citation at a different entry to make the check pass.

### Phase 5: Update main.tex

Make the smallest edit that compiles.

1. **Inputs.** Confirm an `\input{sources/...}` line exists for the destination file, in the Phase 1 order. Add a missing one; never duplicate one.
2. **Introduction (`intro` argument), additional steps.**
   - If `\title{}` is empty, fill it with the working title from CLAUDE.md 2.1, `Who Does the AI Work For? Negotiating an AI Agent's Role Between Older Adults and Family Caregivers in Bangladesh`, and note in the report that it is the working title, not a final one. If `\title{}` is already populated, leave it.
   - The `abstract` environment is empty. Populate it only from an abstract that exists in a repository file. With no such file, leave it empty and report `[MISSING DATA: abstract]`.
   - `\keywords{}` is empty. Populate only from a repository source; otherwise report `[MISSING DATA: keywords]`.
   - The CCS block sits inside a `comment` environment. Leave it commented and report `[MISSING DATA: CCS concepts]` once.
   - Do not touch `\shortauthors` or the author block; both live inside the disabled `\ifx` region and the submission is anonymous.
3. **Abstract argument.** Convert with `--no-section` and place the result between `\begin{abstract}` and `\end{abstract}`. Nothing else changes.
4. Report every line of `main.tex` you changed, old and new.

### Phase 6: Compile and Verify

Compilation runs in the texlive Docker container from the repository root:

```bash
make pdf
```

The Makefile's `PROJECT` variable defaults to `care_network_agent`; override it with `make pdf PROJECT=other_folder` only when building a different project under `output/latex/`. If Docker is unavailable, say so plainly and report the conversion as unverified rather than claiming a build. On a build:

1. Read `output/latex/care_network_agent/main.log` for errors and for `Undefined control sequence`, `Missing $ inserted`, `Runaway argument`, and `LaTeX Warning: Citation ... undefined`.
2. `acmart` with `titlesec` emits a known sectioning-redefinition complaint that the Makefile's `-f` flag rides past; the target still verifies `main.pdf` exists. Do not "fix" that warning.
3. Report the page count and the list of undefined citations, if any.

### Phase 7: Report

End with:

1. **Target:** source markdown, destination `.tex`, and whether existing LaTeX was replaced (with what it was).
2. **Citations:** count of distinct `\cite` keys, count of resolved keys, every unresolved key by name, and every `[Author Year; filename.pdf]` citation still needing a numbered bib entry.
3. **Placeholders carried into LaTeX:** every `[cite: ...]`, `[cite]`, `[MISSING DATA: ...]`, `[BLOCKED: ...]`, and `[NOT YET IMPLEMENTED: ...]`, quoted, with its section.
4. **Hand-built structures:** tables, figures, labels, packages added, each with its justification.
5. **Dashes found in the source:** each one with its line, flagged for `/polish`, since CLAUDE.md 7.2 bans them.
6. **main.tex changes:** every edited line.
7. **Build:** `make pdf` result, page count, and log warnings that matter.
8. **Fidelity attestation:** state plainly that the prose is unchanged, or name every deviation. A deviation you did not report is a failed task.

### Notes

- This skill runs after `/polish`, on prose the user considers finished. Converting a draft mid-revision is fine, but say in the report that the LaTeX will need a re-run.
- Re-running on the same section is idempotent: the destination `.tex` is regenerated from the markdown, and `main.tex` gains no duplicate lines.
- If the project grows a second document with its own build target (a proposal, say), never write paper section files into it.
