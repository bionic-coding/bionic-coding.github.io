---
title: "Qwen3.8-Max-Preview — fact sheet (compiled)"
slug: qwen3-8-max-preview-fact-sheet
type: source
source_url: null
source_date: null
author: null
captured_at: 2026-07-20
last_source_check: 2026-07-20
raw_path: research/raw/2026-07-20/qwen3-8-max-preview-fact-sheet/
previous_captures: []
static: false
tags: [qwen, qwen3-8-max, alibaba, china, model-release, preview, multimodal, moe]
---

# Qwen3.8-Max-Preview — fact sheet (compiled)

_Provenance: user-compiled fact sheet, pasted 2026-07-20. Not a single-URL capture — a compilation drawn from Alibaba's 2026-07-19 WAIC announcement (X @Alibaba_Qwen + lead researcher Shuai Bai) and secondary coverage. **There is no official model card, blog post, or technical report yet** — the whole point of this source is separating what is **confirmed** by Alibaba's announcement from what is **claimed or inferred**. Vendor and third-party claims are flagged inline; `static: false` — re-check once a real model card / open-weights repo ships._

## 1. Identity

| Field | Value |
|---|---|
| **Official name** | Qwen3.8-Max-Preview |
| **Product / API ID** | `qwen3.8-max-preview` |
| **Informal names** | "Qwen 3.8 Max", "Qwen3.8 Max Preview" |
| **Pre-launch codename** | reportedly "Kaleb" (appeared anonymously on LMArena) — *unverified* |
| **Parent model** | Qwen3.8 (full flagship, not yet released) |
| **Maker** | Alibaba Cloud — Qwen / Tongyi Qianwen team |
| **Announced** | July 19, 2026, at the World AI Conference (WAIC), Shanghai |
| **Announcement channel** | X post from @Alibaba_Qwen + posts from lead researcher Shuai Bai — **no blog post, no model card, no technical report** |
| **Status** | Paid hosted **preview**, described by Alibaba as "continuously evolving" |
| **Not to be confused with** | **Qwen3-8B** — a completely separate 8.2B-parameter open dense model from 2025 |

## 2. Confirmed facts (from Alibaba's own announcement)

- **Total parameters:** 2.4 trillion (vendor-stated). Would make it the second-largest publicly announced model, behind Moonshot's Kimi K3 (2.8T).
- **Modality:** Multimodal — text, images, video, and documents. Alibaba's first trillion-parameter-class *multimodal* model.
- **Reasoning style:** Uses explicit chain-of-thought / extended thinking by default.
- **Availability:** Live now as a paid hosted preview through three first-party surfaces:
  - **Alibaba Token Plan** (credit-based subscription)
  - **Qoder** (agentic coding platform)
  - **QoderWork** (agentic knowledge-work platform)
- **API compatibility:** OpenAI-compatible endpoint (international quickstart documents it for agent tools); Anthropic-compatible endpoint also reported.
- **Preview pricing behavior:** ~10% of standard rate during preview, dropping further overnight (reported ~1/50th rate during 22:00–08:00 UTC+8).
- **Open weights:** Promised — Alibaba says Qwen3.8 will "go open-weight soon."
- **Market reaction:** Alibaba's Hong Kong-listed shares rose as much as ~5.4% the next session; US-listed shares up ~3% pre-market.

### Alibaba's headline claim
Alibaba states the model is "one of the most powerful available today … **second only to Fable 5**." **This is a marketing statement, not a measurement** — no benchmark names, scores, prompts, harnesses, or methodology were published to support it.

## 3. NOT confirmed (unknowns, inferences, and rumors)

As of July 20, 2026, **none** of the following has an official source:

