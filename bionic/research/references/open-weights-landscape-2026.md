---
title: "Open-Weights Models — 2026 Landscape"
slug: open-weights-landscape-2026
type: references
tags: [open-weights, local-llms, licensing, benchmarks, apple-silicon, claimed-vs-verified]
sources: [state-of-open-source-local-llms-july-2026, willison-kimi-k3, willison-inkling, raschka-notable-open-weight-models, qwen3-8-open-weight-announcement, kimi-k3-technical-report, kimi-k3-docs, qwen3-8-max-preview-fact-sheet, qwen3-8-max-a-new-bar-for-coding-and-cowork, qwen3-8-max-qwencloud-model-page, glm-5-3-frontier-coding-with-emergent-cyber-capabilities, deepseek-v4-pro-0813-model-card, deepseek-v4-pro-0813-fireworks-model-page, qwen3-8-2-4t-a95b-open-weights-release, qwen3p8-max-fireworks-model-page]
last_reviewed: 2026-08-15
---

# Open-Weights Models — 2026 Landscape

A running reference for the **open-weights** side of the model landscape — the models you can download and run, as opposed to the API-only frontier tracked in [[research/references/frontier-models-2026]]. Built to back the Articles column and a possible "what can I actually run" lesson.

**Read the claimed-vs-verified marking on every number here.** July 2026 produced an unusual volume of open-weight releases and an unusual volume of vendor superlatives to go with them. Where a figure is a lab's own claim or a single outlet's index, this page says so. That distinction is the substance, not a disclaimer.

## The trust ladder for these sources

Sorted by how much weight a claim from each deserves:

1. **Vendor technical reports** — [[research/sources/kimi-k3-technical-report]]. Methodology stated, numbers reproducible in principle. Still vendor-run.
2. **Named independent practitioners** — [[research/sources/willison-kimi-k3]], [[research/sources/willison-inkling]], [[research/sources/raschka-notable-open-weight-models]]. First-hand measurements, small scope, explicit about limits.
3. **Vendor launch posts with a full benchmark table and footnotes** — [[research/sources/qwen3-8-max-a-new-bar-for-coding-and-cowork]], [[research/sources/glm-5-3-frontier-coding-with-emergent-cyber-capabilities]]. Weaker than a technical report (no architecture detail, no training description), stronger than a tweet: the harness, the effort level, and the caveats are stated, and some of the rows are in-house benchmarks nobody else can run. **Vendor HF model cards sit on this rung too** — [[research/sources/deepseek-v4-pro-0813-model-card]] and [[research/sources/qwen3-8-2-4t-a95b-open-weights-release]] carry full tables with footnotes, plus the architecture spec a launch post omits.
4. **Vendor serving pages** — [[research/sources/qwen3-8-max-qwencloud-model-page]], [[research/sources/deepseek-v4-pro-0813-fireworks-model-page]], [[research/sources/qwen3p8-max-fireworks-model-page]]. Authoritative for price, context, and rate limits; marketing copy for anything else.
5. **Aggregator indexes** — [[research/sources/state-of-open-source-local-llms-july-2026]]. Broad coverage, single proprietary methodology, commercial incentives (affiliate hardware links).
6. **News reports of vendor announcements** — [[research/sources/qwen3-8-open-weight-announcement]]. Repeats a claim; adds no measurement.
7. **Vendor tweets** — the July Qwen 3.8 "second only to Fable 5" claim. Citable as a claim only, and now superseded by the launch post's own table (below).

## GLM-5.3 (Z.ai / Zhipu) — launched 14 August; weights promised within two weeks

Source: [[research/sources/glm-5-3-frontier-coding-with-emergent-cyber-capabilities]] (launch post, 2026-08-14). **Every number below is a vendor claim from Z.ai's own runs** — but the post states a harness and parameters for every row in its footnotes, which puts it on trust-ladder rung 3.

