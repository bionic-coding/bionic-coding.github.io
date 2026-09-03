---
title: "Introducing Gemini 3.8 Flash and 3.8 Flash Cyber"
slug: gemini-3-8-flash
type: source
source_url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/
source_date: 2026-09-02
author: "Tulsee Doshi and Raluca Ada Popa (Google / Google DeepMind)"
captured_at: 2026-09-03
last_source_check: 2026-09-03
raw_path: research/raw/2026-09-03/gemini-3-8-flash/
previous_captures: []
static: true
tags: [google, gemini, gemini-3-8-flash, model-release, pricing, benchmarks, cybersecurity, fairwind]
---

Google's launch post for **Gemini 3.8 Flash** and **Gemini 3.8 Flash Cyber**, published 2026-09-02 on The Keyword, one day after Anthropic's Fable 5.1. Two authors: Tulsee Doshi (Senior Director, Product Management) and Raluca Ada Popa (Gemini Security Lead, Google DeepMind). The post is a vendor launch announcement: every benchmark number is Google's own, and the comparison tables are images. The table below was transcribed from the image in the raw capture. The pricing was verified against Google's API pricing page, fetched the same day and saved in the raw capture as `gemini-api-pricing.html`.

Related: Google's Gemini 3.7 Flash appears as a comparison column in Z.ai's GLM-5.3-Flash table ([[research/sources/glm-5-3-flash]]); this is the first Google source page in the wiki.

## What the post says

- **Third Flash release in six weeks.** Gemini 3.8 follows 3.7 Flash "from three weeks ago." Google calls 3.8 "our best reasoning & coding model yet, at the same speed and low cost of 3.7." Both variants share one base model; Google credits the gains partly to "rigorous training in the highly demanding domain of cybersecurity" and to "long-running agentic loops designed to recursively evaluate and refine the underlying models."
- **Gemini 3.8 Flash** — "our most intelligent workhorse model." Available now to developers (Gemini API via AI Studio, Antigravity, Android Studio, Stitch), enterprises (Gemini Enterprise), and consumers (Google AI Pro and Ultra subscribers in the Gemini app, AI Mode in Search, Sheets).
- **Gemini 3.8 Flash Cyber** — "our most capable cybersecurity model," available only to "trusted defenders" through the new **Fairwind Program** (government authorities, critical-infrastructure operators, software maintainers, by application). It "ships with a more permissive set of mitigations for cybersecurity." Google says it prioritized "vulnerability fixing from the start ... over offensive capabilities like exploitation."
- **3.8 Flash "works harder."** Google's own framing: on complex tasks it executes extra reasoning steps and calls tools iteratively, and "might use more tokens to maximize performance, especially at higher effort levels." Developers who need to hold cost down are told to use lower effort levels or stay on 3.7 Flash, "which remains fully supported for efficiency-first workloads."
- **Safety:** CBRN and cyber-offense safeguards per Google's Frontier Safety Framework; a claimed "significant leap in prompt injection robustness as measured by Gray Swan" (chart not transcribed).

## Pricing (verified against ai.google.dev/gemini-api/docs/pricing, fetched 2026-09-03)

| | Through 2026-12-31 (introductory) | From 2027-01-01 |
|---|---|---|
| Input, per MTok | **$0.75** | $1.50 |
| Output incl. thinking tokens, per MTok | **$3.75** | $7.50 |
| Context caching, per MTok | $0.075 | $0.15 |
| Cache storage, per MTok per hour | $0.50 | $1.00 |
| Batch input / output | $0.375 / $1.875 | $0.75 / $3.75 |

The pricing page lists **Gemini 3.7 Flash at the identical schedule**, including the same 2026-12-31 expiry. So "the same introductory price as 3.7 Flash" is exact, and the headline $0.75 / $3.75 is a price that doubles on 2027-01-01 for both models. Free tier: input and output free of charge, "used to improve our products: yes."

## Benchmark table (transcribed from the post's image; all figures Google's)

Methodology link in the image footer: `deepmind.google/models/evals-methodology/gemini-3-8-flash` (not captured). Bold in the image marked the column leader; reproduced here as **bold**.

| Benchmark | Gemini 3.8 Flash | Gemini 3.7 Flash | Claude Opus 5 | Claude Sonnet 5 | GPT-5.6 Sol | GPT-5.6 Terra |
|---|---|---|---|---|---|---|
| Input price $/MTok (no caching) | $0.75 ($1.50 regular) | $0.75 ($1.50 regular) | $5.00 | $2.00 | $4.00 | $2.00 |
| Output price $/MTok | $3.75 ($7.50 regular) | $3.75 ($7.50 regular) | $25.00 | $10.00 | $20.00 | $12.00 |
| DeepSWE v1.1 (long-horizon SWE) | 73.7% | 65.3% | **74.0%** | 53.8% | 72.7% | 69.6% |
| GDPVal-AA v2 (knowledge work, Elo) | 1545 | 1482 | **1824** | 1584 | 1710 | 1528 |
| Vals Finance Agent v2 | **61.4%** | 59.0% | 58.6% | 53.9% | 53.8% | 54.4% |
| Harvey's Legal Agent Benchmark (all pass rate) | **10.0%** | 8.8% | 6.7% | 5.0% | 2.5% | 0.8% |
| Terminal-Bench 2.1 | **89.4%** | 85.8% | 89.1% | 80.4% | 88.8% | 87.4% |
| Terminal-Bench 4.0 (general agent) | 19.1% | 11.2% | **51.8%** | 12.4% | 37.3% | 23.6% |
| GDP.PDF (expert PDF comprehension, all pass) | 35.0% | 34.0% | 37.0% | 28.0% | **40.0%** | 29.0% |
| CharXiv Reasoning (no tools) | **86.2%** | 84.5% | 83.7% | 70.1% | 85.8% | 85.9% |
| LVBench (long video) | **87.8% agentic / 87.1% static** | 85.4% | 75.4% | 68.5% | 82.1% | 78.9% |
| HLE-Verified | **54.9%** | 53.6% | 54.4% | 31.0% | 54.5% | 51.1% |
| OSWorld-2.0 (partial score, batch tool) | 59.0% | 50.6% | **75.4%** | 42.6% | 62.6% | 50.2% |
| BioMysteryBench, human-solvable | 88.8% | 87.1% | **90.1%** | 87.5% | 79.5% | 83.8% |
| BioMysteryBench, human-difficult | **56.5%** | 43.5% | 49.4% | 34.1% | 44.7% | 49.4% |
| LABBench2 | **86.2%** | 82.1% | 84.2% | 80.1% | 82.1% | 81.2% |

