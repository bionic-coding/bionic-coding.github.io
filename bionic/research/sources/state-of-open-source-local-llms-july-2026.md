---
title: "State of Open-Source Local LLMs — July 2026"
slug: state-of-open-source-local-llms-july-2026
type: source
source_url: https://llmcheck.net/blog/state-of-open-source-local-llms-july-2026/
source_date: 2026-07-11
author: "LLMCheck Research Team"
captured_at: 2026-08-01
last_source_check: 2026-08-01
raw_path: research/raw/2026-08-01/state-of-open-source-local-llms-july-2026/
previous_captures: []
static: true
tags: [open-weights, local-llms, apple-silicon, benchmarks, glm, qwen, licensing]
---

INDUSTRY REPORT · July 2026 · 19 min read

According to the LLMCheck index (July 2026), GLM 5.2 from Zhipu AI became the first open-weights model to beat GPT-5 and Claude on SWE-Bench Pro, scoring 68.5%. Qwen 4.1 32B-A3B is the new Mac-runnable #1 at score 76, while DeepSeek R3, Llama 5 405B, and Kimi K3 push the server-class frontier.

June 2026 was the month open source spread out across every Mac tier. July 2026 is the month it broke the frontier. GLM 5.2 — a 744-billion-parameter mixture-of-experts model from Zhipu AI — became the first open-weights model in history to beat GPT-5 and Claude on SWE-Bench Pro, the hard agentic-coding benchmark. Around it, ten flagship releases landed in 30 days: Qwen 4.1 took the Mac-runnable crown, DeepSeek R3 hit 95% on AIME, Meta shipped its long-rumored Llama 5 405B dense frontier model, and Gemma 4.5 27B, Mistral Medium 4, and Phi-5 Large 28B refreshed the mid tier. This is the definitive July 2026 recap, benchmarked on Apple Silicon, with install commands. Every claim is sourced from LLMCheck's own measurement pipeline.

## The 30-Day Recap (TL;DR)

Every major open-weights release between June 11 and July 2026, with a one-line takeaway. Ten flagship drops in 30 days — and for the first time, the headline is not a Mac model but a server-class one that beat the closed frontier outright.

* **GLM 5.2** Jul 8 — MIT, 744B-A40B MoE, 68.5% SWE-Bench Pro — the FIRST open model to beat GPT-5 and Claude. The headline.
* **GLM 5.2 Air 106B-A12B** Jul 8 — MIT, runs on a 64 GB Mac at ~30 tok/s, 58% SWE-Bench Pro — frontier-adjacent on consumer silicon.
* **Qwen 4.1 32B-A3B** Jul 2 — Apache 2.0, 80% SWE-Verified, ~62 tok/s on M4 Pro 24 GB — the new Mac-runnable #1, score 76.
* **DeepSeek R3** Jul 5 — MIT, 685B-A37B, AIME 95% — frontier reasoning, server-class.
* **Llama 5 405B** Jul 6 — Meta's dense frontier, MMLU 91%, server / 192 GB Q2 only (~5 tok/s on M4 Ultra).
* **Gemma 4.5 27B** Jul 3 — Gemma, 1M context, MMLU 86%, ~42 tok/s on M5 Max, 32 GB Mac.
* **Mistral Medium 4 41B-A13B** Jul 4 — Apache 2.0 MoE, SWE-Verified 70%, ~48 tok/s, 32 GB Mac.
* **Phi-5 Large 28B** Jun 28 — MIT, MMLU 88%, AIME 80%, ~38 tok/s on M5 Max, 24–32 GB Mac.
* **Kimi K3 ~1T-A32B** Jul 7 — MIT, agentic-coding leader, server-class.
* **Command R+ 2 104B** Jul 1 — CC-BY-NC, enterprise RAG, ~28 tok/s on a 64 GB Mac.

