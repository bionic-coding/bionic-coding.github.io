---
layout: crux
title: Installing Crux
permalink: /crux/installation/
description: "Install Crux in Claude Code, Codex, OpenCode, or OMP."
---

> [!NOTE] _Just want the source?_ **[Get Crux on GitHub](https://github.com/bionic-coding/crux)**

## Requirements

- A supported agentic coding harness: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex/), [OpenCode](https://opencode.ai/), or [OMP (Oh My Pi)](https://github.com/bionic-coding/crux/blob/main/OMP_INSTALL.md). The OpenCode integration requires OpenCode 2.x.
- Python 3.13 or newer. macOS ships 3.9 at `/usr/bin/python3`, which cannot parse Crux's scripts.
- [uv](https://docs.astral.sh/uv/). Every script declares its interpreter floor and its dependencies in a PEP 723 header, so `uv run <script>` resolves both. A bare `python3` runs only the scripts with no dependencies.
- Optional: an [OpenRouter](https://openrouter.ai/) API key. The Standard and Strict councils send each decision to three models from different providers, and OpenRouter is the gateway for those calls. The Lite council and every documentation workflow run without one. You can use the same key in OpenCode if that is your harness.

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Choose your harness

Crux provides the same skills and ten role agents in each supported harness. The installation path differs by host. In Codex, OpenCode, and OMP, the plugin and the role agents are two separate steps.

### Claude Code

Crux installs through the Claude Code plugin marketplace. In any Claude Code session, run two slash commands:

```
/plugin marketplace add bionic-coding/crux
/plugin install crux@crux
```

The first command adds the marketplace, which is named `crux`. The second installs Crux from it. Restart Claude Code so the skills and role agents register. Claude Code reads the role agents straight from the plugin, so there is no second step.

To upgrade, update the marketplace and run the install command again, then restart:

```text
/plugin marketplace update crux
/plugin install crux@crux
```

An optional run dashboard, `crux-mods`, adds a band above the prompt and a `/crux-dashboard` pane. Install it with `/plugin install crux-mods@crux`. It works in Claude Code only.

### Codex

Codex installs Crux through its plugin marketplace:

```text
codex plugin marketplace add bionic-coding/crux
codex plugin add crux@crux
```

Start a new Codex thread so the skills register. Then say **"install the Crux agents in Codex"**. The skill writes the ten `crux_*` role agents to `~/.codex/agents/`, so every project on the machine sees them. Say **"install the Crux Codex agents in this project only"** to write them to the project's `.codex/agents/` instead. A project agent with the same name shadows the personal one.

To confirm the install, say **"check the Crux Codex agents and inspect this project for shadows"**. The check reads the agent files and changes nothing. It cannot prove that Codex loaded the roles; a fresh thread that uses one is the proof.

To upgrade, update the marketplace and the plugin, start a new thread, and say **"refresh the Crux agents in Codex"**:

```text
codex plugin marketplace upgrade crux
codex plugin add crux@crux
```

The refresh refuses to overwrite a modified agent file until you review the change and allow `--force`. [CODEX.md](https://github.com/bionic-coding/crux/blob/main/CODEX.md) covers the sandbox settings a council needs in Codex.

### OpenCode

There is no OpenCode marketplace package. OpenCode support is a manual setup against a clone of the public repo, and it requires OpenCode 2.x. The outline:

1. Clone the repo to a permanent path, such as `~/.local/share/crux`. The config uses absolute paths, so moving the clone later breaks the setup.
2. Generate the OpenCode agent tree with `uv run python3 crux/scripts/generate-opencode-agents.py` from inside the clone.
3. Add the clone's `crux/skills` directory, as an absolute path, to the `skills` array in `~/.config/opencode/opencode.json`.
4. Symlink every generated agent from `opencode/agents/*.md` into `~/.config/opencode/agents/`.
5. Quit and restart the OpenCode host. It loads config once at startup.
6. Verify with `opencode debug agents`, which should list the ten Crux roles. Run it twice before you diagnose a missing role: the first call can return `[]` while the project loads.

> [!IMPORTANT]
> Run step 2 again after every `git pull`. The agent tree is generated and not tracked by git, so an upgrade
> updates its source but leaves the old projection in place until you regenerate it.

To keep the roles inside one project, register the skills, then say **"install the Crux agents in this project"**. The skill writes the ten roles to `.opencode/agents/`. A project install does not update through the symlinks; refresh it in each project.

Check the version before you rely on the roles. A 1.x runner ignores the V2 `permissions` array, so it loads every role with its `deny` rules dropped, and nothing warns you. Run `opencode --version` and read the major number. [OPENCODE.md](https://github.com/bionic-coding/crux/blob/main/OPENCODE.md) has the exact commands and the config snippet.

### OMP

OMP reads the Claude Code marketplace catalog for skills. In OMP, run:

```text
/marketplace add bionic-coding/crux
/marketplace install crux@crux
```

Start a fresh OMP session, then say **"install the Crux agents for OMP"**. The skill writes the ten roles to `~/.omp/agent/agents/`, or to the project's `.omp/agents/` when you say "in this project only". Use the installer rather than copying the role files by hand: the installer adds each role's OMP model selectors, thinking level, tools, and spawn limits.

A cycle delegates three levels deep: main session, commander, dev-lead, developer. OMP's default limit is two, so raise it in `~/.omp/agent/config.yml`:

```yaml
task:
  maxRecursionDepth: 3
```

To upgrade, update Crux through OMP's marketplace, start a fresh session, and say **"refresh the OMP agents"**. Put model overrides in `modelRoles` in your OMP config, not in the generated role files. [OMP_INSTALL.md](https://github.com/bionic-coding/crux/blob/main/OMP_INSTALL.md) covers the check command and the optional `crux-omp` dashboard.

## What each harness calls the roles

{% assign cat = site.data.crux_catalog %}
The names below are identifiers from the Crux source. A name here means the role is defined, not that it is installed in your session.

| Role | Claude Code | Codex | OpenCode | OMP |
|---|---|---|---|---|
{% for role in cat.agents %}| {{ role.id | escape }} | `{{ role.runtime_names.claude_code | escape }}` | `{{ role.runtime_names.codex | escape }}` | `{{ role.runtime_names.opencode | escape }}` | `{{ role.id | escape }}` |
{% endfor %}

The catalog records names for Claude Code, Codex, and OpenCode. The OMP column comes from the `install-omp-agents` skill, which installs each role under its bare name.

## Initialize a project

Installation does not create anything in your repository. After you restart the harness, follow [Setup]({{ "/crux/setup/" | relative_url }}) to bootstrap the `bionic/` tree.

If you upgrade from a release before 3.19.0, say **"audit docs --migrate"** in each project, even when `schema_version` is already `"5"`. The migration converts tracked `CLAUDE.md` instruction files to `AGENTS.md`. Where a scope holds both files, the old `CLAUDE.md` becomes the new `AGENTS.md`, and the previous `AGENTS.md` is kept under a name the report gives. Where a move is unsafe, the migration changes nothing in that scope and names the next step.

The current plugin works on tree schema 5 only. A schema 2, 3, or 4 tree needs the recovery ladder in the public `v3.23.2` release, run on a copy. The [user guide](https://github.com/bionic-coding/crux/blob/main/USER_GUIDE.md#recover-older-trees-and-markdown-promptbooks) has that procedure. The [changelog](https://github.com/bionic-coding/crux/blob/main/CHANGELOG.md) lists what each release added.

## Store API keys

The Standard and Strict councils call other models, so they need an API key. Crux includes a CLI that keeps keys in `~/.crux/env`, outside any repo, with file mode `0600`.

```sh
CRUX_ROOT=/path/to/crux
python3 "${CRUX_ROOT}/scripts/crux-env.py" init
python3 "${CRUX_ROOT}/scripts/crux-env.py" set OPENROUTER_API_KEY sk-or-...
```

Set `CRUX_ROOT` to the installed Crux directory or the `crux/` directory in a source checkout. Claude Code exposes its installed directory as `${CLAUDE_PLUGIN_ROOT}`. In the other harnesses, the plugin root is the parent of the `skills/` directory that holds any Crux skill. The key name is logged; the value never is. The Lite council and the documentation workflows need no API key.

## Next

[Setup]({{ "/crux/setup/" | relative_url }}): bootstrap the tree in a project and choose its conventions.
