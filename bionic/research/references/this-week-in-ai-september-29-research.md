---
title: "This Week in AI — September 29 release research"
slug: this-week-in-ai-september-29-research
type: references
tags: [google, gemini-4, argon, weekly, model-news, openai, anthropic, fireworks, ember-1, kimi-k3, pricing, benchmarks, migration, safety]
sources: [introducing-gpt-6-1-sol, using-gpt-6-1-sol, gpt-6-1-sol-model, gpt-6-1-sol-system-card-addendum, introducing-claude-sonnet-5-5, claude-sonnet-5-5-overview, claude-sonnet-5-5-migration-guide, claude-sonnet-5-5-system-card, introducing-ember-1, fireworks-serverless-pricing, gemini-4-argon, gemini-models]
last_reviewed: 2026-09-30
---

# This Week in AI — September 29 release research

Research intake for the week beginning September 28. This is preparation for the post; it is not a draft. Published specifications are distinguished from reported evaluation results. No local model comparisons were performed.

## GPT-6.1 Sol release

OpenAI presents Sol 6.1 as approaching Astra on coding, computer use, and professional work at one fifth of Astra's standard token prices. Standard input/output remain $2/$10 per million tokens; cache reads fall from Sol 6's $0.20 to $0.10.

OpenAI reports matching Astra on DeepSWE at roughly one fifth of its task cost. It reports fewer factual errors at low effort: 11.4% to 7.7% on deliberately difficult, user-flagged prompts. These are vendor-reported results, not a measured error rate for ordinary use.

Available in Work, Codex, and the API on capture day; not yet in Chat. Ultrafast in Codex is announced for the coming days, with an up-to-8x generation-speed claim. Do not describe it as already shipped.

Source: [[research/sources/introducing-gpt-6-1-sol]].

## Sol migration and model selection

The current guide positions Astra for the most demanding work, Sol 6.1 for a balance of capability and cost, and Luna for focused high-volume tasks. The older September 22 capture remains a historical snapshot.

Sol 6.1 supports low through max effort, default medium; none and minimal are unavailable. Tool calling requires Responses. Chat Completions works without tools. Existing Sol 6 requests using none, or tools through Chat Completions, need changes. Remove unsupported sampling parameters when reasoning is enabled.

The supplied fragment `#gpt-6-astra-gpt-61-sol` is absent from the Markdown export. The actual Sol section anchors are `#gpt-61-sol` and `#gpt-6.1-sol`. Preserve the supplied URL for intake provenance; use the existing Sol anchor when drafting.

Source: [[research/sources/using-gpt-6-1-sol]].

## Sol specifications and pricing

The API ID is `gpt-6.1-sol`. Context is 1,050,000 tokens; maximum input is 922,000 and maximum output 128,000. Inputs are text/images; output is text. Knowledge cutoff is April 30, 2026.

Per million tokens: input $2, cache read $0.10, cache write $2.50, output $10. Requests above 272K input tokens charge 2x input/cache and 1.5x output for the whole request. Fast is 2x Standard; Batch/Flex are half Standard. Regional processing adds 10% where available.

The page confirms no none/minimal effort and Responses-only tool calling. US/EU residency is supported; Fast is unavailable with EU residency. These are published API terms, not measured latency or task cost.

Source: [[research/sources/gpt-6-1-sol-model]].

## Sol safety results and limits

OpenAI designates Sol 6.1 Critical for cybersecurity, High for biological/chemical capability, and below High for AI self-improvement. It uses Astra's safeguards stack.

Selected adversarial results: no auto-review bypass attempts; broken-search nondisclosure 2.08% versus Sol 6's 4.92%; warning circumvention 23.5% versus Astra's 17.4%. Coding misrepresentation is 1.50%, versus Astra's 0.51% and Sol 6's 1.30%. The improvements are not uniform.

In the external-agent-message test, peer engagement rises from 26% to 38%, while the specified unauthorized action falls from 11% to 3%, conditional on discovering the board. Preserve that denominator.

These selected evaluations deliberately elicit failures. Their rates do not estimate ordinary production behavior. Older-model comparison values can reflect later versions, so launch tables should not be combined without checking conditions.

