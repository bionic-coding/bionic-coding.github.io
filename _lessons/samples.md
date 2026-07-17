---
title: Samples
order: 9
summary: "Copy-paste examples you can run today."
status: published
updated: 2026-07-17
---

Every other lesson explains an idea. This one is a **shelf** — copy-paste examples you can lift and run: a prompt, a skill, a whole agent setup. Take one, swap in your details, and go. This page is the label on the shelf: what a sample is, what each one promises, and how to use one without getting burned.

## What counts as a sample

A sample is something you can **copy and actually run**, not just read about. Four kinds show up here, each from an earlier lesson:

- A **prompt** — a single reusable instruction ([Prompting and Evals]({{ "/learn/prompting-and-evals/" | relative_url }})).
- A **skill** — a packaged capability with its tools ([Skills]({{ "/learn/skills/" | relative_url }})).
- An **agent setup** — a configured agent and the tools it's wired to ([Agents]({{ "/learn/agents/" | relative_url }}) / [Agentic Harnesses]({{ "/learn/agentic-harnesses/" | relative_url }})).
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

The shelf grows over time, and every entry — basic or advanced — carries the format and the safety label above, so a beginner can start at the shallow end and wade deeper only when they're ready. Here's what a basic one looks like, filled in:

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

## Contribute a sample

Got one that works? Send it in — a pull request or an issue on the site's repository is the easiest way. The bar it has to clear is the same one every sample on the shelf met: it follows the format above, carries an **honest safety label**, and **runs from a clean start** (not just on your machine, with your half-remembered setup). Everything gets tested before it goes up — an untested sample is a liability, not a gift.

## See also

The samples draw on the ideas from across the series: **[Prompting and Evals]({{ "/learn/prompting-and-evals/" | relative_url }})** (prompts and rubrics); **[Skills]({{ "/learn/skills/" | relative_url }})**, **[Agents]({{ "/learn/agents/" | relative_url }})**, and **[Agentic Harnesses]({{ "/learn/agentic-harnesses/" | relative_url }})** (the runnable bits); **[MCP]({{ "/learn/mcp/" | relative_url }})** (the tools the advanced ones wire in); and **[Sharing Agents and Skills]({{ "/learn/sharing-agents-and-skills/" | relative_url }})** (how to install one safely).
