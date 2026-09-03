---
title: "GLM-5.3-Flash: Frontier Intelligence, Flash Cost"
slug: glm-5-3-flash
type: source
source_url: https://z.ai/blog/glm-5.3-flash
source_date: 2026-08-26
author: "Z.ai"
captured_at: 2026-09-01
last_source_check: 2026-09-01
raw_path: research/raw/2026-09-01/glm-5-3-flash/
previous_captures: []
static: true
tags: [glm, zhipu, z-ai, open-weights, multimodal, benchmarks, model-release, chinese-chips]
---

Z.ai's launch post for GLM-5.3-Flash, dated 2026-08-26. The page is a client-rendered single-page app: the HTML shell is 604 bytes and the article text lives in the page's JavaScript bundle (`bundle-glm-5.3-flash.js` in the raw capture). The body below was reconstructed from that bundle in source order; headings, paragraphs, and the three table components are verbatim. Figures are described in `## Capture gaps`.

# GLM-5.3-Flash: Frontier Intelligence, Flash Cost

_2026-08-26_

We introduce GLM-5.3-Flash, the first natively multimodal model in the GLM-5 series. With 320B total parameters and just 18B active parameters, it outperforms GLM-5.2 across benchmarks and real-world workloads at one-tenth the price, while approaching Claude Opus 4.8 on coding and agentic benchmarks.

GLM-5.3-Flash starts from a newly trained base model, with its architecture and training recipe redesigned around capability and efficiency. For the first time in the GLM series, we introduce a hybrid architecture combining sparse and linear attention, sharply reducing long-context serving costs while preserving precise long-context capabilities. The model also adopts Manifold-Constrained Hyper-Connections (mHC) to further improve scaling efficiency. Together with our latest 30T-token multimodal pre-training corpus, these changes enable GLM-5.3-Flash to deliver more intelligence with less compute.

Before release, we tested GLM-5.3-Flash anonymously as `ox-alpha` on OpenCode and OpenRouter to gather user feedback. It quickly became the most popular model of the week — with all of this traffic served on Chinese AI chips.

## Competitive Performance at Flash Cost

GLM-5.3-Flash pushes the Pareto frontier of the Artificial Analysis Intelligence Index v4.1.1, scoring 57 at just $0.045 per task (discounted) — a level of intelligence previously only available at roughly 10× the cost. This makes it a highly competitive default choice for a broad range of workloads.

_[Figure: Artificial Analysis Intelligence Index v4.1.1 Pareto chart — not captured, see Capture gaps.]_

Across six coding and agentic benchmarks, GLM-5.3-Flash consistently outperforms GLM-5.2, often by a wide margin — 63.4 vs. 46.2 on DeepSWE v1.1 and 48.8 vs. 26.2 on AutomationBench — while approaching Claude Opus 4.8 overall.

_[Figure: six-benchmark bar chart. The same chart is published on the Hugging Face model card and is transcribed in [[research/sources/glm-5-3-flash-model-card]]; its numbers match the table below.]_

This holds on our in-house coding evaluation as well: on Z.ai Code Bench v1.0, GLM-5.3-Flash clearly outperforms GLM-5.2 at every effort level, and at max effort nearly matches Claude Opus 4.8 (29.0 vs. 29.5).

_[Figure: Z.ai Code Bench v1.0 by effort level — not captured.]_

### Benchmark table (rendered on the page as an interactive table component; column order as published)

**Coding**

| Benchmark | GLM-5.3-Flash | GLM-5.2 | DeepSeek-V4-Vision-Exp | Claude Opus 4.8 | GPT-5.6 Terra | Gemini 3.7 Flash |
|---|---|---|---|---|---|---|
| Terminal Bench 2.1 | 84.3 | 81 | 83.9 | 85 | 87.4 | 85.8 |
| DeepSWE (v1.1) | 63.4 | 46.2 | 59.3 | 58 | 69.6 | 65.3 |
| NL2Repo | 56.3 | 48.9 | 57.7 | 69.7 | — | — |

**Agentic**