| Missing spec | Status / best available inference |
|---|---|
| **Active parameters per token** | **Unknown.** The single most important missing number. Qwen's Max tier is sparse MoE (cf. Qwen3-235B-A22B = 22B active; Qwen3-30B-A3B = 3B active), so 3.8 is presumed MoE — but the sparsity ratio and active count are undisclosed. Without this, serving cost per token cannot be derived. |
| **Architecture (dense vs MoE)** | Presumed sparse **MoE** by inference from Qwen history; **not officially stated.** A dense 2.4T model would be impractical to serve. |
| **Context window** | **Unconfirmed.** A **1M-token** figure circulates but traces to Qwen Code v0.20.0 integration notes and the *predecessor* Qwen3.7-Max spec — not an official 3.8 spec sheet. |
| **Max output tokens** | Unknown (Qwen3.7-Max was 65,536). |
| **Benchmarks (official)** | **None published.** Every benchmark number circulating "for" Qwen3.8 is almost certainly a **Qwen3.7-Max** number. |
| **Training data scale / token count** | Not disclosed. |
| **Knowledge cutoff** | Not disclosed. |
| **Per-token API price** | Not published; access is bundled into Token Plan/Qoder/QoderWork. |
| **Open-weight date & license** | No date, no license file. It is also unstated whether the *exact* 2.4T checkpoint (vs. a smaller/quantized/distilled sibling) will be the thing released. |
| **Hugging Face / ModelScope repo** | **Does not exist yet.** |
| **OpenRouter listing** | **Absent** (OpenRouter lists ~76 Qwen models; none is 3.8). This absence is the most reliable evidence the weights genuinely have not shipped. |
| **Artificial Analysis / LMArena entry** | None yet. BenchLM has created a profile but shows 0 of 321 tracked benchmarks scored. |

## 4. Independent evaluation (very limited)

No formal third-party benchmarks exist yet. The only independent signals so far are small, single-task tests:

