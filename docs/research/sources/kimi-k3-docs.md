---
title: "Introducing Kimi K3 (platform docs)"
slug: kimi-k3-docs
type: source
source_url: null
source_date: null
author: "Kimi (Moonshot AI)"
captured_at: 2026-07-15
last_source_check: 2026-07-15
raw_path: research/raw/2026-07-15/kimi-k3-docs/
previous_captures: []
static: false
tags: [kimi, kimi-k3, open-weights, moe, model-release, vision]
---

# Introducing Kimi K3 (platform docs)

_Kimi's own K3 platform docs, pasted by the user 2026-07-15. Vendor marketing + API facts — the self-descriptive "firsts" and scale claims need independent verification before publishing; there are no benchmark or pricing numbers here._

## What Kimi says it is

> Kimi K3 is Kimi's most capable flagship model to date, with **2.8 trillion parameters**… built on **Kimi Delta Attention (KDA)**, a hybrid linear attention mechanism, and **Attention Residuals**, with **native visual understanding** and a **1M-token context window**. It is **the world's first open-source model in the 3-trillion-parameter class**.

## Facts (from the docs)

- **Scale / architecture:** 2.8T total parameters, **Mixture-of-Experts** activating **16 of 896 experts** ("Stable LatentMoE") — so active params per token are a small fraction of 2.8T. KDA + Attention Residuals; Kimi claims ~**2.5× the scaling efficiency of K2**. (Vendor claim.)
- **"First / frontier scale":** Kimi claims the first open-source model to reach 2.8T, and that "in 9 of the past 12 months (2025/07–2026/07)" its models held the open-source scale frontier. **Marketing claim — verify.**
- **Context / vision:** 1M-token context window; native vision (images + video).
- **Release timing:** an **announcement** — "full model weights will be released by **July 27, 2026**"; benchmarks + a technical report still to come. API available now.
- **API:** OpenAI-compatible; model id `kimi-k3`, base URL `https://api.moonshot.ai/v1`. Thinking always on via `reasoning_effort` (only `max` for now). Streaming splits `reasoning_content` from `content`. Structured output, partial mode, tool calling, dynamic tool loading, 1M context with automatic caching.
- **Limits:** `max_completion_tokens` default 131072, up to 1048576; sampling params fixed (`temperature=1.0`, `top_p=0.95`, …) and must be omitted.
- **Pricing shape:** flat pay-as-you-go, **no tiering by context length**; input (separate cache-hit / cache-miss rates) + output at uniform per-token prices. **No actual numbers in the source.**
- **Strengths (Kimi's framing):** long-horizon coding, coding+vision (game dev / frontend / CAD), agentic knowledge work — partly on *internal* evals.

## Capture gaps

- **Provenance:** user paste, not a fetched capture; canonical URL not verified (`source_url: null`). The technical blog (`kimi.com/blog/kimi-k3`) was **unreachable** at capture time, so the **benchmarks and case studies live there, uncaptured**.
- **No numbers:** no benchmark scores and no per-token pricing in this source — both flagged as TBD for the Kimi K3 draft.
- `static: false` — a pre-release doc that will change once weights ship (July 27, 2026); re-check then.
