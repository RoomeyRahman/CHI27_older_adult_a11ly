# Project Context for Research Question Work

Context for applying the general rules in `rq-rules.md` to this CHI 2027 submission. Sources, in order of authority: `/output/Method.md` (the study as executed) and `/output/Related-Work.md` (positioning and gaps) are canonical; `/proposal/proposal.md` supplies the research questions and contribution framing only. Where the proposal disagrees with either canonical file, the canonical file wins and the proposal's version is ignored. Empirical facts live in `/Supplementary/Interviews/`; the filed thematic analysis is `/output/codes/A2/`.

## Working title

_Who Does the AI Work For? Negotiating an AI Agent's Role Between Older Adults and Family Caregivers in Bangladesh_

## Current research questions (proposal Section 4, verbatim)

**RQ1 (Formative).** How do Bangladeshi intergenerational care networks distribute, claim, and morally account for medication work, and which existing relational assets, from proxy device use to collective decision-making to checking-as-care, does that work run on?

**RQ2 (Interaction).** When an agent with genuine initiative joins such a care network, through what everyday practices do older adults and caregivers assign, contest, share, and revoke its allegiance, and what makes a shift acceptable to the family?

**RQ3 (Design and Outcomes).** Which of the agent's roles, whether tool, coach, or advocate, do older adults and caregivers treat as legitimate under which conditions, and which design mechanisms make a change of role visible, negotiable, and dignity-preserving?

Phase 1 answers RQ1. The deployment and Phase 2 answer RQ2 and RQ3.

## The study as executed (from `/output/Method.md`)

- **Design.** A two-phase qualitative household study in Bangladesh, January to June 2026, with a two-week prototype deployment between the phases. All sessions in participants' homes, in Bangla. Phase 1: formative interviews, contextual observation, and medication-routine walkthroughs, analysed before the prototype was built. Phase 2: post-deployment interviews about the same two-week period, older adult and caregiver each from their own perspective; divergent accounts retained.
- **Participants.** 25: 17 older adults (aged 65 to 80, mean 69.4, median 68; 9 women, 8 men; eleven needing large text, two unable to read; nine with low or very low smartphone comfort) and 8 family caregivers (4 women, 4 men; six reported ages 20 to 31; daughters, sons, a daughter-in-law, grandchildren). Snowball recruitment from the team's networks; roughly 30 households approached; voluntary and unpaid. Eligibility: older adults at least 65 taking daily medication; family members doing medication work for a co-resident older adult. Sixteen older adults in both phases, one (P14) in Phase 2 only. Method's Tables 1 and 2 carry per-participant detail.
- **Deployed prototype.** Manual schedule entry by participant or family member; scheduled reminders with medicine name and timing; logbook, streak, daily heat map; when a dose stayed unconfirmed, a request asking whether a family member should be notified, which the participant could decline; a spoken announcement of whom the system was serving. Schedules and changes in whom the system served stayed under human control. Nine older adults used their own smartphone, five a household smartphone shared with or operated by a relative, three not recorded.
- **Not built.** Prescription capture (concept figure only). Four mechanisms described to participants but never implemented: a risk-graded weakening veto, patterned interpretation of silence, a probationary onboarding mode, shared family scores. Responses to these support claims about how participants reasoned about proposed designs, never claims about use. Several Phase 2 probes imply prior experience; prompted agreement is weaker evidence than volunteered accounts.
- **Records.** Interviews are the only record. No app or decision logs, no adherence, error, or health-outcome measures. Machine-drafted Bangla transcripts and English renderings, each verified by two Bangla-fluent researchers; the Bangla record is analytically primary.
- **Analysis.** Reflexive thematic analysis, inductive first, then related to the research questions; no inter-rater reliability; no saturation claim. Three researchers, all fluent in Bangla and English. Ethics approval from the Brac University Ethics Committee.
- **Terminology.** Method calls the deployed artifact "the prototype" and its behaviour "the system". The rest of the paper calls the conceptual object "the agent".

## Positioning and gaps (from `/output/Related-Work.md`)

