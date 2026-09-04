---
title: "GPT-6 Astra — OpenAI API model page"
slug: gpt-6-astra-model-page
type: source
source_url: https://developers.openai.com/api/docs/models/gpt-6-astra
source_date: null
author: "OpenAI"
captured_at: 2026-09-03
last_source_check: 2026-09-03
raw_path: research/raw/2026-09-03/gpt-6-astra-model-page/
previous_captures: []
static: false
tags: [openai, gpt-6, astra, pricing, api, context-window, rate-limits]
---

# GPT-6 Astra — OpenAI API model page

_Captured 2026-09-03 with `web-to-markdown` (page title "GPT-6 Astra Model | OpenAI API"). A rolling reference page: pricing, limits, and availability change in place, so `static: false`. The only image on the page is the model's logo tile, saved in raw as `gpt-6-astra-62cb0f7d.png` and not referenced below._

**GPT-6 Astra** — Default

Our most capable model, built for the hardest end-to-end work

GPT‑6 Astra is rolling out today for enterprises in our [Trusted Access Program](https://openai.com/form/enterprise-trusted-access-for-cyber/), with access through API and our Plus, Pro, Business and Enterprise plans coming in the coming days.

| Reasoning | Speed | Price | Input | Output |
|---|---|---|---|---|
| Highest | Fast | $10 • $50 (Input • Output) | Text, image | Text |

GPT-6 Astra is our most capable model, built for the hardest end-to-end work. Use it for complex reasoning, coding, computer use, research, and document creation. `reasoning.effort` supports `low`, `medium`, `high`, `xhigh`, and `max`.

Get started with GPT-6 Astra using the [model guide](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra).

- 1,050,000 context window
- 128,000 max output tokens
- Apr 30, 2026 knowledge cutoff
- Reasoning token support

## Pricing

Pricing is based on the number of tokens used, or other metrics based on the model type. For tool-specific models, like search and computer use, there's a fee per tool call. See details in the [pricing page](https://developers.openai.com/api/docs/pricing).

Text tokens, per 1M tokens:

| Input | Cached input | Cache writes | Output |
|---|---|---|---|
| $10.00 | $1.00 | $12.50 | $50.00 |

Prompts with more than 272K input tokens are priced at 2x input and cache rates and 1.5x output for the full request.

Cache writes are billed at 1.25x the uncached input token rate.

Batch and Flex are priced at 50% of Standard rates. Fast mode is priced at 2x the applicable rates.

## Modalities

| Modality | Support |
|---|---|
| Text | Input and output |
| Image | Input only |
| Audio | Not supported |
| Video | Not supported |

## Endpoints

The page lists every API endpoint with a supported / not-supported marker. The marker is rendered as an icon and did not survive text extraction; the three endpoints the page's own summary and the announcement name as supported are **Chat Completions** (`v1/chat/completions`), **Responses** (`v1/responses`), and **Batch** (`v1/batch`). The full endpoint roster on the page: Chat Completions, Responses, Realtime, Realtime translation, Realtime transcription, Assistants, Batch, Fine-tuning, Embeddings, Image generation, Videos, Image edit, Speech generation, Transcription, Translation, Moderation, Completions (legacy).

## Features

| Feature | Support |
|---|---|
| Streaming | Supported |
| Function calling | Supported |
| Structured outputs | Supported |
| Fine-tuning | Not supported |

## Tools

Tools supported by this model when using the Responses API.

| Tool | Support |
|---|---|
| Web search | Supported |
| File search | Supported |
| Image generation | Supported |
| Code interpreter | Supported |
| Hosted shell | Supported |
| Apply patch | Supported |
| Skills | Supported |
| Computer use | Supported |
| MCP | Supported |
| Tool search | Supported |

## Snapshots

Snapshots let you lock in a specific version of the model so that performance and behavior remain consistent. Below is a list of all available snapshots and aliases for GPT-6 Astra.

- `gpt-6-astra` → `gpt-6-astra` (the alias and the snapshot share one name; no dated snapshot is listed)

## Rate limits

Rate limits ensure fair and reliable access to the API by placing specific caps on requests, tokens, audio duration, or other usage within a given time period. Your usage tier determines how high these limits are set and automatically increases as you send more requests and spend more on the API.

| Tier | RPM | TPM | Batch queue limit |
|---|---|---|---|
| Free | Not supported | | |
| Tier 1 | 500 | 500,000 | 1,500,000 |
| Tier 2 | 5,000 | 1,000,000 | 3,000,000 |
| Tier 3 | 5,000 | 2,000,000 | 100,000,000 |
| Tier 4 | 10,000 | 4,000,000 | 200,000,000 |
| Tier 5 | 15,000 | 40,000,000 | 15,000,000,000 |

## Capture gaps

- The endpoint support markers are icons; only the roster of endpoint names was captured. The three confirmed-supported endpoints above are taken from the page's summary strip and the launch announcement ([[research/sources/gpt-6-astra-announcement]]).
- The "Compare" and "Try in Playground" controls and the model guide link target were not captured.
