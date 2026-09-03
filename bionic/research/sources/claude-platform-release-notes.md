---
title: "Claude Platform release notes"
slug: claude-platform-release-notes
type: source
source_url: https://platform.claude.com/docs/en/release-notes/overview
source_date: null
author: null
captured_at: 2026-08-25
last_source_check: 2026-08-25
raw_path: research/raw/2026-08-25/claude-platform-release-notes/
previous_captures: []
static: false
tags: [anthropic, pricing, release-notes, opus-5, sonnet-5, api]
---

The Claude Platform release notes list changes to the Claude API, the client SDKs, and the Claude Console, newest first.

> This capture covers the window **2026-07-24 through 2026-08-20** — from the Claude Opus 5 launch entry forward. See `## Capture gaps` for what was left out and why.




## August 20, 2026

  * We've released **v1.0 of the[Python SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python)**. The SDK's HTTP layer moves from `httpx` to [httpx2](https://httpx2.pydantic.dev), a maintained, API-compatible fork: build custom `http_client`, `Timeout`, and transport objects from `httpx2` (the `DefaultHttpxClient` helpers are unchanged), and call `httpx2.alias_httpx()` at startup if you rely on tracing or mocking libraries that patch `httpx`. v1.0 requires Python 3.10 or later and removes long-deprecated surface, including the legacy Text Completions API, the `temperature`, `top_p`, and `top_k` parameters on Messages methods, and the tool runner's client-side `compaction_control`. On the async client, `.with_raw_response` results now need `await response.parse()`, and `AnthropicBedrock` now raises an error when no AWS region is configured instead of defaulting to `us-east-1`. See the [v1 migration guide](https://github.com/anthropics/anthropic-sdk-python/blob/main/MIGRATION.md) for every change with before-and-after snippets.



## August 19, 2026

  * The [computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) is out of beta on the Claude API as the `computer_toolset_20260801` toolset: no beta header, batch actions (several actions in one turn), `zoom` enabled by default, and per-member configuration through `configs`. Earlier beta versions remain available. Upgrading an existing integration changes the request shape and tool handling; see [Migrate from `computer_20251124`](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#migrate-from-computer-20251124).
  * We've launched the [browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool) (`browser_toolset_20260801`), a client toolset for driving a browser that your application hosts. It works inside a browser viewport rather than a whole desktop, reading the page itself (its accessibility tree, elements, forms, and tabs) and adding element references, form input, tab management, download reporting, and opt-in file upload on top of screenshot-and-click control.
  * Both toolsets are available for Claude Fable 5, Claude Mythos 5, Claude Opus 5, Claude Sonnet 5, and Claude Opus 4.8 on the Claude API.
  * The [Files API](https://platform.claude.com/docs/en/build-with-claude/files) is out of beta on the Claude API. Requests to the `/v1/files` endpoints, and Messages API requests that reference an uploaded file, no longer require the `files-api-2025-04-14` beta header. Requests sent without the header use the current response format: [file expiration](https://platform.claude.com/docs/en/build-with-claude/files#file-expiration) (set `expires_in_seconds` when you upload a file; file objects report `expires_at`), and `page` and `next_page` [pagination](https://platform.claude.com/docs/en/api/overview#pagination) plus an `ids[]` filter when you [list files](https://platform.claude.com/docs/en/build-with-claude/files#list-files). `/v1/files` requests that still send the beta header keep working and return the previous response format.
  * [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) and the Skills API (`/v1/skills`) are out of beta on the Claude API. Requests no longer require the `skills-2025-10-02` beta header, including Messages API requests that load Skills through the `container` parameter. Requests that still send the header continue to work unchanged. See [Using Agent Skills with the API](https://platform.claude.com/docs/en/build-with-claude/skills-guide).
  * The [Admin API](https://platform.claude.com/docs/en/api/admin) user-management endpoints for **Claude Enterprise** (claude.ai) organizations (members, invites, groups, and custom roles) are out of beta. The `anthropic-beta: ce-user-management-2026-07-13` header is no longer required on group and custom-role requests; requests that still send it are accepted unchanged. See [User management](https://platform.claude.com/docs/en/manage-claude/user-management).
  * You can now restrict which sites a Claude Managed Agents agent's `web_search` and `web_fetch` tools can reach. Set `allowed_domains` or `blocked_domains` on the tool's entry in the `agent_toolset_20260401` `configs` array; `web_fetch` also accepts `max_content_tokens` and `web_search` accepts `user_location`. Each `configs` entry is identified by its `name` and typed by an optional `type`, and requests that pass only `name`, `enabled`, and `permission_policy` continue to work; in the typed SDKs, `configs` entries become per-tool types. See [Restrict web search and web fetch domains](https://platform.claude.com/docs/en/managed-agents/tools#restrict-web-search-and-web-fetch-domains).
  * Claude Managed Agents sessions that run in a [self-hosted sandbox](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) can now attach [memory stores](https://platform.claude.com/docs/en/managed-agents/memory). The Python, TypeScript, and Go SDK workers download each attached store into the sandbox at its `mount_path` and sync the agent's changes back to the store. See [Use memory stores](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#use-memory-stores).
  * The session viewer in the Claude Console has been redesigned with a timeline minimap, a transcript grouped by model request, and an Inspector panel for session details and cost, raw events, per-tool statistics, mounted resources, and per-thread activity. See [Console observability](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#console-observability).



## August 18, 2026

  * Workbench is now [**Playground**](https://platform.claude.com/playground) in the Claude Console. Playground supports every Messages API parameter and includes templates that demonstrate API features such as code execution and web search. It shows the full SDK request and the API response for each run, to help you understand the API and build with it. For more, see the [Claude Help Center](https://support.claude.com/en/articles/8606378-how-do-i-use-playground) or try it at [platform.claude.com/playground](https://platform.claude.com/playground).



## August 11, 2026

  * The [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api) now returns transcripts of Cowork and Claude Code sessions that run on your users' machines, in beta for Claude Enterprise organizations. `GET /v1/compliance/apps/sessions/local` lists sessions across your organization, `GET /v1/compliance/apps/sessions/local/{session_id}` retrieves one session's metadata, and `GET /v1/compliance/apps/sessions/local/{session_id}/messages` returns its transcript, all with your existing Compliance Access Key and the `read:compliance_user_data` scope. See [Sessions on users' machines](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#retrieve-local-sessions).
  * We've added the `anthropic-workspace-id` response header to the Claude API. It carries the `wrkspc_`-prefixed ID of the workspace that the request's API key or access token resolved to, including your organization's Default Workspace. See [Identify the workspace behind an API response](https://platform.claude.com/docs/en/manage-claude/workspaces#identify-the-workspace-behind-an-api-response).



## August 10, 2026

  * The introductory pricing for **Claude Sonnet 5** ($2 / $10 per MTok) is now the standard price: the previously scheduled increase to $3 / $15 per MTok on September 1, 2026 will not occur. See [Pricing](https://platform.claude.com/docs/en/about-claude/pricing).



## August 7, 2026

  * You can now set a budget on a Claude Managed Agents session: a hard cap on the session's spend, priced at public list rates. A session that reaches its budget pauses with the `budget_reached` stop reason instead of starting new model requests; changing or removing the budget resumes it. Deployments accept the same budget and apply it to each session they start. See [Session budgets](https://platform.claude.com/docs/en/managed-agents/budgets).
  * You can now give a Claude Managed Agents session an advisor: a model at least as capable as the agent's own that the session's primary thread can consult mid-turn for strategic guidance. Configure it as a `{"type": "advisor"}` entry in the agent's multiagent roster, naming the `model` to consult. See [Give the session an advisor](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration#give-the-session-an-advisor).
  * You can now control where model inference runs for a Claude Managed Agents agent. Set `inference_geo` inside the `model` object when you [create the agent](https://platform.claude.com/docs/en/managed-agents/agent-setup#pin-the-inference-geo), or [override it for a single session](https://platform.claude.com/docs/en/managed-agents/sessions#pin-the-inference-geo-for-a-session). See [Data residency](https://platform.claude.com/docs/en/manage-claude/data-residency) for the available geos and pricing.
  * Claude Managed Agents sessions can now [load skills from a GitHub repository](https://platform.claude.com/docs/en/managed-agents/skills#load-skills-from-a-github-repository). When a session [mounts a repository](https://platform.claude.com/docs/en/managed-agents/github), any skills in its root `.claude/skills` directory are discovered automatically at session start and available to the agent for that session.



## August 5, 2026

  * **Inference hooks** are now in beta for Claude Enterprise organizations. Point Claude at your organization's AI security server, and each governed prompt across claude.ai, Cowork, and Claude Code is held for the server's allow or deny verdict before inference proceeds. Requests are signed, failure handling is configurable, and every denial is recorded in the compliance [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed). See [Inference hooks](https://platform.claude.com/docs/en/manage-claude/inference-hooks).
  * We've retired the Claude Opus 4.1 model (`claude-opus-4-1-20250805`). All requests to this model on the Claude API will now return an error. We recommend upgrading to [Claude Opus 5](https://platform.claude.com/docs/en/models/overview#latest-models-comparison). Researchers can request ongoing access through the [External Researcher Access Program](https://support.claude.com/en/articles/9125743-what-is-the-external-researcher-access-program).



## August 3, 2026

  * The [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api) now returns transcripts of Cowork sessions started on claude.ai web or mobile, in beta for Claude Enterprise organizations. `GET /v1/compliance/apps/sessions/remote` lists sessions and `GET /v1/compliance/apps/sessions/remote/{session_id}/messages` returns one session's transcript, using your existing Compliance Access Key with the `read:compliance_user_data` scope. See [Sessions in the cloud](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#retrieve-remote-sessions).



## August 1, 2026

  * [Dreams](https://platform.claude.com/docs/en/managed-agents/dreams) (research preview) now supports Claude Opus 5. See [Supported models](https://platform.claude.com/docs/en/managed-agents/dreams#limits).



## July 24, 2026

  * We've launched **Claude Opus 5** (`claude-opus-5`), a step-change improvement over Claude Opus 4.8. Claude Opus 5 supports a [1M token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) (both the default and the maximum), 128k max output tokens, and [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) on by default, at $5 / $25 USD per MTok, the same pricing as Claude Opus 4.8. It's available on the Claude API, [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), [Claude on Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai), and [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry). See [What's new in Claude Opus 5](https://platform.claude.com/docs/en/models/opus-5/whats-new-opus-5) for new features, behavior changes, and migration guidance, and the [models overview](https://platform.claude.com/docs/en/models/overview) for complete specs.
  * On Claude Opus 5, disabling thinking is allowed only at effort `high` or below: `thinking: {"type": "disabled"}` with effort `xhigh` or `max` returns a 400 error, a breaking change from Claude Opus 4.8. See [What's new in Claude Opus 5](https://platform.claude.com/docs/en/models/opus-5/whats-new-opus-5#behavior-changes).
  * [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) is the primary control for steering Claude Opus 5: the model supports the full ladder (`low`, `medium`, `high`, `xhigh`, `max`), with `max` for capability-critical work.
  * Mid-conversation tool changes are now in beta on Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, and Claude Opus 5: add or remove tools between turns of a conversation while preserving the prompt cache. Include the `mid-conversation-tool-changes-2026-07-01` beta header in your requests.
  * The `fallbacks` parameter now supports a `"default"` mode, which applies Anthropic's recommended fallback models by refusal category. Server-side fallback is in beta, and the `"default"` mode requires the `server-side-fallback-2026-07-01` beta header. See [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback).
  * We've removed [fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode) for Claude Opus 4.7. Requests to `claude-opus-4-7` with `speed: "fast"` now return an error; unlike Claude Opus 4.6, they do not fall back to standard speed. Claude Opus 4.7 itself remains available at standard speed. To continue using fast mode, migrate to [Claude Opus 5](https://platform.claude.com/docs/en/models/opus-5/migration-guide#migrating-from-claude-opus-47) or Claude Opus 4.8. Read more in [Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode#supported-models).



## July 22, 2026

  * You can now set an `effort` level on a Claude Managed Agents agent's model configuration. Pass `effort` inside the `model` object when you [create the agent](https://platform.claude.com/docs/en/managed-agents/agent-setup#create-an-agent). See [Effort levels](https://platform.claude.com/docs/en/build-with-claude/effort#effort-levels) for what each level does.
  * Webhooks for Claude Managed Agents now cover the environment and memory store lifecycle: four `environment.*` event types and three `memory_store.*` event types. You can react to environment and memory store lifecycle changes without polling. See the Environment events and Memory store events tabs in [Subscribe to webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks#supported-event-types).
  * When creating a Claude Managed Agents session, you can now [seed it with initial events](https://platform.claude.com/docs/en/managed-agents/sessions#seed-the-session-with-initial-events). Pass `initial_events` on `POST /v1/sessions` with up to 50 `user.message` and `user.define_outcome` events. A non-empty list starts the agent loop in the same call, so you don't need a separate send-events request to start work.
  * The `version` field is now optional when [updating a Claude Managed Agents agent](https://platform.claude.com/docs/en/managed-agents/agent-setup#update-an-agent). Supply it for optimistic concurrency (a mismatch returns a 409 error), or omit it to apply the update unconditionally. See [Update semantics](https://platform.claude.com/docs/en/managed-agents/agent-setup#update-semantics).
  * Claude Managed Agents session thread event streams now support [event deltas](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#event-deltas). `GET /v1/sessions/{session_id}/threads/{thread_id}/stream` accepts the same `event_deltas[]` query parameter as the session-level stream, so you can preview a subagent's text as the model generates it. A connection previews only the thread it's reading. See [Preview session thread events](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#preview-session-thread-events).


## Capture gaps

This page is a **rolling index**, not a dated article — it is the newest-first log of every Claude Platform change and it grows on every release. `static: false` is set accordingly, so `refresh-research-sources` re-checks it.

Two deliberate omissions:

- **Entries dated before 2026-07-24 were not transcribed.** The full page ran to roughly 10,300 words covering releases back through 2024. The complete capture is preserved verbatim at `research/raw/2026-08-25/claude-platform-release-notes/source.html` and `extracted.md`; only the window above was lifted into this audited page.
- The linked sub-pages (Pricing, model overviews, per-feature docs) were not captured.

> [paraphrased] A cookie-consent banner, twelve "Loading" placeholders, a subscribe link, and the page's navigation chrome were stripped from the head of the extraction.
