# Operations log

_Append-only. Newest first._

## [2026-09-03] refresh | gpt-5-6-pricing — OpenAI cut GPT-5.6 prices; Sol $4 / $20 promotional

Refreshed while cross-checking Google's Gemini 3.8 Flash comparison table, which priced GPT-5.6 Sol at $4 / $20 against the wiki's $5 / $30. Fetched `platform.openai.com/docs/pricing` (curl with a browser user agent; `web-to-markdown` was not used). New raw: research/raw/2026-09-03/gpt-5-6-pricing/ (`source.html`, tag-stripped `extracted.md`); the July paste kept under `previous_captures`. Page now lists Sol $4 / $20, Terra $2 / $12, Luna $0.20 / $1.20 (short context; long context double) with "GPT-5.6 Sol's promotional pricing is available at least through November 21, 2026." `source_url` filled (was null), `last_source_check` 2026-09-03. Source page rewritten with a current-prices table, a July-vs-September delta table, and the original paste preserved. Synthesis: research/references/frontier-models-2026.md GPT-5.6 pricing bullet gained an update line; the price-direction note now counts five hold-or-cut moves across Anthropic, OpenAI, and Google.

## [2026-09-03] ingest | meta-muse-spark-1-3

Meta Superintelligence Labs launch post "Introducing Muse Spark 1.3" (2026-09-02), user-supplied URL for the This Week in AI draft. Raw: research/raw/2026-09-03/meta-muse-spark-1-3/ (extracted.md, five images, plus the linked four-page evaluation-methodology PDF fetched separately). The 11-row benchmark scorecard is an image; transcribed by reading it (Muse Spark 1.3 max vs 1.2 xhigh vs GPT-5.6 Sol max vs Opus 5 max). Synthesis: research/references/frontier-models-2026.md, new "Meta — Muse Spark 1.3" section; research/references/open-weights-landscape-2026.md Muse Glimmer section gained an update note that Meta now names a Muse Spark open-weights release on its roadmap. Cross-vendor check against Google's same-day table: Opus 5 DeepSWE 74.0 and GDPVal 1824 match; Opus 5 Terminal-Bench 2.1 differs (86.7 vs 89.1). Vendor-run; no pricing, no context or cutoff figures.

## [2026-09-03] ingest | gemini-3-8-flash

Google launch post "Introducing Gemini 3.8 Flash and 3.8 Flash Cyber" (The Keyword, 2026-09-02), user-supplied URL for the This Week in AI draft. Raw: research/raw/2026-09-03/gemini-3-8-flash/ (extracted.md, 20 images, plus `gemini-api-pricing.html` fetched from ai.google.dev to verify the price). The 14-row comparison table is an image; transcribed by reading it. Pricing verified: $0.75 / $3.75 through 2026-12-31, $1.50 / $7.50 from 2027-01-01, identical schedule to 3.7 Flash. Synthesis: research/references/frontier-models-2026.md, new "Google — Gemini 3.8 Flash" section (first Google entry in the file), scope note and frontmatter updated (sources 26, tags +google +meta +gemini +muse-spark). Contradiction found and resolved: the table's GPT-5.6 Sol $4 / $20 disagreed with the wiki's July $5 / $30; OpenAI's live page confirms the cut (see the `refresh` entry above). DeepSWE cost-chart readings are approximate and marked so.

## [2026-09-03] schema | refresh bionic/CLAUDE.md from the crux 3.5.0 template

Re-rendered `bionic/CLAUDE.md` from `~/.claude/plugins/cache/crux/crux/3.5.0/templates/CLAUDE.md.tmpl` (`{{repo_name}}` → bionic-coding, `{{today}}` → 2026-09-03), replacing the 2026-07-31 render from the 1.8.0 template. The 3.5.0 template already carries the schema-ladder and `.bionic.yml` relocation corrections the July render had to patch by hand, so those local edits are dropped. Two local deltas remain: the one leftover `<tree>` literal (§7, the `"4"` rung) resolved to `bionic/invariants/checks/`, and the ADR-0044 citation in §14 preserved. New sections now present: §11.C (cycle tiers and `patch` blast radius), §11.D (ADR body content rule), §17 (observations concern), and the `governs` row in §11.A, which clears the CHK-ADR-1a warning from the 2026-09-01 audit. `manifest.yml` untouched: `observations` and `arch` stay unenabled (opt-in for existing trees per §17 / §4).

## [2026-09-01] audit | 0 broken, 0 drift fixed, 7 warnings

Full vault walk at `schema_version: "5"`, docs_dir `bionic` (`.bionic.yml`, `source: ".bionic.yml"`), against installed crux 3.5.0. No repo-level BROKEN findings and no auto-fixes applied — nothing in the tree needed repair.

**Clean:** CHK-CFG-1/2/3/4 (one tree, bare artifact prefix throughout, no `(type, NNNN)` collisions); CHK-SCHEMA-1 (`"5"`); CHK-INBOX-1/2/3 (inbox present and empty, `research/new/` absent); CHK-MI-1/2/3 (every enabled concern has a section, all counts exact, `_Last updated: 2026-09-01_`); CHK-LOG-1..4 (105 headings, all in-enum, all reverse-chronological); CHK-RES-1..10 (41 sources, 6 synthesis pages, 41 raw dirs each referenced exactly once, registry 9 columns and 41 rows, 177 research wiki-links all resolving); CHK-ADR-1..12 (6 ADRs, contiguous 0000-0005, keyset matches §11.A exactly, ADR-0004↔ADR-0005 supersession bidirectional, `next_number: 6`); CHK-BR (4 briefs, no ADR cites a draft); CHK-JR-1..5 (7 entries across 2 months, index counts and per-category breakdowns exact, all links resolve); CHK-PB-1..12 + CHK-PB-SCHEMA/BIND/ABANDON/CYCLE (PB-0001 and both runs validate against the 3.5.0 schemas; `book_content_hash` recomputes identical on both runs — the CHK-PB-BIND mismatch left open by the 2026-07-30 audit is resolved); CHK-CAT-1..6 (59 skills = 59 catalog entries, no drift, no validation errors); CHK-DOCTRINE-1 (0 domains); governs coverage (cohort size 0). CHK-INV-* vacuously clean: invariants enabled, 0 pins, `checks: []`. CHK-ARCH-*, CHK-CODE-*, CHK-OBS-* silent (concerns not enabled, trees absent). CHK-ADR-SPEC inert (`adr.spec_rule_from` not set).

**Drift (2), recommend-only, NOT applied.** Two regenerated-artifact projections that crux 3.5.0 enrolls have never been generated in this tree: `summarize-adrs.py --dry-run` reports `bionic/adrs/summaries/{_meta.json,implementation-map.md,resolver.json,rule-table.md}` missing, and `compile-doctrine.py --dry-run` reports `bionic/adrs/doctrine/{_meta.json,index.md}` missing. Both project from ADR `governs` blocks, which no ADR here carries (governs cohort is empty), so both would produce empty projections. Per the audit contract these are recommended, never auto-regenerated.

**Warnings (7).** (1) CHK-ADR-1a: the 3.5.0 `templates/ADR-template.md` keyset carries `governs`; this tree's §11.A does not list it. Root cause is broader — `bionic/CLAUDE.md` was last rendered from the crux 1.8.0 template (see the 2026-07-31 entry) and lacks §11.C (cycle tiers / patch blast radius), §11.D (ADR body content rule), §17 (observations concern), and the `governs` row. (2) `bionic/adrs/lineage.md` still carries a dangling `[[adrs/ADR-0016-add-link-adr-graph-skill]]` — hard-coded at `scripts/generate-lineage.py:80` in crux 3.5.0, unchanged since first reported 2026-08-25; it names the plugin's own ADR and re-dangles on every regenerate, so it is not fixable here. (3) 12 dangling `[[inbox/gardener-*]]` links across 7 garden morning notes and `log.md`, all pointing at items `process-inbox` relocated to `bionic/inbox/_dispatched/<date>/`; both surfaces are append-only, so these stay as historical references. (4) 3 dangling `[[_lessons/*]]` links (`mcp`, `skills`, `sharing-agents-and-skills`) from garden notes and two research concepts pages — proposed Jekyll lessons that do not exist yet; they point outside the docs tree. (5) CHK-RES-11: 3 `> [contradiction]` markers in 2 files (`research/sources/state-of-open-source-local-llms-july-2026.md` x2, `research/references/open-weights-landscape-2026.md` x1); 0 unresolved / source-updated / refresh-failed; 39 `## Capture gaps` sections. (6) 2 source pages carry no `## Capture gaps` section: `research/sources/bionic-coding-manifesto.md` and `research/sources/qwen3-8-2-4t-a95b-open-weights-release.md`. (7) `bionic/index.md` delegates its Research, Journal, and Promptbooks sections to the concern indexes (`See [[research/index]].`) rather than inlining the per-page bullets the §5 template sketches. Applied consistently across three concerns, heading counts exact, and consistent with §5's own closing sentence that the file is a rollup while each concern index carries the authoritative detail — left as-is.