- **A post-training-only release.** Same base model as GLM-5.2; "every gain comes from post-training." The hero subtitle is the whole thesis: "Scaling post-training is all we did for GLM-5.3."
- **Weights did NOT ship at launch.** "We will release the weights in two weeks after launch, once safety evaluation and hardening are complete" — due ~2026-08-28. The page's Hugging Face link is a `#` placeholder. No license named (GLM 5.2 was MIT per LLMCheck; do not assume 5.3 follows).
- **Claimed: the most capable open-weights coding model.** +50% over GLM-5.2 on the in-house Z.ai Code Bench (private, contamination-controlled, nobody else can run it), and open-source SOTA on Terminal Bench 3.0 (28.3 vs Kimi K3's 17.4) and Agents' Last Exam (28.5 vs K3's 27.6, DeepSeek-V4-Pro-0813's 25.7). In its own table it beats both open rivals on nearly every row. **The frontier still leads, though:** Fable 5 ahead on Terminal Bench 3.0 (33.7), DeepSWE (69.7), FrontierSWE (88.2), ProgramBench (33), PostTrainBench (41.8); GPT-5.6 Sol ahead on DeepSWE (72.7) and TB3.0 (34.6). The open-weights-SOTA claim survives the table; a frontier-SOTA claim would not.
- **The headline is emergent cyber capability — carry the caveats.** Vulnerability-discovery data entered post-training and the capability "developed faster than we expected": **CyberGym 84.5, best on the benchmark**, ahead of the 83.8 the post attributes to Mythos 5 and GPT-5.6 Sol's 83.6. Further up the exploitation chain the closed frontier stays well ahead: **ExploitBench 54.4 vs Mythos 5's 78.0**, **ExploitGym 105/130 tasks (2h/6h) vs Mythos 5's 181/247**. Z.ai's own summary: "Capability is growing fastest exactly where we are furthest behind."
  - **Labeling quirk:** the cyber-table column headed "Fable 5 (w/ fallback)" carries the scores the body text attributes to **Mythos 5**. Read those cells as Mythos 5.
  - **Internal inconsistency:** the body says "Mythos 5 remains well ahead at 181 and 247 tasks" on ExploitGym, but the same table's GPT-5.6 Sol column reads **216 / 293** — higher. Cite the table, not the sentence.
- **Real-world vulnerability claims:** with several Chinese security teams, the model found **2,436 vulnerabilities across 269 OSS projects** (1,097 medium-to-high severity; oldest ~40 years). Public record at the Z.ai Security Disclosure Ledger (cvd.z.ai): per the dashboard embedded in the post, 53 publicly disclosed, 2,383 under embargo. Claimed, single-source, unaudited — but the ledger is a checkable artifact.
- **Cross-vendor corroboration — the best this week's captures offer:** Z.ai's rows for DeepSeek-V4-Pro-0813 (TB2.1 87.9, DeepSWE 62.7, CyberGym 83.3) and Qwen3.8-Max (TB2.1 86.6, DeepSWE 56.6) **exactly match what DeepSeek and Qwen publish for themselves**. Three vendors' tables agreeing on shared rows is the closest thing to verification available. (Harness-dependent rows still diverge: Fable 5's TB2.1 is 88 in Z.ai's Claude Code run, 84.6 in Qwen's Terminus-2 figure.)
- **API changes:** thinking is now always-on (`thinking.type: "disabled"` removed — breaking migration), effort levels `low`/`high`/`max` with `max` default. GLM Coding Plan moved to a points-based quota with 50% off-peak pricing (peak 14:00–18:00 UTC+8 weekdays).

## DeepSeek-V4-Pro-0813 (DeepSeek) — official release, MIT, 13 August

Source: [[research/sources/deepseek-v4-pro-0813-model-card]] (HF model card, release dated 2026-08-13 by name suffix). All benchmark figures vendor-run (DeepSeek Harness, `max` effort) — claimed, not independently verified.

