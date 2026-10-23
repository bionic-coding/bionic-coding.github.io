---
layout: crux
title: Reference
permalink: /crux/reference/
description: "What to say, which cycle to pick, and good habits."
---

## What to say

Each skill declares the phrases it answers to. Say one in a sentence and your coding agent routes the request to the matching skill. These are trigger phrases, not commands. No phrase selects a skill deterministically, and none of them is a slash command.

| Ask for | Crux will |
|---|---|
| **"Start a cycle for X"** | Open one tracked cycle for X, with the type that fits the change. The main entry point |
| "Quick fix" / "refactor this" / "simplify X" / "release cycle" | Start a cycle of that type |
| "Cycle status" | Show phases, tasks, passes, evidence, and approval waits, without changing anything |
| "Resume the cycle" | Continue the same paused cycle |
| "Add to the queue" / "run the next item" | Queue work for later, then authorize the commander to start queued cycles |
| "Propose an ADR for X" | Allocate the next ADR number and draft a decision record, status Proposed |
| "Accept ADR-0007" | Flip the status to Accepted once its approvals are in. The body is frozen from then on |
| "Supersede ADR-0001 with ADR-0005" | Update both ends of the link |
| "Migrate ADRs" | Have the architect assess old decisions, clause by clause, against current objectives |
| "Process inbox" | Classify what you dropped in `bionic/inbox/`, confirm the routing, and file each item |
| "Log work: fixed the X bug" | Append an entry to this month's journal |
| "Build the arch" | Derive the current architecture from the project's sources |
| "Extract code docs" | Regenerate `bionic/code/` from docstrings |
| "Audit docs" | Run the integrity checks and fix the safe drift |
| "What's next" | Scan the tree's process state and write a prioritized list to `bionic/whats_next.md` |
| "What does X do?" / "Why did we choose Y?" | Search the tree and answer with citations |
| "Install micro-crux" | Add the standalone guide for agents without the plugin |

You can also name a role directly; most of them declare their own trigger phrases. Ask for the outcome instead and your coding agent supplies the role's context. It also commissions review from whoever assigned the work, never from the author. [Using Crux]({{ "/crux/team/" | relative_url }}) covers all ten roles.

## Which cycle for a change

Every change runs as one **cycle**: a single record with a visible plan, tasks, the current phase, a pass count, evidence, and history. The type sets the phases and how many passes the cycle gets. Pick the type by the size and kind of the change, not its urgency.

| Type | Use it for | Phases | Pass limit |
|---|---|---|---:|
| dev | Major changes | Plan → Build → Test → Review → Reflect | 7 |
| iterate | Minor changes | Plan → Build → Test → Review → Reflect | 2 |
| refactor | Better structure or efficiency, same behavior | Plan → Build → Test → Review → Reflect | 7 |
| simplify | Less complexity, same behavior | Plan → Build → Test → Review → Reflect | 3 |
| quick-fix | A small, bounded correction | Build → Test → Review → Reflect | 1 |
| release | Publishing one release target | Release | none |

There is no prompt minimum. A quick fix records its scope and success criteria without a Plan phase, and its Test, Review, and Reflect stay short. A functional change needs iterate or dev; refactor and simplify must leave behavior unchanged and say how that is verified.

**Simplify** starts with the architect assessing a feature or recent changes and listing removal proposals. You approve the proposals to build. A council can select them only for a cycle started from the queue, within that item's scope. In Test, the cycle records, for production code, tests, instructions, and execution steps, whether complexity went down, stayed the same, or went up. Any increase stops the cycle, and a cycle with no decrease is refused.

### Passes, returns, and pauses

- **A pass** is one trip through the phases. The limit includes the first attempt.
- **A return.** A blocking Test or Review finding sends the cycle back to Plan, or to Build for a quick fix. The return records what improved, what is still open, and why another pass is justified.
- **A pause.** The cycle pauses when progress stalls, the limit runs out, the scope changes, a decision needs you, or new evidence contradicts the premise. It reports the blocker, the evidence, and a recommended next step. It does not retry just because passes remain.
- **More passes** need your approval, recorded on the cycle. Approval never turns off the stall rule.
- **Changing type** keeps the cycle's identity, history, and pass count, so it cannot reset an exhausted limit.
- **Resume, don't restart.** "Resume the cycle" continues the same record.
- **Closed is closed.** A completed or abandoned cycle closes with a reflection. Follow-up work starts a new cycle.

