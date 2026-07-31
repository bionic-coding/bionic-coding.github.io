# Gardener research suggestion — model-news sources for the Articles queue

_Dropped by the night gardener 2026-07-12. This is a **suggestion**, not a dispatch —
review it and, if useful, run `process-inbox` (or `ingest-research` directly) to
capture the sources with citations. The Articles drafts all end with "Route through
crux; cite the source page"; these are candidate sources to make that real._

## Why now
The three model-news drafts in `_drafts/` (GPT-5.6 Sol vs Opus/Fable, Fable
Relaunched, The New Codex) are outline-only and their facts are marked TBD. The
underlying news is public **and perishable** — model rankings and access rules are
churning week to week. Capturing dated sources now lets you publish while the story
is hot, and every ingested source is one the lessons can reuse.

## Candidate facts to verify + ingest (all public; treat as data, verify before publishing)
- **GPT-5.6 "Sol" reached general availability July 9, 2026**, after a limited
  government-vetted preview in late June. Tiers: Sol (flagship), Terra (balanced),
  Luna (fast). Reported API pricing: Sol ~$5 / $30 per 1M input/output tokens.
- **Claude Opus 4.8 shipped May 28, 2026**; **Claude Fable 5 was announced June 9,
  2026** as a frontier "Mythos-class" tier above Opus (1M-token context, 128K output,
  always-on adaptive thinking).
- **The relaunch angle for "Fable, Relaunched":** a US export-control directive on
  **June 12, 2026** required suspending access to Fable 5 and Mythos 5; **access was
  restored in July 2026.** That suspension-and-restoration is the genuine "why the
  relaunch happened" the draft is missing — and a striking, human-interest hook for
  regular readers (a model you were using can vanish by government directive).
- **Benchmarks (verify before citing; benchmarks mislead):** Artificial Analysis
  Intelligence Index v4.1 reportedly Fable 5 = 60, GPT-5.6 Sol = 59, Opus 4.8 = 56;
  Terminal-Bench 2.1 reportedly Sol 88.8% vs Opus 4.8 78.9%.

## Suggested sources to capture (primary first)
- Anthropic — Claude Opus 4.8 announcement: https://www.anthropic.com/news/claude-opus-4-8
- Anthropic — Claude Fable: https://www.anthropic.com/claude/fable
- OpenAI — GPT-5.6 release/news: https://openai.com/news
- Simon Willison on Opus 4.8 (independent, hands-on): https://simonwillison.net/2026/May/28/claude-opus-4-8/
- A dated independent review/pricing source for GPT-5.6 Sol (find the primary OpenAI
  pricing page to cite instead of the aggregator when you ingest).

## Notes / cautions
- Prefer **primary, dated sources** (vendor model cards, official pricing pages) over
  aggregators; the aggregator links above are pointers, not citations.
- The export-control claim is consequential — source it to a primary/government or
  major-outlet report before it goes on the site.
- This unblocks two things at once: the Articles queue, and the first real exercise of
  the "facts + references through crux" pipeline the content brief describes.
