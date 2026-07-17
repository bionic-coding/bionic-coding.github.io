---
title: Skills
order: 4
summary: "Packaged capabilities an agent picks up — including the tools it can call."
status: published
updated: 2026-07-17
---

A **skill** is a capability you've packaged up so it can be reused — a prompt, plus the tools, examples, and rules that go with it, that you've decided is worth keeping and naming instead of retyping. The [Prompting and Evals]({{ "/learn/prompting-and-evals/" | relative_url }}) lesson ended on exactly this: when you catch yourself giving the same instructions over and over, that prompt wants to become a skill. This is that.

And a **tool** is the other half of the story. If a skill is *something an agent knows how to do*, a tool is *what it reaches for to do it* — a function it can call to search the web, read a file, run some code, or hit an outside service. Skills and tools travel together, so this lesson covers both.

## What a skill is

"Skill" is used loosely across the industry — one vendor's *skill* is another's *plugin*, *custom GPT*, *action*, or *extension*. On this site the meaning is simple: **a packaged, reusable capability an agent (or you) can pick up on demand.** It bundles a few things that would otherwise live in your head or scattered across old chats:

- a **name** and a description of *when* to use it,
- **instructions** for *how* to do the job,
- the **tools** it's allowed to use,
- **examples**, and the **limits**.

The whole point is to turn a good prompt from a thing *you* remember into a thing the *system* remembers — and can run consistently, with the same instructions and the same checks each time, instead of only when you happen to phrase it well.

And because a skill carries a description of *when* it applies, an agent (or the app running it) can pull it in **only when it's relevant** — the system loads it into the model's working memory on demand, instead of cramming every skill in up front. That's what lets you keep dozens of them around without drowning the model: it reaches for the one the moment the job calls for it, and ignores the rest.

## Anatomy of a skill

Peel one open and it looks a lot like a well-formed prompt with a job title:

- **A trigger / description** — when this skill should kick in ("use this to turn a receipt photo into an expense line").
- **Instructions** — how to do the job: the reusable prompt at its core.
- **Inputs and outputs** — what it needs to start, and what it hands back.
- **Allowed tools** — which actions it may take, and (just as important) which it may not.
- **Examples** — a sample input and output or two, so the model matches the pattern. (That's few-shot, straight from the prompting lesson.)
- **Constraints** — length, format, tone, the don'ts.
- **Tests / evals** — a couple of known inputs with known-good outputs, so you can tell when a change made it *worse*. (See [Prompting and Evals]({{ "/learn/prompting-and-evals/" | relative_url }}).)

## Skills vs. prompts — when to graduate one

A one-off prompt is perfect for a one-off task. Promote it to a skill when:

- you've typed roughly the same thing **three times**,
- you need it to come out **consistent** every time — not just when you happen to phrase it well,
- **someone else** (a teammate, or an agent) should be able to run it without you, or
- it's important enough to be worth **testing and versioning**.

The moment a prompt becomes infrastructure, make it a skill.

## Tools: how a skill acts on the world

Tools are the functions a skill can call — web search, reading and writing files, running code, querying a database, hitting an external API. They're what let a skill do more than talk.

Here's the part that surprises people: **the model doesn't run the tool itself.** When it wants to use one, it doesn't execute anything — it *writes a request*, a small structured (usually JSON) message that says, in effect, "call `get_weather` with `city = Denver`." The **harness** — the program wrapped around the model (see [Agentic Harnesses]({{ "/learn/agentic-harnesses/" | relative_url }})) — is what actually runs the function and feeds the result back in. The model asks; the harness acts; the model reads the answer and continues.

> [!NOTE]
> This gap is where all your safety lives. The model chooses *what* to call and *with what* — but the **harness** decides whether that call is allowed to run at all. The model can *want* to delete a file; the harness is what does, or doesn't, let it.

Two practical consequences:

- **Strict definitions matter.** Each tool declares its name, what it does, and exactly what parameters it takes — types and all. Vague definitions mean the model guesses, and guesses produce wrong calls. It's the *ask-for-a-shape* idea from the prompting lesson, pointed at tools.
- **The trust model is everything.** A tool is a door into the real world, so: **least privilege** (only the tools the job needs), **guard the secrets** (API keys live in the harness, never in the prompt), **sandbox** the risky ones, and **require human approval** for anything destructive or costly. That's the same guardrail list from the [Agents]({{ "/learn/agents/" | relative_url }}) lesson — because a tool is exactly the spot where an agent's words turn into actions.

The main open standard that's emerged for plugging tools and data into a model — so you don't hand-wire every single one — is the Model Context Protocol, and it gets its own lesson: [MCP]({{ "/learn/mcp/" | relative_url }}).

## Worked example: a weather tool

Start with what the harness *offers* the model — a tool declaration:

```text
name: get_weather
description: Get the current temperature for a city.
parameters:
  city  (string, required) — the city to look up
```

You ask: *"Should I bring a jacket in Denver?"* The model can't feel the weather, so instead of answering it emits a **call**:

```json
{ "tool": "get_weather", "arguments": { "city": "Denver" } }
```

The harness runs the real function and hands back a **result**:

```json
{ "city": "Denver", "temperature_c": 9 }
```

Now the model has a fact it didn't have a moment ago, and answers: *"It's about 9°C in Denver — yes, grab a jacket."* Notice the division of labor: the model decided *to* check and *where*; the tool supplied the number; the model turned it back into a sentence. And when a tool *fails* — the service is down, or "Denver" comes back as "not found" — it hands back an error instead of a number, and a well-built skill notices: it retries, asks you, or admits it couldn't, rather than inventing a temperature. Wrap that whole exchange in a reusable package — the instructions, the tool, an example, the rule "check before acting on an ambiguous city (is that Denver, Colorado?)" — and you've got a skill.

## Lifecycle

A skill is a small piece of software, so treat it like one:

- **Create** it — usually by promoting a prompt that earned it.
- **Document** it — what it's for, what it needs, what it returns.
- **Test** it — with the eval set from *Anatomy* above.
- **Version** it — when you change it, note what changed and keep the old one until the new one's proven.
- **Share** it — hand it to a teammate or an agent (that's the [Sharing Agents and Skills]({{ "/learn/sharing-agents-and-skills/" | relative_url }}) lesson).
- **Combine** them — big skills are often small ones stacked; an agent picks the right skill for each step.
- **Retire** it — when the task is gone or a better skill replaces it, take it out of circulation so nobody trusts a stale one.

## Further reading

A short, still-live (2026) list — where to go deeper.

- **[Anthropic — Tool use with Claude](https://docs.claude.com/en/docs/build-with-claude/tool-use)** — the first-party guide to how a model requests a tool and reads the result back.
- **[OpenAI — Function calling](https://platform.openai.com/docs/guides/function-calling)** — the same idea from the other side, including why strict parameter schemas matter.
- Next door: **[Agents]({{ "/learn/agents/" | relative_url }})** (what uses skills), **[MCP]({{ "/learn/mcp/" | relative_url }})** (the standard for connecting tools), and **[Sharing Agents and Skills]({{ "/learn/sharing-agents-and-skills/" | relative_url }})** (handing them to other people).
