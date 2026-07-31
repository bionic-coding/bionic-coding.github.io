---
title: "Introducing Claude Opus 4.8"
slug: claude-opus-4-8
type: source
source_url: https://www.anthropic.com/news/claude-opus-4-8
source_date: 2026-05-28
author: "Anthropic (@AnthropicAI)"
captured_at: 2026-07-12
last_source_check: 2026-07-12
raw_path: research/raw/2026-07-12/claude-opus-4-8/
previous_captures: []
static: true
tags: [anthropic, claude, opus, model-release, pricing]
---

# Introducing Claude Opus 4.8

_May 28, 2026 — Product / Announcements_

We're upgrading Claude Opus to a new version: Claude Opus 4.8. It builds on Opus 4.7 with improvements across benchmarks, and is a more effective collaborator. It's available today for the same price.

Opus 4.8 launches alongside several new features. Users on claude.ai now have control over the amount of effort Claude puts into a task. Claude Code has a new "dynamic workflows" feature that allows it to tackle very large-scale problems. And fast mode for Opus 4.8—where the model can work at 2.5× the speed—is now three times cheaper than it was for previous models.

## Opus 4.8's capabilities

The table below shows how Opus 4.8 compares to its predecessor and to other models on tests of coding, agentic skills, reasoning, and practical knowledge work tasks. More details and a much wider range of capability evaluations are provided in the [Claude Opus 4.8 System Card](https://www.anthropic.com/claude-opus-4-8-system-card).

> [capture gap] The benchmark comparison table is published as an image (`image-88141d41.bin` in the raw capture), not as text — the individual benchmark scores are not machine-readable from this capture. See **Capture gaps** below.

## Collaborating with Opus 4.8

Early testers found Claude Opus 4.8 to be more reliable and sharper in its judgment on agentic tasks. Selected tester quotes (verbatim):

> Claude Opus 4.8 has noticeably better judgment. In Claude Code, it asks the right questions, catches its own mistakes, pushes back when a plan isn't sound, and builds up confidence around complex, multi-service explorations before making big changes. It's a great model to build with.

> On our Super-Agent benchmark, Claude Opus 4.8 is the only model to complete every case end-to-end, beating prior Opus models and GPT-5.5 at parity on cost.

> Claude Opus 4.8 is the strongest computer-use and browser-agent model we've tested, scoring 84% on Online-Mind2Web, which is a meaningful jump over both Opus 4.7 and GPT-5.5.

> In Genie, Databricks' AI agent for data and knowledge work, the new Opus model unlocks a step change in agentic reasoning... Its multimodal strength also lets Genie reason directly over PDFs, diagrams, and other unstructured content at 61% cheaper token cost than Opus 4.7.

_(The page carries 11 customer quotes in total; the full set is in the raw capture.)_

One of the most prominent improvements in Opus 4.8 is its _honesty_. Early testers report that Opus 4.8 is more likely to flag uncertainties about its work and less likely to make unsupported claims. This is borne out in the evaluations, which show that Opus 4.8 is around four times less likely than its predecessor to allow flaws in code it has written to pass unremarked.

As always, Anthropic ran a detailed alignment assessment before release. The Alignment team concluded that Opus 4.8 "reaches new highs on our measures of prosocial traits like supporting user autonomy and acting in the user's best interest." The assessment also showed rates of misaligned behavior substantially lower than Opus 4.7, and similar to "our best-aligned model, Claude Mythos Preview."

## Also launching today

- **Dynamic workflows** (research preview). Lets Claude take on bigger tasks in Claude Code: plan the work, run hundreds of parallel subagents in a single session, then verify outputs before reporting back. Claude Code with Opus 4.8 can carry out codebase-scale migrations across hundreds of thousands of lines of code from kickoff to merge, using the existing test suite as its bar.
- **Effort control in claude.ai and Cowork.** A control alongside the model selector lets users choose how much effort Claude puts into a response. Higher effort = more/deeper thinking; lower effort = faster responses that use rate limits more slowly. Available on all plans.
- **The Messages API now accepts system entries inside the messages array.** Developers can update Claude's instructions mid-task without breaking the prompt cache or routing the update through a user turn (e.g. update permissions, token budgets, or environment context as an agent runs).

## A note on effort

Opus 4.8 defaults to high effort, judged the best overall balance of quality and user experience. On coding tasks, this level spends a similar number of tokens as Opus 4.7's default, but with better performance. Users can choose "extra" ("`xhigh`" in Claude Code) or "max" to spend more tokens for better results; "extra" is recommended for difficult tasks and long-running asynchronous workflows.

## What's next?

Anthropic frames Opus 4.8 as "a modest but tangible improvement on its predecessor," and says it is working on models that provide many of the same capabilities as Opus at lower cost.

> Not only that, but we plan to release a new class of model with even higher intelligence than Opus. As part of Project Glasswing, a small number of organizations are currently using Claude Mythos Preview for cybersecurity work. Models of this capability level require stronger cyber safeguards before they can be generally released... we expect to be able to bring Mythos-class models to all our customers in the coming weeks.

## Availability

Claude Opus 4.8 is available everywhere today. **Pricing for regular usage is unchanged from Opus 4.7: $5 per million input tokens and $25 per million output tokens. Pricing for fast mode is $10 per million input tokens and $50 per million output tokens.** Developers can use `claude-opus-4-8` via the Claude API.

## Footnotes (from the source)

- **Terminal-Bench 2.1:** Anthropic reported scores for all models using the Terminus-2 public harness. GPT-5.5's reported score with the Codex CLI harness is 83.4%.
- **OSWorld-Verified:** Anthropic changed how it runs OSWorld-Verified to more accurately reflect real-world performance, and updated the Opus 4.7 score to 82.3%.
- **Finance Agent v2:** Gemini 3.5 Flash scores 57.9%, a significant improvement over Gemini 3.1 Pro.

## Capture gaps

- The **benchmark comparison table** (coding / agentic / reasoning / knowledge-work scores for Opus 4.8 vs. Opus 4.7 and other models) is published as an image and was captured as `image-88141d41.bin`; the numeric scores are **not** available as text in this capture. The only text benchmark figures on the page are the three footnotes above (which reference **GPT-5.5**, not GPT-5.6). To cite specific head-to-head numbers, consult the [System Card](https://www.anthropic.com/claude-opus-4-8-system-card) directly.
- The page's downloaded raster images had an undetected content-type and were saved with a `.bin` extension in the raw folder; customer-logo SVGs saved normally.
