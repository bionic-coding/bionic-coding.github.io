---
title: "OpenRouter model page — Qwen: Qwen3.8 Flash"
slug: openrouter-qwen3-8-flash
type: source
source_url: https://openrouter.ai/qwen/qwen3.8-flash
source_date: null
author: null
captured_at: 2026-09-01
last_source_check: 2026-09-01
raw_path: research/raw/2026-09-01/openrouter-qwen3-8-flash/
previous_captures: []
static: false
tags: [openrouter, qwen, alibaba, pricing, serving, multimodal]
---

OpenRouter's model page for `qwen/qwen3.8-flash`, captured 2026-09-01. The page is a **rolling dashboard**: provider prices, discounts, latency, throughput, uptime, per-provider benchmark scores, and the top-apps list all change daily. Treat every number below as a 2026-09-01 snapshot. The page's "Released" date and the API record's `created` field are the stable facts. The author uses this model as part of the current working set (see [[research/references/open-weights-landscape-2026]]).

## OpenRouter API record (`/api/v1/models`, fetched 2026-09-01; saved as `api.json` in the raw capture)

| field | value |
|---|---|
| id | `qwen/qwen3.8-flash` |
| canonical_slug | `qwen/qwen3.8-flash-20260826` |
| name | Qwen: Qwen3.8 Flash |
| created | 2026-08-26 (epoch 1787773060) |
| hugging_face_id | `Qwen/Qwen3.8-Flash-Next` |
| modality | `text+image+video->text` (in: text, image, video; out: text) |
| tokenizer | Qwen |
| context_length | 1,000,000 |
| top_provider.context_length | 1,000,000 |
| top_provider.max_completion_tokens | 131,072 |
| pricing.prompt (per MTok) | $0.15 |
| pricing.completion (per MTok) | $0.47 |
| pricing.input_cache_read (per MTok) | $0.016 |
| pricing.input_cache_write (per MTok) | $0.2 |
| is_moderated | False |
| supported_parameters | `frequency_penalty`, `include_reasoning`, `logprobs`, `max_tokens`, `presence_penalty`, `reasoning`, `response_format`, `seed`, `stop`, `structured_outputs`, `temperature`, `tool_choice`, `tools`, `top_k`, `top_logprobs`, `top_p` |

OpenRouter's description field: Qwen3.8 Flash is a multimodal reasoning model from Alibaba. It is suited for coding assistance, agentic workflows, visual understanding, document and codebase analysis, desktop interaction, chart analysis, and long-video analysis.


## Page content as captured (`web-to-markdown`, 2026-09-01)

> Layout note: in the provider table, a cell such as `$1.30$1.17` is a struck-through list price followed by the discounted price; the discount badge (e.g. `10% off`) is glued to the provider name. Favicon images were stripped.

# Qwen: Qwen3.8 Flash

### [qwen](<https://openrouter.ai/qwen>)/qwen3.8-flash

