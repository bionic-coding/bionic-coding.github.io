---
title: "OpenRouter model page — Z.ai: GLM 5.3"
slug: openrouter-glm-5-3
type: source
source_url: https://openrouter.ai/z-ai/glm-5.3
source_date: null
author: null
captured_at: 2026-09-01
last_source_check: 2026-09-01
raw_path: research/raw/2026-09-01/openrouter-glm-5-3/
previous_captures: []
static: false
tags: [openrouter, glm, z-ai, open-weights, pricing, serving, providers]
---

OpenRouter's model page for `z-ai/glm-5.3`, captured 2026-09-01. The page is a **rolling dashboard**: provider prices, discounts, latency, throughput, uptime, per-provider benchmark scores, and the top-apps list all change daily. Treat every number below as a 2026-09-01 snapshot. The page's "Released" date and the API record's `created` field are the stable facts. The author uses this model as part of the current working set (see [[research/references/open-weights-landscape-2026]]).

## OpenRouter API record (`/api/v1/models`, fetched 2026-09-01; saved as `api.json` in the raw capture)

| field | value |
|---|---|
| id | `z-ai/glm-5.3` |
| canonical_slug | `z-ai/glm-5.3-20260816` |
| name | Z.ai: GLM 5.3 |
| created | 2026-08-18 (epoch 1787086655) |
| hugging_face_id | `zai-org/GLM-5.3` |
| modality | `text->text` (in: text; out: text) |
| tokenizer | Other |
| context_length | 1,310,720 |
| top_provider.context_length | 1,048,576 |
| top_provider.max_completion_tokens | 131,072 |
| pricing.prompt (per MTok) | $1.4 |
| pricing.completion (per MTok) | $4.4 |
| pricing.input_cache_read (per MTok) | $0.26 |
| pricing.input_cache_write (per MTok) | — |
| is_moderated | False |
| supported_parameters | `frequency_penalty`, `include_reasoning`, `logit_bias`, `logprobs`, `max_tokens`, `min_p`, `parallel_tool_calls`, `presence_penalty`, `reasoning`, `reasoning_effort`, `repetition_penalty`, `response_format`, `seed`, `stop`, `structured_outputs`, `temperature`, `tool_choice`, `tools`, `top_k`, `top_logprobs`, `top_p` |

OpenRouter's description field: GLM-5.3 is a large-scale reasoning model from Z.ai, built for complex software engineering and long-horizon agent tasks. It supports text input and output with a 1M-token context window, and improves...


## Page content as captured (`web-to-markdown`, 2026-09-01)

> Layout note: in the provider table, a cell such as `$1.30$1.17` is a struck-through list price followed by the discounted price; the discount badge (e.g. `10% off`) is glued to the provider name. Favicon images were stripped.

# Z.ai: GLM 5.3

### [z-ai](<https://openrouter.ai/z-ai>)/glm-5.3

