# Fireworks model page — fireworks/qwen3p8-max (serves the Qwen3.8-2.4T-A95B listing)

- **source_url:** https://fireworks.ai/models/fireworks/qwen3p8-max
- **fetched_at:** 2026-08-15
- **note:** Fireworks AI hosting page at the `fireworks/qwen3p8-max` URL. **Capture anomaly, recorded honestly:** the page served at this URL is the **Qwen3.8-2.4T-A95B** listing (open-weights model), not a separate "Qwen3.8 Max" hosted-preview listing. The page's own CMS payload ties `_id: "qwen3p8-max"` to `modelName: "Qwen3.8-2.4T-A95B"`, the canonical/og:url meta tags point at the qwen3p8-max URL, and the displayed model path is `accounts/fireworks/models/qwen3p8-2p4t-a95b`. As of capture there is no distinct qwen3p8-max serverless listing with its own specs on this page — the "max" URL appears to have been repointed at the open-weights release (created 8/12/2026, two days after the Qwen3.8-Max API launch and before the weights release). Vendor serving page; pricing/context are authoritative, everything else is marketing copy.
- **capture_method:** WebFetch (server-rendered markdown; the page is Next.js but prerendered — curl confirms HTTP 200 with `x-matched-path: /models/fireworks/qwen3p8-max`, no redirect). Fireworks site nav/footer chrome stripped; model listing content preserved.

---

# Qwen3.8-2.4T-A95B

(Page title at the qwen3p8-max URL: "Qwen3.8-2.4T-A95B API & Playground | Fireworks AI")

Status: **Ready**

Model path: `accounts/fireworks/models/qwen3p8-2p4t-a95b`

Qwen3.8-2.4T-A95B is Alibaba's most capable Qwen model to date, a 2.4T-parameter sparse MoE with ~95B active parameters. It is built for autonomous, long-horizon work: multi-day coding runs, research-paper reproduction and self-improvement.

## Qwen3.8-2.4T-A95B API Features

### Serverless

Qwen3.8-2.4T-A95B is available via Fireworks' serverless API, where you pay per token. There are several ways to call the Fireworks API, including Fireworks' Python client, the REST API, or OpenAI's Python client.

### On-demand Deployment

On-demand deployments allow you to use Qwen3.8-2.4T-A95B on dedicated GPUs with Fireworks' high-performance serving stack with high reliability and no rate limits.

### Available Serverless

Run queries immediately, pay only for usage

**$2.00 / $0.25 / $6.00** — Per 1M Tokens (input/cached input/output)

### Metadata

| field | value |
|---|---|
| State | Ready |
| Created on | 8/12/2026 |
| Kind | Base model |
| Provider | Qwen |
| Hugging Face | [Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) |

### Specification

| field | value |
|---|---|
| Calibrated | No |
| Mixture-of-Experts | Yes |
| Parameters | 2.41T |

### Supported Functionality

| field | value |
|---|---|
| Fine-tuning | Not supported |
| Serverless | Supported |
| Context Length | 262k tokens |
| Function Calling | Supported |
| Embeddings | Not supported |
| Rerankers | Not supported |
| Support image input | Not supported |

Site-wide banner at capture time: "DeepSeek-V4-Pro-0813 available now on Fireworks".
