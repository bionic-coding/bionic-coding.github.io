---
title: "Open-Weights Models — 2026 Landscape"
slug: open-weights-landscape-2026
type: references
tags: [open-weights, local-llms, licensing, benchmarks, apple-silicon, claimed-vs-verified]
sources: [state-of-open-source-local-llms-july-2026, willison-kimi-k3, willison-inkling, raschka-notable-open-weight-models, qwen3-8-open-weight-announcement, kimi-k3-technical-report, kimi-k3-docs, qwen3-8-max-preview-fact-sheet, qwen3-8-max-a-new-bar-for-coding-and-cowork, qwen3-8-max-qwencloud-model-page]
last_reviewed: 2026-08-03
---

# Open-Weights Models — 2026 Landscape

A running reference for the **open-weights** side of the model landscape — the models you can download and run, as opposed to the API-only frontier tracked in [[research/references/frontier-models-2026]]. Built to back the Articles column and a possible "what can I actually run" lesson.

**Read the claimed-vs-verified marking on every number here.** July 2026 produced an unusual volume of open-weight releases and an unusual volume of vendor superlatives to go with them. Where a figure is a lab's own claim or a single outlet's index, this page says so. That distinction is the substance, not a disclaimer.

## The trust ladder for these sources

Sorted by how much weight a claim from each deserves:

1. **Vendor technical reports** — [[research/sources/kimi-k3-technical-report]]. Methodology stated, numbers reproducible in principle. Still vendor-run.
2. **Named independent practitioners** — [[research/sources/willison-kimi-k3]], [[research/sources/willison-inkling]], [[research/sources/raschka-notable-open-weight-models]]. First-hand measurements, small scope, explicit about limits.
3. **Vendor launch posts with a full benchmark table and footnotes** — [[research/sources/qwen3-8-max-a-new-bar-for-coding-and-cowork]]. Weaker than a technical report (no architecture detail, no training description), stronger than a tweet: the harness, the effort level, and the caveats are stated, and roughly a quarter of the rows are in-house benchmarks nobody else can run.
4. **Vendor serving pages** — [[research/sources/qwen3-8-max-qwencloud-model-page]]. Authoritative for price, context, and rate limits; marketing copy for anything else.
5. **Aggregator indexes** — [[research/sources/state-of-open-source-local-llms-july-2026]]. Broad coverage, single proprietary methodology, commercial incentives (affiliate hardware links).
6. **News reports of vendor announcements** — [[research/sources/qwen3-8-open-weight-announcement]]. Repeats a claim; adds no measurement.
7. **Vendor tweets** — the July Qwen 3.8 "second only to Fable 5" claim. Citable as a claim only, and now superseded by the launch post's own table (below).

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

## Qwen3.8-Max (Alibaba) — launched 2 August; weights still pending

Sources: [[research/sources/qwen3-8-max-a-new-bar-for-coding-and-cowork]] (Qwen Team launch post, 2026-08-02) and [[research/sources/qwen3-8-max-qwencloud-model-page]] (serving page, captured 2026-08-03), superseding the announcement-stage captures [[research/sources/qwen3-8-open-weight-announcement]] (GIGAZINE, 21 July) and [[research/sources/qwen3-8-max-preview-fact-sheet]] (20 July).

**Read the first bullet before writing the word "released."**

- **The API launched; the weights did not.** The post is unambiguous: "the open weights will be released next week," on Hugging Face and ModelScope. As of the 2026-08-03 capture there is **no downloadable Qwen3.8-Max and still no named license.** This is the **third** deferral — "soon" on 19 July, "soon" again on 21 July, "next week" on 2 August. Alibaba has earned the hedge; check the repos before calling this an open-weights model.
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

The downstream-community argument, concretely: because Qwen 3.6 was open, volunteers shipped **"Bonsai 27B" on 14 July** — Qwen3.6-27B shrunk to a 3.9 GB memory footprint, running on an iPhone. Nothing comparable can happen to 3.8 until the weights land. And the open/closed zigzag is still the reason to wait for them: **3.5 and 3.6 open, 3.7 closed-only, 3.8 promised open.**

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

