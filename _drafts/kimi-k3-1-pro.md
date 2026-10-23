---
layout: post
title: "TITLE"
date: 2026-10-23
description: "DESCRIPTION"
tags: [model-news, kimi, open-weights]
---

TODO: opening — why this release matters to you.

## What shipped

TODO

<!--
Facts (Moonshot's launch post, checked Oct 23; all vendor-reported):
- K3.1 Pro: post-trained K3, "3T-class" open-weight, 1M-token context.
- K3.1 Pro Highspeed: claims 2-3x the speed of K3.1 Pro.
- Live today: Kimi.ai, apps, Kimi Work, Kimi Code (/model), API (kimi-k3.1-pro, kimi-k3.1-pro-highspeed). Zero Data Retention on the API.
- Weights promised "by Nov 4, 2026". No license on the launch page.
- API price (platform.kimi.ai/docs/pricing/chat, checked Oct 23): K3.1 Pro $2 in / $10 out per MTok, cached $0.20. Highspeed $4 / $20. K3 was $3 / $15, so the new model is cheaper.
- Cache writes billed separately: $2 (5m TTL, default) / $4 (1h). Caching is on automatically.
- K2 series: closed to new users Oct 31, retired by end of December 2026.
- Compare Gemini 4 Argon: $2 / $10 until Nov 30, then $4 / $20.
-->

## How it compares

TODO

<!--
Vendor chart (Claude Code harness for most Kimi runs; competitor scores often copied from their own reports):
- Terminal-Bench 4.0: K3.1 Pro 65.7, Opus 5.5 66.4, GPT-6 Astra 58.2, Fable 5.1 57.9.
- SWE Marathon: K3.1 Pro 51.7 (first), Opus 5.5 46.3.
- Terminal-Bench Science 0.1: K3.1 Pro 38.1, GPT-6 Astra 68.1, Opus 5.5 63.3. (trails)
- OfficeQA Pro v2: 64.4 (first). Frontier Finance: 58.6 (Fable 5.1 60.8 leads).
- Leads DeepSeek-V4.1-Flash-1017 and GLM-5.3 on every panel.
- Gemini 4 Argon TB4.0 was 57.4 (Google-reported) — see bionic/briefs/BRIEF-gemini-4-argon-release.md.
Full table: bionic/research/sources/kimi-k3-1-pro.md
-->

## The cyber decision

TODO

<!--
- Moonshot removed cyber-related data from mid-training and RL for the open-weight release.
- Internal xdev-bench-hard pass@3: unfiltered checkpoint 90.5, released 81.0, K3 33.3.
- Stated principles: open weights shouldn't extend the absolute cyber frontier; raise open cyber capability progressively, for defenders.
-->

## What I'm going to do with it

TODO

<!--
Open questions before publishing:
- License (K3 was MIT) — check when weights land.
- Did weights actually ship by Nov 4?
-->

**More info:**

- [Introducing Kimi K3.1 Pro (checked Oct 23)](https://www.kimi.ai/blog/kimi-k3-1-pro) — TODO annotation.
- [Kimi API pricing (checked Oct 23)](https://platform.kimi.ai/docs/pricing/chat) — TODO annotation.