| Benchmark | GLM-5.3-Flash | GLM-5.2 | DeepSeek-V4-Vision-Exp | Claude Opus 4.8 | GPT-5.6 Terra | Gemini 3.7 Flash |
|---|---|---|---|---|---|---|
| Toolathlon Verified | 78.4 | 59.9 | 75.9 | 76.2 | 74.9 | — |
| AutomationBench (v1.0.6) | 48.8 | 26.2 | 38.8 | 41 | 37.2 | 52.3 |
| Agents' Last Exam | 26.3 | 20.4 | 27.3 | 27 | 28 | — |
| HLE w/ Tools | 55.3 | 54.7 | 55.1 | 57.9 | — | — |
| GDPval-AA v2 | 1773 | 1504 | 1675 | 1582 | 1571 | 1527 |

**Vision**

| Benchmark | GLM-5.3-Flash | GLM-5.2 | DeepSeek-V4-Vision-Exp | Claude Opus 4.8 | GPT-5.6 Terra | Gemini 3.7 Flash |
|---|---|---|---|---|---|---|
| OfficeQA Pro | 62.4 | — | 57.9 | 48.9 | — | — |
| CharXiv Reasoning (w/ Tools) | 89.4 | — | 80.4 | 89.9 | 88 | 88.7 |
| Chartography (w/ Tools) | 78 | — | 64.3 | 75 | 68 | 65 |
| BabyVision | 53.4 | — | 35.1 | 46.8 | 61.6 | 70.9 |
| MVbench | 77.8 | — | 69.4 | 67.1 | 75 | 82.2 |
| MMVU | 80.5 | — | 72.7 | 67.4 | 75.8 | 82.3 |

## Architecture for Extreme Efficiency

_[Figure: architecture diagram — not captured.]_

Compared with the GLM-4.5 series, GLM-5.3-Flash is specifically designed for ultra-low-cost inference. Despite a similar total parameter count (320B vs. 355B), it nearly halves both the activated parameter count (18B vs. 32B) and the number of layers (45 vs. 92).

To minimize attention costs in long-context scenarios, we use a hybrid architecture combining linear and sparse attention. Linear attention captures local dependencies through state modeling, while sparse attention retrieves relevant global context through a lightweight indexer. To further reduce the latency and memory overhead of the indexer at a 1M-token context length, we introduce IndexPool, which compresses four indexer key vectors into one through weighted pooling.

To illustrate the efficiency of our architecture, we compare the per-token compute and KV cache size of GLM-5.3-Flash against GLM-5.3 and two recent open models: DeepSeek-V4-Flash and Kimi-K3. For a fair comparison among different scales, we calculate the attention compute per head per layer and average KV cache size per layer (BF16). Compared with GLM-5.3, GLM-5.3-Flash uses 3.0× less attention compute and a 4.4× smaller KV cache. GLM-5.3-Flash has the lowest attention compute among all models compared. The KV cache size is still slightly larger than Kimi-K3 and DeepSeek-V4-Flash, leaving further room for improvement.

The overall architecture improvements, combined with optimized pre-training corpus, enable GLM-5.3-Flash to produce more intelligence with less compute.

The table below compares GLM-5.3-Flash-Base with our previous base models and DeepSeek-V4-Flash-Base. GLM-5.3-Flash-Base outperforms GLM-4.5-Base overall and remains competitive with GLM-5-Base across most benchmarks.

|  | GLM-4.5-Base | GLM-5-Base | DeepSeek-V4-Flash-Base | GLM-5.3-Flash-Base |
|---|---|---|---|---|
| Activated Params | 32B | 40B | 13B | 18B |
| Total Params | 355B | 744B | 284B | 320B |
| MMLU | 86.1 | 88.3 | 88.5 | 88.1 |
| BBH | 86.2 | 87.4 | 84.9 | 86.6 |
| HellaSwag | 87.1 | 88.1 | 85.3 | 87.1 |
| LiveCodeBench-Base | 28.1 | 34.4 | 29.9 | 37.6 |
| SimpleQA | 30 | 36 | 31.2 | 33.5 |

(Results for DeepSeek-V4-Flash-Base were evaluated using our internal evaluation framework to control for implementation differences)

## Visual Intelligence in the Coding Loop

