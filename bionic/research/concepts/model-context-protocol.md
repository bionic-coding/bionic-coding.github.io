---
title: "Model Context Protocol — what it is, and what the 2026-07-28 revision changed"
slug: model-context-protocol
type: concepts
tags: [mcp, protocol, tools, resources, prompts, deprecation, transports]
sources: [mcp-spec-2026-07-28-changelog]
last_reviewed: 2026-08-25
---

# Model Context Protocol

Backs [[_lessons/mcp]]. The lesson teaches MCP's three primitives in plain language; this page holds the protocol facts behind it and tracks revision-to-revision change.

## The three primitives the lesson teaches

**Tools**, **Resources**, and **Prompts**. All three remain core in the `2026-07-28` revision. Nothing in that revision requires a lesson edit — see the lesson-impact check below.

## Revision `2026-07-28` — the largest revision to date

Source: [[research/sources/mcp-spec-2026-07-28-changelog]] (primary, read in full 2026-08-25). Previous revision: `2025-11-25`.

**The headline: MCP became stateless.** Four changes carry that:

1. **Protocol-level sessions removed**, along with the `Mcp-Session-Id` header. List endpoints no longer vary per connection. A server that needs cross-call state now mints an explicit handle and passes it as an ordinary tool argument.
2. **The `initialize` / `notifications/initialized` handshake removed.** Every request carries its own protocol version and client capabilities in `_meta`.
3. **`server/discover` added**, and servers **MUST** implement it — the replacement advertisement path for versions, capabilities, and identity.
4. **SSE stream resumability removed** (`Last-Event-ID` and SSE event IDs). A broken stream loses the in-flight request; the client re-issues with a new request ID.

**Also removed or moved:** `ping`, `logging/setLevel`, `notifications/roots/list_changed`; the HTTP GET endpoint and `resources/subscribe`/`unsubscribe` (replaced by a single `subscriptions/listen` stream); experimental tasks moved out of core into the `io.modelcontextprotocol/tasks` extension.

**New patterns:** Multi Round-Trip Requests (MRTR) replaces server-initiated requests — a server returns `resultType: "input_required"` with `inputRequests`, and the client retries the original request carrying `inputResponses`. Every result now carries a required `resultType`.

## Deprecated, on a twelve-month clock

- **Roots, Sampling, and Logging** (SEP-2577). Suggested migrations: tool parameters / resource URIs / server config instead of Roots; direct LLM provider APIs instead of Sampling; `stderr` or OpenTelemetry instead of Logging.
- **HTTP+SSE transport** reclassified Deprecated (soft-deprecated since `2025-03-26`).
- **OAuth 2.0 Dynamic Client Registration**, in favour of Client ID Metadata Documents.

**The governance change is what makes the deprecations survivable.** The revision adopts a feature lifecycle policy defining Active / Deprecated / Removed states with a **minimum twelve-month deprecation window** and a registry of deprecated features. Deprecated features remain fully functional inside that window.

## Lesson-impact check (2026-08-25): no edit needed

[[_lessons/mcp]] teaches Tools, Resources, and Prompts. All three are untouched. The lesson never mentions sessions, transports, Roots, Sampling, or Logging, so its plain-language model survives this revision intact, and its `## More info` link points at the evergreen spec site rather than a pinned revision. `updated: 2026-07-17` can stand.

## The column angle

> **[claimed-vs-verified] The popular misread is "MCP had a breaking change, my servers are broken."**
> The changelog says otherwise. The twelve-month deprecation window keeps Deprecated features working, and `server/discover` exists specifically as a backward-compatibility probe. **The honest asterisk is that the transport changed hard while the primitives did not** — anyone who wrote against `Mcp-Session-Id`, the `initialize` handshake, or SSE resumability has real work to do; anyone who wrote Tools, Resources, and Prompts does not.

## Unverified — ecosystem response

Both of these arrived as search snippets in the night gardener's drop, preserved at `research/raw/2026-08-25/mcp-spec-2026-07-28-changelog/gardener-note.md`, and **neither has been checked against a primary**. Do not publish either without a read:

- Google described a stateless MCP redesign on 2026-08-05 (claimed; a Google Developers Blog post).
- Microsoft released an MCP C# SDK v2.0 with a stateless HTTP model around 2026-08-12, said to keep backward compatibility (claimed).

## Not captured

The linked sub-pages — the feature lifecycle policy, the deprecated-features registry, the MRTR pattern page, and the Streamable HTTP transport page — were not captured. This wiki holds the changelog only.
