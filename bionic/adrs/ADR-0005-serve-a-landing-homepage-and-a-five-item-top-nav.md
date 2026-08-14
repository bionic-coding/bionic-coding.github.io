---
id: ADR-0005
title: "Serve a landing homepage and a five-item top nav"
status: Accepted
date: 2026-08-14
proposed_date: 2026-08-14
accepted_date: 2026-08-14
deprecated_date: null
superseded_date: null
supersedes: [ADR-0004]
superseded_by: null
deciders: ["Mark Madsen"]
tags: [information-architecture, navigation, homepage, jekyll, publication]
related_briefs: []
related_research: []
---

# ADR-0005 — Serve a landing homepage and a five-item top nav

## Context

[[adrs/ADR-0004-single-source-the-manifesto-homepage-from-research]] is Accepted and
contradicted by HEAD on three points:

1. ADR-0004 decides that `index.md` presents "The Bionic Coding Manifesto". At HEAD
   `index.md` is `layout: home` — a hero, a manifesto pull-quote, the latest three posts,
   and a `featured_lessons` list.
2. ADR-0004 decides that `header_pages` lists only About. At HEAD it lists five pages.
3. ADR-0004 decides that the manifesto is reached by the site title and therefore does not
   appear as a nav item. At HEAD the site title links `/`, `manifesto.md` carries
   `permalink: /manifesto/`, and Manifesto is the first nav item.

HEAD is the option ADR-0004 explicitly rejected as its Option A. The decision is stale, not
merely drifted in its file paths.

**How the drift happened.** Commit `f8a3e82` ("update about", 2026-07-18) renamed
`about.markdown` to `about.md` and added `- tools.md` to `header_pages`, but left the entry
`- about.markdown` in place. `header_pages` resolves by exact source path, so the stale
entry dropped About from the nav without a build error — the silent-failure mode of the
lookup. Commit `ff17186` ("more cleanup", 2026-07-18) fixed the entry
(`- about.markdown` → `- about.md`) and also touched `about.md`, `articles.md`, and
`tools.md`. Commit `a77ecf2` ("scss fixes", 2026-07-18) changed `_layouts/default.html` and
`assets/main.scss` only; it touched neither About nor `_config.yml`.

**Two records need correcting, and neither can be corrected in place.**

- `ff17186` also edited four body lines of ADR-0004 — substituting `index.markdown` for
  `index.md` in the Decision, Consequences, and References sections — after ADR-0004 had
  been Accepted. An Accepted ADR's body is frozen (`bionic/CLAUDE.md` §4), and no `adr` op
  was written to `bionic/log.md`. Reverting the edit would be a second frozen-body edit, so
  the edit is recorded here instead.
- The 2026-07-20 `promptbook` entry in `bionic/log.md` — the one abandoning RUN-001 —
  attributes the About fix to `f8a3e82` and `a77ecf2`. It names the breaking commit as the
  fixing commit, omits `ff17186`, and credits an uninvolved commit. `bionic/log.md` is
  append-only and ordered newest-first, so the correction is recorded here rather than by
  editing that entry.

