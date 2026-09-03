---
layout: post
title: "This Week in AI — September 3, 2026"
date: 2026-09-03
description: "Claude Fable 5.1 ships at the same price, Google's Gemini 3.8 Flash undercuts closed models at $0.75 a million tokens, Meta's Muse Spark 1.3 arrives with open weights promised, GLM-5.3 and two new Flash-class open models land, and closed-model prices went down, not up."
tags: [model-news, weekly]
---

It's been a busy week with releases from Anthropic, Meta, and Google. (My understanding is that we should expect news from OpenAI soon too - though slightly delayed because of the Hugging Face incident.)

## Claude Fable 5.1: same price, cheaper cache, and a watermark on everything

Anthropic released Claude Fable 5.1 on September 1 at Fable 5's price, $10 in and $50 out per million tokens, with cache reads cut to a quarter.

**Verified, from Anthropic's own docs:** the price held. Cache reads dropped from $1.00 to $0.25 per million tokens, a quarter of Fable 5's rate and half of Opus 5's. Context is 1M tokens, output 128K, knowledge cutoff June 2026. Anthropic's own routing advice is blunt: "start with Claude Opus 5," and reach for Fable 5.1 when Opus at higher effort still falls short.

**Claimed, no numbers:** gains over Fable 5 "widest at higher effort levels" in long-session agentic coding, document and spreadsheet work, multistep research, and vision on dense PDFs. There is no benchmark table in any of the three docs pages. The system card exists but I haven't read it yet.

**Three things that break if you build on the API yourself:** forced tool use returns an error, thinking blocks are readable only by 5.1 or newer, and the conversation history must be append-only. Claude Code, claude.ai, and the Agent SDK handle all three for you, so the popular "Fable 5.1 broke my setup" reading only applies to people assembling the messages array by hand.

**Oh, and don't forget the Watermark:** every text output from Fable 5.1 carries Anthropic's statistical watermark, on every platform. Anthropic says it adds no tokens or hidden characters and carries nothing about you. Anthropic also documents, against its own model, that 5.1 is "more likely to reproduce passages of the source without marking them as quotations" when summarizing.

From my usage this week, so far so good. It definetly feels like a step up from Fable 5.0 which I stopped using because
the output didn't justify the premium pricing.

