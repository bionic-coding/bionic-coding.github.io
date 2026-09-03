---
title: "OpenRouter model page — Z.ai: GLM 5.3 Flash"
slug: openrouter-glm-5-3-flash
type: source
source_url: https://openrouter.ai/z-ai/glm-5.3-flash
source_date: null
author: null
captured_at: 2026-09-01
last_source_check: 2026-09-01
raw_path: research/raw/2026-09-01/openrouter-glm-5-3-flash/
previous_captures: []
static: false
tags: [openrouter, glm, z-ai, open-weights, pricing, serving, providers, multimodal]
---

OpenRouter's model page for `z-ai/glm-5.3-flash`, captured 2026-09-01. The page is a **rolling dashboard**: provider prices, discounts, latency, throughput, uptime, per-provider benchmark scores, and the top-apps list all change daily. Treat every number below as a 2026-09-01 snapshot. The page's "Released" date and the API record's `created` field are the stable facts. The author uses this model as part of the current working set (see [[research/references/open-weights-landscape-2026]]).

## OpenRouter API record (`/api/v1/models`, fetched 2026-09-01; saved as `api.json` in the raw capture)

| field | value |
|---|---|
| id | `z-ai/glm-5.3-flash` |
| canonical_slug | `z-ai/glm-5.3-flash-20260826` |
| name | Z.ai: GLM 5.3 Flash |
| created | 2026-08-26 (epoch 1787752741) |
| hugging_face_id | `zai-org/GLM-5.3-Flash` |
| modality | `text+image+video->text` (in: text, image, video; out: text) |
| tokenizer | Other |
| context_length | 1,310,720 |
| top_provider.context_length | 1,048,576 |
| top_provider.max_completion_tokens | 131,072 |
| pricing.prompt (per MTok) | $0.075 |
| pricing.completion (per MTok) | $0.25 |
| pricing.input_cache_read (per MTok) | $0.015 |
| pricing.input_cache_write (per MTok) | — |
| is_moderated | False |
| supported_parameters | `frequency_penalty`, `include_reasoning`, `logit_bias`, `logprobs`, `max_tokens`, `min_p`, `presence_penalty`, `reasoning`, `reasoning_effort`, `repetition_penalty`, `response_format`, `seed`, `stop`, `structured_outputs`, `temperature`, `tool_choice`, `tools`, `top_k`, `top_logprobs`, `top_p` |

OpenRouter's description field: GLM-5.3-Flash is a native multimodal model from Z.ai. It is suited for efficient coding and long-horizon agent tasks. Its hybrid sparse and linear attention architecture maintains accurate long-context behavior while...


## Page content as captured (`web-to-markdown`, 2026-09-01)

> Layout note: in the provider table, a cell such as `$1.30$1.17` is a struck-through list price followed by the discounted price; the discount badge (e.g. `10% off`) is glued to the provider name. Favicon images were stripped.

Limited-time 50% discount via ZAI through September 9, 2026 at 16:00 UTC.

# Z.ai: GLM 5.3 Flash

### [z-ai](<https://openrouter.ai/z-ai>)/glm-5.3-flash

