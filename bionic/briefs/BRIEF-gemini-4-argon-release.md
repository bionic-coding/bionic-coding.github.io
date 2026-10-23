---
title: "Gemini 4 Argon release research brief"
slug: gemini-4-argon-release
type: brief
status: draft
created_at: 2026-10-13
updated_at: 2026-10-13
authors: ["Codex"]
tags: [google, gemini-4, argon, model-news, coding, pricing, editorial]
related_adrs: []
---

# Gemini 4 Argon release research brief

**Research checked October 13, 2026.** Prepared for Bionic Coding as background for model coverage and practical evaluation.

Gemini 4 Argon deserves a trial on difficult coding and document work. Its strongest evidence combines a lead on an external knowledge-work benchmark with support for much longer reasoning runs. The practical questions are whether it finishes your tasks correctly, how much review it needs, and what each accepted result costs.

## What came out and who gets it

Google announced Argon on **September 30**, initially for trusted cybersecurity defenders through its Fairwind Program. That announcement described broader access as forthcoming. [Google announcement, September 30](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/).

The **October 13 release** adds public developer availability and consumer rollout:

| Product | Access confirmed in current documentation |
| --- | --- |
| Gemini API and AI Studio | Argon is available; API usage requires the paid tier. |
| Gemini app | Rolling out globally to Google AI Pro and Ultra subscribers. |
| Google Antigravity | Ultra subscribers and eligible enterprise subscriptions; Pro does not include Argon. |

