---
title: Agentic Harnesses
order: 5
summary: "The tools that give an AI model hands — Claude Code, Codex, and OpenCode."
status: published
updated: 2026-07-17
---

The [Agents]({{ "/learn/agents/" | relative_url }}) lesson described the *idea* of an agent — a model in a loop with tools. An **agentic harness** is the actual product that runs that loop for you: the thing you install and point at a job. If the model is the engine, the harness is the whole car around it — the seat, the wheel, the brakes, the dashboard. You don't drive an engine; you drive the car.

You may know these by other names — *coding agents*, *AI IDEs*, *CLI agents*, *agent workbenches*. This lesson calls the category **agentic harnesses**, and — because the products move fast — it treats the specific tools lightly and the **way to compare them** as the part worth keeping. Harnesses exist for other kinds of work too, but the clearest examples today are coding tools, so that's what this lesson uses.

## What a harness actually is

The harness is everything wrapped around the model that turns "predict text" into "get work done." It holds the conversation, hands the model its **tools** (files, a terminal, the web, [MCP]({{ "/learn/mcp/" | relative_url }}) servers — the capabilities from the [Skills]({{ "/learn/skills/" | relative_url }}) lesson), runs the reason → act → observe loop, sets the approval rules and sandboxing, and shows you a log of what happened.

The first thing to get straight: **the harness is not the AI.** Claude Code isn't a model — it's a program that *drives* one. In principle the model and the harness are separate pieces; in practice some harnesses let you swap models freely (OpenCode) while others weld the hood shut and drive only their maker's models (Claude Code runs Claude; Codex runs GPT). Either way, the harness is where the plumbing and the safety live — the same point the [Skills]({{ "/learn/skills/" | relative_url }}) lesson made about the harness deciding whether a tool call actually runs.

## How you actually interact with one

Three shapes, and most products offer more than one:

- **Command line (CLI)** — you type to it in a terminal. Powerful and scriptable, a little intimidating at first. (Claude Code, Codex, and OpenCode all work this way.)
- **In your editor (IDE)** — it lives inside VS Code or a JetBrains editor as a side panel or inline suggestions.
- **Cloud app** — you hand it a task in a web app and it works in a hosted environment, nothing installed on your machine.

Where you type doesn't change what it *is* — a loop with tools — only how close it sits to your files and your risk.

## A framework for comparing them

This is the durable part. Judge any harness on these axes, and every product decision becomes a point on them:

- **Local vs. hosted** — does it run on *your* machine (your files, your secrets, your risk) or in the cloud (someone else's)?
- **File & terminal access** — can it read and write your files and run commands? That's its power *and* its blast radius.
- **Repo awareness** — does it understand a whole codebase, or just the file in front of it?
- **Tool support** — can you plug in more tools, and does it speak [MCP]({{ "/learn/mcp/" | relative_url }}) (a standard way to plug in tools and data — its own lesson)?
- **Approvals & sandboxing** — does it pause before risky actions, and can it run walled off from the real thing?
- **Model choice** — locked to one model, or can you pick?
- **Cost** — how it bills, and how fast a loop can run up the tab.
- **Privacy** — where your code and data go, and what's retained.

## Cost and limits

Because a harness runs the model in a **loop**, it can spend a lot, fast — every step is another model call, and a big task is dollars, not cents. Watch for usage caps, the "it got stuck in a loop" burn, and the plain fact that more autonomy means more calls. Set a budget and a stop before you start.

And the safety caveats from the Agents lesson apply *double* here, because a harness has hands. Coding harnesses have already been caught doing real damage: one (GPT-5.6 running in Codex) deleted users' files in a full-access mode, and another (the Grok Build CLI) uploaded whole repositories to the cloud. Sandbox a harness before you trust it; don't hand it full access to everything on the first date. (Sandboxing just means giving it a walled-off place to work — a throwaway copy of the project, a fresh git branch, or a container — so a mistake can't reach the real thing.)

## The tools, briefly (as of 2026 — features move fast)

Treat this as a map, not a spec sheet — check each product's current docs before you rely on a specific feature.

- **Claude Code** (Anthropic) — a terminal-first coding harness that drives Claude models, strong at whole-repo, multi-step work; also available inside editors.
- **Codex** (OpenAI) — OpenAI's coding agent, in the terminal and the cloud, driving GPT models. (It's the one in the file-deletion story above — a nudge to check its sandboxing settings before granting full access.)
- **OpenCode** — an open-source, model-agnostic terminal harness: you bring your own model and keys. Worth a look if avoiding lock-in matters — though "your own keys" doesn't automatically mean *private*: if the model behind them is a cloud service, your code still travels to that provider.

## A real workflow

Point a harness at a repo and say: *"add input validation to the signup form, with tests."* It reads the relevant files, proposes an edit (you approve), writes the code, runs the tests, sees a failure, fixes it, runs again, and opens a pull request with a summary (if you've connected it to your code host) — pausing for your okay at the steps that matter, like writing files or opening the PR. You're the reviewer; it's the tireless junior that shows its work. Your job isn't to type the code — it's to *check what it did* before you say yes: read its plain-English summary, see whether the tests passed, and try the thing it changed.

## How to choose

A quick guide, keyed to the framework above:

- **Nervous, or not a coder?** Start with a hosted app on a throwaway project — no local access, low stakes, easy to walk away from.
- **Working in a real codebase?** A local CLI or in-editor harness with repo awareness — but sandbox it and keep approvals on.
- **Care about lock-in?** An open, model-agnostic harness where you control the model and the keys. (Privacy is a *separate* question — it turns on where the model actually runs: a local or self-hosted model keeps your data in; a cloud model sends it out no matter which harness you use.)
- **Whatever you pick:** turn on approvals, sandbox it, grant least privilege, watch the log. Yes — the same four habits from the [Agents]({{ "/learn/agents/" | relative_url }}) lesson. They're the whole ballgame.

## Further reading

A short, still-live (2026) list — where to go deeper. These move fast, so check the current docs before relying on a specific feature.

- **[Claude Code docs](https://docs.claude.com/en/docs/claude-code/overview)** — Anthropic's terminal-first harness.
- **[OpenAI Codex](https://developers.openai.com/codex)** — OpenAI's coding agent, terminal and cloud.
- **[OpenCode](https://opencode.ai)** — the open-source, model-agnostic option.
- Next door: **[Agents]({{ "/learn/agents/" | relative_url }})** (the idea a harness runs) and **[MCP]({{ "/learn/mcp/" | relative_url }})** (how it plugs in more tools).