Before a cycle completes, its changes are committed and the commits are recorded. Only your own request leaves work uncommitted, and the record quotes it.

### Release cycles

A release cycle has one phase, Release, and no pass limit. Its type carries a fixed step list, so nobody writes a release plan.

- **Beta:** prep, prepare, verify, beta-and-smoke, tag, record.
- **Official:** live-check-and-go-ahead, official, record.

Publication happens only under your own words, quoted, for the exact artifact. A failed step stops the release; after the fix lands, the step and every later one reopen. A defect in tagged bytes ends that version, and the fix ships as a new version in a new beta cycle. A withheld go-ahead pauses the official cycle; it never abandons it.

### The queue

Say "add to the queue" to capture and order work in `bionic/queue/cycles.yaml`. Say "run the next item", "run the next N items", or "run the queue" to authorize the commander to start queued cycles one after another. Your message is quoted as the authorization.

Authorization starts cycles and nothing else. It never pushes, publishes, or releases, never extends a pass limit, and never approves an IDR or ADR. Each queued cycle keeps its own type, limit, and stops. An empty queue, an exhausted authorization, or a blocked item ends the run with a report.

> [!NOTE]
> Older names still route. "Dev cycle", "iterate", "patch cycle", "fix directly", and "author a promptbook" now start a
> cycle. They are not separate workflows. Existing promptbooks stay readable, and an in-progress run can finish under
> its original rules. No new promptbook is written.

## Decisions: ADRs and IDRs

Crux keeps two kinds of decision record.

- **An ADR** records an enduring constraint the project must keep. Its rules govern later work.
- **An IDR** (Implementation Decision Record) records how to build something within those constraints. It keeps the reasoning and the council evidence, and it governs nothing.

Every dev cycle needs a council-approved IDR before dependent implementation starts. Simplify needs an approved IDR that selects its proposals. The other types need one only for a material choice with alternatives worth keeping. Approval binds the exact revision the council reviewed; any change needs a new revision and a fresh council. A later cycle can replace an earlier choice without revoking it, and the earlier reasoning stays readable.

An IDR can collide with a constraint. When review finds that, the work stops and moves to the ADR process.

Inside a cycle, an ADR takes three approvals in order. First a council justifies creating it, then a separate council approves its contents, and then it is accepted. Acceptance needs you unless `.bionic.yml` sets `adr.acceptance: council-only`. Accepting an ADR under the current policy makes its rules binding at once; no separate promotion step exists. The cycle then returns to Plan to recheck the IDRs that the decision affects.

### Council approval and independent review are different gates