**More info:**
- [**Claude Fable 5.1 overview** (Anthropic docs)](https://platform.claude.com/docs/en/models/fable-5-1/overview) — specs, pricing, lineup table; the primary source for everything above.
- [What's new in Fable 5.1 (Sep 01)](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1) — the three breaking changes, the watermark, and Anthropic's list of behavior differences from Fable 5.
- [Migration guide (Sep 01)](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide) — the append-only history rule and how to check your integration for it.

## Gemini 3.8 Flash: $0.75 a million tokens, with an asterisk

Google shipped Gemini 3.8 Flash and a defenders-only Gemini 3.8 Flash Cyber on September 2, its third Flash release in six weeks.

**Verified, from Google's pricing page:** $0.75 in and $3.75 out per million tokens, the same as 3.7 Flash. The asterisk is on the pricing page too: that is an introductory price for both models, and on January 1, 2027 it doubles to $1.50 and $7.50.

**Claimed, Google's own table:** 3.8 Flash leads 8 of 14 rows against Opus 5, Sonnet 5, and GPT-5.6 Sol and Terra, mostly by under two points. On DeepSWE, the long-horizon coding benchmark, it scores 73.7% to Opus 5's 74.0% at roughly a sixth of the cost per task. Where the table measures general agency, Opus 5 wins by a mile: Terminal-Bench 4.0 is 51.8% to 19.1%, OSWorld is 75.4% to 59.0%. Google's own phrasing, "often approaching the performance of higher-cost frontier models," is the honest reading of its own table.

**The popular misread to head off:** cheap per token is not cheap per task. Google says 3.8 Flash "works harder," runs more reasoning steps and tool calls, and "might use more tokens," and it points cost-sensitive developers back to 3.7 Flash. That is the verbosity problem from the August 14 issue, now stated by the vendor.

**Flash Cyber** is the same base model with looser cyber mitigations, available only through Google's new Fairwind Program for governments, critical-infrastructure operators, and software maintainers. Google says it prioritized patching over exploitation; the one external number is CWE-Bench patching at 47.2% against an unnamed leader's 47.8%.

This all sounds promising but it's so much more expensive thatn GLM 5.3 Flash that I am not even sure I want to even try it.

**More info:**
- [**Introducing Gemini 3.8 Flash and 3.8 Flash Cyber** (Google, Sep 02)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) — the launch post; the comparison table is an image.
- [Gemini API pricing (Sep 03)](https://ai.google.dev/gemini-api/docs/pricing) — where the December 31 expiry and the 2027 price live.

## Meta's Muse Spark 1.3, and which Muse you can actually download

Meta released Muse Spark 1.3 on September 2, a closed model you get only through Muse Code and the Meta Model API, and said open weights for Spark are on the roadmap.

**The naming, settled:** Muse Glimmer is the open one, a 30B Apache 2.0 model Meta released in August that runs in under 20 GB on a 24 GB or 32 GB machine. Muse Spark is the closed teacher it was distilled from. Coverage last month conflated the two. This week's post is the first place Meta says in its own words that Spark itself will get an open-weights release, with no version and no date.

**Claimed, Meta's scorecard:** Spark 1.3 leads Opus 5 and GPT-5.6 Sol on all three coding rows (DeepSWE 75.4 to Opus 5's 74.0, Terminal-Bench 2.1 tied with Sol at 88.8) and both long-context rows (98.5 and 98.1 on MRCR, where Opus 5 has no entry), and trails Opus 5 on five of six agent rows by under two points. Meta's methodology note says it reports, for each model, the highest figure available from its own runs, official leaderboards, or the vendor's card. The headline column is "max" reasoning, a mode that was not yet shipping on launch day.

**Cross-checked:** Meta's and Google's tables, published the same day, agree on Opus 5's DeepSWE (74.0) and GDPVal (1824). Two vendors independently landing on the same competitor number is the closest thing to verification this week has.

**Behavior claims, unverified but worth quoting:** asks clarifying questions when a prompt is ambiguous, "confirms before taking consequential actions," and used about 20% fewer tool calls and 25% fewer tokens than 1.2 in Meta's internal coding comparisons. No pricing anywhere in the post.

Meta and Goolge have been at the back of the pack for a while. I'm hoping this means we are going to start seeing them catch up.

**More info:**
- [**Introducing Muse Spark 1.3** (Meta, Sep 02)](https://research.meta.ai/blog/introducing-muse-spark-1-3) — the launch post and scorecard.
- [Introducing Muse Glimmer (Meta, Aug 10)](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) — the open-weights 30B model; the one you can download today.

## The open Flash tier: GLM-5.3 weights landed, and two 15-cent models arrived

Z.ai shipped the GLM-5.3 weights on August 25, then a new GLM-5.3 Flash on August 26, the same day Alibaba released Qwen3.8 Flash. Both Flash models list at about $0.15 in and $0.50 out.

**Verified, from the repositories:** GLM-5.3 Flash is a new 320B-total, 18B-active model under a plain **MIT** license with a 1,048,576-token context. The full GLM-5.3, the model the August 14 issue said was coming with weights "in the next two weeks," did land, but under a custom "GLM-5.3 License," not MIT: MIT-shaped, with a security-review clause for very large model-as-a-service operators. Qwen3.8 Flash's weights are on Hugging Face under Alibaba's custom license.

**Verified, from OpenRouter on September 1:** GLM-5.3 Flash lists at $0.15 / $0.50 and is half that through September 9. Qwen3.8 Flash lists at $0.15 / $0.47. The full GLM-5.3 is $1.40 / $4.40. Hermes Agent alone pushed 1.38 trillion tokens through GLM-5.3 Flash in its first week; every top app on these pages is a coding agent.

**Claimed, Z.ai's table:** GLM-5.3 Flash beats Opus 4.8 on four of eight coding and agentic rows and trails on four. Note the comparison is Opus 4.8, not Opus 5. Z.ai also says the whole launch week was served on Chinese AI chips at per-token cost "comparable to mainstream NVIDIA GPUs," single-source and unaudited, and the first open-weights launch this year to make the hardware the story.

**What the evidence shows:**
- [GLM-5.3-Flash `LICENSE` on Hugging Face](https://huggingface.co/zai-org/GLM-5.3-Flash) is MIT; the repo's `config.json` gives the 1,048,576 context and the 34 linear + 11 sparse attention layers Z.ai describes.
- OpenRouter's API record, not the page, is the price source: [GLM 5.3 Flash](https://openrouter.ai/z-ai/glm-5.3-flash) and [Qwen3.8 Flash](https://openrouter.ai/qwen/qwen3.8-flash).
- GLM-5.3 Flash's self-reported DeepSWE score (63.4) matches its position on Google's DeepSWE cost chart in the Gemini post above.

I am using GLM-5.3 Flash for my coding tasks. I have a larger model review the work. So far, it's been a great experience.

**More info:**
- [**GLM-5.3-Flash launch post** (Z.ai, Aug 26)](https://z.ai/blog/glm-5.3-flash) — the vendor table and the Chinese-chips claim; the page is a JavaScript app, so it may not load without scripts.
- [zai-org/GLM-5.3-Flash on Hugging Face (Aug 25)](https://huggingface.co/zai-org/GLM-5.3-Flash) — weights, MIT license, config.
- [GLM-5.3 launch post (Z.ai, Aug 14)](https://z.ai/blog/glm-5.3) — the original "weights in two weeks" promise, now kept.

## Correction: closed-model prices went down

Every closed-model price recorded on this site since July has held or fallen. The August 14 issue said the opposite.

**Pricing changes for closed models:**
- Anthropic launched Opus 5 at Opus 4.8's price, $5 / $25 (July 24).
- Anthropic cancelled the scheduled Sonnet 5 increase to $3 / $15; $2 / $10 is now the standard price (August 10).
- Anthropic held Fable 5.1 at $10 / $50 and cut cache reads to $0.25 (September 1).
- OpenAI's pricing page now lists GPT-5.6 Sol at $4 / $20, down from the $5 / $30 from July, labeled promotional "at least through November 21, 2026." Terra and Luna are lower too, with no promotional label.
- Google launched Gemini 3.8 Flash at 3.7 Flash's $0.75 / $3.75 (September 2).

**The honest asterisk:** two of the five have expiry dates on the page (OpenAI November 21, Google December 31), and the open-model discount on GLM-5.3 Flash ends September 9. The only scheduled price increases anywhere this week are promotions ending. And per-token price is only half the bill: Google itself says its new model uses more tokens per task.

Honestly, I don't think they have a choice. Good open models are driving prices down. 

**More info:**
- [**Claude Platform release notes**, Aug 10 entry](https://platform.claude.com/docs/en/release-notes/overview) — the Sonnet 5 increase "will not occur."
- [OpenAI API pricing (Sep 03)](https://platform.openai.com/docs/pricing) — Sol $4 / $20 and the November 21 promotional note.

## What I'm actually using

These days I am running Fable 5.1 for planning and research. It's expensive to pay for tokens so I am using a Max plan.
Crux allows me to flip between Claude Code and Opencode2 easily so I will often plan in Claude Code and then switch to Opencode2 for execution.

When running coding tasks I will drive with Qwen3.8 2.4T A95B (1M) and run several subagents where the supervisor is GLM 5.3 but the code is written by GLM 5.3 Flash.
