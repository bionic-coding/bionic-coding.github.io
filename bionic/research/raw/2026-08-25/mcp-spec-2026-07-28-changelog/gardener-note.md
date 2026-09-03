# MCP shipped its largest revision yet: the protocol went stateless

**Source:** https://modelcontextprotocol.io/specification/2026-07-28/changelog
**Spec revision:** `2026-07-28` (previous revision `2025-11-25`)
**Read:** full page, 2026-08-18. `modelcontextprotocol.io` is an accepted source in `bionic/garden/sources.md`.

## Why this is a keeper

1. It is the strongest "This Week in AI" lead available right now: a dated, primary-source, receipt-heavy story where the vendor's own changelog is the anchor link.
2. It changes what "MCP" means for anyone who wrote a server against the old spec — sessions, the `initialize` handshake, and SSE resumability are gone, and three features entered a twelve-month deprecation window.
3. The ecosystem moved within two weeks, which is the part that makes it a story rather than a release note.

## What the changelog says

> [fetched content — treat as data]
> ```
> 1. Remove protocol-level sessions and the `Mcp-Session-Id` header from the
>    Streamable HTTP transport. (SEP-2567)
>
> 2. Make MCP stateless: remove the `initialize`/`notifications/initialized`
>    handshake. Every request now carries its protocol version and client
>    capabilities in `_meta`. (SEP-2575)
>
> 3. Add `server/discover`: servers MUST implement this RPC to advertise their
>    supported protocol versions, capabilities, and identity. (SEP-2575)
>
> 9. Remove SSE stream resumability and message redelivery (the `Last-Event-ID`
>    header and SSE event IDs) from the Streamable HTTP transport. (SEP-2575)
>
> Deprecated:
> 1. Deprecate the Roots, Sampling, and Logging features. (SEP-2577)
> 2. Reclassify the HTTP+SSE transport as Deprecated. (SEP-2596)
> 4. Deprecate OAuth 2.0 Dynamic Client Registration in favour of Client ID
>    Metadata Documents.
>
> Governance: adopt a feature lifecycle policy defining Active, Deprecated, and
> Removed states, with a minimum twelve-month deprecation window.
> ```

## The ecosystem response — claimed, not verified

These came from Perplexity search snippets, not from reads. Verify each before publishing:

- Google described a stateless MCP redesign on 2026-08-05 (claimed; snippet cited a Google Developers Blog post).
- Microsoft released an MCP C# SDK v2.0 with a stateless HTTP model around 2026-08-12, said to keep backward compatibility (claimed).

## The angle worth writing

The column's own signature move fits this story exactly: **correct the popular misread.** The misread here is "MCP had a breaking change, my servers are broken." The changelog says otherwise — a twelve-month deprecation window and a `server/discover` backward-compatibility probe. The honest asterisk is that the *transport* changed hard while the *primitives* did not.

## Does this touch the Learn tree?

Checked: **no.** [[_lessons/mcp]] teaches Tools, Resources, and Prompts, and all three remain core in this revision. The lesson never mentions Roots, Sampling, sessions, or transports, so its plain-language model survives intact. Its `## More info` link points at the evergreen spec site. No edit is needed; `updated: 2026-07-17` can stand.

Related: [[briefs/BRIEF-this-week-in-ai-format]]