**Pending user decision:** none. The two drift items and warnings 1-4 all need a decision about whether to adopt 3.5.0 contracts in this tree; nothing is blocking.

## [2026-09-01] cleanup-campsite | 0 open (0 P1, 0 P2, 0 P3), 1 closed, 0 dismissed

No open findings. Closed: `cleanup-CLN-ADR-1-ADR-0005`, because rule `CLN-ADR-1` was retired in crux 3.5.0 (carried five runs, never actioned; the ADR itself is unchanged). Every other implemented rule reported clean or skipped on its existence gate; August 2026 sits exactly at the `CLN-JR-2` floor (2 journal entries, 42 ops). `## What's next` section removed from `bionic/index.md` since N = 0. See [[whats_next]].

## [2026-09-01] ingest | openrouter-kimi-k3

OpenRouter model page — MoonshotAI: Kimi K3, user-supplied URL, one of five OpenRouter pages for the author's current open-model working set. Raw: research/raw/2026-09-01/openrouter-kimi-k3/ (page capture plus `api.json` from `/api/v1/models`). Synthesis: research/references/open-weights-landscape-2026.md (shared serving-snapshot section and comparison table). Kimi K3 on OpenRouter: $3 / $15 list across 17 providers, 943,718-token max output, per-provider GPQA spread 67–93%. Side finding via Hub API: `moonshotai/Kimi-K3` exists, ungated, 2.78M downloads, license tag `other` — the K3 weights open question is marked resolved for availability, still open for license terms. Rolling page, `static: false`.

## [2026-09-01] ingest | openrouter-qwen3-8-flash

OpenRouter model page — Qwen: Qwen3.8 Flash, user-supplied URL, one of five OpenRouter pages for the author's current open-model working set. Raw: research/raw/2026-09-01/openrouter-qwen3-8-flash/ (page capture plus `api.json` from `/api/v1/models`). Synthesis: research/references/open-weights-landscape-2026.md (shared serving-snapshot section and comparison table). Qwen3.8 Flash on OpenRouter: new model to the wiki, released 2026-08-26, $0.15 / $0.47, text+image+video in, single provider. HF repo `Qwen/Qwen3.8-Flash-Next` created 2026-08-24, license tag `other` (not captured). Rolling page, `static: false`.

## [2026-09-01] ingest | openrouter-glm-5-3-flash

OpenRouter model page — Z.ai: GLM 5.3 Flash, user-supplied URL, one of five OpenRouter pages for the author's current open-model working set. Raw: research/raw/2026-09-01/openrouter-glm-5-3-flash/ (page capture plus `api.json` from `/api/v1/models`). Synthesis: research/references/open-weights-landscape-2026.md (shared serving-snapshot section and comparison table). GLM 5.3 Flash on OpenRouter: $0.15 / $0.50 list, 50% promotion through 2026-09-09, 22 providers, 1.38T tokens from Hermes Agent in week one. Listed context 1,310,720 exceeds the model config's 1,048,576; synthesis says cite the config. Rolling page, `static: false`.

## [2026-09-01] ingest | openrouter-glm-5-3

OpenRouter model page — Z.ai: GLM 5.3, user-supplied URL, one of five OpenRouter pages for the author's current open-model working set. Raw: research/raw/2026-09-01/openrouter-glm-5-3/ (page capture plus `api.json` from `/api/v1/models`). Synthesis: research/references/open-weights-landscape-2026.md (shared serving-snapshot section and comparison table). GLM 5.3 on OpenRouter: first captured API price for GLM-5.3, $1.40 / $4.40, cache read $0.26, 22 providers, released 2026-08-18. Rolling page, `static: false`.

## [2026-09-01] ingest | openrouter-qwen3-8-2-4t-a95b

OpenRouter model page — Qwen: Qwen3.8 2.4T A95B, user-supplied URL, one of five OpenRouter pages for the author's current open-model working set. Raw: research/raw/2026-09-01/openrouter-qwen3-8-2-4t-a95b/ (page capture plus `api.json` from `/api/v1/models`). Synthesis: research/references/open-weights-landscape-2026.md (shared serving-snapshot section and comparison table). Qwen3.8 2.4T A95B on OpenRouter: $2 / $6 at 5 of 7 providers, 262,144 max output, text only, Exacto benchmarks vary 84–91% GPQA by provider. Rolling page, `static: false`.

## [2026-09-01] ingest | glm-5-3-flash-model-card

Hugging Face model card for zai-org/GLM-5.3-Flash, user-supplied URL. Raw: research/raw/2026-09-01/glm-5-3-flash-model-card/ (card, three images, plus fetched `LICENSE`, `config.json`, Hub API record). Synthesis: research/references/open-weights-landscape-2026.md (shared GLM-5.3-Flash section). Closes the blog's gaps: MIT license, 1,048,576-token context, 45 layers (34 linear + 11 sparse attention), repo created 2026-08-25. Side finding via Hub API and raw LICENSE fetch: zai-org/GLM-5.3 weights also shipped 2026-08-25, under a custom "GLM-5.3 License" (MIT text plus a security-review clause for Model-as-a-Service operators above US$10B revenue), not MIT — the 5.3 open question is marked resolved; the 5.3 card itself remains uncaptured. Benchmark figure transcribed from the image; matches the blog's table data.

## [2026-09-01] ingest | glm-5-3-flash

Z.ai launch post "GLM-5.3-Flash: Frontier Intelligence, Flash Cost" (2026-08-26), user-supplied URL. Raw: research/raw/2026-09-01/glm-5-3-flash/. Capture note: the page is a JavaScript app; `web-to-markdown` and a rendering fetch both returned empty bodies, so the article was reconstructed in order from string literals in the page's JS bundle (saved in raw). Three benchmark tables recovered as data; four figures not captured. Synthesis: research/references/open-weights-landscape-2026.md (new section; GLM-5.3 header and license paragraph updated). Vendor-run numbers marked as such; "approaching Opus 4.8" survives the table, comparison set is Opus 4.8 not Opus 5.

## [2026-09-01] ingest | claude-fable-5-1-migration-guide

Claude Platform docs, "Migrating to Claude Fable 5.1 and Claude Mythos 5.1" (release-day page, user paste plus same-day fetch). Raw: research/raw/2026-09-01/claude-fable-5-1-migration-guide/. Synthesis: research/references/frontier-models-2026.md (new Fable 5.1 section, shared with the two sibling captures). Operational detail behind the what's-new page: the append-only history requirement, the three-step history check, fallback targets Opus 4.8 and Opus 5, and the Opus 5 deltas (2× per-token price, 30-day retention, not on Priority Tier). Multi-language code groups reduced to Python in the source page; full set in the raw capture. Dispatched from inbox by `process-inbox`.

## [2026-09-01] ingest | claude-fable-5-1-whats-new

Claude Platform docs, "What's new in Claude Fable 5.1" (release-day page, user paste plus same-day fetch). Raw: research/raw/2026-09-01/claude-fable-5-1-whats-new/. Synthesis: research/references/frontier-models-2026.md (new Fable 5.1 section). Three breaking changes, five additive features, seven vendor-documented behavior differences; content provenance (statistical text watermark on all Fable 5.1 output, C2PA on media) noted as relevant to BRIEF-wire-the-publication-boundary-oracle-into-ci. Capability claims carry no benchmarks and are marked claimed-not-verified. Dispatched from inbox by `process-inbox`.

## [2026-09-01] ingest | claude-fable-5-1-overview

