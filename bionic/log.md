# Operations log

_Append-only. Newest first._

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
