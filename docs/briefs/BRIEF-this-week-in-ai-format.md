---
title: "This Week in AI: standardized issue format"
slug: this-week-in-ai-format
type: brief
status: published            # draft | published
created_at: 2026-07-17
updated_at: 2026-07-17        # bumped on every edit
authors: ["Mark Madsen"]
tags: [content, editorial, model-news, weekly, template]
related_adrs: []             # ADR ids that reference this brief (back-populated by audit-docs)
---

# This Week in AI: standardized issue format

"This Week in AI" is the recurring weekly model-news roundup — plain-language coverage of the week's AI developments for people who want to keep up but don't have time to follow it. This brief documents the standard shape of an issue so every one reads consistently, and so drafting a new one is copy-fill, not reinvention. It's the recurring-post companion to the editorial guidance in [[briefs/BRIEF-teaching-regular-people-ai-content-plan]].

The reusable skeleton lives at **`_templates/this-week-in-ai.md`** (a root `_templates/` directory excluded from the Jekyll build). This brief is the "how"; the template is the "what to copy."

## The one thing that makes this format different
Unlike a Learn lesson, an issue is a **dated snapshot**. Perishable links are a *feature* here, not a bug — the links are the receipts, and they're allowed to age. The "pull the links before they go stale" rule we apply to evergreen lessons is inverted for these posts.

## How to write an issue
1. Copy `_templates/this-week-in-ai.md` to `_posts/YYYY-MM-DD-this-week-in-ai.md`.
2. Fill the frontmatter: `title` prefix + date, and a `description` that names each story in plain language (this is the scannable teaser).
3. Write the lede, 3-5 story sections (biggest first, related stories grouped), and the standing closer.
4. For each claim, mark what's *claimed* (the vendor's words) vs. what's *verified*, and correct the popular misread when there is one.
5. Publish. It renders at `/YYYY/MM/DD/this-week-in-ai.html`.

Same discipline as everything else on the site: the template is scaffold; the sentences are yours.

## Anatomy — three layers
**Post:** frontmatter → narrative lede → 3-5 story sections → standing closer.

- **Lede** — 2-3 sentences, first person, warm. Sums up the week and sets the tone. This is where the personality lives.
- **Standing closer** — a permanent `## What I'm actually using` beat: opinion, not news. What you're reaching for this week and why. It's the column's signature and the reader payoff.

**Story:**
- `## Headline` — plain *or* playful (both are on-brand).
- **One line: what happened**, plain language, right under the heading.
- **Substance** — a paragraph or two; separate claimed from verified.
- **Evidence module** *(optional)* — a bolded label + bullets for receipt-heavy stories (`**What the evidence shows:**`, `**The response (dates):**`). Skip it for simple items.
- **One-line take** *(optional)* — italic, only when you have one.
- **`More info:`** — annotated link list (see below).

**Link:** every link is annotated and dated. The anchor/primary source is **bolded and listed first**; every other link gets `(Mon DD)` plus a short "what it is / why it's here" gloss.

## The signature moves (the actual voice)
These are the point of the column, not decoration:
1. **Honest asterisks** — separate vendor claims from verified facts ("the headline numbers are the vendor's own; no independent benchmarks yet").
2. **Correct the popular misread** — e.g. "it was the CLI, not the model."
3. **A personal close** — end on opinion, turning the news back toward *you*.

## Settled conventions
- **No separate TL;DR block.** The frontmatter `description` plus the narrative lede cover skimming; a bullet list would flatten the voice.
- **"My take" is optional per story.** Forced, it becomes filler; use it only when there's a real opinion.
- **`What I'm actually using` is a permanent fixture** — every issue closes on it.
- **The evidence module is an optional per-story module** — pull it in for receipt-heavy stories, skip it otherwise.
- **3-5 stories**, biggest first, related stories grouped.

## Open questions
- Cadence and how issues are triggered (weekly review vs. ad hoc); overlap with the night gardener's ideation.
- Whether to standardize a house sign-off line in the closer.
- Whether the roundup and single-topic articles should ever cross-link to each other.
- Graduate this to a standing runbook once the cadence is settled.
