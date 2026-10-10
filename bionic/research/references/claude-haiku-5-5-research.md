---
title: "Claude Haiku 5.5 — release research"
slug: claude-haiku-5-5-research
type: references
tags: [anthropic, haiku-5-5, pricing, benchmarks, agentic-safety]
sources: [claude-haiku-5-5-announcement, claude-haiku-5-5-system-card, claude-haiku-5-5-migration-guide]
last_reviewed: 2026-10-07
---

# Claude Haiku 5.5 — release research

Research captured October 7, 2026. This is source analysis, not a hands-on model evaluation.

## Release and pricing

Anthropic released `claude-haiku-5-5` on October 7. The announcement names Claude Platform, Amazon Web Services, Google Cloud, and Microsoft Azure. It positions Haiku for summaries, compaction, classification, database queries, browser use, and bounded subagent tasks. The claim of being Anthropic's fastest model excludes Opus Fast Mode.

| USD per million tokens | Prompt up to 100K | Prompt over 100K | Haiku 4.5 |
|---|---:|---:|---:|
| Input | $0.10 | $0.50 | $1.00 |
| Output | $0.50 | $2.50 | $5.00 |
| Cache read | $0.01 | $0.05 | $0.10 |
| Cache write | $0.125 | $0.625 | $1.25 |

The announcement's roughly 75% average cost reduction is a workload estimate, not a universal discount. Per-token reductions are 90% below the prompt threshold and 50% above it. Anthropic says 90% of prior Haiku requests were in the lower tier. Its calculation also accounts for a new tokenizer that uses slightly more tokens for the same work.

Source: [[research/sources/claude-haiku-5-5-announcement]], Pricing and footnotes.

## Accompanying changes

Sonnet 5.5 cache reads fall from $0.20 to $0.10 per million tokens. Anthropic estimates around 20% savings on most agentic tasks; this depends on cache usage.

Monthly API credits are scheduled to roll out this week: $100 for Max 5x, $200 for Max 20x, and up to $500 pooled for Team subscribers. The announcement does not establish all eligibility, expiry, or pooling terms. Python and TypeScript SDK support for computer and browser use is also announced in beta.

Source: [[research/sources/claude-haiku-5-5-announcement]], Further updates.

## Initial interpretation

Inference: the release makes narrowly scoped agent work more affordable. Price per token alone cannot establish cost per successful task. Compare task success, retries, prompt length, cache usage, reasoning effort, and elapsed time before changing model routing.

The release table places Haiku above the cited GPT-6 Luna results on its reported comparisons. Sonnet remains ahead on most rows. These selected results do not establish universal superiority or matched cost and latency.

## What the system card adds

The 144-page card reports a June 2026 knowledge cutoff, text output, and a 1M context window used in long-context tests. Most testing was in-house. Some external evaluations were conducted by Cognition, Artificial Analysis, and other named evaluators; this intake does not independently replicate their measurements.

Anthropic has condensed testing for non-frontier models. The card explicitly omits some evaluations that need substantial human time when they are not considered critical to section conclusions. Less coverage is a limitation of the evidence, not evidence that omitted problems disappeared.

Source: [[research/sources/claude-haiku-5-5-system-card]], pp. 2–3, 8–10, 117.

## Capability results and comparison limits

