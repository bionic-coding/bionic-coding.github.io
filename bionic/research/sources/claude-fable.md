---
title: "Claude Fable 5 (product page)"
slug: claude-fable
type: source
source_url: https://www.anthropic.com/claude/fable
source_date: 2026-07-01
author: "Anthropic (@AnthropicAI)"
captured_at: 2026-07-12
last_source_check: 2026-07-12
raw_path: research/raw/2026-07-12/claude-fable/
previous_captures: []
static: false
tags: [anthropic, claude, fable, mythos, model-release, pricing, export-controls]
---

# Claude Fable 5

_Anthropic product page. Captured 2026-07-12. Tagline: "Next generation of intelligence for the hardest knowledge work and coding problems."_

## Announcements (timeline on the page, newest first)

- **Jul 1, 2026 — "Claude Fable 5 is rolling out."** "Access to Claude Fable 5 has been restored. It brings 5th-generation intelligence to your most ambitious coding and professional work." → links to `/news/redeploying-fable-5`.
- **Jun 12, 2026 — "Claude Fable 5 access unavailable."** "We apologize for this disruption to our customers and are working to restore access as soon as possible." → links to `/news/fable-mythos-access`.
- **Jun 9, 2026 — "Claude Fable 5."** "Claude Fable 5 introduces our 5th model generation for your most ambitious work. Tackle days-long, complex, and asynchronous tasks previous models couldn't sustain." → links to `/news/claude-fable-5-mythos-5`.

> [note] The page states the *dates* of the outage (unavailable Jun 12 → restored Jul 1) and ties the redeployment to enhanced safeguards, but it does **not** state a *cause* for the Jun 12 suspension. See **Capture gaps**.

## Availability and pricing

Claude Fable 5 is available to Pro, Max, Team, and Enterprise users. For developers it is available on the Claude Platform natively, through marketplaces, and on Amazon Web Services, Google Cloud, and Microsoft Foundry.

> Claude Fable 5 is priced at **$10 per million input tokens and $50 per million output tokens**, with the existing **90% input token discount for prompt caching**. ... To get started, use `claude-fable-5` via the Claude API.

> For workloads that need to run in the US, **US-only inference is available at 1.1x pricing** for input and output tokens.

## Use cases

Claude Fable 5 is described as "a Mythos-level model built for your most ambitious, long-running projects... thorough, proactive, and tests its own work."

- **Agents:** in a harness like Claude Code or Claude Managed Agents, "it can work for days at a time: planning across stages, delegating to sub-agents, and checking its own work."
- **Coding:** "our most capable model for ambitious coding projects, including large migrations, complex implementations, and multi-day autonomous sessions." Writes its own tests; uses vision to check outputs against goals.
- **Enterprise workflows:** "complex, multi-stage knowledge work with minimal oversight... Teams can hand off large projects and review completed work rather than supervising every step."
- **Vision:** understands diagrams, charts, and tables nested in files and PDFs; also uses vision to evaluate its own coding work.

## Safeguards

> Claude Fable 5 includes robust safeguards for cybersecurity and biology. Many queries in these domains are automatically routed to Opus 4.8 if flagged by these safeguards. You won't be charged Fable prices for rerouted requests.

The page adds: "We recently further enhanced our safeguards" (linking to the redeployment post), and points to the [Fable 5 / Mythos 5 system card](https://anthropic.com/claude-fable-5-mythos-5-system-card).

## Data retention

"Using Fable requires 30-day data retention for safety monitoring."

## Benchmarks

> Claude Fable 5 is state-of-the-art at coding, knowledge work, vision, and computer use.

> [capture gap] The benchmark comparison ("Claude Fable and Mythos compared to other leading models") is an image (`image-8a62650d.bin`); numeric scores are not captured as text.

## Selected customer quotes (verbatim; page carries 26)

> Claude Fable 5 is a real step forward for the developers GitHub serves... it took on complex, long-horizon coding tasks with a level of autonomy and reliability that exceeded previous benchmarks. — GitHub

> Claude Fable 5's reasoning is a clear step beyond Opus 4.8. It works at senior research scientist grade — picking directions, allocating resources, killing its incorrect beliefs, and producing novel first-principles outputs.

> Claude Fable 5 is the strongest model we've tested on frontier physics research while using a third of the reasoning tokens. In 36 hours it got nearly to where GPT-5.5 landed after four days.

> Claude Fable 5 compresses months of engineering into days. In our 50-million-line Ruby codebase, it did in a day what would've taken us more than two months by hand.

> Claude Fable 5 is the first to break 90% on our core analytics benchmark of complex, long-running analytical tasks — a 10-point jump over Opus.

## Frequently asked questions (verbatim excerpts)

**When should I use Claude Fable 5?** "Claude Fable 5 is our most capable generally available model. It's best for ambitious, long-running, asynchronous work."

**Why did you create new safeguards for Claude Fable 5?** "Making a model as capable as Fable 5 generally available comes with risks. The model's capabilities in specific areas like cybersecurity, biology, and chemistry are advanced enough that they could be misused to create wide-reaching cyberattacks or build dangerous bioweapons. For that reason, Fable 5 comes with safeguards... Many queries on topics including biology and cybersecurity will instead receive a response from our next-most-capable generally available model, Claude Opus 4.8."

**When can I get access to Mythos 5 for cybersecurity and biology research?** "Our goal is to safely open up access to vetted partners to use Mythos 5 for cybersecurity and biology research."

**How does the fallback work?** "For most Claude applications, queries flagged by our cybersecurity and biology safeguards automatically route to Opus 4.8. API customers must configure their settings with our new Fallback API."

## Capture gaps

- **Cause of the Jun 12 suspension is not stated on this page.** It records the outage dates (unavailable Jun 12 → restored Jul 1) and links the redeployment to "enhanced safeguards," but gives no reason for the original suspension. The night-gardener memo attributed it to "a US export-control directive" — that cause is **not** corroborated here and reads as inconsistent with the safeguards framing. The linked posts `/news/fable-mythos-access` (Jun 12) and `/news/redeploying-fable-5` (Jul 1) are the primary sources to capture before writing the "why."
- **No context-window or max-output figures** ("1M-token context / 128K output" per the memo) appear on this page — unverified.
- Benchmark table captured as an image (`image-8a62650d.bin`), not text.