[Model weights](<https://huggingface.co/Qwen/Qwen3.8-Flash-Next>)

[Compare](<https://openrouter.ai/compare/qwen/qwen3.8-flash>)PlaygroundTry this model

Qwen3.8 Flash is a multimodal reasoning model from Alibaba. It is suited for coding assistance, agentic workflows, visual understanding, document and codebase analysis, desktop interaction, chart analysis, and long-video analysis.

Modalities

In / Out Price

$0.15 / $0.47per 1M

Context

1M

Released

Aug 26, 2026

Qwen: Qwen3.8 Flash

[Compare](<https://openrouter.ai/compare/qwen/qwen3.8-flash>)PlaygroundTry this model

Providers

## Providers

This model is hosted by one provider. OpenRouter forwards every request to it directly — no routing decisions to make.

## Pricing

The average price customers actually pay for this model, next to the prices providers post. Caching and discounts mean the price actually paid is often well below the listed one.

## Performance

Throughput is how fast the model writes (tokens per second — higher is better). Latency is total round-trip time (lower is better). TTFT is time-to-first-token — how long before you see anything appear (lower is better).

## Uptime

Uptime is the percentage of the past 3 days that at least one provider was responding to requests. Availability is the percentage of time that inference was successfully served. OpenRouter continuously monitors and uses the next-best provider when one returns an error.

## Apps

Public apps that send the most traffic to this model. Good signal for what real production workloads look like — and a hint at which use cases this model is best suited for.

## Activity

Token volume and request traffic to this model over time.

## Quick Start

Drop-in code to call this model. OpenRouter's API is OpenAI-compatible — most SDKs work by just swapping the base URL. The only thing that changes between models is the model slug below.

## Explore more models

[AI Models with Vision: Multimodal LLMs for Image UnderstandingCollection](<https://openrouter.ai/collections/vision-models>)[AI Model RankingsRanking](<https://openrouter.ai/rankings>)

Latency / throughputP50

Provider| Input /M| Output /M| Cache read /M| Cache create 5m /M| Cache read 5m /M| Latency| Throughput| Uptime  
---|---|---|---|---|---|---|---|---  
Alibaba Cloud Int.| $0.15| $0.47| $0.016| $0.20| $0.016| 1.63s| 59 tps| 99.99%  
  
Throughput

59tok/s

P50, best across providers

Latency

1.63s

P50, best provider

All locations

1 week

Uptime (3d)

100.00%

Availability (3d)

99.49%

### Availability over the last 3 days

Last 72 hours

Availability 99.49%

3 Days Ago2 Days AgoYesterdayNow

### Availability over the last 24 hours

OpenRouter Availability

99.63%

When an error occurs in an upstream provider, we can recover by routing to another healthy provider, if your request filters allow it. You can access per-provider uptime data programmatically through the [Endpoints API](<https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints>). [Learn more](<https://openrouter.ai/docs/provider-routing>) about our load balancing and customization options.

1.

[Hermes Agent ](<https://openrouter.ai/apps/hermes-agent>)

Hermes Agent is an open-source, self-improving AI agent by Nous Research that runs persistently with memory across sessions, and builds reusable skills from experience. It comes with 40+ built-in tools, including web search, browser automation, and vision, plus scheduled automations and subagents.

19.3Btokens

2.

[pi ](<https://openrouter.ai/apps/pi>)

There are many coding agents, but this one is yours.

6.42Btokens

3.

[omp ](<https://openrouter.ai/apps/url/https%3A%2F%2Fomp.sh%2F>)

new

5.61Btokens

4.

[DeepSeek Harness ](<https://openrouter.ai/apps/url/https%3A%2F%2Fgithub.com%2Fdeepseek-ai%2Fdeepseek-harness>)

new

4.02Btokens

5.

[Claude Code ](<https://openrouter.ai/apps/claude-code>)

Claude Code is Anthropic's agentic coding tool that reads your entire codebase, plans and executes changes across files, runs tests, and iterates on failures, all from natural language prompts.

3.96Btokens

## Frequently asked questions

### What is Qwen3.8 Flash?

Qwen3.8 Flash is a multimodal reasoning model from Alibaba. It is suited for coding assistance, agentic workflows, visual understanding, document and codebase analysis, desktop interaction, chart analysis, and long-video analysis.

### How much does Qwen3.8 Flash cost?

Qwen3.8 Flash costs $0.15/M input tokens and $0.47/M output tokens, with separate rates for Cache Read at $0.016/M tokens, Cache Creation (5min) at $0.20/M tokens and Cache Read (5min) at $0.016/M tokens.

### What is the context length of Qwen3.8 Flash?

Qwen3.8 Flash has a 1,000,000 token context window. It supports up to 131,072 completion tokens.

### Does Qwen3.8 Flash support tool calling and structured outputs?

Yes. Qwen3.8 Flash accepts `tools` and `tool_choice` for function calling. It also supports structured outputs via a JSON schema in `response_format`.

### What inputs and outputs does Qwen3.8 Flash support?

Qwen3.8 Flash accepts text, images and video as input and returns text.

### What other text models does Qwen have?

[Qwen3.8 27B](<https://openrouter.ai/qwen/qwen3.8-27b>), [Qwen3.8 2.4T A95B](<https://openrouter.ai/qwen/qwen3.8-2.4t-a95b>), [Qwen3.8 Max](<https://openrouter.ai/qwen/qwen3.8-max>) and 47 more are other text models from Qwen.

### When was Qwen3.8 Flash released?

Qwen3.8 Flash was released on August 26, 2026.

## Capture gaps

- Charts (pricing history, latency/throughput, uptime, activity) are rendered client-side and were not captured; only their headline figures survive in the text.
- Per-provider benchmark rows list only the first few providers ("+N more providers" collapsed on the page).
- The "Quick Start" code sample and "Explore more models" links were not captured.
- Rolling page: `static: false`, so `refresh-research-sources` re-checks it. Compare prices against the API record's `created` date and the page's "Released" date, which do not change.
