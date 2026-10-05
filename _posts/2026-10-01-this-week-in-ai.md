---
layout: post
title: "This Week in AI — October 1, 2026"
date: 2026-10-01
description: "Claude Sonnet 5.5 and GPT-6.1 Sol promise more capability at the same token prices, while Fireworks' Ember-1 reduces tokens to making Kimi K3 cheaper to run."
tags: [model-news, weekly]
---

Last week brought a lot of new models. This week, Sonnet and Sol are already getting upgrades, with both companies promising more useful work for the same token prices. I'm also interested in Ember-1, which tackles something that has kept me from using Kimi K3 more: the cost of all that thinking.

## Claude Sonnet 5.5 closes some of the gap with Opus

Anthropic released Sonnet 5.5 on September 28, positioning it for everyday coding, bug fixes, and work with documents, slides, and spreadsheets.

Standard API pricing stays at $2 per million input tokens and $10 per million output tokens. Cache reads remain $0.20. Anthropic says Sonnet 5.5 generates output more than 30% faster than Sonnet 5. It also reports up to 30% lower costs per task because the model uses fewer tokens. Your savings will depend on the work you give it.

**From Anthropic's release:** Sonnet 5.5 scores 70.6% on Terminal-Bench 4.0, compared with Sonnet 5's 10.3%. On CursorBench 4.0, which uses tasks from real coding sessions, it rises from 34.1% to 55.5%. Opus 5.5 scores 57.8% on that same evaluation. Sonnet also comes within two points of Opus on GDPval-AA, a test of professional work.

That gives Sonnet more room to handle work we might previously have handed to Opus. Anthropic still says Opus is clearly stronger on complex, open-ended tasks that require sustained judgment. I would keep that distinction in mind before moving an entire workflow over.

There is a practical catch for API users. Sonnet 5.5 rejects the old setting that disables thinking entirely, and it no longer accepts forced tool calls. The replacement thinking setting allows reasoning between tool calls. If you maintain your own integration, read the migration guide before changing the model name.

**More info:**

- [**Introducing Claude Sonnet 5.5**](https://www.anthropic.com/claude-sonnet-5-5) — launch, pricing, benchmark comparisons, and where Anthropic still prefers Opus.
- [Sonnet 5.5 overview](https://platform.claude.com/docs/en/models/sonnet-5-5/overview) — model limits and supported features.
- [Sonnet 5.5 migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide) — changes for existing API integrations.

## GPT-6.1 Sol moves closer to Astra

OpenAI released GPT-6.1 Sol on September 29, just a week after GPT-6 Sol.

Standard API input and output prices stay at $2 and $10 per million tokens. Cached input falls from $0.20 to $0.10. For agents that repeatedly reuse the same context, that is a price reduction you can benefit from without needing a benchmark improvement.

OpenAI's larger claim is that Sol now approaches Astra on coding, computer use, and professional work at one-fifth of Astra's standard token prices.

**From OpenAI's release:** Sol matches Astra on DeepSWE v1.1, a software engineering evaluation, at roughly one-fifth of the cost per task. On AutomationBench, which tests business workflows involving multiple tools, Sol at medium effort scores 2.2 percentage points above Opus 5.5. OpenAI reports roughly a third of the cost for that comparison.

These results make Sol more interesting for work that would otherwise consume a lot of Astra tokens. They don't establish that Sol can replace Astra across the board. Astra still leads OpenAI's scientific workflow evaluation, for example.

The Sonnet and Sol announcements also don't settle which of the two new models is better. Anthropic's comparisons use the older GPT-6 Sol. The releases cover different evaluations and settings. I'd rather compare them on familiar work than try to assemble a ranking from those tables.

Sol is available in ChatGPT Work and Codex, but OpenAI's launch announcement says it is not yet available in ordinary Chat.

**More info:**

- [**Introducing GPT-6.1 Sol**](https://openai.com/index/introducing-gpt-6-1-sol/) — capability claims, task-cost comparisons, and rollout.
- [GPT-6.1 Sol model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol) — API pricing, limits, and tool support.
- [GPT-6.1 Sol system card addendum](https://deploymentsafety.openai.com/gpt-6-1-sol) — safety evaluations and their test conditions.

## Ember-1 and the cost of Kimi K3

I've liked Kimi K3, but found it expensive. Fireworks' Ember-1 is interesting for exactly that reason: it is built on Kimi K3 and trained to shorten its reasoning.

**Fireworks' claim:** comparable quality with roughly 40% fewer tokens. Ember-1 and Kimi K3 have the same standard per-token prices on Fireworks; the promised savings come from using fewer tokens to finish the work. Fireworks released Ember-1 on September 23 as a research preview with an initial two-week serverless access window.

**More info:**

- [**Introducing Ember-1**](https://fireworks.ai/blog/ember-1) — training approach, Fireworks' benchmark results, and customer A/B tests.
- [Fireworks serverless pricing](https://docs.fireworks.ai/serverless/pricing) — per-token prices for Ember-1 and Kimi K3.

## What I'm actually using

I've tried Ember-1 but I don't think the API is ready for production use yet. I typically have long running tasks and it error'd out several times before task completion.

I am using GPT-6.1 Sol right now as the pricing is competitive with other models and the API is stable.

Sonnet 5.5 is great, but more expensive than my current coding model for daily use. If you're running Claude Code it should help bring the costs down.
