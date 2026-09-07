---
layout: crux
title: Reference
permalink: /crux/reference/
description: "What to say, which workflow to pick, and the habits that keep the tree honest."
---

## What to say

Every skill is triggered by a phrase. Say it in a sentence, and your coding agent selects the matching skill.

| Say this | Crux will |
|---|---|
| **"Start a cycle for X"** | Assemble a tracked plan that takes X from decision to reviewed code. The main entry point. |
| "Advance" / "next prompt" | Move the active cycle or promptbook forward one prompt |
| "Propose an ADR for X" | Allocate the next ADR number and draft a decision record, status Proposed |
| "Accept ADR-0007" | Flip the status to Accepted. The body is frozen from then on |
| "Supersede ADR-0001 with ADR-0005" | Update both ends of the link |
| "Process inbox" | Classify what you dropped in `bionic/inbox/`, confirm the routing, and file each item |
| "Log work: fixed the X bug" | Append an entry to this month's journal |
| "New promptbook for X" | Scaffold a plan of prompts you co-author, for work that does not need a full cycle |
| "Run promptbook PB-0003" | Start an immutable run snapshot of that book |
| "Build the arch" | Derive the current architecture from the project's sources |
| "Extract code docs" | Regenerate `bionic/code/` from docstrings |
| "Audit docs" | Run the integrity checks and fix the safe drift |
| "What's next" | Scan the tree's process state and write a prioritized list to `bionic/whats_next.md` |
| "What does X do?" / "Why did we choose Y?" | Search the tree and answer with citations |
| "Have the reviewer check the diff" | Dispatch a named agent directly |

## Which workflow for a change

crux has four ways to drive a change, in decreasing rigor. The choice is about the size and kind of the change, not its urgency.

- **Net-new or architectural work** takes a **cycle** ("start a cycle for X"). A decision is recorded as an ADR and reviewed by a multi-model council, implemented, then independently reviewed. Thirteen prompts minimum.
- **A fix to something that exists** takes **iterate** ("iterate on X"). Same council and review, but a verify module that reproduces and root-causes the problem replaces the ADR. If the council finds the fix is architectural after all, it stops and routes you to a cycle.
- **A small, reversible fix** with a footprint you can name up front takes a **patch** ("patch this"). Five phases, one prompt each. You declare the paths it may touch; archival checks the run against them using git.
- **A defect whose failing test you can name now** takes **fix-directly** ("just fix it"). No plan, no council. A failing test first, the smallest green change, one commit, one journal entry.

Every cycle has a three-round escalation built in. If a review loop has not converged after three tries, the run stops and puts the stuck decision in front of you.

## Habits that keep the tree honest

### 1. Audit regularly

Say "audit docs" after every ten or so writes, after a research refresh, and before a release. It catches dangling links, supersession asymmetries, missing index rows, and stale counters, and fixes the safe ones. Derived sections have their own regenerators. Regenerate rather than hand-fix.

### 2. Treat append-only as append-only

- **ADRs.** Once accepted, the body is immutable. Write a new ADR that supersedes it.
- **`bionic/code/` and `bionic/arch/`.** Regenerated on every run. If a docstring is wrong, fix the source.
- **`bionic/research/raw/`.** Every capture lives there forever, dated. It is the audit chain when a summary is challenged.
- **`bionic/journal/` and `bionic/log.md`.** Chronological. Do not reorder or edit past entries.
- **ADR and promptbook numbers.** Never reused.

### 3. Capture by dropping, not by filing

Drop a file, a URL, a stray idea, or a half-formed decision into `bionic/inbox/` and say "process inbox". The skill decides where it goes and asks before it files anything it is unsure about. Later, "refresh sources" re-fetches the URLs and flags the summary pages that upstream changes affect.

### 4. Promptbooks for anything you would paste twice

A sequence you would otherwise give your coding agent prompt by prompt belongs in a promptbook. The plan is mutable and co-authored. Each run is an immutable snapshot. To change the plan mid-run, abandon the run and author a successor book that names its predecessor.

### 5. Read the schema before deep work

`bionic/CLAUDE.md` is the operational schema that crux's skills and role agents read. The filename remains for compatibility, but its rules apply in every supported harness. When you wonder whether a coding agent should write somewhere, that file has the answer.

### 6. Ask; do not hand-edit

When you spot a stale page, a contradiction, or a broken link, ask crux to fix it. Hand edits to managed files slip past audits and desynchronize the counters and indexes that the whole tree relies on. Your sense that something looks off is the intended trigger.

## When something looks wrong

| Symptom | Try this |
|---|---|
| "Where did crux put X?" | Read `bionic/index.md`, then the concern's own index |
| `bionic/code/` is stale | "Extract code docs" regenerates it fully |
| An accepted ADR is wrong | Write a new ADR that supersedes it |
| A research page contradicts itself | "Refresh synthesis" walks you through the reconciliation |
| You lost track of a plan | `bionic/promptbooks/index.md` shows the current run and its progress |
| A script exits 2 | That is your environment, not your docs. Read the remediation message; it names the missing parser, `uv`, or PyYAML |
| The whole tree feels broken | "Audit docs" |

## Next

[In practice]({{ "/crux/in-practice/" | relative_url }}): how this site is built with it.
