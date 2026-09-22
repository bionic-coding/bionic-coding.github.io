---
title: "GPT-6 Sol Model | OpenAI API"
slug: gpt-6-sol
type: source
source_url: https://developers.openai.com/api/docs/models/gpt-6-sol
source_date: null
author: null
captured_at: 2026-09-22
last_source_check: 2026-09-22
raw_path: research/raw/2026-09-22/gpt-6-sol/
previous_captures: []
static: false
tags: [openai, gpt-6, model-page, vendor-docs]
---

# GPT-6 Sol

> Captured via the page's clean `.md` export (`https://developers.openai.com/api/docs/models/gpt-6-sol.md`), which OpenAI serves by appending `.md` to any doc URL. A rendered-HTML capture of the same page was also taken (`source.html`, `gpt-6-sol-*.png`) but the `.md` export is the body of this page — it drops the site's nav chrome that the HTML capture keeps.

> Built to power complex coding and agentic workflows.

Model ID: `gpt-6-sol`

GPT-6 Sol is built for complex coding and agentic workflows.

`reasoning.effort` supports `none`, `low`, `medium` (default), `high`, `xhigh`, and `max`.
Use the Responses API for built-in tools and function calling. Chat Completions supports function calling only with `reasoning_effort` set to `none`.

EU data residency is available only with Standard processing.
See [data residency eligibility](https://developers.openai.com/api/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency).

## Model details

- Default snapshot: `gpt-6-sol`
- Input modalities: text, image
- Output modalities: text
- 1,050,000 context window
- Maximum input tokens: 922,000
- 128,000 max output tokens
- Apr 20, 2026 knowledge cutoff
- Reasoning token support

## Pricing

Pricing is based on the number of tokens used, or other metrics based on the model type. For tool-specific models, like search and computer use, there's a fee per tool call. See details in the [pricing page](https://developers.openai.com/api/docs/pricing).

### Text tokens

| Metric | Price | Unit |
| --- | ---: | --- |
| Input | $2 | 1M tokens |
| Cached input | $0.2 | 1M tokens |
| Cache writes | $2.5 | 1M tokens |
| Output | $10 | 1M tokens |

- Cached input tokens are priced at 10% of the uncached input token rate.
- Cache writes are billed at 1.25x the uncached input token rate.
- Prompts with more than 272K input tokens are priced at 2x input and cache rates and 1.5x output for the full request.
- Regional processing adds a 10% premium where available. EU data residency is available only with Standard processing.
- Batch and Flex are priced at 50% of Standard rates. Fast mode is priced at 2x the applicable rates.

## Endpoints

| Endpoint | Route | Support |
| --- | --- | --- |
| Live | `v1/live/sessions` | Not supported |
| Chat Completions | `v1/chat/completions` | Supported |
| Responses | `v1/responses` | Supported |
| Realtime | `v1/realtime` | Not supported |
| Realtime translation | `v1/realtime/translations` | Not supported |
| Realtime transcription | `v1/realtime/transcription_sessions` | Not supported |
| Assistants | `v1/assistants` | Not supported |
| Batch | `v1/batch` | Supported |
| Fine-tuning | `v1/fine-tuning` | Not supported |
| Embeddings | `v1/embeddings` | Not supported |
| Image generation | `v1/images/generations` | Not supported |
| Videos | `v1/videos` | Not supported |
| Image edit | `v1/images/edits` | Not supported |
| Speech generation | `v1/audio/speech` | Not supported |
| Transcription | `v1/audio/transcriptions` | Not supported |
| Translation | `v1/audio/translations` | Not supported |
| Moderation | `v1/moderations` | Not supported |
| Completions (legacy) | `v1/completions` | Not supported |

## Supported features

- streaming
- structured_outputs
- function_calling
- file_search
- image_input
- web_search
- prompt_caching

## Supported tools

Tools supported by this model when using the Responses API.

- web_search
- file_search
- image_generation
- code_interpreter
- hosted_shell
- apply_patch
- skills
- computer_use
- mcp
- tool_search

## Snapshots

Use `gpt-6-sol` in your API requests.

- `gpt-6-sol`

## Rate limits

Rate limits ensure fair and reliable access to the API by placing specific caps on requests, tokens, audio duration, or other usage within a given time period. Your usage tier determines how high these limits are set and automatically increases as you send more requests and spend more on the API.

### Standard

| Tier | RPM | TPM | Batch queue limit |
| --- | ---: | ---: | ---: |
| Tier 1 | 500 | 500,000 | 1,500,000 |
| Tier 2 | 5,000 | 1,000,000 | 3,000,000 |
| Tier 3 | 5,000 | 2,000,000 | 100,000,000 |
| Tier 4 | 10,000 | 4,000,000 | 200,000,000 |
| Tier 5 | 15,000 | 40,000,000 | 15,000,000,000 |

## Capture gaps

- No benchmark figures appear on this doc page — the model page never carries benchmarks; comparative numbers, if any, live in an announcement post or system card, neither of which is linked from this page and neither was located during this capture.
- No release-date or announcement-post link appears on this page. The page is `static: false` (doc pages change) and carries no dated snapshot notice, unlike GPT-6 Astra's launch post treatment on 2026-09-03.