Sources: [API release documentation](https://ai.google.dev/gemini-api/docs/latest-model), [API pricing](https://ai.google.dev/gemini-api/docs/pricing), [Gemini app release notes, October 13](https://gemini.google/release-notes/), and [Antigravity release announcement, October 13](https://www.antigravity.google/blog/gemini-4-argon-in-google-antigravity).

Antigravity's model matrix adds a product distinction: Argon supports Antigravity 2.0, CLI, and IDE extensions; it excludes the product called Antigravity IDE. A subscription and a supported client both matter. [Antigravity model availability](https://www.antigravity.google/docs/models/).

## What changes technically

The stable API model ID is `gemini-4-argon`. It accepts text, images, audio, video, and PDFs, and produces text. It supports tools, structured outputs, search grounding, code execution, and preview computer use. It does not directly generate images or audio, or support the Live API. [Model specifications](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon).

The million-token headline needs care. **Input, reasoning, and output share a single 1,048,576-token window.** A large input leaves less room for reasoning and output. The Developer API model page lists a default synchronous output limit of 65,536 tokens. Cloud distinguishes 65,536 tokens for streaming from 32,768 for non-streaming direct HTTP requests. [Model specifications](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon), [Cloud developer guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-argon).

Long decode allows generation beyond that limit through continuation. On the **Gemini Developer API**, the Interactions API requires background execution and a larger output budget; the server continues generation in hops. Changing the model ID alone does not enable it. Thinking defaults to `medium`, with `low` and `high` available. [API release and migration guide](https://ai.google.dev/gemini-api/docs/latest-model), [long decode guide](https://ai.google.dev/gemini-api/docs/long-decode).

### Cloud integration and migration

The **Gemini Enterprise Agent Platform** has different API requirements. Its guide supports long decode through GenerateContent on **`v1beta1` only**, and explicitly excludes the Cloud Interactions API. The SDK follows continuation tokens automatically; a custom loop must resend the original request with the latest token. Python requires `google-genai >= 2.30.1`; JavaScript requires `@google/genai >= 2.29.1`. [Cloud developer guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-argon).

For migrations, Cloud ignores `temperature`, `top_p`, and `top_k`. It rejects `thinking_budget`, `MINIMAL` thinking, `candidate_count`, and frequency or presence penalties. Prefilled model turns are unsupported. Implicit caching requires a shared prefix of at least 6,144 tokens. Continuation requests bill prior decoded tokens again as input, with the cache discount when eligible. These requirements affect existing agent harnesses and cost estimates. [Cloud developer guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-argon).

## What it costs

Standard Gemini Developer API prices, in USD per million tokens:

| Token type | Through November 30, 2026 | From December 1, 2026 |
| --- | ---: | ---: |
| Input | $2.00 | $4.00 |
| Output, including thinking | $10.00 | $20.00 |
| Cached input | $0.10 | $0.20 |

Caching is implicit only. Batch and Flex charge half the standard token rates. Argon has no free API tier. [Google pricing](https://ai.google.dev/gemini-api/docs/pricing).

For illustration, 100,000 uncached input tokens plus 100,000 billed output tokens cost **$1.20 now**, or **$2.40 from December 1**. That calculation excludes tools, grounding, retries, and additional continuation input. Long reasoning can consume the output budget before much visible text appears.

## What the benchmarks establish

**External evidence:** Vals AI's October 12 leaderboard places Argon first at **68.90%**, ahead of Sonnet 5.5 at 67.04% and Opus 5.5 at 66.97%. The index combines finance, coding, legal, and tax tasks using economic weights. Argon leads the aggregate; other models lead several components. [Vals Index results and methodology](https://www.vals.ai/benchmarks/vals_index).

Vals lists Argon at $15.68 per test and GPT-6.1 Sol at $3.24, with Sol scoring 61.15%. These are benchmark-specific costs, not forecasts for a user's workload. The table uses Argon's $4/$20 rates. Token price alone does not establish the cheapest completed task. [Vals Index](https://www.vals.ai/benchmarks/vals_index).

**Google-reported results:** the October model card shows strengths and gaps within coding:

| Benchmark | Argon | GPT-6 Astra | Claude Opus 5.5 |
| --- | ---: | ---: | ---: |
| DeepSWE v1.1 | 77.9% | 74.1% | 74.2% |
| FrontierSWE v2 | 55.0% | 65.5% | 62.3% |
| Terminal-bench 4.0 | 57.4% | 58.2% | 66.4% |
| CWE-bench v1 | 68.0% | 68.0% | 67.0% |

These results support a claim of competitive coding capability. They do not establish a universal coding lead. Evaluation settings belong to the published methodology. [Google model card](https://deepmind.google/models/model-cards/gemini-4-argon/).

## Production evidence and remaining limits

Google reports a 35% increase in agentic code and a 30% decrease in post-submit rollbacks over four weeks of internal Antigravity use. Its examples include performance optimization, security review, and legacy-code migration. These are vendor reports about Google workflows; the announcement does not establish a controlled causal comparison. [Antigravity release announcement](https://www.antigravity.google/blog/gemini-4-argon-in-google-antigravity).

The model card lists hallucinations, occasional slowness, and timeouts as limitations. Its knowledge cutoff is March 2026, with older knowledge in some domains. Current facts still require retrieval and verification. [Google model card](https://deepmind.google/models/model-cards/gemini-4-argon/).

## Implications for Bionic Coding

The editorial angle is concrete: **Google's new model can spend much longer on difficult work, but access, cost, and task fit determine its value.** Explain the shared token window, separate the announcement from availability, and pair the Vals lead with the coding results where Argon trails.

A practical trial should use the same task, source material, tools, and acceptance criteria across models. Start with a bug requiring repository investigation, a migration requiring passing checks, and a synthesis task requiring traceable citations. Record accepted outcomes, elapsed time, total cost, retries, and human review time.

Begin at medium thinking. Try high thinking or long decode when a failed task gives a reason to spend more. Compare results at December pricing before making Argon a default. The decision should turn on the cost of an accepted result and the judgment needed to reach it.

## Research follow-up

- Test Argon on representative Bionic Coding tasks; no hands-on evaluation was performed for this brief.
- Check continuation billing and latency during a long-decode trial.
- Test Developer API and Cloud integrations separately; their long-decode routes differ.
- Recheck plan and client availability before publishing instructions, since the rollout began today.

Earlier announcement material is preserved at [[research/sources/gemini-4-argon]]. That September capture predates today's API specifications and dated pricing schedule.
