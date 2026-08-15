---
title: "DeepSeek-V4-Pro-0813 — Fireworks model page"
slug: deepseek-v4-pro-0813-fireworks-model-page
type: source
source_url: https://fireworks.ai/models/deepseek-ai/deepseek-v4-pro-0813
source_date: null
author: "Fireworks AI"
captured_at: 2026-08-15
last_source_check: 2026-08-15
raw_path: research/raw/2026-08-15/deepseek-v4-pro-0813-fireworks-model-page/
previous_captures: []
static: false
tags: [deepseek, fireworks, pricing, api, serving-limits]
---

# DeepSeek-V4-Pro-0813

Status: **Ready** · model path: `accounts/fireworks/models/deepseek-v4-pro-0813`

DeepSeek-V4-Pro-0813 is the official release of DeepSeek-V4-Pro, superseding the preview version, with greatly enhanced agentic capabilities and performance improvements that are especially pronounced in production environments. It is built on the DeepSeek-V4-Pro (Preview) model structure, with a DSpark speculative decoding module attached.

## API Features

- **Fine-tuning** — supported. "DeepSeek-V4-Pro-0813 can be customized with your data to improve responses. Fireworks uses LoRA to efficiently train and deploy your personalized model."
- **Serverless** — supported, pay per token. "There are several ways to call the Fireworks API, including Fireworks' Python client, the REST API, or OpenAI's Python client."
- **On-demand deployment** — supported. "On-demand deployments allow you to use DeepSeek-V4-Pro-0813 on dedicated GPUs with Fireworks' high-performance serving stack with high reliability and no rate limits."

## Pricing (serverless)

**$1.32 / $0.044 / $3.96 per 1M tokens (input / cached input / output).**

## Metadata

| field | value |
|---|---|
| State | Ready |
| Created on | 8/13/2026 |
| Kind | Base model |
| Provider | Deepseek |
| Hugging Face | deepseek-ai/DeepSeek-V4-Pro-0813 |

## Specification

| field | value |
|---|---|
| Calibrated | No |
| Mixture-of-Experts | Yes |
| Parameters | 1.6T |

## Supported Functionality

| field | value |
|---|---|
| Fine-tuning | Supported |
| Serverless | Supported |
| Context Length | 1040k tokens |
| Function Calling | Supported |
| Embeddings | Not supported |
| Rerankers | Not supported |
| Support image input | Not supported |

Site-wide banner at capture time: "DeepSeek-V4-Pro-0813 available now on Fireworks".

## Capture gaps

- **This is a serving fact sheet, not a model card.** Pricing, context, and the spec fields are the page's authoritative content; the description paragraph is DeepSeek's model-card text repeated verbatim, and there are **no benchmarks, no license text, and no active-parameter count**.
- **Parameters reads 1.6T here vs 1.7T on the HF model card** ([[research/sources/deepseek-v4-pro-0813-model-card]]). Both are vendor/host spec fields; neither explains the difference. Treat the true figure as unresolved pending the technical report.
- **Context Length 1040k** is the first explicit context figure captured for V4-Pro; it corroborates the paper title's "Million-Token Context" claim. Source is the host's spec field, not DeepSeek.
- "Created on 8/13/2026" is the platform listing date; it matches the "-0813" release suffix and is the basis for the model card's inferred `source_date`.
- Fireworks navigation/footer chrome stripped. Pricing carries no currency label on the page; figures are USD per 1M tokens.
