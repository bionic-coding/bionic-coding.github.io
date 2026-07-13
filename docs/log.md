# Operations log

_Append-only. Newest first._

## [2026-07-13] cleanup-campsite | 5 open (0 P1, 5 P2, 0 P3), 5 closed, 0 dismissed

Top-3 P1 ids: none (all P1s discharged). Closed since last run: `cleanup-CLN-AUD-1-recency` (audit ran) + `cleanup-CLN-JR-1-ADR-0001..0004` (launch retrospective journaled). Remaining 5 are all CLN-ADR-1 "ADR not linked from README/USER_GUIDE" — optional for a content site. See [[whats_next]].

## [2026-07-13] journal | learning: Soft-launch retrospective — ADR-0001–0004 in hindsight

Entry in `docs/journal/2026-07.md` at 13:30. Reflective launch retrospective discharging the four CLN-JR-1 journal-gap P1s. Refs: [[adrs/ADR-0001-use-jekyll-4-4-with-ruby-pinned-to-4-0-5]] [[adrs/ADR-0002-deploy-to-github-pages-via-github-actions]] [[adrs/ADR-0003-ship-a-custom-presentation-layer-over-minima]] [[adrs/ADR-0004-single-source-the-manifesto-homepage-from-research]].

## [2026-07-13] schema | disable code concern (Jekyll content site, no source to document)

Removed `code` from `concerns_enabled` in `docs/manifest.yml` and deleted the inert `code:` extractor block (all extractors were commented). Removed the `## Code` section from `docs/index.md` and deleted the empty `docs/code/` scaffold (`_meta/.gitkeep`). This clears the CHK-CODE-1 (missing `_meta/manifest.json`) BROKEN and CHK-CODE-5 (missing `code/index.md`) warning from the 2026-07-13 audit — there is no code to document on this site. `schema_version` unchanged (still `"3"`; disabling a concern is not a layout bump).

## [2026-07-13] audit | 1 broken (pending), 0 drift fixed, 2 warnings

First full-tree audit since `init` (49-check walk, inline; 34 md files). **Fixed:** none — the tree is internally consistent (research 6 sources / 6 raw dirs, frontmatter + `sources.md` + wiki-links all resolve; ADRs 5 complete/contiguous/indexed; all `docs/index.md` + concern-index counts match; log op-enum + reverse-chron order valid; schema_version 3, inbox clean). **Pending broken:** CHK-CODE-1 — `code` is in `concerns_enabled` but no extractor is configured (all commented in `manifest.yml`) and `docs/code/_meta/manifest.json` is absent; decide: configure an extractor + run `extract-code-docs`, or drop `code` from `concerns_enabled` (this is a Jekyll content site with no source to document). **Warnings:** CHK-CODE-5 (`docs/code/index.md` missing — same root cause); 5 research pages carry `## Capture gaps` (expected — the GPT-5.6/Opus/Fable captures). Baseline established for the research wiki.

## [2026-07-13] cleanup-campsite | 10 open (5 P1, 5 P2, 0 P3), 0 closed, 0 dismissed

Top-3 P1 ids: `cleanup-CLN-AUD-1-recency`, `cleanup-CLN-JR-1-ADR-0001`, `cleanup-CLN-JR-1-ADR-0002`. Findings unchanged from 2026-07-12 (no audit run, journal still empty, ADRs still unlinked from README/USER_GUIDE); today's two GPT-5.6 ingests added research surface but no new process-state findings. See [[whats_next]].

## [2026-07-13] ingest | gpt-5-6-pricing

Source: OpenAI GPT-5.6 API pricing (Sol $5/$30, Terra $2.50/$15, Luna $1/$6 per MTok; model ids + reasoning-effort ladder), pasted by the user to fill the pricing gap the system card left open. Raw: `research/raw/2026-07-13/gpt-5-6-pricing/` (verbatim paste). Synthesis: `research/references/frontier-models-2026.md` (pricing moved from _Open/unverified_ to the verified GPT-5.6 section; sources 4→5) — confirms the memo's ~$5/$30 for Sol exactly. Provenance caveat noted: user paste, canonical URL not captured (`source_url: null`, `static: false`) — supply URL for future refresh.

## [2026-07-13] ingest | gpt-5-6-system-card

Source: OpenAI "GPT-5.6 Preview System Card" (dated 2026-07-09), the 4th and final primary source from `gardener-model-news-2026-07-12.md` — closes the OpenAI-403 gap the earlier ingests flagged. Ingested from a downloaded 81-page PDF (the live blog was too large to fetch): converted to markdown via `pdftotext`. Raw: `research/raw/2026-07-13/gpt-5-6-system-card/` (original PDF + `source.md`/`source.txt` renditions). Synthesis: `research/references/frontier-models-2026.md` (added verified GPT-5.6 section; sources 3→4) — confirms the Jul 9 date + Sol/Terra/Luna tiers and moves them out of _Open/unverified_. **Pricing stays unverified:** the card contains no pricing, so the memo's ~$5/$30 figure remains flagged. Capture gaps noted on the source page: flattened benchmark tables, uncaptured figures, garbled math notation.

## [2026-07-12] ingest | simon-willison-claude-opus-4-8