Source: [[research/sources/gpt-6-1-sol-system-card-addendum]].

## Sonnet release claims and benchmark footnotes

Released September 28. Anthropic keeps Sonnet 5's $2/$10 token rates and $0.20 cache reads. It claims output generation is 30%+ faster and task cost up to 30% lower, from fewer tokens. The percentages come from Anthropic's testing.

The announcement reports Terminal-Bench 4.0 at 70.6% versus Sonnet 5's 10.3%, GDPval-AA 1844 versus Opus 5.5's 1846, and CursorBench 55.5% versus Opus 5.5's 57.8%. Anthropic still recommends Opus for complex open-ended work requiring sustained judgment.

FrontierCode Main scores 52.1% at xhigh but 46.2% at max. Its footnote describes extra review work causing timeouts or out-of-scope edits. More effort did not mean a better result on that evaluation.

The comparison is against GPT-6 Sol, not GPT-6.1 Sol. Footnotes also identify a fixed Sonnet structured-output bug and older Sol image-understanding issues. Keep those qualifications when using the table.

Source: [[research/sources/introducing-claude-sonnet-5-5]].

## Sonnet specifications and availability

The API ID is `claude-sonnet-5-5`; Bedrock uses `anthropic.claude-sonnet-5-5`. The overview lists Claude API, Bedrock, Google Cloud, Microsoft Foundry, and Claude Platform on AWS.

Context is 1M tokens; synchronous output is 128K. A separate batch beta allows 300K output. Text/images enter; text comes out. Both knowledge and training-data cutoffs are June 2026.

Per million tokens: input $2, output $10, 5-minute cache write $2.50, 1-hour write $4, cache read $0.20. Batch input/output is half price. Minimum cacheable prompt length is 512 tokens.

The API defaults to high effort. The announcement says Claude apps and Claude Code default to medium. Compare task costs at stated effort levels, rather than assuming the defaults match.

Source: [[research/sources/claude-sonnet-5-5-overview]].

## Sonnet migration changes

This guide covers Messages API clients. Managed Agents needs only the model-name change, per the guide.

Adaptive thinking is the default. `thinking.type: disabled` returns 400; use `between_tools` for no up-front thinking at low/medium/high effort. It still produces thinking blocks between tool calls. Xhigh/max require adaptive thinking.

Forced `tool_choice` values any/tool return 400. Use auto and, where supported, strict schemas; strict validates arguments but does not force a call. Bedrock lacks strict structured outputs for this model.

Replay thinking blocks unchanged. Account/conversation binding can make edited histories fail; cross-model blocks can be dropped without failing the request. On Claude API/Google Cloud, migrate old computer use to `computer_toolset_20260801`. Check advisor compatibility.

Longer progress notes now arrive in thinking blocks and are empty under default display. Interfaces must handle display settings or between_tools to show them. Cyber/frontier-LLM refusals can fall back to Sonnet 5 with the API's beta default-fallback option. That option does not retry every refusal category.

Source: [[research/sources/claude-sonnet-5-5-migration-guide]].

## Sonnet system-card checks

The user-supplied PDF is dated September 28 and contains 148 pages. Its executive summary says Sonnet crosses no new RSP threshold, improves prompt-injection resistance, and has regressions in some multi-turn harmlessness tests. It notes less legible thinking. These are Anthropic's assessments.

Table 8.1.A (page 109) reports SWE-Bench Pro 81.3/63.2/89.9 for Sonnet 5.5/Sonnet 5/Opus 5.5; OSWorld 2.1 80.1/57.0/81.8; AutomationBench 44.7/10.7/42.5. DeepSWE v1.1 is 71.0% over five trials (page 110).

Terminal-Bench 4.0 (pages 112–113) uses 66 tasks and five Sonnet trials per task, 330 trials. Sonnet 5.5 scores 70.6% with safeguards and default fallback; 1.2% of requests trigger fallback, affecting 1.5% of trials. Anthropic reports standard error of ±2.5 points. It uses Claude Code bare mode at max; Opus's 66.4% comparison uses xhigh. The card describes a run without internet egress and cached resources. The point score alone does not establish a general win over Opus.