Visual coding is not just about processing images. It expands the boundary of what coding can reach. For tasks such as frontend development, game development, and 3D simulation, the final output is not code alone, but an interface, an interaction, or a world experienced by the user. Many failures only surface through rendering, interaction, or playtesting. CUA further extends coding beyond programmable systems into visible and interactive environments. Vision therefore needs to be natively integrated into the model, enabling it to decide when to observe and use visual feedback to guide subsequent actions.

We developed data synthesis pipelines for visual coding, with a focus on visual self-evaluation and test-time improvement. The resulting trajectories require the model to interact with environments, inspect its own outputs, and refine them iteratively. For frontend coding, we also explored reinforcement learning with environment feedback and further strengthened GUI evaluation through agent-based verification grounded in real user flows. This extends validation beyond functional correctness to the rendered and interactive product.

**Code lets the model build and change the world. Vision lets it enter the world people see and use.** The key is to close the loop between generation and visual feedback: the model can render its output, inspect what users would actually see, identify visual issues, and revise the underlying artifact accordingly. This applies not only to interfaces and games, but also to visually structured outputs such as presentations. In the example below, GLM-5.3-Flash detects layout problems in a generated slide and refines the composition through visual self-verification.

_[Figures: "Initial Version with Layout Issues" / "After Visual Self-Verification" — not captured.]_

## Beyond Coding — Your Partner at Work

Coding capabilities provide an important foundation for intelligent knowledge work, while visual intelligence extends these capabilities to a broader range of professional tasks. A substantial portion of professional activities involves interpreting heterogeneous visual and structured information, including documents, spreadsheets, presentations, dashboards, interfaces, and meeting artifacts.

Visual intelligence extends the model's capabilities beyond code-centric environments by enabling it to jointly reason over textual, visual, and structural context. Rather than requiring users to explicitly translate their working environment into textual instructions, the model can directly interpret the artifacts associated with a task and identify relevant information. It can also assess its own outputs against the visual context and intended outcome, enabling more effective self-verification and refinement — including stronger judgments of presentation quality and aesthetics.

These capabilities become particularly evident in the following examples of professional workflows.

_[Interactive examples: "Eight Planets of the Solar System" and "2026 Hospitality Responsibility Report" — embedded PDF viewers, not captured.]_

## Serving at Scale on Chinese AI Chips

Over the past week, we have served GLM-5.3-Flash on a large-scale cluster of Chinese AI chips, supported by a high-bandwidth interconnect and a serving stack optimized for the underlying hardware.

To overcome the relatively limited compute and memory capacity of individual chips, we built a dedicated inference engine for this architecture on top of SGLang. Notably, this effort was accelerated by our GLM-5.3-powered infrastructure agent, which assisted engineers in developing and optimizing kernels, diagnosing performance bottlenecks, and improving the serving stack — creating a feedback loop in which the model helped optimize the system serving the model itself.

These chips are primarily constrained by memory capacity and bandwidth, especially when supporting context lengths of up to one million tokens. This calls for aggressive memory optimization, including compute-for-bandwidth and communication-for-bandwidth techniques tailored to the underlying architecture. Our stack combines intra-node tensor parallelism for linear attention and the LM head, ReplaySSM, W8A8 quantization, hybrid INT8/FP8/BF16 cache quantization, and Layer Split.

At cluster scale, our production-grade Encode–Prefill–Decode (EPD) disaggregated architecture separates multimodal encoding, prompt prefill, and token-by-token decoding into independently scheduled and scalable worker pools, enabling efficient and reliable serving.

Compared with our initial baseline on the same hardware, we achieved a 3× improvement in end-to-end serving performance, reaching hardware efficiency and per-token cost comparable to mainstream NVIDIA GPUs. This demonstrates that Chinese chips can support frontier-model inference efficiently and economically at scale.

## Conclusion

GLM-5.3-Flash shows that frontier intelligence does not have to come at frontier cost. This is not the result of any single trick, but of three layers working together: an architecture that delivers stronger capability from less compute, a richer multimodal pre-training corpus, and infrastructure co-designed with inference hardware. We are now scaling this recipe to larger models — GLM-5.3-Flash pushes the cost-performance frontier, and the lessons from building it are already shaping our next frontier model.