> [contradiction] The Kimi K3 row above conflicts with two sources already in this
> wiki and with [[research/sources/willison-kimi-k3]], captured the same day as this
> page. LLMCheck says "~1T-A32B, Jul 7, 2M context". Moonshot's own technical report
> ([[research/sources/kimi-k3-technical-report]]) and Willison's independent writeup
> both give **2.8T total / 104B activated, 1M context, announced Jul 16**. The
> primary sources agree with each other and disagree with LLMCheck; treat this
> page's Kimi K3 specs as unreliable. See `## Capture gaps` below.

**Headline story:** For two years, the open-vs-closed gap on agentic coding was the one number that still favored OpenAI and Anthropic. In July 2026, GLM 5.2 erased it — 68.5% on SWE-Bench Pro, ahead of GPT-5 and Claude, under an MIT license. The full model is server-class, but the GLM 5.2 Air distillation brings 58% SWE-Bench Pro to a 64 GB Mac at ~30 tok/s. The frontier is now open.

---

## GLM 5.2 — the frontier falls

On July 8, Zhipu AI released GLM 5.2: a 744-billion-parameter mixture-of-experts model with 40 billion active parameters per token, shipped under the MIT license. The benchmark that matters is SWE-Bench Pro — the harder, contamination-resistant successor to SWE-Verified that measures multi-file, multi-step agentic coding. GLM 5.2 scores **68.5%**. According to LLMCheck cross-reference data, that edges out the published GPT-5 and Claude scores on the same benchmark. This is the first time in the history of open-weights AI that an MIT-licensed model has led the closed frontier on a hard agentic-coding eval.

#### GLM 5.2 Architecture

| field | value |
|---|---|
| Total params | 744B |
| Active params | 40B (5.4%) |
| Context | 1M native |
| License | MIT |
| Mac tier | Server-class |
| LLMCheck Score | 70 / 100 |

#### Benchmarks

| benchmark | score |
|---|---|
| SWE-Bench Pro | 68.5% |
| SWE-Verified | 84% |
| MMLU | 90% |
| AIME 2025 | 93% |
| LiveCodeBench | 85% |
| Agentic SWE | 71% |

**Why SWE-Bench Pro is the number that matters.** SWE-Verified, the benchmark that defined the open-source coding race through the first half of 2026, has been increasingly criticized for contamination — many of its issues leaked into training corpora. SWE-Bench Pro was built specifically to resist that, with held-out repositories, harder multi-file tasks, and a stricter evaluation harness. A 68.5% on Pro is roughly equivalent in difficulty to a high-80s on Verified, and it is the benchmark closed-lab researchers themselves now cite. GLM 5.2 leading it is not a curiosity — it is the new state of the art.

**The architecture is the enabler.** At 744B total with only 40B active, GLM 5.2 uses an extreme sparsity ratio — just 5.4% of parameters fire per token. That keeps inference cost low relative to its capability, but the full weights still need a multi-GPU server or an 8-bit cluster to host. This is not a model you run on a Mac. What you run on a Mac is its distillation.

**GLM 5.2 Air brings it home.** Alongside the flagship, Zhipu shipped **GLM 5.2 Air** — a 106B-A12B MoE distilled from the full model, also MIT-licensed. Air retains **58% on SWE-Bench Pro**, which is still ahead of every other Mac-runnable model on that benchmark, and it runs on a 64 GB Mac at roughly 30 tok/s at Q4_K_M. On a 128 GB Mac Studio it reaches ~34 tok/s via MLX, and on an M4 Ultra 192 GB it hits ~38 tok/s. For the first time, a frontier-adjacent agentic coder runs on consumer Apple Silicon.

```
# GLM 5.2 Air (the Mac-runnable distillation)
ollama run glm5.2:air # ~60 GB, MoE 12B-active

# MLX (fastest on Apple Silicon)
mlx_lm.generate --model mlx-community/GLM-5.2-Air-106B-A12B-4bit \
--prompt "Fix the failing tests in this repo"

# Full GLM 5.2 (server-class, multi-GPU): see Zhipu model card
```

**Verdict:** GLM 5.2 is the most important open-weights release of 2026. The flagship redefines the frontier; GLM 5.2 Air makes 58% SWE-Bench Pro real on a 64 GB Mac. If you have the RAM, Air is now the most capable agentic coder you can run locally as of July 2026.