AutomationBench 44.7% uses default fallbacks. Opus 42.5% reruns previously refused tasks with fallback, versus the original 40.0% without that rerun (page 137). Avoid mixing those configurations.

The complete PDF and complete text extraction are preserved. Pages 3, 109, 112, and 113 were rendered and inspected to verify the cited summary and benchmark conditions.

Source: [[research/sources/claude-sonnet-5-5-system-card]].

## Ember-1 — K3 efficiency, reported by Fireworks

Published September 23, so include it as a catch-up story. Fireworks trained Kimi K3 to shorten reasoning. It claims about 40% fewer tokens while retaining comparable quality; two customer coding A/B tests report approximately 35% fewer tokens.

Its table is mixed: DeepSWE 1.1 rises from K3-max's 66.4% to 75.2%, while SWE-bench Verified falls from 93.2% to 92.2%. Benchmark cost reductions span 5.9–51.9%. These are Fireworks' measurements on public tasks and customer workloads, not independent reproduction. Do not combine them with other vendors' harnesses.

The launch offers a two-week serverless research preview; permanence depends on demand. Recheck before publication. No downloadable weights or Ember-specific license is established by this capture.

Mark's context: he liked Kimi K3 but found it too expensive. Ember addresses that reason to reconsider it. This is a candidate for evaluation, not a model the author has tested.

Source: [[research/sources/introducing-ember-1]].

## Ember and K3 prices — checked September 29

Fireworks' official pricing table lists the same rates for Ember-1 and Kimi K3:

| Per million tokens, USD | Standard | Priority |
|---|---|---|
| Input | $3 | $3.75 |
| Cached input | $0.30 | $0.375 |
| Output | $15 | $18.75 |

Ember's proposed savings come from using fewer tokens, not from a token-price cut. Its standard rates remain above Sol 6.1 and Sonnet 5.5's $2/$10 input/output rates. Token rates alone do not decide task cost.

For an illustration only: 40% fewer output tokens at $15/M costs the same as the original output-token count at $9/M. That does not predict whole-request cost; input, caching, retries, and task quality also matter.

The useful trial would compare K3 and Ember on the same bounded tasks, judging completed results and total billed cost. No API calls or paid trial were run during this research.

Source: [[research/sources/fireworks-serverless-pricing]].

## Comparison for drafting

Published API terms, captured September 29. Prices are USD per million tokens at standard rates; task costs depend on token use, effort, tools, and applicable premiums.

| Item | GPT-6.1 Sol | Claude Sonnet 5.5 |
|---|---|---|
| Release | September 29 announcement, corroborated by dated safety addendum | September 28 |
| Input / output | $2 / $10 | $2 / $10 |
| Cache read | $0.10 | $0.20 |
| Context / standard maximum output | 1.05M / 128K | 1M / 128K |
| API default effort | medium | high |
| Lowest reasoning setting | low | between_tools at high effort or below |
| Main upgrade caveat | Responses required for tools; no none/minimal effort | Changes to thinking, forced tool use, and progress blocks |

Sources: [[research/sources/gpt-6-1-sol-model]], [[research/sources/claude-sonnet-5-5-overview]], [[research/sources/using-gpt-6-1-sol]], [[research/sources/claude-sonnet-5-5-migration-guide]].

## Editorial direction and open checks

Candidate angle: both vendors put more capability into their everyday work tier while holding standard token prices. Lower task cost is a reported outcome on selected workloads. It is not a guaranteed reduction for every user.

The post can use four sections: Sol's release, Sonnet's release, Ember as a K3 efficiency catch-up, and the practical migration changes shared across the week's news. Group safety and evaluation caveats into their respective release sections. Keep the standing personal closer from [[briefs/BRIEF-this-week-in-ai-format]]. This research does not establish which model the author prefers this week.

