---
layout: post
title: "This Week in AI — August 14, 2026"
date: 2026-08-14
description: "Qwen3.8 Max lands on Fireworks.ai, Deepseek 4 ships, GLM5.3 arrives with weights promised, plus what running Qwen 3.8 Max and Kimi K3 is actually like."
tags: [model-news, weekly]
---

Open weight models appear poised to take over as the costs of closed weight models keep increasing largely due to model verbosity at this point.

## Qwen 3.8 Max lands as open weights

Qwen3.8 Max is now available as open weights. (I am using Fireworks.ai to access it.)

I've had about a day with it and it seems very capable. The way it talks to itself in its reasoning logs bothers me a little bit. There's too much "actually", "wait" and "hmm" for my liking. But I was happy with the results. 

**More info:**
- [Qwen3.8-2.4T-A95B on Hugging Face](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Qwen3.8 Max on Fireworks](https://fireworks.ai/models/fireworks/qwen3p8-max)

## Deepseek V4 Pro 0813

Deepseek released Deepseek V4 Pro 0813.

From the description:
> DeepSeek-V4-Pro-0813 is the official release of DeepSeek-V4-Pro, superseding the preview version, with greatly enhanced agentic capabilities and performance improvements that are especially pronounced in production environments. It is built on the DeepSeek-V4-Pro (Preview) model structure, with a DSpark speculative decoding module attached.

**More info:**
- [DeepSeek-V4-Pro-0813 on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
- [DeepSeek-V4-Pro-0813 on Fireworks](https://fireworks.ai/models/deepseek-ai/deepseek-v4-pro-0813)

## GLM5.3
GLM5.3 from Z.ai is out, with weights promised in the next two weeks.

It claims to be stronger for coding that previous iterations and appears to land amongst the top models on the leaderboard on various benchmarks.

I will definetely give it a try once the weights are released.

Right now it's only available in their [ZCode](https://zcode.z.ai/en) or a subscription and not on the API.

**More info:**
- [Z.AI GLM5.3](https://z.ai/blog/glm-5.3)

## What I'm actually using
I've been running Kimi K3 + Opencode as my primary driver this week while calling into other models for coding tasks.

It is every bit as capable as Claude Opus 4.8 and Claude Code with my crux tooling.
