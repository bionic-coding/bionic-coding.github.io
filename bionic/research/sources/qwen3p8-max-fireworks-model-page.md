---
title: "Fireworks qwen3p8-max model page (serves the Qwen3.8-2.4T-A95B listing)"
slug: qwen3p8-max-fireworks-model-page
type: source
source_url: https://fireworks.ai/models/fireworks/qwen3p8-max
source_date: null
author: "Fireworks AI"
captured_at: 2026-08-15
last_source_check: 2026-08-15
raw_path: research/raw/2026-08-15/qwen3p8-max-fireworks-model-page/
previous_captures: []
static: false
tags: [qwen, fireworks, pricing, api, serving-limits]
---

**Capture anomaly, stated up front:** this is what the server returns at `https://fireworks.ai/models/fireworks/qwen3p8-max` as of 2026-08-15 — the **Qwen3.8-2.4T-A95B** listing, not a separate "Qwen3.8 Max" hosted-preview listing. HTTP 200, no redirect (`x-matched-path: /models/fireworks/qwen3p8-max`); the canonical and og:url meta tags point at the qwen3p8-max URL while the page title is "Qwen3.8-2.4T-A95B API & Playground | Fireworks AI"; the page's CMS payload ties `_id: "qwen3p8-max"` to `modelName: "Qwen3.8-2.4T-A95B"`; the displayed model path is `accounts/fireworks/models/qwen3p8-2p4t-a95b`. The "max" URL appears to have been repointed at the open-weights release.

# Qwen3.8-2.4T-A95B

Status: **Ready** · model path: `accounts/fireworks/models/qwen3p8-2p4t-a95b`

Qwen3.8-2.4T-A95B is Alibaba's most capable Qwen model to date, a 2.4T-parameter sparse MoE with ~95B active parameters. It is built for autonomous, long-horizon work: multi-day coding runs, research-paper reproduction and self-improvement.

## API Features

- **Serverless** — supported, pay per token. "There are several ways to call the Fireworks API, including Fireworks' Python client, the REST API, or OpenAI's Python client."
- **On-demand deployment** — supported. "On-demand deployments allow you to use Qwen3.8-2.4T-A95B on dedicated GPUs with Fireworks' high-performance serving stack with high reliability and no rate limits."

## Pricing (serverless)

**$2.00 / $0.25 / $6.00 per 1M tokens (input / cached input / output).**

## Metadata

| field | value |
|---|---|
| State | Ready |
| Created on | 8/12/2026 |
| Kind | Base model |
| Provider | Qwen |
| Hugging Face | Qwen/Qwen3.8-2.4T-A95B |

## Specification

| field | value |
|---|---|
| Calibrated | No |
| Mixture-of-Experts | Yes |
| Parameters | 2.41T |

## Supported Functionality

| field | value |
|---|---|
| Fine-tuning | Not supported |
| Serverless | Supported |
| Context Length | 262k tokens |
| Function Calling | Supported |
| Embeddings | Not supported |
| Rerankers | Not supported |
| Support image input | Not supported |

Site-wide banner at capture time: "DeepSeek-V4-Pro-0813 available now on Fireworks".

## Capture gaps

- **The URL/content mismatch is the finding.** The owner supplied this URL as "Qwen3.8 Max hosted on Fireworks"; the page served is the open-weights model's listing (created 8/12/2026 — after the Qwen3.8-Max API launch of 2 August, before the weights release). Whether Fireworks ever ran a distinct `qwen3p8-max` serverless listing with its own specs is not answerable from this capture; only the current state is recorded.
- **This is a serving fact sheet.** Pricing, context, and spec fields are the authoritative content; the description paragraph is marketing copy (the "multi-day coding runs, research-paper reproduction and self-improvement" line traces to Alibaba's launch-post showcases, claimed not verified). **No benchmarks, no license text.**
- **Context Length 262k** is the open model's native window ([[research/sources/qwen3-8-2-4t-a95b-open-weights-release]]); the QwenCloud API's 1M context is not on offer here. Pricing matches QwenCloud's $2/$6 and $0.25 implicit-cache figures exactly ([[research/sources/qwen3-8-max-qwencloud-model-page]]).
- Fine-tuning is **not** supported for this listing (it is for DeepSeek-V4-Pro-0813 on the same platform).
- Fireworks navigation/footer chrome stripped. Pricing carries no currency label on the page; figures are USD per 1M tokens.
