---
title: "Teaching regular people AI: content plan for Articles and the Learn section"
slug: teaching-regular-people-ai-content-plan
type: brief
status: published            # draft | published
created_at: 2026-07-11
updated_at: 2026-07-11       # bumped on every edit
authors: ["Mark Madsen"]
tags: [content, ai-literacy, editorial, articles, learn]
related_adrs: []             # ADR ids that reference this brief (back-populated by audit-docs)
---

# Teaching regular people AI: content plan for Articles and the Learn section

Bionic Coding is adding two content tracks for people who want to understand and use AI but don't build models for a living:

- **Articles** (`/articles/`) — timely posts on new developments.
- **Learn** (`/learn/`) — an evergreen AI-literacy section of lessons.

This brief records how we produce and keep that content honest. Draft — edit freely.

## Who it's for
Curious non-experts who are willing to try things. Not researchers, not total non-users. _(Open: pin the reading level and how much prior exposure we assume.)_

## How we write: scaffold, then author
- Claude scaffolds structure only — front matter, section outlines, TODO prompts. Mark writes the sentences.
- The goal is writing that does not read as machine-generated. Avoid the tells (e.g. "load bearing," "delve," tidy rule-of-three cadences, reflexive em-dashes).
- The prose is the human part; the scaffold is the disposable part. Same idea as the manifesto.

## Sourcing: facts and references, all through crux
- Every claim gets a fact and a reference. No unsourced assertions.
- **All research runs through crux:** `ingest-research` captures the source; the page cites its `docs/research/sources/<slug>`.
- Each article and lesson has a `## References` section. Citations get added in the research pass, after the scaffold.

## Freshness
- **Last-reviewed dates.** Every lesson carries an `updated:` date, shown as "Last reviewed …". Highest-priority convention — bump it on every review.
- **Weekly review.** Once a week, comb through recent articles and every lesson, check claims against current reality, fix what's stale, and bump `updated:`. _(To settle: the checklist, who runs it, how it's triggered.)_

## Ideation
- New post ideas come from the crux night gardener (`tend-garden`) — it watches what shipped and what's moving, and proposes topics.

## Launch scope
- **Lessons: 7–9.** Have 8 scaffolded: Glossary, Markdown, Prompting & Evals, Agents & Skills, Agentic Harnesses, Sharing Agents & Skills, Wikis/Knowledge/RAG, Samples.
- **Posts: 5–10.** Have 4 scaffolded: GPT-5.6 Sol vs Opus/Fable; Fable Relaunched; The New Codex; The MCP Moment. Need 1–6 more.

## Open questions
- Reading level / assumed background.
- Voice: keep the manifesto register, or go plainer for teaching?
- Keep the name "agentic harnesses"?
- Which additional posts for launch.
- Weekly review mechanics (checklist / owner / trigger); night-gardener cadence and where its suggestions land.
- Graduate this brief to an ADR + a standing runbook once settled?
