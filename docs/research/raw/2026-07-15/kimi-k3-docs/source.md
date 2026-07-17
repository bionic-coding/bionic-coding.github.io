# Kimi K3 — platform docs (Introducing Kimi K3)

_Provenance: pasted by the user 2026-07-15 from Kimi's platform docs (platform.kimi.ai). Citable marketing/spec portions preserved; the API code tutorials in the original are omitted here (not citable facts). Canonical URL not captured._

## Introducing Kimi K3

Kimi K3 is Kimi's most capable flagship model to date, with 2.8 trillion parameters. It is built on Kimi Delta Attention (KDA), a hybrid linear attention mechanism, and Attention Residuals, with native visual understanding and a 1M-token context window. It is the world's first open-source model in the 3-trillion-parameter class, designed for frontier intelligence scenarios including long-horizon coding, knowledge work, and reasoning.

For complete benchmarks and case studies, see the technical blog (https://www.kimi.com/blog/kimi-k3). Kimi is currently working closely with inference partners and open-source maintainers to align technical details and ensure the model launches reliably across the ecosystem. The full model weights will be released by July 27, 2026. More details on architecture, training, and evaluation will be published with the Kimi K3 technical report.

### A 3-trillion-scale open-source model

Kimi K3 is the first open-source model to reach 2.8 trillion parameters. This is the latest step in Kimi's continued push of model-scale boundaries: in 9 of the past 12 months (2025/07–2026/07), Kimi models have maintained the frontier in open-source model scale.

Kimi K3 is built on Kimi Delta Attention (KDA) and Attention Residuals (AttnRes). Both architectural updates are designed to help information flow more smoothly through longer sequences and deeper models. We also further increased the sparsity of the Mixture of Experts (MoE): with the Stable LatentMoE framework, the model efficiently activates 16 out of 896 experts. Together with improvements in training methodology and data recipes, these structural advances give Kimi K3 roughly 2.5x the overall scaling efficiency of K2.

### Coding

Kimi K3 has strong long-horizon coding capabilities. With minimal human supervision, it can sustain long-running engineering tasks, understand and work with large codebases, and coordinate terminal tools. Kimi K3 also excels at tasks that combine software engineering and visual reasoning. It can use screenshots and visual feedback to improve workflows in game development, frontend engineering, CAD, and related scenarios.

### Knowledge work

Kimi K3 advances end-to-end knowledge work. Beyond public benchmarks, Kimi K3 (max) also shows consistent gains in internal evaluations reflecting recurring task patterns from real user-agent collaboration workflows.

## API surface (facts)

- Model id `kimi-k3`, served via an OpenAI-compatible API at base URL `https://api.moonshot.ai/v1`.
- Thinking mode always enabled; configured via top-level `reasoning_effort` (currently only `max`; more levels "coming soon"). Do NOT use the K2.x `thinking` parameter.
- Streaming returns separate `reasoning_content` and final-answer `content` deltas.
- Vision input: images and video; `content` must be an array of objects; no public image URLs (use base64 or `ms://<file-id>`).
- Structured output via `json_schema` with `strict: true`. Partial mode, custom tools + `tool_choice`, dynamic tool loading, official tools via "Formula". Web search "being updated," not recommended near-term.
- 1M context with automatic caching (no cache ID/TTL needed).

## Important limits

- `reasoning_effort` currently supports only `max`; K3 always has thinking mode enabled.
- `max_completion_tokens` defaults to 131072 and can be set up to 1048576.
- `temperature=1.0`, `top_p=0.95`, `n=1`, `presence_penalty=0`, `frequency_penalty=0` are fixed; omit them from requests.

## FAQ — billing

Kimi K3 offers a 1M-token context and uses flat pay-as-you-go pricing — there is no tiering by context length. Input (with separate rates for cache hits and misses) and output are billed at uniform per-token prices. (Actual per-token numbers: see Kimi K3 pricing page; not included in the paste.)