Source: Simon Willison's hands-on Opus 4.8 post (2026-05-28). Raw: `research/raw/2026-07-12/simon-willison-claude-opus-4-8/`. Synthesis: updated `research/references/frontier-models-2026.md` (independent confirmation; sources 2→3). Confirms $5/$25 pricing, 1M context / 128K output (Opus, not Fable — corrected memo mis-attribution), Jan 2026 cutoff; surfaces a GPT-5.6 (Jul 9) writeup to close the OpenAI-403 gap. Third of 3 primary sources from `gardener-model-news-2026-07-12.md`.

## [2026-07-12] ingest | claude-fable

Source: Claude Fable 5 product page (Anthropic). Raw: `research/raw/2026-07-12/claude-fable/`. Synthesis: updated `research/references/frontier-models-2026.md` (added Fable section; sources 1→2). Verified the Jun 9 → Jun 12 → Jul 1 outage timeline + $10/$50 pricing. Flagged a **contradiction**: the memo's "export-control directive" cause is not on the page (Anthropic frames it as enhanced safeguards) — recorded as `> [contradiction]`/unverified, not published. Second of 3 primary sources from `gardener-model-news-2026-07-12.md`.

## [2026-07-12] ingest | claude-opus-4-8

Source: Introducing Claude Opus 4.8 (Anthropic, 2026-05-28). Raw: `research/raw/2026-07-12/claude-opus-4-8/`. Synthesis: created `research/references/frontier-models-2026.md` (new page in existing `references/` category). Verified ship date + $5/$25 pricing; benchmark table is an image (numbers not captured) — noted in Capture gaps. First of 3 primary sources dispatched from `gardener-model-news-2026-07-12.md`.

## [2026-07-12] garden | morning note 2026-07-12 (3 headlines, 1 artifact)

First visit — baselined the repo and created `docs/garden/`. Reviewed the soft-launch + Lessons rename. One inbox drop: `docs/inbox/gardener-model-news-2026-07-12.md`. See [[garden/2026-07-12]].

## [2026-07-12] cleanup-campsite | 10 open (5 P1, 5 P2, 0 P3), 0 closed, 0 dismissed

Top-3 P1 ids: `cleanup-CLN-AUD-1-recency`, `cleanup-CLN-JR-1-ADR-0001`, `cleanup-CLN-JR-1-ADR-0002`. See [[whats_next]].

## [2026-07-11] brief | BRIEF-teaching-regular-people-ai-content-plan: draft → published

Transitioned BRIEF-teaching-regular-people-ai-content-plan from `draft` to `published`. Body unchanged.

## [2026-07-11] brief | scaffolded BRIEF-teaching-regular-people-ai-content-plan

Teaching regular people AI: content plan for Articles and the Learn section.
File `docs/briefs/BRIEF-teaching-regular-people-ai-content-plan.md`, status: draft. Body human-authored next.

## [2026-07-08] adr | ADR-0004: accept (accepted)

Single-source the manifesto homepage from research. Proposed → Accepted.

## [2026-07-08] adr | ADR-0003: accept (accepted)

Ship a custom presentation layer over Minima. Proposed → Accepted.

## [2026-07-08] adr | ADR-0002: accept (accepted)

Deploy to GitHub Pages via GitHub Actions. Proposed → Accepted.

## [2026-07-08] adr | ADR-0001: accept (accepted)

Use Jekyll 4.4 with Ruby pinned to 4.0.5. Proposed → Accepted.

## [2026-07-07] adr | ADR-0004: Single-source the manifesto homepage from research

Proposed. File `docs/adrs/ADR-0004-single-source-the-manifesto-homepage-from-research.md`.
Tags: content, information-architecture, manifesto, single-source, navigation. Cites `[[research/sources/bionic-coding-manifesto]]`.

## [2026-07-07] adr | ADR-0003: Ship a custom presentation layer over Minima

Proposed. File `docs/adrs/ADR-0003-ship-a-custom-presentation-layer-over-minima.md`.
Tags: design, presentation, sass, css, typography, theming. Cites `[[research/sources/bionic-coding-manifesto]]`.

## [2026-07-07] adr | ADR-0002: Deploy to GitHub Pages via GitHub Actions

Proposed. File `docs/adrs/ADR-0002-deploy-to-github-pages-via-github-actions.md`.
Tags: deployment, github-pages, github-actions, ci, build.

## [2026-07-07] adr | ADR-0001: Use Jekyll 4.4 with Ruby pinned to 4.0.5

Proposed. File `docs/adrs/ADR-0001-use-jekyll-4-4-with-ruby-pinned-to-4-0-5.md`.
Tags: static-site, jekyll, ruby, tooling, build.

## [2026-07-07] ingest | bionic-coding-manifesto

Source: The Bionic Coding Manifesto. Raw: `research/raw/2026-07-07/bionic-coding-manifesto/`.
Synthesis touched: `research/concepts/bionic-coding.md` (new page, existing category).
Dispatched from inbox by `process-inbox`.

## [2026-07-07] init | crux bootstrap

Created `docs/` tree at schema_version 3. Detected languages: (none — Jekyll/Ruby project; no crux extractor markers matched). Meta-ADR seeded.
