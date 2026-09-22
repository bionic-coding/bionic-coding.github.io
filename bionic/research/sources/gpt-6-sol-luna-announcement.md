---
title: "Introducing GPT-6 Sol and Luna"
slug: gpt-6-sol-luna-announcement
type: source
source_url: https://openai.com/index/introducing-gpt-6-sol-and-luna/
source_date: 2026-09-22
author: "OpenAI"
captured_at: 2026-09-22
last_source_check: 2026-09-22
raw_path: research/raw/2026-09-22/gpt-6-sol-luna-announcement/
previous_captures: []
static: true
tags: [openai, gpt-6, announcement, pricing, benchmarks, alignment]
---

# Introducing GPT-6 Sol and Luna

> [paraphrased] `openai.com` returns 403 to plain/scripted fetches, so this page was captured by rendering it in headless Chrome and saving the resulting DOM (`source.html`). Body text below is transcribed from that DOM render (`extracted.txt` holds the raw text-extraction pass); markup/layout chrome (nav, cookie banner, "Keep reading" related-post teasers) is dropped, prose content is preserved verbatim. The byline block reads "Author — OpenAI" with no named individual.
>
> No explicit publish date appears anywhere in the captured DOM (no `article:published_time` meta, no visible dateline on the article itself — only on unrelated "Keep reading" teaser links, dated Sep 16, 2026, which are a different post). The article opens "Earlier this month, we introduced GPT‑6 Astra" — Astra's own launch date is recorded elsewhere in this wiki as 2026-09-03 — so this post's actual publish date is somewhere in September 2026 after that, but not pinned down by anything in this capture. Marked `static: true` (fixed announcement) on the assumption its text will not change even though its date could not be confirmed.

More ways to bring frontier intelligence into the work you do every day.

Earlier this month, we introduced GPT‑6 Astra, the most intelligent and aligned model in the world. While the most demanding and important projects still call for Astra's full depth, work happens at different scales, rhythms, and budgets.

That's why we're expanding the GPT‑6 universe with GPT‑6 Sol and GPT‑6 Luna. GPT‑6 Astra introduced a new generation of intelligence — these models help distribute the benefits of that intelligence by advancing the frontier on cost efficiency. We trained GPT‑6 Sol and Luna with similar methods as GPT‑6 Astra, bringing the advances behind Astra's state-of-the-art performance in professional work, factuality, coding, computer use, and alignment to faster, more affordable models.

The GPT‑6 models lead across the cost–intelligence curve, combining exceptional capabilities at every tier with infrastructure that delivers them efficiently at scale. Improvements in caching and inference let us serve these models at lower cost, and we're passing those savings directly on to users and customers by reducing API prices for Sol and Luna by 50% compared with their GPT‑5.6 promotional pricing.

## GPT‑6 API pricing

| Model | Input | Output | Price reduction |
| --- | ---: | ---: | --- |
| GPT‑6 Sol vs. GPT‑5.6 Sol | $4 → $2 | $20 → $10 | 50% cheaper |
| GPT‑6 Luna vs. GPT‑5.6 Luna | $0.20 → $0.10 | $1.20 → $0.50 | 50% cheaper |

Prices are per 1 million tokens.

**GPT‑6 Astra continues to be our best model across the board. Choose it when you want the best results and an uncompromising experience.**

## A step up across the model family

GPT‑6 Sol and Luna bring intelligence upgrades and cost efficiency to the models you already know and use across capabilities most useful for getting complex work done.

### Professional work

GPT‑6 Sol can take on difficult work tasks while giving more room to iterate with higher usage limits and lower cost, offering more intelligence and better results versus similarly priced competitor models.

On **AutomationBench**, a test of business workflows across apps, GPT‑6 Sol at xhigh effort outperforms Claude Opus 5 at max effort at just 9% of Opus 5's cost per task. At high effort, GPT‑6 Luna improves on its predecessor by 5.4 percentage points at 58% lower cost per task.

> AutomationBench 1.0.6: AI agents are tested on end-to-end workflows using 47 tools across sales, marketing, operations, support, finance, and HR. The datapoint for Claude Fable 5.1 understates its actual cost, as it omits the cost of the Opus 5 fallbacks, which occurred on ~40% of tasks.

GPT‑6 Sol also exceeds Claude Fable 5.1 at far lower cost, and even bests low-effort GPT‑6 Astra.

| Model (and effort) | Score | Cost per task |
| --- | ---: | --- |
| GPT‑6 Sol (xhigh) | 33.2% | $0.27 |
| GPT‑6 Astra (low) | 30.3% | 3.9× GPT‑6 Sol |
| Claude Opus 5 (max) | 26.9% | 11.1× GPT‑6 Sol |
| Claude Fable 5.1 w/ Opus 5 Fallback (max) | 31.4% | >8.9× GPT‑6 Sol (fallback cost not reported) |

On **Agents' Last Exam**, which evaluates agents on complex professional workflows, GPT‑6 Sol at max effort scores **56.4%**, above Claude Opus 5's highest score in the evaluation at 60% lower cost per task.

> Agents' Last Exam V1: AI agents are evaluated on long-horizon, economically valuable tasks spanning 55 sub-industries, covering most major fields of professional work performed on a computer.

### Factuality

