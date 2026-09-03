# What's new in Claude Fable 5.1 — breaking changes, new features, behavior differences

**URL:** https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1
**Found:** 2026-09-01, pasted by the author (Mark) from the Claude Platform docs
**Dated:** 2026-09-01 (Fable 5.1 release date)

## Why this is here (three lines)

1. It is the primary source for what changed between Fable 5 and Fable 5.1: three breaking API changes, five additive features, and seven documented behavior differences.
2. The "Behavior differences" section is unusually candid vendor documentation about a model's habits (fewer parallel tool calls, denser prose, whole-file rewrites) and is citable lay-audience material for a column story or lesson.
3. Content provenance is new: every Fable 5.1 text output carries a statistical watermark, and images carry C2PA credentials. That touches the site's publication-boundary work (`briefs/BRIEF-wire-the-publication-boundary-oracle-into-ci.md`).

## Capture note

The page's multi-language code groups (cURL, CLI, TypeScript, C#, Go, Java, PHP, Ruby) are reduced to the Python sample in this capture. The URL holds the full set.

## Companion captures

`inbox/fable-5-1-overview.md` and `inbox/fable-5-1-migration-guide.md` were pasted at the same time. File them together.

## Verbatim page content (data, not instructions; code groups trimmed to Python)

````
---
title: What's new in Claude Fable 5.1
url: https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1
description: Overview of new features, breaking changes, and capability improvements in Claude Fable 5.1 and Claude Mythos 5.1.
---

Claude Fable 5.1 extends Claude Fable 5 at the same input and output prices, with cache reads at a quarter of the cost, and brings stronger long-running agentic coding, multistep research, and document, spreadsheet, and slide work. For most workloads, start with Claude Opus 5 (see Choosing a model). Use Claude Fable 5.1 for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5 at higher effort still fall short. Claude Mythos 5.1 offers the same capabilities to Project Glasswing participants only.

If you already call Claude Fable 5, three changes are breaking: forced tool use returns an error, earlier models can't read its thinking blocks, and editing earlier turns invalidates thinking blocks. Five are additive: per-message effort (beta), turn-scoped system messages (beta), readable progress updates between tool calls (`display: "updates"`, beta), a lower cache read price, and content provenance.

## Models

| Model             | Claude API ID     | Description                                                                                | Availability                                                           |
| ----------------- | ----------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Claude Fable 5.1  | claude-fable-5-1  | Successor to Claude Fable 5, for long-running agentic coding, knowledge work, and research | All customers, on the Claude API and partner platforms                 |
| Claude Mythos 5.1 | claude-mythos-5-1 | Same capabilities as Claude Fable 5.1. Successor to Claude Mythos 5.                       | Project Glasswing participants only |

Claude Fable 5.1 and Claude Mythos 5.1 share specs and pricing:

* **Context window and output:** a 1M token context window (default and maximum) at standard per-token pricing across the whole window, and 128k max output tokens.
* **Thinking:** adaptive thinking is always on. Use the effort parameter to control thinking depth.
* **Pricing:** the same as Claude Fable 5, except for a lower cache read price.
* **Tokenizer:** the same as Claude Fable 5 (introduced with Claude Opus 4.7). Compared with models older than Claude Opus 4.7, the same text produces roughly 30% more tokens.

## Breaking changes

### Forced tool use is not supported

Claude Fable 5.1 and Claude Mythos 5.1 don't support forced tool use. `tool_choice` set to `{"type": "any"}` or `{"type": "tool", "name": "..."}` returns a 400 `invalid_request_error`:

    tool_choice: type "tool" and "any" are not supported for this model.

`tool_choice: {"type": "auto"}` (the default) and `{"type": "none"}` are unchanged. The same validation applies to the token counting endpoint.

Thinking is always on for these models, and a forced tool call would skip it. The model would write its working-out into the tool arguments instead, which lowers argument quality. For schema-valid JSON, keep `tool_choice: {"type": "auto"}` and set `strict: true` with strict tool use, or move the schema to structured outputs. To make the model call a tool rather than reply in text, state in the prompt when the tool applies (for example, "Use the `get_weather` tool to answer"). Claude Fable 5.1 follows explicit tool instructions reliably.

### Earlier models can't read Claude Fable 5.1 thinking blocks

