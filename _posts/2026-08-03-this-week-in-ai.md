---
layout: post
title: "This Week in AI — August 3, 2026"
date: 2026-08-03
description: "I've given up on Opus 5"
tags: [model-news, weekly]
---

After a day of using Opus 5 I suspected something was up. A couple days in I have rolled back to Opus 4.8 and I'm running mostly running Kimi K3 + Opencode.

## I Switched from Claude Code to Kimi K3 + Opencode

Burried in the Opus 5 system card are these little gems:

> Claude Opus 5 is more accurate than Opus 4.8 but hallucinates slightly more claims of a factual nature. When pushed by the user on something it knows to be incorrect, Claude Opus 5 resorts to agreeing with the user more than Sonnet 5 and Mythos Preview, but less than all other recent models.

and

> Alignment issues did not surface as major themes in the feedback that either internal or external users gave. The most relevant themes from internal users were:
> 
> - Overconfident and unsupported claims, sometimes from model-fabricated data, often followed by theatrical retractions;

About half way through last week I started hitting issues similar to the ones described above. I'd ask for a review of some information and end up with inconsistent or contradictory results. Eventually I reverted the model back to Opus 4.8 and was shocked at how much better the response was.

I contemplated forcing a downgrade in Claude Code, but I'd heard great things about Kimi K3. I had been keeping Crux in a spot where I could run it in Opencode so I cut over to using it with Kimi K3.

I had it review the previous two weeks worth of work and the results were damning. 

To be clear, I don't run everything through K3. It's a primary driver that reports to me and ensures that the process that I've laid out is being followed. There are tasks that run through about a dozen different models as part of the workflow. 

And so far so good. But we're still cleaning up the mess Opus 5 left behind.

## Qwen 3.8 Max Landed — the API, Anyway

On the subject of open weight models, Qwen 3.8 Max is now available via Alibaba Cloud.
They have also promised to release the weights shortly.

**Here are the key details:**
- **2.4T parameters, 95B active** — the serving number Alibaba withheld through two prior announcements.
- **$2 / $6 per million tokens** — against Kimi K3's $3 / $15 and Fable 5's $10 / $50. An eighth of Fable's output price.
- **1M context**, image, text *and video* in; three effort levels (`xhigh` default, `medium`, `low`).
- **Fable 5 still leads on coding:** SWE-bench Pro 80.0 vs 67.7, FrontierSWE 88.8 vs 73.5 — and Fable beats Qwen on three of Qwen's own four in-house coding benchmarks.
- **The comparison table stops at Opus 4.8** — which is probably for the best. 

**More info:**
- [Qwen3.8-Max: A New Bar for Coding and Cowork](https://qwen.ai/blog?id=qwen3.8) — Alibaba's launch post and the source of every benchmark number above; the full table and its footnotes are at the bottom. Note footnote 1: "Fable5 results may involve fallbacks."
- [Qwen3.8-Max on QwenCloud](https://www.qwencloud.com/models/qwen3.8-max) — the serving page: price, context, and rate limits. This is where the verifiable numbers live.