- Do not compare Sol's OSWorld 2.0 offline result directly with Sonnet's OSWorld 2.1 result. Versions and scoring conditions differ.
- Terminal-Bench 4.0 and Terminal-Bench Science 0.1 are different evaluations.
- The captured Sonnet announcement compares GPT-6 Sol. It predates GPT-6.1 Sol and provides no direct comparison with it.
- Some Anthropic results are attributed to external evaluators. We captured Anthropic's reporting, not those evaluators' original result files. No independent head-to-head check of these two new releases was performed.
- Keep fallback policy and reasoning effort alongside benchmark results. A point score can change when either changes.
- Sol Ultrafast and Haiku 5.5 are announced future releases in these captures. Recheck availability before describing them as shipped.
- Publication links should use release dates; mutable API documentation links should say “checked September 29.”
- The OpenAI announcement's original HTML and interactive charts remain a capture gap. Its substantive text is preserved from the web reader. The API pages and safety addendum have direct captures; all Sonnet sources have direct captures or the original PDF.

## Gemini 4 Argon announcement — September 30 addition

Google announces Argon on September 30, with access initially rolling out to trusted cyber defenders through Fairwind. Broader access is planned after further safeguard testing, starting with paid API customers and Google AI Ultra subscribers. No general-release date is supplied. This is an announcement and restricted rollout, not an immediately available alternative for ordinary API users.

Published launch terms: introductory input/output pricing of $2/$10 per million tokens; cached input is 95% below input pricing, implying $0.10 during the introductory period. The footnote sets post-introductory input/output pricing at $4/$20. The introductory period's duration and later cache price are not stated.

The one-million-token figure is an **output limit**, increased from 64K, including room for extended reasoning. Do not describe it as a newly announced one-million-token context window. Longer output capacity can also increase token spend; it does not establish cheaper completed tasks.

Google reports DeepSWE v1.1 at 77.9%, AutomationBench at 51.3%, LVBench at 91.7%, and CWE-bench v1 at 68% (tied first). It claims leadership on the Vals Index. These are claims in Google's release, not locally replicated results; chart-only comparisons and settings remain in image captures. They do not settle a direct comparison with this week's Sol or Sonnet.

Google reports internal engineering results, including over 300 TiB of freed memory and a 2.7x speedup over an existing Rust video-decoder port. The latter comparison is with the Rust port, not the optimized C++ version. Large code migrations remain subject to automated and manual auditing and testing before production.

Trusted cyber defenders and Google's internal teams receive a version without cyber guardrails. Google separately describes safeguards under development for broader access, including misuse prevention, prompt-injection resistance, misalignment monitoring, and sandbox hardening. Avoid framing restricted cyber access as a public model without safeguards.

Source: [[research/sources/gemini-4-argon]].

## Gemini model-page benchmark table — September 30 addition

The rolling Gemini model page currently features Argon and supplies a text table with 19 evaluation rows, including two GraphWalks input-length ranges. This closes the text-table gap left by the announcement's image captures; those original captures remain unchanged.

Google's table puts Argon at 77.9% on DeepSWE v1.1 versus Astra's 74.1% and Opus 5.5's 74.2%. It also reports Vals Index 68.9%, Vals Finance Agent v2 65.4%, Harvey's Legal Agent Benchmark 19.6%, and AutomationBench 51.3%.

The table also shows where Argon trails: Terminal-bench 4.0 is 57.4% versus Opus 5.5's 66.4%; FrontierSWE v2 is 55.0% versus Astra's 65.5% and Opus 5.5's 62.3%; Terminal-Bench Science 0.1 is 57.6% versus Astra's 68.1%. On OSWorld-2.0's offline subset, the partial score is 69.2% versus Astra's 72.6%. CWE-bench v1 ties Astra at 68.0%.

These are Google's published comparisons, not independent replication. The table compares Astra, Fable 5.1, and Opus 5.5; it contains no Sol 6.1 or Sonnet 5.5 column. The linked evaluation-methodology page remains uncaptured, so effort levels and other comparison conditions need checking before drawing conclusions about model selection. GraphWalks' 256K–1M input range is an evaluation label, not a standalone API context-limit specification.

The model page repeats Google's safeguard descriptions but supplies no general-availability date or pricing. Preserve the announcement's restricted-rollout and introductory-price qualifications when using this companion page. The source is marked refreshable because this URL can change to feature a later model.

Source: [[research/sources/gemini-models]].
