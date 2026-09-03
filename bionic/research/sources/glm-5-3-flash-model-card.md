---
title: "zai-org/GLM-5.3-Flash — Hugging Face model card"
slug: glm-5-3-flash-model-card
type: source
source_url: https://huggingface.co/zai-org/GLM-5.3-Flash
source_date: null
author: "Z.ai (zai-org)"
captured_at: 2026-09-01
last_source_check: 2026-09-01
raw_path: research/raw/2026-09-01/glm-5-3-flash-model-card/
previous_captures: []
static: false
tags: [glm, zhipu, z-ai, open-weights, model-card, hugging-face, benchmarks, local-models]
---

Hugging Face model card for GLM-5.3-Flash, the open-weights release announced in [[research/sources/glm-5-3-flash]]. Captured 2026-09-01; the card carries no publication date of its own (the linked collection was "updated 5 days ago" at capture time). Hub chrome (download widgets, sidebar) is paraphrased at the end.

# GLM-5.3-Flash

Join our WeChat or Discord community.
Check out the GLM-5.3-Flash [blog](https://z.ai/blog/glm-5.3-flash) and GLM-5 [Technical report](https://arxiv.org/abs/2602.15763).
Use GLM-5.3-Flash API services on [Z.ai API Platform](https://docs.z.ai/guides/llm/glm-5.3-flash).

## Introduction

We introduce GLM-5.3-Flash, the first natively multimodal model in the GLM-5 series. With 320B total parameters and just 18B active parameters, it outperforms GLM-5.2 across benchmarks and real-world workloads at one-tenth the price, while approaching Claude Opus 4.8 on coding and agentic benchmarks.

GLM-5.3-Flash starts from a newly trained base model, with its architecture and training recipe redesigned around capability and efficiency. For the first time in the GLM series, we introduce a hybrid architecture combining sparse and linear attention, sharply reducing long-context serving costs while preserving precise long-context capabilities. The model also adopts Manifold-Constrained Hyper-Connections (mHC) to further improve scaling efficiency. Together with our latest 30T-token multimodal pre-training corpus, these changes enable GLM-5.3-Flash to deliver more intelligence with less compute.

![[../raw/2026-09-01/glm-5-3-flash-model-card/bench_53-c52678c7.png]]

Transcription of the figure ("LLM Performance Evaluation — 6 benchmarks"), read from the image:

| Benchmark | GLM-5.3-Flash | GLM-5.2 | DeepSeek-V4-Vision-Exp | Claude Opus 4.8 | GPT-5.6 Terra | Gemini 3.7 Flash |
|---|---|---|---|---|---|---|
| Terminal Bench 2.1 | 84.3 | 81.0 | 83.9 | 85.0 | 87.4 | 85.8 |
| DeepSWE v1.1 | 63.4 | 46.2 | 59.3 | 58.0 | 69.6 | 65.3 |
| Agents' Last Exam | 26.3 | 20.4 | 27.3 | 27.0 | 28.0 | — |
| AutomationBench v1.0.6 | 48.8 | 26.2 | 38.8 | 41.0 | 37.2 | 52.3 |
| HLE w/ Tools | 55.3 | 54.7 | 55.1 | 57.9 | — | — |
| GDPval-AA v2 | 1773 | 1504 | 1675 | 1582 | 1571 | 1527 |

## Serve GLM-5.3-Flash Locally

GLM-5.3-Flash supports deployment with the following frameworks. Feel free to try them out:

- [SGLang](https://github.com/sgl-project/sglang) — see [cookbook](https://cookbook.sglang.io/autoregressive/GLM/GLM-5.3-Flash)
- [vLLM](https://github.com/vllm-project/vllm) — see [recipes](https://recipes.vllm.ai/zai-org/GLM-5.3-Flash)
- [TokenSpeed](https://github.com/lightseekorg/tokenspeed) — see [here](https://lightseek.org/tokenspeed/recipes/models#glm-5-3-flash)
- [Transformers](https://github.com/huggingface/transformers) — see [transformers docs](https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/glm5_next.md)
- [KTransformers](https://github.com/kvcache-ai/ktransformers) — see [tutorial](https://github.com/kvcache-ai/ktransformers/blob/main/doc/en/kt-kernel/GLM-5.3-Flash-Tutorial.md)
- [Unsloth](https://github.com/unslothai/unsloth) — see [guide](https://unsloth.ai/docs/models/glm-5.3)

### Note

- GLM-5.3-Flash supports controlling the thinking budget through the `reasoning_effort` parameter, which accepts three levels: `low`, `high`, and `max`. It defaults to `max` if not passed (or if set to any other value). To use `low` or `high`, pass them explicitly. For benchmark and leaderboard reproduction, keep the default `max`.
- In the chat template for GLM-5.3-Flash, `clear_thinking` defaults to `false` if not passed. For chat scenarios, explicitly pass `clear_thinking=true`.

## Footnotes

- **HLE w/ tools (full set)**: We use sampling parameters of `temperature=1.0` and `top_p=0.95` for evaluation, with a maximum generation length of `163,840` tokens. The evaluation is conducted with a maximum context length of `300,000` tokens, using a context management strategy. We use GPT-5.6-luna (medium) as the judge model.
- **NL2Repo**: We evaluated NL2Repo with temperature=1.0, top_p=1.0, and max_new_tokens=64k under 1M context. To prevent hacking, we use rule-based and a LLM-based judgement to prevent malicious behaviors (e.g., unauthorized pip or curl operations).
- **DeepSWE**: We run DeepSWE using the mini-swe-agent harness with `temperature=0.95`, `top_p=1.0`, `timeout=6h` and 400K context.
- **Terminal-Bench 2.1**: We evaluate in Claude Code 2.1.207 with temperature=1.0, top_p=1, max_new_tokens=65536 with 6h timeout.
- **Agent's Last Exam**: _(empty on the card)_
- **Toolathlon Verified**: We obtain all results via the official evaluation service and report pass@1 averaged over 3 independent runs.
- **AutomationBench**: We evaluate on AutomationBench **v1.0.6**, incorporating the fix for the `null`-type handling issue introduced in [PR #13](https://github.com/zapier/AutomationBench/pull/13).
- **GDPval-AA v2**: Models are evaluated by Artificial Analysis.
- **BabyVision**: We use temperature=1.0, top_p=0.95, and a maximum context length of 164K tokens. We resize the input images such that their shorter side is at least 1.5K pixels, consistent with other baselines.

## Citation

If you find GLM-5.3-Flash useful in your research, please cite our technical report: GLM-5 Team, "GLM-5: from Vibe Coding to Agentic Engineering," arXiv:2602.15763 (2026). Full BibTeX with the author list is in the raw capture's `extracted.md`.

## Hub metadata

> [paraphrased] Downloads last month: 441,348. Safetensors, model size 321B params, tensor types BF16 · F8_E4M3 · F32, chat template present. Model tree: 1 adapter, 11 finetunes, 1 merge, 80 quantizations (llama.cpp, LM Studio, Jan, Ollama). 5 Spaces use the model. Part of the `zai-org/glm-53` collection (4 items). Paper: arXiv 2602.15763, published Feb 17. Hub evaluation-results widget: llamaindex/ExtractBench mean 80.75 (short 96.3, medium 51.56, one-shot structured-output pipeline, community-submitted); harborframework/terminal-bench-2.1 84.3; datacurve/deep-swe 63.4; two more benchmarks collapsed.

## Repository files fetched alongside the card (2026-09-01)

Saved in the raw capture: `LICENSE`, `config.json`, the Hub API record (`hf-api.json`), and, for comparison, the sibling repo's license as `GLM-5.3-LICENSE.txt` (a custom "GLM-5.3 License", not MIT).

- **License: MIT** — `LICENSE` reads "MIT License / Copyright (c) 2026 Z.AI Co., Ltd"; the Hub tag is `license:mit`.
- **Repository created 2026-08-25, last modified 2026-08-31** (Hub API). The blog post is dated 2026-08-26.
- **`config.json`** (`Glm5NextForConditionalGeneration`, `model_type: glm5_next`): `max_position_embeddings` **1,048,576** (1M context); **45 layers**, of which **34 linear-attention and 11 DeepSeek-style sparse-attention** (`layer_types`); 42 sparse-MoE and 3 dense MLP layers; **8 experts per token**; hidden size 4096; 64 attention heads; vocab 154,880; a vision tower (`vision_config`, hidden 1024). Total and active parameter counts are not in the config; the card states 320B / 18B.

## Capture gaps

- The benchmark figure is an image; the transcription above was read visually and matches the blog's table data exactly.
- Footnotes for OfficeQA Pro, CharXiv, Chartography, MVBench/MMVU appear only on the blog, not the card.
- No API price on the card (the Z.ai API Platform docs page linked from the card was not captured).