- **The official release of DeepSeek-V4-Pro**, superseding the preview, "with greatly enhanced agentic capabilities and performance improvements that are especially pronounced in production environments." Built on the preview structure **with a DSpark speculative decoding module attached** — the draft weights come from the same checkpoint (no separate draft model; one flag in vLLM or SGLang enables it).
- **MIT license** — stated twice on the page. The most permissive license among this week's three releases (Qwen went custom; GLM-5.3's is unnamed).
- **Scale: 1.7T params** (HF spec field only — the card never states it in prose). **Active-parameter count is not disclosed on the card**; the uncaptured technical report (arXiv 2606.19348, "DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence") is where that lives. Context likewise: only the paper title's "Million-Token" and a recommended **384K max output** at high/max effort.
- **DeepSeek's own verdict: "broadly competitive with the strongest proprietary models available."** Their table is more precise: V4-Pro **beats** Opus 4.8 and Fable 5 on CyberGym (83.3 vs 78.3 / 83.1), AutomationBench (31.8 vs 27.2 / 29.1), and is 0.1 pt behind K3 on Terminal Bench 2.1 (87.9 vs 88.3). It **trails** Fable 5 on HLE (42.7/60.0 vs 53.3/63.0) and DeepSWE (62.7 vs 70.0), and Opus 4.8 on NL2Repo (61.5 vs 69.7) and DSBench-Hard (67.2 vs 71.7). The preview→official jump is the big number: DeepSWE 12.8 → 62.7, CyberGym 52.7 → 83.3, TB2.1 72.1 → 87.9.
- **Three reasoning-effort levels — `low`, `high`, `max`** — same shape as Qwen3.8's and GLM-5.3's; the single-"max" era (K3) is now the exception.
- **Cross-vendor corroboration:** Z.ai's GLM-5.3 table (captured the same day) reproduces DeepSeek's self-reported TB2.1 87.9, DeepSWE 62.7, and CyberGym 83.3 exactly.
- **Serving recipe:** a single **4×GB300 node** with vLLM (fp8 KV cache, expert parallel, DSpark with 7 speculative tokens); SGLang cookbook variant with mxfp4. 19,945 HF downloads in the first month; six community quantizations already listed.
- **Third-party hosting (Fireworks, [[research/sources/deepseek-v4-pro-0813-fireworks-model-page]]):** serverless at **$1.32 / $0.044 / $3.96 per MTok** (input / cached input / output), **1040k context**, function calling and LoRA fine-tuning supported, listing created 8/13/2026. That is **the cheapest frontier-scale serving captured in this wiki so far** — under Qwen3.8-Max's $2 / $6 and K3's $3 / $15 on both input and output. Its spec field says **1.6T** params against the HF card's 1.7T — an unresolved host-vs-lab discrepancy. The 1040k figure is also the first explicit V4-Pro context number captured.

## Kimi K3 (Moonshot) — the spec conflict, resolved

**Resolved facts** (agreed by Moonshot's technical report and Willison's same-day writeup):

- **2.8T total parameters, 104B activated per token.** Moonshot markets this as the first "open 3T-class model," rounding up.
- **1M-token context**, native vision, thinking always on.
- **Announced 16 July 2026**; open-weight release promised "by July 27, 2026."
- **$3 / $15 per MTok** — Sonnet-tier pricing, and per Willison "the most expensive model released by a Chinese AI lab to date," up from K2.6's $0.95 / $4.
- **Moonshot's own verdict:** K3 "still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol."

> [contradiction] [[research/sources/state-of-open-source-local-llms-july-2026]] states
> Kimi K3 is "~1T-A32B, Jul 7, 2M context, 66% SWE-Bench Pro." Every one of those four
> figures disagrees with Moonshot's own technical report and with Willison. **Use the
> technical report.** LLMCheck's K3 row should be treated as an error, and its presence
> is a reason to discount LLMCheck's other spec-table entries — though not necessarily
> its per-Mac-tier speed measurements, which are its own instrument.
>
> A third date exists: [[research/sources/qwen3-8-open-weight-announcement]] says K3 was
> "released on July 17." Willison, writing on the 16th as it happened, is the better
> source for the announcement date.

**Independent corroboration worth citing** (Artificial Analysis, quoted by Willison): Elo **1547** on a private long-horizon knowledge-work evaluation, "+732 points from Kimi K2.6 and behind only Claude Fable 5"; cost per task **$0.94** vs GPT-5.6 Sol's $1.04 and Opus 4.8's $1.80; 21% fewer output tokens than K2.6. K3 also led Arena.ai's Frontend Code arena, above Fable 5.