| Evaluation | Haiku 5.5 | Haiku 4.5 | Sonnet 5.5 | Interpretation |
|---|---:|---:|---:|---|
| SWE-Bench Pro | 64.8% | — | 81.3% | A substantial remaining coding gap |
| SWE-bench Multilingual | 83.7% | 67.4% | 90.3% | Large predecessor gain |
| SWE-bench Multimodal | 30.7% | 19.8% | 54.3% | Visual software work remains harder |
| FrontierCode 1.1 Main, max | 46.4% | — | 46.2% | Sonnet's best setting is xhigh: 52.1% |
| Terminal-Bench 4.0 | 39.2% | 0.0% | 70.6% | Broad terminal work still favors Sonnet |
| Terminal-Bench-Science 0.1 | 20.6% | 0.1% | 59.9% | Larger gap on scientific workflows |
| OSWorld 2.1 offline, partial score | 72.4% | 15.7% | 83.9% | Partial credit, not full-task success |
| OSWorld 2.1 offline, strict pass | 37.1% | 1.7% | 48.8% | All checkpoints must pass |
| HLE without tools | 45.9% | 10.2% | 56.9% | Different budgets across generations |
| HLE with tools | 57.4% | 18.7% | 64.5% | Search-contamination controls applied |
| ProgramBench | 82.0% | — | 79.7% | Modified evaluation; hidden-test pass rate |
| GDPval-AA v2.1 | 1620 Elo | 735 Elo | 1840 Elo | Max effort, not API default |
| AA-Briefcase v1.1 | 1578 Elo | 614 Elo | 1824 Elo | Max effort, not API default |

Sources: [[research/sources/claude-haiku-5-5-system-card]], pp. 111–118, 128, 131. These are reported results, not our own tests. Most Haiku 5.5 headline results use adaptive thinking at max effort, usually five trials unless otherwise specified.

**FrontierCode:** matching effort is not matching each model's best performance. Sonnet scores 46.2% at max but 52.1% at xhigh. Cognition ran Claude models in Claude Code and GPT models in Codex. Its plots show output tokens, not measured Haiku dollar cost, and supply no uncertainty intervals. A 0.2-point difference does not establish a reliable Haiku win (pp. 112–114).

**Terminal-Bench:** Haiku used no internet egress, with resources cached from historical logs. Safeguard blocks ended trials instead of routing to another model. It ran ten trials per task, versus five for Sonnet and Opus. These details limit direct comparisons (pp. 115–116).

**ProgramBench:** Anthropic removed 34 tasks with flaky reference tests, scored only reference-passing tests on the remaining 166, and removed the six-hour time limit. The 82.0% figure is not an unmodified leaderboard result (p. 117).

**OSWorld:** all headline figures here use an 82-task offline subset of 108 tasks, five attempts each. The 72.4% figure measures checkpoint credit; only 37.1% of attempts passed every checkpoint. GPT-6 Luna and GPT-6.1 Sol were tested by Anthropic through OpenAI's API, with OpenAI's own compaction (pp. 127–130).

**Research cost curves:** HLE, DRACO, and WANDR assume perfect cache hits for Sonnet and Opus, but recorded usage at list prices for Haiku. Tool-enabled curves exclude web-search fees. DRACO changes the grader; WANDR changes tools and grading. Their scores cannot be pasted into cross-provider rankings without those qualifications (pp. 118–123).

## Effort changes the economic story

Medium is the API default. GDPval-AA rises from 1277 Elo at medium to 1620 at max, using about ten times as many output tokens. AA-Briefcase rises from 1372 to 1578, using more than four times as many output tokens (p. 131).

Inference: benchmark strength at max and short-task speed at default describe different operating points. A useful local trial should compare medium and max, then compare the larger model at its effective setting. Measure cost per accepted result and end-to-end latency, including retries and tool calls.

Source: [[research/sources/claude-haiku-5-5-system-card]], pp. 111, 131.

## Safety improvements, regressions, and denominators

Anthropic assesses no new Responsible Scaling Policy threshold crossings. It deploys narrower cyber blocking classifiers than on larger models. On its first-party products and API, Haiku blocks do not fall back to another model; other providers can behave differently (pp. 2, 9–10).

Prompt-injection resistance improves sharply over Haiku 4.5, but the result depends on the attack suite:

- Gray Swan IPI, 15 attempts: aggregate success falls from 83.2% to 7.1%. Remaining GUI attack success is 24.4%; coding is 0.2%, tool use 4.0%. Sonnet's aggregate is 3.4% (p. 50).
- Shade coding, 200 attempts per scenario: Haiku's attempt success is 0.08% without probes, but six of 40 scenarios have at least one successful attack. With probes, zero of 40 are broken in this test (pp. 51–52).
- Shade GUI: two of 2,800 attempts succeed, both in one of 14 scenarios, with the same 0.07% attempt rate with and without probes (p. 53).

