---
layout: post
title: "Running Qwen3.8-27B locally"
date: 2026-08-16
description: "[AUTHOR: one scannable sentence — what the piece is: running the 27B multimodal Qwen locally across Q8/Q6/Q4, and what it costs in RAM.]"
tags: [local-models, qwen]
---

<!--
  DRAFT SCAFFOLD — not ready to publish.
  Filled in by Claude: verified model specs (from the HuggingFace card) and your own
  RAM measurements. Left for you: every [AUTHOR: ...] block — these are judgment calls
  and impressions only you can make. Move to _posts/YYYY-MM-DD-slug.md when the prose is yours.
  .
  Verify each spec against the model card before publishing; numbers below are from the
  Qwen/Qwen3.8-27B card, not my own testing.
-->

[AUTHOR: lede — a sentence or two on why you tried this one. It's a 27B model that runs on a laptop, and it's multimodal. Set up the "how much machine does it actually need" question the rest of the post answers.]

## What it is

Qwen3.8-27B is a dense, multimodal (image-text-to-text) model that Alibaba's Qwen team released in August 2026 under Apache 2.0. The specs worth knowing before you download a 27B model:

- **27.8B parameters**, dense (not a mixture-of-experts).
- **262,144-token native context**, extensible toward 1M.
- **Multimodal**: it takes text and images.

*Verify these against the [model card](https://huggingface.co/Qwen/Qwen3.8-27B) before you rely on them — they're from the card, not from my own testing.*

## What it costs in RAM

I ran three quantizations locally: Q8, Q6, and Q4. The one number that decides whether this fits your machine is context window, not just the weights.

At **Q8 with the full context window, it needed ~76 GB of RAM** — more than my 48 GB laptop has. To make it fit, I dropped the context window to **80k tokens**, which brought it inside 48 GB.

| Quant | Context window | RAM used | Fit in 48 GB? |
| --- | --- | --- | --- |
| Q8 | max (262k) | ~76 GB | No |
| Q8 | 80k | [AUTHOR: measured RAM] | Yes |
| Q6 | [AUTHOR: window] | [AUTHOR: measured RAM] | [AUTHOR] |
| Q4 | [AUTHOR: window] | [AUTHOR: measured RAM] | [AUTHOR] |

[AUTHOR: the takeaway readers came for — the context window is the RAM knob, not just the quant. Say how far you had to turn it down and whether that hurt.]

## How the quants held up

[AUTHOR: this is the part only you can write — did Q6 or Q4 noticeably degrade the outputs versus Q8? On what kind of task did you notice, and where didn't it matter? This is the first-hand judgment that makes the post worth reading; don't let me guess it.]

## What I'm using it for

[AUTHOR: the honest verdict. Is a laptop-sized 27B multimodal model good enough to keep in your kit, or a curiosity? What task, if any, did it earn a place in?]

## References

- [Qwen/Qwen3.8-27B on HuggingFace](https://huggingface.co/Qwen/Qwen3.8-27B) — the model card and weights.
- [QwenLM on GitHub](https://github.com/QwenLM) — Qwen's official code org.