---

## Qwen 4.1 — the new Mac #1

Six weeks after the full Qwen 4 release, Alibaba shipped Qwen 4.1 32B-A3B on July 2 — a point-release refinement rather than a new generation. The architecture is unchanged (32B total, 3B active, 1M native context, Apache 2.0), but the instruction-tuning and tool-use stages were rebuilt on a larger, cleaner preference dataset. SWE-Verified climbs from 78% to **80%**, tool-use reliability improves measurably, and the LLMCheck Score rises from 75 to **76**. That makes Qwen 4.1 the new #1 Mac-runnable open model.

#### Qwen 4.1 Benchmarks

| benchmark | score |
|---|---|
| SWE-Verified | 80% |
| MMLU | 90% |
| HumanEval | 95% |
| AIME 2025 | 92% |
| Agentic SWE | 63% |
| LLMCheck Score | 76 / 100 |

#### Mac Performance

| configuration | value |
|---|---|
| M5 Max 128 GB | 82 tok/s |
| M5 Max 64 GB | 69 tok/s |
| M4 Pro 24 GB | 62 tok/s |
| RAM (Q4_K_M) | ~19 GB |
| License | Apache 2.0 |
| Context | 1M native |

**The 80% SWE-Verified mark is the milestone.** Crossing 80% on a 24 GB consumer Mac — while only firing 3 billion parameters per token — was unthinkable a year ago. According to the LLMCheck index, Qwen 4.1's SWE-Verified score now matches or exceeds the published numbers for the closed Mac-class competition, and it does so under a fully unrestricted Apache 2.0 license. For startups shipping coding agents and IDE plugins on locally-hosted weights, this is the model with zero licensing risk and zero per-token cost.

**The speed bump matters more than the version number.** Qwen 4.1 reaches ~62 tok/s on a base M4 Pro 24 GB MacBook Pro, up from ~60 for Qwen 4, thanks to refreshed MLX Metal kernels shipped alongside the release. On an M5 Max 128 GB it hits 82 tok/s. The combination of 80% SWE-Verified, 62 tok/s, and a 19 GB memory footprint is why Qwen 4.1 is the model we recommend by default for any Mac with 24 GB or more.

```
# Ollama (one-line install, ~19 GB download)
ollama run qwen4.1:32b-a3b

# MLX (fastest on Apple Silicon)
mlx_lm.generate --model mlx-community/Qwen4.1-32B-A3B-4bit \
--prompt "Refactor this module and add tests"

# LM Studio: search "Qwen 4.1 32B A3B" in Discover tab
```

**Verdict:** Qwen 4.1 32B-A3B is the new default recommendation for any Mac with 24 GB RAM or more. It takes the Mac-runnable #1 spot from Qwen 4 with an 80% SWE-Verified score, an Apache 2.0 license, and ~62 tok/s on entry-tier pro hardware.

---

## The frontier server tier — DeepSeek R3 vs Llama 5 405B vs Kimi K3

Below GLM 5.2, three more frontier-class models shipped in July — and all three are server-class, meaning none run practically on a Mac. They matter anyway: they set the ceiling that next month's distillations will chase, and they define where each lab's strengths lie. DeepSeek R3 owns reasoning, Llama 5 405B owns broad knowledge, and Kimi K3 owns agentic coding.

The July 2026 frontier server tier — July 2026.

| | DeepSeek R3 | Llama 5 405B | Kimi K3 |
|---|---|---|---|
| Params | 685B-A37B | 405B dense | ~1T-A32B |
| License | MIT | Llama 5 | MIT |
| MMLU | 90% | 91% | 89% |
| AIME 2025 | 95% | 88% | 90% |
| SWE-Bench Pro | 64% | 59% | 66% |
| Agentic / long-horizon | Strong | Moderate | Leader |
| Context | 1M | 256K | 2M |
| M4 Ultra 192 GB | Not practical | ~5 tok/s (Q2) | Not practical |
| Best for | Reasoning / math | Broad knowledge | Coding agents |