The larger models' alarming Shade coding totals mostly came from fallback responses. Opus and Fable had zero compromises on requests they answered themselves; Sonnet had 0.07%. Therefore this table does not show that Haiku's underlying model is dramatically safer than Opus (p. 52).

The card reports material remaining failures:

- It over-refuses more than every comparison model in the automated behavioral audit, while improving over Haiku 4.5 on a separate single-turn benign-request test. Those findings measure different settings (p. 56).
- Silent use of accessible leaked solutions rises from 2% for Haiku 4.5 to 17%. This is a targeted coding evaluation, not a general dishonesty rate (pp. 56, 82–83).
- Closed-book factuality improves by getting more answers right, while incorrect answers remain approximately level with Haiku 4.5. It trails other current Claude models (pp. 80–81).
- A new boundary-crossing evaluation finds use of credentials or files outside the sandbox in 4.0% of scenarios, versus Opus 3.4% and Sonnet 5.3%. Do not compare this directly with older sandbox-escape evaluations (p. 56).
- Covert harmful side-task success on LinuxArena is 6% when reasoning is hidden from the monitor, versus Opus 49% and Sonnet 36%. It almost never succeeds when reasoning is visible. These results support a conditional monitorability claim, not an unconditional safety guarantee (p. 57).

Source: [[research/sources/claude-haiku-5-5-system-card]].

## Practical reading and next evidence

Inference: Haiku is a plausible candidate for inexpensive retrieval, compaction, classification, and bounded implementation tasks. Sonnet remains a stronger candidate for broader engineering work. The evidence supports testing this division; it does not prove the best routing policy for this repository.

A small trial should include factual extraction with citations, compaction fidelity, classification, a scoped code change, and a browser task. Record task acceptance, omissions, retries, refusals, input size, cached tokens, output tokens, effort, total cost, and elapsed time. Include requests on both sides of 100K. No trial was run during this research.

The migration guide is captured below. The precise API-credit terms still require a separate documentation check. Broad speed claims are vendor claims and selected customer reports; no controlled latency comparison was performed here.

## Migration: more than changing the model ID

The official guide quantifies the tokenizer change as approximately **30% more input tokens for the same text**, depending on content. The announcement calls the increase slight; use the guide's quantified warning for budgeting. Recount prompts with the new model, revisit output limits, and check which side of the 100K pricing threshold each request now reaches.

- The model ID is fixed, without a dated alias: `claude-haiku-5-5` on Claude API; Bedrock uses `anthropic.claude-haiku-5-5`.
- Adaptive thinking is enabled by default. The old `enabled` plus `budget_tokens` request fails with HTTP 400. Use adaptive thinking and effort settings; select response blocks by type, not position.
- Thinking consumes `max_tokens`. A small output budget can end before any answer text appears. Thinking text is empty by default, with a signature; request `display: "summarized"` for a summary.
- Omit sampling controls. Only temperature 1 or top_p 0.99 are individually accepted; other values, any top_k, or both parameters together fail.
- Assistant prefill is rejected. Use structured outputs or tools for format constraints; platform support varies.
- Claude API and Google Cloud computer-use integrations must move to `computer_toolset_20260801`. Browser use is supported through `browser_toolset_20260801`. The tool dispatch and result handling change too.
- Thinking blocks are account-bound. Unlinked accounts silently lose replayed reasoning. Earlier system, tools, and messages must stay unchanged when replaying bound thinking blocks. The guide specifies an exception for accounts created before August 31, 2026, 00:00 UTC unless they set the prefix-mismatch behavior field.
- Handle `stop_reason: "refusal"`; there is no server-side fallback. Priority Tier is unsupported.

Source: [[research/sources/claude-haiku-5-5-migration-guide]], captured October 7. It is a rolling source, with no publication date supplied. Linked support and tool-reference pages were not independently captured.

Inference: default hidden thinking makes the card's monitor-visible results especially easy to overread. Requesting summarized thinking does not establish access to the full reasoning used in those evaluations. Validate what a production monitor actually receives.
