---
title: Claude Code mods — capabilities, control, and trust
slug: claude-code-mods
type: references
tags:
- claude-code
- mods
- plugins
- agentic-harnesses
- security
sources:
- claude-code-mods-overview
- claude-code-mods-events
- claude-code-mods-api
last_reviewed: '2026-10-10'
---

# Claude Code mods

Research checked October 10, 2026. Documentation and sample-source review; no mod was installed or executed. These are rolling sources, not proof of a release date.

## What changes

A mod is a plugin containing JavaScript or TypeScript event handlers that execute inside Claude Code. Handlers can observe, modify, or replace behavior. This adds direct control over parts of the agent application, beyond instructions supplied by a skill or tools supplied by an MCP server.

| Extension | Main purpose | Can draw mod UI? |
|---|---|---|
| Skill | Reusable instructions for Claude | No |
| MCP server | External tools and data | No |
| Settings hook | Run a script, HTTP request, or prompt on an event | No |
| Mod | Handle events inside Claude Code; commands, requests, tool calls, UI | Yes, on supported surfaces |

A plugin can package these together. Mods are an additional plugin capability, not a replacement format for existing skills or MCP servers.

## What users can see and do

- Add panes, tabs, buttons, inputs, or a band above the prompt.
- Restyle built-in rows and the spinner; the permission prompt itself cannot be restyled.
- Pause, rewrite, refuse, or answer a tool call; select a different model for one request.
- Register a slash command that runs code immediately, including while Claude is working.
- Share state across handlers, such as counters or request token usage.

Anthropic's examples include token-weather (context display), blast-radius (command impact preview), and replay-theater (file-edit replay). These are unsupported samples. Built-in examples include the diff pane and AGENTS.md loader. A side-agent mod, you-should-know, is disabled by default and subject to organization availability.

## Availability and platform limits

Mods are enabled by default from terminal version 2.1.287 and Desktop's bundled Claude Code 2.1.286. These are documented minimum versions, not a verified launch date.

| Surface | Hooks | Mod UI |
|---|---|---|
| Terminal, including an editor's integrated terminal | Yes | Yes |
| Desktop Code tab, excluding WSL | Yes | Yes, with some terminal-only elements |
| Desktop WSL session | No; plugins unavailable | No |
| VS Code chat panel | Yes | No |
| Headless CLI and Agent SDK | Yes | No |
| Remote Control | On the host machine | In the host terminal |
| Cloud session | If plugin reaches the session | No |

Mods install through normal plugin marketplaces. A shell-side install/update requires `/reload-plugins` in an existing session. `claude plugin validate` can report handled events and API calls without executing the mod. Validation is an inspection aid, not a safety certification.

## Trust boundary

Mods run with the user's account permissions. They can read secrets, access files, start processes, use the network, change session content, approve calls, and spend model usage. Processes started by a mod are outside Claude Code's Bash sandbox. API-mediated access does not mean sandboxed access.

The overview says a mod can override some user permission decisions. Managed controls require a closer reading before treating a mod as a policy boundary. The settings that disable installed mods do not necessarily disable built-in mods.

## Editorial angle

Inference: Claude Code is opening its own interface and execution flow to customization. A context meter is the visible example; interception of model requests and tool decisions is the larger change. Useful potential applications include an agent-status pane, a test-run budget display, or approval controls informed by project state. These are possibilities, not built features or proven benefits.

For the weekly post, distinguish documentation-confirmed capabilities from hands-on results. Do not describe mods as universally available UI widgets, as sandboxed plugins, or as a guaranteed fix for runaway testing.

Source: [[research/sources/claude-code-mods-overview]].

## Event middleware and failure behavior

Handlers receive `($, e, next)`. Events are deeply frozen: rewriting means passing a changed copy to `next`. Omitting `next` replaces normal behavior and stops later handlers. A `tool.call` handler wraps tool execution, including subagent and MCP calls; code after execution cannot undo the tool's side effects.

`tool.check` follows permission rules and settings-hook decisions, and can change allow, ask, or deny. User settings hooks are therefore not an absolute boundary against installed mods. Organization-managed `PreToolUse` hooks run before mod `tool.call` handlers, and their blocks are final.

Order matters: the built-in security guard (where applicable), organization prepend/ordinary mods, user mods, organization append mods, then other built-ins. An earlier handler can inspect or stop later handlers and their API calls. Dependencies run after the mods depending on them.

A failing hook is skipped by default. Before `next`, that can let ordinary behavior continue; after `next` completes, Claude Code preserves its result without rerunning the operation. A handler's `.catch` can return a denial, but if that error handler itself fails or times out, the fallback is still to skip it. A guard therefore needs deliberate failure handling and tests; merely adding an interception hook does not establish a fail-closed control.

`$.ui.ask` can hold a tool call for a decision. Its API wait does not consume the hook execution budget, but waiting on a mod's own promise does. A timeout can skip the hook and allow the original call to continue. Headless sessions need an explicit fallback when no user can answer.

`turn.step` can change the model for a request and inspect actual usage, including cache usage. Subagent requests carry an agent identifier. Server-side tools such as an advisor do not produce ordinary `tool.call` or `tool.check` events; `serverToolUses` requires v2.1.290. Rewriting prompts or context can reduce prompt-cache reuse.

**Application inference:** test-budget tracking and a confirmation gate before repeated expensive commands are plausible mods. They would need headless behavior, failure-path coverage, and shell-command classification tests before being treated as dependable controls.

Source: [[research/sources/claude-code-mods-events]].

## API capabilities and boundaries

Mods can register slash commands at session start. An `immediate: true` command runs while Claude is working, without a model turn. They can also register tools directly; their `mcp__...` names do not imply that an external MCP server is involved.

`$.model.complete` makes an isolated model request without project context or tools. `$.model.fork` includes the current conversation, project context, and tool definitions, but the model cannot call those tools. Both consume usage under the session's plan, API key, or provider. These helpers should not be confused with a full autonomous agent runtime.

Timers run mod code without a model turn unless the mod submits a prompt. Timers stop when the mod reloads. Submitted prompts queue until idle; `asUser: true` can omit mod sender attribution. Session messaging supports other sessions and agents, but sender labels are not trustworthy identities.

The hooks module cannot directly use Node APIs, filesystem/network globals, or normal timer globals. Instead, the `$` API exposes files, processes, HTTP, persistent storage, environment access, settings, conversation history, usage, and MCP calls. This API mediation enables inspection and earlier policy-mod interception; it is not operating-system sandboxing. In particular, denying a process-spawn event after the process starts does not undo it.

Some capabilities have higher version requirements than the overall mods minimum: cache block arrays require v2.1.292 and explicit `isDeferred: false` tool registration requires v2.1.293. Version-sensitive examples need checking against the installed runtime.

Source: [[research/sources/claude-code-mods-api]].
