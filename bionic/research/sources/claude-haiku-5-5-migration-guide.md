---
title: "Claude Haiku 5.5 migration guide"
slug: claude-haiku-5-5-migration-guide
type: source
source_url: https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide
source_date: null
author: "Anthropic"
captured_at: 2026-10-07
last_source_check: 2026-10-07
raw_path: research/raw/2026-10-07/claude-haiku-5-5-migration-guide/
previous_captures: []
static: false
tags: [anthropic, haiku-5-5, models, pricing, benchmarks]
---

Capture method: direct HTTP using Crux web-to-markdown. UI icon glyphs and the copy-page label removed; guidance and examples preserved. Publication date not supplied.

# Claude Haiku 5.5 migration guide

This guide covers moving code that calls Claude Haiku 4.5 to Claude Haiku 5.5. To move up to a Sonnet or Opus model instead, see [Upgrade between model versions](<https://platform.claude.com/docs/en/about-claude/models/migration-guide>). For how long Claude Haiku 4.5 stays available, see [Model deprecations](<https://platform.claude.com/docs/en/about-claude/model-deprecations>).

## Migration checklist

Each item is one change to make in code that calls Claude Haiku 4.5.

  1. Replace the model ID with the Claude Haiku 5.5 ID for your platform. See [Use the Claude Haiku 5.5 model ID](<https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#use-the-claude-haiku-5-5-model-id>).
  2. Recount your prompts, and revisit `max_tokens` limits and cost estimates, because the same text counts as more tokens. See [Recount tokens](<https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#recount-tokens>).
  3. If your requests send `thinking: {"type": "enabled", "budget_tokens": N}`, change `thinking` to `{"type": "adaptive"}`. See [Configure thinking](<https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#configure-thinking>).
  4. If your code reads the first content block as the answer, select blocks by `type` instead. See [Configure thinking](<https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#configure-thinking>).
  5. Remove `temperature`, `top_p`, and `top_k` from your requests. See [Remove sampling parameters](<https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#remove-sampling-parameters>).
  6. If your requests end `messages` with an assistant turn for the model to continue, end them with a user turn instead. See [Replace assistant prefill](<https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#replace-assistant-prefill>).
  7. If you use computer use on the Claude API or Google Cloud, move from `computer_20250124` to the `computer_toolset_20260801` toolset. See [Move computer use to the toolset](<https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#computer-use-toolset>).
  8. If you replay stored conversations through a different account, replay each one through the account that produced it. See [Replay thinking blocks through the account that produced them](<https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#replay-thinking-blocks-through-the-producing-account>).
  9. If your code changes `system`, `tools`, or earlier `messages` between requests in a conversation and sends thinking blocks back, keep the conversation append-only. See [Keep earlier turns unchanged](<https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#keep-earlier-turns-unchanged>).
  10. Handle `stop_reason: "refusal"`. Claude Haiku 5.5 runs safety classifiers that can decline a request, and it has no server-side fallback. See [Safeguard refusals](<https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5#safeguard-refusals>).

If your organization has a [Priority Tier](<https://platform.claude.com/docs/en/api/service-tiers#supported-models>) commitment on Claude Haiku 4.5, plan capacity separately: Priority Tier is not supported on Claude Haiku 5.5.

## Use the Claude Haiku 5.5 model ID

Replace the Claude Haiku 4.5 model ID with the Claude Haiku 5.5 ID for your platform.

Platform| Claude Haiku 4.5| Claude Haiku 5.5  
---|---|---  
Claude API| `claude-haiku-4-5-20251001` or `claude-haiku-4-5`| `claude-haiku-5-5`  
Amazon Bedrock| `anthropic.claude-haiku-4-5`| `anthropic.claude-haiku-5-5`  
Claude Platform on AWS| `claude-haiku-4-5`| `claude-haiku-5-5`  
Google Cloud| `claude-haiku-4-5@20251001`| `claude-haiku-5-5`  
Microsoft Foundry| `claude-haiku-4-5`| `claude-haiku-5-5`  
  
`claude-haiku-5-5` is a fixed model ID with no date suffix and no separate alias.

## Recount tokens

Claude Haiku 5.5 uses the same newer tokenizer as Claude 4.7 and later models. As with all models that use this tokenizer, the same input text produces approximately 30% more tokens on Claude Haiku 5.5 than on Claude Haiku 4.5. The exact increase depends on the content. Requests, responses, and streaming events keep the same shape. What changes is anything you measure or budget in tokens:

  * `usage` fields and [token counting](<https://platform.claude.com/docs/en/build-with-claude/token-counting>) results are higher for the same text.
  * A given number of tokens holds less text.
  * A `max_tokens` limit tuned for Claude Haiku 4.5 may cut off equivalent output.
  * Cost estimates made from Claude Haiku 4.5's token counts need recomputing with Claude Haiku 5.5's counts and [prices](<https://platform.claude.com/docs/en/about-claude/pricing>).

Count your prompts with `model` set to `claude-haiku-5-5` rather than reusing counts measured on Claude Haiku 4.5.

## Configure thinking

Claude Haiku 5.5 configures thinking differently from Claude Haiku 4.5. A `thinking` value of `{"type": "enabled", "budget_tokens": N}` returns a 400 error, so a request that sends it needs a new `thinking` value.

Before, a request to Claude Haiku 4.5 set `thinking` to `enabled` with a token budget:
    
    
    {
      "model": "claude-haiku-4-5",
      "max_tokens": 16000,
      "thinking": { "type": "enabled", "budget_tokens": 8000 },
      "messages": [{ "role": "user", "content": "..." }]
    }



After, the same request to Claude Haiku 5.5 uses adaptive thinking. The `thinking` value changes, and `output_config.effort` sets how much the model thinks:
    
    
    {
      "model": "claude-haiku-5-5",
      "max_tokens": 16000,
      "thinking": { "type": "adaptive" },
      "output_config": { "effort": "medium" },
      "messages": [{ "role": "user", "content": "..." }]
    }



Adaptive thinking is on by default, so a response can begin with one or more `thinking` blocks even when the request doesn't set `thinking`. Leave `thinking` unset or set it to `{"type": "adaptive"}`, and use [effort](<https://platform.claude.com/docs/en/build-with-claude/effort>) as the lever: where Claude Haiku 4.5 ran without thinking, or with a small budget to save tokens, choose a lower effort level. At a lower level the model thinks less, and it can skip thinking entirely on simpler requests. For prompting guidance, see [Use effort to control thinking](<https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5#use-effort-to-control-thinking>). Select content blocks by their `type` field rather than by position, and pass `thinking` blocks back unmodified with tool results.

Thinking tokens count toward `max_tokens`, so a request with a small `max_tokens` can stop with `stop_reason: "max_tokens"` after a `thinking` block and before any text. If you set a small `max_tokens` for Claude Haiku 4.5, raise it to leave room for thinking, or choose a lower [effort](<https://platform.claude.com/docs/en/build-with-claude/effort>) level.

By default, Claude Haiku 5.5 returns each `thinking` block with an empty `thinking` field and only a `signature`, where Claude Haiku 4.5 returned summarized thinking. To receive summarized thinking, set `thinking: {"type": "adaptive", "display": "summarized"}`.

Claude Haiku 5.5 accepts a forced `tool_choice` (`any` or a named tool), but the response starts with the tool call and has no `thinking` block. To let the model think before it calls a tool, use `tool_choice: {"type": "auto"}` and say in the prompt when to use the tool.

## Remove sampling parameters

Claude Haiku 4.5 accepts `temperature`, `top_p`, and `top_k`. On Claude Haiku 5.5, omit all three and use prompting to guide the model's behavior instead. If a request includes `temperature`, it must be `1`. If it includes `top_p`, it must be `0.99`, its default. Any other `temperature` or `top_p` value returns a 400 error, including a `top_p` of `1`. So does any `top_k` value, and so does a request that includes both `temperature` and `top_p`.

## Replace assistant prefill

A prefill is a final assistant turn in `messages` that the model continues. Claude Haiku 4.5 accepts one when thinking is off. Claude Haiku 5.5 rejects it with a 400 error, even with thinking turned off. End `messages` with a user turn, and replace each prefill according to what it was for:

  * **Output format:** use [structured outputs](<https://platform.claude.com/docs/en/build-with-claude/structured-outputs>), or tools with enum fields for classification. On Claude in Amazon Bedrock, which doesn't support structured outputs, use tools.
  * **Preambles:** ask in the system prompt for a direct answer.
  * **Continuations:** move them to the user message, for example "Your previous response was interrupted and ended with `[previous_response]`. Continue from where you left off."
  * **Context reminders:** put them in the user turn.

## Move computer use to the toolset

Claude Haiku 4.5 supports [computer use](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool>) through the `computer_20250124` tool, with the `computer-use-2025-01-24` beta header. On the Claude API and Google Cloud, Claude Haiku 5.5 supports computer use only through the `computer_toolset_20260801` toolset, and a request that declares `computer_20250124` returns a 400 error.

To move an integration, drop the `computer-use-2025-01-24` beta header and replace the `tools` entry with `{"type": "computer_toolset_20260801"}`. Then make the other request and agent-loop changes in [Migrate from `computer_20251124`](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#migrate-from-computer-20251124>): dispatch on each member `tool_use` block's `name` and `toolset_name` rather than on `input.action`, handle every such block in a turn, and echo `toolset_name` on results. Zoom is on by default in the toolset; if your environment doesn't implement it, add `"configs": {"zoom": {"enabled": false}}`. If you send the `fine-grained-tool-streaming-2025-05-14` beta header, remove it. Alongside a toolset entry, it returns a 400 error. For other platforms, see the computer use tool's [Compatibility](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#compatibility>) section.

On the Claude API and Google Cloud, Claude Haiku 5.5 also supports the [browser use tool](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool>) (`browser_toolset_20260801`) for tasks inside webpages. Claude Haiku 4.5 doesn't support it.

## Replay thinking blocks through the account that produced them

Thinking blocks from Claude Haiku 5.5 work only in the account that produced them, or in an account linked to it. When another account sends one of these blocks, the API drops the block before the model sees it, and the request succeeds without that reasoning. This affects code that stores conversations and replays them through a different account, for example a service that serves several customers from one conversation store. Replay each conversation through the account that produced it. See [Thinking blocks stay with the account that produced them](<https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#account-bound-thinking>).

## Keep earlier turns unchanged

A Claude Haiku 5.5 thinking block stays valid only while everything sent before it is unchanged: a request that sends a thinking block back after a change to `system`, `tools`, or earlier `messages` returns a 400 error. Claude Haiku 4.5 doesn't run this check. Keep conversations append-only. On accounts created before August 31, 2026, 00:00 UTC, the error comes only on requests that set `thinking.block_binding.prefix_mismatch_behavior`. For the changes that trigger the error and what to do instead, see [Who needs to change anything](<https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#who-is-affected>).

Was this page helpful?
