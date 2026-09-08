---
layout: post
title: "Introducing Crux"
date: 2026-09-07
description: "Meet Crux: an open-source project memory for agentic coding harnesses, built around durable objectives, decisions, research, plans, and invariants."
tags: [crux, agentic-coding]
---

[Crux](https://github.com/bionic-coding/crux) gives agentic coding harnesses a shared project memory in a `bionic/` folder inside the repo. Decisions, research, the work journal, plans, and the invariants that must stay true all live there as plain Markdown. Your coding agent reads the folder at the start of each session, updates it as the work happens, and checks it for drift. You decide and curate. Your coding agent does the bookkeeping.

It runs locally. There is no server, no account, and no background service. It is MIT licensed, and version 3.9.0 shipped today.

## Why I built it

The further we get down the road we are on, the less that code will matter.
Instead we will care about intent, objectives, and invariants.

I'm sure Crux isn't the final state. But it's a good step towards a more unified, agentic coding experience.

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

## Getting started

Install crux for your harness, then restart it. Claude Code and Codex use their respective plugin marketplaces. OpenCode currently uses a manual setup.

Then, in a project, say **"init docs"**. That bootstraps the folder, writes the operational schema your coding agent reads in each session, and records the first decision: that this project records decisions. Crux's scripts require Python 3.11 or newer and `uv`.

The [installation]({{ "/crux/installation/" | relative_url }}) and [setup]({{ "/crux/setup/" | relative_url }}) pages have the details, and the [reference]({{ "/crux/reference/" | relative_url }}) has every phrase.
