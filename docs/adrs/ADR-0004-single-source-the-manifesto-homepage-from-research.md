---
id: ADR-0004
title: "Single-source the manifesto homepage from research"
status: Accepted
date: 2026-07-08
proposed_date: 2026-07-07
accepted_date: 2026-07-08
deprecated_date: null
superseded_date: null
supersedes: []
superseded_by: null
deciders: ["Mark Madsen"]
tags: [content, information-architecture, manifesto, single-source, navigation]
related_briefs: []
related_research: [bionic-coding-manifesto]
---

# ADR-0004 — Single-source the manifesto homepage from research

## Context

Bionic Coding is, above all, a manifesto. The site's front door should *be* the argument,
not a link farm that routes to it. The manifesto text also exists as a captured research
source in this repo: the immutable raw capture at
`docs/research/raw/2026-07-07/bionic-coding-manifesto/manifesto.md`, with an audited
rendition at `docs/research/sources/bionic-coding-manifesto.md`
(see [[research/sources/bionic-coding-manifesto]]).

There are two copies of the same words in play — the ingested research capture and the
published page — and they must not drift. This is itself an application of the manifesto's
own principle: **the intent is the durable artifact; the rendered surface is a derived,
regenerable projection.** The captured manifesto is the durable intent; the homepage is a
projection of it and should be treated as regenerable, not independently authored.

## Decision

Serve the manifesto **as the homepage**. `index.markdown` (rendered at `/`) presents "The
Bionic Coding Manifesto"; its body is **generated from the immutable raw capture**
(`docs/research/raw/2026-07-07/bionic-coding-manifesto/manifesto.md`, audited at
`docs/research/sources/bionic-coding-manifesto.md`), keeping the published text faithful
to the ingested source rather than hand-maintained in parallel. The page's `title` and
`description` (tagline) are promoted to the page masthead. Top-nav is controlled via
`_config.yml`'s `header_pages`, which lists **only About** — the manifesto is reached by
the site title, so it does not also appear as a nav item.

## Alternatives Considered

### Option A — A landing/index homepage that links to the manifesto as a separate post
- **Pros:** Conventional blog shape; room for teasers, a post list, and calls to action
  on the front page.
- **Cons:** Puts a routing layer in front of the one thing the site exists to say;
  demotes the manifesto to "a post".
- **Why not:** For a manifesto-first publication the argument *is* the front door. A
  landing page adds a click and dilutes the message.

### Option B — Author the homepage manifesto independently of the research capture
- **Pros:** Simplest to set up — just write the page.
- **Cons:** Creates a second, hand-maintained copy of the manifesto that will drift from
  the captured source; no single source of truth for the canonical text.
- **Why not:** Violates the manifesto's own durable-intent principle. The captured source
  is the intent; the page should be a faithful projection of it, not a fork.

## Consequences

**Positive:**
- The front door *is* the manifesto — the message is unmediated.
- The published text stays faithful to the ingested, audited source; there is a single
  canonical origin for the manifesto's words.
- The site models its own thesis: durable intent (the capture) vs. a regenerable
  projection (the page).

**Negative:**
- The homepage is a **derived artifact**: edits to the manifesto must be made to the
  canonical source and re-projected onto `index.markdown`, not typed directly into the
  page, or the single-source guarantee erodes.
- The raw capture is immutable by the research contract, so a genuine revision of the
  manifesto means a **new dated capture** (re-ingest), then re-projection — not an in-place
  edit of the existing `raw/` file.

**Follow-on work:**
- Document the "edit the source, then re-project" flow so future manifesto changes do not
  drift the page from the capture.
- If the manifesto is revised, re-ingest it as a new research capture and regenerate
  `index.markdown` from the new source.

## References

- [[research/sources/bionic-coding-manifesto]] — the audited manifesto source the homepage is projected from
- [[adrs/ADR-0003-ship-a-custom-presentation-layer-over-minima]] — the masthead/typography that renders the promoted title + tagline
- `index.markdown`, `_config.yml` `header_pages` (in this repo)