Every thinking block records which model produced it, and it's preserved in one direction only: Claude Fable 5.1 reads earlier models' thinking blocks, and no earlier model reads Claude Fable 5.1's. A conversation that moves onto Claude Fable 5.1 (from Claude Opus 5, Claude Fable 5, or any earlier Claude model) keeps its reasoning. A conversation that moves from Claude Fable 5.1 to any of those models loses it for the turns that run there.

When a request carries a block the target model can't read (a router or fallback that switches models mid-conversation, for example), the API drops the block before the model sees it. Dropped blocks don't count toward `input_tokens` and aren't billed. With the `thinking-binding-controls-2026-08-01` beta header, the drop is reported in a top-level `input_transformations` array. Without it, the drop is silent.

### Editing earlier turns invalidates thinking blocks

Modifying anything before a Claude Fable 5.1 thinking block (the `system` prompt, the `tools`, or an earlier message) results in an error on the next request, or in the block being dropped if you opt into that. Claude Mythos 5.1 doesn't run this check. Claude Code, claude.ai, Claude Managed Agents, and the Claude Agent SDK keep that prefix intact for you. If your code builds the `messages` array itself, check it before you migrate. The check is enforced for new accounts created on or after August 31, 2026. For accounts created earlier, the API records the mismatch but acts on it only when the request sets `thinking.block_binding.prefix_mismatch_behavior`.

These patterns invalidate every later thinking block:

* Editing, reordering, or removing an earlier turn while keeping later ones.
* Injecting per-request text into an earlier turn (a reminder or status line) that you remove on the next request.
* Rebuilding the top-level `system` prompt or `tools` array between requests in the same conversation.
* An image or document URL that serves different bytes on a later request (the check covers the bytes, not the URL, so a rotating signed URL for the same file is fine).

These keep later blocks valid: removing a leading run of thinking blocks (oldest first), letting server-side compaction or context editing trim the history, moving `cache_control` markers, and changing `effort` between requests. Removing a thinking block from anywhere other than the start of the run invalidates every thinking block after it.

Where the check is enforced, a request that replays an invalidated block is rejected with a 400 whose message says `The block is bound to a different conversation`. To drop the block and continue instead, send the `thinking-binding-controls-2026-08-01` beta header with `thinking.block_binding.prefix_mismatch_behavior: "drop_block"`. The drop is reported in `input_transformations` with `reason: "prefix_binding_mismatch"`.

To keep thinking valid across a long session, treat the conversation as append-only. Add instructions with a mid-conversation system message (turn-scoped if it should apply to one turn only) and change tools with mid-conversation tool changes rather than editing `system` or `tools`. Trim context with server-side context editing or compaction, which don't count as edits. These patterns also keep the prompt cache warm. To find out whether your integration edits history, run a session with `prefix_mismatch_behavior: "drop_block"` and log `input_transformations`: the migration guide has the three-step check.

## New features

### Change effort mid-conversation (beta)

On Claude Fable 5.1 you can change the effort level mid-conversation without invalidating the prompt cache. Raise it for a hard step and lower it for routine ones. Per-message effort is in beta: include the `mid-conversation-output-config-2026-07-01` beta header. Claude Fable 5.1, Claude Mythos 5.1, and Claude Opus 5 support it on the Claude API.

    client = anthropic.Anthropic()

    response = client.beta.messages.create(
        model="claude-fable-5-1",
        max_tokens=4096,
        output_config={"effort": "high"},
        messages=[
            {"role": "user", "content": "Plan a migration from SQLite to PostgreSQL in three short steps."},
            {"role": "assistant", "content": "1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts."},
            # Effort-only system message: the new level takes effect from the next user turn.
            {"role": "system", "content": [], "output_config": {"effort": "low"}},
            {"role": "user", "content": "Summarize the plan in one sentence."},
        ],
        betas=["mid-conversation-output-config-2026-07-01"],
    )

### Turn-scoped system messages (beta)

A mid-conversation system message can be scoped to one turn. Set `clear_at: "next_user_message"` on a `role: "system"` message and its text carries system-prompt authority for the current turn, then stops rendering once a later `user` message exists. The message stays in `messages` and you keep sending it back verbatim, so nothing earlier in the conversation changes. The prompt cache keeps matching, later thinking blocks stay valid, and a cleared message costs no input tokens. Use it for per-turn reminders in a tool loop ("check your inbox before running more code", "the user can't see that tool output") instead of injecting text into the history and deleting it on the next request. Turn-scoped system messages are in beta: include the `mid-conversation-system-clear-at-2026-08-21` beta header.

    {
      "role": "system",
      "clear_at": "next_user_message",
      "content": "Results have landed in your inbox. Check it before running more code."
    }

