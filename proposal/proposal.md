# Who Does the AI Work For? Negotiating an AI Agent's Role Between Older Adults and Family Caregivers in Bangladesh

**Research Proposal — ACM CHI Conference on Human Factors in Computing Systems**

---

## 1. Main Research Idea

An AI agent that decides for itself when to remind, when to stay silent, and when to alert a family member must also decide whom it serves. In a Bangladeshi household that question has no settled answer. Medication work there is not an individual task supported by a private device; it is a collective practice in which family members remind, interpret unclear prescriptions, supervise doses, and express affection through checking. We study what happens when an autonomous agent joins this care network: how families assign its allegiance, contest it, hand it over, and take it back, and which design choices make those shifts visible and acceptable rather than silent and imposed.

**Theoretical framing.** Rather than treating older adults in the Global South as forgetful individuals in need of technological correction, we begin from the assets their households already hold. Our formative interviews document a working care system: younger relatives operate devices by proxy, health decisions are made together, prescriptions are deciphered around the kitchen table, and checking on a parent doubles as an expression of love. The agent is designed to join this system, not to replace it. We contrast this collectivist arrangement with the individualist assumptions built into mainstream adherence tools, which defend autonomy, privacy, and independence as if care threatened all three. The mismatch is structural, not a matter of localization.

**The agent's shifting role.** An agent embedded in a care network cannot keep one master. We analyze it across three roles: a tool aligned with the older adult, which protects privacy and supports independent routine; a coach shared between older adult and caregiver, which surfaces missed doses and proposes joint activity; and an advocate aligned with the family, which takes initiative when capability declines. Families move the agent between these roles. We describe that movement with four questions: in which direction the agent's allegiance currently points, whether every member of the care network can see it, who has standing to pull it back, and through what ceremony a shift is announced and accepted.

**The prototype, described honestly.** The system section states which decisions the agent takes on its own, which follow fixed rules, and which wait for human confirmation, and it grounds each claim in decision logs from deployment rather than in capability language. Its central mechanism is the Affiliation Ledger, a consent choreography with four commitments. The agent announces in plain Bangla whom it currently serves. A change of role requires a visible request and grant. The older adult holds a veto that weakens gradually and audibly, never silently, as health risk grows. Silence from the older adult is read as a patterned form of participation rather than as failure, an interpretation our formative work supports. Onboarding adds a probationary mode that invites people to test the agent before trusting it; we observed exactly this testing behavior in our first deployment, and the feature turns a found practice into a design commitment.

**Gamification, demoted and renamed.** Points and streaks appear in the system, but not as behavioral levers. We treat them as relational triggers, small occasions the agent creates for family members to express care, as when a daughter tells her mother how far her score has climbed. Our deployment data complicates the mechanism rather than confirming it: a broken streak produced real if mild grief, and one participant asked for shared family scores in place of a private tally. The household study implements that request and asks whether shared framing turns the anxiety of loss into mutual encouragement.

**The empirical arc.** The program runs from a formative interview study of 26 older adults and caregivers, through deployment and evaluation of the working prototype, to a multi-week household study in which older adult and caregiver use the agent together. In the household study the same caregiving episode is narrated by both parties and matched against the agent's own decision log. Each phase answers a question the previous one raised.

---

## 2. Novelty

Alignment research assumes the agent answers to a single principal: one user, one master, fixed at configuration. Work on multi-stakeholder health technology has mapped the tensions of caregiver dashboards and shared monitoring, yet its systems are passive; none must itself decide whom to serve and when to say so. Research on technology use in Bangladesh and the wider Global South has documented proxy use and family mediation with care, but its object has been the mediated tool rather than an agent whose loyalty the family negotiates. The gap sits at the intersection of the three. No empirical account exists of a household assigning, contesting, and revoking an autonomous agent's allegiance in daily life, and that is the account we provide. The work also carries a finding that runs against expectation. Several older adults treated handing the agent's loyalty to their children not as surrendered independence but as an exercise of agency, a performance of trust that deepened kinship; Western aging research, which builds its designs around preserving autonomy, predicts the opposite. Deployment produced two further results a formative study could not reach. Participants trusted the agent only after running verification tests of their own design, and sustained use appeared to retrain rather than replace their internal sense of when a dose was due.

---

## 3. Motivation

Older adults managing several chronic conditions carry medication schedules that punish small lapses. One caregiver in our formative study described her diabetic mother hospitalized after a dose forgotten at a wedding. Adherence technology has answered this risk with tools built for a different world, one in which a single user holds a private device, keeps a personal schedule, and defends autonomy against everyone else. In a Bangladeshi household none of those assumptions holds. Devices are shared and operated by proxy, health decisions are collective, and being checked on reads as love as much as oversight. A tool that assumes a lone user does not merely underperform in this setting; it is misaligned with the setting's structure.

The urgency comes from the technology side. Agents now escalate, withhold, and act rather than merely remind, and every one of those acts answers the question of whom the agent serves, today by silent default and usually in favor of whoever configured the device. Both directions of error are costly. An agent that reports everything to caregivers becomes surveillance and strips the older adult of dignity; an agent that guards the older adult absolutely can hide genuine danger from the people responsible for responding to it. The same unanswered question waits for household assistants, shared financial agents, and classroom AI. We study it in eldercare because that is where care is most explicitly collective, and where the negotiation is therefore easiest to see.

---

## 4. Research Questions

**RQ1 (Formative).** How do Bangladeshi intergenerational care networks distribute, claim, and morally account for medication work, and which existing relational assets, from proxy device use to collective decision-making to checking-as-care, does that work run on?

**RQ2 (Interaction).** When an agent with genuine initiative joins such a care network, through what everyday practices do older adults and caregivers assign, contest, share, and revoke its allegiance, and what makes a shift acceptable to the family?

**RQ3 (Design and Outcomes).** Which of the agent's roles, whether tool, coach, or advocate, do older adults and caregivers treat as legitimate under which conditions, and which design mechanisms make a change of role visible, negotiable, and dignity-preserving?

---

## 5. Contribution

**(C1) Empirical.** An account of how Bangladeshi care networks distribute and morally account for medication work before any technology arrives (RQ1), and of how the same networks negotiate an autonomous agent's allegiance once it does. The evidence pairs both sides of the same caregiving episode with the agent's logged decision for it, and it keeps the negative cases: families for whom shifting loyalty bred suspicion or was refused. The result is a typology of how allegiance is assigned, contested, gifted, and revoked.

**(C2) Conceptual.** A framework for alignment when the principal is a family rather than an individual: the tool, coach, and advocate roles, negotiated along four dimensions of direction, visibility, revocability, and ceremony. Any agent serving a household, a shared budget, or a classroom faces the same plural principal, so the framework travels beyond eldercare.

**(C3) Design.** Reusable mechanisms for agents that serve more than one person, centered on the Affiliation Ledger: the agent declares whom it serves, role changes pass through visible request-and-grant rituals, the older adult's veto weakens audibly rather than silently, and silence counts as participation. Scores and streaks are reframed as relational triggers, with evidence of when these mechanisms preserved dignity and when they failed to.

If agents are going to live inside families, their loyalty has to become something families can see and move. This proposal supplies the vocabulary and the mechanisms for making it so.
