---
title: "OpenCode 2.0 release research brief"
slug: opencode-2-0-release
type: brief
status: draft
created_at: 2026-10-13
updated_at: 2026-10-13
authors: ["Codex"]
tags: [opencode, anomaly, coding-agents, agent-harness, plugins, migration, editorial]
related_adrs: []
---

# OpenCode 2.0 release research brief

**Research checked October 13, 2026.** Prepared for Bionic Coding from the supplied announcement and OpenCode's V2 documentation.

OpenCode 2.0 expands how developers direct and extend coding agents. A shared service coordinates clients and sessions. Code Mode composes tools in scripts. Background work lets the main conversation continue. The practical value depends on whether those capabilities reduce waiting and coordination without increasing review work.

## What Anomaly announced

Anomaly describes six main changes: a default background service, a rebuilt server API, Code Mode, background tasks, revised plugins, and an embeddable SDK. The agent can use its own API to manage sessions and worktrees. MCP tools enter Code Mode by default, where the agent can discover them and combine calls in JavaScript. [OpenCode 2.0 announcement](https://anoma.ly/notes/opencode-2-0/).

The note also announces stable TUI plugins and hot reload, including plugins written and loaded during a session. Anomaly says it implemented more than 80 internal plugins to exercise the API. The note's scale and performance language is vendor reporting; it supplies no comparative benchmark establishing better task outcomes. [Announcement](https://anoma.ly/notes/opencode-2-0/).

## What changes in everyday use

### One service across clients

Local clients discover or start one shared background server per user account. It owns sessions, configuration, integrations, permissions, and tool execution. The CLI supports a private server through `--standalone`, or an explicit endpoint through `--server`. [CLI service documentation](https://opencode.ai/v2/docs/cli).

The practical implication is continuity: a terminal session and another client can operate through the same service. Private servers remain available when a workflow needs separate runtime state. This changes where session lifecycle and failures must be inspected.

### Tools composed through code

The `execute` tool runs JavaScript against a tool catalog. It can parallelize independent calls and process results before returning selected information to the model. The interpreter has no direct filesystem access, imports, timers, or `fetch`. Each nested tool still enforces its own permissions. [Tools documentation](https://opencode.ai/v2/docs/tools/).

That provides a mechanism for reducing intermediate context. For example, a script can retrieve records, filter them, and submit selected records to another tool. Whether this saves tokens or improves correctness depends on the workload and the generated script.

### Work continues in the background

Shell commands and subagents can return immediately, then notify the session when finished. A background subagent returns a session ID so the parent can continue the same child conversation. The default subagent nesting depth is one. Background shell commands have no timeout unless one is supplied. [Tools documentation](https://opencode.ai/v2/docs/tools/).

The announcement also describes a hotkey for moving running foreground work into the background and subagents using a different model. [Announcement](https://anoma.ly/notes/opencode-2-0/).

These capabilities can shorten waiting between independent tasks. They also require clear task ownership and a check that all relevant results have arrived before declaring completion.

## What changes for builders

| Package | Role |
| --- | --- |
| `@opencode/client` | Connects an application to an OpenCode server over HTTP. |
| `@opencode/sdk` | Hosts OpenCode within an application. |
| `@opencode/plugin` | Defines extensions through the V2 plugin API. |

The network client includes local service discovery and startup helpers. Its event subscriptions are live-only: they do not replay missed events or reconnect automatically. Integrations must handle recovery rather than assume a continuous event history. [Client documentation](https://opencode.ai/v2/docs/build/client/).

The SDK assembles the server and routes calls in memory, without opening an HTTP listener. Applications explicitly own the host and release it when finished. Plugins can customize agents, models, and tools at startup or register afterward. [SDK documentation](https://opencode.ai/v2/docs/build/sdk).

A separate Workerd profile supports Cloudflare Durable Objects, using SQLite storage and durable events for eviction recovery. It replaces unavailable local filesystem and process services. This is a specialized hosting profile; a local CLI environment should not be assumed to carry over unchanged. [Cloudflare SDK guide](https://opencode.ai/v2/docs/build/sdk/cloudflare).

## Migration requirements worth calling out

The main breaks are the plugin API, server API, and terminal configuration. Terminal settings move to global `cli.json`; project-local terminal settings are not migrated. Supported V1 configuration, agent files, commands, and skills generally remain accepted. [V1 migration guide](https://opencode.ai/v2/docs/migrate-v1/).

Two additional details affect this repository's workflows:

- **Instructions:** V2 currently discovers `AGENTS.md` only. A workflow relying on the V1 `CLAUDE.md` fallback needs its guidance carried into `AGENTS.md`.
- **Diagnostics:** V2 preserves `lsp` configuration but does not run language servers, expose LSP tools, or produce LSP diagnostics. Use lint, typecheck, or compiler commands for those checks.

The guide also says V1 and V2 share configuration locations and the `opencode` command. Preserve the V1 setup while validating V2. Native V2 configuration conversion is optional. [Migration guide](https://opencode.ai/v2/docs/migrate-v1/).

Plugin implementations require a port. Renaming the configuration or moving a file is insufficient. V2 uses `Plugin.define` with a stable ID and `setup(ctx)`, where extensions register hooks and transforms. Verify each extension's behavior, reload cleanup, options, and persisted state. [Plugin migration guide](https://opencode.ai/v2/docs/build/plugins/migrate-v1/).

The announcement's CLI upgrade instruction is to update to the latest 1.x release, then run `opencode upgrade --major`. [Announcement](https://anoma.ly/notes/opencode-2-0/).

## Implications for Bionic Coding

The editorial angle is **what the agent harness enables**. A model's ability to solve a task and the harness's ability to manage tools, sessions, and concurrent work are separate things. This release offers concrete examples for explaining that distinction.

For Crux workflows, the immediate research question is compatibility. File-based roles and skills need different evaluation from executable plugins and server integrations. Review instruction discovery, permission behavior, background completion, and diagnostic commands before adopting V2 for a real cycle.

A useful trial would compare the same model and repository task across V1 and V2. Include one MCP workflow, one background review, and one plugin-dependent workflow. Measure accepted outcomes, elapsed time, token cost, missed completion events, and human interventions. That isolates the harness change more clearly than comparing different models at the same time.

## Evidence and follow-up

The linked documentation corroborates the advertised mechanisms and identifies migration constraints. This brief does not establish measured productivity gains. No OpenCode upgrade, plugin port, or hands-on evaluation was performed.

Next steps are to inventory any V1 integrations, test a representative workflow with preserved configuration, and verify that instructions and required checks still reach the agent. Keep the proposed trial separate from a decision to migrate.