Claude Platform docs, "Claude Fable 5.1" model overview (release-day page, user paste plus same-day fetch). Raw: research/raw/2026-09-01/claude-fable-5-1-overview/. Synthesis: research/references/frontier-models-2026.md (new Fable 5.1 section; Fable 5 section marked superseded; naming note updated). Fable 5.1 released 2026-09-01 at Fable 5's $10 / $50 with cache reads cut to $0.25 per MTok; the vendor lineup table re-confirms Sonnet 5 at $2 / $10 and adds knowledge cutoffs. Source inconsistency flagged: the page's table footnote says cache reads cost 10% of input, its own pricing table says 2.5%. No contradiction with existing pages. Dispatched from inbox by `process-inbox`.

## [2026-08-25] brief | scaffolded BRIEF-wire-the-publication-boundary-oracle-into-ci

"Wire the publication-boundary oracle into CI" — bionic/briefs/BRIEF-wire-the-publication-boundary-oracle-into-ci.md, status: draft. Scaffold only; the body is the author's to write. Dispatched by owner decision after this session's inbox pass held the item back as `unsure` between `adr` and `brief`; owner chose `brief`. Reference material preserved at bionic/inbox/_dispatched/2026-08-25/gardener-idea-publication-boundary-gate.md — verified diagnosis, four open design questions (which oracle, count vs allowlist, where it runs, fail vs warn). Becomes an ADR once those are answered.

## [2026-08-25] audit | 1 broken (upstream), 2 drift fixed, 1 warning

