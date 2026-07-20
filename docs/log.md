# Operations log

_Append-only. Newest first._

## [2026-07-20] ingest | qwen3-8-max-preview-fact-sheet

"Qwen3.8-Max-Preview — fact sheet (compiled)" — user-pasted compilation on Alibaba's Qwen3.8-Max-Preview (announced 2026-07-19 at WAIC; no model card yet). Raw: `research/raw/2026-07-20/qwen3-8-max-preview-fact-sheet/`. Modeled on [[research/sources/kimi-k3-docs]] — vendor/announcement claims flagged inline (confirmed-vs-claimed teardown; the "2.4T" and "second only to Fable 5" figures are Alibaba's unverified claims). Synthesis: added a Qwen3.8-Max-Preview section to [[research/references/frontier-models-2026]] (now 10 sources, `last_reviewed: 2026-07-20`) and qualified its intro's "no open flags" line for the two pre-release Chinese-lab entries. No new category; no contradictions.

## [2026-07-20] journal | misc: Triaged the night gardener's 2026-07-20 next-issue candidates into the weekly-post queue

Entry in `docs/journal/2026-07.md` at 09:16. Refs: [[garden/2026-07-20]]

## [2026-07-20] promptbook | abandoned PB-0001-fix-mobile-nav-and-restore-about/RUN-001

RUN-001 set `status: abandoned`, `completed_at: 2026-07-20T15:11:02Z`, `current_prompt: null`. Prompts 1–2 (verify diagnosis + council, converged round 1 / 0 MUST-FIX) left `done`; prompt 3 left `running` and 4–13 `pending` as evidence — not fabricated terminal states. Reason: the nav fix (mobile hamburger + About restoration via the `about.markdown`→`about.md` rename) was delivered directly in commits `f8a3e82`/`a77ecf2` on 2026-07-18 and verified live (green `jekyll build`, both pages render); the iterate cycle's heavyweight develop/review modules were disproportionate to a CSS+config fix. Book `PB-0001` left `status: active` with `current_run: null` (dormant; not archive-eligible while prompts are non-terminal). See [[promptbooks/runs/PB-0001-fix-mobile-nav-and-restore-about/run-RUN-001]].
## [2026-07-20] garden | morning note 2026-07-20 (3 headlines, 1 artifact)

Reviewed the delta since 2026-07-17 (`c38d596`→`6c16601`): the 07-18 buildout — README rewrite, new scaffolded `tools.md`, a de-AI-ing pass on titles/emdashes, and the mobile-nav fix (hamburger + JS + `@media` scss) with About restored via the `about.markdown`→`about.md` rename. Verified the nav fix is live (both pages render, build green). Flagged that PB-0001's RUN-001 is still `in_progress` at prompt 3 while its fix already shipped in commits — a run-ledger/reality mismatch. News sweep (WebSearch fallback; sources still `(proposed)`) firmed both carried leads — MCP `2026-07-28` final spec (8 days out) and Kimi K3 (#4 AAII / #1 Frontend Code Arena) — and surfaced the new "model + harness" frame. Escalated the `mcp.md` freshness clock once, per the 07-17 commitment. Dropped [[inbox/gardener-next-issue-candidates-2026-07-20]]. See [[garden/2026-07-20]].

## [2026-07-20] cleanup-campsite | 5 open (0 P1, 5 P2, 0 P3), 0 closed, 0 dismissed

Top-3 P1 ids: none (no P1s). All 5 open are CLN-ADR-1 "ADR-000N not linked from README/USER_GUIDE" — unchanged from 2026-07-17, optional for a content site. PB-0001 exempt from CLN-PB-1 (last run timestamp 2026-07-18, within the 7-day active-progress window); no Proposed ADRs; audit ran 2026-07-13 (7 days, < 14); retro not due. See [[whats_next]].

## [2026-07-18] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-001 to prompt 2

