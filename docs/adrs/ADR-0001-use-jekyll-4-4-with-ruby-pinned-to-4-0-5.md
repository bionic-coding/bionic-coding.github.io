---
id: ADR-0001
title: "Use Jekyll 4.4 with Ruby pinned to 4.0.5"
status: Proposed
date: 2026-07-07
proposed_date: 2026-07-07
accepted_date: null
deprecated_date: null
superseded_date: null
supersedes: []
superseded_by: null
deciders: ["Mark Madsen"]
tags: [static-site, jekyll, ruby, tooling, build]
related_briefs: []
related_research: []
---

# ADR-0001 — Use Jekyll 4.4 with Ruby pinned to 4.0.5

## Context

The Bionic Coding blog is a text-first publication: a manifesto, essays, and an About
page. It needs a static-site generator that is low-friction for prose, has a mature
templating and content pipeline, and deploys cleanly to GitHub Pages (the repo is
`bionic-coding/bionic-coding.github.io`, served at the custom domain `bionic-coding.com`).

Jekyll is the native generator behind GitHub Pages and the default for a `github.io`
repo, so it is the path of least resistance for a Markdown-driven site. We adopt the
current line — **Jekyll 4.4** (`gem "jekyll", "~> 4.4.1"`) — with the **Minima** theme
pulled in as a base gem (`gem "minima", "~> 2.5"`) to bootstrap layouts and styles
before we override them.

Jekyll 4.4's dependency chain forces a Ruby-version decision. Transitive native gems —
notably `ffi 1.17` — require **Ruby ≥ 3.0**. The development machine's default Ruby is
**2.7.6**, which is end-of-life and fails `bundle install` against this dependency graph.
The build therefore cannot rely on the ambient system Ruby; the required interpreter
version has to be captured in the repo so every contributor and every CI runner resolves
the same toolchain.

## Decision

Build the blog with **Jekyll 4.4** on top of the **Minima 2.5** base gem, and pin the
Ruby interpreter to **4.0.5** via a repo-root `.ruby-version` file. The `Gemfile` is the
single source of truth for the Jekyll toolchain (`bundle exec jekyll build` / `serve`);
contributors run under the pinned Ruby, not the system default.

## Alternatives Considered

### Option A — A JavaScript static-site generator (Astro / Eleventy / Hugo)
- **Pros:** Modern authoring ergonomics; Astro/Eleventy have strong component stories;
  Hugo is a single fast Go binary with no interpreter-version problem at all.
- **Cons:** None is the native GitHub Pages generator, so deployment needs custom CI
  regardless; introduces a Node (or Go) toolchain the project otherwise does not need;
  more machinery than a text-first manifesto site warrants.
- **Why not:** The site is prose, not an application. Jekyll's Markdown-first pipeline
  and first-class GitHub Pages lineage are a better fit than an SSG chosen for
  component-heavy or JS-driven sites. (Hugo would sidestep the Ruby pin, but at the cost
  of leaving the ecosystem GitHub Pages is built around.)

### Option B — Jekyll on the ambient system Ruby (2.7.6)
- **Pros:** Zero version-management setup; uses what is already installed.
- **Cons:** Ruby 2.7.6 is EOL and cannot satisfy Jekyll 4.4's dependency chain —
  `bundle install` fails on `ffi 1.17` (needs Ruby ≥ 3.0). Working around it would mean
  downgrading Jekyll and giving up the 4.x line.
- **Why not:** Demonstrably broken — the install fails. Pinning a modern Ruby is the
  minimal fix that keeps Jekyll 4.4.

## Consequences

**Positive:**
- Markdown-first authoring with a mature, well-documented generator.
- Native alignment with GitHub Pages / the `github.io` convention.
- A reproducible toolchain: `.ruby-version` + `Gemfile`/`Gemfile.lock` pin both the
  interpreter and the gem set, so local and CI builds match.

**Negative:**
- Contributors must have **Ruby ≥ 3.0** available (the pinned 4.0.5 via a version manager
  such as `rbenv`/`asdf`/`chruby`); the system Ruby 2.7.6 will not build the site.
- Carries a Ruby toolchain purely to render a static text site — heavier than a single
  static binary would be.

**Follow-on work:**
- The GitHub Pages *legacy* branch build ships its own Jekyll 3.x and ignores this
  `Gemfile`, so it cannot honor this decision — the site must be built by CI that uses
  the project's own Gemfile. That is decided separately in
  [[adrs/ADR-0002-deploy-to-github-pages-via-github-actions]].
- Onboarding docs (README/USER_GUIDE) must state the Ruby ≥ 3.0 / `.ruby-version`
  requirement.

## References

- [[adrs/ADR-0002-deploy-to-github-pages-via-github-actions]] — the CI build that honors this Gemfile
- Jekyll — https://jekyllrb.com/
- Minima theme — https://github.com/jekyll/minima
- `ffi` gem (requires Ruby ≥ 3.0 as of 1.17) — https://github.com/ffi/ffi
