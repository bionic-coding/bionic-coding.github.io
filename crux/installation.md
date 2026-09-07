---
layout: crux
title: Installing crux
permalink: /crux/installation/
description: "Install crux in Claude Code, Codex, or OpenCode."
---

**[Access the Crux repository on GitHub](https://github.com/bionic-coding/crux)**

## Requirements

- A supported agentic coding harness: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex/), or [OpenCode](https://opencode.ai/). The OpenCode integration currently targets V2 (`opencode2`).
- `python3` 3.11 or newer on your PATH. Crux's scripts are Python. macOS ships 3.9 at `/usr/bin/python3`, which cannot run them.
- [uv](https://docs.astral.sh/uv/). Every script declares its dependencies in a PEP 723 header, so `uv run <script>` resolves them. A bare `python3` runs only the scripts with no dependencies.

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Choose your harness

Crux provides the same skills and ten role agents in each supported harness. The installation path differs by host.

### Claude Code

crux installs through the Claude Code plugin marketplace. In any Claude Code session, run two slash commands:

```
/plugin marketplace add bionic-coding/crux
/plugin install crux@crux
```

The first command adds the marketplace, which is named `crux`. The second installs crux from it. Restart Claude Code so the skills and role agents register.

To upgrade, update the marketplace and run the install command again:

```text
/plugin marketplace update crux
/plugin install crux@crux
```

### Codex

Codex installs crux through its plugin marketplace:

```text
codex plugin marketplace add bionic-coding/crux
codex plugin add crux@crux
```

Restart Codex so the skills register. Then, inside a project, say **"install the Crux agents in Codex"**. The skill writes the ten `crux_*` role agents into `.codex/agents/`. It refuses to overwrite a modified agent file without `--force`.

To upgrade, repeat the marketplace and plugin commands, then restart Codex and refresh the role agents.

### OpenCode

There is no OpenCode marketplace package yet. OpenCode support is a manual, preview-grade setup against a public clone of the repo, and it targets OpenCode V2 (`opencode2`). The outline:

1. Clone the repo to a permanent path, such as `~/.local/share/crux`. The config uses absolute paths, so moving the clone later breaks the setup.
2. Generate the OpenCode agent tree with `uv run python3 crux/scripts/generate-opencode-agents.py` from inside the clone.
3. Add the clone's `crux/skills` directory, as an absolute path, to the `skills` array in `~/.config/opencode/opencode.json`.
4. Symlink every generated agent from `opencode/agents/*.md` into `~/.config/opencode/agents/`.
5. Quit and restart the OpenCode host. It loads config once at startup.
6. Verify with `opencode2 debug agents`, which should list the ten crux roles.

Run step 2 again after every `git pull`. The agent tree is generated and not tracked by git. An upgrade updates its source but leaves the old projection in place until you regenerate it.

The README's [OpenCode section](https://github.com/bionic-coding/crux#opencode-manual-setup) has the exact commands, the config snippet, and the caveat about V1 dropping the `deny` rules from the V2 agent files.

## Initialize a project

Installation does not create anything in your repository. After you restart the harness, follow [Setup]({{ "/crux/setup/" | relative_url }}) to bootstrap the `bionic/` tree.

When an upgrade changes the tree's schema, say **"audit docs --migrate"** in the project. The [changelog](https://github.com/bionic-coding/crux/blob/main/CHANGELOG.md) lists what each release added.

## Optional: a place for API keys

Some workflows call other models. The multi-model council, for example, asks Claude, Gemini, and GPT to review a decision together. Those workflows need API keys. Crux includes a CLI that keeps them in `~/.crux/env`, outside any repo, with file mode `0600`.

```sh
CRUX_ROOT=/path/to/crux
python3 "${CRUX_ROOT}/scripts/crux-env.py" init
python3 "${CRUX_ROOT}/scripts/crux-env.py" set OPENROUTER_API_KEY sk-or-...
```

Set `CRUX_ROOT` to the installed crux directory or the `crux/` directory in a source checkout. Claude Code exposes its installed directory as `${CLAUDE_PLUGIN_ROOT}`. The key name is logged; the value never is. Core documentation workflows need no API key.

## Next

[Setup]({{ "/crux/setup/" | relative_url }}): bootstrap the tree in a project and choose its conventions.
