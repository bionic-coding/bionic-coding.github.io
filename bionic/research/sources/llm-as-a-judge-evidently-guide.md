---
title: "LLM-as-a-judge: a complete guide to using LLMs for evaluations"
slug: llm-as-a-judge-evidently-guide
type: source
source_url: https://www.evidentlyai.com/llm-guide/llm-as-a-judge
source_date: 2026-05-19
author: "Evidently AI"
captured_at: 2026-07-14
last_source_check: 2026-07-14
raw_path: research/raw/2026-07-14/llm-as-a-judge-evidently-guide/
previous_captures: []
static: false
tags: [llm-as-judge, evals, evaluation, pairwise, rubric, practical-guide]
---

# LLM-as-a-judge: a complete guide to using LLMs for evaluations

_Evidently AI — LLM guide. Last updated 2026-05-19. A practical, vendor-neutral walkthrough of using LLMs to evaluate LLM output._

## What it covers (source's own summary)

> LLM-as-a-judge is a common technique to evaluate LLM-powered products… a practical alternative to costly human evaluation when assessing open-ended text outputs.

Metrics like accuracy don't work well on open-ended text — "there are many ways to be 'right' without exactly matching the example answer," and style/tone are subjective. Humans handle the nuance but don't scale; an LLM judge is the scalable stand-in. ("Interestingly, the LLM is both the source of the problem and the solution.")

## Key points

- **Two modes of judging:**
  - **Pairwise comparison** — give the judge two responses and ask which is better. Best for picking between models/prompts/configs during development; typically run offline. (The guide traces the "judge" nickname to [[research/sources/judging-llm-as-a-judge-mt-bench]].)
  - **Direct scoring** — evaluate one output against a property (correctness, relevance, politeness, bias). Works offline **and** online for continuous monitoring.
- **Binary beats fine scales.** "Binary evaluations… tend to be more reliable and consistent for both LLMs and human evaluators" than a 1–5 scale — with a 5-point scale, "what's the difference between a 3 and a 4?" is hard for humans and models alike. If you can't explain the distinction, simplify the scale.
- **Define your criteria explicitly** — the rubric/labels must be spelled out; ambiguous criteria produce inconsistent scores.
- **The same prompting tricks apply to the judge** — chain-of-thought and clear instructions improve a judge just like any other task.
- **Reduce variance with multiple evaluations + voting** — "combine the results using methods like max voting or averaging," citing _"Replacing Judges with Juries"_ (Verga et al., 2024). This is the practitioner grounding for a **jury/council** of judges.
- **Sanity-check the judge against yourself:** "Try labeling some responses yourself! If you need extra clarification to make a decision, the LLM will likely do so too."
- Covers pros/cons and alternatives (reference-based metrics like ROUGE, embedding semantic similarity).

## Capture gaps

- This is a ~7,700-word guide; the page above captures its structure and the load-bearing claims. The full immutable capture (`source.html` + rendition + images) is in `research/raw/2026-07-14/llm-as-a-judge-evidently-guide/`. `static: false` — it's a living guide, so `refresh-research-sources` should re-check it.
