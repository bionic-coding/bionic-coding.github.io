---
title: "GPT-5.6 Frontier Models — API Pricing (Sol / Terra / Luna)"
slug: gpt-5-6-pricing
type: source
source_url: https://platform.openai.com/docs/pricing
source_date: null
author: "OpenAI"
captured_at: 2026-07-13
last_source_check: 2026-09-03
raw_path: research/raw/2026-09-03/gpt-5-6-pricing/
previous_captures: [research/raw/2026-07-13/gpt-5-6-pricing/]
static: false
tags: [openai, gpt-5-6, sol, terra, luna, pricing, api]
---

# GPT-5.6 Frontier Models — API Pricing

_OpenAI API pricing for the GPT-5.6 family. First captured 2026-07-13 from a user paste; refreshed 2026-09-03 from the live pricing page at `platform.openai.com/docs/pricing`, which is now the `source_url`._

## Current prices (refreshed 2026-09-03)

Standard tier, per MTok. OpenAI splits every price into **short context** and **long context** columns; the long-context column is exactly double. The page states: **"GPT-5.6 Sol's promotional pricing is available at least through November 21, 2026."** No promotional label is attached to Terra or Luna.

| Model | Input | Cached input | Cache writes | Output | Long-context input / output |
|---|---|---|---|---|---|
| `gpt-5.6-sol` | **$4.00** | $0.40 | $5.00 | **$20.00** | $8.00 / $30.00 |
| `gpt-5.6-terra` | **$2.00** | $0.20 | $2.50 | **$12.00** | $4.00 / $18.00 |
| `gpt-5.6-luna` | **$0.20** | $0.02 | $0.25 | **$1.20** | $0.40 / $1.80 |

Batch and Flex tiers are half the standard price (Sol $2 / $10); Fast mode (renamed from Priority processing on 2026-07-30) is double (Sol $8 / $40). Regional data-residency endpoints carry a 10% uplift.

## What changed since the July capture

| Model | July 13 capture (input / output) | September 3 page (short context) |
|---|---|---|
| Sol | $5 / $30 | **$4 / $20**, labeled promotional through at least 2026-11-21 |
| Terra | $2.50 / $15 | **$2 / $12** |
| Luna | $1 / $6 | **$0.20 / $1.20** |

All three tiers are cheaper than the July figures. The Sol cut is a labeled promotion with an end date; the Terra and Luna figures carry no such label on the page. The July capture was a user paste whose URL was never recorded, so it is possible the two captures describe different pages (the July paste may have been a long-context or launch-day schedule). Treat the September figures as current and the July figures as superseded. Google's Gemini 3.8 Flash comparison table, published 2026-09-02, uses the September figures for Sol and Terra ([[research/sources/gemini-3-8-flash]]).

This is the first OpenAI price move recorded in the wiki, and it moves the same direction as Anthropic's three (Opus 5 held at Opus 4.8's price, the Sonnet 5 increase cancelled, Fable 5.1 held with cache reads cut). See the price-direction note in [[research/references/frontier-models-2026]].

## Original capture (2026-07-13, user paste)

> Start with GPT-5.6 Sol for complex reasoning and coding, choose GPT-5.6 Terra to balance intelligence and cost, or use GPT-5.6 Luna for cost-sensitive, high-volume workloads.

All three GPT-5.6 tiers expose the same reasoning-effort levels: **none, low, medium, high, xhigh, max.**

| Tier | Model ID | Alias | Blurb | Input ($/MTok) | Output ($/MTok) |
|---|---|---|---|---|---|
| **GPT-5.6 Sol** | `gpt-5.6-sol` | `gpt-5.6` | Frontier model for complex professional work | $5 | $30 |
| **GPT-5.6 Terra** | `gpt-5.6-terra` | — | GPT-5.6 model that balances intelligence and cost | $2.50 | $15 |
| **GPT-5.6 Luna** | `gpt-5.6-luna` | — | GPT-5.6 model optimized for cost-sensitive workloads | $1 | $6 |

## Capture gaps

- **The July provenance is a user paste, not a fetched capture**, and its URL was not recorded. The September refresh is a fetched capture of the platform docs pricing page (`source.html` and a tag-stripped `extracted.md` in the raw directory); the page is JavaScript-heavy and the extraction is a flattened text dump, not a rendered table.
- The refresh did not capture the page's model-catalog entries (context window, knowledge cutoff), the tool-call pricing, or the audio/image/video model prices.
- Whether the Terra and Luna reductions are permanent is not stated on the page.
