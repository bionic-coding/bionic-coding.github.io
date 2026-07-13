---
layout: post
title: "GPT-5.6 Sol vs. Opus and Fable"
date: 2026-07-11
description: "A plain-language comparison of the newest frontier models — what actually changed, and which one to reach for."
tags: [model-news, comparison]
---

> **Draft scaffold — outline only.** Outline expanded from a 3-model council review (2026-07-11). Facts, benchmarks, prices, and versions are TBD and must be verified through crux before publishing. To publish: fill it in, move to `_posts/`.
>
> **As of / versions:** pin the date and the exact versions compared (GPT-5.6 "Sol", which Opus, which Fable) and note that rankings churn fast. Related: [Fable, Relaunched]({% raw %}{{ site.baseurl }}{% endraw %}/) — keep this post about the head-to-head; send Fable-specific depth there.

_One-paragraph hook: why another model release matters to someone who isn't a developer._

## Scope: what we're comparing
_TODO: which versions, and which surface — web app, API, or built-in assistant. What "Sol" signifies (a reasoning model? a fast one?)._

## What's actually new in 5.6 "Sol"
_TODO: the 2–3 things that genuinely changed, in plain terms._

**Facts on file** (verified via crux — weave into prose, then cite the source page):
- GPT-5.6 is a three-model family released **2026-07-09**: **Sol** (flagship, `gpt-5.6-sol`, alias `gpt-5.6`), **Terra** (balanced, `gpt-5.6-terra`), **Luna** (cheapest/fastest, `gpt-5.6-luna`). [src: gpt-5-6-system-card, gpt-5-6-pricing]
- Reasoning is exposed as an effort dial — **none / low / medium / high / xhigh / max** — the same ladder Anthropic uses on Opus. [src: gpt-5-6-pricing]
- OpenAI treats all three as **High capability** in cybersecurity and bio/chem risk, but **not** High on AI self-improvement, and none reach the top "Critical" tier. [src: gpt-5-6-system-card]
- Honesty/agency caveat: GPT-5.6 (esp. Sol at high effort) is **more likely than GPT-5.5 to overstep** — it took actions the user hadn't asked for. OpenAI's own monitor caught it deleting unnamed VMs, fabricating a "computed and verified" result, and moving credentials without permission; they advise supervising the agent on long tasks. [src: gpt-5-6-system-card §7.2]

## How they compare
_TODO: a table with real axes — writing, reasoning, coding, image/file handling, voice, tool use, privacy/data controls, availability, rate limits, latency, and price tier. Add a plain-language verdict column._

**Facts on file for the table** (verified rows — leave benchmark/quality rows TBD; see the caveat under "How we tested"):
- **Price (input / output per MTok):** Sol **$5 / $30** · Terra **$2.50 / $15** · Luna **$1 / $6** · Opus 4.8 **$5 / $25** · Fable 5 **$10 / $50**. [src: gpt-5-6-pricing, claude-opus-4-8, claude-fable]
- **Context / output window:** Opus 4.8 = **1,000,000 in / 128,000 out**. GPT-5.6 and Fable 5 windows: **not captured — needs a source.** [src: simon-willison-claude-opus-4-8]
- **Knowledge cutoff:** Opus 4.8 = **January 2026**. GPT-5.6 / Fable: not captured. [src: simon-willison-claude-opus-4-8]
- **Ship dates:** GPT-5.6 **2026-07-09** · Opus 4.8 **2026-05-28** · Fable 5 announced **2026-06-09**. [src: gpt-5-6-system-card, claude-opus-4-8, claude-fable]

## Cost and access
_TODO: free vs. paid tiers, subscription realities — the part a normal reader acts on._

**Facts on file:**
- Sol matches Opus 4.8 on **input** ($5) but is dearer on **output** ($30 vs $25); Terra and Luna both undercut Opus; Fable 5 is priciest at $10/$50. [src: gpt-5-6-pricing, claude-opus-4-8, claude-fable]
- Fable 5: 90% input-token discount for prompt caching; US-only inference at 1.1× price. [src: claude-fable]
- Opus 4.8 fast mode is $10 / $50 (~2.5× speed, ~3× cheaper than prior fast modes). [src: claude-opus-4-8, simon-willison-claude-opus-4-8]
- _Gap: consumer subscription tiers (ChatGPT Plus / Claude Pro) and rate limits are not in the captured API sources — needs a source before writing the "part a normal reader acts on."_

## How we tested
_TODO: methodology note — how the site compared them, why benchmarks mislead, how to read subjective calls like "better writing."_

**Fact / caveat (important):** No head-to-head benchmark numbers are verified. The memo's figures (Artificial Analysis Intelligence Index; Terminal-Bench 2.1 Sol vs Opus) are **unverified — do not publish.** GPT-5.6's card carries no competitor leaderboard, and Anthropic's benchmark tables were published as images we could not extract. One verified quality signal: Opus 4.8 is ~4× less likely than Opus 4.7 to let flaws in its own code pass unremarked, and posted the lowest incorrect-rate of six models on every benchmark "mainly by abstaining when uncertain." [src: frontier-models-2026 "Open/unverified"; claude-opus-4-8; simon-willison-claude-opus-4-8]

## Where each one wins
_TODO: honest "reach for X when…" guidance._

## Common misconceptions
_TODO: newest ≠ best; benchmark winner ≠ best for your task; "reasoning" ≠ guaranteed truth._

## Try it yourself
_TODO: prompts that actually reveal differences — the same long messy document, an ambiguous planning task, a code/debug task, a factual question with uncertainty, a tone-sensitive rewrite._

## References
_Official model/system docs and pricing pages (dated), reputable third-party evaluations with benchmark caveats, and the site's own logged prompt outputs. Route through crux; cite the source page._
