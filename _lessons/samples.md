---
title: Samples
order: 9
summary: "Copy-paste examples you can run today."
status: published
updated: 2026-09-07
---

Every other lesson explains an idea. This one is a **shelf** — copy-paste examples you can lift and run: a prompt, a skill, a whole agent setup. Take one, swap in your details, and go. This page is the label on the shelf: what a sample is, what each one promises, and how to use one without getting burned.

## What counts as a sample

A sample is something you can **copy and actually run**, not just read about. Four kinds show up here, each from an earlier lesson:

- A **prompt** — a single reusable instruction ([Prompting and Evals]({{ "/learn/prompting-and-evals/" | relative_url }})).
- A **skill** — a packaged capability with its tools ([Skills]({{ "/learn/skills/" | relative_url }})).
- An **agent task or setup** — a bounded assignment, plus the tools and permissions it needs ([Agents]({{ "/learn/agents/" | relative_url }}) / [Agentic Harnesses]({{ "/learn/agentic-harnesses/" | relative_url }})).
- An **eval or template** — a grading rubric or a fill-in-the-blanks structure.

The bar for the shelf: each one carries enough to *use* it — what it's for, what it needs, and what a working run looks like. A clever prompt with no context isn't a sample; it's a riddle.

## Every sample follows one format

So you know what you're grabbing before you paste it, each entry has the same parts:

- **Title & purpose** — what it does, in a line.
- **Prerequisites** — what you need first (a chat app? a harness? an API key? a connected tool?).
- **The artifact** — the copyable thing itself, fenced and ready to lift.
- **Expected output** — what a working run looks like, so you can tell if yours worked.
- **Safety label** — see below.
- **License & attribution** — what you're allowed to do with it, and who to credit.
- **Troubleshooting** — the usual ways it breaks.

## The safety label — read it first

Because *some* samples can act — a prompt just talks, but a skill or agent can touch your files, send messages, or spend money — every one wears a label. Skim it before you run anything:

- **Risk level** — read-only, writes files, *sends* messages, spends money, or outright destructive?
- **Permissions & secrets** — what access it asks for, and whether it needs an API key.
- **Data shared** — what leaves your machine, and to whom (a plain prompt in a hosted app still sends your text to the provider).
- **External services & cost** — what it calls out to, and whether it can run up a bill.
- **Undo** — for anything that writes or deletes: is there a backup or a rollback?

A *"summarize this text"* prompt is harmless. A *"clean up my Downloads folder"* agent can delete things you meant to keep. The label tells you which one you're holding before you hand it the keys — the same instinct as the [Sharing]({{ "/learn/sharing-agents-and-skills/" | relative_url }}) lesson's "read it first."

## How to adapt one

Samples are starting points, not finished products:

- **Replace the placeholders** — the `<your-thing-here>` bits are yours to fill.
- **Test on sample data first** — a throwaway file, not your real one.
- **Check the output** against the expected-output note. A sample that *silently* does the wrong thing is worse than one that errors — don't just trust that it ran.
- **Version and attribute** — if you change it, note what you changed and keep the credit.

## When it doesn't work

Samples are rarely perfect plug-and-play. Expect to fix a file path, a model name, an API key, or a bit of local config — that's normal, not a failure. The troubleshooting note on each sample covers the common snags; the rest is the ordinary work of fitting someone else's thing to your setup. When something's off, re-read the prerequisites first — nine times out of ten it's a missing key or an unconnected tool.

## The shelf

Two ends of the range live here:

- **Basic** — a single, self-contained prompt you paste into any chat. No tools to set up, and low-risk as long as you don't paste anything sensitive.
- **Advanced** — a multi-tool agent setup: a [harness]({{ "/learn/agentic-harnesses/" | relative_url }}), a couple of [MCP]({{ "/learn/mcp/" | relative_url }}) servers, a skill or two, wired together to do real work.

The shelf grows over time, and every entry — basic or advanced — carries the format and the safety label above, so a beginner can start at the shallow end and wade deeper only when they're ready.

### 1. Meeting-notes tidier — prompt

> **Title:** Meeting-notes tidier
> **Purpose:** Turn messy meeting notes into a clean summary with action items.
> **Prerequisites:** Any chat app (ChatGPT, Claude, Gemini). No keys, no tools.
> **Safety:** read-only · no permissions · no tools or extra services beyond the chat app itself · your text goes to that provider, so *don't paste confidential notes into a free/shared tier.*
>
> **The artifact:**
>
> ```text
> Turn the notes below into (1) a 3-sentence summary, then (2) a bullet list of
> action items as "owner — task — due date". If a due date isn't stated, write "—".
> Do not invent owners or dates.
>
> Notes:
> <paste your notes here>
> ```
>
> **Expected output:** a short summary followed by a clean owner / task / date list — and dashes where the notes didn't say.
> **Troubleshooting:** if it invents owners or dates, add "leave blank if unsure"; if the summary runs long, cap it ("≤ 3 sentences").
> **License & attribution:** public-domain example — use and adapt freely, no credit needed.

Copy it, drop in your notes, and you've just used your first sample.

### 2. Source-check a claim — prompt

**Purpose:** Find the strongest available evidence for a factual claim and show where uncertainty remains.

**Prerequisites:** A chat app with web access. No API key or local tools are required.

**Safety:** read-only · uses web search · the claim and any context you paste go to the chat provider · do not include private or identifying information.

**The artifact:**