**Two hands-on details from Willison that no vendor document contains:**

- K3 ships with **one reasoning effort level, "max"** — and it is expensive as a result. A single SVG-pelican prompt burned 13,241 reasoning tokens to produce 3,417 tokens of output, costing 25 cents.
- Token counts suggest an **~85-token hidden system prompt** (prompting "hi" counted 86 tokens). Willison flags this as an inference, and the model refused to leak it.

**Did the weights ship on time?** Unresolved. Raschka, writing **26 July**, still says "everyone is waiting for the Kimi K3 and Ling 3.0 weights to land on the model hub any day now" — one day before Moonshot's own deadline. No captured source confirms the release. **Check the Hugging Face repo before writing that K3 weights are available.**

## Inkling (Thinking Machines Lab) — the US open-weights entrant

Source: [[research/sources/willison-inkling]] (16 July 2026). A link post, so the specs are quoted from Thinking Machines' announcement rather than independently verified.

- **975B total / 41B active MoE**, Apache 2.0, multimodal (text, images, audio, video), trained on **45 trillion tokens**. First open-weights model from Mira Murati's lab.
- **Inkling-Small (276B / 12B active)** promised, weights pending "once that work is complete."
- **The lab disclaims frontier status in its own words** — "Inkling is not the strongest overall model available today, open or closed. Instead, a combination of qualities makes it a good open-weights base for customization." It is positioned as a fine-tuning base for their Tinker platform.
- **The training-data documentation is the story.** Willison notes the model card is "much shorter than I've come to expect from US AI labs," and its data documentation reduces to two boilerplate paragraphs saying the data includes public-domain content and content "that may be subject to intellectual property protection." A concrete, citable example for anything written about training-data transparency.
- **Why it matters strategically:** Willison frames it as "a new viable contender to join NVIDIA Nemotron and Gemma 4" — i.e. the US open-weights ecosystem, which had thinned as Chinese labs took the lead.

A self-disclaimed non-frontier model is the rarest thing in this file: a vendor claim that undersells. Cite it as the counterexample when writing about benchmark hype.

## Qwen3.8 (Alibaba) — weights SHIPPED under a custom license; API since 2 August

Sources: [[research/sources/qwen3-8-2-4t-a95b-open-weights-release]] (HF model card, weights live, captured 2026-08-15 — **now the authoritative source**), [[research/sources/qwen3p8-max-fireworks-model-page]] (third-party hosting, 2026-08-15), [[research/sources/qwen3-8-max-a-new-bar-for-coding-and-cowork]] (Qwen Team launch post, 2026-08-02) and [[research/sources/qwen3-8-max-qwencloud-model-page]] (serving page, 2026-08-03), superseding the announcement-stage captures [[research/sources/qwen3-8-open-weight-announcement]] (GIGAZINE, 21 July) and [[research/sources/qwen3-8-max-preview-fact-sheet]] (20 July).

