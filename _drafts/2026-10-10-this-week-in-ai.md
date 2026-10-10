---
layout: post
title: "This Week in AI — October 10, 2026"
date: 2026-10-10
description: "GPT-6.1 Sol can get carried away with testing, while Claude Haiku 5.5 brings cheaper tokens and stronger coding results, with some qualifications."
tags: [model-news, weekly]
---

<!-- LEDE: Add once the rest of this week's stories are assembled. -->

## GPT-6.1 Sol can get carried away with testing

Something I've noticed specifically with GPT-6.1 Sol: it has a tendency to overcomplicate things, especially around testing, in ways I haven't seen with GPT-6 Sol or other models.

**Evidence status:** **Reported** — These are observations from my own agent runs, not a controlled comparison between models.

I often run multi-day tasks using an agent graph, where several agents work through different parts of a job. Since adopting Sol 6.1, I've seen a pattern emerge. It's so intent on proving it's correct that it writes test suites that take days to run. Then it attempts to run them multiple times as it works toward a solution.

The testing grows until the task effectively becomes impossible to complete.

I've seen this several times now. The only fix I've found has been to walk back the run and start from scratch.

GPT-6 Sol didn't do this in my runs. It's new with GPT-6.1 Sol. Just something to keep an eye out for.

## Claude Haiku 5.5 makes smaller jobs cheaper

Anthropic released Haiku 5.5 on October 7, with lower token prices and a substantial improvement over Haiku 4.5 on its published coding evaluations.

**Evidence status:** **Verified** — The release and launch prices are documented by Anthropic.

**Evidence status:** **Claimed** — The performance figures below are published in Anthropic's system card; I haven't run my own comparison.

For prompts up to 100,000 tokens, Haiku 5.5 costs $0.10 per million input tokens and $0.50 per million output tokens. That's 90% below Haiku 4.5's token prices. Above that prompt threshold, the rates rise to $0.50 and $2.50. Long conversations need different cost estimates.

The coding results are interesting. On SWE-Bench Pro, which tests fixes to real software repositories, Haiku scores 64.8% against Sonnet 5.5's 81.3%. On Terminal-Bench 4.0, which tests broader engineering work in a terminal, it scores 39.2% against Sonnet's 70.6%. That's a large gap, even with Haiku's improvement over the previous version.

The qualification I'd keep in mind is effort. Most of Haiku's headline scores use maximum effort, while the API defaults to medium. On one professional-work benchmark, maximum effort used roughly ten times as many output tokens as medium. Cheap tokens can still add up.

For an agent graph, I'd be interested in trying Haiku on smaller, clearly defined jobs: finding a piece of information, summarizing context, or implementing a scoped change. The question is whether it finishes those jobs correctly enough that retries and review don't eat the savings.

There's also a migration detail worth checking: the same input text counts as approximately 30% more tokens than on Haiku 4.5. Anthropic changed the thinking configuration and several other API behaviors too, so read the migration guide before swapping the model name.

Alongside the launch, Anthropic halved Sonnet 5.5's cache-read price to $0.10 per million tokens. That also lowers the cost of agent runs that repeatedly send the same context.

**More info:**

- [**Claude Haiku 5.5** (Oct 7)](https://www.anthropic.com/claude-haiku-5-5) — announcement, launch pricing, and the Sonnet cache-price change.
- [Haiku 5.5 system card (Oct 7)](https://www.anthropic.com/claude-haiku-5-5-system-card) — coding results and evaluation settings; see pages 111–115 and 131.
- [Haiku 5.5 migration guide (checked Oct 7)](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide) — tokenizer changes and request compatibility.

<!-- Add further stories here. Revisit the description and story order as the issue grows. -->

## What I'm actually using

<!-- Add this week's personal closer before publication. -->
