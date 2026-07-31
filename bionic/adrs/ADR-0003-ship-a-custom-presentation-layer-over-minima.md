---
id: ADR-0003
title: "Ship a custom presentation layer over Minima"
status: Accepted
date: 2026-07-08
proposed_date: 2026-07-07
accepted_date: 2026-07-08
deprecated_date: null
superseded_date: null
supersedes: []
superseded_by: null
deciders: ["Mark Madsen"]
tags: [design, presentation, sass, css, typography, theming]
related_briefs: []
related_research: [bionic-coding-manifesto]
---

# ADR-0003 — Ship a custom presentation layer over Minima

## Context

The site pulls in the **Minima** theme as a base gem (see
[[adrs/ADR-0001-use-jekyll-4-4-with-ruby-pinned-to-4-0-5]]), but Minima's stock
look-and-feel is a generic blog aesthetic that does not carry the editorial identity this
publication wants. The Bionic Coding manifesto turns on a specific duality — **durable
intent vs. disposable code** (see [[research/sources/bionic-coding-manifesto]]) — and the
site's visual identity is meant to embody it rather than read as a default template.

Minima also carries baggage we do not want: its stylesheet emits Sass **deprecation
warnings** under modern Dart Sass, and inheriting its CSS would mean fighting styles we
did not author.

## Decision

Ship our **own presentation layer** and fully override Minima:

- Custom `_layouts/` — `default.html`, `page.html`, `post.html` — replacing Minima's
  templates.
- A hand-written `assets/main.scss` that **fully overrides** Minima's stylesheet, so none
  of Minima's CSS (and none of its Sass deprecation warnings) is used.
- A deliberate editorial design system: a warm **"paper"** surface; **Fraunces** display
  serif for prose and headings paired with **JetBrains Mono** for the masthead, taglines,
  and labels; a single **rust** accent; a constrained reading measure; styled section
  dividers; and **automatic dark mode** via `prefers-color-scheme`.

The serif/mono pairing is intentional and thematic: the humanist serif carries the
*durable intent* (the prose, the argument) and the monospace carries the machine register
(*disposable code*), so the typography itself echoes the manifesto's central duality.

The stylesheet uses **Dart-Sass / modern-CSS-only** functions — `clamp()` for fluid type
scales and `color-mix(in srgb, …)` for accent tints. These are not compatible with the
old libsass engine, which is exactly why the site must be built with modern Jekyll under
GitHub Actions (see [[adrs/ADR-0002-deploy-to-github-pages-via-github-actions]]).

## Alternatives Considered

### Option A — Use Minima as-is (or lightly customized via theme overrides)
- **Pros:** Zero design work; the supported default; least code to maintain.
- **Cons:** Generic blog appearance that does not express the manifesto's identity;
  inherits Minima's Sass deprecation warnings; customizing on top means fighting styles we
  did not write.
- **Why not:** The publication's whole point is a distinct editorial voice; a stock theme
  undercuts it.

### Option B — Adopt a different off-the-shelf Jekyll theme
- **Pros:** A more opinionated starting look than Minima without authoring CSS.
- **Cons:** Still someone else's design language; still inherited CSS and its constraints;
  swapping themes later is disruptive.
- **Why not:** No third-party theme encodes the intent/duality identity; owning a thin,
  purpose-built layer is cleaner than bending a foreign one.

## Consequences

**Positive:**
- A distinctive editorial identity that visually encodes the manifesto's thesis.
- No inherited Minima CSS and no Minima Sass deprecation warnings.
- Full control of typography, color, measure, dividers, and dark mode.

**Negative:**
- We own the CSS: presentation is now our maintenance surface, not the theme's.
- **Hard coupling to the build:** the modern CSS functions (`clamp()`,
  `color-mix()`) require the Dart-Sass / Jekyll-4 build. The presentation layer **must
  stay Actions-built** — the legacy libsass pipeline would silently break styling (the
  exact failure that motivated [[adrs/ADR-0002-deploy-to-github-pages-via-github-actions]]).

**Follow-on work:**
- Because Minima is now fully overridden, the base theme and the web fonts (Fraunces /
  JetBrains Mono) are **swappable** later without touching content — a future redesign is
  a presentation-layer change, not a content migration.
- Any change to `assets/main.scss` must be validated against the Actions build, not just a
  local render.

## References

- [[adrs/ADR-0001-use-jekyll-4-4-with-ruby-pinned-to-4-0-5]] — the Minima base gem this layer overrides
- [[adrs/ADR-0002-deploy-to-github-pages-via-github-actions]] — the modern build the custom Sass requires
- [[research/sources/bionic-coding-manifesto]] — the durable-intent / disposable-code duality the typography echoes
- Fraunces — https://fonts.google.com/specimen/Fraunces
- JetBrains Mono — https://www.jetbrains.com/lp/mono/