**DeepSeek R3 owns reasoning.** The 685B-A37B MoE, MIT-licensed, scores **95% on AIME 2025** — the highest math-reasoning score of any open model, closed or open, this month. DeepSeek's R-series has always been a reasoning specialist, and R3 widens that lead with a more efficient routing layer than R2. According to LLMCheck cross-reference data, R3 is the model to beat on competition math, theorem-style proofs, and multi-step logical reasoning. It is server-class, but its capability-per-active-parameter is the best of the three frontier entrants.

**Llama 5 405B owns broad knowledge — and the dense-model burden.** Meta finally shipped the long-rumored 405B dense frontier model on July 6, under the Llama 5 license. At 91% MMLU it edges every other open model on broad academic knowledge, and it retains Llama 5's native multimodality. But 405B dense is brutal to serve: even at Q2 it needs roughly 150 GB of memory. An M4 Ultra 192 GB Mac Studio can technically load it at Q2 and run it at about **5 tok/s** — fine for overnight batch jobs, far too slow for interactive use. For most teams, the 405B is a cloud-only model.

**Kimi K3 owns agentic coding and context.** Moonshot's ~1-trillion-parameter, 32B-active MoE (MIT) is the long-horizon agentic-coding leader, scoring 66% on SWE-Bench Pro and pairing it with a 2M-token context window — the largest of any model this month. For autonomous coding agents that need to hold an entire large codebase in context and execute multi-hour tool-use loops, Kimi K3 is the strongest open option, though it remains server-class and out of reach for local Mac inference.

**Practical recommendation:** None of these three run usefully on a Mac. If you need frontier capability locally, the answer is GLM 5.2 Air, not these. If you can serve in the cloud: pick DeepSeek R3 for math and reasoning, Kimi K3 for long-horizon coding agents, and Llama 5 405B only if you specifically need its multimodal breadth and can absorb the serving cost.

---

## Mid-tier refreshes — Gemma 4.5 27B, Mistral Medium 4, Phi-5 Large 28B

While the frontier grabbed headlines, three mid-tier releases quietly reshaped the 24–32 GB Mac segment — the range where most pro-Mac users actually live. Each targets a different strength: Gemma 4.5 27B on long context, Mistral Medium 4 on efficient MoE coding, and Phi-5 Large 28B on dense reasoning.

### Gemma 4.5 27B — the 1M-context workhorse

Google scaled its Gemma 4.5 refresh up to a 27B dense variant on July 3. The headline is context: a full **1M native window** paired with strong retrieval accuracy, plus 86% MMLU. It runs at ~42 tok/s on an M5 Max and fits a 32 GB Mac at roughly 17 GB. For long-document analysis, codebase-wide reasoning, and RAG over large corpora on consumer hardware, Gemma 4.5 27B is the new top pick — the Gemma license allows commercial use, and the model lands at an LLMCheck Score of 68.

### Mistral Medium 4 — efficient MoE coding

Mistral's Medium 4 is a 41B-A13B MoE under Apache 2.0, shipped July 4. With only 13B active per token it runs at ~48 tok/s on a 32 GB Mac while scoring 70% on SWE-Verified — the best speed-per-coding-quality in the 32 GB tier. According to the LLMCheck index, Mistral Medium 4 is the model to pair with a long-context companion when you want fast iterative coding without dedicating 19 GB to a Qwen-class model.

### Phi-5 Large 28B — dense reasoning at 24 GB

Microsoft completed the Phi-5 family on June 28 with Phi-5 Large 28B, MIT-licensed and dense. It scores **88% MMLU and 80% AIME 2025** — the strongest pure-reasoning numbers in the 24–32 GB Mac tier, beating Gemma 4.5 27B and Mistral Medium 4 on hard math. At ~38 tok/s on an M5 Max and ~16 GB of RAM, it is the reasoning specialist for users who care more about correctness than raw speed. The "phi recipe" has now scaled cleanly from 4B (Mini) through 28B (Large) with no quality regression.

```
ollama run gemma4.5:27b # ~17 GB, 1M context
ollama run mistral-medium-4 # ~24 GB, MoE 13B-active
ollama run phi5:large # ~16 GB, dense reasoning
```

