---
title: "Introducing MiMo-V2.6 series"
slug: mimo-v2-6
type: source
source_url: https://mimo.xiaomi.com/mimo-v2-6/article
source_date: 2026-09-22
author: null
captured_at: 2026-09-22
last_source_check: 2026-09-22
raw_path: research/raw/2026-09-22/mimo-v2-6/
previous_captures: []
static: true
tags: [mimo, xiaomi, open-weights, reinforcement-learning, recursive-self-improvement, agentic-coding, benchmarks]
---

# Introducing MiMo-V2.6 series

> **Provenance note.** The canonical landing URL for this launch is
> `https://mimo.xiaomi.com/mimo-v2-6` — a JS-hydrated (Rspress) shell that loads its
> content client-side and returned zero extractable text on first fetch attempt
> (`word_count: 0`, `thin_content: true`). The actual article body is served
> statically at `https://mimo.xiaomi.com/mimo-v2-6/article` (curl-fetchable, ~1,868
> words) and is captured here as `source_url`. Treat the two as the same
> announcement; cite `/article` for content, the bare `/mimo-v2-6` path when
> referring to the canonical landing page a reader would visit.

September 22, 2026. Xiaomi releases and open-sources the **MiMo-V2.6** series: two natively omnimodal models, **MiMo-V2.6-Pro** (most capable to date) and **MiMo-V2.6-Flash** (balance of intelligence, efficiency, cost), plus a rollout of **MiMo-V2.6-Pro-UltraSpeed** (up to 20× faster output at the same quality). The release is framed explicitly as an "exploration of the RSI path: scaling RL compute on verifiable, complex tasks, so the model can continuously expand its capability frontier through exploration and feedback."

## Headline benchmark claim

**MiMo-V2.6-Pro scores 46.32 on the Artificial Analysis Intelligence Index v4.3** (September 2026), "surpassing Kimi K3 and Qwen3.8 Max to become the strongest open-source model to date." API pricing is unchanged from the V2.5 series — "higher intelligence at the same price."

## Scaling RL — training run details

Both models' RL production runs were live-streamed (`https://mimo.xiaomi.com/rl`). In under six days: MiMo-V2.6-Flash and MiMo-V2.6-Pro each completed **30 RL steps over roughly 750k trajectories**, at a cost of **about $0.85M (Flash) and $2.62M (Pro)** respectively. Average pass rate on training tasks rose **25% (Flash) and 12% (Pro)** in relative terms. On **DeepSWE v1.1** (a held-out long-horizon SWE benchmark): Flash rose ~17 points (48.8 → 65.68), Pro rose ~14 points (58.4 → 72.57).

Scaling axes named: (1) larger batches / higher throughput — 1,568 samples per update, up to 1M context length, 3.5–3.7B tokens per step, fully asynchronous architecture; (2) more tasks/richer environments — a multi-task suite spanning coding, general agents, visual, and cyber, mixed across harnesses; (3) more grader compute — relative comparison within each group for finer reward signal. The router was frozen during scale-up "to suppress training drift"; a defense against reward hacking is described spanning "reward design, adversarial evaluation, anomaly detection and cross-checking between verifiers."

The company states it is **open-sourcing "the full technical report, the training environments and the RL code."**

## Capabilities showcased (vendor demos, not benchmarked)