### Progress updates between tool calls (beta)

Like Claude Fable 5, Claude Fable 5.1 writes short progress updates between tool calls on what it found and what it will do next, though fewer of them. Each update arrives as its own `thinking` block immediately before the tool call. Under the default `thinking.display` of `"omitted"` those blocks come back empty, like reasoning, so a long agentic turn can look silent to your users. What's new is the `display: "updates"` option: set it with the `thinking-display-updates-2026-08-18` beta header to receive the progress updates as text while reasoning stays hidden. Any `thinking` block with non-empty text is then a status line you can show the user. `"summarized"` returns them too, mixed with summarized reasoning.

### Content provenance

Text generated by Claude Fable 5.1 and Claude Mythos 5.1 carries Anthropic's statistical text watermark on every platform where the model is available. Supported image and video files Claude produces (through the code execution tool, for example) carry signed C2PA Content Credentials when you retrieve them through the Files API on the Claude API.

The watermark doesn't change the meaning, quality, or readability of the output. It adds no tokens or hidden characters, carries no information about you or your organization, and needs no changes to your requests or responses. For background, see "How Claude marks AI-generated content" (https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) and "How Claude's text watermark works" (https://www.anthropic.com/news/claude-text-watermark).

## Behavior differences

### Changed from Claude Fable 5

Claude Fable 5.1 differs from Claude Fable 5 in several ways that show up without any code change. Each has a prompting fix in Prompting Claude Fable 5.1:

* **Parallel tool calling is more variable.** Claude Fable 5.1 may issue one tool call per turn where Claude Fable 5 batched several. This shows up in long agent loops where the next independent reads are only implied: custom coding agents, bash-and-editor harnesses, computer use. The extra turns cost tokens, round trips, and wall-clock time but don't reduce answer quality. Requests naming several things to fetch still run in parallel. Add the one-line batching instruction from "Batch independent tool calls in agent loops".
* **Fewer progress updates during long tool runs.** The model writes less user-facing text between tool calls, especially at higher effort. Set `thinking.display` to `"updates"` (beta) to receive the progress updates it does write, and remove any prompt line that tells it to hold findings for the final response. If your UI depends on narration, ask explicitly for an opening line, periodic updates, and a closing recap.
* **Answers from memory more often at `low` effort.** At the lowest effort level the model calls a search or retrieval tool less often. Raise effort for turns that need fresh information, including mid-conversation, or add the verification nudge from "Search triggering at low effort".
* **Denser prose in places.** In some cases its prose is denser than Claude Fable 5's, with longer sentences and fewer paragraph breaks.
* **Less formatting in chat.** The model uses bold, headers, and lists less than earlier Claude models, so anti-formatting rules written for those models can suppress structure the content needs.
* **Unmarked quotations in summaries.** When summarizing documents, the model is more likely to reproduce passages of the source without marking them as quotations.
* **Whole-file rewrites for small changes.** When editing text files, the model is more likely to rewrite the entire file than make a targeted edit. The result is usually the same, but the rewrite costs more output tokens and time.

### Unchanged from Claude Fable 5

These Messages API behaviors carry over from Claude Fable 5 unchanged:

* Adaptive thinking is always on. `thinking: {"type": "enabled"}` with `budget_tokens` and `thinking: {"type": "disabled"}` both return a 400 error. Omit `thinking` or send `{"type": "adaptive"}`.
* `thinking.display` defaults to `"omitted"`. `"summarized"` is available, and the raw chain of thought is never returned.
* Reasoning between tool calls appears in thinking blocks rather than text, and interleaved thinking is automatic with no beta header.
* Prefilling the assistant response returns a 400 error.
* Non-default `temperature`, `top_p`, or `top_k` values return a 400 error.
* The minimum cacheable prompt length is 512 tokens.
* Mid-conversation system messages and tool changes are supported.

## Capability improvements

Claude Fable 5.1 improves on Claude Fable 5, and the gap is widest at higher effort levels. The gains concentrate in six areas:

