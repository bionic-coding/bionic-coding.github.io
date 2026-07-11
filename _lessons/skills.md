---
title: Skills
order: 4
summary: "Packaged capabilities an agent picks up — including the tools it can call."
status: stub
updated: 2026-07-11
---

> **Stub — content coming soon.** Outline expanded from a 3-model council review (2026-07-11).

If an agent is the worker, a skill is something it knows how to do — and a tool is what it reaches for to do it.

## What a skill is
_TODO: a packaged, reusable capability. Note that "skill" means slightly different things across platforms — define the site's meaning._

## Anatomy of a skill
_TODO: trigger/description, instructions, inputs/outputs, allowed tools, examples, constraints, tests/evals._

## Skills vs. prompts
_TODO: when a one-off prompt should graduate into a skill._

## Tools: how a skill acts on the world
_TODO: tools are the functions a skill can call — search, files, code, web, external APIs._
_TODO: how the model actually uses one — it emits a structured (JSON) call; the harness executes it. The model doesn't run the code itself._
_TODO: why strict parameter definitions matter for reliability._
_TODO: the trust model — permissions, secrets/API keys, sandboxing, least privilege, human approval for risky actions._

## Lifecycle
_TODO: create, version, document, test, share, retire, or combine._

## Worked example
_TODO: a weather tool — what the model sends (a city), what the tool returns (a temperature)._

## References
_Platform skill/plugin docs, tool-calling / function-calling docs, packaging & versioning references, and security best practices. Route through crux; cite the source page._
