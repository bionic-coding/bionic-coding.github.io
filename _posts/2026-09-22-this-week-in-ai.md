---
layout: post
title: "This Week in AI — September 22, 2026"
date: 2026-09-22
description: "So many models: Anthropic releases Opus 5.5, OpenAI adds GPT-6 Sol and Luna, Xiaomi opens MiMo-V2.6 weights..."
---

Last week I wrote about calls to slow frontier AI development. This week brings new models from Anthropic, OpenAI, and Xiaomi, with lower prices across much of the lineup. I'm also interested in two smaller stories about how we put these models to work: giving agents better feedback, and putting bounded AI decisions inside ordinary software.

## Anthropic releases Claude Opus 5.5

Anthropic released Opus 5.5 today, with access through its API and Pro, Max, Team, and Enterprise plans.

Standard API pricing is $4 per million input tokens and $20 per million output tokens, down 20% from Opus 5. Cache reads drop from $0.50 to $0.20. Anthropic's larger claim of 40% lower running costs comes from its tests of typical workloads at default settings. That is different from a 40% reduction in token prices.

**From Anthropic's release:** Opus 5.5 scores 66.4% on Terminal-Bench 4.0, up from Opus 5's 52.3%. Cursor's separately run CursorBench 4.0 result rises from 46.6% to 57.8%. Anthropic also cautions that benchmark margins overstate the difference it sees between Opus 5.5 and Fable 5.1 in everyday use.

The safety figures need the same care. The announcement reports roughly 85% fewer attempts to circumvent boundaries than Opus 5 or Mythos 5.1. That is a relative reduction. In the system card's containment test without safeguards, Opus 5.5 attempted to cross a boundary in 1.5% of cases. Anthropic rated those attempts low severity and says the model reported them afterwards.

A separate package-registry test without cyber safeguards still produced potentially harmful behavior in roughly half of cases. These are different evaluations, and neither is a measure of the failure rate in ordinary use.

The immediate benefit is a cheaper Opus with reported coding gains. The release gives me a reason to test it on familiar work; the benchmark table alone doesn't settle which model to use.

**More info:**

