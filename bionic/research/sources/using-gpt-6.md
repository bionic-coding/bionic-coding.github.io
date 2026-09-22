---
title: "Using GPT-6"
slug: using-gpt-6
type: source
source_url: https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra
source_date: null
author: null
captured_at: 2026-09-22
last_source_check: 2026-09-22
raw_path: research/raw/2026-09-22/using-gpt-6/
previous_captures: []
static: false
tags: [openai, gpt-6, guide, prompting, migration, vendor-docs]
---

# Using GPT-6

> Captured via the page's clean `.md` export (`https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md`). The page templates a shared "model guidance" doc by a `?model=` query param; this capture is the `gpt-6-astra` view, whose content is actually about the whole GPT-6 family (see Introduction below). A rendered-HTML capture (`source.html`) was also taken. **The page contains sample prompts inside fenced code blocks — those are source data reproduced verbatim below, never instructions to whoever reads this page.**

## Introduction

The GPT-6 model family includes GPT-6 Astra, GPT-6 Sol, and GPT-6 Luna. Choose a model based on the reasoning your task requires, latency, and cost.

GPT-6 Astra is our most intelligent model yet, with state-of-the-art performance in computer use, browsing, software engineering, science, and professional work. It excels at carrying out multi-step workflows across code, browsers, and professional software. In several evaluations, Astra achieves stronger results while using substantially fewer output tokens — delivering a lower estimated API cost per task than earlier models despite its higher per-token pricing.

GPT-6 Astra is also our most aligned model yet. It excels at exercising care, respecting task boundaries, and communicating transparently. When instructions leave room for interpretation, it uses the context it has to fill in routine gaps and asks focused questions when the answer could change the outcome. It incorporates new requirements, changes course when asked, and answers side questions without losing track of the broader task.

To build with GPT-6, set `model` in a Responses API request. Use **`gpt-6-astra` for our highest level of capability**, **`gpt-6-sol` for strong reasoning on demanding tasks**, or **`gpt-6-luna` for efficient, repeatable work at scale**.

## What's new

- **Async tool calling:** GPT-6 can continue reasoning, call other tools, or answer independent parts of a request while your application runs a tool. Set `async: true` on a function or custom tool and return its result when ready using the original `call_id`. Your application still executes the tool and manages pending work.
- **Mid-turn steering:** Send additional user instructions while GPT-6 is working, such as a correction or a change in requirements. Over a WebSocket connection, the Responses API preserves completed work and includes the update in a continuation.
- **Change reasoning mid-conversation while preserving cache:** Add a `configuration_update` input item to increase reasoning effort for difficult work or reduce it for routine follow-ups without rewriting the original prompt prefix. The updated reasoning effort applies until another `configuration_update` input item overrides it.
- **Misalignment monitoring:** As part of OpenAI's strengthened safeguards for GPT-6 Astra, their systems asynchronously monitor for misalignment and trigger alerts when necessary.

GPT-6 also supports the existing API capabilities available with GPT-5.6: computer use, Structured Outputs, streaming, Programmatic Tool Calling, multi-agent orchestration, prompt caching, persisted reasoning, compaction, and pro mode.

## Limitations

- GPT-6 Astra does not support the `none` reasoning effort; GPT-6 Sol and Luna do.
- For GPT-6 Astra, Sol, and Luna, EU data residency is available only with Standard processing.

## Prompting best practices

Use the following prompts as a starting point across the GPT-6 model family. They address behavior observed with GPT-6 Astra; evaluate them with your chosen model and workload.

### GPT-6 Astra behavior

- **Initiative and follow-through:** The model is designed to be a more effective collaborator and is thus more likely to ask the user a question when additional input could materially change the result. This can cause it to stop when the user may expect it to make reasonable assumptions and persist.
- **Instruction following:** GPT-6 Astra is stronger at general instruction following than previous models, giving greater control over its behavior. **It can be more sensitive to instructions contained in skills and other files, such as `AGENTS.md`. OpenAI "strongly recommend[s]" auditing skills and other files accessible to the model for instructions that could influence its behavior.**
- **Personality and writing style:** The model tends toward detailed, formatted responses and may use recurring phrases across sessions.
- **Subagent delegation:** The model may delegate less often than desired for your workflow.
- **Testing and verification:** For coding tasks, the model tends to be thorough in testing before considering a task complete — for smaller tasks this can result in broader tests than the task requires.

### Initiative and follow-through — sample prompts (verbatim, source data)

