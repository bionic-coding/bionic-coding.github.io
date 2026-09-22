---
title: "Claude Opus 5.5"
slug: claude-opus-5-5-announcement
type: source
source_url: https://www.anthropic.com/claude-opus-5-5
source_date: 2026-09-22
author: "Anthropic"
captured_at: 2026-09-22
last_source_check: 2026-09-22
raw_path: research/raw/2026-09-22/claude-opus-5-5-announcement/
previous_captures: []
static: true
tags: [anthropic, claude, opus-5-5, announcement, pricing, benchmarks, frontier-models]
---

Captured via `web-to-markdown` (word_count 6122, thin_content: false). This is Anthropic's
announcement/blog post for Claude Opus 5.5, distinct from the system card
([[research/sources/claude-opus-5-5-system-card]]) and the product page
([[research/sources/claude-opus-5-5-product-page]]).

> [paraphrased] The page includes a long "Communication" section with side-by-side example
> transcripts (a bug explanation, a Slack thread summary, and a chess/TensorFlow code
> review) contrasting Opus 5 vs. Opus 5.5 responses, and a large block of named customer
> testimonials (GitHub, Clio, Lovable, Quantium, Spotify, Optiver, Column, Kiro, Ramp,
> Stripe, Box, Chicago Trading Company, Factory, Deloitte Consulting, Rogo, LexisNexis,
> Walleye Capital, Hex, Thomson Reuters Labs, Hebbia, Viktor). These are marketing
> illustrations, not independently verifiable claims, and are summarized rather than
> reproduced verbatim in full below — the load-bearing factual claims (release date,
> pricing, availability, benchmark table, safety/safeguards) are preserved verbatim.

## Release date, headline framing (verbatim)

> # Claude Opus 5.5
> September 22, 2026
>
> We're introducing Claude Opus 5.5, the first model in our new Claude 5.5 family. It
> performs at the level of Claude Fable 5.1 on most work and costs 40% less to run than
> Opus 5.
>
> Claude Opus 5.5 is our first release since we called for [pacing the frontier]. It was tested
> before release by external evaluators, including [Frontier Design] and [METR]. On our
> automated behavioral audit, the most comprehensive alignment test we run, Opus 5.5 is
> the strongest-performing model we've tested to date. It also comes with the safeguards
> we've developed for our most capable models.

## Availability (verbatim)

> Claude Opus 5.5 is now available on all platforms, including Amazon Web Services, Google
> Cloud, and Microsoft Azure. On the Claude Platform, developers can [get started] with
> `claude-opus-5-5`.

Model ID for API use: **`claude-opus-5-5`**.

## Pricing (verbatim table + prose)

> Because Opus 5.5 is comparable to Claude Mythos 5.1 in biology and cybersecurity, we're
> deploying it with safeguards similar to those on Claude Fable 5.1. ... **Cost and speed.**
> Opus 5.5 requires less compute to serve than Opus 5, and its pricing reflects that. Our
> tests show that at default settings it will cost 40% less than Opus 5 on typical workloads.
> Input and output tokens are $4 and $20 per million, 20% less than Opus 5. Cache reads
> (which make up the majority of agentic and coding work costs) are $0.20 per million
> tokens, 60% less than Opus 5. Opus 5.5 also generates output more than 30% faster than
> Opus 5.
>
> In addition to the price drop, we're increasing five-hour usage limits on Pro, Max, and
> Team plans. We're also providing subscription users a rate limit reset, which you can now
> save and use whenever you choose.

| Prices per 1M tokens | Claude Opus 5.5 | Claude Opus 5 |
|---|---|---|
| Cache reads | $0.20 | $0.50 |
| Input tokens | $4 | $5 |
| Output tokens | $20 | $25 |
| Cache writes | $5 | $6.25 |

> Fast mode for Opus 5.5 is also available in Claude Code and the Claude Platform with up
> to 2.5x speed. It costs $8 per million input tokens and $40 per million output tokens.

