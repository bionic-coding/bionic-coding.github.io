---
title: "Claude Opus 4.8: \"a modest but tangible improvement\" (Simon Willison)"
slug: simon-willison-claude-opus-4-8
type: source
source_url: https://simonwillison.net/2026/May/28/claude-opus-4-8/
source_date: 2026-05-28
author: "Simon Willison"
captured_at: 2026-07-12
last_source_check: 2026-07-12
raw_path: research/raw/2026-07-12/simon-willison-claude-opus-4-8/
previous_captures: []
static: true
tags: [anthropic, claude, opus, independent-review, pricing, context-window]
---

# Claude Opus 4.8: "a modest but tangible improvement"

_Simon Willison's Weblog, 28th May 2026. Independent, hands-on commentary on the Opus 4.8 release._

Anthropic shipped Claude Opus 4.8 today. Willison's favourite thing about it is a note in the release announcement:

> Users will find Opus 4.8 to be a modest but tangible improvement on its predecessor. There's still more to be done: we're working on developing and releasing models that provide many of the same capabilities as Opus at a lower cost.

> It's so refreshing to see an AI lab honestly describe a release as a minor incremental improvement over the previous model!

**Honesty as a theme.** He also highlights the announcement's honesty claim (~4× less likely than 4.7 to let flaws in its own code pass unremarked), and quotes the system card:

> Claude Opus 4.8 had the lowest incorrect-rate of the six models on every benchmark—the most direct measure of factual hallucination. It achieved this mainly by abstaining on questions about which it was uncertain rather than by answering more questions correctly.

## Model characteristics (independent confirmation)

> Not much has changed since 4.7.

- **Pricing:** "priced the same as Opus 4.5/4.6/4.7—$5/million input and $25 per million output." Fast mode is 2× that ($10/$50), "a significant reduction from their previous models—fast mode on 4.6/4.7 remains at $30/$150." Fast mode is only available to research-preview organizations ("Contact your account manager to request access").
- **Cutoff:** "Both the reliable knowledge cutoff and the training data cutoff are January 2026, the same as for 4.7."
- **Context / output:** "The context window is still 1,000,000 tokens, and the max output is 128,000 tokens." _(Note: these are Opus 4.8's figures — the gardener memo attributed the same numbers to Fable 5; Fable's specs remain separately unverified.)_
- **Mid-conversation system messages:** Opus 4.8 accepts `role: "system"` messages immediately after a user turn, letting you append updated instructions in a long conversation without restating the full system prompt (preserving prompt-cache hits on earlier turns).
- **Lower prompt cache minimum:** minimum cacheable prompt length is 1,024 tokens on 4.8, down from 4,096 on 4.7.

## The pelican/SVG test

Willison ran his "pelican riding a bicycle" SVG test across all five thinking levels (`low`, `medium`, `high`, `xhigh`, `max`). "The max one was clearly the best, but it did take 25 input, 17,167 output tokens for a total cost of 43 cents." He notes in passing that he "had GPT-5.5 xhigh in Codex update that code to remove any XSS holes... GPT-5.5 is my code security blanket at the moment."

## Follow-on pointers (from the page's "recent articles")

- **"The new GPT-5.6 family: Luna, Terra, Sol" — 9th July 2026** (`https://simonwillison.net/2026/Jul/9/gpt-5-6/`). Independent confirmation of the GPT-5.6 tier names and the July 9 date; a candidate capture to fill the GPT-5.6 gap left by OpenAI's blocked news page.
- **"sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)" — 5th July 2026.** Corroborates that Fable was usable again in early July (consistent with the Jul 1 restoration).

## Capture gaps

- The five pelican/duck illustrations were captured as local PNGs in the raw folder; not reproduced inline here.
