# Gardener research suggestion — the last open frontier-models item (Fable 5 specs) is now public

_Dropped by the night gardener 2026-07-15. A **suggestion**, not a dispatch — review and, if useful, run `process-inbox` / `ingest-research`. Snippet-level facts below (your `sources.md` rows are still `(proposed)`, so I did not fetch directly). Verify at the source before publishing._

## Why now

`research/references/frontier-models-2026.md` has exactly **one** item left under _Open / unverified_: Fable 5's reported **1M-token context, 128K output, and "always-on adaptive thinking."** Tonight's news sweep found the primary source that confirms all three — capture it and the frontier-models reference is **fully verified**.

## Keeper — Fable 5's specs, from Anthropic's own model docs

Primary source to capture: **Anthropic Claude Platform Docs — "Introducing Claude Fable 5 and Claude Mythos 5"**
`https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5`

Snippet-level facts to verify:
- **1M-token context window** (default), **up to 128K output tokens** per request. ✅ confirms the memo.
- **Adaptive thinking is always on** — you steer depth with the **effort** parameter; raw chain-of-thought is never returned (a summarized version is available). ✅ confirms "always-on adaptive thinking."
- Supports vision, tool use, structured outputs, prompt caching, Batch API.
- Uses the **Opus 4.7 tokenizer** — counts ~30% more tokens than older Claude models for the same text (worth a footnote anywhere you compare per-token cost).
- Pricing **$10 / $50** per MTok — matches what's already captured.

## Note

- This is the same page linked from the redeploy post ([[research/sources/anthropic-redeploying-fable-5]]) as the Fable/Mythos launch announcement.
- Capturing it lets you move the three specs out of _Open / unverified_ and cite them — and closes the frontier-models reference entirely. It also feeds the head-to-head draft (context/output windows are a real comparison axis).
- The tokenizer detail (~30% more tokens) is a genuinely useful, non-obvious fact for a plain-language cost article.
