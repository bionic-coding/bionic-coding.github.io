---
layout: post
title: "Fable, Relaunched"
date: 2026-07-11
description: "What changed in the new Fable, who it's for, and where it fits next to the other models."
tags: [model-news]
---

> **Draft scaffold — outline only.** Outline expanded from a 3-model council review (2026-07-11). Nothing below is verified; confirm through crux before publishing. To publish: fill it in, move to `_posts/`.
>
> **As of / versions:** pin the date, the new version, and a dated baseline for "the last version." Related: the head-to-head lives in *GPT-5.6 Sol vs. Opus and Fable* — this post is Fable-specific; cross-link, don't duplicate.

_Hook: Fable is back / different — the one-line reason to care._

## What Fable is now
_TODO: who makes it, and whether it's a standalone model, a product, or an API — and where you actually access it._

**Facts on file** (verified via crux — weave in, then cite):
- Fable 5 is Anthropic's **5th-generation, "Mythos-level" model — a tier above Opus** — built for days-long, complex, asynchronous work. API id `claude-fable-5`. [src: claude-fable]
- Access: claude.ai **Pro / Max / Team / Enterprise**, plus **AWS, Google Cloud, Microsoft Foundry**. [src: claude-fable]

## What changed (and what didn't)
_TODO: before/after on concrete axes — capabilities, interface, context length, multimodality, tool use, safety policy, speed, cost, reliability. Include a "what did not change" beat to avoid release-hype framing._

**Facts on file:**
- Pricing: **$10 / $50 per MTok**; 90% input-token discount for prompt caching; US-only inference at 1.1×. [src: claude-fable]
- Safeguards/fallback: cyber- and bio-flagged queries **auto-route to Opus 4.8** (not billed at Fable prices); API customers wire this via a new **Fallback API**. **Mythos 5** is a gated higher tier for vetted cyber/bio research partners. [src: claude-fable]
- Using Fable requires **30-day data retention** for safety monitoring. [src: claude-fable]
- ⚠️ **Do not publish specs as fact:** the "1M context / 128K output / always-on adaptive thinking" figures are **unverified** — the Fable page states none of them, and the 1M/128K numbers actually belong to **Opus 4.8**. [src: claude-fable, simon-willison-claude-opus-4-8]

## Why the relaunch happened
_TODO: the motivation, briefly._

**Facts on file — handle with care (this is the post's riskiest claim):**
- Verified timeline: announced **Jun 9 2026** → access **unavailable Jun 12 2026** → **restored Jul 1 2026**. The dates are safe to cite. [src: claude-fable]
- ⚠️ **Contradiction — do NOT state the cause yet.** The council memo attributes the outage to a "US export-control directive," but Anthropic's page gives **no cause** and frames the return around **"enhanced safeguards."** Publish the *what / when*, not the *why*, until a primary (government or major-outlet) source confirms a reason. This gap is itself the honest, human-interest hook. [src: claude-fable, frontier-models-2026 "Open/unverified"]

## Cost and access
_TODO: free? subscription? region-limited? What changed about availability or limits._

**Facts on file:** $10 / $50 per MTok; 90% input-caching discount; **US-only inference at 1.1×**; on claude.ai Pro/Max/Team/Enterprise + AWS/GCP/Microsoft Foundry. Consumer-plan availability and rate limits not in the captured source — needs a source. [src: claude-fable]

## Who it's for
_TODO: the reader who should pay attention._

## What it's unusually good (or bad) at
_TODO: concrete everyday tasks — a sensitive email, summarizing a document, brainstorming, spreadsheet help, light coding, creative writing._

## Common misconceptions
_TODO: "relaunched" ≠ automatically better; a rename/repackage is not the same as a genuinely new model._

## Bottom line
_TODO._

## References
_Official release notes / model card, pricing & availability pages, independent benchmark summaries, and a hands-on test with reproducible prompts. Route through crux; cite the source page._