**Permissive licensing is now the default, not a differentiator.** MIT or Apache 2.0 covers 9 of LLMCheck's top 10; Inkling is Apache 2.0; K3 is MIT. The outliers are Meta's Llama 5 license and Cohere's CC-BY-NC. Independently corroborated in kind by Raschka's six releases. Qwen 3.8's license remains unannounced — the open question, given the 3.7 closed-only detour.

**1M context is the spec-sheet floor.** Claimed across Qwen 4.1, Gemma 4.5, GLM 5.2, DeepSeek R3, Laguna S 2.1, and Kimi K3. Six months ago 256K was the ceiling. Differentiation has moved to retrieval accuracy at depth, which none of these sources measures.

**Chinese labs lead the open frontier; the US answer is arriving.** Moonshot, Zhipu, DeepSeek and Alibaba hold the top of the open leaderboards. Inkling is the notable counter-move — and its lab says outright it is not frontier-class.

**Benchmark claims are outrunning benchmark evidence — and the pattern now has a control case.** Three separate "beats Fable 5" claims appear in these sources: Qwen 3.8's July tweet, GIGAZINE's characterization of K3, and LLMCheck's GLM 5.2 headline. **Both labs that eventually published detail — Moonshot's technical report and Alibaba's launch table — concluded something more modest about their own models than their marketing had.** Qwen's own table shows Fable 5 ahead on most coding rows, including three of Qwen's four in-house coding benchmarks. The lesson is not that vendors lie; it is that **the gap between the tweet and the table is where the story is**, and waiting two weeks costs nothing.

**Price is now the open-weights differentiator, not capability.** Qwen3.8-Max at **$2 / $6** undercuts every frontier API on this page while landing mid-pack on coding benchmarks. K3 went the other way — $3 / $15, the most expensive Chinese-lab model to date. Whatever "open" comes to mean commercially, the two leading Chinese labs are betting opposite ways on it.

**Willison's methodological warning, worth quoting directly:** the pelican benchmark's correlation with model quality "has been mostly severed," and its biggest limitation is that "it doesn't touch at all on the thing that matters most for today's model: agentic tool calling and the ability to operate tools reliably as conversations grow in length." Applies to every casual benchmark, not just his.

## Open questions

- **Did Kimi K3's weights ship by 27 July 2026?** No captured source confirms it. Check `huggingface.co/moonshotai` before making any claim about downloadable K3.
- **What license do the K3 weights carry?** The technical report links the repo but never names a license. LLMCheck says MIT — a source with a demonstrated K3 error.
- **✅ Resolved (2026-08-03) — Qwen3.8-Max's active parameter count, context window, and pricing.** 95B active of 2.4T; 1M context; $2 / $6 per MTok. See the section above.
- **Did Qwen3.8-Max's weights ship?** Promised for the week of 2026-08-09 on Hugging Face and ModelScope. This is the third deferral. **Check `huggingface.co/Qwen` and ModelScope before describing 3.8 as downloadable.**
- **What license will the Qwen3.8-Max weights carry?** Still unnamed in every capture — and given the 3.7 closed-only detour, not safely assumable as Apache 2.0.
- **Does anything outside Alibaba corroborate the Qwen3.8-Max table?** No independent benchmark, Artificial Analysis entry, or hands-on review is captured. Willison or Artificial Analysis on 3.8 is the cheapest next ingest.
- **Is GLM 5.2's SWE-Bench Pro result reproducible outside LLMCheck's index?** Nothing captured corroborates it. A GLM 5.2 primary source (Zhipu model card) is the obvious next capture.
- **Inkling's model card and Raschka's Inkling/K3 architecture notes** are all uncaptured and directly cited by the sources here — the cheapest next ingests.