Prompt 1 (verify: research & reproduce) marked `done`. Diagnosis: `about.md`/`about.markdown` header_pages mismatch (verify-only, already fixed), sub-44px hamburger tap target, unstyled mobile menu panel — all reproduced by 2 independent agents + a clean `jekyll build`; recorded in [[promptbooks/runs/PB-0001-fix-mobile-nav-and-restore-about/run-RUN-001]] `notes`. `current_prompt` now 2 (council review of the diagnosis).

## [2026-07-18] promptbook | started PB-0001-fix-mobile-nav-and-restore-about/RUN-001

Started a new run against the active book. `total_prompts: 13`, `current_prompt: 1`. Snapshot: [[promptbooks/runs/PB-0001-fix-mobile-nav-and-restore-about/run-RUN-001]]. `book_content_hash` bound at start; all 13 prompts `pending`.

## [2026-07-18] promptbook | authored PB-0001-fix-mobile-nav-and-restore-about (iterate)

Iterate cycle (`cycle_kind: verify`) to fix the broken header nav — mobile hamburger (sub-44px tap target + unstyled open panel) and the About link dropped from the menu (`header_pages` referenced `about.markdown`, file is `about.md`). `total_prompts: 13`, modules `(1×verify, 1×dev, 1×review)`. Assembled from modular templates; seeded by a crux:architect diagnosis. Validated (cycle-coverage pass, exit 0). See [[promptbooks/active/PB-0001-fix-mobile-nav-and-restore-about]].

## [2026-07-17] journal | processed the 2026-07-17 gardener inbox — order fix + link-checker merge

Dispatched both gardener drops (work notes) → `docs/inbox/_dispatched/2026-07-17/`. Fixed the `order: 4` collision: `_lessons/leveraging-ai.md` → 10, `_lessons/glossary.md` → 11 (Glossary stays last). Council-merged the two link-checker branches into one two-pass checker on `garden/link-check-lessons` (`7e115e9`); deleted `garden/lesson-link-check`. Narrative: [[journal/2026-07]].

## [2026-07-17] garden | morning note 2026-07-17 (3 headlines, 3 artifacts)

Reviewed the delta since 2026-07-15 (commit `fdc917f` buildout — 7 lessons filled to published (10/11 now live), the first weekly "This Week in AI" post, Fable/Kimi research ingests, and the three model-news drafts *deleted*, not shipped — plus `c38d596` standardizing the weekly-post format via `_templates/this-week-in-ai.md` + [[briefs/BRIEF-this-week-in-ai-format]]). News sweep fed the new weekly cadence: dropped [[inbox/gardener-next-issue-candidates-2026-07-17]] (Kimi K3 receipts + Jul 27 weights; MCP spec RC Jul 28) and [[inbox/gardener-lesson-freshness-2026-07-17]] (MCP lesson vs the Jul 28 RC; the skills/leveraging-ai `order: 4` collision). Drafted branch `garden/link-check-lessons` — internal-link checker, resolving the thrice-offered link-checker in a scope that respects the perishable-post design. See [[garden/2026-07-17]].

## [2026-07-17] cleanup-campsite | 5 open (0 P1, 5 P2, 0 P3), 0 closed, 0 dismissed

Top-3 P1 ids: none (no P1s). All 5 open are CLN-ADR-1 "ADR not linked from README/USER_GUIDE" — unchanged from 2026-07-13, optional for a content site. Everything else clean: audit ran 4 days ago (< 14), no Proposed ADRs, no promptbooks, no phantom/drifted ADR-body paths, no journal gaps in the last 7 days, no forged skills, retro not due. See [[whats_next]].

## [2026-07-15] ingest | kimi-k3-docs

Captured Kimi's K3 platform docs (user paste) to back the new `_drafts/kimi-k3.md` article. Raw: `research/raw/2026-07-15/kimi-k3-docs/` (paste; canonical URL unverified, technical blog `kimi.com/blog/kimi-k3` was unreachable). Synthesis: added a **Kimi K3 (open-weights)** section to `research/references/frontier-models-2026.md` (sources 8→9) — the open/closed contrast the landscape lacked. Vendor claims (2.8T "world's first," 2.5× K2, benchmarks, pricing numbers) flagged unverified. Sources 11→12.