**Sonnet/Haiku 5.5 (verbatim):** "Claude Sonnet 5.5 and Claude Haiku 5.5 will follow in the
coming weeks, with many of the same improvements to performance, efficiency, and
safety." — not yet released as of this capture.

## Benchmark table (verbatim, reformatted)

> Unless otherwise noted, all Claude Opus 5.5 results use adaptive thinking at max effort.
> Terminal-Bench 4.0 results are reported for Claude Opus 5.5 at xhigh effort and GPT-6
> Astra at high effort, as reported by OpenAI; these represent each model's highest score.
> Claude Opus 5.5 was evaluated with its production safeguards enabled. When they
> intervened, cybersecurity tasks were completed by Claude Opus 4.8, and biology and
> frontier LLM development tasks were completed by Claude Opus 5. This likely reduces
> Claude Opus 5.5's performance on these benchmarks.

| Evaluation | Opus 5.5 | Fable 5.1 | Opus 5 | GPT-6 Astra | GPT-5.6 Sol |
|---|---|---|---|---|---|
| Agentic coding — Terminal-Bench 4.0¹ | 66.4% | 55.8% | 52.3% | 57.9% | 37.3% |
| Agentic coding — FrontierCode v1.1 (Main) | 54.4% | 50.3% | 48.0% | 53.3% | 47.5% |
| Agentic coding — CursorBench 4.0 | 57.8% | 51.8% | 46.6% | — | 41.7% |
| Knowledge work — GDPval-AA v2.1 | 1846 | 1735 | 1708 | 1542 | 1588 |
| Business workflows — AutomationBench² | 40.0% | 31.4% | 26.9% | 41.4% | 28.8% |
| Multidisciplinary reasoning — Humanity's Last Exam (with tools) | 67.7% | 65.6% | 63.6% | 57.2% | — |
| Agentic scientific research — Terminal-Bench-Science 0.1³ | 58.7% | 52.6% | 29.0% | 64.6% | 22.4% |
| Computer use — OSWorld 2.0 (partial) | 81.8% | 80.7% | 74.0% | — | — |
| Visual chart recognition — Chartography (with tools) | 89.0% | 88.4% | 83.4% | — | — |

Footnotes (verbatim):
1. **Terminal-Bench 4.0:** "The standard error is ±2.6 pts for Claude Opus 5.5 and ±1.6–2
   pts for the other Claude models. The public leaderboard (5 trials/task, Claude Code
   harness) reports Claude Opus 5 at 51.8%; our setup reproduces it at 52.3%, within
   noise. GPT-6 Astra and GPT-5.6 Sol figures are as reported by OpenAI."
2. **AutomationBench:** "results were run and reported by Zapier. These runs were
   performed without fallback models, so safeguard interventions were considered
   failures—this resulted in a lower score than Claude Opus 5.5 would achieve in
   practice."
3. **Terminal-Bench-Science 0.1:** "The standard error is ±3.5–5 pts per model. The public
   leaderboard (3 trials/task, Claude Code harness) reports Claude Opus 5 at 30.0%; our
   setup reproduces it at 29.0%, within noise. The GPT-6 Astra figure is as reported by
   OpenAI."

**Baselines named:** Fable 5.1, Opus 5, GPT-6 Astra (OpenAI), GPT-5.6 Sol (OpenAI) —
every number in this table is an Anthropic-run first-party evaluation *except*
AutomationBench (run/reported by Zapier) and the GPT-6 Astra / GPT-5.6 Sol columns
(as reported by OpenAI, not independently reproduced by Anthropic).

## Safety and safeguards (verbatim, selected)

