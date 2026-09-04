---
layout: post
title: "Astra Lands, Qwen Refreshes Max, and What September Still Holds"
date: 2026-09-04
description: "OpenAI's GPT-6 Astra ships with impressive results, Alibaba's Qwen3.8-Max-0902 doubles its terminal scores at the same $2 / $6 with no new weights, and what to expect for the rest of September."
tags: [model-news]
---

Yesterday OpenAI released GPT-6 Astra following on the heels of the Fable 5.1 release from Anthropic. After working with both it's very clear that Astra is significantly ahead of Fable. (And I thought Fable 5.1 was a clear step up from the original Fable 5.0)

When I use a model like Fable or Astra I am not delegating specific tasks to it - they are slotted in to run a graph of agents. (Those agents themselves manage a team of agents...)

This flow requires the Apex Model to manage planning, coordination and delegation.

I had stopped using Fable a month ago because the results were not worth the token costs. Astra is both more efficient and more effective.


## GPT-6 Astra: Fable 5.1's price and a Critical cyber rating

OpenAI released GPT-6 Astra on September 3, one model with one name, above the GPT-5.6 family, and started a staged rollout that as of today has not reached most developers.

**From OpenAI's model page:** $10 in and $50 out per million tokens, the same list price as Claude Fable 5.1. Cache reads are $1, four times Fable 5.1's $0.25. Requests over 272K input tokens are billed at double the input rate and 1.5x the output rate for the whole request, a surcharge Anthropic does not levy. Context is 1,050,000 tokens, output 128K, knowledge cutoff April 30, 2026. Reasoning is always on: the effort ladder runs low to max with no "none" setting. No fine-tuning.

**OpenAI's benchmark claims:** Astra leads where computer use, cyber, or long context is measured. Terminal-Bench 4.0 is 57.9 to Fable 5.1's 55.8. It does not sweep. Fable 5.1 leads the Artificial Analysis Intelligence Index 65.7 to 61.2, and Opus 5 leads the Coding Agent Index 68.1 to 67.0. The ARC-AGI-3 headline of 99.9% carries a footnote: OpenAI ran it "with our responses API harness, which changes two settings." Two of the Fable 5.1 cells are Mythos numbers, per OpenAI's own footnote.

**The Cyber story:** Astra is the first model OpenAI rates Critical under its Preparedness Framework, the level above GPT-5.6's High. OpenAI says it found and used two previously unknown zero-days during testing. What ships is narrower than what was tested: the launch model refuses to write proof-of-concept exploits, allows code review and patching, and the looser version goes to vetted defenders through a program called Daybreak.

**One product behavior worth knowing before you build on it:** OpenAI documents that Astra's misalignment monitoring "can sometimes slow, pause, or stop legitimate work," including work unrelated to cyber. In ChatGPT and Codex a paused task asks you to review. In the API, the task stops.

I have been nothing but impressed by Astra.