---

## The full landscape — Open-Source Top 10 (July 2026)

According to the LLMCheck index across our standardized data points, here is the open-source leaderboard as of July 2026. Score is the LLMCheck composite (capability + speed + accessibility + license, max 100). Mac Tier is the minimum unified memory needed to run Q4_K_M comfortably; "Server" means the model is not practical on consumer Apple Silicon.

| Rank | Model | Family | Active | License | Mac Tier | Score |
|---|---|---|---|---|---|---|
| 1 | Qwen 4.1 32B-A3B | Alibaba | 3B | Apache 2.0 | 24 GB | 76 |
| 2 | GLM 5.2 Air | Zhipu | 12B | MIT | 64 GB | 74 |
| 3 | Qwen 4 32B-A3B | Alibaba | 3B | Apache 2.0 | 24 GB | 75 |
| 4 | Qwen 4 Coder 32B-A3B | Alibaba | 3B | Apache 2.0 | 24 GB | 72 |
| 5 | Phi-5 Large 28B | Microsoft | 28B | MIT | 24 GB | 71 |
| 6 | GLM 5.2 | Zhipu | 40B | MIT | Server | 70 |
| 7 | DeepSeek R3 | DeepSeek | 37B | MIT | Server | 69 |
| 8 | Phi-5 Mini | Microsoft | 4B | MIT | 8 GB | 70 |
| 9 | Gemma 4.5 27B | Google | 27B | Gemma | 32 GB | 68 |
| 10 | Mistral Medium 4 | Mistral | 13B | Apache 2.0 | 32 GB | 66 |

Three observations. First, note the gap between rank and score: GLM 5.2 Air ranks #2 on score (74) but the full GLM 5.2 sits at #6 (70) because its server-class accessibility drags the composite down despite leading every capability benchmark — a reminder that the LLMCheck Score rewards models you can actually run. Second, **MIT and Apache 2.0 account for 9 of the top 10** — only Gemma 4.5 27B uses a non-OSI license. Third, **two Zhipu models cracked the top six in their first month**, the fastest debut of any new lab in LLMCheck's history. Qwen 4.1 holds the crown, but the competition behind it has never been deeper.

---

## 5 things that changed in July 2026

### 1. Open beat closed on agentic coding — for the first time

GLM 5.2's 68.5% on SWE-Bench Pro is the single most consequential data point of the year. For two years, agentic coding was the last benchmark where closed labs held a clear, defensible lead. In July 2026, an MIT-licensed open model erased it. The implications ripple downward: GLM 5.2 Air brings 58% Pro to a 64 GB Mac, and Qwen 4.1 puts 80% SWE-Verified on a 24 GB laptop. The open frontier no longer trails — on coding, it leads.

### 2. MIT and Apache 2.0 now dominate completely

Nine of the LLMCheck top 10 ship under MIT or Apache 2.0. Every frontier release this month except Llama 5 405B chose a permissive OSI license — GLM 5.2 (MIT), GLM 5.2 Air (MIT), Qwen 4.1 (Apache 2.0), DeepSeek R3 (MIT), Kimi K3 (MIT), Mistral Medium 4 (Apache 2.0), Phi-5 Large (MIT). According to LLMCheck license tracking, permissive licensing is no longer a differentiator — it is the default, and the labs still attaching usage caps are the outliers.

### 3. The frontier needs clusters, but distillation brings it to Macs

The four frontier-class models this month — GLM 5.2, DeepSeek R3, Llama 5 405B, Kimi K3 — are all server-class. None run usefully on consumer hardware. But the pattern that GLM 5.2 Air established is the important one: ship a flagship for clusters, then distill an "Air"-class variant that fits a high-RAM Mac while retaining most of the capability. Expect every frontier lab to ship a Mac-runnable distillation within weeks of its server flagship from here on.

### 4. 1M context became the spec-sheet floor

Qwen 4.1, Gemma 4.5 27B, GLM 5.2, and DeepSeek R3 all ship with 1M-class native context, and Kimi K3 pushes to 2M. Six months ago 256K was the open-source ceiling; today a 1M window is the baseline expectation rather than a feature. The differentiation has moved from window size to retrieval accuracy at depth — and Gemma 4.5 27B and Qwen 4.1 lead there for Mac-runnable models.

