---
layout: post
title: "This Week in AI — July 27, 2026"
date: 2026-07-27
description: "Anthropic ships Claude Opus 5, and Kimi K3's open weights finally land on Hugging Face."
tags: [model-news, weekly]
---

Early last week I predicted an Opus release based on model degradation I was seeing, and sure enough, Anthropic released it on Friday.

## Claude Opus 5 Is Here

Anthropic released Claude Opus 5 on Friday, an upgrade to Opus 4.8 with the biggest gains in agentic coding, computer use, and long-horizon knowledge work.

Knowledge cutoff is May 2026. It ships under the same **ASL-3** protections as Opus 4.8. Anthropic assesses its overall alignment risk as "very low" — calling it their most aligned model to date, ahead of Sonnet 5, Opus 4.8, and even Mythos 5.

**What's genuinely interesting is what Anthropic published against itself.** In the alignment section: Opus 5 **hallucinates factual claims slightly more than Opus 4.8 — despite being more accurate overall.** They also found "a surprising number of cases" where the model **confidently stated an answer it was actually unsure about**.

**More info:**
- [**Anthropic's announcement**](https://www.anthropic.com/news/claude-opus-5) — the primary post.

## Kimi K3's Weights Are Out

Moonshot released the Kimi K3 weights on Hugging Face, hitting the July 27th target they set at announcement.

This is the 2.8-trillion-parameter open-weights model I covered when it was announced — Mixture-of-Experts, 16 of 896 experts active per request, 1M-token context, native vision. Back then it was an announcement with a hosted API and no weights. Now it's a download.

**More info:**
- [**Kimi K3 on Hugging Face**](https://huggingface.co/moonshotai/Kimi-K3) — the weights.

<!-- STANDING CLOSER — permanent fixture, every issue closes on it. First-person, opinion not news: what you're reaching for this week, and why. -->
## What I'm actually using

`<closing take — what you're reaching for this week, and why>`
