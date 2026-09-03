# Report template and writing conventions

Read this before Phase 6. Contents:

1. Deliverable structure
2. The claim → extract → interpretation → implication rhythm
3. Quote selection and formatting
4. Answering "so what?"
5. Worked example of analytic prose
6. Venue variants (CHI/CSCW paper, thesis chapter, applied UX report)

---

## 1. Deliverable structure

Default structure for the written analysis. Adjust for venue, but keep the order of argument.

```
# [Study title]

## 1. Analytic approach
Reflexive TA; theoretical position; inductive/deductive balance; dataset description;
single-analyst rationale; software or manual process; conventions for quotes and pseudonyms.

## 2. Reflexivity and positionality
(see quality-and-reflexivity.md for structure)

## 3. Overview of the thematic structure
Thematic map + one paragraph stating the overall argument the themes make together.
The reader should be able to stop here and know what the analysis claims.

## 4. Theme 1 — [Name]
   Definition paragraph
   Subtheme 1.1 — analysis with extracts
   Subtheme 1.2 — analysis with extracts
   Boundary and variation
   So what: theoretical/design significance

## 5. Theme 2 — [Name]
   …

## 6. Relations between themes
Where they reinforce, where they pull against each other, what the tension means.

## 7. Discussion
Connection to prior literature and theory; what this extends, complicates, or contradicts;
implications for design or for HCI theory; limitations and boundary conditions.

## Appendix A — Codebook
## Appendix B — Theme-development log (Phases 3–4 decisions and reasons)
## Appendix C — Analytic memos
```

For an applied or industry deliverable, invert: lead with the thematic overview and
implications, move the method and appendices to the back, keep the interpretive depth.

## 2. The rhythm

Every analytic paragraph follows the same underlying movement:

1. **Claim** — the analytic point, stated in your voice, not the participant's.
2. **Extract** — the data that earns it.
3. **Interpretation** — what in the extract supports the claim; attend to the specific words.
4. **Implication** — what follows, for the theme, for design, or for theory.

The failure mode to avoid is the "quote sandwich with no filling": a topic sentence, three
quotes in a row, and a sentence saying that participants had varied views. If two extracts sit
adjacent, there must be a reason (contrast, escalation, range) and you must state it.

## 3. Quotes

- Short extracts (under ~25 words) run inline in quotation marks. Longer ones are block quotes
  with the participant identifier and, where useful, line or turn reference.
- Attribute every extract: `(P7)` or `(P7, lines 214–219)`.
- Choose for **vividness** and **coverage**. Across a theme's extracts the reader should see its
  range, including at least one extract that sits near its boundary or complicates it.
- Do not use a quote merely because it restates the theme name. The best extracts are slightly
  in excess of the claim — they carry something the claim does not fully capture, and you
  comment on that surplus.
- Elision: `[…]`. Insertions for sense: `[the app]`. If you have removed disfluencies for
  readability, state that once in the conventions note; otherwise leave them.
- Balance across participants. If one participant supplies more than roughly a third of the
  extracts in a theme, revisit the theme.

## 4. Answering "so what?"

Each theme ends with a passage that does at least two of these:

- **Extends theory**: names an existing construct and shows where the data push past it.
- **Complicates a design assumption**: identifies a belief embedded in current systems that the
  data undercut.
- **Reframes the problem**: shows that what the field treats as a usability issue is better
  understood as something else (an organizational, moral, or infrastructural matter).
- **Specifies conditions**: states when and for whom the pattern holds, and when it breaks.

Weak: *This suggests trust is important for adoption.*
Strong: *Calibrated trust models assume users adjust reliance in response to observed system
error. These accounts show adjustment running the other way: participants revised their account
of their own competence to preserve a stable picture of the system. Reliance was not calibrated
against performance so much as defended against the effort of re-evaluation — which suggests
that transparency features aimed at supporting calibration may instead supply material for
rationalization.*

Cite real, checkable literature. If you are unsure a source exists, describe the position and
mark it for the user to verify rather than inventing a citation. Fabricated references are
worse than an unreferenced claim.

## 5. Worked example of analytic prose

> Participants' oversight practices were less about verifying the system than about maintaining
> a workable account of themselves as competent users. P4 described a nightly routine of
> reviewing the automation log, immediately disowning the obvious reading of it:
>
> > "I always check the log afterwards. Not because I don't trust it exactly, it's just […] I
> > like to see it did what it said." (P4)
>
> The denial is the interesting part. The practice described — retrospective verification of
> every automated action — is a distrust practice by any ordinary description, and P4's
> qualification is unprompted, which suggests she anticipates the reading and moves to block it.
> What is being managed here is not the system's reliability but her own position: neither the
> paranoid user who cannot let go, nor the naive one who lets the system run unchecked. The log
> makes this position available. Because the system renders its actions inspectable, oversight
> can be performed as diligence rather than confessed as suspicion.
>
> This pattern held even where verification had never once surfaced an error […]

Note what the passage does: names the analytic point first, uses the extract as evidence rather
than illustration, reads the specific wording, and identifies the mechanism (the affordance that
makes the stance available).

## 6. Venue variants

- **CHI/CSCW paper**: findings section of 2,500–4,000 words; method compressed to a paragraph
  plus positionality statement; themes as subsection headings; implications folded into the
  discussion rather than bulleted as "design implications" unless the venue expects them.
- **Thesis chapter**: full structure above, with the theme-development log and analytic memos as
  appendices; expect the examiner to test the audit trail.
- **Applied UX report**: lead with the thematic overview and what to do about it; keep quotes
  prominent; retain the interpretive claims but shorten the theory linkage; add a short "what we
  are not claiming" section, which prevents over-reading by stakeholders.