## [2026-07-15] ingest | anthropic-introducing-fable-5-mythos-5

Processed the inbox — dispatched the night gardener's `gardener-fable-specs-2026-07-15` suggestion. Captured Anthropic's Fable 5 model docs page. Raw: `research/raw/2026-07-15/anthropic-introducing-fable-5-mythos-5/`. Synthesis: `research/references/frontier-models-2026.md` (sources 7→8) — **resolved the last open flag**: Fable's specs (1M context / 128K output / always-on adaptive thinking, all confirmed). The frontier-models reference now carries **no open flags**. Sources 10→11.

## [2026-07-15] garden | morning note 2026-07-15 (3 headlines, 1 artifact)

Reviewed the delta since 2026-07-14 (commit `6beae98` — the published Prompting & Evals lesson + the research backing it + the two model-news flags resolved from my last suggestion — plus a `4315e73` cleanup). News sweep closed the last frontier-models gap (Fable specs); dropped `[[inbox/gardener-fable-specs-2026-07-15]]`. Lead nudge: ship an article — the runway is fully built. See [[garden/2026-07-15]].

## [2026-07-14] ingest | fable-redeploy + gpt-5-6-benchmarks (2)

Processed the inbox — dispatched the night gardener's `gardener-model-news-followup-2026-07-14` suggestion by capturing the two primary sources it flagged. `anthropic-redeploying-fable-5` (Anthropic, Jun 30) and `artificial-analysis-gpt-5-6` (AA Intelligence Index v4.1). Raw: `research/raw/2026-07-14/{anthropic-redeploying-fable-5,artificial-analysis-gpt-5-6}/`. Synthesis: `research/references/frontier-models-2026.md` (sources 5→7) — **resolved both remaining flags**: the Fable suspension *cause* (export controls + Amazon jailbreak, safeguards fix — contradiction dissolved) and the head-to-head benchmarks (AA numbers; suites disagree). Sources 8→10. Only Fable's context/output specs remain open.

## [2026-07-14] ingest | llm-evaluation sources (2)

Ingested the two Evals sources the Prompting & Evals lesson needed: `judging-llm-as-a-judge-mt-bench` (Zheng et al. 2023, the canonical LLM-as-judge paper + position/verbosity/self-enhancement biases) and `llm-as-a-judge-evidently-guide` (Evidently AI practical guide). Raw: `research/raw/2026-07-14/{judging-llm-as-a-judge-mt-bench,llm-as-a-judge-evidently-guide}/` (fetched via web-to-markdown). Synthesis: new `research/concepts/llm-evaluation.md` (sources 0→2) consolidating LLM-as-judge, the three judge biases, and the jury/council mitigation — backs the lesson's Evals section + council note. Sources 6→8, synthesis 2→3.

## [2026-07-14] garden | morning note 2026-07-14 (3 headlines, 1 artifact)

Reviewed the delta since 2026-07-12 (commits `078e719` model-news pipeline + `4574762` cleanup, and an uncommitted *My AI Kit* polish). Night's news sweep resolved both _Open/unverified_ items in `frontier-models-2026` (Fable suspension cause; head-to-head benchmarks) — dropped `[[inbox/gardener-model-news-followup-2026-07-14]]` for morning dispatch. See [[garden/2026-07-14]].

## [2026-07-13] cleanup-campsite | 5 open (0 P1, 5 P2, 0 P3), 5 closed, 0 dismissed

Top-3 P1 ids: none (all P1s discharged). Closed since last run: `cleanup-CLN-AUD-1-recency` (audit ran) + `cleanup-CLN-JR-1-ADR-0001..0004` (launch retrospective journaled). Remaining 5 are all CLN-ADR-1 "ADR not linked from README/USER_GUIDE" — optional for a content site. See [[whats_next]].

## [2026-07-13] journal | learning: Soft-launch retrospective — ADR-0001-0004 in hindsight

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
