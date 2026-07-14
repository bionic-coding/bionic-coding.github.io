---
title: "LLM Evaluation & LLM-as-a-Judge"
slug: llm-evaluation
type: concepts
tags: [evals, llm-as-judge, evaluation, bias, council]
sources: [judging-llm-as-a-judge-mt-bench, llm-as-a-judge-evidently-guide]
last_reviewed: 2026-07-14
---

# LLM Evaluation & LLM-as-a-Judge

Curated backing for the evals half of the **Prompting and Evals** lesson. Facts are cited to their `docs/research/sources/` captures.

## Why open-ended output is hard to score

Deterministic metrics (exact match, accuracy) fail on open-ended text — "there are many ways to be 'right' without exactly matching the example answer," and qualities like tone are subjective ([[research/sources/llm-as-a-judge-evidently-guide]]). Humans judge well but don't scale. Overlap metrics like **ROUGE** and embedding **semantic similarity** are cheaper proxies but miss meaning.

## LLM-as-a-judge

Using a strong LLM to grade another model's output. Named and popularized by **Zheng et al., 2023** ([[research/sources/judging-llm-as-a-judge-mt-bench]]), which showed a strong judge (GPT-4) matched human preferences at **>80% agreement — the same rate humans agree with each other**, making it a scalable, explainable stand-in for costly human evaluation.

Two modes ([[research/sources/llm-as-a-judge-evidently-guide]]):
- **Pairwise comparison** — "which of these two is better?" Easier and more reliable than absolute scoring; best for choosing between models/prompts. Usually offline.
- **Direct scoring** — grade one output against a criterion (correctness, relevance, safety). Works offline and for online monitoring.

Practitioner rules of thumb: **binary labels beat fine-grained scales** (a 1–5 scale forces the unanswerable "what separates a 3 from a 4?"); **spell out the criteria** or scores drift; and **the same prompt tricks (chain-of-thought, clear instructions) improve a judge** like any other task.

## The catch: a judge has the failure modes you're testing for

Zheng et al. document three biases in LLM judges ([[research/sources/judging-llm-as-a-judge-mt-bench]]):
- **Position bias** — favoring a response by where it appears (first/last).
- **Verbosity bias** — preferring longer answers even when they aren't better.
- **Self-enhancement bias** — favoring text from the judge's own model/family.

Plus limited reasoning ability. These are the load-bearing citation for the lesson's council note.

## Mitigation: juries / councils, and verify before scaling

Variance and single-judge bias are reduced by **running multiple evaluations and combining them** — max voting or averaging — the "jury" approach (_Replacing Judges with Juries_, Verga et al., 2024, via [[research/sources/llm-as-a-judge-evidently-guide]]). This is the grounding for the site's **council** (three models from different providers voting): drawing judges from different labs lowers the odds of a *shared* blind spot, but does not eliminate it — position/verbosity/self-enhancement biases can still correlate. So the discipline holds: **spot-check any judge or council against your own labels before trusting it at scale** ("if you need extra clarification to decide, the LLM will too").