- [**Introducing Claude Opus 5.5** (Anthropic)](https://www.anthropic.com/claude-opus-5-5) — launch, pricing, benchmarks, and the caveat about real-world differences.
- [Claude Opus 5.5 System Card (Anthropic)](https://anthropic.com/claude-opus-5-5-system-card) — the containment and package-registry evaluations, including their test conditions.
- [Claude Opus product page](https://www.anthropic.com/claude/opus) — plan availability and API pricing.

## OpenAI adds GPT-6 Sol and GPT-6 Luna

OpenAI released GPT-6 Sol and Luna today as well, expanding the family below Astra.

OpenAI positions Sol for demanding reasoning and coding, and Luna for focused work at volume. Astra remains its most capable model. Both newcomers are available through the API, with these standard prices per million tokens:

| Model | Input | Cached input | Output |
| --- | ---: | ---: | ---: |
| GPT-6 Sol | $2 | $0.20 | $10 |
| GPT-6 Luna | $0.10 | $0.01 | $0.50 |

Both have a 1.05-million-token context window and a 128,000-token output limit. Requests exceeding 272,000 input tokens carry higher rates. Sol's base input and output prices are half Opus 5.5's; Luna's are one-twentieth of Sol's. The actual cost of finishing a task still depends on how many tokens and attempts it takes.

**OpenAI's benchmark results:** Sol at xhigh reasoning effort scores 33.2% on AutomationBench at $0.27 per task. Its comparison puts Astra at low effort at 30.3%, costing 3.9 times as much. That is a useful example of matching effort to a task, rather than evidence that Sol has overtaken Astra. The competitor comparisons use older Claude models, including Opus 5, so they don't settle a comparison with today's Opus 5.5.

**More info:**

- [**Introducing GPT-6 Sol and Luna** (OpenAI)](https://openai.com/index/introducing-gpt-6-sol-and-luna/) — rollout and vendor benchmark comparisons.
- [GPT-6 Sol model page](https://developers.openai.com/api/docs/models/gpt-6-sol) — pricing, limits, and supported tools.
- [GPT-6 Luna model page](https://developers.openai.com/api/docs/models/gpt-6-luna) — pricing and the same context and output limits.

## Xiaomi releases MiMo-V2.6 with open weights

Xiaomi announced MiMo-V2.6-Pro and Flash on September 22, alongside an UltraSpeed serving option for Pro.

The Hugging Face release includes Pro, Flash, and a distilled 9B model, with repository metadata listing MIT licenses. That gives people another option to run and adapt model weights themselves and DeepInfra has already released a hosted pro option.

Xiaomi and DeepInfra list Pro at $0.435 per million uncached input tokens and $0.87 per million output tokens. Flash costs $0.14 and $0.28 respectively. Those prices are unchanged from V2.5.

**Xiaomi's claim:** Pro is the strongest open-source model, with a 46.32 score on Artificial Analysis's Intelligence Index. The research capture of OpenRouter's benchmark page shows an Artificial Analysis score of 46.3, corroborating that number to one decimal place. It doesn't independently establish Xiaomi's broader ranking claim or reproduce the rest of its benchmark table.

Xiaomi also describes the release as progress toward recursive self-improvement. Its account describes reinforcement learning on complex tasks with checkable results. It does not demonstrate a model designing and training its own successor. That distinction carries into the next story.

**More info:**

- [**Introducing MiMo-V2.6 series** (Xiaomi)](https://mimo.xiaomi.com/mimo-v2-6) — models, training account, benchmarks, and API pricing.
- [MiMo-V2.6-Pro on OpenRouter](https://openrouter.ai/xiaomi/mimo-v2.6-pro#benchmarks) — model specifications and the Artificial Analysis results.
- [MiMo-V2.6 collection (Hugging Face)](https://huggingface.co/collections/XiaomiMiMo/mimo-v26) — the released model repositories.

## Z.ai Serving GLM with the help of GLM

Z.ai published an account on September 17 of a GLM-5.3-powered agent helping engineers build the serving system for GLM-5.3-Flash.

**Reported by Z.ai:** the system reached production in under two weeks, with roughly three times the throughput of its initial baseline. It serves the model on more than 100,000 Chinese-made accelerators. The account doesn't isolate how much of the gain came from the agent versus the engineers.

The useful part is how they gave the agent feedback. Correctness tests exposed numerical errors. Execution traces showed where work was waiting. Small benchmarks let it test an optimization before running the full system again. Engineers still chose the objectives, set boundaries, and reviewed consequential changes.

Z.ai explicitly says this has not reached recursive self-improvement. The related Dream-RSI paper uses that term for a narrower experiment: improving the code that chooses how an agent explores. The underlying models and evaluator stay fixed. Its replay system tests choices against recorded discovery branches, which limits what it can establish about unseen outcomes.

These accounts describe different kinds of improvement. The practical lesson I take from them is to give an agent tests that explain whether its latest change worked, and enough evidence to decide what to try next.

**More info:**

- [**How GLM Built Its Own Inference Infrastructure** (Z.ai)](https://z.ai/blog/glm-built-its-inference-infrastructure) — the engineering account and its explicit limit on the self-improvement claim.
- [Dream-RSI: Recursive Self-Improvement through Evolving Worlds (arXiv v1)](https://arxiv.org/html/2609.14858v1) — exploration-policy improvement using recorded discovery histories.

## TypeSafe introduces Jev: AI decisions without generated text

TypeSafe introduced Jev on September 15.

Jev accepts unstructured information and returns typed decisions with probabilities. You define the possible choices; ordinary code decides what happens next. That could mean classifying a request or flagging a document for review, while leaving calculation and control flow in software.

**TypeSafe's launch claims:** $0.042 per million input tokens, free output, and response times of 70–500 milliseconds. Its headline speed and cost comparisons come from four internally authored workflows. The reference answers average Astra and Fable probabilities rather than using established ground truth. Competitors also use an adapter that adds overhead to produce compatible probabilities.

The promise of an output that always fits a schema needs a separate caveat: a valid choice can still be wrong. TypeSafe acknowledges that its plotted 0% error rate follows from its schema guarantee, rather than an empirical accuracy result.

**In our own synthetic tests:** a single multiple-choice question correctly classified 16 of 20 cases comparing an architecture decision with its stated rules. Four separate yes/no judgments managed 10 of 20 on the same cases. These were agent-labeled synthetic cases, not a human-reviewed trial on real work. The result suggests that how we frame a decision matters enough to test explicitly.

**More info:**

- [**Introducing System One Models & Jev** (TypeSafe)](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — early access, pricing, and the company's evaluation caveats.
- [Composable AI manifesto and appendix (captured Sep 17)](https://typesafe.ai/manifesto#appendix) — the argument for putting bounded model decisions inside ordinary software.

## What I'm actually using

I am putting all of the new models through their paces right now so I am a bit hesitant to guess where I will actually land. Here are some thoughts on what you might want to consider testing out in your workflows.

If you are using Kimi K3, you might want to consider either MiMo-V2.6-Pro or GPT 6.0 Sol. Both should be a step up with a reduction in costs.

I am evaluating MiMo-V2.6-Pro as a replacement for Qwen 3.8 Max. I've problems with Qwen 3.8 Max recently and even the 0902 refresh doesn't seem to help.

Claude Opus 5.5 and GPT 6.0 Sol both look incredibly promising. I need to try them on long running tasks before I provide real guidance on usage.

I though Opus 5.0 was a step down from Opus 4.8 but so far Opus 5.5 is looking much better.

As it stands I still consider Astra the most powerful model.