## Getting started with GLM-5.3-Flash

We've rolled out GLM-5.3-Flash to all GLM Coding Plan users. GLM-5.3-Flash gives you **3x** the usable quota of GLM-5.3. Try [Z.ai](https://z.ai).

Unlock GLM-5.3-Flash's multimodal capabilities in [ZCode](https://zcode.z.ai) with **Browser Use** and **Computer Use**: the agent clicks through and visually verifies web pages, and operates your desktop apps.

The model weights of GLM-5.3-Flash are publicly available on [Hugging Face](https://huggingface.co/zai-org/GLM-5.3-Flash). For local deployment, GLM-5.3-Flash currently supports inference frameworks including SGLang, vLLM and TokenSpeed. Support for more frameworks is on the way.

## Footnotes

- **HLE w/ tools (full set)**: We use sampling parameters of `temperature=1.0` and `top_p=0.95` for evaluation, with a maximum generation length of `163,840` tokens. The evaluation is conducted with a maximum context length of `300,000` tokens, using a context management strategy. We use GPT-5.6-luna (medium) as the judge model.
- **NL2Repo**: We evaluated NL2Repo with temperature=1.0, top_p=1.0, and max_new_tokens=64k under 1M context. To prevent hacking, we use rule-based and a LLM-based judgement to prevent malicious behaviors (e.g., unauthorized pip or curl operations).
- **DeepSWE**: We run DeepSWE using the mini-swe-agent harness with `temperature=0.95`, `top_p=1.0`, `timeout=6h` and 400K context.
- **Terminal-Bench 2.1**: We evaluate in Claude Code 2.1.207 with temperature=1.0, top_p=1, max_new_tokens=65536 with 6h timeout.
- **Agent's Last Exam**: We evaluate ALE using the official evaluation protocol with the Claude Code harness (reasoning effort=max, 1M context, and 64K maximum output). Tool Search is disabled, and results are scored by the official ALE evaluators.
- **Toolathlon Verified**: We obtain all results via the official evaluation service and report pass@1 averaged over 3 independent runs.
- **AutomationBench**: We evaluate on AutomationBench **v1.0.6**, incorporating the fix for the `null`-type handling issue introduced in [PR #13](https://github.com/zapier/AutomationBench/pull/13).
- **GDPval-AA v2**: Models are evaluated by Artificial Analysis.
- **BabyVision**: We use temperature=1.0, top_p=0.95, and a maximum context length of 164K tokens. We resize the input images such that their shorter side is at least 1.5K pixels, consistent with other baselines.
- **OfficeQA Pro**: We evaluate the agent on the Treasury Bulletin PDF corpus without providing access to embedded text. We use a temperature of 1.0, top_p of 0.95, and a maximum context length of 512K tokens.
- **CharXiv Reasoning**: We use temperature=1.0, top_p=0.95, and a maximum context length of 256K tokens.
- **Chartography**: We use temperature=1.0, top_p=0.95, and a maximum context length of 256K tokens.
- **MVBench and MMVU**: We use temperature=1.0, top_p=0.95, and a maximum context length of 256K tokens. For models that natively accept video input, such as Gemini 3.7 Flash, we feed the raw video directly for evaluating. For models that do not support video input, we adapt a default 1 fps frame-extraction strategy. If the total number of extracted frames exceeds the API's maximum limit, we perform uniform frame-sampling across the video up to this maximum frame count.

## Capture gaps

- The page is a JavaScript-rendered app. `web-to-markdown` and a rendering fetch both returned an empty body; the text above was reconstructed from string literals in the page's JS bundle (`bundle-glm-5.3-flash.js`, saved in the raw capture). Paragraph order follows the bundle. Inline link targets other than the three "Getting started" links were not recovered.
- Four figures were not captured: the Artificial Analysis Pareto chart, the six-benchmark bar chart (available via the model card, see above), the Z.ai Code Bench effort-level chart, and the architecture diagram. The slide before/after images and the two PDF workflow examples were also not captured.
- The blog gives no API price, license, or context-window figure for GLM-5.3-Flash. "One-tenth the price" and "$0.045 per task (discounted)" are the only cost statements.
