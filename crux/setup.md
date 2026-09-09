---
layout: crux
title: Setting up a project
permalink: /crux/setup/
description: "Bootstrap the tree, then choose its conventions."
---

Installation adds crux to your agentic coding harness. Setup happens once per project, and it starts with two words.

## Bootstrap the tree

Open the project in your crux-enabled harness and say:

> **init docs**

That creates the `bionic/` tree with every concern scaffolded, plus four files worth knowing about:

- **`bionic/CLAUDE.md`** is the operational schema. The filename remains for compatibility, but crux uses it in every supported harness. It tells your coding agent what lives where and who may write it. Skim its first seven sections once.
- **`bionic/manifest.yml`** records the schema version, the enabled concerns, and which code-doc extractors run.
- **`bionic/adrs/ADR-0000-record-architecture-decisions.md`** is the first decision: that this project records decisions.
- **`.bionic.yml`** at the repo root records where the tree lives.

Crux's skills and role agents already point to the operational schema. To load it before a crux workflow starts, link to `bionic/CLAUDE.md` from your harness's project-instruction file. In Claude Code, `init docs` adds that link when the repo already has a root `CLAUDE.md`.

## Choose the conventions first

`.bionic.yml` is committed per-project configuration. The default reads:

```yaml
config_version: "1"
docs_dir: bionic
artifact_prefix: ""
```

- **`docs_dir`** relocates the tree, for example to `docs/` or `meta/docs/`. It is repo-root-relative, with no absolute paths and no `..`.
- **`artifact_prefix`** brands artifact ids so they are distinguishable across repos. With `artifact_prefix: "CRX"`, a new record is `CRX-ADR-0012`. Existing records are never renamed.

To use a non-default location, copy the template to the repo root and edit it **before** you say "init docs":

```sh
CRUX_ROOT=/path/to/crux
cp "${CRUX_ROOT}/templates/bionic-yml.tmpl" .bionic.yml
```

Set `CRUX_ROOT` to the installed crux directory or the `crux/` directory in a source checkout.

`init docs` writes the file when it is absent and merges one you already committed. Validation fails loud: a malformed `.bionic.yml` makes every consumer exit 1 with the error rather than fall back to defaults.

> [!CAUTION]
> Never put a secret in `.bionic.yml`. It is committed, and unknown keys are ignored without an error. API keys go in `~/.crux/env`, described on the [installation page]({{ "/crux/installation/" | relative_url }}).

## Turn concerns on or off

`concerns_enabled` in `bionic/manifest.yml` lists what the tree tracks. A new tree enables all nine, including the two derived surfaces. Two are worth a decision on day one:

- **`code`** extracts docs from source docstrings. Set `code.extractors` to the languages in the repo. A content-only repo, like this site, can leave the concern off.
- **`arch`** derives the current architecture from the project's own sources. It ships packs for Python, Ruby, Node.js, and Elixir/Phoenix. Say **"build the arch"** to derive it the first time, and re-derive after a change to any input. An unsupported stack produces an empty but valid spine.

A tree that predates a concern opts in by adding its name to `concerns_enabled`, then running the concern's regenerator.

## Give it something to work with

Run things through the inbox. This allows the agents to store and maintain their own knowledge.

1. Drop your existing design notes, specs, PDFs, or chat exports into `bionic/inbox/`.
2. For web sources, paste URLs one per line into `bionic/inbox/urls.md`. Add `(static)` after a URL to exclude it from refresh checks.
3. Say **"process inbox"**. Your coding agent classifies each item and shows you the proposed routing. After your approval, it files each item. Research sources get a dated raw capture plus an audited summary page. Decisions become proposed ADRs. Notes go to the journal.

## The first day

1. **Record why you are here.** Say "Propose an ADR explaining why we're using crux for this project." Review it, then "Accept ADR-0001."
2. **File the planning material** through the inbox, as above.
3. **Plan the first chunk of work.** Say "New promptbook for X", co-author the prompt list, then "Run it."
4. **Journal at the end of the day.** Say "Log today's work" with a one-line summary.
5. **Audit after the first ten writes.** Say "Audit docs" and confirm nothing has drifted.

## Adopting crux in an existing project

Nothing has to be written down before you start. `init docs` scaffolds an empty tree, and two machine passes mine what the code already encodes:

- **"Recover decisions"** finds decisions the code embodies that no ADR records, and writes them as candidates. You ratify or reject each one.
- **"Recover invariants"** finds candidate invariants and writes a check for each. Again, nothing is ratified until you say so.

Both passes propose. Neither can accept its own findings.

## Next

[Reference]({{ "/crux/reference/" | relative_url }}): what to say, which workflow to pick, and the habits that keep the tree honest.
