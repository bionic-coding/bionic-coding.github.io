---
title: "Introducing Muse Spark 1.3"
slug: meta-muse-spark-1-3
type: source
source_url: https://research.meta.ai/blog/introducing-muse-spark-1-3
source_date: 2026-09-02
author: "Meta Superintelligence Labs"
captured_at: 2026-09-03
last_source_check: 2026-09-03
raw_path: research/raw/2026-09-03/meta-muse-spark-1-3/
previous_captures: []
static: true
tags: [meta, muse-spark, model-release, closed-model, agents, coding, benchmarks]
---

Meta Superintelligence Labs' launch post for **Muse Spark 1.3**, published 2026-09-02, the same day as Gemini 3.8 Flash and the day after Fable 5.1. Muse Spark is Meta's **closed** frontier model, the teacher from which the open-weights Muse Glimmer was distilled ([[research/sources/muse-glimmer-open-agentic-model]]). It is available in Meta's own coding agent, **Muse Code**, and through the **Meta Model API**; no third-party hosting and no weights. The benchmark scorecard is an image; it was transcribed below from the raw capture. Meta's four-page evaluation-methodology report, linked from the post, was fetched and saved in the raw capture as a PDF. It describes harnesses and metrics and carries no numbers.

## What the post says

- **Positioning:** "improved performance across agentic and coding tasks" and "easier to use in real-world settings," drawing on "months of broad adoption of Muse Code and Meta Model API." Meta frames it as a step "toward personal superintelligence."
- **Rollout:** available today in Muse Code and the Meta Model API. Existing reasoning modes ship now; the new **max reasoning** mode arrives "shortly after we finish additional safety testing." So the scorecard's "Muse Spark 1.3 (max)" column describes a mode that was not yet available on launch day.
- **Agentic behavior, as Meta describes it:** sustains longer-horizon work in "a single, long thread"; generates its own context from "messy and conflicting sources"; **asks clarifying questions when prompts are ambiguous, invokes help from the user when stuck, and confirms before taking consequential actions**; adapts between frequent updates and working silently; maps interrupting prompts to the right task in a busy thread; "better sense of what it can and can't do ... instead of hallucinating outcomes."
- **Coding:** trained on more long-horizon coding tasks. Versus 1.2, "takes fewer turns where not needed and is less verbose," and in Meta engineers' comparisons used **~20% fewer tool calls and ~25% fewer tokens**. Internal comparison, no benchmark attached.
- **Safety:** "stronger adversarial robustness" to prompt injection; "better calibration on what constitutes irreversible actions." No numbers.
- **Roadmap, one sentence:** "bigger models, **the Muse Spark open weights release**, and more." This is the first primary-source statement that Muse Spark itself will get an open-weights release. It does not say which version or when.

## Benchmark scorecard (transcribed from the image; all figures Meta's)

Per the methodology PDF: Muse Spark 1.3 at max effort, Opus 5 and GPT-5.6 Sol at max effort, Muse Spark 1.2 at xhigh. For each model Meta reports "the highest comparable primary-metric value available from our evaluation, the official leaderboard, or the model provider's self-reported results." Refusals and ungradable answers score zero. Third-party runs are "best-effort" and "may not reflect their best provider-optimized performance." Bold marks the row leader as highlighted in the image.

| Group | Benchmark | Muse Spark 1.3 (max) | Muse Spark 1.2 (xhigh) | GPT-5.6 Sol (max) | Opus 5 (max) |
|---|---|---|---|---|---|
| Agent | GDPVal-AA v2 (Elo) | 1754 | 1615 | 1710 | **1824** |
| Agent | JobBench | 64.9 | 61.6 | 45.4 | **65.7** |
| Agent | OSWorld 2.0, partial / binary | 66.9 / **32.0** | 47.6 / 17.9 | 62.7 / 27.3 | **68.3** / 31.4 |
| Agent | DeepSearchQA | 89.4 | 85.9 | **93.0** | 90.4 |
| Agent | Agentic IF Index (Meta internal) | 57.8 | 46.2 | **60.5** | 59.1 |
| Agent | AutomationBench | 49.4 | 38.2 | 46.7 | **50.3** |
| Long context | MRCR v2, 256K–512K | **98.5** | 66.3 | 91.5 | – |
| Long context | MRCR v2, 512K–1M | **98.1** | 55.5 | 73.8 | – |
| Coding | DeepSWE v1.1 | **75.4** | 55.0 | 73.0 | 74.0 |
| Coding | SWE-Atlas Codebase QnA | **59.4** | 46.2 | 53.5 | 52.7 |
| Coding | Terminal-Bench 2.1 | **88.8** | 82.9 | **88.8** | 86.7 |

Reading the table: Muse Spark 1.3 **leads on the three coding rows and both long-context rows**, ties GPT-5.6 Sol on Terminal-Bench 2.1, and **trails Opus 5 on five of the six agent rows**, in every case by less than two points or 70 Elo. The 1.2 → 1.3 jump is large everywhere (DeepSWE 55.0 → 75.4, MRCR 512K–1M 55.5 → 98.1). Opus 5 has no MRCR entry; the methodology says GPT-5.6 Sol's MRCR and Terminal-Bench figures come from OpenAI's model card rather than Meta's runs.

### Cross-vendor corroboration

Google's Gemini 3.8 Flash table, published the same day ([[research/sources/gemini-3-8-flash]]), reports the same Opus 5 DeepSWE (74.0) and GDPVal-AA (1824) and the same GPT-5.6 Sol GDPVal-AA (1710). Sol's DeepSWE is 73.0 here and 72.7 there. Opus 5's Terminal-Bench 2.1 differs, 86.7 here versus 89.1 at Google; Meta runs each model "with the coding agent named in the result," Google's harness is unstated. Muse Spark 1.2's DeepSWE 55.0 matches its position on Google's DeepSWE cost chart.

## Availability

Muse Code installs with a one-line script from `dev.meta.ai` (macOS and Linux). API access is through the Meta Model API at the same site. **No pricing appears in the post**, and no third-party provider (OpenRouter, Fireworks) lists Muse Spark.

## Capture gaps

- **All numbers are vendor-run or vendor-selected**; Meta's stated policy of taking the highest available figure per model from any of three sources makes the third-party columns a mix of Meta runs, leaderboards, and model cards.
- No pricing, context-window, output-limit, or knowledge-cutoff figures anywhere in the post or the PDF.
- Four worked-example outputs (a CFD report, an audio-edit report, a slide deck, a constituent-feedback summary) are images of first pages only; the prompts were captured in full.
- The three coding demos ("Psychic Storm," "Stimm Tuner," "Startup City 3D") and the agent-prototype video are embedded players and did not survive extraction.
- "Max reasoning" was not available at capture time, so the headline column could not be checked against the product.
- The methodology PDF (saved) names the harnesses but publishes no per-benchmark numbers of its own.
