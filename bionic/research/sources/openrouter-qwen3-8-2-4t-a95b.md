---
title: "OpenRouter model page — Qwen: Qwen3.8 2.4T A95B"
slug: openrouter-qwen3-8-2-4t-a95b
type: source
source_url: https://openrouter.ai/qwen/qwen3.8-2.4t-a95b
source_date: null
author: null
captured_at: 2026-09-01
last_source_check: 2026-09-01
raw_path: research/raw/2026-09-01/openrouter-qwen3-8-2-4t-a95b/
previous_captures: []
static: false
tags: [openrouter, qwen, open-weights, pricing, serving, providers]
---

OpenRouter's model page for `qwen/qwen3.8-2.4t-a95b`, captured 2026-09-01. The page is a **rolling dashboard**: provider prices, discounts, latency, throughput, uptime, per-provider benchmark scores, and the top-apps list all change daily. Treat every number below as a 2026-09-01 snapshot. The page's "Released" date and the API record's `created` field are the stable facts. The author uses this model as part of the current working set (see [[research/references/open-weights-landscape-2026]]).

## OpenRouter API record (`/api/v1/models`, fetched 2026-09-01; saved as `api.json` in the raw capture)

| field | value |
|---|---|
| id | `qwen/qwen3.8-2.4t-a95b` |
| canonical_slug | `qwen/qwen3.8-2.4t-a95b-20260812` |
| name | Qwen: Qwen3.8 2.4T A95B |
| created | 2026-08-12 (epoch 1786551702) |
| hugging_face_id | `Qwen/Qwen3.8-2.4T-A95B` |
| modality | `text->text` (in: text; out: text) |
| tokenizer | Qwen |
| context_length | 1,048,576 |
| top_provider.context_length | 1,000,000 |
| top_provider.max_completion_tokens | 262,144 |
| pricing.prompt (per MTok) | $2 |
| pricing.completion (per MTok) | $6 |
| pricing.input_cache_read (per MTok) | $0.25 |
| pricing.input_cache_write (per MTok) | — |
| is_moderated | False |
| supported_parameters | `frequency_penalty`, `include_reasoning`, `logit_bias`, `logprobs`, `max_tokens`, `min_p`, `presence_penalty`, `reasoning`, `reasoning_effort`, `repetition_penalty`, `response_format`, `seed`, `stop`, `structured_outputs`, `temperature`, `tool_choice`, `tools`, `top_k`, `top_logprobs`, `top_p` |

OpenRouter's description field: Qwen3.8 2.4T A95B is an open-weight sparse mixture-of-experts model from Qwen and the open-weight variant of [Qwen3.8 Max](/qwen/qwen3.8-max), with 95 billion active parameters out of 2.4 trillion total. It is...


## Page content as captured (`web-to-markdown`, 2026-09-01)

> Layout note: in the provider table, a cell such as `$1.30$1.17` is a struck-through list price followed by the discounted price; the discount badge (e.g. `10% off`) is glued to the provider name. Favicon images were stripped.

# Qwen: Qwen3.8 2.4T A95B

### [qwen](<https://openrouter.ai/qwen>)/qwen3.8-2.4t-a95b

[Model weights](<https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B>)