- **✅ The weights shipped — on the fourth promise.** "Soon" on 19 July, "soon" on 21 July, "next week" on 2 August — and the `Qwen/Qwen3.8-2.4T-A95B` repo was live on Hugging Face by the 2026-08-15 capture: weights + config in HF Transformers format (xet), 6,381 downloads in the first days, 18 community quantizations and 2 finetunes already listed, Together AI as listed inference provider. The deferral streak is over; this is now an open-weights model in the mechanical sense.
- **The license is the catch: `qwen3.8-max` — a custom license, not Apache 2.0 or MIT.** The HF license field carries the name of the API model. The license text itself is not captured; **read it before any commercial-use or redistribution claim.** After MIT (K3, DeepSeek-V4-Pro-0813, GLM 5.2 per LLMCheck), this is the first restrictive-looking move of the season — and the 3.7 closed-only detour makes it less surprising.
- **What exactly shipped: the text-only base of Qwen3.8-Max, not the Max feature set.** The card is explicit: **Qwen3.8-Max is "the official version based on Qwen3.8-2.4T-A95B with more features, such as vision input & non-thinking support, 1M context length by default, official built-in tools."** The released weights are **text-only, thinking cannot be disabled**, context is **262,144 natively, extensible to 1,010,000** — so the 1M/991K-input figures captured from QwenCloud belong to the API version, not the default open artifact.
- **Architecture — disclosed for the first time.** 2.4T total / 95B active; 92 layers, hidden dim 8192; **hybrid hidden layout: 23 × (3 × (Gated DeltaNet → MoE) → 1 × (Gated Attention → MoE))** — a 3:1 linear-attention-to-full-attention pattern, DeltaNet-style heads (128 V / 16 QK, dim 128) alongside gated attention (64 Q / 4 KV, dim 256); **512 experts, 10 routed + 1 shared active**, expert intermediate dim 2048; multi-token prediction trained with multiple steps. Built on the Qwen3.5 foundation. The ~4.0% activation ratio stands, and the hybrid attention is the notable structural choice at 2.4T scale.
- **Benchmark table re-published with the weights**, identical Qwen3.8-Max column to the launch post (corroboration, not new claims) plus a **Qwen3.7-Max column** showing the generational gap (FrontierSWE 40.7 → 73.5, DeepSWE 21.6 → 56.6, TB2.1 74.5 → 86.6) and general-capability rows (GPQA Diamond 92.6, IFBench 82.8, HealthBench 60.2, MRCR v2 256K 92.9). Same footnotes, same "Fable5 results may involve fallbacks" caveat. HF's eval-results widget adds third-party-hosted numbers matching the card (DeepSWE 56.6, SWE-bench Pro 67.7, GPQA Diamond 92.6, HLE 43.6) plus WildClawBench 56.2.
- **Recommended sampling:** temperature 1.0, top_p 0.95, top_k 20; `reasoning_effort` xhigh (default) / medium / low; `preserve_thinking` on by default; budget 262K reasoning + 131K final output within the 1M extended context.
- **Third-party hosting (Fireworks, [[research/sources/qwen3p8-max-fireworks-model-page]]):** serverless at **$2.00 / $0.25 / $6.00 per MTok** — matching QwenCloud's $2/$6 and $0.25 cache pricing exactly — with **262k context** (the native window, not the API's 1M), function calling, no fine-tuning; listing created 8/12/2026. **The anomaly worth a sentence in anything written:** Fireworks' `fireworks/qwen3p8-max` URL serves this open-weights listing (model path `qwen3p8-2p4t-a95b`) — the hosted "max" entry now points at the released weights.
- **Scale — RESOLVED.** **2.4T total parameters, 95B active** ("2.4T parameters (95B active)"), ~4.0% activation. That active-param count is the number two weeks of captures kept failing to produce, and it puts Qwen3.8-Max in the same serving class as Kimi K3 (2.8T / 104B).
- **Price is the story the benchmark table buries: $2 / $6 per MTok.** Against Kimi K3's $3 / $15, Opus 5-class $5 / $25, GPT-5.6 Sol's $5 / $30, and Fable 5's $10 / $50, that is **an eighth of Fable's output price**. Implicit cache reads are $0.25; explicit cache reads $0.17.
- **Serving specs (from the QwenCloud page):** 1M context — 991K max input, 131K max output, 262K max reasoning (983K input with thinking). 2M TPM / 15K RPM. Input modalities **image, text, and video**; text output.
- **Three reasoning-effort levels — `xhigh` (default), `medium`, `low`** — and `preserve_thinking` on by default. Worth contrasting with Kimi K3, which ships only a single "max" effort and is expensive as a result.
- **It speaks the Anthropic API protocol.** The post documents `ANTHROPIC_BASE_URL=https://dashscope-intl.aliyuncs.com/apps/anthropic` with `ANTHROPIC_MODEL="qwen3.8-max"` — i.e. a drop-in swap under Claude Code — plus Codex, OpenClaw, Qoder CLI, and Qwen Code configs. The harness lock-in argument gets weaker every month.

### What the benchmark table actually says

The July "second only to Fable 5" tweet is now testable against Alibaba's own numbers, and **on text and coding work it does not hold.** Fable 5 leads Qwen3.8-Max on **9 of the 12 coding-agent rows** and on 6 of 8 general-agent rows.