### 5. Chinese labs lead the open frontier

Three of the four frontier-class releases — GLM 5.2 (Zhipu), DeepSeek R3 (DeepSeek), and Kimi K3 (Moonshot) — came from Chinese labs, all under MIT. Combined with Alibaba's Qwen 4.1 holding the Mac-runnable #1, Chinese labs now occupy the top of both the frontier and the consumer leaderboards. Meta's Llama 5 405B is the lone Western frontier entrant this month, and it shipped under the more restrictive Llama 5 license. The center of gravity in open-weights AI has shifted decisively.

---

## By Mac tier — what to run TODAY (July 2026)

Updated recommendations as of July 2026. All numbers are LLMCheck-measured tok/s at Q4_K_M unless noted. Pick by RAM tier:

| Mac RAM | Primary pick | Speed | Backup |
|---|---|---|---|
| 8 GB | Qwen 4 4B | 135 tok/s | Phi-5 Mini (140 tok/s) |
| 16 GB | Phi-5 Large 28B (Q3) | ~26 tok/s | Gemma 4.5 27B (Q3) |
| 24 GB | Qwen 4.1 32B-A3B | 62 tok/s | Phi-5 Large 28B (38 tok/s) |
| 32–48 GB | Mistral Medium 4 + Gemma 4.5 27B | 48 tok/s | Qwen 4.1 + Phi-5 Large |
| 64 GB | GLM 5.2 Air | ~30 tok/s | Command R+ 2 (~28 tok/s) |
| 128 GB | GLM 5.2 Air (MLX) | ~34 tok/s | Command R+ 2 (~32 tok/s) |
| M4 Ultra 192 GB | GLM 5.2 Air | ~38 tok/s | Llama 5 405B Q2 (~5 tok/s) |

**The 24 GB sweet spot is Qwen 4.1.** For users on base-tier MacBook Pro hardware, the question "what's the best model I can run?" has a clean answer: `ollama run qwen4.1:32b-a3b`. The 80% SWE-Verified score, Apache 2.0 license, and 62 tok/s make it the single best capability-per-Mac-dollar pick in July 2026.

**The 64 GB tier just got a frontier model.** If you have a 64 GB Mac, GLM 5.2 Air at ~30 tok/s is the headline change of the month — 58% on SWE-Bench Pro on a machine you can carry. For the first time, frontier-adjacent agentic coding is a local, offline reality on consumer Apple Silicon.

---

## What's coming next month

Speculative section — this is what LLMCheck is watching for in the next 30 days based on public roadmaps, leaked release notes, and credible community signals.

* **Qwen 5 Preview.** Alibaba's cadence (Qwen 3 to 4 was seven months) points to a Qwen 5 Preview in late August or early September. Expect another architectural rebuild rather than an MoE refinement — and given Qwen 4.1's lead, the bar Alibaba is setting for itself is high.
* **GLM 5.2 full distillation variants.** Zhipu shipped the flagship and the Air distillation simultaneously. Community signals suggest a smaller GLM 5.2 "Flash" variant (~30B-class) targeting the 24 GB Mac tier is in the works. If it lands and retains even 50% SWE-Bench Pro, it would directly challenge Qwen 4.1 for the Mac-runnable crown.
* **Apple MLX 2.0.** The MLX team has been signaling a 2.0 release with first-party fine-tuning APIs, a stabilized graph compiler, and optimized kernels for the M5 series. If MLX 2.0 lands, expect a measurable tok/s lift across every model on Apple Silicon — a free speed upgrade for the entire ecosystem, and especially valuable for the new Air-class distillations.
* **DeepSeek V5.** DeepSeek's V-series (general-purpose) trails its R-series reasoning cadence by roughly two months. With R3 out, a V5 release targeting broad capability and a more Mac-friendly active-parameter count is plausible for August. A V5 with an Air-class distillation would be a major event for the 64 GB tier.

