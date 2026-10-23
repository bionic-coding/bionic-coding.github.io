---
layout: post
title: "This Week in AI — October 14, 2026"
date: 2026-10-14
description: "Gemini 4 Argon is earning a place in my rotation, we're introducing Claude mods support in Crux, and OpenCode 2 has launched with Crux support."
tags: [model-news, weekly, gemini, claude-code, opencode, crux]
---

Gemini 4 has finally arrived, and I've slowly been working it into my rotation. This week also brings OpenCode 2 and more ways to customize how coding agents work. We're introducing support for Claude mods in Crux, with a similar plugin planned for OpenCode.

## Gemini 4 is impressive for the price

Google's Gemini 4 Argon is now available through the paid API, and my early impression is that it's impressive for the price.

**Evidence status:** **Verified** — Google's documentation confirms API availability, token limits, and the dated pricing schedule. My impression comes from using it.

Standard API pricing starts at US$2 per million input tokens and US$10 per million output tokens, including thinking. Cached input costs US$0.10 per million tokens. Those are introductory prices through November 30. On December 1, all three rates double.

That's a detail worth keeping in mind when deciding where it fits. I'm gradually adding it to the work I'm already doing. So far, it's giving me a reason to keep using it.

The other headline is how long it can spend on a problem. Argon supports a million-token window shared across input, thinking, and output. That means a large input leaves less room for the answer and the reasoning that produces it. Longer generation also requires the appropriate continuation setup; swapping the model name doesn't enable everything.

I haven't settled on its permanent place in the rotation yet. The introductory price makes it easier to try, but the useful comparison is what a completed job costs after retries and review.

**More info:**

- [**Gemini 4 Argon API guide (checked Oct 14)**](https://ai.google.dev/gemini-api/docs/latest-model) — availability, the shared token window, and longer generation.
- [Gemini API pricing (checked Oct 14)](https://ai.google.dev/gemini-api/docs/pricing) — current rates and the December 1 increase.
- [Cloud developer guide (checked Oct 13)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-argon) — the Cloud integration has different continuation requirements.

## Claude mods are coming to Crux

We're introducing support for Claude Code mods in Crux.

**Evidence status:** **Verified** — Anthropic documents mods' capabilities and supported interfaces. Crux support is upcoming.

I mentioned mods last week. They're plugins with JavaScript or TypeScript handlers that run inside Claude Code. They can add interface elements, respond to events, and intervene in tool calls.

A skill gives the agent instructions. A mod can change the application around the agent. It could display project state in a pane, or pause a tool call while it asks you to make a decision. Commands can also run code immediately without waiting for another model turn.

That opens up useful possibilities for Crux. Having a process written down helps the agent follow it. Making parts of that process visible while the agent works could make it easier for the human to follow too. That's the direction we're exploring as we introduce mods support.

One qualification carries over from last week: mods run with your account's access to files, processes, and the network. Installing one means trusting its code. Custom UI also depends on where you run Claude Code; supported terminal and Desktop sessions can show interfaces that headless runs cannot.

**More info:**

- [**Claude Code mods overview (checked Oct 14)**](https://code.claude.com/docs/en/plugins/mods/overview) — what mods can do, where they run, and what access they have.
- [Mods API (checked Oct 14)](https://code.claude.com/docs/en/plugins/mods/api) — commands, session data, and model calls available to a mod.

## OpenCode 2 has finally launched

OpenCode 2 is here. Crux supports it, and we'll add a plugin that offers similar customization to Claude mods.

**Evidence status:** **Verified** — Anomaly's announcement and V2 documentation confirm the release and its main changes. The Crux plugin is planned.

The biggest everyday change is a shared background service. The terminal, web interface, and desktop app connect to the same process. Background subagents and shell commands let work continue while you keep prompting.

There's also Code Mode. The agent can write a small JavaScript script that calls tools, processes the results, and calls other tools. That gives it a way to compose a workflow without returning every intermediate result to the conversation.

For Crux, the new plugin system is the part to watch. OpenCode can load changes during a session, and plugins can customize both behavior and the terminal interface. We'll use its own plugin APIs for the planned Crux extension.

If you're upgrading an existing setup, read the migration guide. V1 plugin implementations need a port, and the server API has changed. Most supported configuration, agent files, commands, and skills remain accepted. There's no need to rewrite the whole setup just to try V2.

**More info:**

- [**OpenCode 2.0 announcement (checked Oct 14)**](https://anoma.ly/notes/opencode-2-0/) — the shared service, Code Mode, background work, and plugin changes.
- [V1 migration guide (checked Oct 14)](https://opencode.ai/v2/docs/migrate-v1/) — what breaks and what should continue working.
- [V2 tools guide (checked Oct 14)](https://opencode.ai/v2/docs/tools/) — how Code Mode and background tasks work.

## What I'm actually using

Gemini 4 is slowly joining my rotation. I'm impressed with what it offers for the price, and I want more time with it before deciding how much work to send its way.

On the Crux side, we're introducing Claude mods support and planning a similar plugin for OpenCode 2. I'm interested in what those interfaces can make visible while an agent works. The human still needs to understand what's happening and decide what comes next.
