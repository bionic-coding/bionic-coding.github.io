---
id: ADR-0002
title: "Deploy to GitHub Pages via GitHub Actions"
status: Proposed
date: 2026-07-07
proposed_date: 2026-07-07
accepted_date: null
deprecated_date: null
superseded_date: null
supersedes: []
superseded_by: null
deciders: ["Mark Madsen"]
tags: [deployment, github-pages, github-actions, ci, build]
related_briefs: []
related_research: []
---

# ADR-0002 — Deploy to GitHub Pages via GitHub Actions

## Context

The blog is hosted on GitHub Pages from the repo `bionic-coding/bionic-coding.github.io`,
served at the custom domain `bionic-coding.com` (a root `CNAME` file carries the domain).
GitHub Pages offers two publishing pipelines:

1. **Legacy "Deploy from a branch":** GitHub builds the site itself, using a *pinned*
   `github-pages` gem — currently **Jekyll 3.10** — in `--safe` mode, and **ignores the
   repo's own `Gemfile`**.
2. **GitHub Actions:** the repo runs its own workflow, builds with whatever toolchain it
   declares, and publishes the resulting artifact.

We build with **Jekyll 4.4** and pin Ruby to 4.0.5 (see
[[adrs/ADR-0001-use-jekyll-4-4-with-ruby-pinned-to-4-0-5]]). The legacy pipeline is
fundamentally incompatible with that choice: it runs Jekyll 3.10, not 4.4, and the older
Jekyll bundles the **libsass** Sass engine. Our hand-written stylesheet
(`assets/main.scss`, see [[adrs/ADR-0003-ship-a-custom-presentation-layer-over-minima]])
uses **Dart-Sass / modern-CSS-only** features — `clamp()` and
`color-mix(in srgb, …)` — that libsass cannot compile. Under the legacy build the CSS
fails and the site renders **unstyled**. The modern Sass and modern CSS are exactly what
force a modern-Jekyll build, and the legacy pipeline cannot provide one.

## Decision

Publish via **GitHub Actions**. A `.github/workflows/jekyll.yml` workflow builds the site
with the project's own `Gemfile` (Jekyll 4.4, Ruby from `.ruby-version`) and deploys the
artifact using the official Pages actions (`actions/configure-pages`,
`actions/upload-pages-artifact`, `actions/deploy-pages`). The Pages "Source" setting is
switched from "Deploy from a branch" to **GitHub Actions**. To let the Linux CI runners
resolve native gems, `Gemfile.lock` gained Linux platform tuples (e.g.
`x86_64-linux-gnu`) alongside the local `arm64-darwin`.

## Alternatives Considered

### Option A — Keep the legacy "Deploy from a branch" build, downgrade to the `github-pages` gem
- **Pros:** Zero CI to maintain; GitHub builds and serves automatically; the officially
  "supported" default path.
- **Cons:** Pins Jekyll 3.x and libsass. That loses Jekyll 4 and, critically, cannot
  compile the custom Dart-Sass stylesheet — `clamp()` / `color-mix()` break and the site
  ships unstyled. It also silently ignores our `Gemfile`, so local and production builds
  diverge.
- **Why not:** It produced the actual bug this ADR fixes (an unstyled page). Rejected —
  it forfeits both Jekyll 4 and the custom Sass.

### Option B — Build locally and commit the rendered `_site/` to a publishing branch
- **Pros:** Full control of the toolchain; no dependence on GitHub's build.
- **Cons:** Manual, error-prone, and pollutes history with generated output; every
  contributor needs the full local toolchain to publish; easy to forget to rebuild.
- **Why not:** GitHub Actions gives the same toolchain control with none of the manual
  build-and-commit ritual, and keeps generated output out of source history.

## Consequences

**Positive:**
- The published site is built with the **same Jekyll 4.4 toolchain** as local
  development — production matches what contributors see with `bundle exec jekyll serve`.
- The custom Dart-Sass stylesheet compiles correctly; the site is styled in production.
- Deploys are automated on push to `main` (plus manual `workflow_dispatch`).

**Negative:**
- A CI workflow is now a maintained artifact (action version pins, Ruby setup) rather
  than relying on GitHub's turnkey build.
- **The presentation layer is coupled to the Actions build:** the modern CSS in
  `assets/main.scss` must stay Actions-built. Reverting Pages to the legacy branch build
  would silently re-break styling. Any future change that would move off Actions must
  re-check the Sass/CSS-engine compatibility this ADR resolved.

**Follow-on work:**
- Keep `Gemfile.lock`'s platform list covering the CI runner architecture(s); a runner
  whose platform tuple is missing will fail `bundle install`.
- The root `CNAME` (`bionic-coding.com`) must survive the deploy; the workflow uploads the
  built artifact, so `CNAME` remains part of the site source.

## References

- [[adrs/ADR-0001-use-jekyll-4-4-with-ruby-pinned-to-4-0-5]] — the Jekyll 4.4 / Ruby pin this build honors
- [[adrs/ADR-0003-ship-a-custom-presentation-layer-over-minima]] — the modern-CSS stylesheet that forces a modern build
- GitHub Pages — building with a custom GitHub Actions workflow — https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- `.github/workflows/jekyll.yml` (in this repo)
