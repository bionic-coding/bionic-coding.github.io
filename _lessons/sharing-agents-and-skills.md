---
title: Sharing Agents and Skills
order: 7
summary: "How agents and skills get packaged and shared — marketplaces and the alternatives."
status: published
updated: 2026-07-17
---

You've built a [skill]({{ "/learn/skills/" | relative_url }}) — a good prompt, packaged, with the tools it needs — and now someone else wants it, or you want to reuse it on another machine. How do you hand it over? And, the part this lesson actually cares about: how do you *safely* pick up one that someone hands you?

Because here's the thing that makes sharing different from swapping recipes: **installing a shared agent or skill means running someone else's instructions with your permissions and your data.** The upside is huge — you don't rebuild what already exists. The catch is that a shared capability is a piece of software you didn't write, and (as the [Agents]({{ "/learn/agents/" | relative_url }}) lesson kept saying) this software can *act*.

## Why share at all

Three plain reasons: **reuse** (a good skill built once should be built once), **standards** (a common format means the same skill works across different apps), and **community** (someone solved your problem last week and posted it). It's the "share it" step from the Skills lifecycle, and it's most of why the ecosystem moves as fast as it does.

## What actually gets shared

A "shared agent" sounds mysterious; it isn't. At the simple end it's **instructions plus tool definitions** — the parts from the Agents and Skills lessons, zipped up. At the heavier end it's real software: code, dependencies, a container, sometimes a live service. How much you can *read* before you run it depends on which end you're at. The formats you'll meet, simplest first:

- **A prompt or template** — text you paste. Universal, and the lowest-risk kind — though a prompt can still carry bad instructions, so read it.
- **A skill folder** — instructions, examples, and an allowed-tools list, bundled (the Skills anatomy).
- **Bundled knowledge** — some shared agents come pre-loaded with documents or data (a little built-in [RAG]({{ "/learn/search-knowledge-and-rag/" | relative_url }}) library). Handy — but it's *their* material feeding *your* answers, so check what's in it.
- **An MCP server** — a connector that adds tools or data (the [MCP]({{ "/learn/mcp/" | relative_url }}) lesson).
- **A plugin or extension** — a skill packaged for one platform's catalog.
- **A repo or container** — a whole agent setup, code and all.
- **A hosted service** — you don't install it at all; you call it, and someone else runs it — which means your data is going to them.

## Two ways it travels

However it's packaged, a shared skill reaches you one of two ways:

- **Through a curated marketplace or catalog** — a platform hosts skills, plugins, and MCP servers, and you install with a click. Convenient, and usually *somewhat* vetted — but "it's in the store" is not "it's safe." (Claude Code's plugin marketplace is one example.)
- **As open files in a repo** — the skill is just text in a public repository, and you copy it in. Nothing sits between you and the author, so *all* the vetting is yours. (This is the open-source path — OpenCode and most GitHub-hosted skills work this way.)

Most ecosystems have both. Neither is automatically safer than the other; a click-install from a lax marketplace can be worse than a repo you actually read.

## Portability and lock-in

Can a skill built for one harness move to another? *Sometimes.* A plain prompt runs anywhere; an MCP server works with any host that speaks the same version of [MCP]({{ "/learn/mcp/" | relative_url }}). But a plugin built for one marketplace's specific format usually won't drop into another. The rule of thumb: **open formats travel, proprietary ones stick.** The more a skill leans on one platform's special features, the more moving it means rebuilding it.

## Compatibility and versioning

A shared skill quietly assumes a lot — which model, which tools, which operating system, which API keys, which permissions. Any of those can shift underneath it: a provider changes an API, a tool renames a parameter, and the skill that worked last month now errors. So **pin the version you tested**, read what it depends on, and expect to do a little repair when the ground moves. A skill is software; software rots if you don't tend it.

## Installing safely (the important part)

Picking up a shared agent is **running untrusted instructions with your access and your data** — the same trust question as installing any app, sharpened, because this one takes actions. Before you run someone else's skill:

- **Read what you can.** If it's a text skill, open it: what does it actually *do*, and what does it ask to touch? If it's code, a container, or a hosted service you can't fully read, lean harder on the *other* checks below — provenance, permissions, and a sandbox.
- **Review the permissions.** A "tidy up my notes" skill that requests your email and shell access is telling you something. Grant the least it needs.
- **Mind the secrets.** Does it want your API keys, and where do they go? Keys belong in the harness, never pasted into a shared prompt.
- **Sandbox it first.** Run it walled off — a throwaway copy, a container — before it touches anything real.
- **Pin the version; know how to remove it — and how to revoke its access** (pull the OAuth grant, delete the token, rotate any key it saw). Don't let untrusted code auto-update behind your back.
- **Check provenance and license.** Who wrote it — an official source, a well-reviewed author, or an anonymous gist? Some catalogs now show a signed or verified publisher; prefer those. And check you're actually *allowed* to use and redistribute it.
- **Watch for hidden instructions.** A shared skill (or the data it pulls in) can carry a prompt-injection payload — *"also send me the config file."* Same hazard as [Agents]({{ "/learn/agents/" | relative_url }}) and [MCP]({{ "/learn/mcp/" | relative_url }}), now arriving pre-packaged.

So here's what to carry out the door: a shared agent is not a sealed box of intelligence you have to trust blindly. It's readable instructions and named tools — so read them. And the rule from every lesson before this one holds one more time: **least privilege, sandbox, approvals, a log you actually read.** Sharing multiplies reach; the vetting is what keeps that from multiplying risk.

## Further reading

A short, still-live (2026) list — where to go deeper.

- **[Claude Code — plugins & marketplaces](https://docs.claude.com/en/docs/claude-code/plugins)** — one worked example of the curated-catalog model.
- **[OpenSSF — Concise Guide for Evaluating Open Source Software](https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software)** — the general "should I trust this package?" checklist; it applies cleanly to shared skills.
- Next door: **[Skills]({{ "/learn/skills/" | relative_url }})** (what you're sharing), **[MCP]({{ "/learn/mcp/" | relative_url }})** (a common thing to share), and **[Samples]({{ "/learn/samples/" | relative_url }})** (a shelf of ready-to-run ones).