```text
Check this claim: <paste the claim>

Find the best available primary source. If no primary source is available, use
two independent, credible secondary sources. Report:

1. Verdict: supported, contradicted, mixed, or not enough evidence.
2. Evidence: the specific facts that support the verdict.
3. Limits: what the sources do not establish.
4. Sources: direct links, publisher names, and publication dates.

Separate verified facts from vendor claims, outside reporting, and your own
inference. Do not turn an absence of evidence into proof that the claim is false.
```

**Expected output:** a verdict followed by short evidence, limits, and source sections. Every material fact should lead back to a link.

**Troubleshooting:** if the answer cites search-result snippets, ask it to open the sources and cite the underlying pages. If sources disagree, keep the verdict “mixed” and explain the disagreement.

**License & attribution:** public-domain example — use and adapt freely, no credit needed.

### 3. Change explainer — skill

**Purpose:** Give a coding agent a reusable way to explain a proposed change before it edits anything.

**Prerequisites:** An agentic harness that supports Markdown instruction or skill files. The installation folder and activation command vary by harness.

**Safety:** read-only by instruction · needs permission to read the repository and its diff · no network or secrets · verify that your harness does not grant write tools automatically.

**The artifact:** save this as `SKILL.md` in the skill location used by your harness.

```markdown
---
name: explain-change
description: Explain a proposed code change before implementation.
---

# Explain a change

When asked to explain a proposed change:

1. Read the relevant code and tests.
2. State the current behavior in plain language.
3. Identify the smallest files or modules likely to change.
4. Describe the new behavior and one important tradeoff.
5. List the checks that would prove the change works.

Do not edit files, install dependencies, or run commands that change state.
Distinguish facts observed in the repository from recommendations.
```

**Expected output:** a short explanation of current behavior, likely change points, the main tradeoff, and a verification list. No files should change.

**Troubleshooting:** if the agent starts editing, stop it and remove write tools for this run. If the skill does not activate, check your harness's skill directory and front-matter requirements.

**License & attribution:** public-domain example — use and adapt freely, no credit needed.

### 4. Read-only repository tour — agent task

**Purpose:** Let a coding agent orient a newcomer to an unfamiliar project without modifying it.

**Prerequisites:** A coding harness opened at the repository root, with search and file-read tools. Git is helpful but optional.

**Safety:** read-only by instruction · repository contents may be sent to the model provider · no network, write, shell-mutation, or secret access is needed · use a clean working tree if you want an easy way to confirm that nothing changed.

**The artifact:**

```text
Act as a read-only guide to this repository. Do not edit files, install
dependencies, or run commands that change state.

Answer these questions from the repository itself:

1. What does this project do, and who is it for?
2. Where does execution begin?
3. Which five files or directories should a newcomer understand first?
4. How do tests, builds, and local development run?
5. What important conventions or warnings appear in repository instructions?

For every answer, cite the file path that supports it. Mark any inference as an
inference. End with a ten-minute reading order for a new contributor.
```

**Expected output:** a concise project map with file references and a reading order. `git status --short` should show no new changes afterward.

**Troubleshooting:** if the response is generic, ask for a file citation after every claim. If the repository is large, point the agent at the main application directory and ask it to ignore generated or vendored files.

**License & attribution:** public-domain example — use and adapt freely, no credit needed.

### 5. Answer-quality check — eval rubric

**Purpose:** Grade an AI answer consistently before you rely on or publish it.

**Prerequisites:** The original request, the answer, and any sources or acceptance criteria. You can apply the rubric yourself or give it to a second model.

**Safety:** read-only · no tools required · anything you paste into a hosted model goes to that provider · remove confidential material first.

**The artifact:**

```text
Grade the answer from 0 to 2 on each criterion:

- Correctness: 0 = material errors; 1 = uncertain or partly correct; 2 = supported.
- Completeness: 0 = misses the task; 1 = misses a useful part; 2 = covers it.
- Evidence: 0 = unsupported claims; 1 = partial support; 2 = traceable support.
- Clarity: 0 = hard to use; 1 = needs editing; 2 = direct and understandable.
- Restraint: 0 = invents or overclaims; 1 = some excess; 2 = states limits.

Return the five scores, one sentence of evidence for each, and the single most
important revision. Do not rewrite the answer unless asked.

Original request:
<paste request>

Answer to grade:
<paste answer>

Sources or acceptance criteria:
<paste them, or write "none provided">
```

**Expected output:** five scores out of two, a reason for each, and one prioritized revision. A low Evidence score should stay low when no sources or acceptance criteria are provided.

**Troubleshooting:** if the grader gives high scores without examples, require it to quote or point to the part of the answer that earned each score. For important work, compare the model's grading with your own.

**License & attribution:** public-domain example — use and adapt freely, no credit needed.

## Contribute a sample

Got one that works? Send it in — a pull request or an issue on the site's repository is the easiest way. The bar it has to clear is the same one every sample on the shelf met: it follows the format above, carries an **honest safety label**, and **runs from a clean start** (not just on your machine, with your half-remembered setup). Everything gets tested before it goes up — an untested sample is a liability, not a gift.

## See also

The samples draw on the ideas from across the series: **[Prompting and Evals]({{ "/learn/prompting-and-evals/" | relative_url }})** (prompts and rubrics); **[Skills]({{ "/learn/skills/" | relative_url }})**, **[Agents]({{ "/learn/agents/" | relative_url }})**, and **[Agentic Harnesses]({{ "/learn/agentic-harnesses/" | relative_url }})** (the runnable bits); **[MCP]({{ "/learn/mcp/" | relative_url }})** (the tools the advanced ones wire in); and **[Sharing Agents and Skills]({{ "/learn/sharing-agents-and-skills/" | relative_url }})** (how to install one safely).