Full vault walk at `schema_version: "5"`, docs_dir `bionic` (`.bionic.yml`). **Drift fixed (2):** `bionic/adrs/index.md` regenerated by `generate-adr-index.py` (dropped the non-canonical `_Last updated:_` line, added the `## Archived (0)` section, picked up ADR-0000's `process` tag that the hand-maintained table had dropped); `bionic/adrs/lineage.md` created by `generate-lineage.py` — the file was missing entirely (6 ADRs, 1 supersedes edge, 0 amends, 4 topic clusters). Both are regenerated artifacts per CLAUDE.md §4; all three regenerator dry-runs now report no drift. **Broken (1), NOT a repo defect:** the freshly generated `lineage.md` header carries a wiki-link to `ADR-0016-add-link-adr-graph-skill`, hard-coded at `scripts/generate-lineage.py:80` in crux 2.0.1 — it names the *plugin's own* ADR, which does not exist in this project. It re-dangles on every regenerate, so it is not editable here; fix belongs upstream. **Warning (1) — since cleared:** CHK-INBOX-3 reported 1 item pending at scan time (`gardener-idea-publication-boundary-gate.md`, held back as `unsure` between `adr` and `brief`); the owner chose `brief` and it was dispatched after the walk. The inbox is now empty. Clean: CHK-SCHEMA-1, CHK-CFG-1/3, CHK-RES-1..10 (31 sources, 6 synthesis pages, no orphan or shared raw captures, registry 9 columns and 31 rows), CHK-ADR-1..9, CHK-BR, CHK-LOG-1..4, CHK-JR-1..5, CHK-MI-1..3, CHK-PB. CHK-INV silent: invariants enabled, ledger empty (0 pins), `bionic/invariants/checks/` absent — vacuously clean. CHK-RES-11: 3 contradiction/unresolved markers and 29 `## Capture gaps` sections across research pages.

## [2026-08-25] cleanup-campsite | 1 open (0 P1, 1 P2, 0 P3), 0 closed, 0 dismissed

No P1 findings. The single open id is `cleanup-CLN-ADR-1-ADR-0005`, carried unchanged for a fifth consecutive run; it ages out on 2026-09-13. Every other implemented rule reported clean or skipped on its existence gate. See [[whats_next]].

## [2026-08-25] brief | scaffolded BRIEF-a-third-content-stream-field-notes

"A third content stream: what to do about field notes" — bionic/briefs/BRIEF-a-third-content-stream-field-notes.md, status: draft. Scaffold only; the body is the author's to write. Reference material is the night gardener's drop, preserved at bionic/inbox/_dispatched/2026-08-25/gardener-idea-field-notes-stream.md (four options, cheapest first). Anything past option A touches ADR-0005 and wants an ADR after this brief.

## [2026-08-25] ingest | snyk-toxicskills-agent-skills-audit

Snyk "ToxicSkills" audit of 3,984 agent skills (published 2026-02-05). Raw: research/raw/2026-08-25/snyk-toxicskills-agent-skills-audit/. Synthesis: new page research/concepts/agent-skill-supply-chain-security.md. Corrects the drop that requested it: the post's own title ("Prompt Injection in 36%") misstates its body — 36.82% is any-severity, 13.4% is critical, prompt injection is 2.6% of the corpus and 91% of the 76 confirmed-malicious samples. February measurement of an ecosystem the post says grew 10x in weeks; re-check before publishing. Suggested `_lessons/sharing-agents-and-skills` edit (a scan-step bullet) is scaffolded, not written — author's prose. Attacker payloads summarized, not reproduced; the mcp-scan technical report PDF was not captured.

## [2026-08-25] ingest | claude-platform-release-notes

Claude Platform release notes, a rolling page (static: false); window 2026-07-24 to 2026-08-20 transcribed, earlier entries left in the raw capture. Raw: research/raw/2026-08-25/claude-platform-release-notes/. Synthesis: research/references/frontier-models-2026.md (new platform-and-pricing section). Verifies the drop's claim against the primary: the Sonnet 5 increase to $3/$15 on 2026-09-01 was cancelled and $2/$10 is now standard (note dated 2026-08-10). Contradiction flagged, not resolved: the lede of _posts/2026-08-14-this-week-in-ai.md argues open weights win because closed-model costs "keep increasing" — four days before that post published. Editorial call is the author's. Also closes the Opus 5 pricing/spec flag the system card left open ($5/$25, 1M context default and max, 128k output, thinking on by default).

## [2026-08-25] ingest | muse-glimmer-open-agentic-model

Meta Superintelligence Labs' Muse Glimmer (2026-08-10): 30B, Apache 2.0, local-agent focus. Raw: research/raw/2026-08-25/muse-glimmer-open-agentic-model/. Synthesis: research/references/open-weights-landscape-2026.md (new section). Resolves the naming question the drop left open: Muse Glimmer is the released open-weights model, Muse Spark is the closed teacher it was distilled from — the CNBC framing ("open the weights for Muse Spark 1.2") is the misread. Capture gap: both benchmark tables are figure images, so no numbers were captured; the linked methodology report would need a second ingest.

## [2026-08-25] ingest | mcp-spec-2026-07-28-changelog

MCP specification revision 2026-07-28 changelog, read in full. Raw: research/raw/2026-08-25/mcp-spec-2026-07-28-changelog/. Synthesis: new page research/concepts/model-context-protocol.md. Sessions and the initialize handshake removed, server/discover now mandatory, SSE resumability gone; Roots, Sampling, and Logging deprecated under a new twelve-month lifecycle policy. Lesson-impact check recorded: _lessons/mcp teaches Tools, Resources, and Prompts, all untouched — no edit needed, `updated: 2026-07-17` stands. Two ecosystem-response claims (Google 2026-08-05, Microsoft C# SDK v2.0) carried forward as unverified; neither was fetched.

## [2026-08-18] garden | morning note 2026-08-18 (3 headlines, 4 artifacts)

Ten owner commits since `daeef0d`, two posts shipped, five research sources ingested. Note: [[garden/2026-08-18]]. Artifacts: three inbox drops (`gardener-news-mcp-2026-07-28-spec`, `gardener-news-agent-skill-scanning`, `gardener-idea-field-notes-stream`) and the branch `garden/fix-live-post-typos`.

## [2026-08-18] cleanup-campsite | 1 open (0 P1, 1 P2, 0 P3), 0 closed, 0 dismissed

No P1 findings. The single open id is `cleanup-CLN-ADR-1-ADR-0005`, carried unchanged from the 2026-08-15 run. See [[whats_next]].

## [2026-08-15] ingest | qwen3p8-max-fireworks-model-page

Fireworks model page at fireworks/qwen3p8-max — capture anomaly recorded: the URL serves the Qwen3.8-2.4T-A95B open-weights listing ($2.00/$0.25/$6.00 per MTok, 262k context, created 8/12/2026), not a separate Qwen3.8-Max listing. Raw: research/raw/2026-08-15/qwen3p8-max-fireworks-model-page/. Synthesis: research/references/open-weights-landscape-2026.md (Qwen section hosting bullet) and research/references/frontier-models-2026.md (Qwen3.8-Max section hosting bullet). Host spec fields.

## [2026-08-15] ingest | qwen3-8-2-4t-a95b-open-weights-release

Qwen3.8-2.4T-A95B — Hugging Face model card: the Qwen3.8 open-weights release (live by capture date; custom `qwen3.8-max` license; text-only, thinking always on; architecture disclosed). Raw: research/raw/2026-08-15/qwen3-8-2-4t-a95b-open-weights-release/. Synthesis: research/references/open-weights-landscape-2026.md (Qwen section rewritten — weights shipped, license resolved-with-caveat, two open questions closed, licensing observation updated) and research/references/frontier-models-2026.md (Qwen3.8-Max section updated).

## [2026-08-15] ingest | deepseek-v4-pro-0813-fireworks-model-page

DeepSeek-V4-Pro-0813 — Fireworks model page ($1.32/$0.044/$3.96 per MTok, 1040k context, created 8/13/2026). Raw: research/raw/2026-08-15/deepseek-v4-pro-0813-fireworks-model-page/. Synthesis: research/references/open-weights-landscape-2026.md (DeepSeek section hosting bullet; pricing observation updated). Host spec fields; 1.6T vs HF 1.7T flagged unresolved.

## [2026-08-15] ingest | deepseek-v4-pro-0813-model-card

DeepSeek-V4-Pro-0813 — Hugging Face model card (official release, MIT, 1.7T params, DSpark speculative decoding). Raw: research/raw/2026-08-15/deepseek-v4-pro-0813-model-card/. Synthesis: research/references/open-weights-landscape-2026.md (new DeepSeek-V4-Pro-0813 section + open question on active-param count / technical report). All benchmark figures vendor claims.

## [2026-08-15] ingest | glm-5-3-frontier-coding-with-emergent-cyber-capabilities

GLM-5.3: Frontier Coding with Emergent Cyber Capabilities (Z.ai launch blog, 2026-08-14). URL serves a JS SPA shell — text extracted verbatim from the page's own JS bundle (preserved in raw). Raw: research/raw/2026-08-15/glm-5-3-frontier-coding-with-emergent-cyber-capabilities/. Synthesis: research/references/open-weights-landscape-2026.md (new GLM-5.3 section, trust ladder, open question), research/references/frontier-models-2026.md (new GLM-5.3 data-points section). All figures vendor claims.

## [2026-08-15] garden | morning note 2026-08-15 (3 headlines, 4 artifacts)

Note: [[garden/2026-08-15]]. Headlines: publication boundary (CHANGELOG.md published; V7 oracle unwired), link-annotation decay across four issues, open-weights + pricing news. Artifacts: branch `garden/exclude-changelog-from-build`; `bionic/inbox/gardener-news-muse-glimmer.md`; `bionic/inbox/gardener-news-sonnet5-price-hold.md`; `bionic/inbox/gardener-idea-publication-boundary-gate.md`.

## [2026-08-15] cleanup-campsite | 1 open (0 P1, 1 P2, 0 P3), 7 closed, 0 dismissed

Top-3 P1 ids: none (no P1 findings). Sole open finding: `cleanup-CLN-ADR-1-ADR-0005`. See [[whats_next]].

## [2026-08-14] promptbook | archived PB-0001-fix-mobile-nav-and-restore-about

Final run RUN-002 completed 13/13 prompts (13 done, 0 skipped, 0 blocked-confirmed).
Forge-log evaluated fold: clean no-op (no forged skills invoked this cycle — only
plugin skills council/run-promptbook/propose-adr/transition-adr/audit-docs/log-work).
Completion summary written to the run's `summary` field; PR draft stays stored in
`pr_draft`, uncommitted at HEAD 43ab7f2 — not opened, nothing pushed. Book moved
[[promptbooks/active/PB-0001-fix-mobile-nav-and-restore-about]] ->
[[promptbooks/archive/PB-0001-fix-mobile-nav-and-restore-about]].

## [2026-08-14] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-002 to prompt 13

Prior prompt #12 (Prep: changelog, docs, journal, PR notes), outcome done — CHANGELOG.md
created (didn't exist; adaptation recorded), audit-docs gate PASSED (0 broken / 1 drift
auto-fixed / 4 warnings classified), reflective journal entry written, PR draft stored in
the run snapshot's `pr_draft` field. No PR opened, nothing pushed or committed. Current
prompt #13 (Summary: completion report AND archive the book), state running.

## [2026-08-14] audit | 0 broken, 1 drift fixed, 4 warnings

Full vault-walk (54-check; 77 md files, inline) — the PB-0001/RUN-002 Prompt 12 documentation gate.

**Fixed (drift + safe-broken):** research — `research/sources.md` row `bionic-coding-manifesto`: `static` column `n/a` → `false` (frontmatter is source of truth, CHK-RES-8).

**Pending broken:** none. The 2026-07-30 audit's three pending-broken items are all discharged (schema now `"5"`; journal corrective entry written 2026-07-30; RUN-001 hash realigned 2026-07-30 — CHK-PB-BIND recompute now matches both runs). This cycle's writes verified clean: ADR-0005 ↔ ADR-0004 supersession is bidirectional (CHK-ADR-6), ADR frontmatter/date state machine valid (CHK-ADR-1/3/5), `adrs/index.md` + `index.md` ADR rollup match frontmatter (vendored `generate-index-rollup.py --dry-run` exit 0), journal 2026-08 row correct (2 entries: decision 1, review 1), promptbook validator exit 0 on the active book + both run snapshots (cycle-coverage pass included), PB-0001 index 12/13 with RUN-002 prompt 12 `running` is a valid mid-run state. Also clean: config (`.bionic.yml`, bare prefix, no second tree), schema/inbox (`"5"`, inbox empty), log enum + order, master-index counts, research graph (22 sources / 22 raw dirs 1:1 / 4 synthesis, registry rows, wiki-links), briefs back-refs, invariants (delegated `check_invariants.py`: 0 pins, 0 checks), catalog (`validate-catalog.py --dry-run`: 0 drift), ADR template ↔ §11.A keyset equality.

**Warnings:** (1) CHK-RES-11 — 8 synthesis markers (6 contradiction, 1 unresolved, 1 source-updated) + 21 `## Capture gaps` sections; expected baseline, `refresh-research-synthesis` when wanted. (2) `whats_next.md` (generated 2026-08-02) still describes ADR-0004 as Accepted in suggestion 5 — stale since the 2026-08-14 supersession; REGENERATED artifact owned by `cleanup-campsite`, not an audit fix surface — run `cleanup-campsite` to refresh. (3) Cosmetic missing blank line between entries at `log.md:245–246` — append-only history, surfaced not fixed (same class as the 2026-07-30 note). (4) `invariants/index.md` scaffold prose still cites pre-schema-5 paths (`docs/invariants/<slug>.md`; suite "in `bionic/invariants/`" rather than `bionic/invariants/checks/`) — cosmetic, no audit check owns it; refresh on next invariants touch.

## [2026-08-14] journal | review: PB-0001/RUN-002 mobile-nav verify cycle converged after 3 review rounds

Entry in `journal/2026-08.md` at 18:12. Refs: [[promptbooks/PB-0001-fix-mobile-nav-and-restore-about]] [[adrs/ADR-0005-serve-a-landing-homepage-and-a-five-item-top-nav]]

## [2026-08-14] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-002 to prompt 12

Prior prompt #11, outcome done (fix loop converged in 3 review rounds with zero
MUST-FIX: ADR-0005 accepted / ADR-0004 superseded closing MX-1/MX-2; the
_config.yml comment rewritten true closing MX-3; README/USER_GUIDE/CLAUDE
excluded with a recorded published-file-set regression unit closing MX-4 and
S3-MF-1; rendered-output units added for every ff17186-touched file closing
CV-M1; the mobile card moved out of flow at ≤46rem, eliminating the
reflow-during-gesture retarget class — S1-M1 measured 0/9 retargets against
9/9 on the reconstructed round-2 artifact — with a real-Chrome interaction
harness recorded closing CV-M3; every loop-authored comment spot-checked
zero-false-clause; the in-flow-to-out-of-flow design change disclosed; a true
iOS WebKit device check recommended pre-merge, since both harness rounds ran
Chrome emulation only), current prompt #12.

## [2026-08-14] adr | ADR-0004: post-acceptance body edit by `ff17186` (retroactive record)

Retroactive record closing MX-2 from the PB-0001/RUN-002 external review. Commit `ff17186`
("more cleanup", 2026-07-18) edited four body lines of ADR-0004 — `index.markdown` →
`index.md` in the Decision, Consequences (Negative), Follow-on work, and References
sections — after ADR-0004 had been Accepted on 2026-07-08. An Accepted ADR's body is frozen
(`bionic/CLAUDE.md` §4/§11) and no `adr` op was written at the time. The op is recorded here
after the fact, per the review; the 2026-07-18 history is NOT edited in place, and the four
edited lines stay exactly as `ff17186` left them. Context and rationale:
[[adrs/ADR-0005-serve-a-landing-homepage-and-a-five-item-top-nav]].

## [2026-08-14] adr | ADR-0004: supersede (superseded by ADR-0005)

Single-source the manifesto homepage from research. Accepted → Superseded by ADR-0005 at
the independent acceptance gate. Frontmatter only: `status: Superseded`, `date: 2026-08-14`,
`superseded_date: 2026-08-14`, `superseded_by: ADR-0005`. Body byte-identical (verified by
hash against `HEAD`) — including the four lines `ff17186` edited post-acceptance, which are
recorded above rather than reverted. ADR-0005 already carried `supersedes: [ADR-0004]` from
drafting, so the back-pointer is now symmetric and the `audit-docs` BROKEN asymmetry
ADR-0005 anticipated is closed. Rows updated in `bionic/adrs/index.md` and `bionic/index.md`.

## [2026-08-14] adr | ADR-0005: accept (accepted)

Serve a landing homepage and a five-item top nav. Proposed → Accepted at an independent
acceptance gate (a fresh architect, not the drafting instance). Frontmatter only:
`status: Accepted`, `accepted_date: 2026-08-14`, `date: 2026-08-14`; body now frozen.
Council: MAJORITY_APPROVE at 94% consensus, all 10 dissent points drafting fixes, all
applied by the drafter and verified closed at this gate. Acceptance criterion 4 re-run
against HEAD after the `_config.yml` edit: `bundle exec jekyll clean && bundle exec jekyll
build` green, 24 HTML pages, zero pages missing `href="/about/"`, all five nav links
(`/manifesto/`, `/articles/`, `/learn/`, `/tools/`, `/about/`) present in
`_site/index.html`. Supersedes ADR-0004 (see the entry above). Closes MX-1.

## [2026-08-14] adr | ADR-0005: Serve a landing homepage and a five-item top nav

Proposed. File `bionic/adrs/ADR-0005-serve-a-landing-homepage-and-a-five-item-top-nav.md`.
Tags: information-architecture, navigation, homepage, jekyll, publication. Drafted as the
MX-1/MX-2 remedy from PB-0001/RUN-002. Records the landing-page homepage (`index.md`,
`layout: home`), the five-entry `header_pages` nav and its exact-match silent-drop failure
mode, the site title linking `/` with `manifesto.md` at `/manifesto/`, and the
repo-documentation exclusion. Also records two things that cannot be corrected in place:
`ff17186`'s unlogged post-acceptance edit to ADR-0004's frozen body, and this log's
2026-07-20 `promptbook` entry misattributing the About fix to `f8a3e82`/`a77ecf2` instead
of `ff17186`. Frontmatter carries `supersedes: [ADR-0004]`; ADR-0004 is untouched, so the
supersession is one-sided until the independent acceptance gate runs `transition-adr`.

## [2026-08-14] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-002 to prompt 11

Prior prompt #10, outcome done (conformance audit complete — 3 blind
auditors: coverage GAPS-FOUND with 2 MUST-FIX, 4 of 5 ff17186 files
uncovered and the MX-4 fix has no unit, plus 5 SHOULD-FIX incl. a
mutation-proven V1; comments/docs DRIFT-FOUND with 2 MUST-FIX, the
_config.yml comment (MX-3) and a false CLAUDE.md site-title claim, plus a
log.md:168 commit misattribution; dev-practice conformance PASS with 0
Tier-1 violations, all tokens independently reproduced, plan hash intact;
consolidated MUST-FIX list + fix/defer decisions recorded for Prompt 11),
current prompt #11.