A council approves a decision. An independent reviewer examines the implementation. Neither satisfies the other. [Setup]({{ "/crux/setup/" | relative_url }}#choose-the-review-policy) describes the Lite, Standard, and Strict council modes. In every mode, a demonstrated binding failure or missing authorization blocks approval. Council deliberation rounds are counted separately from cycle passes.

### Current authority and historical decisions

An accepted ADR body never changes, but its clauses can stop governing. **"Migrate ADRs"** has the architect review old decisions against current objectives, five per page by default. Each clause gets one of four dispositions:

| Disposition | Effect |
|---|---|
| retain | The clause still serves an objective; nothing changes |
| amend | The clause stays live at a narrower scope |
| replace | A successor decision takes over, with a map of which obligations move |
| retire | The clause stops governing. Needs a demonstrated conflict with an objective, or evidence that it serves none |

A clause that is dormant, missing from doctrine, or lacking evidence is not grounds for retirement. Every migration needs its own council approval and, by default, your approval of the exact package. Publication changes which clauses govern. It leaves the ADR bodies, earlier reports, and approval evidence as they were, and every citation keeps resolving.

To see what currently governs, read `bionic/adrs/doctrine/`. Doctrine is compiled from the ADR summaries and reconciled against ratified invariants. It holds no authority of its own: a disagreement resolves in the source decisions.

## Review and test evidence

### Scrutiny scales with risk

`review.scrutiny` in `.bionic.yml` sets the default depth. The reviewer records the level used and the reason for any change.

- **Focused:** one independent reviewer checks correctness, relevant tests, clarity, and security on the changed surface.
- **Standard:** review the affected behavior and integration points, and add specialists only for risks that apply.
- **Intensive:** threat analysis, adversarial checks, and specialist review of the affected boundaries and failure modes.

Specialists are targeted at actual risk: authentication and tenant isolation, credentials and sensitive data, untrusted input reaching execution, dependency and release distribution, and destructive operations. Categories that do not apply are left out. Findings are blocking, advisory, or cosmetic, and a confirmed defect keeps its severity at every level. The reviewer must differ from the implementer and must not change the work under review.

### Test results are reused when the inputs match

Test evidence belongs to the repository, not to one phase or one cycle. Before a check runs, Crux looks for a passing result recorded against the same inputs in a matching environment. The inputs are the declared files, the dependency lock, and the toolchain. A match is reused by reference.

- **A check runs again** when a relevant input changed, the evidence is missing, or a declared freshness limit expired.
- **A check does not run again** just because the phase changed, a review was requested, a new commit landed, or a new cycle or release started. A commit hash alone neither proves nor invalidates a result.
- **Bookkeeping does not invalidate.** Journal entries, log appends, queue edits, and cycle-record writes leave matching results valid.
- **Packaging, installation, and deployment checks** bind the actual artifact or deployment, so they establish their own coverage.

Each cycle declares the affected behavior and selects related tests, with a reason for each and for each one left out. Reviewers read that declaration and the evidence; they do not rerun suites by default. A project declares its own checks with the `whole-tree` preset and its own test command.

The other evidence presets (`drift-gates`, `mods-gate`, `opencode-gate`, `omp-gate`, `release-metadata`, `journal-index`) run scripts that exist only in the Crux development repository, and they now refuse elsewhere.

## Habits that keep the tree honest

### 1. Audit regularly

Say "audit docs" after every ten or so writes, after a research refresh, and before a release. It catches dangling links, supersession asymmetries, missing index rows, and stale counters, and fixes the safe ones. Derived sections have their own regenerators. Regenerate rather than hand-fix.

### 2. Treat append-only as append-only

- **ADRs.** Once accepted, the body is immutable. Write a new ADR that supersedes it, or migrate its clauses.
- **`bionic/code/` and `bionic/arch/`.** Regenerated on every run. If a docstring is wrong, fix the source.
- **`bionic/research/raw/`.** Every capture lives there forever, dated. It is the audit chain when a summary is challenged.
- **`bionic/journal/` and `bionic/log.md`.** Chronological. Do not reorder or edit past entries.
- **Cycle records.** The cycle commands write them. Do not edit phase, pass, evidence, or approval fields by hand.
- **ADR, cycle, and promptbook numbers.** Never reused.

### 3. Capture by dropping, not by filing

Drop a file, a URL, a stray idea, or a half-formed decision into `bionic/inbox/` and say "process inbox". The skill decides where it goes and asks before it files anything it is unsure about. Later, "refresh sources" re-fetches the URLs and flags the summary pages that upstream changes affect.

### 4. Plan in the cycle, not in your head

Discuss the cycle goal, plan, tasks, and acceptance criteria with your coding agent, and let the cycle commands keep the record. The plan stays visible while work proceeds, and a return keeps the earlier plan alongside the new one. Queue work you want done later instead of holding it in a chat.

### 5. Read the schema before deep work

`bionic/AGENTS.md` is the operational schema that Crux's skills and role agents read. When you wonder whether a coding agent should write somewhere, that file has the answer.

### 6. Ask; do not hand-edit

When you spot a stale page, a contradiction, or a broken link, ask Crux to fix it. Your sense that something looks off is the intended trigger.

> [!WARNING]
> Hand edits to managed files slip past audits and desynchronize the counters and indexes that the whole tree
> relies on.

## When something looks wrong

| Symptom | Try this |
|---|---|
| "Where did Crux put X?" | Read `bionic/index.md`, then the concern's own index |
| `bionic/code/` is stale | "Extract code docs" regenerates it fully |
| An accepted ADR is wrong | Write a new ADR that supersedes it, or "migrate ADRs" to amend or retire its clauses |
| A research page contradicts itself | "Refresh synthesis" walks you through the reconciliation |
| You lost track of current work | "Cycle status" shows phases, tasks, pass count, and approval waits. Historical runs stay in `bionic/promptbooks/index.md` |
| A cycle paused | Read its report. Approve more passes, answer the decision, or let it close and start a new cycle |
| A script exits 2 | That is your environment, not your docs. Read the remediation message; it names the missing parser, `uv`, or PyYAML |
| The whole tree feels broken | "Audit docs" |

## Next

The [catalog]({{ "/crux/catalog/" | relative_url }}) is the full inventory: every role and every skill, generated from the Crux source.
