---
layout: crux
title: Setting up a project
permalink: /crux/setup/
description: "Bootstrap the tree, then choose its conventions."
---

Installation adds Crux to your agentic coding harness. Setup happens once per project, and it starts with two words.

## Bootstrap the tree

Open the project in your Crux-enabled harness and say:

> **init docs**

That creates the `bionic/` tree with every concern scaffolded, plus five files worth knowing about:

- **`bionic/AGENTS.md`** is the operational schema. It tells your coding agent what lives where and who may write it. Skim its first seven sections once.
- **`bionic/objectives.md`** is a placeholder for the project's mission and goals. Crux never drafts them. Until you write them, the decision review, the cleanup pass, and the night gardener ask you to fill the file in rather than cite it.
- **`bionic/manifest.yml`** records the schema version, the enabled concerns, and which code-doc extractors run.
- **`bionic/adrs/ADR-0000-record-architecture-decisions.md`** is the first decision: that this project records decisions.
- **`.bionic.yml`** at the repo root records where the tree lives and the project's review policy.

`init docs` also points your harness at the schema. When the repo root has no `AGENTS.md` or `CLAUDE.md`, it creates a root `AGENTS.md` with a line that says to read `bionic/AGENTS.md`, and an instruction to read `bionic/objectives.md`. When a root `AGENTS.md` exists, it appends whichever of the two is missing.

> [!IMPORTANT]
> `init docs` never writes to a root `CLAUDE.md`. If your repo has one, the init summary says so and names the
> remedy. Claude Code reads `CLAUDE.md`, so add a line there yourself that tells it to read `bionic/AGENTS.md`.