## [2026-08-14] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-002 to prompt 10

Prior prompt #9, outcome done (external review complete — 8 blind reviewers:
3 quality dimensions + S1–S5 security fan-out with mandatory reports;
correctness PASS with all gates re-run green incl. CI-exact; consistency FAIL
on 2 MUST-FIX, both ADR-0004 — stale/contradicted decision and an unlogged
frozen-body edit; clarity FAIL on 1 MUST-FIX, a false header_pages comment;
security all N/A on the diff; 1 pre-existing MUST-FIX, README/USER_GUIDE/
CLAUDE.md reachable at the site root with no live credentials; 4 MUST-FIX
carried to Prompt 11), current prompt #10.

## [2026-08-14] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-002 to prompt 9

Prior prompt #8, outcome done (internal review verdict READY-FOR-EXTERNAL-
REVIEW: all four root causes confirmed resolved, desktop provably untouched,
CI-exact build passes closing the F3 evidence gap, no security exposure; 1
CONFIRMED-low a11y finding F2 + 3 nits deferred with rationale under the
verify-only posture; F1 iOS pointerdown carried to Prompt 11 as should-fix),
current prompt #9.

## [2026-08-14] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-002 to prompt 8

Prior prompt #7, outcome done (all quality gates green in one loop: G1–G6
recorded with exact commands + result tokens, jekyll clean/build exit 0 at 24
pages, production-overlay build exit 0 with About present; N/A gates recorded
with reasons; security analysis deferred to Prompt 9), current prompt #8.

## [2026-08-14] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-002 to prompt 7

Prior prompt #6, outcome done (verification team ran verify-only — nothing to
implement, all fixes already committed in ff17186/a77ecf2; V1–V6 executed per
plan and PASS with exact commands + verbatim result tokens; no source file
modified, G1 empty before and after), current prompt #7.

## [2026-08-14] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-002 to prompt 6

Prior prompt #5, outcome done (verification plan derived from the verified
approach: 6 verification units V1–V6 + gates G1–G6 + N/A gate reasons + risks
R1–R7 + acceptance criteria; zero code-edit units, all fixes already
committed in ff17186/a77ecf2; 5 findings carried forward to Prompt 12),
current prompt #6.

## [2026-08-14] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-002 to prompt 5

Prior prompt #4, outcome done (committed to the verify-only approach; decision
journal entry filed at bionic/journal/2026-08.md), current prompt #5.

## [2026-08-14] journal | PB-0001/RUN-002: commit to verify-only approach for the mobile-nav fix

Appended a `decision` entry to `bionic/journal/2026-08.md` (new file — first
2026-08 entry): root causes (S1 ff17186; S2/S3/toggle a77ecf2), the verify-only
approach, why it's right, and non-obvious council findings. Updated
`bionic/journal/index.md` with the new 2026-08 row.

## [2026-08-14] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-002 to prompt 4

Prior prompt #3, outcome done (council findings resolved across 2 fix-rounds;
round-3 council UNANIMOUS APPROVE, confidence 0.973, CONVERGED round 3 of 3),
current prompt #4.

## [2026-08-14] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-002 to prompt 3

Prior prompt #2, outcome done (carry-over from RUN-001), current prompt #3.

## [2026-08-14] promptbook | advanced PB-0001-fix-mobile-nav-and-restore-about/RUN-002 to prompt 2

Prior prompt #1, outcome done (carry-over from RUN-001), current prompt #2.

## [2026-08-14] promptbook | started PB-0001-fix-mobile-nav-and-restore-about/RUN-002

book_id: PB-0001, run_id: RUN-002, total_prompts: 13, current_prompt: 1.
RUN-002 carries RUN-001's completed verify work (Prompts 1–2: diagnosis +
council verdict) forward per user authorization to continue the abandoned
cycle (RUN-001 abandoned 2026-07-20 at Prompt 3).