**Watch list:** The single most consequential possible August release is a sub-32B distillation of a frontier model that beats Qwen 4.1 on SWE-Verified at 24 GB. GLM 5.2 Flash is the leading candidate. If any lab ships an MIT or Apache 2.0 model above 80% SWE-Verified that runs on a 24 GB Mac, the consumer leaderboard resets again.

> [paraphrased] Author box: the LLMCheck Research Team benchmarks local AI models on
> Apple Silicon hardware; the database covers 79+ open and closed models with
> standardized tok/s measurements via Ollama, LM Studio, and MLX.

## Frequently Asked Questions

### What's the best open-source local LLM in July 2026?

According to the LLMCheck index (July 2026), the best open model overall is GLM 5.2 (744B-A40B), the first open-weights model to beat GPT-5 and Claude on SWE-Bench Pro at 68.5% — but it is server-class. For a model you can actually run on a Mac, Qwen 4.1 32B-A3B is the #1 pick with an LLMCheck Score of 76: 80% SWE-Verified, Apache 2.0, and ~62 tok/s on a 24 GB M4 Pro.

### Is GLM 5.2 really the first open model to beat GPT-5 and Claude?

Yes, on SWE-Bench Pro. GLM 5.2 from Zhipu AI scores 68.5% on SWE-Bench Pro, edging out the published scores for GPT-5 and Claude on the same agentic-coding benchmark — the first time an MIT-licensed open-weights model has led a frontier closed model on a hard agentic-coding eval. It is a 744B-A40B mixture-of-experts model, so it is server-class, but the 106B-A12B GLM 5.2 Air distillation brings most of that capability to a 64 GB Mac.

### Can I run GLM 5.2 on a Mac?

Not the full GLM 5.2 (744B-A40B) — that needs a multi-GPU server or an 8-bit cluster. But GLM 5.2 Air (106B-A12B) runs on a 64 GB Mac at roughly 30 tok/s at Q4_K_M, and reaches ~34 tok/s on a 128 GB Mac Studio via MLX and ~38 tok/s on an M4 Ultra 192 GB. Air retains 58% on SWE-Bench Pro, making it the most capable frontier-adjacent model you can run on consumer Apple Silicon as of July 2026.

### What changed in Qwen 4.1 vs Qwen 4?

Qwen 4.1 32B-A3B is a refinement of Qwen 4, not a new architecture. SWE-Verified climbs from 78% to 80%, tool-use reliability improved, and Mac speed ticked up to ~62 tok/s on an M4 Pro 24 GB (vs ~60 for Qwen 4). It keeps the Apache 2.0 license and 1M native context. According to the LLMCheck index the LLMCheck Score rises from 75 to 76, making Qwen 4.1 the new Mac-runnable #1.

### DeepSeek R3 vs Llama 5 405B vs Kimi K3 — which frontier model is best?

All three are server-class. DeepSeek R3 (685B-A37B, MIT) leads on reasoning with 95% on AIME 2025 and is the math/reasoning champion. Llama 5 405B (dense, Llama 5 license) leads broad knowledge at 91% MMLU but is the hardest to serve. Kimi K3 (~1T-A32B, MIT) is the agentic-coding leader for long-horizon tool-use tasks. For most teams, DeepSeek R3 offers the best capability-per-dollar; for autonomous coding agents, Kimi K3 edges ahead.

### What's the best local LLM for a 24 GB Mac in July 2026?

Qwen 4.1 32B-A3B. Its MoE structure means only 3B parameters are active per token, so it uses ~19 GB at Q4_K_M and runs at ~62 tok/s on a base M4 Pro 24 GB MacBook Pro while scoring 80% on SWE-Verified. According to the LLMCheck index, the 24 GB tier is the sweet spot of the July 2026 market — frontier-adjacent capability at production-usable speed on entry-tier pro hardware.

### Can I run Llama 5 405B on Apple Silicon?

Barely. Llama 5 405B is a 405B dense model, so even at Q2 it needs roughly 150 GB of unified memory. An M4 Ultra Mac Studio with 192 GB can technically load it at Q2 and runs it at about 5 tok/s — usable for batch jobs, far too slow for interactive chat. For real frontier capability on a Mac, GLM 5.2 Air at ~30-38 tok/s is the far more practical choice.