On OpenAI's internal factuality evaluation (based on de-identified real-world conversations where users flagged mistakes), **GPT‑6 Sol makes about half as many mistakes as its predecessor**, approaching Astra-level reliability at much lower cost. GPT‑6 Luna also improves substantially; at higher effort levels it matches GPT‑5.6 Sol at about a hundredth its cost.

> Evaluated on de-identified ChatGPT conversations where users had flagged a factual error from a prior model. These error-inducing conversations are not representative of typical usage, where factual errors are more rare. Scores are not controlled for length; verbosity sweeps showed almost no dependence on answer length.

### Coding

OpenAI's internal daily coding-agent token usage has "exceeded $600 for the median researcher and $7,000 for researchers at the 90th percentile" (valued at API prices), citing an internal post "Research acceleration: The view inside OpenAI" (not captured).

On **FrontierCode**, which evaluates whether coding agents produce changes ready to merge into real codebases, GPT‑6 Sol improves substantially over GPT‑5.6 Sol, and is able to match Claude Fable 5.1 xhigh at much lower cost.

> FrontierCode 1.1 Main: AI agents write code graded on correctness and "mergeability" (test quality, scope discipline, code style, adherence to codebase standards).

On **DeepSWE v1.1**, GPT‑6 Sol at max effort scores **68.8%**, within 1.1 percentage points of Claude Fable 5's highest score in the evaluation (69.9% at xhigh effort) at approximately 80% lower cost per task. GPT‑6 Luna at max effort scores **66.6%**, comparable to Claude Opus 5 and Fable 5 at medium effort — Luna costs 93% less per task than Opus 5 and 96% less than Fable 5 in these comparisons.

### Computer use

"While GPT‑6 Astra remains the world's best model for computer use, GPT‑6 Sol and Luna offer more cost-efficient performance than their predecessors." On **OSWorld 2.0 offline**, GPT‑6 Sol at xhigh effort achieves a similar score to Claude Opus 5 at medium effort — **60.5% versus 60.3%** — at approximately 80% lower cost per task. GPT‑6 Luna (max) exceeds GPT‑5.6 Sol (medium) at one tenth of its cost.

> OSWorld 2.0: AI agents attempt long-horizon computer-use workflows spanning everyday and professional tasks; partial reward reported on the offline set from the v2026.08.08 release.

### Collaboration style

"We've also brought GPT‑6 Astra's improved communication style to Sol and Luna" — expect "more clarity, less jargon, fewer odd turns of phrase, fewer low-value details, and slightly shorter answers overall without losing substance." A worked before/after prompt example (GPT-5.6 Sol vs GPT-6 Sol replying to the same website-redesign request) is included on the page; OpenAI states a stylistic preference for GPT‑6 Sol's reply ("doesn't jump to conclusions as quickly... uses less vague language... more forthcoming with what it did and didn't check").

### Improving caching for agents and long conversations

"We've improved prompt caching for GPT‑6 to deliver higher cache hit rates by default... discounts of 90% on cached input-token reads." New developer tooling: a Prompt Caching Dashboard, a caching diagnostics tool, reasoning-effort/tool-toggle changes that now preserve cache, and explicit cache-breakpoint control over prefixes. **Third-party claim, attributed to GitHub**: "GitHub reports that, over the past several months, these improvements have reduced the share of prompt tokens requiring fresh processing by more than 50% across billions of requests to OpenAI models, helping Copilot respond faster."

### Continuing to improve alignment

"GPT‑6 Sol and Luna build on the alignment work introduced with Astra, our most aligned model to date. In our alignment evaluations, both Sol and Luna show improvements over their GPT‑5.6 counterparts, including lower rates of misleading claims about their coding work." **"The evaluations below deliberately test challenging situations and do not measure failure rates in typical use. See the system card for the full results."** — this "system card" link resolves to `https://deploymentsafety.openai.com/gpt-6-astra`, i.e. **GPT-6 Astra's own deployment-safety/system-card page**, not a Sol/Luna-specific system card. No separate Sol/Luna system card is linked anywhere in this capture.

### Availability

"GPT‑6 Sol and GPT‑6 Luna are available in ChatGPT Work and Codex starting today for all Plus, Pro, Business, Enterprise, and Edu users. Free and Go users can access GPT‑6 Luna in the desktop app. **These models are not yet available in Chat.** In the OpenAI API, they are available as `gpt-6-sol` and `gpt-6-luna`." Rollout in ChatGPT is staged "gradually throughout the day."

### Methodology note (vendor's own caveat)

"Evaluations of GPT were performed in our research environment or via our API, which may provide slightly different output from production ChatGPT due to differences in the system prompts, tools available, etc. Evaluations of competitor models were taken from publicly available reports. Scores for Claude Fable 5 were reported when scores for Claude Fable 5.1 were unavailable."

## Capture gaps

- No independent/third-party benchmark verification — every comparison figure in this post is OpenAI's own, run against "publicly available reports" for competitor models (their caveat, quoted above).
- No confirmed publish date (see the top note).
- The "Research acceleration: The view inside OpenAI" post cited for the coding-usage figures was not captured.
- The article does not use the word "Terra" anywhere, and makes no explicit statement resolving whether GPT-6 Terra exists or is planned — see the synthesis page for how this bears on the earlier "no Sol/Terra/Luna split" record.
