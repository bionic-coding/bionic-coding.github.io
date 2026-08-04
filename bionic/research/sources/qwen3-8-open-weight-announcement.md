---
title: "Alibaba announces the open model release of 'Qwen 3.8,' a large-scale model with 2.4 trillion parameters"
slug: qwen3-8-open-weight-announcement
type: source
source_url: https://gigazine.net/gsc_news/en/20260721-qwen3-8/
source_date: 2026-07-21
author: null
captured_at: 2026-08-01
last_source_check: 2026-08-01
raw_path: research/raw/2026-08-01/qwen3-8-open-weight-announcement/
previous_captures: []
static: true
tags: [qwen, alibaba, open-weights, model-release, vendor-claims]
---

Jul 21, 2026 12:36:00

Alibaba, a major Chinese technology company, has announced that it will soon release its proprietary AI model, '**Qwen3.8**,' as an open model. A preview version, '**Qwen3.8-Max-Preview**,' is also available for use in chat AI services such as Qwen Studio.

> Qwen3.8 is launching and going open-weight soon!🌐
>
> With a massive 2.4T parameters, this model is continuously evolving. We believe it's one of the most powerful model available today, compatible to leading frontier AI models, second only to Fable 5.
>
> You don't have to wait to…
>
> — Qwen (@Alibaba_Qwen) [July 19, 2026](https://x.com/Alibaba_Qwen/status/2078759124914098291)

According to the Qwen team, Qwen 3.8 has 2.4 trillion parameters. They also claim that its performance is 'one of the highest-performing AI models currently available, comparable to Frontier AI models and second only to Claude Fable 5.' However, specific benchmark results have not yet been released.

Alibaba has released 'Qwen3.8-Max-Preview' as a preview version of Qwen3.8, and it is available for use with [the Qwen Studio](https://chat.qwen.ai/) chat AI service and [the Qwen Cloud token plan](https://www.qwencloud.com/pricing/token-plan).

Examples of SVG animations created with Qwen3.8-Max-Preview have also been posted on the internet. [Cypress Frankenfeld](https://cypressf.com/), who created the image, explains that he simply typed 'create an SVG of a pelican riding a bicycle' into Qwen Studio and the SVG image [animation](https://news.ycombinator.com/item?id=48987293) was generated.

Qwen3.8-Max-Preview has reportedly continued to improve in performance since its release. The official release version is expected to be even more powerful.

> During Preview, Qwen3.8 is getting better by the day. Latest version is live now, with broad gains and a big step up on web frontend.
>
> Thank you all — the response to Qwen3.8-Max-Preview blew us away. 🫶🫶
>
> Qwen3.8 is still evolving daily. Come test it, and tell us what breaks.…
>
> — Qwen (@Alibaba_Qwen) [July 20, 2026](https://x.com/Alibaba_Qwen/status/2079172722161299801)

Alibaba released Qwen 3.5 and Qwen 3.6 as open models, but Qwen 3.7 was only released as a closed model. With Qwen 3.8, they have returned to an open model strategy. The open model status of Qwen 3.5 and Qwen 3.6 led to the release of numerous quantized and fine-tuned versions by volunteers. For example, on July 14, 2026, 'Bonsai 27B' appeared, which was a miniaturized version of Qwen 3.6-27B with memory usage reduced to 3.9GB, making it possible to run on an iPhone alone. Similar developments can be expected for Qwen 3.8.

Related: ['Bonsai 27B,' an AI model with 27 billion parameters that can be run locally on an iPhone, has been released. It's a smaller version of Qwen3.6-27B, using only 3.9GB of memory, allowing it to run at a practical speed on a smartphone alone — GIGAZINE](https://gigazine.net/news/20260715-bonsai-27b/)

While American companies like OpenAI and Anthropic dominate the closed model market, Chinese companies have achieved remarkable results in the open model market. The Chinese-made 'Kimi K3,' released on July 17, 2026, is an open model, yet it has outperformed Claude Fable 5 and GPT-5.6 Sol in some benchmark tests.

Related: ['Kimi K3,' a Chinese-made AI model comparable to GPT-5.6 Sol, has emerged, a massive open model with 2.8 trillion parameters — GIGAZINE](https://gigazine.net/news/20260717-kimi-k3/)

Jul 21, 2026 12:36:00 in AI, Posted by log1o_hf

## Capture gaps

* **The headline "second only to Fable 5" is a vendor tweet, not a measurement.** The
  page says so plainly: "specific benchmark results have not yet been released." This
  is a textbook claimed-not-verified figure — the claim is citable, the ranking is not.
* **This page contradicts Willison on Kimi K3.** GIGAZINE says K3 "outperformed Claude
  Fable 5 and GPT-5.6 Sol in some benchmark tests"; Moonshot's own technical report
  ([[research/sources/kimi-k3-technical-report]]) states K3 "still trails… Claude Fable 5
  and GPT-5.6 Sol", and [[research/sources/willison-kimi-k3]] reports the self-reported
  table as losing to both. Prefer the technical report. The release date also differs —
  GIGAZINE says July 17, Willison says announced July 16.
* **No active-parameter count, context window, pricing, license, or open-weight date.**
  The single most important serving number (active params per token) is absent, as it
  was in [[research/sources/qwen3-8-max-preview-fact-sheet]] a week earlier. "Soon" is
  the only ship-date signal.
* **Secondary-source translation.** GIGAZINE is a Japanese outlet; this is its English
  edition reporting on English-language X posts. The quoted tweets are reproduced
  verbatim, including their grammatical errors ("compatible to leading frontier AI
  models").
* 13 images downloaded to the raw capture; screenshots and related-post thumbnails are
  not reproduced inline here. Social buttons and the related-posts grid were stripped.