- **Trilogy AI "StackPerf"** blind head-to-head: Qwen3.8-Max-Preview scored **80 vs. Kimi K3's 83** — one run, one task. A later report frames the same class of result as **65/80** in independent early testing. Treat these as isolated data points, not verdicts.
- Assorted reviewer coding tests (e.g., Thomas Wiegold's 4-task run) report results "rivaling Fable 5 and Grok 4.5," with **latency/speed** flagged as the main weakness. Anecdotal.

## 5. Capabilities claimed at launch (per Shuai Bai)
"First trillion-parameter multimodal model," spanning image/video/document understanding, visual coding, content creation, and complex task execution. Alibaba expects it to **beat Qwen3.7-Max** on coding, full-stack development, data analysis, and office workflows. These are expectations stated at launch, not measured results.

## 6. Practical serving reality (why "2.4T" is not the whole story)
A 2.4T model at 4-bit precision needs **~1.2 TB just for weights**. A single Nvidia H200 holds 141 GB, so even 8 cards leave awkward math. For comparison, DeepSeek-V3.2 at 685B is already a serious self-hosting project, and 3.8 is ~3.5× that size. Realistic takeaway: even after weights drop, expect to consume this via inference providers rather than self-host — **unless Alibaba ships a smaller-active-parameter, quantized, or distilled variant.**

## 7. Context: why it launched now
- Dropped **2–3 days after Moonshot AI's Kimi K3** (2.8T open-weight) — widely read as a competitive response. (Notable: Alibaba holds ~36% of Moonshot.) Moonshot set **July 27** for Kimi K3's full-weight release.
- Came days after Chinese regulators approved Qwen to help power **Apple Intelligence in China** (announced July 15, 2026).
- Fits Alibaba's rapid 2026 cadence — a new Max tier roughly every 4–6 weeks.

## 8. Verified predecessors (use these if you need documented specs)

**Qwen3.7-Max** — released May 19, 2026 ("The Agent Frontier"); the latest Qwen flagship *with a published benchmark table*:
- Proprietary, API-only; **1M-token context**; ~1T total / ~24B active (MoE, third-party est.); extended-thinking default.
- SWE-Bench Verified **80.4**; SWE-Bench Pro 60.6; Terminal-Bench 2.0 69.7; GPQA Diamond 92.4; HMMT Feb 2026 97.1; Artificial Analysis Intelligence Index 56.6.
- Pricing $2.50 in / $7.50 out per 1M tokens (list), 90% cached-input discount.

**Qwen3-Max** — released September 23, 2025 (the original "Max"):
- >1T params, pretrained on **36T tokens**, MoE; **262K context**, 66K max output.
- SWE-Bench Verified **69.6**; Tau2-Bench 74.8; preview ranked top-3 on Text Arena.
- ~$1.20 in / $6.00 out per 1M tokens.

**Open-weight option today:** the Qwen3.6 line (e.g., Qwen3.6-27B dense, Qwen3.6-35B-A3B MoE) is Apache 2.0 on Hugging Face; 262K context natively (extensible to ~1M); 27B dense reported at 77.2 SWE-Bench Verified.

## 9. Bottom line & what to watch
**Do not put production workloads on Qwen3.8-Max-Preview on the strength of a teaser.** It's fine to *test*; pin the model ID and re-run evals, since Alibaba may change or replace the preview endpoint.

Five checkable signals will tell you it has matured (each verifiable in under a minute once it exists):
1. An official Qwen blog post / model card **with a benchmark table**.
2. The disclosed **active-parameter count** (and MoE config).
3. A real **Hugging Face/ModelScope repo with a license file**.
4. Published **per-token API pricing**.
5. **Independent evaluation** from Artificial Analysis or LMArena.

Until at least three of these land, treat every "3.8 beats X" claim as marketing.

## Sources and further reading

The URLs behind this compilation (added 2026-07-20). None is an official model card — that still does not exist.

**Primary / official**
- Alibaba Qwen announcement (@Alibaba_Qwen): https://x.com/Alibaba_Qwen/status/2078759124914098291

**News coverage**
- South China Morning Post ("second only to Fable 5"): https://www.scmp.com/tech/article/3361119/alibaba-says-newest-qwen-ai-model-second-only-anthropics-claude-fable-5
- MarkTechPost: https://www.marktechpost.com/2026/07/19/alibaba-previews-qwen3-8-max-a-2-4-trillion-parameter-multimodal-model-days-after-moonshots-kimi-k3-open-weight-launch/
- daily.dev: https://daily.dev/posts/qwen-3-8-max-preview-benchmarks-ollama-raises-88m-53k9hbodt

**Independent testing / benchmarks**
- Trilogy AI "StackPerf" (80 vs 83 head-to-head): https://trilogyai.substack.com/p/qwen-38-max-benchmark-how-it-compares
- Thomas Wiegold (4-task coding review): https://thomas-wiegold.com/blog/qwen-3-8-max-review/
- BenchLM (tracking profile, 0 sourced benchmarks): https://benchlm.ai/models/qwen3-8-max-preview

**Analysis / explainer blogs**
- BuildFastWithAI: https://www.buildfastwithai.com/blogs/qwen3-8-preview-2-4t-params-open-weights-release
- techsy.io: https://techsy.io/en/blog/qwen-3-8
- kie.ai: https://kie.ai/blog/what-is-qwen3-8-max
- eesel AI: https://www.eesel.ai/blog/qwen38-max-review
- Fello AI (Qwen3.7-Max predecessor review): https://felloai.com/qwen-3-7-max-review/

The analysis/explainer blogs vary in reliability and several recycle vendor claims. Cite the primary announcement and the independent tests, not the explainer blogs, for anything you need to stand behind.

## Capture gaps

- **Provenance:** a user compilation, not a fetched capture — `source_url: null` because no single URL is the source. The URLs behind it are now listed under _Sources and further reading_ above; the primary is the @Alibaba_Qwen announcement.
- **No official numbers:** the model has **no model card, benchmark table, or published pricing**. Every hard spec in §3 is unconfirmed; benchmark figures circulating for "3.8" are most likely Qwen3.7-Max numbers.
- `static: false` — a pre-release preview that will change; re-check once an official model card or open-weights repo exists.

> [paraphrased] Compilation note from the source, verbatim: several competitor/model names in mid-2026 coverage (Fable 5, Kimi K3, Grok 4.5, GPT-5.6, DeepSeek V3.2/V4) come from a fast-moving landscape; some figures originate from vendor slides or affiliate blogs and should be treated as unverified. The 2.4T parameter figure and the "second only to Fable 5" ranking are Alibaba's own unverified claims.
