---
layout: post
title: "This Week in AI — September 15, 2026"
date: 2026-09-15
description: "Anthropic proposes slowing frontier AI development, OpenAI pauses new Pro 20x subscriptions, and OpenCode reaches version 2.0.3."
tags: [model-news, weekly]
---

Despite calls for an AI slowdown, I just can't see it happening. I worry that this is insincere and actually the start of regulatory capture to lock out open weight models. 

That being said,I do think outside evaluation is meaningful. Hopefully that ends up being the main takeaway.

## Amodei calls for slower AI development and outside evaluators

Dario Amodei published a proposal on September 12 to slow the growth of frontier AI capabilities and give safety work time to catch up.

**From Amodei's essay:** Anthropic commits to embedding outside evaluators with continuing access comparable to its internal risk-assessment staff. The proposal gives reviewers the right to publish findings, subject to specified redactions. Broader coordination among companies and governments remains a proposal.

**Amodei's assessment:** AI's growing ability to help build subsequent models is accelerating progress. He warns that more capable agent swarms could cause catastrophic damage within 6–12 months. That is his forecast, not an observed capability.

The concrete step to watch is whether outside evaluators receive the promised access. The essay announces a commitment; it does not establish that the reviewers are already embedded or that an industry-wide slowdown has begun.

This follows the incidents covered in the September 5 timeline. Amodei explicitly cites the Hugging Face intrusion and acknowledges operational failures involving training environments. 

It also comes on the heals of rumours that Google has reached RSI with DeepMind.

**More info:**

- [**We Must Pace the Frontier** (Dario Amodei, Sep 12)](https://darioamodei.com/post/we-must-pace-the-frontier) — the proposal, Anthropic's evaluator commitment, and the limits of the proposed coordination.
- [Anthropic CEO says safety measures need time to catch up (AP, Sep 12)](https://apnews.com/article/d59552edcb27892d8ee4d98a48397706) — contemporary coverage establishing the publication date.
- [Rogue Agents: A Timeline From the Hugging Face Incident Onwards (Sep 05)]({{ "/2026/09/05/rogue-agents-a-timeline.html" | relative_url }}) — the earlier incident timeline this proposal follows.

## OpenAI pauses new Pro 20x subscriptions as Astra strains capacity

OpenAI paused new subscriptions and upgrades to its $200 ChatGPT Pro plan on September 10.

**From OpenAI's help center:** the pause covers new purchases and upgrades from Free, Go, Plus, and Pro $100. Existing Pro $200 subscriptions remain active. New and existing Pro $100 subscriptions are unaffected.

There is a practical catch for existing subscribers: once a cancellation or downgrade takes effect and Pro $200 access ends, they cannot buy back in until the pause lifts. A scheduled change can be undone before the billing cycle ends.

**OpenAI's explanation:** Tibo Sottiaux attributes the pause to demand for Astra and the strain the $200 tier puts on infrastructure. His announcement says other plans and the API remain available while OpenAI adds capacity. It gives no reopening date or capacity figures.

Honestly this is pretty frustrating given the way Astra can chew through tokens. I pretty much ONLY use my ChatGPT account for Astra in codex at this point.

**More info:**

- [**About ChatGPT Pro tiers** (OpenAI Help Center)](https://help.openai.com/en/articles/9793128-what-is-chatgpt-pro/) — dates the pause September 10 and explains its scope, cancellations, and upgrades.
- [Tibo Sottiaux's announcement (Sep 10)](https://x.com/thsottiaux/status/2098113585683808624) — OpenAI's capacity explanation; [a mirror of the announcement](https://zamantika.com/de/thsottiaux/status/2098113585683808624) supplied the text because X did not load during research.
- [Astra Lands, Qwen Refreshes Max, and What September Still Holds (Sep 04)]({{ "/2026/09/04/astra-lands-qwen-refreshes-max.html" | relative_url }}) — the launch assessment this follows up on.

## OpenCode 2 reaches version 2.0.3 as a release nears.

OpenCode v2.0.3 was released on September 12 with changes to the way the command line is called. It's taken back the `opencode` command and installs over top of OpenCode V1.

This simplifies running the new version and is a welcome change. I have been running it for a while now without issue but the setup was cumbersome.

Now you can just install it using the `/v2` branch:

```bash
curl -fsSL https://opencode.ai/v2/install | bash
```

**More info:**

- [**OpenCode 2 Docs**](https://opencode.ai/v2/docs)
- [**OpenCode v2.0.3** (GitHub)](https://github.com/anomalyco/opencode/releases/tag/v2.0.3) — the version tag; no detailed release notes were available during research.
- [OpenCode changelog](https://opencode.ai/changelog) — the separately maintained 1.x release history.

## What I'm actually using

I've moved most thinking work to Astra this week and I am driving inside of Claude Code. I use Fable inside of Claude Code for certain reviews and architecture tasks, delegating all other work to Opus and Sonnet. By splitting effort between a Claude Max and OpenAI Pro subscription I am able to get by without paying for additional tokens. 

If you're pushing a lot of tokens (1B+), OpenCode and OpenRouter are still the best bet. But I would keep subscriptions for use with the heavier frontier models.