[Model weights](<https://huggingface.co/zai-org/GLM-5.3>)

[Compare](<https://openrouter.ai/compare/z-ai/glm-5.3>)PlaygroundTry this model

GLM-5.3 is a large-scale reasoning model from Z.ai, built for complex software engineering and long-horizon agent tasks. It supports text input and output with a 1M-token context window, and improves on GLM-5.2 in coding and in the balance between performance and token efficiency.

Reasoning is always on and cannot be disabled. Reasoning efforts `low`, `high`, and `max` are supported; `max` is the default.

Modalities

In / Out Price

10% off

$1.17 / $3.96per 1M

Context

1M

Released

Aug 18, 2026

Z.ai: GLM 5.3

[Compare](<https://openrouter.ai/compare/z-ai/glm-5.3>)PlaygroundTry this model

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

Provider| Input /M| Output /M| Cache read /M| Latency| Throughput| Uptime  
---|---|---|---|---|---|---  
AkashML10% off| $1.30$1.17| $4.40$3.96| $0.26$0.234| 4.62s| 16 tps| 93.46%  
io.net5% off| $1.25$1.188| $4.40$4.18| $0.26$0.247| 1.92s| 35 tps| 98.98%  
DeepInfra| $1.20| $4.00| $0.12| 2.25s| 41 tps| 95.09%  
Morph| $1.25| $4.40| $0.26| 1.65s| 74 tps| 94.52%  
Friendli10% off| $1.40$1.26| $4.40$3.96| $0.26$0.234| 0.73s| 134 tps| 99.99%  
Cloudflare| $1.40| $4.40| $0.26| 3.70s| 37 tps| 99.38%  
Fireworks| $1.40| $4.40| $0.26| 1.38s| 59 tps| 99.78%  
Baseten| $1.40| $4.40| $0.14| 1.25s| 69 tps| 99.94%  
GMICloud| $1.40| $4.40| $0.26| 2.63s| 50 tps| 97.41%  
Modal| $1.40| $4.40| $0.26| 0.88s| 83 tps| 99.58%  
Parasail| $1.40| $4.40| $0.26| 1.12s| 86 tps| 98.73%  
NovitaAI| $1.40| $4.40| $0.26| 2.04s| 46 tps| 99.70%  
DigitalOcean| $1.40| $4.40| $0.26| 1.25s| 50 tps| 99.53%  
Together| $1.40| $4.40| $0.26| 0.53s| 107 tps| 95.04%  
Phala| $1.40| $4.40| $0.26| 1.65s| 60 tps| 99.60%  
SiliconFlow| $1.40| $4.40| $0.26| 2.42s| 48 tps| 99.71%  
Reka AI| $1.40| $4.40| $0.26| 1.06s| 90 tps| 98.40%  
Decart| $1.40| $4.40| $0.23| 1.27s| 110 tps| 97.70%  
Inceptron| $1.40| $4.40| $0.26| 0.58s| 77 tps| 100.00%  
Z.ai| $1.40| $4.40| $0.26| 3.02s| 45 tps| 99.94%  
Venice| $1.75| $5.50| $0.325| 1.87s| 62 tps| 97.42%  
Wafer| $1.40| $4.40| $0.26| 2.04s| 66 tps| 99.30%  
  
Throughput

134tok/s

P50, best across providers

Latency

0.53s

P50, best provider

All locations

Latency / throughputP501 week

AutoExacto Benchmarks

GPQA DiamondTAU-Bench

DigitalOcean

90.6%79.3%

Phala

91.3%73.3%

AtlasCloud

86.5%78.0%

auto-routing

84.2%80.0%

Fireworks

83.5%79.4%

+17 more providers

Uptime (3d)

100.00%

Availability (3d)

99.96%

### Availability over the last 3 days

Last 72 hours

Availability 99.96%

3 Days Ago2 Days AgoYesterdayNow

### Availability over the last 24 hours

OpenRouter Availability

99.91%

Without Routing

97.01%

When an error occurs in an upstream provider, we can recover by routing to another healthy provider, if your request filters allow it. You can access per-provider uptime data programmatically through the [Endpoints API](<https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints>). [Learn more](<https://openrouter.ai/docs/provider-routing>) about our load balancing and customization options.

1.

[Hermes Agent ](<https://openrouter.ai/apps/hermes-agent>)

Hermes Agent is an open-source, self-improving AI agent by Nous Research that runs persistently with memory across sessions, and builds reusable skills from experience. It comes with 40+ built-in tools, including web search, browser automation, and vision, plus scheduled automations and subagents.

260Btokens

2.

[Claude Code ](<https://openrouter.ai/apps/claude-code>)

Claude Code is Anthropic's agentic coding tool that reads your entire codebase, plans and executes changes across files, runs tests, and iterates on failures, all from natural language prompts.

180Btokens

3.

[omp ](<https://openrouter.ai/apps/url/https%3A%2F%2Fomp.sh%2F>)

new

106Btokens

4.

[pi ](<https://openrouter.ai/apps/pi>)

There are many coding agents, but this one is yours.

100Btokens

5.

[Strix ](<https://openrouter.ai/apps/url/https%3A%2F%2Fstrix.ai%2F>)

new

75.7Btokens

Filter quantization

## Frequently asked questions

### What is GLM 5.3?

GLM-5.3 is a large-scale reasoning model from Z.ai, built for complex software engineering and long-horizon agent tasks. It supports text input and output with a 1M-token context window, and improves on GLM-5.2 in coding and in the balance between performance and token efficiency. Reasoning is always on and cannot be disabled. Reasoning efforts low, high, and max are supported; max is the default.

### How much does GLM 5.3 cost?

GLM 5.3 costs $1.17/M input tokens and $3.96/M output tokens, with separate rates for Cache Read at $0.234/M tokens.

### What is the context length of GLM 5.3?

GLM 5.3 has a 1,310,720 token context window. It supports up to 1,048,576 completion tokens.

### Does GLM 5.3 support tool calling and structured outputs?

Yes. GLM 5.3 accepts `tools` and `tool_choice` for function calling. It also supports structured outputs via a JSON schema in `response_format`.

### Which providers serve GLM 5.3?

GLM 5.3 is served by 22 providers on OpenRouter: AkashML, io.net, DeepInfra, Morph, Friendli, Cloudflare, Fireworks, Baseten and 14 more. Requests are routed to the best available provider, with automatic failover to the others, and you can pin or exclude providers with [provider routing](<https://openrouter.ai/docs/features/provider-routing>).

### When was GLM 5.3 released?

GLM 5.3 was released on August 18, 2026.

## Capture gaps

- Charts (pricing history, latency/throughput, uptime, activity) are rendered client-side and were not captured; only their headline figures survive in the text.
- Per-provider benchmark rows list only the first few providers ("+N more providers" collapsed on the page).
- The "Quick Start" code sample and "Explore more models" links were not captured.
- Rolling page: `static: false`, so `refresh-research-sources` re-checks it. Compare prices against the API record's `created` date and the page's "Released" date, which do not change.