[Compare](<https://openrouter.ai/compare/qwen/qwen3.8-2.4t-a95b>)PlaygroundTry this model

Qwen3.8 2.4T A95B is an open-weight sparse mixture-of-experts model from Qwen and the open-weight variant of [Qwen3.8 Max](<https://openrouter.ai/qwen/qwen3.8-max>), with 95 billion active parameters out of 2.4 trillion total. It is suited for coding, research, complex reasoning, and agentic workflows.

Modalities

In / Out Price

$2 / $6per 1M

Context

1M

Released

Aug 12, 2026

Qwen: Qwen3.8 2.4T A95B

[Compare](<https://openrouter.ai/compare/qwen/qwen3.8-2.4t-a95b>)PlaygroundTry this model

Providers

## Providers

Different companies host the same model. OpenRouter routes your request to one of them based on the routing mode you pick — Balanced (price + speed), Nitro (fastest), or Exacto (highest tool-calling accuracy).

## Pricing

The average price customers actually pay for this model, next to the prices providers post. Caching and discounts mean the price actually paid is often well below the listed one.

## Performance

Throughput is how fast the model writes (tokens per second — higher is better). Latency is total round-trip time (lower is better). TTFT is time-to-first-token — how long before you see anything appear (lower is better).

## Uptime

Uptime is the percentage of the past 3 days that at least one provider was responding to requests. Availability is the percentage of time that inference was successfully served. OpenRouter continuously monitors and uses the next-best provider when one returns an error.

## Benchmarks

Scores on standardized evaluations. Higher percentages are better — and rank percentile shows where this model lands among all models on OpenRouter.

## Apps

Public apps that send the most traffic to this model. Good signal for what real production workloads look like — and a hint at which use cases this model is best suited for.

## Activity

Token volume and request traffic to this model over time.

## Quick Start

Drop-in code to call this model. OpenRouter's API is OpenAI-compatible — most SDKs work by just swapping the base URL. The only thing that changes between models is the model slug below.

## Explore more models

[AI Model RankingsRanking](<https://openrouter.ai/rankings>)

Standard

Latency / throughputP50

Provider| Input /M| Output /M| Cache read /M| Cache create 5m /M| Cache read 5m /M| Latency| Throughput| Uptime  
---|---|---|---|---|---|---|---|---  
DeepInfra| $2.00| $6.00| $0.20| \--| \--| 1.75s| 55 tps| 98.87%  
Modal| $2.00| $6.00| $0.25| \--| \--| 0.35s| 87 tps| 99.23%  
Alibaba Cloud Int.| $2.00| $6.00| $0.25| $2.50| $0.17| 2.26s| 35 tps| 100.00%  
NovitaAI| $2.00| $6.00| $0.25| \--| \--| 2.61s| 34 tps| 99.90%  
SiliconFlow| $2.00| $6.00| $0.25| \--| \--| 1.81s| 34 tps| 99.99%  
Together| $2.50| $6.25| $0.50| \--| \--| 0.71s| 164 tps| 99.93%  
Venice| $2.50| $7.50| $0.3125| \--| \--| 2.75s| 90 tps| 99.56%  
  
Throughput

164tok/s

P50, best across providers

Latency

0.35s

P50, best provider

All locations

Latency / throughputP501 week

AutoExacto Benchmarks

GPQA DiamondTAU-Bench

DeepInfra

87.3%79.0%

Venice

91.2%72.9%

auto-routing

84.3%76.7%

Alibaba Cloud Int.

85.3%75.3%

Modal

86.0%74.0%

+3 more providers

Uptime (3d)

100.00%

Availability (3d)

99.88%

### Availability over the last 3 days

Last 72 hours

Availability 99.88%

3 Days Ago2 Days AgoYesterdayNow

### Availability over the last 24 hours

OpenRouter Availability

99.90%

Without Routing

96.03%

When an error occurs in an upstream provider, we can recover by routing to another healthy provider, if your request filters allow it. You can access per-provider uptime data programmatically through the [Endpoints API](<https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints>). [Learn more](<https://openrouter.ai/docs/provider-routing>) about our load balancing and customization options.

1.

[pi ](<https://openrouter.ai/apps/pi>)

There are many coding agents, but this one is yours.

7.95Btokens

2.

[Hermes Agent ](<https://openrouter.ai/apps/hermes-agent>)

Hermes Agent is an open-source, self-improving AI agent by Nous Research that runs persistently with memory across sessions, and builds reusable skills from experience. It comes with 40+ built-in tools, including web search, browser automation, and vision, plus scheduled automations and subagents.

5.92Btokens

3.

[omp ](<https://openrouter.ai/apps/url/https%3A%2F%2Fomp.sh%2F>)

new

4.76Btokens

4.

[Claude Code ](<https://openrouter.ai/apps/claude-code>)

Claude Code is Anthropic's agentic coding tool that reads your entire codebase, plans and executes changes across files, runs tests, and iterates on failures, all from natural language prompts.

2.26Btokens

5.

[Kilo Code ](<https://openrouter.ai/apps/kilo-code>)

Kilo Code is an open-source AI coding agent that works across VS Code, JetBrains, and CLI to help developers ship code faster with agentic workflows.

2.18Btokens

Filter quantization

## Frequently asked questions

### What is Qwen3.8 2.4T A95B?

Qwen3.8 2.4T A95B is an open-weight sparse mixture-of-experts model from Qwen and the open-weight variant of Qwen3.8 Max, with 95 billion active parameters out of 2.4 trillion total. It is suited for coding, research, complex reasoning, and agentic workflows.

### How much does Qwen3.8 2.4T A95B cost?

Qwen3.8 2.4T A95B costs $2.00/M input tokens and $6.00/M output tokens, with separate rates for Cache Read at $0.20/M tokens.

### What is the context length of Qwen3.8 2.4T A95B?

Qwen3.8 2.4T A95B has a 1,048,576 token context window. It supports up to 131,072 completion tokens.

### Does Qwen3.8 2.4T A95B support tool calling and structured outputs?

Yes. Qwen3.8 2.4T A95B accepts `tools` and `tool_choice` for function calling. It also supports structured outputs via a JSON schema in `response_format`.

### Which providers serve Qwen3.8 2.4T A95B?

Qwen3.8 2.4T A95B is served by 7 providers on OpenRouter: DeepInfra, Modal, Alibaba Cloud Int., NovitaAI, SiliconFlow, Together and Venice. Requests are routed to the best available provider, with automatic failover to the others, and you can pin or exclude providers with [provider routing](<https://openrouter.ai/docs/features/provider-routing>).

### When was Qwen3.8 2.4T A95B released?

Qwen3.8 2.4T A95B was released on August 12, 2026.

## Capture gaps

- Charts (pricing history, latency/throughput, uptime, activity) are rendered client-side and were not captured; only their headline figures survive in the text.
- Per-provider benchmark rows list only the first few providers ("+N more providers" collapsed on the page).
- The "Quick Start" code sample and "Explore more models" links were not captured.
- Rolling page: `static: false`, so `refresh-research-sources` re-checks it. Compare prices against the API record's `created` date and the page's "Released" date, which do not change.