The review runs in four subsections, each closing on the gap it leaves open:

1. **Older Adults, Autonomy, and Family Support.** Gap: how older adults interpret shifts between independent support and family involvement when an autonomous system, rather than a person, initiates the change.
2. **Older Adults and Technology Use in the Global South.** Gap: how older adults in mediated households negotiate authority when an autonomous agent begins acting within, rather than merely supporting, existing family arrangements.
3. **Negotiating Who the Agent Serves.** Defines **allegiance**: whose interests or authority an agent's action appears to prioritise at a particular moment; narrower than alignment, different from access control. Gap: how older adults and family caregivers interpret, negotiate, and change an agent's allegiance when more than one person has a legitimate claim over what it should do.
4. **Making Agent Roles Visible and Negotiable.** Gap: how changes in an agent's role can be made visible, revocable, and negotiable without making the older adult's dependence more socially exposed or diminishing dignity.

Two stances from the review: the older adult's position stays analytically distinct from the caregiver's, and medication management is the setting in which questions of agency become concrete, not the paper's central object. The roles the paper works with are tool, coach, and advocate. The literatures it writes against: alignment assuming a single principal, passive caregiver dashboards, mediated tools rather than agents in Bangladesh and Global South HCI.

## Contribution framing (proposal Section 5, as far as Method supports it)

C1 empirical: how Bangladeshi care networks distribute and account for medication work before technology arrives, and how they negotiate an agent's allegiance once it does, negative cases retained. C2 conceptual: tool, coach, and advocate roles negotiated along direction, visibility, revocability, and ceremony. C3 design: mechanisms for agents serving more than one person, centred on the Affiliation Ledger (announcement of whom the agent serves; visible request-and-grant), with scores and streaks read as relational triggers. The proposal's claims that episodes are matched against the agent's decision log, that the older adult's veto weakens audibly, and that shared scores were implemented are not supported by Method and are ignored.

## Evidence available for answering or refining a question

- Phase 1 transcripts: 16 older adults (no P14) and 8 caregivers, plus both Phase 1 guides.
- Phase 2 transcripts: 17 older adults and 8 caregivers, plus both post-deployment guides. Method states seven caregivers in both phases and one in Phase 1 only; the corpus holds eight per phase. Surface this rather than repeat either figure.
- Demographics CSVs; Method Tables 1 and 2.
- `/output/codes/A2/`: the filed analysis. Phase 1: 40 codes, 12 subthemes, 4 themes (medication work distributed through differentiated household roles; routine transitions expose weak coordination and uncertain verification; existing aids fit tasks but miss household handoffs; families expect technology to support bounded care-network roles). Phase 2 older adults: 5 themes (acceptance of family involvement when they stay in control; routines and prescriptions over scores and streaks; community shapes care but doctors decide medicine; care tasks divided while older adults stay involved; the agent helps when it supports routines and shows uncertainty). Phase 2 caregivers: 2 themes (agent coordination that remains selective and accountable; streaks as records of routine care work). Lived and hypothetical evidence are kept separate; single-instance codes are marked.
- Not available: a household pairing map linking caregiver IDs to older-adult IDs, so no claim that an older adult and a caregiver described the same episode; any log-based evidence.

## Constraints a question for this project must respect

- Qualitative shape: "how", "through what practices", "under which conditions"; no effect or outcome language, no causal verbs about adherence or health.
- Scope is Bangladesh and Bangla; no claim extended to "any Global South context".
- Older adults are not framed as a deficit population; the care network, not the lone user, is the unit; checking is care as well as oversight; silence and non-use are patterned participation; gamification is a relational trigger, not a behavioural lever.
- Fixed names: tool, coach, advocate; direction, visibility, revocability, ceremony; the Affiliation Ledger; anchor terms care network, allegiance, the agent, dignity, older adult, caregiver. No priority claims ("first", "only"). No em-dashes or en-dashes in paper prose.
- Caregiver transcripts still carry real names; quote caregivers by ID only and never carry a name or employer into any output.
