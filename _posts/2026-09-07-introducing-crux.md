---
layout: post
title: "Introducing crux"
date: 2026-09-07
description: "The toolkit that gives agentic coding harnesses a project memory: decisions, research, plans, and invariants kept in the repo across sessions and models. What it is, why I built it, and how to start."
tags: [crux, agentic-coding]
---

<!--
STATUS: draft, 2026-09-07. Factual paragraphs are drawn from the crux README
and user guide at v3.9.0 and from this site's own bionic/ tree. The three
backticked placeholders are your voice: the lede, the why, and the closer.
The "My AI Kit" post from July already describes crux in four bullets; this
post should not contradict it. Delete this comment before publishing.
-->

<!--
`<lede>` — two or three sentences. The kit post promised crux was "the part
that stays" while the models are swappable. This is the post that pays that
off. Open with the problem you had before it: the same context re-explained
every session, decisions living in chat history, research pasted and lost.
-->

`<lede>`

[crux](https://github.com/bionic-coding/crux) gives agentic coding harnesses a shared project memory in a `bionic/` folder inside the repo. Decisions, research, the work journal, plans, and the invariants that must stay true all live there as plain Markdown. Your coding agent reads the folder at the start of each session, updates it as the work happens, and checks it for drift. You decide and curate. Your coding agent does the bookkeeping.

It runs locally. There is no server, no account, and no background service. It is MIT licensed, and version 3.9.0 shipped today.

## Why I built it

<!--
`<why>` — yours. The manifesto argues the invariants are the asset and the
code is a projection. Say what was missing between that argument and a
working day: where the intent actually went when a session ended, and what
you wanted a tool to hold for you. One to three paragraphs.
-->

`<why>`

## What it keeps

The folder has seven concerns, plus two derived surfaces that a new repo gets by default.

| Folder | What lives there | Who writes it |
|---|---|---|
| `adrs/` | Architecture Decision Records, the "why" behind each decision | You decide; your coding agent writes. Frozen once accepted |
| `research/` | Articles, papers, URLs, meeting notes, chat exports | You drop sources; your coding agent ingests |
| `briefs/` | Pre-decision explorations | You write; your coding agent tracks |
| `journal/` | A day-by-day record of the work | Your coding agent appends |
| `promptbooks/` | Plans of prompts, with immutable run snapshots | Co-authored |
| `invariants/` | What must stay true, each pin backed by an executable check | Your coding agent proposes; you ratify |
| `code/` | Docs extracted from source docstrings | Regenerated |
| `observations/` | What the code already does, pinned to a `path:line-range` | You write; you ratify |
| `arch/` | The current architecture, derived from the sources | Regenerated |

Two rules hold it together. Anything regenerated is never edited by hand. Anything accepted is never edited afterward. To change an accepted decision, you write a new one that supersedes it, and both records keep the link.

## What it feels like to use

Once crux is installed, every skill is triggered by the same plain phrase in each supported harness.

- **"Process inbox."** Drop a PDF, a URL, a half-formed decision, or a stray idea into `bionic/inbox/` and say it. Your coding agent classifies each item and proposes where to file it. After your approval, it files the item. Web sources get dated raw captures and summaries that separate the sources' claims from verified facts.
- **"Propose an ADR for X."** Your coding agent writes the decision record and leaves it as Proposed. You accept it, and from then on the body is frozen.
- **"Start a cycle for X."** Your coding agent assembles a tracked plan that takes a feature from decision to reviewed code. The plan includes a multi-model review of the ADR, an implementation, and an independent code review. Thirteen prompts minimum. You drive it with "advance".
- **"Why did we choose Y?"** Your coding agent searches the folder and answers with citations.
- **"Audit docs."** Your coding agent checks the whole tree for broken links, stale counts, and missing index rows, then fixes the safe ones.

Under the phrases are ten role agents. Crux projects the same roles into each supported harness's native format. Each role has tool permissions that enforce its boundaries. The librarian answers and cannot write. The reviewer reads a diff and cannot edit it. The historian owns every write under `bionic/` and cannot touch source. The separation is structural, not a matter of instructions.

## The council

<!--
Optional. The kit post called this "the LLM-as-judge I keep mentioning". Keep
or cut. Fact: the council puts a decision to Claude, Gemini, and GPT together;
every ADR in a cycle passes through it before you accept; a split verdict is
resolved by a follow-up pass rather than by a human tiebreak. Keys live in
~/.crux/env, outside the repo. Nothing else in crux needs a key.
-->

`<council>`

## This site runs on it

<!--
Facts from this repo's tree as of today: 43 research sources and 6 synthesis
pages behind the weekly column; every figure in a "This Week in AI" story links
back to a dated capture; a night-gardener routine reviews the repo overnight
and leaves a morning note that suggests posts and lesson refreshes; the
column's format is itself a brief. Say which of these has changed how you
write, in one or two paragraphs. The In practice page covers the workflow at
length, so keep this short and link to it.
-->

`<this site>`

The longer version, from defining an objective to splitting a large project across repos, is on the [In practice]({{ "/crux/in-practice/" | relative_url }}) page.

## Getting started

Install crux for your harness, then restart it. Claude Code and Codex use their respective plugin marketplaces. OpenCode currently uses a manual setup.

Then, in a project, say **"init docs"**. That bootstraps the folder, writes the operational schema your coding agent reads in each session, and records the first decision: that this project records decisions. Crux's scripts require Python 3.11 or newer and `uv`.

The [installation]({{ "/crux/installation/" | relative_url }}) and [setup]({{ "/crux/setup/" | relative_url }}) pages have the details, and the [reference]({{ "/crux/reference/" | relative_url }}) has every phrase.

## What it does not do

<!--
`<limits>` — yours, and the paragraph readers will trust most. Candidates:
it does not write your ADRs' reasoning for you; it does not stop you from
ignoring the audit; the council costs API money; OpenCode support is manual
and preview-grade; the public repo is generated on release, so file issues
rather than pull requests.
-->

`<limits>`

<!--
`<closer>` — one paragraph. Where to go: the CRUX pages, the GitHub repo,
issues welcome. End on the augmentation note: the human keeps the decisions,
the machine keeps the books.
-->

`<closer>`
