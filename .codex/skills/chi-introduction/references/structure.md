# The Six-Part Introduction Recipe

The Drop → World Building → The Players → Player One → The Deal → The Loot

Vaguely inspired by the hero's journey, with video-game terminology. The goal of the whole structure: make the rest of the paper feel inevitable. A reviewer forms an opinion quickly after the introduction — whether the authors understand the problem, have thought carefully about the literature, have somewhere interesting to go, and whether the reviewer is in good hands. A strong introduction creates that feeling of security.

**Write the introduction last.** It has to tie the entire paper together, and you cannot tie together something that does not yet exist. Findings might change what the paper is about; the discussion might reveal the contribution more clearly; sometimes the argument you thought you were making does not survive the data.

---

## Part 1: The Drop — Why does this problem matter?

The first job of an introduction is NOT to define the problem. It is to make the reader care about the problem.

Many introductions begin with conceptual housekeeping: "Conversational agents are systems that allow users to interact with computers using natural language…" That sentence may eventually need to exist, but not first.

**Techniques:**
- **Drop into a scene where the problem already hurts.** Example: a paper on serious illness conversations opens with a patient with end-stage heart failure arriving in the ED in severe respiratory distress; within minutes the clinician must choose between aggressive intervention and comfort-focused care during what may be the patient's final hours. Suddenly there is a person, a decision, very little time — and the decision should reflect what the patient wants. But what if nobody knows what the patient wants? Now you have attention. Only after establishing stakes do you explain terminology and workflows.
- **The "you must be wondering how I got here" move.** Like movies that open mid-action: the reader watches something unfold without full understanding; the introduction fills in the missing pieces.
- **Start with a story.** A paper on personality in LLM-based agents opens in 1966 with ELIZA: simple pattern matching, yet people responded socially — Weizenbaum's secretary asked to be left alone with it despite knowing how it worked. The drop then creates the question: if people perceived personality in something as simple as ELIZA, what happens with an LLM?
- **A striking statistic** or a situation the reader immediately recognizes.

Your first sentence has a disproportionate amount of work to do — like the opening joke of a comedy set, it should be one of your strongest. Do not waste it.

**Failure modes:** opening with a definition; opening with "In recent years, X has become increasingly important"; stakes that are asserted ("X is a critical problem") rather than shown.

## Part 2: World Building — What is the problem, exactly?

Now that the reader cares, you can explain things: what concepts they need, what causes the problem, where it happens, who is affected, who the stakeholders are, what assumptions or constraints shape this environment.

For serious illness conversations: what those conversations involve, why they are difficult in EDs, which clinicians, patients, and family members are involved. For LLM personality: what personality means in conversational systems, how it can be simulated, why it might matter differently in casual vs. goal-oriented interaction.

This is where many introductions start too early — defining everything before showing why the definition is needed. Once you have shown that something consequential is happening, the reader is willing to learn the rules of the world. Like a video game: something gets you interested enough to play, then the game teaches you the buttons, the rules, the goal.

The reader should leave this section knowing what world they are in and how it works. They should not have to guess.

## Part 3: The Players — What has been done before?

Introduce everyone who got here before you: researchers, theories, systems, methods, studies.

Practical reality: the people you cite are very likely your reviewers. HCI is not that big. Keep that in mind before writing "Prior work has failed to consider…"

**Do not make previous research look bad to make your paper look good.** A paper can be excellent and still leave something unresolved — most good papers do. One study establishes that something happens without explaining why; another works for one community but says little about another; a system solves one problem while creating new questions. That is how research progresses.

**Give previous work its flowers.** Explain what those researchers did, what they allowed us to understand, why it mattered. Then identify the limitation, blind spot, or unanswered question that lets your work move the conversation forward.

The framing difference:
- Not: "These people did a bad job, and now we are here to fix it."
- Instead: "Because of what these people taught us, we can now ask the next question."