- **"Vibe World"** — extends natural-language-driven programming from software to interactive 3D worlds: game development (image/video/text → 3D scene + interaction logic + iterative visual-feedback refinement), 3D modeling (Blender asset generation), embodied simulation (multi-view camera input driving a Franka Panda robotic arm for grasping/placement tasks).
- **Visual & design** — frontend interfaces, slide decks, Figma fluency, image/video generation with style consistency.
- **Video** — end-to-end creative/product video (visual design, shot sequencing, music, beat-synced editing) and educational video (concept breakdown → narration via MiMo-V2.5-TTS → animation).
- **Music composition** — described as a "first exploration"; demo cases include a ten-instrument orchestral MIDI piece ("Night Road") and two piano pieces in A minor.
- **Research** — a materials-research case (MOF design for PFAS adsorption, web search + literature review + computational "dry experiments") and a Lean 4 formalization of the full Li–Yorke theorem ("Period Three Implies Chaos," >6,000 lines, verified by Lean's kernel with no unfinished placeholders, no Lean-specific post-training). Full Lean source linked: `https://mimocode-cdn.xiaomimimo.com/mimocode/blog/mimo-v2-6/LiYorke-lean.zip`.

## Availability

MiMo-V2.6-Pro and MiMo-V2.6-Flash are live today in **AI Studio** (`https://aistudio.xiaomimimo.com/#/`), **MiMo Code** (`https://mimo.xiaomi.com/coder`), **MiMo Desktop** (`https://mimo-ai.xiaomimimo.com/desktop/`), the **MiMo API Platform** (`https://mimo.mi.com/`), and on **OpenRouter** (`https://openrouter.ai/xiaomi`).

- **MiMo Desktop** exits early access with its first official release, ships with Pro and Flash built in, and adds the UltraSpeed mode (up to 20× Pro's speed). Early-access program runs one more week.
- **API pricing** (USD per million tokens; cache writes free "for a limited time"):

| Model | Input (cache hit) | Input (cache miss) | Output |
|---|---|---|---|
| MiMo-V2.6-Flash | $0.0028 | $0.14 | $0.28 |
| MiMo-V2.6-Pro | $0.0036 | $0.435 | $0.87 |
| MiMo-V2.6-Pro-UltraSpeed | $0.036 | $4.35 | $8.7 |

A **Token Plan** (`https://platform.xiaomimimo.com/token-plan`) is available for predictable high-volume usage. RMB China pricing lives on a separate pricing page.

## Weights, license, and technical report (from raw HTML — not in the article's extracted text)

The article's rendered body links to a **Hugging Face collection**: `https://huggingface.co/collections/XiaomiMiMo/mimo-v26`, and to a **technical-report PDF hosted on Hugging Face**: `https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf`. Neither was ingested (not fetched, not captured in raw/) — recorded here as pointers only, per instruction not to ingest them. **License terms, exact model sizes (params/active/MoE structure), context window, and modality list are NOT stated anywhere in the captured article text** — the piece describes capabilities and RL training but never states architecture specs (total/active parameter counts, MoE structure, or context length) in prose. This is a **capture gap**, not a confirmed absence — the technical report (uncaptured) likely contains this.

## Appendix: Full benchmark results (transcribed verbatim from `bench.js`)

The article's rendered "Appendix: Full Benchmark Results" table is populated client-side by a companion JavaScript data file at `https://mimo.xiaomi.com/mimo-v2-6/bench.js` (not visible in the static-HTML article fetch). Saved to `research/raw/2026-09-22/mimo-v2-6/bench.js`. Its header comment cites the data source as "V26 Benchmark 主表" (a Feishu/Lark wiki sheet), snapshot 2026-09-22.

Models in the source data, left to right: **MiMo-V2.6-Pro, MiMo-V2.6-Flash, MiMo-V2.5-Pro, DeepSeek V4.1 Flash, Kimi K3, Claude Opus 5, GPT 5.6 Sol, Claude Fable 5, GPT 6 Astra, Claude Fable 5.1**. (GLM 5.3 appears in the source data's `scores` arrays but is flagged `table: false` in the script — i.e. **excluded from the vendor's own published table** — so it is omitted below; its scores exist only in the chart-card view.) Bold in the vendor's rendering = the best score in that row; `-` = no result reported.

**Coding**

| Benchmark | Pro | Flash | V2.5 Pro | DeepSeek V4.1 Flash | Kimi K3 | Opus 5 | GPT 5.6 Sol | Fable 5 | GPT 6 Astra | Fable 5.1 |
|---|---|---|---|---|---|---|---|---|---|---|
| DeepSWE v1.1 | 71.9 | 67.9 | 19.0 | **74.2** | 69.0 | 74.0 | - | 70.0 | 74.0 | - |
| ProgramBench | 26.5 | 26.0 | 12.5 | 20.3 | 24.5 | **37.0** | 25.0 | 33.0 | - | - |
| MiMo Code Bench *(in-house)* | 63.2 | 61.2 | 40.4 | 60.2 | 60.1 | **68.6** | 59.3 | - | 61.4 | - |

**General**

| Benchmark | Pro | Flash | V2.5 Pro | DeepSeek V4.1 Flash | Kimi K3 | Opus 5 | GPT 5.6 Sol | Fable 5 | GPT 6 Astra | Fable 5.1 |
|---|---|---|---|---|---|---|---|---|---|---|
| GDPVal 2.1 (AA, Elo) | 1673 | - | 1107 | 1600 | 1524 | 1708 | 1588 | 1595 | 1542 | **1735** |
| Toolathlon-verified | 76.9 | 73.6 | 49.1 | - | 76.5 | **80.6** | 74.9 | 77.9 | - | 77.8 |
| Automation Bench v1.0.6 | 53.1 | 52.3 | 16.0 | **54.8** | 46.7 | 50.3 | 45.8 | 46.2 | 52.0 | - |
| Agents' Last Exam | 31.6 | 27.6 | 13.2 | 31.8 | 28.3 | 31.6 | 30.8 | 25.7 | **34.2** | - |
| Terminal Bench 4.0 | 34.9 | 28.8 | 1.5 | 26.8 | 12.6 | 49.0 | 39.9 | 42.4 | **59.6** | 55.1 |
| Terminal Bench 2.1 | 89.9 | 87.6 | 65.2 | 90.6 | 88.3 | 89.1 | 88.8 | 84.3 | 89.9 | **91.4** |
| OSWorld-Verified | 82.0 | 80.8 | - | - | 84.8 | 83.4 | 83.0 | **86.0** | - | - |
| JobBench | 62.0 | 61.2 | 25.0 | 45.8 | 54.3 | **65.7** | 45.4 | 57.4 | - | - |

**Visual**

| Benchmark | Pro | Flash | V2.5 Pro | DeepSeek V4.1 Flash | Kimi K3 | Opus 5 | GPT 5.6 Sol | Fable 5 | GPT 6 Astra | Fable 5.1 |
|---|---|---|---|---|---|---|---|---|---|---|
| MiMo Visual Coding *(in-house)* | 72.3 | 71.5 | - | 70.6 | 70.3 | 70.0 | 73.4 | 69.1 | **82.2** | 74.4 |

**Cyber**

| Benchmark | Pro | Flash | V2.5 Pro | DeepSeek V4.1 Flash | Kimi K3 | Opus 5 | GPT 5.6 Sol | Fable 5 | GPT 6 Astra | Fable 5.1 |
|---|---|---|---|---|---|---|---|---|---|---|
| CyberGym | 94.0 | **95.1** | 40.0 | 88.1 | 80.0 | - | - | - | - | - |
| ExploitGym | 17.8 | 6.0 | 0.1 | 15.3 | 8.1 | 22.1 | 30.3 | 28.4 | **42.4** | 30.4 |
| ExploitBench | 47.9 | 25.3 | 16.6 | - | 32.2 | 70.0 | 78.5 | 78.0 | **100.0** | 83.0 |
| SEC Bench Pro | 66.3 | 47.5 | 17.7 | 62.8 | - | - | 79.1 | - | **85.4** | - |
| MiMo Cyber Bench *(in-house)* | **81.7** | 77.2 | 0.0 | 62.7 | 56.3 | - | - | - | - | - |

**Reading the table.** GPT 6 Astra or Claude Fable 5.1 leads most General/Cyber rows; MiMo-V2.6-Pro's headline strength within its own comparison set is concentrated in Coding (ties/wins vs. every non-frontier open model on DeepSWE, and beats every listed model on MiMo Cyber Bench, an in-house benchmark). MiMo-V2.6-Flash beats every other model, including its own Pro sibling, on CyberGym (95.1). No row in this table shows a MiMo model beating every closed frontier model (Opus 5 / Sol / Fable 5 / Fable 5.1 / Astra) simultaneously — the "strongest open-source model" framing in the article body is scoped to the **Artificial Analysis Intelligence Index**, a different, AA-run aggregate metric not itself reproduced in this table.

## Capture gaps

- **No architecture spec captured.** Total/active parameter counts, MoE structure (if any), and context-window length are not stated in the article body. Not in `bench.js` either.
- **HuggingFace collection and technical-report PDF were not ingested** (per instruction) — `https://huggingface.co/collections/XiaomiMiMo/mimo-v26` and `https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf`. License terms are therefore unverified; nothing in the captured article or bench.js states a license.
- **`bench.js` is a JS data file, not prose** — transcribed above as a machine-readable table; its own header comment states the ultimate data source is a Feishu/Lark wiki page, not independently checkable.
- **No independent/third-party corroboration captured** — every number in this page is Xiaomi's own claim (the AA Intelligence Index score is Xiaomi's citation of an AA index, not an AA-authored capture).
- Two images referenced in the article body (Intelligence Index bar chart, Pareto scatter plot) were downloaded to raw/ but not individually described here.