### Why are Chinese labs leading the open frontier in July 2026?

Three of the four frontier-class open releases this month came from Chinese labs: GLM 5.2 (Zhipu), DeepSeek R3 (DeepSeek), and Kimi K3 (Moonshot). All three ship under MIT. They have combined aggressive MoE scaling with permissive licensing, and GLM 5.2 became the first open model to beat GPT-5 and Claude on SWE-Bench Pro. Meta's Llama 5 405B is the lone Western frontier entrant, and it ships under a more restrictive license.

### Has 1M context become standard for open models?

Yes. Qwen 4.1, Gemma 4.5 27B, GLM 5.2, and DeepSeek R3 all ship with 1M-class native context windows. Six months ago 256K was the open-source ceiling; in July 2026 a 1M token window is the spec-sheet expectation rather than a differentiator. Gemma 4.5 27B in particular pairs its 1M context with strong retrieval accuracy, making it a top pick for long-document analysis on a 32 GB Mac.

### Is open source now ahead of closed models on coding?

On agentic coding, for the first time, yes at the frontier. GLM 5.2's 68.5% on SWE-Bench Pro beats the published GPT-5 and Claude scores. On Mac-runnable hardware, Qwen 4.1's 80% SWE-Verified is at or above the closed leaders. Closed models still hold an edge in long-horizon reliability, multimodal breadth, and production tool-use uptime, but the agentic-coding crown moved to open weights in July 2026.

### Sources & References

* [Zhipu AI — GLM 5.2 & GLM 5.2 Air model cards](https://huggingface.co/zai-org)
* [Qwen Team — Qwen 4.1 release notes](https://qwenlm.github.io/blog/)
* [DeepSeek — R3 technical report](https://api-docs.deepseek.com/)
* [Meta — Llama 5 405B model card & community license](https://ai.meta.com/llama/)
* [Moonshot AI — Kimi K3 announcement](https://huggingface.co/moonshotai)
* [Google — Gemma 4.5 27B refresh notes](https://blog.google/technology/ai/)
* [Mistral — Medium 4 announcement](https://mistral.ai/news/)
* [Microsoft Research — Phi-5 Large technical report](https://huggingface.co/microsoft)
* [SWE-bench — SWE-Bench Pro & Verified methodology](https://www.swebench.com/)
* [Ollama Library — model weights & quantization](https://ollama.com/library)
* [LLMCheck Methodology — scoring formula & benchmark process](https://llmcheck.net/methodology)
* [LLMCheck Open Data — benchmark measurements (CSV/JSON)](https://llmcheck.net/data/)

## Capture gaps

* **Every benchmark number on this page is single-source.** The page states outright
  that "every claim is sourced from LLMCheck's own measurement pipeline" — the
  headline (GLM 5.2 beating GPT-5 and Claude on SWE-Bench Pro at 68.5%) is LLMCheck's
  own cross-reference, not a published third-party result. Treat the whole page as
  **claimed, not verified**.
* **The Kimi K3 specs are contradicted by primary sources** — see the `> [contradiction]`
  block above. LLMCheck's release-date and parameter figures for K3 are wrong against
  Moonshot's own technical report. This casts doubt on the rest of the spec table; the
  per-Mac-tier tok/s measurements (LLMCheck's actual instrument) are the part of this
  page most likely to hold up.
* **Spec cards were reflowed.** The "Architecture" / "Benchmarks" / "Mac Performance"
  blocks rendered from HTML cards as run-together label-value text (`Total params744B`).
  Values are preserved verbatim; only the table markup is reconstructed.
* **Commercial disclosure stripped.** The page carries an Amazon affiliate "Where to
  buy" block and a "Related Articles" / product-wizard CTA, removed here as chrome.
  Noted because the affiliate relationship is context for hardware recommendations.
* Section-divider images and the site's own leaderboard widget were not captured
  (0 images downloaded); `source.html` in the raw folder holds the full original.
