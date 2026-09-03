---
title: "Wire the publication-boundary oracle into CI"
slug: wire-the-publication-boundary-oracle-into-ci
type: brief
status: draft                # draft | published
created_at: 2026-08-25
updated_at: 2026-08-25       # bumped on every edit
authors: ["Mark Madsen"]
tags: [ci, deployment, publication-boundary, jekyll, github-actions]
related_adrs: []             # ADR ids that reference this brief (back-populated by audit-docs)
---

# Wire the publication-boundary oracle into CI

> A brief is a short, pre-decision exploration document — usually 1–3 pages. It frames a
> problem, surveys options, and gathers context that an ADR will later compress into a
> single chosen path. Briefs are draft material; humans co-author them. ADRs cite briefs
> via `related_briefs:` and back-populate via `audit-docs`. Delete this stub once you
> start writing.

<body>

<!--
SCAFFOLD ONLY — the body above is yours to write. The reference material for it is the
night gardener's drop, preserved verbatim at:

    bionic/inbox/_dispatched/2026-08-25/gardener-idea-publication-boundary-gate.md

The diagnosis in that drop is already verified, twice over. The V7 inventory oracle
(`find _site -type f ! -path '*/assets/*' ! -path '*/fonts/*'`, recorded in
[[promptbooks/runs/PB-0001-fix-mobile-nav-and-restore-about/run-RUN-002]]) counted 28
files against an expected 27 on `main` at `daeef0d`, and 29 against 29 on the 2026-08-18
pass after the CHANGELOG fix merged. The detector works. Nothing runs it on push.

The four questions the body needs to answer:

1. Which oracle? The run snapshot is explicit that the extension denylist is NOT durable —
   an extensionless root file defeats it. The inventory count is the load-bearing check.
2. Count, or allowlist? A bare count fails on every legitimate new post, which is weekly.
   An allowlist of intended path patterns fails only on genuinely unintended files.
3. Where does it run? `.github/workflows/jekyll.yml` already builds with the production
   overlay; a post-build step there gates the actual deploy.
4. Fail, or warn? The failure mode is "private repo documentation becomes public" — a
   disclosure, not a rendering bug.

Two constraints worth carrying into the body:

- This boundary has failed twice. `ff17186` published three repo docs; the cycle that
  fixed it created a fourth file that then published. The pattern is not carelessness —
  it is a hand-maintained `exclude:` list with no feedback signal.
- The gardener named her own limit here rather than offering to close it: writing a
  workflow file is auto-executing persistence, outside what she is allowed to author.
  This one needs your hand either way.

Once the four questions have answers, this brief becomes an ADR (it touches the deploy
pipeline and sets a policy) — cite it with
`propose-adr --related-briefs BRIEF-wire-the-publication-boundary-oracle-into-ci`.

Related: [[adrs/ADR-0005-serve-a-landing-homepage-and-a-five-item-top-nav]] decision 4 and
its recorded follow-on; the local branch `garden/exclude-changelog-from-build`, which
closed the instance but not the class.
-->
