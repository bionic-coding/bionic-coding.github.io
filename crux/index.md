---
layout: crux
title: Crux
nav_label: Crux
permalink: /crux/
description: "Project memory and workflows for agentic coding harnesses."
---

Crux gives agentic coding harnesses a shared project memory in a `bionic/` folder inside the repo. Your coding agent can find it, update it, and check it for drift. Decisions, research, the work journal, plans, and the invariants that must stay true all live there. Your coding agent does the bookkeeping. You provide the objectives.

Everything runs locally. There is no server, no account, and no background service. Crux is skills, scripts, role agents, and your repository.

## Crux Manages Knowledge and History

The tree has seven primary areas of knowledge it maintains, plus two derived surfaces that new repos get by default.
This was initially inspired by the [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) by Karpathy
but with a focus on software engineering practices.

| Folder | What lives there | Who writes it |
|---|---|---|
| `bionic/adrs/` | Architecture Decision Records, the "why" behind each decision | You decide; your coding agent writes. Frozen once accepted |
| `bionic/research/` | Articles, papers, URLs, meeting notes, chat exports | You drop sources; your coding agent ingests |
| `bionic/briefs/` | Pre-decision explorations | You write; your coding agent tracks |
| `bionic/journal/` | A day-by-day record of the work | Your coding agent appends; you ask |
| `bionic/promptbooks/` | Plans of prompts, with immutable run snapshots | Co-authored |
| `bionic/invariants/` | Statements of what must stay true, each backed by an executable check | Your coding agent proposes; you ratify |
| `bionic/code/` | Docs extracted from source docstrings | Regenerated; never hand-edited |
| `bionic/observations/` | What the code already does, each fact pinned to a `path:line-range` | You write; you ratify |
| `bionic/arch/` | The current architecture: data model, interface surface, module graph, decision index | Regenerated on demand; never hand-edited |

Two rules hold the tree together. Anything regenerated is never edited by hand, because the next run overwrites it. Anything accepted is never edited afterward, because the record is the point. To change an accepted decision, you write a new one that supersedes it.

## Using Crux in your Project

Once Crux is installed, its skills respond to the same plain phrases in each supported harness. You say what you want, and the harness routes the request to the matching skill.

- **"Propose an ADR for X"** writes a decision record and leaves it for you to accept.
- **"Process inbox"** sorts whatever you dropped into `bionic/inbox/` and files each item where it belongs.
- **"What does X do?"** or **"Why did we choose Y?"** searches the tree and answers with citations.
- **"Start a cycle for X"** assembles a tracked plan that takes a feature from decision to reviewed code.
- **"Audit docs"** checks the whole tree for broken links, stale counts, and missing rows, and fixes the safe ones.

[Using Crux]({{ "/crux/team/" | relative_url }}) covers how to ask for these. The [catalog]({{ "/crux/catalog/" | relative_url }}) has the full list.

## Agents With Guiderails

Crux ships ten role agents that operate the skills. It projects the same roles into each supported harness's native format. Each role has a tool list that bounds it. The librarian answers questions and has no tool that writes. The reviewer reads a diff and has no tool that edits it. The developer builds one unit and has no tool that delegates. For those three the separation is structural, not a matter of instructions. The historian owns every write under `bionic/` by its instructions rather than its tool list, and what a harness enforces depends on the harness.

You address the roles; they run the skills. Two of the ten are where you start: the brainstormer when you are exploring an idea, the commander when a plan is approved and ready to run. The night gardener runs when you ask for a pass or schedule one. The other seven are reached through the first two. [Using Crux]({{ "/crux/team/" | relative_url }}) covers that working relationship: where to start, what each specialist returns, and which judgments stay yours.

This site's own `bionic/` tree is maintained by Crux. [In practice]({{ "/crux/in-practice/" | relative_url }}) shows how.

## Next

Start with [Installation]({{ "/crux/installation/" | relative_url }}) to add Crux to Claude Code, Codex, or OpenCode. Then follow [Setup]({{ "/crux/setup/" | relative_url }}) to initialize it in a project.

**[Crux on GitHub](https://github.com/bionic-coding/crux)**
