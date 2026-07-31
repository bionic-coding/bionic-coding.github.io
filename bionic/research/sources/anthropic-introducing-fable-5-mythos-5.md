---
title: "Introducing Claude Fable 5 and Claude Mythos 5"
slug: anthropic-introducing-fable-5-mythos-5
type: source
source_url: https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
source_date: 2026-06-09
author: "Anthropic"
captured_at: 2026-07-15
last_source_check: 2026-07-15
raw_path: research/raw/2026-07-15/anthropic-introducing-fable-5-mythos-5/
previous_captures: []
static: false
tags: [anthropic, claude, fable, mythos, specs, context-window, adaptive-thinking]
---

# Introducing Claude Fable 5 and Claude Mythos 5

_Anthropic Claude Platform Docs — the model page. The primary source for Fable 5's specs (closes the last open item in the frontier-models reference)._

## Specs (verbatim / near-verbatim)

Fable 5 and Mythos 5 "share the same specs and pricing":

- **Context window and output:** "a **1M token context window** by default, and **up to 128k output tokens** per request." ✅ confirms the memo's figures.
- **Pricing:** "$10 per million input tokens and $50 per million output tokens." (Matches [[research/sources/claude-fable]].)
- **Adaptive thinking is always on** — steered by the **effort** parameter; thinking blocks are passed back unchanged in multi-turn conversations on the same model. ✅ confirms "always-on adaptive thinking."
- Model ids: `claude-fable-5`; `claude-mythos-5` (Mythos = same capabilities **without the safety classifiers**, limited to Project Glasswing; successor to Claude Mythos Preview).
- Capabilities: vision, tool use, structured outputs, prompt caching, Batch API, context editing (beta).

## Availability & policy

- **Both became available June 9, 2026.** Fable 5 is GA on the Claude API, AWS / Amazon Bedrock, Google Cloud, and Microsoft Foundry. Mythos 5 is limited-release (Glasswing; contact account team).
- **30-day data retention, no zero-data-retention option** — both are designated "Covered Models."
- Fable 5 "responds to the same prompting techniques as other Claude models, with a few differences in how to structure long-context prompts and reasoning instructions" (Anthropic ships a dedicated *Prompting Claude Fable 5* guide).

## Note worth stealing (for a cost article)

Not on this page but confirmed alongside it: Fable uses the **Opus 4.7 tokenizer**, which counts ~30% more tokens than older Claude models for the same text — so a per-token price isn't directly comparable to older models.

## Capture gaps

- Captures the model page's spec/availability text; full immutable capture in `research/raw/2026-07-15/anthropic-introducing-fable-5-mythos-5/`. `static: false` — platform docs update, so `refresh-research-sources` should re-check.