That is the stronger intellectual position anyway.

For interdisciplinary work, this section may introduce two groups of players — HCI and healthcare, psychology, communication, education — and explain how the paper bridges them.

By the end, the reader should understand the existing landscape and start noticing an empty space in it. That empty space is where you enter.

## Part 4: Player One — What are you doing differently?

The most important transition in the introduction. Player One is you. Stop hiding.

Be specific about the gap. Be specific about your approach. Be specific about what makes your study necessary.

Authors often spend two pages making a strong argument and then write "In this paper, we explore…" Sometimes explore is the right word; often it is just a safer word than the one meant. There is a strange tendency in academic writing to become less confident precisely when describing our own contribution. The opposite should happen.

- If you argue something, say you argue it.
- If you propose something, say you propose it.
- If you introduce a framework, introduce it.
- If you demonstrate an effect, say what you demonstrate.

This section answers: What is the specific gap? What approach are you taking? What methods, theories, or conceptual lenses? Why is that approach useful or novel given what came before?

Clarity matters more than elegance here. You cannot write poetry forever; at some point you have to say what the paper actually does.

## Part 5: The Deal — What are your research questions?

Prefer putting RQs directly in the introduction unless there is a strong reason not to. Research questions establish **a contract with the reviewer**: "Here are the questions I promise this paper will answer."

That contract disciplines the rest of the paper. If RQ1 asks one thing, a finding should answer RQ1. If RQ2 builds on RQ1, the findings should reflect that progression. The reviewer should be able to draw a clean line from questions promised to evidence provided.

**Order matters.** RQ1–RQ3 should not feel like three unrelated questions that survived a lab meeting. They should tell a story: perhaps the first establishes a phenomenon, the second explains how or why, the third asks what it means for design.

**RQs should feel inevitable.** A well-constructed introduction is an intellectual funnel: by the time the reader reaches the RQs, they should almost be able to predict them. If a reader thinks "wait, why are we asking this?", the problem is usually not the RQ — go back and fix the world building or the gap.

## Part 6: The Loot — What did you find, and what do you contribute?

Briefly state what you found and, more importantly, what those findings contribute.

Phrases like "This work provides insights into…" or "Our findings have implications for…" are incomplete until you say what the insight is and who the implication is for. Be concrete:
- A set of design strategies practitioners can use
- A change in how researchers should conceptualize a phenomenon
- Something important about how a community experiences a technology
- A tradeoff designers need to account for

Different papers generate different loot, and different people value different parts: a designer cares about actionable implications, a researcher about a conceptual framework, a clinician about workflow fit, an end user about what changes in systems built for them. **Say who gets what.** This matters especially for literature reviews, where one synthesis yields different contributions for researchers, designers, and practitioners.

Do not make the reviewer reverse-engineer your contribution from twenty pages of findings. Name the insight. Name the audience. Name the implication. Make the journey feel worth it.

---

## Flexing the scaffold

Not every introduction needs six paragraphs. World building might take two. The Players and Player One might be tightly intertwined. Some papers place RQs after related work. Different kinds of HCI papers bend the structure differently. That is fine — what matters is the logic underneath.

A reviewer should finish the introduction understanding: why the problem matters, what world they are in, what we already know, what remains unresolved, what you are doing about it, what you promise to answer, and why the answer is useful. Then the reviewer stops trying to figure out what the paper is supposed to be — and can just read it.

## Final checklist

- [ ] First sentence earns its position (scene, story, stat — not a definition)
- [ ] Stakes established before terminology
- [ ] World building gives every concept the reader needs, no more
- [ ] Prior work praised fairly; one gap per paragraph; no "prior work failed"
- [ ] Player One states gap + approach + necessity with confident verbs
- [ ] RQs present, ordered as a story, and feel inevitable
- [ ] Loot names the insight, the audience, and the implication
- [ ] The whole thing funnels: a reader could almost predict the RQs before reaching them