**More info:**
- [**GPT-6 Astra: A new generation of intelligence** (OpenAI, Sep 03)](https://openai.com/index/gpt-6-astra/) — the launch post, benchmark tables, and the footnotes above.
- [GPT-6 Astra model page (Sep 03)](https://developers.openai.com/api/docs/models/gpt-6-astra) — pricing, context, the 272K surcharge, and the effort ladder; the source for everything marked verified.
- [The path to Astra (OpenAI, Sep 01)](https://openai.com/index/path-to-astra/) — the Critical designation, the two-week training pause, and the Daybreak program.
- [OpenAI announces rollout of GPT-6 Astra (CNBC, Sep 03)](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html) — the phased-rollout wording.

## Qwen3.8-Max-0902: same model, same price, twice the terminal score

Alibaba released Qwen3.8-Max-0902 on September 2, a post-training refresh of the 2.4T Qwen3.8-Max at the same $2 in and $6 out, aimed at long coding runs, multi-tool agent work, and document vision.

**From the QwenCloud page:** the architecture is unchanged, 2.4 trillion total parameters with 95B active, and the context stays at 1M tokens with 128K output. The model id is `qwen3.8-max-0902`. It is an API checkpoint. There is no new Hugging Face repository for it.

**From Alibaba's own numbers:** the biggest jumps are on Terminal-Bench 3.0, from 11.3 to 29.0, and ProgramBench Almost Solved, from 10.5 to 28.0. It ranks first on Code Arena WebDev at 1,691. On SWE-bench Pro it scores 67.7, behind Fable 5 at 80.0 and Opus 4.8 at 69.2, ahead of GPT-5.6 Sol at 64.6. The coverage calling this "matches Fable 5" is reading the WebDev arena row and skipping the SWE-bench Pro row.

**What changes for OpenRouter users:** the qwen/qwen3.8-max listing on OpenRouter switches to the 0902 checkpoint on Saturday, September 5. Hopefully they release the weights so that other providers can serve a Qwen3.8-Max-0902 API endpoint from the US.

Qwen3.8 Max is probably my favorite open weight model for coordinating AI agents right now. I very much look forward to the Qwen3.8-Max-0902 release.

**More info:**
- [**Qwen3.8-Max-0902** (QwenCloud model page, Sep 02)](https://www.qwencloud.com/models/qwen3.8-max-0902) — specs, pricing, the model id.
- [QwenCloud model releases changelog](https://docs.qwencloud.com/changelog/models) — the dated entry for the 0902 checkpoint.
- [qwen/qwen3.8-max on OpenRouter](https://openrouter.ai/qwen/qwen3.8-max) — the listing that switches checkpoints.
- [Qwen/Qwen3.8-2.4T-A95B on Hugging Face (Aug 12)](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) — the weights you can actually download.

## What's still coming in September, sorted by how much I believe it

Release-date lists are circulating. Most of the dates on them have no source. Here is each item with what the vendor has actually said.

**Grok 4.7, around September 12. Vendor-stated.** Elon Musk posted on September 2 that "Grok 4.7 comes out in 10 days," claiming 2.1 trillion parameters, up from 4.6's 1.5T, and training on SpaceX engineering data. That is the only upcoming release with a date from the company. Nothing else is published: no model id, no price, no context window. Expect it to show up in Cursor first, since SpaceX closed its purchase of Cursor on August 15.

**Claude Opus 5.1 and Sonnet 5.1. Leaked strings, nothing from Anthropic.** Two early-access model ids, `claude-marshmallow-eap` and `claude-melon-eap`, appeared in third-party apps around August 24. Testers say marshmallow beats Opus 5. The "5.1" names are a guess, and not confirmed. No date has been stated by anyone with standing to state one.

**Qwen 4.** The next major version is Qwen 4. What Alibaba has confirmed is that Qwen3.8-Flash-Next, released August 28, previews the Qwen 4 architecture. The rumored venue is the Apsara Conference in Hangzhou, September 22 to 24, where Alibaba announced Qwen 2.5 in 2024 and the Qwen3-Max family in 2025. Alibaba has not confirmed a date.

**Kimi K3.1. Rumor.** The only source is an unverified July 26 post on X listing "faster inference" and "better token efficiency" with no numbers, no card, and no date. Moonshot has said nothing since K3 shipped in July. If it lands this month it will be a surprise to the people who track Moonshot closely, not a scheduled event. I've heard people talk about K3.5 but I've seen nothing to back it up yet.

This feels like an acceleration. I can't remember a single month with so many new model releases that I care about. 

**More info:**
- [**Elon Musk: "Grok 4.7 comes out in 10 days"** (X, Sep 02)](https://x.com/elonmusk/status/2094983639780204846) — the one vendor-stated date.
- [SpaceX officially closes its Cursor acquisition (TechCrunch, Aug 15)](https://techcrunch.com/2026/08/15/spacex-officially-closes-its-cursor-acquisition/) — why "Cursor Grok" is a thing.
- [Claude Marshmallow and Melon leaks (Times of AI, Aug 25)](https://www.timesofai.com/news/claude-opus-5-1-marshmallow-melon-leaks/) — the leaked strings and what testers reported.
- [Kimi K3.1 leak: rumored vs confirmed (OrcaRouter)](https://www.orcarouter.ai/blog/kimi-k3-1-leak) — traces the K3.1 rumor to its single source.
- [Alibaba releases Qwen3.8-Flash-Next (The Decoder, Aug 28)](https://the-decoder.com/alibaba-releases-qwen3-8-flash-next-targeting-ultimate-cost-efficiency/) — Alibaba's own "preview of Qwen 4" framing.
- [Qwen 4: what's confirmed (Yotta Labs)](https://www.yottalabs.ai/post/qwen-4-release-date-what-is-known-how-to-prepare-2026) — the Apsara Conference dates and the state of the rumor.

## What I'm actually using

I worked with Fable 5.1 for a day - it was lackluster for the pricing. I'm still using Astra and suspect it will stay as my Apex Model. I will try Qwen 3.8 Max 0902 as soon as it's available.
