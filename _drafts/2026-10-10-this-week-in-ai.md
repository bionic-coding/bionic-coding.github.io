---
layout: post
title: "This Week in AI — October 10, 2026"
date: 2026-10-10
description: "GPT-6.1 Sol can get carried away with testing, Haiku 5.5 makes smaller jobs cheaper, and Claude Code mods let developers customize how the agent works."
tags: [model-news, weekly]
---

It was a slower week in AI this week but Anthropic did finally update Haiku and I have a PSA for anyone relying heavily on GPT 6.1 Sol.

## GPT-6.1 Sol can get carried away with testing

Something I've noticed specifically with GPT-6.1 Sol: it has a tendency to overcomplicate things, especially around testing, in ways I haven't seen with GPT-6 Sol or other models.

**Evidence status:** **Reported** — These are observations from my own agent runs, not a controlled comparison between models.

I often run multi-day tasks using an agent graph, where several agents work through different parts of a job. Since adopting Sol 6.1, I've seen a pattern emerge. It's so intent on proving it's correct that it writes test suites that take days to run. Then it attempts to run them multiple times as it works toward a solution.

The testing grows until the task effectively becomes impossible to complete.

I've seen this several times now. The only fix I've found has been to walk back the run and start from scratch.

GPT-6 Sol didn't do this in my runs. It's new with GPT-6.1 Sol. Just something to keep an eye out for.

## Claude Haiku 5.5 makes smaller jobs cheaper

Anthropic released Haiku 5.5 on October 7, with lower token prices and a substantial improvement over Haiku 4.5 on its published coding evaluations.

For prompts up to 100,000 tokens, Haiku 5.5 costs $0.10 per million input tokens and $0.50 per million output tokens. That's 90% below Haiku 4.5's token prices. Above that prompt threshold, the rates rise to $0.50 and $2.50. Long conversations need different cost estimates.

The coding results are interesting. On SWE-Bench Pro, which tests fixes to real software repositories, Haiku scores 64.8% against Sonnet 5.5's 81.3%. On Terminal-Bench 4.0, which tests broader engineering work in a terminal, it scores 39.2% against Sonnet's 70.6%. That's a large gap, even with Haiku's improvement over the previous version.

The qualification I'd keep in mind is effort. Most of Haiku's headline scores use maximum effort, while the API defaults to medium. On one professional-work benchmark, maximum effort used roughly ten times as many output tokens as medium. Cheap tokens can still add up.

For an agent graph, I'd be interested in trying Haiku on smaller, clearly defined jobs: finding a piece of information, summarizing context, or implementing a scoped change. The question is whether it finishes those jobs correctly enough that retries and review don't eat the savings.

There's also a migration detail worth checking: the same input text counts as approximately 30% more tokens than on Haiku 4.5. Anthropic changed the thinking configuration and several other API behaviors too, so read the migration guide before swapping the model name.

Alongside the launch, Anthropic halved Sonnet 5.5's cache-read price to $0.10 per million tokens. That also lowers the cost of agent runs that repeatedly send the same context.

**More info:**

- [**Claude Haiku 5.5**](https://www.anthropic.com/claude-haiku-5-5) — announcement, launch pricing, and the Sonnet cache-price change.
- [Haiku 5.5 system card](https://www.anthropic.com/claude-haiku-5-5-system-card) — coding results and evaluation settings; see pages 111–115 and 131.
- [Haiku 5.5 migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide) — tokenizer changes and request compatibility.

## Claude Code mods let you change how the agent works

Claude Code now supports **mods**: plugins written in JavaScript or TypeScript that run inside Claude Code. They can add panes and buttons, change tool calls, and run commands without asking the model to do anything.

The interface examples are easy to understand. A mod could show how much context you've used, or display the files a command would delete before you let it run. Anthropic shares samples for both.

What interests me is the control over the work itself. A mod can hold a tool call while it asks you a question. It can change which model handles a request. It can also keep track of what's happened across the session.

There are qualifications. Mods run with your account's access to files, processes, and the network. Claude's tool permissions don't automatically restrict a mod's own file access. You're trusting executable code when you install one.

The custom interfaces appear in the terminal and supported Desktop sessions. Other environments, including the VS Code chat panel and headless runs, can run the hooks without showing those interfaces.

I think this is worth watching. It gives developers a way to change how the coding agent works, including where the human gets to intervene. We're working to adopt them in Crux.

**More info:**

- [Claude Code mods overview](https://code.claude.com/docs/en/plugins/mods/overview) — capabilities, sample mods, and supported environments.
- [Mods events and API](https://code.claude.com/docs/en/plugins/mods/events) — interception and failure behavior; the [API guide](https://code.claude.com/docs/en/plugins/mods/api) covers commands and model calls.
- [Managing mods](https://code.claude.com/docs/en/plugins/mods/admin) — organization controls and the limits of tool permissions.
- [Blast Radius sample](https://github.com/anthropics/claude-code-playground/blob/main/claude-code/mods/blast-radius/README.md) — command previews, testing history, and known limitations.

## What I'm actually using

Given the issues I've seen this week with GPT 5.1 Sol I've moved a couple (but not all) agents off of it: one to Claude Opus 5.5 and the other to Kimi K3. Sol is really cost effective, but every time I reduce model diversity in my agent graph I regret it.