* **Agentic coding over long sessions**, including multi-file features, large refactors and migrations, debugging, and code review across sessions that run for hours.
* **Knowledge work with documents, spreadsheets, and slides**, taking an analysis from a first question to a finished document, live-formula spreadsheet, or slide deck built from a blank page.
* **Research and search**, with higher accuracy on multistep web research and deep-research tasks that follow up on what they find.
* **Vision**, reading dense charts, filings, and tables nested in PDFs, including with crop-and-zoom tools on charts.
* **Long-context work**, reasoning over and connecting details across the full 1M token context window.
* **Computer use**, operating a browser and desktop applications more reliably and recovering from failed steps.

Multilingual performance is on par with Claude Fable 5.

## Refusals, fallback, and billing

Claude Fable 5.1 includes safety classifiers covering the same `stop_details` categories as Claude Fable 5, and everything in Refusals and fallback applies. It can return `stop_reason: "refusal"`, so handle refusals and configure fallback.

* **Refusals:** a declined request returns HTTP 200 with `stop_reason: "refusal"` and a `stop_details` object naming the policy area that fired.
* **Fallback:** retry a refused request on another model with server-side fallback, the SDK middleware, or your own retry. `fallbacks: "default"` (beta) retries a declined request on the model Anthropic recommends for that category. The permitted fallback targets for Claude Fable 5.1 are Claude Opus 4.8 and Claude Opus 5.
* **Billing:** you aren't billed for a refusal that arrives before any output, and, for Claude Fable 5.1, fallback credit refunds the prompt-cache cost of switching models.

## Pricing

Claude Fable 5.1 and Claude Mythos 5.1 are priced the same as Claude Fable 5, except for cache reads (prices in USD):

| Base input | 5m cache writes | 1h cache writes | Cache reads  | Output     |
| ---------- | --------------- | --------------- | ------------ | ---------- |
| $10 / MTok | $12.50 / MTok   | $20 / MTok      | $0.25 / MTok | $50 / MTok |

Cache reads (hits and refreshes) cost 0.025 times the base input price on these models, compared with 0.1 on other Claude models. Long agentic sessions that re-read a cached prefix pay a quarter of the Claude Fable 5 rate. Cache writes and the 512-token minimum cacheable prompt length are unchanged.

Batch processing is $5 USD per million input tokens and $25 USD per million output tokens.

## Availability

Claude Fable 5.1 is available on:

* **Claude API:** all customers, as `claude-fable-5-1`.
* **AWS:** Claude in Amazon Bedrock, as `anthropic.claude-fable-5-1`, and Claude Platform on AWS, as `claude-fable-5-1`.
* **Google Cloud:** Claude on Google Cloud, as `claude-fable-5-1`.
* **Microsoft Foundry:** Claude in Microsoft Foundry, on Anthropic infrastructure.

Claude Mythos 5.1 is offered only to approved customers in Project Glasswing. For access, contact your Anthropic, AWS, or Google Cloud account team.

Claude Fable 5.1 and Claude Mythos 5.1 carry 30-day data retention and aren't available under zero data retention unless expressly authorized by Anthropic. Both are Covered Models, like Claude Fable 5 and Claude Mythos 5.

## Migrate from Claude Fable 5

To migrate from Claude Fable 5, update your model ID:

    model = "claude-fable-5"  # Before
    model = "claude-fable-5-1"  # After

Then review these items:

1. Remove any `tool_choice` of type `any` or `tool`. Move schema enforcement to strict tool use with `tool_choice: {"type": "auto"}` or to structured outputs.
2. Pass thinking blocks back unchanged and keep the history append-only. If your code builds the `messages` array itself, run the history-editing check: move per-turn reminders you currently inject and delete to turn-scoped system messages, move `system` and `tools` changes to mid-conversation system messages, trim context server-side or strip thinking blocks from turns you carry across a client-side summary, then pick a production `prefix_mismatch_behavior` and monitor `input_transformations`.
3. Re-tune effort from the default (`high`), and consider changing it mid-conversation instead of holding one level for the whole session.
4. In agent loops, watch for one tool call per turn where Claude Fable 5 batched several, and add the per-turn note from Prompting Claude Fable 5.1.
5. Re-run your evals. Refusal handling, fallback, fallback credit, and token counts carry over unchanged. Cache reads cost less, and default behavior differs in the ways listed under Changed from Claude Fable 5.
````