`init docs` refuses to touch an existing tree. Trees made by releases before 3.19.0 carry `bionic/CLAUDE.md` instead of `bionic/AGENTS.md`; [Installation]({{ "/crux/installation/" | relative_url }}#initialize-a-project) covers the migration.

## Choose the conventions first

`.bionic.yml` is committed per-project configuration. The default location settings read:

```yaml
config_version: "1"
docs_dir: bionic
artifact_prefix: ""
```

- **`docs_dir`** relocates the tree, for example to `docs/` or `meta/docs/`. It is repo-root-relative, with no absolute paths and no `..`.
- **`artifact_prefix`** brands artifact ids so they are distinguishable across repos. With `artifact_prefix: "CRX"`, a new record is `CRX-ADR-0012`. Existing records are never renamed.

> [!IMPORTANT]
> Decide both values before you say "init docs". Ids are allocated with whatever prefix is in place, and
> existing records are never renamed.

To use a non-default location, copy the template to the repo root and edit it **before** you say "init docs":

```sh
CRUX_ROOT=/path/to/crux
cp "${CRUX_ROOT}/templates/bionic-yml.tmpl" .bionic.yml
```

Set `CRUX_ROOT` to the installed Crux directory or the `crux/` directory in a source checkout.

`init docs` writes the file when it is absent and merges one you already committed. Validation fails loud: a malformed `.bionic.yml` makes every consumer exit 1 with the error rather than fall back to defaults.

> [!CAUTION]
> Never put a secret in `.bionic.yml`. It is committed, and unknown keys are ignored without an error. API keys go in `~/.crux/env`, described on the [installation page]({{ "/crux/installation/" | relative_url }}#store-api-keys).

## Choose the review policy

The same file holds three policy settings. Each one is independent of the others.

```yaml
council:
  mode: standard
review:
  scrutiny: standard
adr:
  acceptance: council-and-human
```

**`council.mode`** sets how a council approves a decision. A new setup records `standard` and offers `lite`.

| Mode | Who reviews | Approval needs |
|---|---|---|
| `lite` | Native reviewers in your harness: one challenges the decision, a fresh one gives the final review | The final reviewer's approval and the architect's agreement with that exact final text. No OpenRouter account |
| `standard` | Three models from different providers, through OpenRouter | Two of three approvals, and the architect's agreement with a reasoned answer to each dissent |
| `strict` | The same three provider seats | All three approvals and no recorded blocking finding |

Lite has verified adapters for Codex and the Claude CLI. A harness without one refuses Lite before it dispatches anything, and OpenCode stays on Standard or Strict. A missing key or capability never switches the mode for you; the council refuses and names the cause. An existing project with no `council` setting keeps Strict until you change it. `council.overrides` sets a different mode per purpose, for example `idr: lite`.

**`review.scrutiny`** sets the depth of independent code review: `focused`, `standard` (the default), or `intensive`. Scrutiny is separate from the cycle type. [Reference]({{ "/crux/reference/" | relative_url }}#review-and-test-evidence) describes each level.

**`adr.acceptance`** decides who accepts an ADR. The default, `council-and-human`, needs your approval after the council's. `council-only` lets an approved council accept on its own. An absent value means `council-and-human`.

Refreshing the tree never resets these values.

### Council attempt and output limits

`council.max_attempts` caps the review attempts for one decision. It defaults to 7, and going past seven needs your approval. A council also stops early when its progress stalls.

Each provider seat sizes its reply budget from that model's limit in Crux's model registry, instead of a flat 32,000 tokens. A seat whose reply is cut off gets one retry at its full limit, and each cycle-council record keeps the budget each attempt used. You do not set these values; they follow the models you configured.

## Turn concerns on or off

`concerns_enabled` in `bionic/manifest.yml` lists what the tree tracks. A new tree enables all nine, including the two derived surfaces. Two are worth a decision on day one:

- **`code`** extracts docs from source docstrings. Set `code.extractors` to the languages in the repo. A content-only repo, like this site, can leave the concern off.
- **`arch`** derives the current architecture from the project's own sources. It ships packs for Python, Ruby, Node.js, Elixir/Phoenix, and Swift. Say **"build the arch"** to derive it the first time, and re-derive after a change to any input. An unsupported stack produces an empty but valid spine.

A tree that predates a concern opts in by adding its name to `concerns_enabled`, then running the concern's regenerator.

Cycle records need no setting. The first cycle creates `bionic/cycles/`.

## Give it something to work with

Run things through the inbox. This allows the agents to store and maintain their own knowledge.

1. Drop your existing design notes, specs, PDFs, or chat exports into `bionic/inbox/`.
2. For web sources, paste URLs one per line into `bionic/inbox/urls.md`. Add `(static)` after a URL to exclude it from refresh checks.
3. Say **"process inbox"**. Your coding agent classifies each item and shows you the proposed routing. After your approval, it files each item. Research sources get a dated raw capture plus an audited summary page. Decisions become proposed ADRs. Notes go to the journal.

## The first day

1. **Write the objectives.** Replace the placeholder in `bionic/objectives.md` with what the project is for. Decision reviews measure against it.
2. **Record why you are here.** Say "Propose an ADR explaining why we're using Crux for this project." Review it, then "Accept ADR-0001."
3. **File the planning material** through the inbox, as above.
4. **Plan the first chunk of work.** Say "Start a cycle for X", and agree on the outcome and the acceptance evidence.
5. **Journal at the end of the day.** Say "Log today's work" with a one-line summary.
6. **Audit after the first ten writes.** Say "Audit docs" and confirm nothing has drifted.

## Adopting Crux in an existing project

Nothing has to be written down before you start. `init docs` scaffolds an empty tree, and two machine passes mine what the code already encodes:

- **"Recover decisions"** finds decisions the code embodies that no ADR records, and writes them as candidates. You ratify or reject each one.
- **"Recover invariants"** finds candidate invariants and writes a check for each. Again, nothing is ratified until you say so.

Both passes propose. Neither can accept its own findings.

## Agents without the plugin: micro-crux

Some agents that open the repo will not have Crux installed. Say **"install micro-crux"** to give them a map. The skill copies one self-contained guide, `micro-crux.md`, to the repo root. It adds a read instruction for that guide inside a managed region of the root `AGENTS.md`.

The guide explains how the tree is organized, how to find only the context a task needs, how to make a bounded change, and how to leave a note in the inbox for the full plugin to file. It also carries the current field contracts for ADRs, cycles, and the other supported records.

The guide is documentation, not the plugin. An agent reading it uses ordinary file tools. It runs no Crux skills, scripts, councils, or role agents, and it gains no approval power. Your local instructions and approval requirements still apply.

- **Opt-in.** `init docs` does not install it. The skill needs an existing schema 5 tree.
- **Edits survive.** An update replaces only unchanged managed text. A local edit to the guide or its read instruction stays and is reported as a conflict for you to resolve. There is no force overwrite.
- **Reach.** The read instruction reaches harnesses that read the root `AGENTS.md`. A root `CLAUDE.md` blocks the managed instruction; add a read instruction there yourself.

Say "update micro-crux" after an upgrade.

## Next

[Using Crux]({{ "/crux/team/" | relative_url }}): where to start, what each specialist returns, and which judgments stay yours.