Reading the table rather than the headline: 3.8 Flash leads 8 of the 14 scored rows, mostly by under two points, and **Opus 5 leads by wide margins on the three rows that measure general agency and knowledge work** (Terminal-Bench 4.0 51.8 vs 19.1, OSWorld-2.0 75.4 vs 59.0, GDPVal-AA 1824 vs 1545). The DeepSWE row is 73.7 vs 74.0, at roughly a sixth of Opus 5's list output price. Google's own text is careful about this: "often approaching the performance of higher-cost frontier models."

The **DeepSWE cost chart** (second image; source Datacurve AI) plots pass rate against average cost per task. Read from the chart, approximately: Gemini 3.8 Flash ~74% at about $1.50 per task; Opus 5 ~74% at about $9; Fable 5 ~70% at about $11; Kimi K3 ~70% at about $3; GLM-5.3 ~66%; Gemini 3.7 Flash ~65%; GLM-5.3 Flash ~63% at under $1; Qwen 3.8 ~59%; Muse Spark 1.2 ~55%. Approximate readings of a chart, not published figures.

### Cross-vendor corroboration

Opus 5's DeepSWE 74.0 and GDPVal-AA 1824, and GPT-5.6 Sol's GDPVal-AA 1710, appear identically in Meta's Muse Spark 1.3 scorecard published the same day ([[research/sources/meta-muse-spark-1-3]]). Terminal-Bench 2.1 for Opus 5 differs: 89.1 here, 86.7 in Meta's table, which runs each model through a named coding agent. GLM-5.3-Flash's DeepSWE reading (~63%) matches Z.ai's self-reported 63.4 ([[research/sources/glm-5-3-flash]]).

> [contradiction] **GPT-5.6 prices.** This table gives GPT-5.6 Sol at $4 / $20 and Terra at $2 / $12. The wiki's July capture ([[research/sources/gpt-5-6-pricing]], user paste of 2026-07-13) had Sol at $5 / $30 and Terra at $2.50 / $15. OpenAI's live pricing page, fetched 2026-09-03, agrees with Google: Sol $4 / $20 short-context with "promotional pricing ... at least through November 21, 2026." Resolved in favor of the current page; see the refreshed pricing source. Google's Opus 5 ($5 / $25) and Sonnet 5 ($2 / $10) figures match Anthropic's own lineup table ([[research/sources/claude-fable-5-1-overview]]).

## Gemini 3.8 Flash Cyber — claims

- **CyberGym:** "frontier-level performance in autonomous vulnerability discovery," surpassing 3.5 Flash Cyber "as well as significantly larger frontier models." Chart not transcribed.
- **Internal 20-language vulnerability benchmark:** success rate "exceeding 70%." Internal, unnamed.
- **CWE-Bench (Collinear, patching):** pass@1 **47.2%** vs "a leading frontier model at 47.8%," at lower cost. The leading model is not named.
- **Deployment anecdotes, all Google or partner self-reports:** Chrome Security saw "2.6 times more correct patches" than "the best commercial models that are much larger"; Wiz reports +7.5–9.7% recall at 2.3–5.2× lower cost on an internal pentest benchmark; Google's Cloud Vulnerability Research team found "a critical foundational vulnerability in less than 2 hours." Partner testimonials (Armadin, Palo Alto Networks, Snowflake, Wiz) are image quotes, not transcribed.

## Demos named in the post

Vendor showcases built in Antigravity or AI Studio, no benchmark attached: a 3D wizard-castle game with Nano Banana textures; a "DOS version of Google Maps" from a single prompt; a USGS-data topographic explorer; "Hardware Anatomy," a Three.js device-teardown visualizer.

## Capture gaps

- **Every benchmark number is vendor-run**, from a single image. The methodology page linked in the image footer was not captured. No independent evaluation existed at capture time.
- The CyberGym, real-world vulnerability, CWE-Bench cost, and Gray Swan charts were downloaded as images but not transcribed; only the figures stated in the post's prose are recorded above.
- The DeepSWE cost-per-task figures are read off a chart and are approximate.
- Context window, output limit, and knowledge cutoff are not stated in the post. The pricing page's "short context / long context" split for Gemini was not examined here.
- The Fairwind Program page and the "Frontier Safety Framework" page are linked but not captured.
- The post's embedded video demos did not survive extraction; only their captions did.
