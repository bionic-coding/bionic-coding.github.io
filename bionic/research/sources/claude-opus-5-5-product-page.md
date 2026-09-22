---
title: "Claude Opus (product page)"
slug: claude-opus-5-5-product-page
type: source
source_url: https://www.anthropic.com/claude/opus
source_date: null
author: "Anthropic"
captured_at: 2026-09-22
last_source_check: 2026-09-22
raw_path: research/raw/2026-09-22/claude-opus-5-5-product-page/
previous_captures: []
static: false
tags: [anthropic, claude, opus-5-5, product-page, pricing, availability]
---

Captured via `web-to-markdown` (word_count 2540, thin_content: false). **`static: false`**
per the assignment — this is Anthropic's evergreen Opus product page, not a dated
announcement; its content will change with future model releases and should be
re-checked by `refresh-research-sources` rather than treated as a fixed capture.

> [note] The page's own `<h1>` and rendered title/description metadata still read "**Claude
> Opus 4.8**" (`title: "Claude Opus \\ Anthropic"`, hero heading "# Claude Opus 4.8") even
> though its "Announcements" list and "Availability and pricing" / "Benchmarks" /
> "Safeguards" sections already describe Opus 5.5 as current. This looks like a partially
> rolled page update — the page's own H1/hero graphic is stale relative to its body copy.
> Flagged as `> [contradiction]` between the page's own hero and its own body — not a
> contradiction with the announcement or system card, but an internal inconsistency on
> the product page itself as captured today.

## Announcements list (verbatim, top entry)

> Claude Opus 5.5 — Sep 22, 2026
>
> We're introducing Claude Opus 5.5. It performs at the level of Claude Fable 5.1 on most
> work and costs 40% less to run than Opus 5.

(Prior entries on the same page, for context: Claude Opus 5 — Jul 24, 2026; Claude Opus 4.8
— May 28, 2026; Claude Opus 4.7 — Apr 16, 2026; Claude Opus 4.6 — Feb 5, 2026.)

## Availability and pricing (verbatim)

> Claude Opus 5.5 is our strongest Opus model yet, powering long-running, highly capable
> agents while delivering improvements in coding and professional work.
>
> For business users and consumers who want to collaborate with a powerful model on
> complex tasks, Opus 5.5 is available on Claude for **Pro, Max, Team, and Enterprise**
> users.
>
> For developers interested in building AI solutions that demand strong intelligence, Opus
> 5.5 is available on the **Claude Platform natively, and in Amazon Web Services, Google
> Cloud, and Microsoft Foundry**. Pricing for Opus 5.5 will cost an estimated 40% less to run
> than Opus 5 for typical workloads billed by token. Opus 5.5 costs $4 per million input
> tokens and $20 per million output tokens, 20% below Opus 5. Cache reads, which are a
> large share of the cost of long-running agentic work, also now cost 60% less than Opus 5,
> at $0.20 per million tokens. ... To get started, use `claude-opus-5-5` via the Claude API.
>
> Fast mode for Opus 5.5 is also available now in Claude Code and on the Claude Platform
> with up to 2.5x faster speed. It costs $8 per million input tokens and $40 per million
> output tokens.
>
> For workloads that need to run in the US, US-only inference is available at 1.1x pricing
> for input and output tokens.

**Note on cloud platform naming divergence:** the product page names "Microsoft
**Foundry**" here, while the announcement page ([[research/sources/claude-opus-5-5-announcement]])
names "Microsoft **Azure**" for the same availability claim. Preserved verbatim as written
on each page — likely the same underlying offering (Azure AI Foundry) referred to by two
different names across the two Anthropic pages, but not reconciled here.

Model ID confirmed again: **`claude-opus-5-5`**. Plans: **Pro, Max, Team, Enterprise**
(consumer/business); **Claude Platform, AWS, GCP, Microsoft Foundry/Azure** (developer).
Claude Code: fast mode explicitly available.

## Use cases (verbatim, condensed)

> Claude Opus 5.5 is our most capable Opus model yet for coding, agents, and knowledge
> work. It costs less per token than Opus 5 and uses fewer tokens per task, so work on the
> Claude Platform, in Claude Code, and in the Claude apps costs about 40% less for work
> billed by token than on Opus 5.

Named use-case categories (headers, verbatim): **Advanced coding**, **Agents**,
**Enterprise workflows**, **Financial analysis**, **Vision & computer use**.

## Benchmarks section

Reuses the identical benchmark table and footnotes already captured verbatim in
[[research/sources/claude-opus-5-5-announcement]] — not re-transcribed here to avoid
duplication; see that source page. The chart image itself was downloaded to the raw
capture (`image-f433907f.bin`) but its embedded data was not separately transcribed.

## Trust and safety / Safeguards (verbatim)

> Extensive testing and evaluation ensures the release of Opus 5.5 meets Anthropic's
> standards for safety, security, and reliability. The accompanying system card covers
> safety results in depth.
>
> Opus 5.5 is the first Opus model to launch with a similar class of safeguards to Fable 5.1
> in cybersecurity, biology, and anti-distillation. As our models grow more powerful,
> stricter safeguards are one way we prevent new capabilities from becoming tools for
> misuse.

## FAQ (verbatim)

> **When should I use Claude Opus 5.5?** We offer Claude models across the spectrum of
> speed, price, and performance. We recommend Opus 5.5 as your daily driver for coding
> and knowledge work—particularly production-ready code, complex document creation,
> and computer use.
>
> **How much does it cost to use Claude Opus 5.5?** Pricing depends on how you want to
> use Opus 5.5. To learn more, check out our pricing page.

## Capture gaps

- 24 images were downloaded (per fetch metadata) but not individually described beyond
  the benchmark chart noted above — mostly customer-logo SVGs accompanying the ~17
  testimonial quotes on this page, which substantially overlap the announcement page's
  testimonial set and were not re-transcribed here (see
  [[research/sources/claude-opus-5-5-announcement]] for the fuller testimonial capture).
- No `published_date` was recoverable from page metadata — this is an evergreen product
  page, not a dated post, consistent with `static: false` and `source_date: null` above.
- The page's own stale hero (`# Claude Opus 4.8`) versus its current body copy is noted
  above but not resolved; a future `refresh-research-sources` pass should re-check whether
  the hero has been corrected.
