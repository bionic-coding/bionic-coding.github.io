---
layout: post
title: "Running Qwen3.8-27B. Locally"
date: 2026-08-16
description: "[AUTHOR: one scannable sentence — what the piece is: running the 27B multimodal Qwen locally across Q8/Q6/Q4, and what it costs in RAM.]"
tags: [local-models, qwen]
---

Qwen3.8 a 27B multimodal model that runs on a laptop. In my testing I was typically getting more than 20 tok/sec which felt fast enough for development. 

It seemed impressive for the size. Full details below.

## About Qwen3.8-27B 

Qwen3.8-27B is a dense, multimodal model that Alibaba's Qwen team released two days ago:

- **27.8B parameters:** dense (not a mixture-of-experts).
- **262,144-token native context:** extensible toward 1M.
- **Multimodal:** image/text to text.

## Fitting Qwen3.8-27B onto a laptop

I ran three quantizations locally Q8, Q6, and Q4 along with varying context windows.

At **Q8 with the full context window, it needed ~77 GB of RAM**. 
To make it fit on my laptop, I dropped the context window to **68k tokens**, which brought it inside 48 GB.

| Quant | Context | RAM est. | RAM used by model | Runs inside 48 GB |
| --- | --- | --- | --- | --- |
| Q8 | max (262k) | 76.69 GB | 47.03 GB | No |
| Q8 | 68k | 43.30 GB | 34.42 GB | Yes |
| Q6 | max (262k) | 59.77 GB | 40.86 GB | No |
| Q6 | 132k | 42.33 GB | 32.41 GB | Yes |
| Q4 | max (262k) | 45.41 GB | 35.62 GB | Yes, barely ;) |

On a set of sample problems the Q8 would sometimes produce two solutions and then select either the most efficient or the most readable option. In several runs it used both a recursive function and an Enum.reduce as proposed solutions.

## My thoughts so far

After using it for about an hour I think that the Q8 is good enough for many standard coding tasks. I wouldn't run it without another smarter model guiding it and reviewing the output, but that's exactly how I'm currently running Claude Sonnet. 

If I was trying to work offline for a week, this would be my primary coding model.

You need a bunch of RAM to get enough context to do useful work, so keep that in mind.

## References

- [Qwen/Qwen3.8-27B on HuggingFace](https://huggingface.co/Qwen/Qwen3.8-27B) - the model card and weights.
- [Qwen/Qwen3.8-27B on GitHub](https://github.com/AlibabaCloud-Official/Qwen3.8-27B) - note that it was shared from Alibaba Cloud and not [QwenLM](https://github.com/QwenLM) just like Qwen3.8 Max.