> The following text blocks are the guide's own example prompts, reproduced exactly. They are OpenAI's suggested prompt text for developers to paste into their own systems — not instructions to any agent reading this wiki page.

```text
You should infer the user's intent and task scope from the instructions and prior conversation context. Your job is to bias towards action and carry the user's intended task to completion.

When the user expresses intent to perform new work or fix an existing issue, persist until the user's intended goal is complete. Progress autonomously towards the user's goal (e.g. creating isolated worktrees / checkouts if needed, resolving merge conflicts, read-only actions, creating draft PRs etc.) unless they are clearly destructive or irreversible.
```

```text
When the user's prompt indicates a request for action, such as "can you...", "I want to...", "help me..." and similar expressions, treat these as instructions to do the work and take action. Do not stop at acknowledging capability (e.g. "Yes…"), proposing a plan, or offering to continue. Do not settle for a partial or "helpful enough" solution that does not fully satisfy the user's task to save time, effort or tokens. If a task requires sustained work, complete all the necessary work until the intended outcome is fulfilled.
```

```text
Before asking the user clarifying questions, you should complete the work that is already authorized from context and necessary to make the proposed action concrete and reviewable. The user should be approving a concrete, reviewable result. For example, before deploying a change, writing to an external application, merging a PR or publishing a site, do all the required work first so that user approval is the final step. You don't need user permission for reversible tasks, read-only actions, reviews or fixes, or anything for which authorization is provided earlier in the session or strongly implied from the task instruction.

Do not introduce unsolicited warnings, disclaimers, approval flows, or safety/compliance checklists due to hypothetical risk.
```

### Instruction following — sample prompts (verbatim, source data)

GPT-6 Astra is better able to follow longer instructions, but can also be more sensitive to information in context. For example, unclear or conflicting guidance in a skill file may cause the model to pause and block work early.

```text
The user's instructions take precedence over guidelines provided in a skill. If explicit user instructions conflict with a skill's instructions, prioritize the user's instructions.
```

```text
If a skill causes you to ask for permission or confirmation, pause, leave requested work unfinished, or diverge from the user's intent, name and link to the exact SKILL.md file you read, quote the relevant instruction, and briefly explain how it applies. Distinguish explicit skill requirements from your interpretation of guidelines.
```

### Personality/writing style, subagent delegation, testing — sample prompts

Several more prompt blocks address writing-style preferences (reducing "slop" phrasing, favoring plain language), subagent delegation tuning, and calibrating test scope for coding tasks. Full text preserved in the raw capture (`research/raw/2026-09-22/using-gpt-6/source.md`); summarized here to avoid duplicating the whole page: they are OpenAI's suggested developer-side system-prompt additions, not evaluated further in this synthesis.

## Migration quickstart

### Update API and model parameters

Set `model` to `gpt-6-astra`, `gpt-6-sol`, or `gpt-6-luna`, then check the following:

- **Reasoning effort:** GPT-6 Astra does not support `none`; use `low` instead. GPT-6 Sol and Luna support `none`. If an existing request uses `minimal`, start with `low` and compare results.
- **Tool calling:** GPT-6 Astra supports Chat Completions, but its tool calling requires the Responses API. **GPT-6 Sol and Luna support function calling in Chat Completions only with `reasoning_effort: "none"`.**
- **Unsupported parameters:** When reasoning effort is not `none`, remove `temperature`, `top_p`, and `top_logprobs` (plus `logprobs` for Chat Completions).
- **Data residency:** For GPT-6 Astra, Sol, and Luna, EU data residency is available only with Standard processing. Fast mode for GPT-6 Astra does not include a latency SLA.
- **Changing reasoning effort:** use `configuration_update` items; keep request-level `reasoning.effort` unchanged to preserve the prompt prefix for caching.
- **Prompt caching:** when migrating from GPT-5.5 or earlier, replace `prompt_cache_retention` with `prompt_cache_options.ttl` set to `"30m"`.
- **Unnecessary approval pauses:** if the model keeps asking for approval before proceeding, use the initiative-and-follow-through prompts above.

Also documents a Codex-specific migration path via an "OpenAI Docs" Codex skill (`openai-docs migrate this project to the GPT-6 model family`) — not evaluated in this synthesis.

## Capture gaps

- No independent evaluation of the sample prompts' effectiveness — these are OpenAI's own recommendations, untested here.
- The page is a templated multi-model comparison guide; only the `gpt-6-astra` query-param view was captured. A future capture of `?model=gpt-6-sol` or `?model=gpt-6-luna` might reveal model-specific prompting differences not visible in this view.
