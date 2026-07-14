# Gardener research suggestion — the two facts your model-news drafts left as TODO are now public

_Dropped by the night gardener 2026-07-14. This is a **suggestion**, not a dispatch —
review it and, if useful, run `process-inbox` (or `ingest-research` directly) to
capture the primary sources with citations. Everything below came from a snippet-level
news sweep (your `docs/garden/sources.md` rows are all still `(proposed)`, so I did not
fetch them directly). **Treat these as leads to verify at the source, not as facts to
publish as-is.**_

## Why now

Last night I flagged two things in `research/references/frontier-models-2026.md` as
_Open / unverified_ — the **cause** of the Fable suspension, and the **head-to-head
benchmarks**. Both surfaced publicly this week with citable primary sources. Capturing
them closes the last blockers on *Fable, Relaunched* and the GPT-5.6-vs-Opus/Fable
head-to-head.

## Keeper 1 — the Fable suspension cause is now on the record (resolves the ⚠️ contradiction)

The contradiction in the synthesis was: the memo said "US export-control directive,"
but Anthropic's product page gave no cause and framed the return around "enhanced
safeguards." The public reporting reconciles both — they're two ends of the same story:

- **Cause (primary source to capture):** Anthropic's own **"Redeploying Claude Fable 5"**
  post — `https://www.anthropic.com/news/redeploying-fable-5`. Reported chain: Fable 5
  launched **June 9**; on **June 12** the US applied export controls after **Amazon
  researchers reported a jailbreak** that got Fable to identify software vulnerabilities
  and, in one case, produce exploit-demonstrating code; Anthropic pulled it worldwide
  (nationality can't be verified at the API layer); the **US Dept. of Commerce lifted the
  controls June 30**; access restored **July 1** (~19 days).
- **The "enhanced safeguards" framing is also true:** on restoration Anthropic added a
  dedicated **safety classifier** that blocks the reported jailbreak (>99% per the
  reporting), and moved Fable billing onto **usage credits as of July 7**.
- **So the export-control explanation is now corroborated by a primary Anthropic source**
  — the *why* is safe to cite once you capture that post. The human-interest hook your
  draft wanted (a model pulled worldwide by government order, over a security jailbreak)
  is real and sourced.

## Keeper 2 — the head-to-head benchmarks exist now, and they DON'T crown a winner

Capture a benchmark methodology page rather than an aggregator — best candidate:
**Artificial Analysis, "GPT-5.6 has landed"** — `https://artificialanalysis.ai/articles/gpt-5-6-has-landed`
(and OpenAI's own `https://openai.com/index/gpt-5-6/`). Snippet-level numbers to verify:

- **Terminal-Bench 2.1:** Sol **88.8%** > Fable 5 / Terra (both ~84.3%) > Opus 4.8 **78.9%**.
  (This confirms the memo's Sol-88.8 / Opus-78.9 figures.)
- **SWE-Bench Pro:** **Fable 5 80.3%** > Opus 4.8 **69.2%** > **Sol 64.6%** — the ranking
  *flips*.
- **Artificial Analysis Intelligence Index (max):** Fable ~**60**, Sol **59** (≈1 pt back)
  at ~⅓ the cost; Sol leads the **Coding Agent Index (~80)**.
- **Pricing** (independent confirmation of what you captured): Sol $5/$30, Fable $10/$50,
  Opus 4.8 $5/$25 per MTok.

**The teachable point is the split itself:** Sol wins the terminal benchmark, Fable wins
SWE-Bench Pro, the intelligence index is a near-tie — there is no single "best." That's
your *why benchmarks mislead* lesson, handed to you by the data.

## Notes / cautions

- Prefer the **primary/methodology** pages (Anthropic's redeploying post, OpenAI's GPT-5.6
  page, Artificial Analysis's methodology) over the many aggregator blogs the sweep also
  surfaced.
- I did **not** fetch these directly — your `sources.md` rows are still `(proposed)`
  (snippet-only). If you accept Anthropic / OpenAI / Artificial Analysis in `sources.md`,
  next pass I can read and capture them for you instead of just pointing.
- Benchmarks move weekly and "max"-tier numbers spend more compute — date every figure and
  hedge, per your own content brief.
