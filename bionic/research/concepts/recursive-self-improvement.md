---
title: "Recursive self-improvement: policy and infrastructure feedback loops"
slug: recursive-self-improvement
type: concepts
tags: [recursive-self-improvement, agents, exploration, replay, orchestration, scientific-discovery]
sources: [dream-rsi-recursive-self-improvement-through-evolving-worlds, glm-built-its-inference-infrastructure, mimo-v2-6]
last_reviewed: 2026-09-22
---

# Recursive self-improvement: policy and infrastructure feedback loops

## Dream-RSI: improving the exploration policy

[[research/sources/dream-rsi-recursive-self-improvement-through-evolving-worlds]] uses “recursive self-improvement” in a narrow, operational sense: improve the code that decides how an agent explores, then use that improved policy for the next exploration run. It does **not** improve the underlying model, evaluator, or execution interface.

The useful idea is to treat completed work as more than context. A recorded discovery tree can act as a replay simulator: alternative policies can choose different saved branches, orders, parallel batches, and stopping points, then receive feedback from outcomes that were already paid for. That can make meta-level experimentation cheaper than repeatedly running the base agent online.

The boundary matters. Replay can evaluate choices within the portion of the search space that has already been explored. It cannot prove that a policy will work on an unrecorded branch or a new task. Dream-RSI's performance and cost results are the authors' reported experiments across eight scientific and engineering tasks, not independent evidence for general-purpose coding agents.

## GLM: improving inference infrastructure

[[research/sources/glm-built-its-inference-infrastructure]] describes a GLM-5.3-powered Infra Agent helping engineers build the serving system for GLM-5.3-Flash. Z.ai explicitly says this has not reached recursive self-improvement. Humans still choose objectives, set boundaries, and review critical changes. The article does not demonstrate autonomous successor-model training or changes to the agent model's weights.

Z.ai reports production readiness in under two weeks and roughly threefold end-to-end throughput relative to its initial baseline. It describes a cluster exceeding 100,000 Chinese-made accelerators. Those are vendor-reported results, not independently reproduced measurements. The article does not isolate the agent's contribution from the engineers' work through a controlled comparison.

The mechanism is “dense feedback”: observations tied to a specific computation or execution path, inexpensive enough for frequent experiments, and checked objectively. More logs alone are not the goal. The three reported cases make that distinction concrete:

- **Correctness:** comparing context-parallel and unpartitioned kernel paths exposed accumulated numerical error. Z.ai describes a precision fix and links Flash Linear Attention PR #1180. The PR is a verification lead; its merge status and agent attribution were not independently checked during this ingest.
- **Concurrency:** traces led the agent to Python GIL contention between DeepEP and Mooncake Transfer. Z.ai reports that releasing the GIL reduced the tested Prefill + KV Transfer performance gap from over 20% to below 1%.
- **Performance:** reusable optimization patterns guided kernel experiments. One change reportedly achieved a 1.71× speedup over the preceding kernel version. That local comparison is distinct from the full stack's threefold throughput gain.

Local checks reject bad candidates quickly. End-to-end tests determine whether local gains survive the actual workload. Engineers retain review of numerical semantics, concurrency, and production risk.

The article identifies GLM-5.3-Flash's earlier anonymous release as **Ox-Alpha**. It supplies no attribution for **Union Alpha**.

## MiMo-V2.6: RSI as a marketing frame for RL scaling

[[research/sources/mimo-v2-6]] (Xiaomi, 2026-09-22) calls its MiMo-V2.6 release "a key step in our exploration of the RSI path," defined in the same sentence as "scaling RL compute on verifiable, complex tasks, so the model can continuously expand its capability frontier through exploration and feedback." That is a **third, looser sense of RSI** next to the two above: not a policy change replaying recorded outcomes (Dream-RSI), and not a description of humans directing an agent to improve serving infrastructure (GLM) — here it names ordinary large-scale RL post-training (30 steps, ~750k trajectories, a frozen router, reward-hacking countermeasures) and calls the resulting capability gain "self-improvement" because the model's own rollouts generate its training signal.

No mechanism in the source demonstrates a model modifying its own training process, objective, or successor architecture — it is RL on fixed infrastructure with fixed grading, the same category Anthropic and others call "scaling," not RSI in Dream-RSI's operational sense. The label functions here as framing for an RL-scaling result, not as a claim this wiki should treat as evidence of a new capability class.

## Reading the three sources together

The shared lesson is to specify what changes and how its improvement is measured. Dream-RSI changes an exploration policy using recorded outcomes. Z.ai describes changes to serving software using tests, traces, and benchmarks. MiMo-V2.6 applies the term to RL post-training on a fixed pipeline. None of the three establishes a system autonomously designing and training its successor — and one of the three (MiMo) applies the term to something that, on the same definition Dream-RSI and Z.ai's account use, would not qualify. When "RSI" appears in vendor copy going forward, check which of these three senses is meant before repeating the term.

For Bionic Coding, the practical implication is better feedback with less irrelevant context, and a caution about vocabulary drift: RSI is being used as a label for ordinary RL scaling, which dilutes it for the cases (Dream-RSI's replay policy) where the term names something structurally distinct. Give an agent evidence that distinguishes its current hypotheses. Keep acceptance criteria and consequential judgments under human control. This is a synthesis of the three accounts, not an independently measured result.