| row | Opus 4.8 | Fable 5 | GPT-5.6 Sol | Qwen3.8-Max |
|---|---|---|---|---|
| SWE-bench Pro | 69.2 | **80.0** | 64.6 | 67.7 |
| FrontierSWE | 70.0 | **88.8** | -- | 73.5 |
| DeepSWE 1.1 | 59.0 | 70.0 | **73.0** | 56.6 |
| Terminal Bench 2.1 | 84.6 | 84.6 | **88.8** | 86.6 |
| PaperBench | 80.3 | 88.8 | 90.5 | **93.0** |
| HLE (no tools) | 45.7 | **53.3** | 47.2 | 43.6 |
| IFBench | 62.2 | 63.5 | 72.7 | **82.8** |

- **The detail worth the column inches: Fable 5 beats Qwen3.8-Max on three of Qwen's own four in-house coding benchmarks** — QwenSWEBench (86.3 vs 80.7), QwenQoderBench (63.1 vs 58.4), QwenReactBench (1770 vs 1724). A lab publishing its house benchmarks losing to a rival is the opposite of the usual failure mode, and it corroborates Moonshot's similar candour about K3.
- **Where it genuinely leads is multimodal**, and the second table is much stronger for it: OSWorld-Verified **86.1** (top), Parametric CAD Bench **91.5**, LogicVista **91.9**, CountQA **82.4**, Dense200 **87.0** vs Fable 5's 31.1, VLMsAreBiased **88.3** vs 43.8. If a claim about this model survives scrutiny, it is a *visual-agent* claim, not a coding claim.
- **The comparison set omits Claude Opus 5** — both tables stop at Opus 4.8, though the Opus 5 system card is dated 2026-07-24 ([[research/sources/claude-opus-5-system-card]]). Any "beats Anthropic's best" framing is measuring against a superseded model.
- **Carry the footnotes.** Footnote 1 reads **"Fable5 results may involve fallbacks"** — the same caveat Moonshot attached to its Fable 5 column, and a reminder that Fable's safeguard routing to Opus 4.8 contaminates third-party comparisons. Nine benchmark rows are in-house with no public definition (`QwenSWEBench`, `QwenQoderBench`, `QwenReactBench`, `QwenSVGBench`, `CoWorkBench`, `QwenBlenderBench`, `QwenVisualOffice`, `RecreationBench`, E-Commerce Bench).

### The agentic showcases — vendor-run, unreproducible, and interesting anyway

None of these are benchmarks; all are single unaudited runs. Cite them as *what Alibaba says it did*, never as measurements.

- **10+ days of autonomous coding.** The model built `oh-my-cli` from an empty folder; the repo (`qwen-code-dev-bot/oh-my-cli`) accumulated **265 commits, 127 PRs, and 151 issues over ~16 days** of claimed fully autonomous operation. The trace is public, which makes this the one showcase a reader could actually audit.
- **Paper reproduction, then improvement.** ~125 hours unattended, ~7,600 lines of code, 33 rounds of GPU training; reproduced the paper's six findings, then evolved a method claimed to beat it by **+2.7 points on AIME24**.
- **A live Tianchi competition** against 526 human teams: accuracy climbed 0.60 → **0.853** across 45 submissions, finishing ahead of **458 of 526** teams.
- **Chip design:** drove a GCD/RSA accelerator from 8,298 gates to **678 gates** over ~500 turns, with an 81% die-area reduction after place-and-route.
- **E-Commerce Bench** (365-day simulated operation): final balance **¥416,252**, 38% ahead of second-place GLM 5.2.

### What open weights would still buy

The downstream-community argument, concretely: because Qwen 3.6 was open, volunteers shipped **"Bonsai 27B" on 14 July** — Qwen3.6-27B shrunk to a 3.9 GB memory footprint, running on an iPhone. **As of 2026-08-15 the 3.8 weights have landed** — 18 community quantizations and 2 finetunes were already listed on the HF repo within days — but a 2.4T model is server-class regardless; the Bonsai-style story would need a distilled Qwen3.8 variant, which does not exist yet. The open/closed zigzag resolved as promised: **3.5 and 3.6 open, 3.7 closed-only, 3.8 open** — under a custom license, which is the new open question.