## [2026-08-03] ingest | qwen3-8-max-a-new-bar-for-coding-and-cowork

"Qwen3.8-Max: A New Bar for Coding and Cowork" (Qwen Team, 2026-08-02).
Raw: `research/raw/2026-08-03/qwen3-8-max-a-new-bar-for-coding-and-cowork/`.
Scripted capture failed (`thin_content`, exit 2 — client-rendered SPA); body captured by headless-browser render, `rendered.html` + `rendered.md` alongside the empty `source.html`. Declared in Capture gaps.
Synthesis: [[research/references/open-weights-landscape-2026]] (Qwen section rewritten), [[research/references/frontier-models-2026]] (section rewritten, retitled from "Qwen3.8-Max-Preview — announced").
Resolves three long-open questions: 95B active params, 1M context, $2/$6 pricing. Weights deferred a third time.

## [2026-08-03] ingest | qwen3-8-max-qwencloud-model-page

"Qwen3.8-Max — QwenCloud model page" (serving page, captured 2026-08-03).
Raw: `research/raw/2026-08-03/qwen3-8-max-qwencloud-model-page/`.
Synthesis: same two references pages — supplies the pricing, context, and rate-limit figures the launch post omits.

## [2026-08-01] cleanup-campsite | 7 open (0 P1, 7 P2, 0 P3), 1 closed, 0 dismissed

No P1 findings — first clean-P1 run since 2026-07-20. See [[whats_next]].
New this run: 2 × CLN-ADR-3 on ADR-0004, both `docs/` paths the schema 4→5 migration relocated to `bionic/`.
Closed: `cleanup-CLN-AUD-1-recency` (audit ran 2026-07-30). Note that run left 3 BROKEN findings pending — an audit-docs question, outside cleanup's remit.

## [2026-08-01] ingest | willison-kimi-k3, willison-inkling, raschka-notable-open-weight-models, state-of-open-source-local-llms-july-2026, qwen3-8-open-weight-announcement

Five open-weights sources from the gardener's 2026-07-30 read-news pass (four inbox items; the Willison item carried two URLs and was split into two source pages).
Raw: research/raw/2026-08-01/{willison-kimi-k3,willison-inkling,raschka-notable-open-weight-models,state-of-open-source-local-llms-july-2026,qwen3-8-open-weight-announcement}/
Synthesis: NEW research/references/open-weights-landscape-2026.md (8 sources); updated research/references/frontier-models-2026.md (K3 pricing $3/$15 and Jul 16 date resolved; Qwen 3.8 second capture, still no benchmarks).
Contradictions flagged: LLMCheck's Kimi K3 row (~1T-A32B / Jul 7 / 2M context / 66% SWE-Bench Pro) contradicts Moonshot's technical report and Willison on all four figures — technical report preferred, LLMCheck spec tables discounted. K3 announcement date differs across three sources (Jul 7 / 16 / 17); Willison's same-day Jul 16 preferred.
Open: whether K3 weights shipped by the promised 2026-07-27 is unconfirmed — Raschka on Jul 26 still reports them pending.

## [2026-07-31] schema | close out the 4→5 migration follow-ups (Jekyll exclude, root CLAUDE.md, bionic/CLAUDE.md refresh)

