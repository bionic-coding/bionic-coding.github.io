---
title: "Qwen3.8-Max — QwenCloud model page"
slug: qwen3-8-max-qwencloud-model-page
type: source
source_url: https://www.qwencloud.com/models/qwen3.8-max
source_date: null
author: null
captured_at: 2026-08-03
last_source_check: 2026-08-03
raw_path: research/raw/2026-08-03/qwen3-8-max-qwencloud-model-page/
previous_captures: []
static: false
tags: [qwen, alibaba, model-release, pricing, api, serving-limits]
---

[Model Marketplace](https://www.qwencloud.com/models)

### Qwen3.8-Max

`qwen3.8-max`

[Try AI](https://www.qwencloud.com/try-ai/chat?models=qwen3.8-max) · API Request · [Add to Compare](https://www.qwencloud.com/compare?models=qwen3.8-max)

Reasoning · Visual Understanding · Text Generation

## Overview

Reasoning · Visual Understanding · Text Generation

2.4-trillion-parameter MoE flagship delivering a comprehensive leap in coding and professional work. Autonomously codes and delivers complete projects spanning 10+ days. Handles hundreds of specialized tasks across legal, financial, design, and other professional domains, producing production-grade results end-to-end in a single conversation. Native visual understanding runs through the full cycle of planning, execution, and verification, enabling deep semantic analysis of ultra-long documents and extended video content. In long-horizon tasks, plans autonomously, iterates through closed feedback loops, and continuously evolves.

#### Input

Image, Text, Video

#### Output

Text

## Features

#### Prefix Completion

Enable Partial Mode when calling the Qwen API to make the model continue strictly from your provided prefix text. [View docs](https://docs.qwencloud.com/developer-guides/text-generation/partial-mode)

#### Function Calling

Use function calling to connect large language models with external tools and systems. [View docs](https://docs.qwencloud.com/developer-guides/text-generation/function-calling)

#### Cache

Context Cache stores shared prefixes for long-context requests to reduce repeated computation, improve latency, and lower cost. [View docs](https://docs.qwencloud.com/developer-guides/text-generation/context-cache#implicit-cache)

#### Structured Outputs

Structured Outputs help ensure the model returns a JSON string in the expected format. [View docs](https://docs.qwencloud.com/developer-guides/text-generation/structured-output)

#### Batches

#### Web Search

Enable web search so the model can answer with real-time retrieved data. [View docs](https://docs.qwencloud.com/developer-guides/text-generation/web-search#enable-web-search)

#### Fine-tuning

## Pricing

Models / Built-in Tools

  * Input — **$2** Per 1M tokens
  * Output — **$6** Per 1M tokens
  * Input (Implicit Cache) — **$0.25** Per 1M tokens
  * Explicit Cache Creation — **$2.5** Per 1M tokens
  * Explicit Cache Read — **$0.17** Per 1M tokens

## Rate Limits & Context

  * Max Input — 991K
  * Max Output — 131K
  * Max Input (Thinking) — 983K
  * Max Output (Thinking) — 131K
  * Context — 1M
  * Max Reasoning — 262K
  * TPM (Tokens Per Minute) — 2M
  * RPM (Requests Per Minute) — 15K

## Built-in Tools

[code_interpreter](https://docs.qwencloud.com/developer-guides/text-generation/code-interpreter) — Responses API

[web_extractor](https://docs.qwencloud.com/developer-guides/text-generation/web-scraping) — Responses API

[web_search](https://docs.qwencloud.com/developer-guides/text-generation/web-search) — Responses API

[t2i_search](https://docs.qwencloud.com/developer-guides/text-generation/image-search) — Responses API

[i2i_search](https://docs.qwencloud.com/developer-guides/text-generation/image-search) — Responses API

## API Reference

[Get API Key](https://home.qwencloud.com/api-keys)

DashScope / OpenAI — Python / Java / cURL

Python

```python
import os
import dashscope
dashscope.base_http_api_url = "https://dashscope-intl.aliyuncs.com/api/v1"

messages = [
    {
        "role": "user",
        "content": [
            {"image": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241022/emyrja/dog_and_girl.jpeg"},
            {"text": "What is depicted in the image?"}]
    }]
response = dashscope.MultiModalConversation.call(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    model='qwen3.8-max',
    messages=messages
)
print(response.output.choices[0].message.content[0]["text"])
```

Highlights

## Capture gaps

* **This is a serving fact sheet, not a model card.** It carries pricing, context, and
  rate limits — the numbers the announcement blog omits — but **no benchmark results, no
  active-parameter count, no license, and no weights link**. The 95B active-parameter
  figure comes from the announcement
  ([[research/sources/qwen3-8-max-a-new-bar-for-coding-and-cowork]]), not from here.
* **Every capability sentence in the Overview is vendor marketing copy**, reproduced
  verbatim so it stays citable. "Autonomously codes and delivers complete projects
  spanning 10+ days" is a claim, not a measurement; the blog is where the supporting
  runs are described.
* **`published_date` reported by the extractor was `2026-03-17 17:59:11`** — a page-template
  timestamp, not a publication date for this model's listing. Left as `source_date: null`
  rather than recording a figure the page does not actually assert.
* **Navigation chrome, the model-selector widgets, and the "Copy success!" toast strings
  were stripped.** The tabbed code samples collapse to the Python/DashScope tab that was
  active at capture; the Java and cURL variants were not rendered.
* Pricing is listed without a currency label on the page itself; the figures are USD per
  1M tokens on the international (Singapore) endpoint.