## Architecture notes — six releases in one week

Source: [[research/sources/raschka-notable-open-weight-models]] (26 July). Architecture commentary, **no benchmarks** — Raschka is explicit that he is "still waiting on some more independent performance benchmarks."

| model | shape | the interesting bit |
|---|---|---|
| Nanbeige 4.2 3B | 22 layers run twice (44 effective) | **Looped depth sharing** — 2× compute, same memory. Two passes retained ~75% of standard token efficiency; more passes gave "barely any gains." |
| Laguna S 2.1 (poolside) | 118B sparse MoE, 8B active, 1M context | 36 sliding-window + 12 global gated-GQA layers. Runs on Raschka's DGX Spark in **under 80 GB** — his personal pick of the six. |
| Motif-3-Beta | 314B-A13B sparse MoE | **Grouped Differential Latent Attention** — MLA-style low-rank compression, but heads are grouped and a learned per-group noise head is subtracted for filtering. |
| Solar Open 2 (Upstage) | 250B-A15B hybrid MoE | Interleaves three Kimi Delta Attention layers per GQA layer — KDA spreading beyond Moonshot. |
| Antares 1B (Cisco) | 1B (also 0.3B) | IBM Granite 4.0 backbone + SFT + GRPO for terminal cybersecurity. Task-specific post-training on a genuinely small model. |
| BTL-3 | rank-32 LoRA on Qwen3.6-27B | Coding agents and structured tool use. Raschka: strong benchmarks suggest "LoRA adapters are still a useful tool/technique in 2026" (performance unquantified). |

Two structural signals worth a column paragraph: **Kimi Delta Attention is being adopted by other labs** (Solar Open 2), and **adapters are not dead** — a rank-32 LoRA on a 27B base is competitive for agentic coding, which is the cheap end of customization.

## Running models locally — the Apple Silicon picture

Source: [[research/sources/state-of-open-source-local-llms-july-2026]] (LLMCheck, published 11 July). **This is the weakest-provenance source on this page and the only one with per-hardware measurements.** Every figure below is LLMCheck's own index; the page states so itself. Its Kimi K3 row is demonstrably wrong (above), so treat the spec tables with suspicion and the tok/s measurements — LLMCheck's actual instrument — as the more defensible part.

Claimed-not-verified headline: **GLM 5.2 (744B-A40B, MIT) scores 68.5% on SWE-Bench Pro**, which LLMCheck says edges published GPT-5 and Claude scores — "the first open model to beat GPT-5 and Claude." No third-party confirmation is captured. Willison offers an indirect and *deflating* data point: GLM 5.2's pelican outclasses the GPT-5.6 and Fable 5 pelicans, and "much as I love GLM I don't think that's a Fable-class model."

The practically useful claims, if they hold:

- **24 GB Mac:** Qwen 4.1 32B-A3B — ~19 GB at Q4_K_M, ~62 tok/s on an M4 Pro, 80% SWE-Verified, Apache 2.0.
- **64 GB Mac:** GLM 5.2 Air (106B-A12B, MIT) — ~30 tok/s, retaining 58% SWE-Bench Pro. The claim that matters: frontier-adjacent agentic coding on a laptop.
- **Frontier models are all server-class.** GLM 5.2, DeepSeek R3, Llama 5 405B, Kimi K3 — none run usefully on consumer hardware. Llama 5 405B dense needs ~150 GB even at Q2 and manages ~5 tok/s on a 192 GB M4 Ultra.
- **The pattern to watch:** ship a cluster-scale flagship, then distil an "Air"-class variant that fits a high-RAM Mac. GLM 5.2 did both on the same day.

## Cross-cutting observations

**Permissive licensing is the default — with one new exception.** MIT or Apache 2.0 covers 9 of LLMCheck's top 10; Inkling is Apache 2.0; K3 is MIT; DeepSeek-V4-Pro-0813 is MIT. The outliers were Meta's Llama 5 license and Cohere's CC-BY-NC — and now **Qwen3.8's custom `qwen3.8-max` license**, the first restrictive-looking entry of this release wave (text uncaptured; terms unknown). GLM-5.3's license is still unnamed pending its weights drop.

