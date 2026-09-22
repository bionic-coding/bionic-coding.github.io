---
title: "Xiaomi: MiMo-V2.6-Pro (OpenRouter)"
slug: openrouter-mimo-v2-6-pro
type: source
source_url: https://openrouter.ai/xiaomi/mimo-v2.6-pro
source_date: 2026-09-21
author: OpenRouter
captured_at: 2026-09-22
last_source_check: 2026-09-22
raw_path: research/raw/2026-09-22/openrouter-mimo-v2-6-pro/
previous_captures: []
static: false
tags: [mimo, xiaomi, openrouter, open-weights, benchmarks, serving, artificial-analysis, pricing]
---

# Xiaomi: MiMo-V2.6-Pro (OpenRouter)

> **Capture note.** `https://openrouter.ai/xiaomi/mimo-v2.6-pro` is JS-rendered — a plain fetch returns an empty shell. `source.html` in this page's `raw_path` is a **headless-Chrome DOM render**, not a raw HTTP response. The companion file `models-api.json` is OpenRouter's `/api/v1/models` endpoint response (fetched the same day), carrying the three MiMo-V2.6 variant records (Pro, Flash, Pro-UltraSpeed) as structured data corroborating the rendered page. This page is an **OpenRouter serving/listing page** — third-party to Xiaomi, but not independent benchmarking; the Artificial Analysis figures below are AA's own measurement, surfaced through OpenRouter's model page, and are the first non-Xiaomi-authored numbers on MiMo-V2.6.

**Released Sep 21, 2026** (per the page's model-detail panel; one day before Xiaomi's own launch article, captured in [[research/sources/mimo-v2-6]]).

## Model descriptions (verbatim from `models-api.json`; each is genuinely truncated at "..." by OpenRouter's own API — not an artifact of this capture)

- **MiMo-V2.6-Pro:** "MiMo-V2.6-Pro is the flagship foundation model developed by Xiaomi. Built at a scale of over 1T parameters, it is designed to push the ceiling of capability for the most demanding..."
- **MiMo-V2.6-Flash:** "MiMo-V2.6-Flash is an open-source foundation model developed by Xiaomi. Built on a Mixture-of-Experts architecture with 309B total parameters and 15B activated per token, it employs a hybrid attention mechanism for..."
- **MiMo-V2.6-Pro-UltraSpeed:** "MiMo-V2.6-Pro-UltraSpeed is the fast speed edition of Xiaomi's flagship foundation model, MiMo-V2.6-Pro. Built from the same 1T MiMo-V2.6-Pro checkpoint, it matches the original model in quality while delivering roughly 10x..."

**This fills the architecture gap [[research/sources/mimo-v2-6]] flagged as a capture gap** — Xiaomi's own launch article stated no parameter counts. OpenRouter's listing states: **Pro >1T parameters** (total; not further broken down — no active-parameter count given, so Pro's MoE structure, if any, is still unstated); **Flash: MoE, 309B total / 15B active per token, hybrid attention**; **Pro-UltraSpeed: same 1T-class checkpoint as Pro, ~10× the output speed at matched quality**.

> [contradiction] **UltraSpeed's speed claim conflicts across sources.** OpenRouter's own model description says UltraSpeed delivers "roughly 10x" Pro's output speed. Xiaomi's launch article ([[research/sources/mimo-v2-6]]) claims "up to 20x faster output speed at the same quality." Same model, same vendor family, two different multipliers from two different first-party-adjacent sources (Xiaomi's own copy vs. OpenRouter's listing, which OpenRouter presumably sourced from Xiaomi or measured independently — unclear which). Not resolved here; cite the specific source when repeating either number, and do not average or split the difference.

## Artificial Analysis benchmark table (transcribed verbatim from the rendered page's benchmarks section)

| Source | Benchmark | Score |
|---|---|---|
| Artificial Analysis | MiMo-V2.6-Pro Intelligence Index | 46.3 |
| Artificial Analysis | MiMo-V2.6-Pro HLE | 49.4% |
| Artificial Analysis | MiMo-V2.6-Pro AA-LCR | 86.3% |
| Artificial Analysis | MiMo-V2.6-Pro GDPval-AA | 58.7% |
| Artificial Analysis | MiMo-V2.6-Pro CritPt | 26.6% |
| Artificial Analysis | MiMo-V2.6-Pro SciCode | 60.9% |
| Artificial Analysis | MiMo-V2.6-Pro AA-Omniscience Accuracy | 34.8% |
| Artificial Analysis | MiMo-V2.6-Pro AA-Omniscience Non-Hallucination Rate | 59.4% |

The page's headline callout: **"Better than 92% of models compared"** on the Intelligence Index (46.3), rendered as a large stat tile alongside the table.

**This is the first non-Xiaomi-sourced figure on MiMo-V2.6** captured in this wiki. Artificial Analysis's own Intelligence Index score (**46.3**) corroborates — to one decimal place — Xiaomi's own claimed figure of **46.32** in the launch article. Given AA is a named, independent third-party benchmark aggregator (already used as a citation source elsewhere in this wiki — see [[research/references/open-weights-landscape-2026]] and [[research/references/frontier-models-2026]]), this is meaningfully stronger evidence than Xiaomi's self-citation of the same index; it does not mean AA independently reproduced the *whole* benchmark suite from Xiaomi's article — only the Intelligence Index score.

## Provider table (DeepInfra + Xiaomi; pricing, latency, throughput, uptime)

| Provider | Input $/MTok | Output $/MTok | Cache read $/MTok | Latency | Throughput | Uptime |
|---|---|---|---|---|---|---|
| DeepInfra | $0.435 | $0.87 | $0.0036 | 1.00s | 24 tps | 97.83% |
| Xiaomi | $0.435 | $0.87 | $0.0036 | 3.87s | 30 tps | 100.00% |

Both providers list identical pricing (matching the `models-api.json` record for `xiaomi/mimo-v2.6-pro`: `prompt: 0.000000435`, `completion: 0.00000087`, `input_cache_read: 0.0000000036` — i.e. $0.435/$0.87/$0.0036 per MTok). DeepInfra is faster to first token (1.00s vs 3.87s) but lower throughput (24 tps vs 30 tps) and lower measured uptime (97.83% vs 100.00%) than Xiaomi's own first-party endpoint.

## API specs (from `models-api.json`, `xiaomi/mimo-v2.6-pro`)

- **Context length: 1,048,576 tokens.** **Max completion tokens: 131,072.**
- **Modality:** `text+image+audio+video->text` (input: text, image, video, audio; output: text only).
- **Pricing (as listed):** prompt $0.435/MTok, completion $0.87/MTok, cache read $0.0036/MTok.
- **Supported parameters:** frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_p.
- **Default parameters:** temperature 1, top_p 0.95, frequency_penalty 0.
- `hugging_face_id` is `null` on the Pro record in this JSON snapshot (Flash's record carries `XiaomiMiMo/MiMo-V2.6-Flash-RL`) — consistent with [[research/sources/mimo-v2-6]]'s note that HuggingFace weights/license were not independently verified there either.

## Capture gaps

- Pro's active-parameter count (if it is MoE) is not stated anywhere in this capture — only ">1T parameters" total.
- The UltraSpeed speed-multiplier contradiction (10x vs 20x) above is flagged, not resolved — no source here explains the discrepancy.
- Only the DeepInfra and Xiaomi provider rows were captured; if OpenRouter lists additional providers for this model at a later date, this page will not reflect them (this capture is a point-in-time snapshot, `static: false`).