Discharged the three stale-reference follow-ups the `[2026-07-30] schema | migrate docs schema 4→5` entry below left open, using the 1.8.0 plugin copy at `~/.claude/plugins/cache/crux/crux/1.8.0/` (the `~/.local/share/crux/` copy is a stale 1.7.0 clone). (1) `_config.yml`'s Jekyll `exclude:` list: `docs/` → `bionic/`, so the 66 management-tree `.md` files stop being built as site content (`_config_production.yml` carries no `docs/` reference, needed no change); verified `bundle exec jekyll build --config _config.yml,_config_production.yml` succeeds and `_site/bionic/` does not exist. (2) Repo-root `CLAUDE.md` (outside the docs tree): two path fixes, `` `docs/CLAUDE.md` `` → `` `bionic/CLAUDE.md` `` and `` `docs/briefs/BRIEF-this-week-in-ai-format.md` `` → `` `bionic/briefs/BRIEF-this-week-in-ai-format.md` ``; nothing else changed. (3) `bionic/CLAUDE.md`: re-rendered from the 1.8.0 `templates/CLAUDE.md.tmpl` ({{repo_name}} → bionic-coding, {{today}} → 2026-07-31 — the only two canonical substitutions per the installed `init-docs` SKILL.md), preserving the one prior project-specific addition found (the ADR-0044 citation in §14, absent from both the 1.7.0 and 1.8.0 templates). The 1.8.0 template itself carries known-stale prose the code contradicts, corrected here rather than copied verbatim: (a) §7's schema-version history mislabeled `"4"` as **current** while its own predicate already checked `schema_version == "5"`, and the ladder had no `"5"` rung at all — added a `"5"` bullet (current) describing the real `migrate-tree.py` 4→5 rung (flat merge of `docs/` + the bare invariants-only `bionic/` onto one `bionic/` root, ledger pages take the top-level `bionic/invariants/*.md` namespace, pre-existing checks pushed down into `bionic/invariants/checks/` first, `.bionic.yml` `docs_dir` rewritten to `bionic`), and demoted `"4"`'s bullet to non-current; (b) §14's `.bionic.yml` note and §15.1 both said relocating the ledger onto `bionic/` "is deferred" via a nested `bionic/docs/` path that `migrate-tree.py` never produces — corrected to describe the real flat-merge mechanism and noted this repo has already run that rung (`docs_dir: bionic`, `schema_version: "5"`). All `<tree>` literal placeholders (template bug — appears verbatim 6 times, never templated) resolved to the constant `bionic` (`migrate-tree.py`'s `DEFAULT_TREE`), giving `bionic/invariants/checks/` throughout. Left everything else's `docs/` spelling as the template ships it, per §14.2's own normative clause (a literal `docs/` segment denotes `<docs_dir>/`; `init-docs` only ever substitutes `{{repo_name}}`/`{{today}}`, confirmed against the installed `skills/init-docs/SKILL.md` step 5/7). Also fixed `bionic/invariants/reconciliation.yml`'s two header-comment cross-references (`docs/CLAUDE.md` → `bionic/CLAUDE.md`, §15.4 and §15.3); `checks: []` data untouched. Verification: diffed the new `bionic/CLAUDE.md` against a template-plus-substitution baseline — every remaining delta traces to one of the corrections listed above or the preserved ADR-0044 sentence; schema-version mentions are internally consistent (`"5"` current everywhere) after the edit; final repo-root `grep -rn "docs/"` sweep (excluding `_site/`, `.jekyll-cache/`, `.git/`, and `bionic/journal/` + `bionic/log.md` historical entries, which correctly narrate the pre-migration path) turned up no other live references to the retired `docs/` tree.

## [2026-07-30] schema | migrate docs schema 4→5 (docs/ → bionic/, invariants unified)

Ran the crux 1.8.0 `audit-docs --migrate` 4→5 rung via `migrate-tree.py` directly (the installed 1.8.0 `audit-docs` SKILL.md's `--migrate` ladder section is stale — it still only documents the 2→3 and 3→4 rungs, not this one — so the script + its test suite were treated as authoritative per the task's explicit guidance). Staged, resumable migration (marker at `bionic/.migrating`, deleted on clean completion — no interruption occurred here, it completed in one pass): (1) unified the invariants concern by clearing the check namespace under `bionic/invariants/` (moving any loose `.md` checks into `bionic/invariants/checks/`) before the ledger arrived — zero candidate checks existed, so this was a no-op move; (2) merged every other `docs/` entry into `bionic/` (`shutil.move`, directory-recurse on collision, refuse-loud on genuine collision — none occurred); (3) moved `docs/manifest.yml` to `bionic/manifest.yml` last (discovery's key); (4) merged `.bionic.yml` (`docs_dir: docs` → `docs_dir: bionic`, `artifact_prefix: ""` preserved — never overwritten); (5) bumped `manifest.yml` `schema_version` `"4"` → `"5"`; (6) removed the emptied `docs/` tree, then the marker. `moved: 13` (the invariants-suite entries + top-level dirs not already merged by the recurse step; most of the 227 pre-existing `docs/` files landed via the directory-recurse `merge_entry` path rather than the counted top-level `moved` list).

**Verification — full before/after file inventory, zero loss:** 227 files under `docs/` (66 `.md`) + 1 file under `bionic/` (`invariants/reconciliation.yml`) before = 228 total; 228 files under `bionic/` after (66 `.md`), confirmed by a full path-diff (docs/X ↔ bionic/X, invariants unification accounted for) — 0 missing, 0 extra. `git add -A` showed 227 renames + 1 modify (`.bionic.yml`, 100%/98% similarity respectively) — no adds/deletes, confirming git tracked the relocation as moves, not delete+recreate.

**Post-migration audit (1.8.0 tooling, schema 5):** `bionic-config.py` resolves `docs_dir: bionic`, `source: ".bionic.yml"`. `validate-catalog.py --dry-run`: clean (0 added/changed/removed). `validate-promptbook.py --kind promptbook|run` on `PB-0001`'s active book + `RUN-001` snapshot: both exit 0. `check_invariants.py --root . --docs-dir bionic`: `{"broken": [], "warning": [], "survey_debt": 0, "pins": 0}` — consistent with the scaffold-only invariants state (0 pins, 0 checks). Manual walk of the remaining CHK-* groups (config, master index/log, schema/inbox, ADRs, briefs, research, promptbooks, journal) inline (66 md files, under the 100-file Explore-agent threshold): `bionic/index.md` rollup counts (ADRs 5, briefs 2, journal 1 month, promptbooks 1 active/0 archived, invariants 0) all match disk; ADR numbering 0000-0004 contiguous, `adr.next_number: 5` correct; `related_research` references resolve; `bionic/promptbooks/index.md` and `bionic/journal/index.md` rollups match; `bionic/research/sources.md` (15 rows + header) matches 15 source pages, 23 raw dirs. No dangling wiki-links found (none used a literal `docs/` path segment — all were already docs_dir-relative per §14.2). CHK-SCHEMA-1 now reads `"5"` — the 1.8.0-supported value.

**Left for a follow-up (not touched here, per task scope):** root `CLAUDE.md` (repo root, outside the docs tree) still says `` `docs/CLAUDE.md` `` and cites `` `docs/briefs/BRIEF-this-week-in-ai-format.md` ``; `_config.yml`'s Jekyll `exclude:` list still excludes `docs/` (now the wrong path — `bionic/` is unexcluded and will be processed as site content until fixed); `bionic/CLAUDE.md` and `bionic/invariants/reconciliation.yml`'s header comments still narrate the pre-migration schema-4 state (`docs/invariants/`, `schema_version: "4"` prose) — regeneratable-adjacent prose, deliberately left for the human-approved refresh the task called out as a separate step.

## [2026-07-30] journal | corrective entry for the ec2e7b9 heading overwrite

User-authorized fix for pending-broken finding #2 from the `[2026-07-30] audit` entry below. Appended a new `## [2026-07-30 23:20] bug | ...` heading to `docs/journal/2026-07.md` (5th heading; verified 4→5, no existing heading clobbered) documenting that commit `ec2e7b9` ("qwen 3.8") overwrote the `## [2026-07-17 17:17] implementation | Processed the 2026-07-17 gardener inbox...` heading with the `## [2026-07-20 09:16] misc | Triaged...` heading still in place today. Reconstructed the split via `git show 4f9cee5:docs/journal/2026-07.md` (pre-overwrite text) + corroboration from the `[2026-07-17] journal` entry below: attributed which surviving paragraphs are genuinely 2026-07-20 vs. the orphaned 2026-07-17 body (order-4 fix + link-checker merge). No history rewritten — append-only preserved. `docs/journal/index.md` rollup: entries 4→5, category tally adds `bug (1)`.

## [2026-07-30] promptbook | realigned RUN-001's book_content_hash (CHK-PB-BIND)

User-authorized fix for pending-broken finding #3 from the `[2026-07-30] audit` entry below. Recomputed `PB-0001`'s frozen-plan hash with the installed plugin's current `validate-promptbook.py` `compute_book_hash` (crux v1.7.0, via `uv run`): got `sha256:878bedef3fd2fe2021000387caa850e2fe842190f45d75b2d36ca5474a290c3c` against both the current book and the run-creation-time book (commit `4f9cee5`) — identical, since git history shows only `current_run`/`current_prompt` (excluded from the frozen-plan subset) changed post-creation across `6432043` and `ec2e7b9`. This confirms writer-vs-validator hash-algorithm drift, not an in-place plan edit / §4 fork-rule violation. Per the `migrate-promptbooks` precedent, updated `docs/promptbooks/runs/PB-0001-fix-mobile-nav-and-restore-about/run-RUN-001.yaml` `book_content_hash` from the stale `sha256:2f4f88ffd96aae68dc5834f0d9fee280f7d2705a9f0beed26543ea0ddb88fd89` to the recomputed value, and appended a `## Hash realignment` section to the run's `notes` field documenting the investigation. Re-ran CHK-PB-BIND (recompute vs. stored): now PASS. Re-validated both files against `validate-promptbook.py` schema: exit 0.

## [2026-07-30] schema | refresh docs/CLAUDE.md to schema "4" (§14 `.bionic.yml`, §15 invariants, ADR-0044)

Discharges the deferred follow-up noted in the two entries below: `docs/CLAUDE.md` still carried pre-migration (schema "3") prose after both the 3→4 migration and the invariants-concern opt-in. Rewrote it wholesale against the installed plugin's current `templates/CLAUDE.md.tmpl` (crux v1.7.0) — the template is the SSOT for this file; no hand-authored bionic-coding-specific prose existed to preserve beyond the repo name (confirmed by diffing the prior render against the template: every delta was mechanical/version-driven, none project-specific). Changes: "six concerns" → "seven" (adds **invariants**, §1); new §14 "Per-repo configuration — the repo-root `.bionic.yml` file (superseding the legacy `.crux`)" replacing the old bare `.crux`-only §14, with the `.bionic.yml` > `.crux` > convention precedence, `bionic-config.py` CLI, and a grounded parenthetical citing the plugin's own ADR-0044 (per `bionic_config.py`/`crux-config.py`/`crux_config.py` docstrings) for the rename rationale; new §15 "The invariants concern" (pin/ledger/check model, ratification safety invariant, reconciliation manifest, CHK-INV-* rules); `${CLAUDE_PLUGIN_ROOT}` → `${CRUX_PLUGIN_ROOT}` throughout (the portable Claude Code/Codex bridge name) with one exception left as explanatory prose (§7.A, defining the bridge itself); §7 `schema_version` example bumped `"3"` → `"4"` with `invariants` added to the example `concerns_enabled` list (matches this repo's actual current state — invariants was enabled by the entry below, dated the same day); `promptbook` op enum gained `invariant`; several small additive template updates (Codex marketplace mention in §1, `template-parity` whats_next category, lifecycle-neutral promptbook citation form in §9/§11). Verified: diffed the rewritten file byte-for-byte against a `{{repo_name}}`→`bionic-coding`/`{{today}}`→2026-07-30 substitution of the template — identical. No unresolved `{{...}}` placeholders remain (one residual literal `CLAUDE_PLUGIN_ROOT` string is intentional, inside the runtime-mapping prose). `docs/CLAUDE.md` is excluded from the concern-section walk (like `README.md`), so no `docs/index.md` change was needed.

## [2026-07-30] schema | enable invariants concern (scaffold-only, user-confirmed)

Follow-up to the 3→4 migration below: user confirmed opt-in for the `invariants` concern left DISABLED at that rung. `docs/manifest.yml`: added `invariants` to `concerns_enabled` (`schema_version` unchanged, still `"4"`); migration-note comment updated to point here instead of describing a pending decision. Created the empty surfaces per `docs/CLAUDE.md` §15 / the plugin's rung-3→4 spec, nothing else: ledger dir `docs/invariants/` (+ `index.md`, 0 pins) and the peer check suite `bionic/invariants/` (+ `reconciliation.yml`, `checks: []`). Also created the repo-root `.bionic.yml` (config_version 1, `docs_dir: docs`, `artifact_prefix: ""` — identical to the pre-existing zero-config defaults; `bionic-config.py` reported `source: "defaults"` before this write) to formalize layout config now that a `bionic/` durable root exists. **No legacy `.crux` file existed in this repo** — checked via `bionic-config.py` (`source: "defaults"`, no file found) before writing; there was nothing to supersede per ADR-0044, so this is a fresh write, not a migration. `docs/index.md` gained `## Invariants (0)` (CHK-MI-1 requires a section per enabled concern regardless of count) linking to `[[invariants/index]]`; `_Last updated:` already `2026-07-30`. **Scaffold-only, no mining performed**: zero pins, zero checks — `recover-invariants` populates the ledger later, always as `provenance: recovered, ratification: observed`; a human ratifies via `transition-invariant`. Verification: `docs/manifest.yml` parses (`python3 -c 'import yaml'`), `schema_version` still `"4"`, `docs/invariants/index.md` is the only new file under `docs/` (65 → 66 `.md` files under `docs/`; `bionic/invariants/reconciliation.yml` and `.bionic.yml` are outside `docs/` and don't count toward that figure), all 65 pre-existing `docs/` files untouched (only `manifest.yml`, `index.md`, and `log.md` edited, each additively). `docs/CLAUDE.md` in this repo still carries pre-migration (schema "3") prose (no §14/§15) — unchanged here, same deferred-follow-up noted in the entry below.

## [2026-07-30] schema | migrate docs schema 3→4 (invariants concern added, disabled)

Ran the `audit-docs --migrate` 3→4 rung (the only implemented rung needed; tree was already past 2→3 with `docs/inbox/` present and `docs/research/new/` absent). Installed plugin: crux v1.7.0, supports `docs/manifest.yml` `schema_version == "4"` (per the plugin's own `audit-docs`/`templates/manifest.yml.tmpl`; note `install-docs-skills`' bundled prose is stale and still cites `"3"` — a plugin-internal doc-drift, not a tree problem). `docs/manifest.yml`: `schema_version: "3"` → `"4"`. **`invariants` left DISABLED** — this repo has no `bionic/` layout and no user confirmation was given to opt in, so per the rung's opt-in rule the concern stays available-but-not-enabled; no `docs/invariants/` ledger or `bionic/invariants/` suite was created. **No docs-tree relocation performed or needed**: the plugin's current template (`docs/CLAUDE.md` §15.1 in the shipped `CLAUDE.md.tmpl`) explicitly defers the `docs/invariants/` → `bionic/docs/invariants/` ledger relocation — it is not part of this rung. `docs/CLAUDE.md` in this repo still reflects the pre-migration (schema "3") schema prose (no §14/§15, no ADR-0044/`.bionic.yml` mention); refreshing it against the current template is a separate, human-confirmed follow-up, not performed here. File count unchanged: 65 `.md` files before and after (only `manifest.yml` and `log.md` were touched). Verification: re-ran the audit checklist inline — CHK-SCHEMA-1 now passes (`"4"`), CHK-INBOX-1/2/3 unaffected (inbox already present, `research/new/` already absent, 4 items still pending), all pre-existing counts/indexes unchanged. Pre-existing pending-broken findings from the 2026-07-30 audit entry below (journal append-only violation, CHK-PB-BIND hash mismatch) are untouched by this migration — still open, still requiring separate user decisions.

## [2026-07-30] audit | 3 broken (pending), 1 drift fixed, 3 warnings

Full vault-walk (54-check, inline; 65 md files) since the 2026-07-13 baseline. **Fixed:** `docs/journal/index.md` — entries count corrected 4→3 for 2026-07 (root cause: commit `ec2e7b9` overwrote a heading rather than adding one; see pending-broken #2). **Pending broken:** (1) CHK-SCHEMA-1 — `docs/manifest.yml` `schema_version: "3"`, but the installed plugin supports `"4"` (confirmed via `recover-invariants`/`transition-invariant` present in `catalog/skills.json`); decide whether to run `audit-docs --migrate` (3→4 rung, invariants concern opt-in). (2) Journal append-only violation — commit `ec2e7b9` ("qwen 3.8", 2026-07-20) overwrote the heading `## [2026-07-17 17:17] implementation | Processed the 2026-07-17 gardener inbox — order fix, next-issue queue, link-checker merge` in `docs/journal/2026-07.md` with a new `## [2026-07-20 09:16] misc | Triaged...` heading; the original body text survives but is now misattributed to the wrong date/category. Corroborated by this log's own `[2026-07-17] journal` entry, which describes the lost heading's content. Recommend a corrective journal entry, not a silent rewrite. (3) CHK-PB-BIND — `PB-0001`/`RUN-001`'s stored `book_content_hash` does not match the recomputed frozen-plan hash; git history shows no in-place plan edit (only `current_run`/`current_prompt` changed), so this looks like a hash-algorithm/writer-vs-validator version drift in the plugin rather than a fork-rule violation — never auto-fixed regardless. **Warnings:** 4 items pending in `docs/inbox/` (gardener news drops from 2026-07-30, awaiting `process-inbox`); 14 research source pages carry `## Capture gaps` (expected, growing baseline); a cosmetic missing-blank-line + a prior em-dash-normalization touch in append-only history (`docs/log.md` line ~27, `docs/journal/2026-07.md` commit `4f9cee5`) — not fixed, append-only. Everything else clean: research (15 sources / 15 raw dirs / 3 synthesis, frontmatter + `sources.md` + wiki-links all resolve, 0 contradiction/unresolved markers); ADRs (5, contiguous, template↔schema keyset match, supersession N/A, `next_number` correct); briefs (2, both published); promptbooks (`PB-0001` schema-valid, `total_prompts` correct, index counts correct); catalog (`validate-catalog.py --dry-run` exit 0, 0 drift); `docs/index.md` counts + `_Last updated:` correct; `log.md` op-enum + reverse-chron order valid; cfg (bare-prefix tree, no split-tree, no config file present — defaults).

## [2026-07-30] cleanup-campsite | 6 open (1 P1, 5 P2, 0 P3), 0 closed, 0 dismissed

Top-3 P1 ids: `cleanup-CLN-AUD-1-recency`. New P1 this run: last audit was 2026-07-13 (17 days, > 14-day threshold) — audit-docs is overdue. The 5 CLN-ADR-1 P2s (ADR-0000 through ADR-0004 not linked from README/USER_GUIDE) are unchanged since 2026-07-13, still optional for a content site. No Proposed ADRs; PB-0001 has no active `current_run` (dormant since its 2026-07-20 abandonment, not stuck); no journal gaps in the last 7 days; retro not due (0 books ever archived). See [[whats_next]].

## [2026-07-21] ingest | kimi-k3-technical-report

"Kimi K3: Open Frontier Intelligence — Technical Report" (Kimi Team / Moonshot, 47pp) — PDF dispatched from `docs/inbox/` by process-inbox. Raw: `research/raw/2026-07-21/kimi-k3-technical-report/` (PDF + full `pdftotext` extraction, `static: true`). **Closes both open gaps on [[research/sources/kimi-k3-docs]]**: activated params (**104B of 2.8T**) and the benchmark table (Figure 1, transcribed). Notable: Moonshot's own abstract states K3 "still trails … Claude Fable 5 and GPT-5.6 Sol," walking back the earlier platform-docs marketing framing. Synthesis: [[research/references/frontier-models-2026]] Kimi section rewritten from "announced" to "SHIPPED"; intro reframed so Qwen3.8 is now the only announcement-only entry; now 12 sources. Added a resolved-by pointer to the older kimi-k3-docs capture gaps. No new category; no contradictions (the softer self-assessment supersedes, not contradicts, the marketing claim).

## [2026-07-21] ingest | claude-opus-5-system-card

"System Card: Claude Opus 5" (Anthropic, 194pp, card dated 2026-07-24) — PDF dispatched from `docs/inbox/` by process-inbox. Raw: `research/raw/2026-07-21/claude-opus-5-system-card/` (PDF + full `pdftotext` extraction, `static: true`). Source page carries Executive Summary, §1, §8.1 table, §8.2 verbatim; §§2–7 + 8.3–9 left to `raw/source.txt` (declared capture gap). Synthesis: [[research/references/frontier-models-2026]] gains a **Claude Opus 5** section as the current Opus flagship (4.8 retitled "predecessor"), now 11 sources, `last_reviewed: 2026-07-21`. Key: ASL-3, most-aligned-to-date, SWE-bench Verified 96.0; hallucinates slightly more than 4.8 despite higher accuracy. No new category; no contradictions.

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
