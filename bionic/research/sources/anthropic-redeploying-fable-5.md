---
title: "Redeploying Claude Fable 5"
slug: anthropic-redeploying-fable-5
type: source
source_url: https://www.anthropic.com/news/redeploying-fable-5
source_date: 2026-06-30
author: "Anthropic"
captured_at: 2026-07-14
last_source_check: 2026-07-14
raw_path: research/raw/2026-07-14/anthropic-redeploying-fable-5/
previous_captures: []
static: true
tags: [anthropic, claude, fable, mythos, export-controls, safeguards, jailbreak]
---

# Redeploying Claude Fable 5

_Anthropic news post, 2026-06-30. The primary source for the Fable 5 suspension **cause** — it reconciles the "export controls" vs. "enhanced safeguards" accounts (both are true: export controls were the cause, new safeguards were the fix)._

## Timeline (verbatim)

> On Friday, June 12, the US government applied export controls to our newest models, Claude Fable 5 and Claude Mythos 5. This required us to restrict access to foreign nationals, whether inside or outside the United States. Because the order took effect immediately and we had no reliable way to verify nationality in real-time, we suspended access to both models for all users.

> As of today, June 30, the export controls on Fable 5 and Mythos 5 have been lifted.

Fable 5 returned **globally on Wednesday, July 1** (Claude Platform, Claude.ai, Claude Code, Cowork). Pro/Max/Team/select Enterprise plans got it for up to 50% of weekly usage limits through **July 7**, after which it moves to **usage credits**. AWS / Google Cloud / Microsoft Foundry to follow. Mythos 5 access was restored to a set of US organizations after government approval on June 26 (Project Glasswing).

## The cause (verbatim)

> The export control directive on June 12 came after the government became aware of a report in which **Amazon researchers had found a method of bypassing Fable 5's safeguards**: prompting it so that it identified a number of software vulnerabilities. In one case, the model produced code demonstrating how the relevant vulnerability could be exploited.

**Important nuance Anthropic adds:** their testing found the reported technique was **not** a unique Mythos-level capability — "many less capable models—including Claude Opus 4.8, GPT-5.5, and Kimi K2.7—could identify the same vulnerabilities," and every model tested (incl. Haiku 4.5, Sonnet 4.6, Opus 4.6/4.7/4.8, GPT-5.4/5.5) could produce the same exploit demonstration. It was "a borderline case for Fable 5's safeguards" involving "routine defensive cybersecurity work."

## The fix (verbatim)

> Working closely with the government, we trained an improved safety classifier that targets and blocks the behavior described in the report. Users will be notified if a request to Fable 5 is blocked, and the request will instead be sent to Opus 4.8.

The new classifier blocks the reported technique "in over 99% of cases." The US Dept. of Commerce's Center for AI Standards and Innovation (CAISI) tested the prior and new safeguards and "agree that they are extraordinarily strong." Anthropic notes the tighter classifier also raises false positives on routine coding/debugging.

## Also in the post

- Anthropic's safeguards use **classifiers** with a deliberate "safety margin" (blocking some likely-benign requests to be sure of catching harmful ones); Fable 5 shipped with the largest safety margin they'd ever applied.
- With Amazon, Microsoft, Google, and Glasswing partners, they've started developing a **shared industry framework for judging jailbreak severity**.

## Capture gaps

- Captures the news post's load-bearing text; the full immutable capture (`source.html` + rendition + the safety-margin diagram) is in `research/raw/2026-07-14/anthropic-redeploying-fable-5/`.
