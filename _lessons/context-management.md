---
title: Context Management
order: 9
summary: "Keep AI focused with fewer tools, bounded subagents, and clear handoffs between chats."
status: published
updated: 2026-09-15
---

A long AI conversation can become a messy workbench. The current plan sits beside abandoned ideas, old errors, search results, and instructions for jobs you finished yesterday.

**Context management** means deciding what the model needs in front of it for the next step. Keep that working set small enough to stay useful, with enough detail to do the job correctly.

## What fills the window

The **context window** is the material available to the model when it answers. Your latest message is only part of it. The harness can also supply standing instructions, conversation history, tool definitions, loaded skills, files, and tool results.

This is why a short request can arrive with a large amount of context. Asking an agent to inspect a failed test might add hundreds of lines of output. Repeating the test adds another result. [Anthropic's context-engineering guide](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) describes managing this growing working set throughout an agent's run.

Models measure context in **tokens**, roughly pieces of words. As a rough English-text estimate, 1,000 tokens is about 750 words. Code, other languages, and images use different amounts.

Here are two documented examples, checked September 15, 2026. They illustrate the range, rather than recommend particular models:

| Model | Documented capacity | What the number means |
| --- | --- | --- |
| [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | 32,768 tokens natively; up to 131,072 with a context-extension method called YaRN | The larger window requires the appropriate configuration. |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro) | 1,048,576 input tokens; 65,536 output tokens | Google lists input and output limits separately. |

Your app may expose less than the model's maximum. Check its context meter or documentation, and leave room for further work and the answer.

For scale, imagine a session containing 4,000 tokens of instructions, 12,000 of conversation, and 20,000 of file contents and logs. That's 36,000 tokens before the next reply. This is an illustrative budget, not a measurement of a particular app.

## Why a bigger window does not solve everything

**Context rot** is a name for declining reliability as context grows. The text has not literally decayed. The model becomes less reliable at finding or using the information it needs among everything else.

Chroma's [Context Rot research](https://www.trychroma.com/research/context-rot) found that added irrelevant material and distracting passages could reduce performance. The effect varied with the model and task. There is no universal token count where every model suddenly becomes unreliable.

A related problem is **lost in the middle**. Researchers found that the models they tested often used information near the beginning or end more reliably than information buried between them. That [study](https://arxiv.org/abs/2307.03172) tested older models; its results are a reason to check retrieval, not a fixed prediction for every current model.

Other problems can accumulate too:

- **Conflicting instructions.** An old plan says one thing; the current plan says another. Anthropic has [documented this problem](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) in overlapping instructions and skills.
- **Lost details after summarizing.** The app may compress the conversation to make room. An important exception can disappear from the summary.
- **More processing.** Extra input can increase cost and waiting time. Caching can reduce those costs, but does not remove irrelevant text from context.

Repeating an old mistake or ignoring a constraint can be a warning sign. It is not proof of context rot: a bad prompt, missing evidence, or a tool failure can produce similar symptoms.

## 1. Give the primary agent fewer tools

The **primary agent** is the one you talk to. On larger jobs, give it responsibility for the plan, delegation, and review. Give specialized work to agents with the tools for that work.

For example, a primary agent coordinating a website update might be able to read the brief and delegate tasks. A worker gets editing tools. A reviewer gets the tools needed to inspect and check the result.

This helps in two ways. Fewer loaded tool definitions leave less machinery in the primary agent's context. Delegation also keeps lengthy working material, such as build logs, with the worker that needs it.

To make delegation a requirement, restrict tool access in the harness and state who owns each task. A general shell can still edit files, so removing only an editing tool does not enforce that boundary. The primary must retain a way to delegate and inspect the evidence returned.

[Claude Code's subagent documentation](https://code.claude.com/docs/en/subagents) gives one implementation of separate contexts and tool permissions. Other harnesses expose different controls.

Skills are a separate consideration. Some harnesses initially load only skill descriptions and read the full instructions when needed. An installed skill is not necessarily taking up its full size in context. [Claude Code documents this distinction](https://code.claude.com/docs/en/skills).

## 2. Give subagents bounded jobs

A **subagent** handles a task on behalf of the primary agent. It can do the detailed reading and return a short report with evidence.

Useful jobs include checking one claim, inspecting one module, or reviewing one proposed change. Give each worker a clear result to produce:

```text
Check whether the three links in this section support its claims.
Read the section and linked sources. Do not edit files.
Return unsupported claims, suggested corrections, and source links.
Include uncertainties. Keep the report under 300 words.
```

Check how your harness starts workers. Some begin with a fresh context; others can inherit the parent's history. Copying the entire conversation into every worker carries the clutter along.

Keep detailed results in files when useful. Return conclusions, file locations, and enough evidence to check them. A summary without receipts can hide a worker's mistake.

Delegation has overhead. Several workers can use more total tokens even while keeping the primary's context smaller. For a one-line correction, a direct edit is usually enough. For independent research questions or separate modules, subagents have more room to help.

## 3. Plan in one chat, execute in another

Planning produces options, objections, and discarded approaches. Once you choose a direction, the execution chat needs the decision and its reasons.

Ask the planning chat for a handoff:

```text
Write a self-contained prompt for a fresh execution chat.
Include:
- the agreed goal and chosen approach;
- important decisions and why they were made;
- files or sources to read;
- constraints and actions that are out of scope;
- completed work and unresolved questions;
- the next step and how to check success.
Distinguish confirmed facts from assumptions.
```

Read and correct that handoff before moving it. Then open a new chat and supply the prompt and any required attachments. File paths only help if the new agent can access those files.

For this site, a planning chat might compare lesson outlines. The execution chat receives the chosen outline, the reading level, the references, and the requirement to preserve the author's voice.

## 4. Read only what the next step needs

Ask for a relevant section before an entire document. Search a repository before opening every file. Request the failure summary before a complete test log.

Keep the full source available so the agent can inspect surrounding material when the excerpt is insufficient. [Search and RAG]({{ '/learn/search-knowledge-and-rag/' | relative_url }}) help retrieve the right material for the question.

The same principle applies to instructions: remove duplicates and obsolete rules, while keeping current constraints. Cutting a requirement that prevents a real mistake makes the context smaller and the work worse.

## 5. Keep a short record outside the chat

Maintain a brief note with the current goal, decisions, completed work, open problems, and next step. Link to evidence and detailed files.

Update it when a decision changes. A stale note can restart the wrong plan just as easily as a stale conversation.

Some apps do **compaction** automatically: they summarize the conversation and continue from that summary. Check important constraints after a compaction. Anthropic's [guide to compaction and note-taking](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) explains the tradeoff: summaries save space but can omit details.

## Try it on your next long task

1. Write the goal and the few constraints that matter.
2. Give the primary agent only the tools its role needs.
3. Delegate a self-contained task with a clear return format.
4. Keep evidence in accessible files and bring concise findings back.
5. At a phase change, review a handoff and start a fresh chat if the old history is mostly finished work.
6. Check the result against the original goal.

The useful question is: **does the agent have the right information for its next decision?** A large context window gives you room. Context management helps you use that room well.