[Model weights](<https://huggingface.co/zai-org/GLM-5.3-Flash>)

[Compare](<https://openrouter.ai/compare/z-ai/glm-5.3-flash>)PlaygroundTry this model

GLM-5.3-Flash is a native multimodal model from Z.ai. It is suited for efficient coding and long-horizon agent tasks. Its hybrid sparse and linear attention architecture maintains accurate long-context behavior while reducing compute overhead.

Modalities

In / Out Price

50% off

$0.075 / $0.25per 1M

Context

1M

Released

Aug 26, 2026

Z.ai: GLM 5.3 Flash

[Compare](<https://openrouter.ai/compare/z-ai/glm-5.3-flash>)PlaygroundTry this model

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

[AI Models with Vision: Multimodal LLMs for Image UnderstandingCollection](<https://openrouter.ai/collections/vision-models>)[AI Model RankingsRanking](<https://openrouter.ai/rankings>)

Standard

Latency / throughputP50

Provider| Input /M| Output /M| Cache read /M| Latency| Throughput| Uptime  
---|---|---|---|---|---|---  
Z.ai50% off| $0.15$0.075| $0.50$0.25| $0.03$0.015| 3.04s| 26 tps| 97.97%  
NovitaAI50% off| $0.15$0.075| $0.50$0.25| $0.03$0.015| 2.45s| 29 tps| 99.21%  
DeepInfra50% off| $0.15$0.075| $0.50$0.25| $0.03$0.015| 1.46s| 24 tps| 99.14%  
GMICloud50% off| $0.15$0.075| $0.50$0.25| $0.03$0.015| 2.55s| 23 tps| 94.00%  
Makora| $0.14| $0.47| $0.024| 0.71s| 79 tps| 97.68%  
Modal67% off| $0.45$0.15| $1.50$0.50| $0.09$0.03| 0.52s| 45 tps| 99.91%  
Morph| $0.15| $0.42| $0.01| 1.09s| 47 tps| 94.70%  
Parasail| $0.15| $0.50| $0.03| 1.52s| 20 tps| 97.35%  
Reka AI| $0.15| $0.50| $0.03| 1.63s| 28 tps| 99.12%  
Together| $0.15| $0.50| $0.03| 1.16s| 34 tps| 96.07%  
Wafer| $0.15| $0.50| $0.03| 1.96s| 49 tps| 95.93%  
DigitalOcean| $0.15| $0.50| $0.03| 1.79s| 35 tps| 98.14%  
SiliconFlow| $0.15| $0.50| $0.03| 9.29s| 20 tps| 99.14%  
Friendli| $0.15| $0.50| $0.03| 4.35s| 49 tps| 97.94%  
Phala| $0.15| $0.50| $0.03| 1.47s| 16 tps| 95.73%  
Fireworks| $0.15| $0.50| $0.03| 0.86s| 15 tps| 99.53%  
NextBit| $0.15| $0.50| $0.03| 1.98s| 25 tps| 96.74%  
StreamLake| $0.15| $0.50| $0.03| 1.13s| 30 tps| 98.15%  
Cloudflare| $0.15| $0.50| $0.03| 1.48s| 39 tps| 99.74%  
io.net| $0.15| $0.50| $0.03| 1.17s| 16 tps| 94.10%  
Baseten| $0.15| $0.50| $0.03| 0.98s| 110 tps| 99.82%  
Venice| $0.15| $0.50| $0.03| 1.94s| 21 tps| 74.51%  
  
Throughput

110tok/s

P50, best across providers

Latency

0.52s

P50, best provider

All locations

Latency / throughputP501 week

AutoExacto Benchmarks

GPQA DiamondTAU-Bench

Phala

90.8%\--

Baseten

84.2%\--

Wafer

88.3%80.0%

Venice

88.9%74.2%

Reka AI

88.0%75.0%

+15 more providers

Uptime (3d)

100.00%

Availability (3d)

99.89%

### Availability over the last 3 days

Last 72 hours

Availability 99.89%

3 Days Ago2 Days AgoYesterdayNow

### Availability over the last 24 hours

OpenRouter Availability

99.88%

Without Routing

89.97%

When an error occurs in an upstream provider, we can recover by routing to another healthy provider, if your request filters allow it. You can access per-provider uptime data programmatically through the [Endpoints API](<https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints>). [Learn more](<https://openrouter.ai/docs/provider-routing>) about our load balancing and customization options.

1.

[Hermes Agent ](<https://openrouter.ai/apps/hermes-agent>)

Hermes Agent is an open-source, self-improving AI agent by Nous Research that runs persistently with memory across sessions, and builds reusable skills from experience. It comes with 40+ built-in tools, including web search, browser automation, and vision, plus scheduled automations and subagents.

1.38Ttokens

2.

[Claude Code ](<https://openrouter.ai/apps/claude-code>)

Claude Code is Anthropic's agentic coding tool that reads your entire codebase, plans and executes changes across files, runs tests, and iterates on failures, all from natural language prompts.

976Btokens

3.

[Cline ](<https://openrouter.ai/apps/cline>)

Cline is an open-source AI coding agent that lives inside your IDE, autonomously exploring your codebase, editing files, running terminal commands, and using browser automation.

700Btokens

4.

[omp ](<https://openrouter.ai/apps/url/https%3A%2F%2Fomp.sh%2F>)

new

401Btokens

5.

[DeepSeek Harness ](<https://openrouter.ai/apps/url/https%3A%2F%2Fgithub.com%2Fdeepseek-ai%2Fdeepseek-harness>)

new

256Btokens

Filter quantization

## Frequently asked questions

### Was ZAI GLM-5.3 Flash the stealth model Ox Alpha?

Yes, the stealth model Ox Alpha was revealed to be ZAI's new model, GLM-5.3 Flash.

### What is GLM 5.3 Flash?

GLM-5.3-Flash is a native multimodal model from Z.ai. It is suited for efficient coding and long-horizon agent tasks. Its hybrid sparse and linear attention architecture maintains accurate long-context behavior while reducing compute overhead.

### How much does GLM 5.3 Flash cost?

GLM 5.3 Flash costs $0.075/M input tokens and $0.25/M output tokens, with separate rates for Cache Read at $0.015/M tokens.

### What is the context length of GLM 5.3 Flash?

GLM 5.3 Flash has a 1,310,720 token context window. It supports up to 131,072 completion tokens.

### Does GLM 5.3 Flash support tool calling and structured outputs?

Yes. GLM 5.3 Flash accepts `tools` and `tool_choice` for function calling. It supports `response_format` for JSON output, without JSON-schema enforcement.

### What inputs and outputs does GLM 5.3 Flash support?

GLM 5.3 Flash accepts text, images and video as input and returns text.

### Which providers serve GLM 5.3 Flash?

GLM 5.3 Flash is served by 22 providers on OpenRouter: Z.ai, NovitaAI, DeepInfra, GMICloud, Makora, Modal, Morph, Parasail and 14 more. Requests are routed to the best available provider, with automatic failover to the others, and you can pin or exclude providers with [provider routing](<https://openrouter.ai/docs/features/provider-routing>).

### When was GLM 5.3 Flash released?

GLM 5.3 Flash was released on August 26, 2026.

## Capture gaps

- Charts (pricing history, latency/throughput, uptime, activity) are rendered client-side and were not captured; only their headline figures survive in the text.
- Per-provider benchmark rows list only the first few providers ("+N more providers" collapsed on the page).
- The "Quick Start" code sample and "Explore more models" links were not captured.
- Rolling page: `static: false`, so `refresh-research-sources` re-checks it. Compare prices against the API record's `created` date and the page's "Released" date, which do not change.
