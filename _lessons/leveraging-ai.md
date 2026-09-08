---
title: Leveraging AI
order: 10
summary: "How to use AI for ambitious work without surrendering judgment."
status: published
updated: 2026-09-07
---

Maybe I should have titled this lesson **Don't Make Slop**.

Nobody needs more generic AI output. If a reader could get the same result from a one-line prompt, you have not added much. The useful question is not, “Can AI make this?” It is, “What can I make now that used to require unreasonable time, money, or coordination?”

AI is most valuable when it expands the work you can attempt while you keep responsibility for the result.

## Use AI where effort used to be unreasonable

Good magic often looks like somebody spent more time on a detail than anyone expected. AI changes what counts as a reasonable amount of effort.

You can now afford to:

- compare several plans before choosing one;
- ask agents with different instructions or models to challenge the same decision;
- investigate every factual claim in an article;
- build and discard many prototypes before committing to a direction;
- generate tests, edge cases, and failure scenarios that would otherwise be postponed;
- explain the same difficult idea for a beginner, a practitioner, and an expert.

The first draft is rarely the advantage. The advantage is the extra exploration, criticism, and verification that AI makes affordable.

This website is an example. AI can help collect sources, organize a lesson, find weak claims, test links, and check the finished site. It cannot decide what Bionic Coding should stand for. That judgment stays with me.

## Drive or navigate

You will usually get the best work when you take one of two roles:

- **Drive:** choose the direction, break down the work, and ask AI to execute bounded parts.
- **Navigate:** let an agent propose and carry out a plan while you inspect decisions, redirect it, and approve consequential actions.

Trouble starts when nobody is doing either job. An agent that controls both the plan and the work can produce a polished answer to the wrong problem. It may also create fifty pages where two would do, repeat a weak assumption at greater scale, or make changes that are hard to reverse.

Staying involved does not mean watching every token. It means making the important decisions explicit:

- What result are we trying to produce?
- What must remain true?
- What can the agent change?
- What evidence will count as success?
- Which actions require approval?

That is why a clear prompt matters, but it is also why [evals]({{ "/learn/prompting-and-evals/" | relative_url }}), tests, and review matter. Instructions describe the destination. Checks tell you whether you arrived.

## Separate exploration from commitment

AI makes it cheap to explore, but not every idea deserves to become a change.

A useful pattern is:

1. **Explore.** Ask for several approaches, risks, or examples. No changes yet.
2. **Choose.** Decide which direction serves the goal and record why.
3. **Build a small slice.** Make the smallest change that tests the direction.
4. **Verify.** Run tests, check sources, inspect the output, or ask another agent to challenge it.
5. **Continue or revise.** Expand only when the evidence supports the direction.

This separation prevents a brainstorm from quietly turning into a production decision. It also gives you useful places to stop an agent before it spends money, writes files, sends messages, or changes a shared system.

## Make the work inspectable

The harder an AI system works on your behalf, the more important it becomes to leave evidence behind.

For software, that evidence might be tests, a readable diff, a decision record, or a list of commands that passed. For research, it might be direct links, publication dates, and a label that separates verified facts from vendor claims. For writing, it might be a clear audience, an outline you approved, and a final fact-check.

Do not settle for “the agent says it worked.” Ask for an artifact you can inspect.

This is also where small, reusable [skills]({{ "/learn/skills/" | relative_url }}) help. A skill can teach an agent your preferred review process, safety limits, or output format. A project memory such as [Crux]({{ "/crux/" | relative_url }}) can preserve the objective and decisions between sessions. Neither replaces judgment. Both make it easier to apply judgment consistently.

## A practical loop

Try this on your next task:

1. Write the outcome in one sentence.
2. List two or three things that must not go wrong.
3. Ask AI for options before asking it to produce the final result.
4. Choose an option and explain your choice.
5. Have the AI make one bounded pass.
6. Check the result with evidence appropriate to the work.
7. Keep, revise, or discard it.

For a low-risk task, this loop may take five minutes. For a large code change or a factual article, it may involve several agents and several rounds of review. The shape is the same: intent, options, choice, execution, evidence.

## The test

Ask two questions when the work is done:

1. **Did AI let me attempt something more ambitious or verify it more thoroughly?**
2. **Can I still explain and defend the result?**

If the answer to the first is no, AI may only have made an ordinary task noisier. If the answer to the second is no, you have given away too much control.

The goal is not automatic production. It is bionic work: more reach, more iteration, and more evidence, with a human still responsible for what ships.

## Try a runnable example

The [Samples]({{ "/learn/samples/" | relative_url }}) lesson has copy-paste prompts, a skill, an agent task, and an evaluation rubric. Start with a read-only example, inspect the result, and adapt it to work you already understand.
