---
title: "Dream-RSI: Recursive Self-Improvement through Evolving Worlds"
slug: dream-rsi-recursive-self-improvement-through-evolving-worlds
type: source
source_url: https://arxiv.org/html/2609.14858v1
source_date: 2026-09-14
author: "Tong Zheng et al."
captured_at: 2026-09-16
last_source_check: 2026-09-16
raw_path: research/raw/2026-09-16/dream-rsi-recursive-self-improvement-through-evolving-worlds/
previous_captures: []
static: true
tags: [recursive-self-improvement, agents, exploration, world-models, coding-agents, scientific-discovery, benchmarks]
---

# Dream-RSI: Recursive Self-Improvement through Evolving Worlds

_Tong Zheng et al., arXiv:2609.14858v1, submitted 2026-09-14. Captured from arXiv HTML on 2026-09-16. The immutable capture contains the rendered page, its two figures, and the full machine-extracted Markdown at `research/raw/2026-09-16/dream-rsi-recursive-self-improvement-through-evolving-worlds/`._

## Abstract

The authors introduce Dream-RSI, a framework for improving an agent's **exploration policy** while leaving the underlying coding agent unchanged. It converts a completed discovery tree—attempts, branches, scores, diagnostics, and saved execution outcomes—into a replay simulator. Candidate policies can then be tested against those recorded outcomes before the selected policy is sent back into an online discovery run.

## Method described by the paper

Dream-RSI has three stages: online exploration produces a discovery tree; that history becomes a pool of replay simulators; then a fixed LLM-based policy-development agent proposes and evaluates alternative exploration-policy code in those simulators. The policy selects branches, concurrency, and stopping decisions. Only that policy code changes: the discovery agent, evaluator, models, and execution interfaces remain fixed.

The paper calls the offline evaluation step “dreaming.” It is off-policy replay over outcomes that were already observed, so it can compare alternative ways of traversing the recorded tree without repeating the underlying agent calls or evaluations. It is not a world model of unexplored states; a candidate policy can only receive feedback on branches already present in the history.

## Reported experiments

The authors evaluate eight tasks in algorithm engineering, mathematical optimization, and GPU-kernel engineering. Their reported comparisons include up to 162× fewer agent calls than SimpleTES for a Lasso-path task; more than 50× budget savings on some mathematical tasks; and comparable target kernel speeds using 1.79×–2.43× fewer generations on two KernelBench tasks. These are the authors' experimental results, not independent replication.

![Dream-RSI overview](../raw/2026-09-16/dream-rsi-recursive-self-improvement-through-evolving-worlds/Dream-RSI-latest-c1cca036.png)

## Limits stated or implied by the setup

The replay simulator reuses a realised discovery history, so its feedback is bounded by what that history contains. The claimed cost savings measure fewer online generations or agent calls in the stated tasks; they do not establish a general reduction in cost for arbitrary coding work. The paper's recursive self-improvement is at the orchestration layer, not self-modification of model weights or the base coding agent.