> On our primary evaluation suite, an automated behavioral audit that assesses Claude
> across nearly 2,000 scenarios, Opus 5.5 scored better than any recent Claude model on
> nearly every measure of misaligned behavior. It's also our strongest model on most
> measures of honesty.
>
> In particular, Opus 5.5 improves over previous models on several of the behaviors that
> contributed to recent cybersecurity incidents, including biased or motivated reasoning,
> attempting to escape a sandbox, and taking harmful actions after concluding it was in a
> simulated environment. In a new evaluation designed to test a model's propensity to
> cross containment boundaries, Opus 5.5 attempted to circumvent boundaries around 85%
> less often than Opus 5 or Claude Mythos 5.1, and every attempt it made was low severity
> and self-reported.
>
> However, as we described in our recent alignment assessment, building evaluations that
> reliably catch every failure prior to deployment remains an unsolved problem. We see
> signs that Opus 5.5 often suspects it is being evaluated, which challenges our ability to
> assess how it will act in the vast variety of real-world settings it is deployed in.

> **Cybersecurity.** Because Opus 5.5 has extremely strong cyber capabilities, we're
> applying cybersecurity safeguards to Opus 5.5 that are similar to Fable 5.1's. Users will
> be able to identify and fix bugs in their code as part of the routine software development
> lifecycle, but most cybersecurity tasks will be re-routed to Opus 4.8.
>
> **Biology.** Opus 5.5 is highly capable in biology, exceeding Opus 5 and matching or
> beating Claude Mythos 5.1 across many areas of work. ... For this reason, Opus 5.5 uses
> the same biology safeguards as Fable 5.1.

> **Distillation.** Opus 5.5 is launching with preserved thinking, the anti-distillation
> safeguard we introduced with Fable 5.1. It stops API users from editing Claude's prior
> context in an attempt to extract Claude's reasoning. It applies to Fable 5.1 and Opus 5.5
> for API accounts created on or after August 31, 2026.

> **Data retention and compliance.** Like previous Opus models, Opus 5.5 is available with
> zero data retention. As with Fable 5.1, Opus 5.5 comes with our watermarking measures
> to comply with the EU AI Act... It is also no longer available with "thinking" mode
> switched off.

**Cross-check against the system card:** the announcement's "85% less often" containment-
boundary framing is consistent in direction with the system card's §6.4.8 finding (1.5% of
cases, all low severity, "recent training interventions... have had a strong effect") but the
two documents state the comparison differently — the announcement gives a relative
percentage reduction vs. Opus 5/Mythos 5.1, the system card gives an absolute rate. Not a
contradiction, but the two numbers are not directly substitutable for each other.

## Limitations noted in the announcement itself (verbatim)

> At these levels of capability we've found that benchmark margins have become a less
> reliable guide to real-world differences. In our own use, the gap between Opus 5.5 and
> Claude Fable 5.1 is narrower than these scores suggest.

> We see signs that Opus 5.5 often suspects it is being evaluated, which challenges our
> ability to assess how it will act in the vast variety of real-world settings it is deployed in.
> As these settings expand and model capabilities increase, we expect this challenge to
> grow, unless we make progress on interpretability.

## Capture gaps

- The "Communication" section's full side-by-side example transcripts (bug explanation,
  Slack summary, chess/TensorFlow code review) and the ~21 customer testimonial quotes
  were paraphrased/summarized above rather than reproduced in full — see the raw
  capture (`../raw/2026-09-22/claude-opus-5-5-announcement/`) for the complete text.
  These are marketing illustrations, not independently verifiable claims.
- No images were downloaded (`images_downloaded: 0` per the fetch metadata) — the
  page's benchmark charts (accuracy-vs-cost plots) are described only by their surrounding
  captions in the captured markdown, not their underlying data points.
- Deep links referenced but not followed: the "We Must Pace the Frontier" post, the
  Opus 5.5 System Card link (captured separately, see
  [[research/sources/claude-opus-5-5-system-card]]), the Life Sciences Verification
  Program, the Cyber Verification Program, the September 2026 threat intelligence
  report, and the alignment-assessment-cybersecurity-incidents research post.