**1M context is the spec-sheet floor.** Claimed across Qwen 4.1, Gemma 4.5, GLM 5.2, DeepSeek R3, Laguna S 2.1, and Kimi K3. Six months ago 256K was the ceiling. Differentiation has moved to retrieval accuracy at depth, which none of these sources measures.

**Chinese labs lead the open frontier; the US answer is arriving.** Moonshot, Zhipu, DeepSeek and Alibaba hold the top of the open leaderboards. Inkling is the notable counter-move — and its lab says outright it is not frontier-class.

**Benchmark claims are outrunning benchmark evidence — and the pattern now has a control case.** Three separate "beats Fable 5" claims appear in these sources: Qwen 3.8's July tweet, GIGAZINE's characterization of K3, and LLMCheck's GLM 5.2 headline. **Both labs that eventually published detail — Moonshot's technical report and Alibaba's launch table — concluded something more modest about their own models than their marketing had.** Qwen's own table shows Fable 5 ahead on most coding rows, including three of Qwen's four in-house coding benchmarks. The lesson is not that vendors lie; it is that **the gap between the tweet and the table is where the story is**, and waiting two weeks costs nothing.

**Price is now the open-weights differentiator, not capability — and the floor keeps dropping.** DeepSeek-V4-Pro-0813 on Fireworks at **$1.32 / $3.96** (cached input $0.044) undercuts Qwen3.8-Max's **$2 / $6**, which undercut every frontier API on 2 August, while K3 went the other way — $3 / $15, the most expensive Chinese-lab model to date. Three leading Chinese labs, three opposite pricing bets, all within one month.

**Willison's methodological warning, worth quoting directly:** the pelican benchmark's correlation with model quality "has been mostly severed," and its biggest limitation is that "it doesn't touch at all on the thing that matters most for today's model: agentic tool calling and the ability to operate tools reliably as conversations grow in length." Applies to every casual benchmark, not just his.

## Open questions

- **What is DeepSeek-V4-Pro's active-parameter count and context length?** Not on the model card. The technical report arXiv 2606.19348 is the obvious next capture — it would also close the 1.7T (HF) vs 1.6T (Fireworks listing) spec-field discrepancy.
- **Do GLM-5.3's weights ship by ~28 August 2026?** Promised "in two weeks after launch, once safety evaluation and hardening are complete." Check `huggingface.co/THUDM` / Z.ai before describing 5.3 as downloadable — and check the license (5.2 was MIT; 5.3 unnamed).
- **Did Kimi K3's weights ship by 27 July 2026?** No captured source confirms it. Check `huggingface.co/moonshotai` before making any claim about downloadable K3.
- **What license do the K3 weights carry?** The technical report links the repo but never names a license. LLMCheck says MIT — a source with a demonstrated K3 error.
- **✅ Resolved (2026-08-03) — Qwen3.8-Max's active parameter count, context window, and pricing.** 95B active of 2.4T; 1M context; $2 / $6 per MTok. See the section above.
- **✅ Resolved (2026-08-15) — Qwen3.8's weights shipped.** `Qwen/Qwen3.8-2.4T-A95B` is live on Hugging Face (6,381 downloads in the first days). See the Qwen3.8 section.
- **✅ Resolved (2026-08-15) — the Qwen3.8 weights license exists and is custom: `qwen3.8-max`.** Not Apache 2.0, not MIT. **What does the license text actually permit?** The license file itself is not captured — read it before any commercial-use claim. This is the most important uncaptured document in this file right now.
- **Does anything outside Alibaba corroborate the Qwen3.8-Max table?** No independent benchmark, Artificial Analysis entry, or hands-on review is captured. Willison or Artificial Analysis on 3.8 is the cheapest next ingest.
- **Is GLM 5.2's SWE-Bench Pro result reproducible outside LLMCheck's index?** Nothing captured corroborates it. A GLM 5.2 primary source (Zhipu model card) is the obvious next capture.
- **Inkling's model card and Raschka's Inkling/K3 architecture notes** are all uncaptured and directly cited by the sources here — the cheapest next ingests.