**Where this ADR comes from.** `PB-0001`/`RUN-002`, a verify-only cycle, verified the nav
fixes: units V1–V6 all PASS, and the round-3 council reached unanimous approve at
confidence 0.973. External review then raised the ADR drift as two MUST-FIX findings —
MX-1 (ADR-0004's decision is stale) and MX-2 (the unlogged post-acceptance body edit) —
and the Prompt 11 fix loop authorized this successor.

**Publication exposure.** The same review raised MX-4: `README.md`, `USER_GUIDE.md`, and
`CLAUDE.md` were published at the site root. The Prompt 11 workstream added all three to
`exclude:` in `_config.yml`, alongside the pre-existing `bionic/` and `_templates/`
entries.

## Decision

Record the site's actual information architecture. Items 1–3 cover the homepage and nav
that the title names. Item 4 records the repo-documentation publication boundary settled in
the same verified workstream; it is recorded here rather than in a separate ADR because
both decisions are carried by the same `_config.yml` and the same review record.

1. **The landing page is `index.md`, with `layout: home`.** It presents a hero, a manifesto
   pull-quote, the latest three posts, and a `featured_lessons` list — not the manifesto
   text.

2. **The top nav is driven by `header_pages` in `_config.yml`**, which lists five pages in
   this order:

   ```yaml
   header_pages:
     - manifesto.md
     - articles.md
     - learn.md
     - tools.md
     - about.md
   ```

   Each entry must match its source file path exactly. A stale or mismatched entry drops
   the page from the nav without a build error — the failure mode that broke the About
   link. A page overrides its nav text with `nav_label`.

3. **The site title links `/`.** `manifesto.md` is served at `/manifesto/` via its
   `permalink` and is reached from the top nav, where it is the first item.

4. **Repo documentation is not published.** `_config.yml`'s `exclude:` list carries
   `bionic/`, `_templates/`, `README.md`, `USER_GUIDE.md`, and `CLAUDE.md`. Repo
   documentation is for the repo, not the site.

This decision supersedes ADR-0004.

## Alternatives Considered

### Option A — Keep ADR-0004 and change the site back to match it
- **Pros:** No ADR churn; the recorded decision and the code agree again; preserves the
  "the argument is the front door" framing ADR-0004 argued for.
- **Cons:** Reverts a shipped, reviewed landing page and a five-item nav that a
  verify-only cycle just certified. Removes the homepage's route into Articles and
  Lessons, which now carry most of the site's content.
- **Why not:** The site grew two content collections after ADR-0004 was written. A
  manifesto-only front door has no place to surface them, and the manifesto is one nav
  click away at `/manifesto/`. The decision is the thing that aged, not the code.

### Option B — Edit ADR-0004's body to match HEAD
- **Pros:** One file changed; the reader finds current facts where they look first.
- **Cons:** An Accepted ADR's body is frozen (`bionic/CLAUDE.md` §4). Editing it destroys
  the record of what was decided in July, and repeats the exact violation `ff17186`
  committed.
- **Why not:** The freeze rule is what makes the ADR set a history rather than a wiki.
  Supersession is the sanctioned way to change an Accepted decision.

### Option C — Leave ADR-0004 Accepted and record nothing
- **Pros:** No work.
- **Cons:** Leaves an Accepted decision that the code contradicts on three points, and
  leaves the `ff17186` body edit and the `log.md` misattribution unrecorded. The next
  reader to consult the ADR set gets three false statements presented as current.
- **Why not:** An Accepted ADR that the code contradicts is worse than no ADR — it is a
  wrong answer with authority.

## Consequences

**Positive:**
- The ADR set states what the site does. A reader consulting ADR-0005 gets the current
  homepage, nav order, and exclusion contract.
- The `header_pages` exact-match failure mode is written down, so the next entry edit has a
  documented hazard to check against.
- The `ff17186` body edit and the `bionic/log.md` commit misattribution are recorded
  without mutating either frozen surface.
- The root `CLAUDE.md` description of how the manifesto is reached was corrected in this
  same workstream and now agrees with this decision: it reads "reached from the top nav".

**Negative:**
- ADR-0004 becomes Superseded. Its body — including the four lines `ff17186` edited after
  acceptance — stays exactly as it is. A reader of ADR-0004 alone still sees the stale
  decision; the `superseded_by` pointer is the only signal, so the supersession transition
  must actually run.
- Until the acceptance gate transitions ADR-0004, this ADR's `supersedes: [ADR-0004]` has
  no matching `superseded_by` on the other end. `audit-docs` flags that asymmetry as
  BROKEN. The finding closes when the transition runs.
- The `exclude:` list is the only thing keeping this repo's documentation off the site.
  Future publishable repo-documentation files may be exposed unless someone adds them to
  that list. Jekyll applies its own default exclusions and processing rules on top, so the
  list is not the whole mechanism — it is the part this repo controls.

**Acceptance criteria.** This ADR moves to Accepted only when all four hold:

1. ADR-0005 transitions Proposed → Accepted, with `accepted_date` set.
2. ADR-0004 transitions Accepted → Superseded, with `superseded_by: ADR-0005` and
   `superseded_date` set. Both ends of the supersession pointer are written.
3. `bionic/log.md` carries the matching `adr` entries: this ADR's acceptance, ADR-0004's
   supersession, and the retroactive record of `ff17186`'s unlogged post-acceptance edit to
   ADR-0004's body.
4. All five `header_pages` entries resolve to titled pages in the rendered nav. RUN-002's
   V1 unit is the standing evidence — 24 HTML pages, an About-link histogram of `{5:24}`,
   and a byte-exact five-link nav block. Re-run it against HEAD at the gate, because
   `_config.yml` was edited after V1 ran.

**Follow-on work** (beyond the acceptance criteria above):
- Add a durable assertion against the `header_pages` silent drop. This ADR documents the
  failure mode; nothing yet enforces it at build time. Recorded, not resolved.
- Add a durable assertion for the publication boundary. The Prompt 11 fix loop prescribes a
  published-file-set check as the regression test for the `exclude:` edit; that check is
  run by hand today. Integrating it into CI is the candidate. Recorded, not resolved.
- Reword the root `CLAUDE.md` kramdown-comment guidance — the rule beginning "Never leave a
  blank line inside an HTML comment." That stated rule did not reproduce under the
  repo's own toolchain when the Prompt 10 docs audit tested it (finding CD-C1). A top-level
  comment with an internal blank line renders fine; the real hazard is an indented or
  paragraph-glued comment leaking as visible text. Deferred as out-of-diff.

## References

- [[adrs/ADR-0004-single-source-the-manifesto-homepage-from-research]] — the decision this
  ADR supersedes
- [[adrs/ADR-0003-ship-a-custom-presentation-layer-over-minima]] — the layouts and
  stylesheet that render the homepage and nav
- [[promptbooks/PB-0001-fix-mobile-nav-and-restore-about]] — the cycle that surfaced the
  drift
- [[promptbooks/runs/PB-0001-fix-mobile-nav-and-restore-about/run-RUN-002]] — the run
  carrying the V1–V6 results, the round-3 council verdict, and findings MX-1 through MX-4
- `index.md`, `_config.yml` (`header_pages`, `exclude`), `manifesto.md`,
  `_layouts/default.html` (in this repo)
- Commits `f8a3e82`, `ff17186`, `a77ecf2` (2026-07-18)
