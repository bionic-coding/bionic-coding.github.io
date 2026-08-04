---
generated_at: 2026-08-02T04:25:08Z
generator: cleanup
generator_version: "1.8.1"
scan_findings: 7
suggestions_open: 7
suggestions_dismissed_carried: 0
dismissed: []
---

# What's next

_Generated 2026-08-01 22:25 by `cleanup-campsite` v1.8.1. **Body regenerated end-to-end on every run; only the `dismissed:` frontmatter list persists.** Hand-edits below the frontmatter are blown away. To dismiss a suggestion, move its `id:` into the `dismissed:` frontmatter list with a `reason:`._

## Open suggestions (7)

### 1. [P2] ADR-0000 not referenced in human-facing docs
- **id:** `cleanup-CLN-ADR-1-ADR-0000`
- **category:** adr-review
- **severity:** P2
- **finding:** `ADR-0000` (Accepted 2026-07-07) is not mentioned by id in `README.md` or `USER_GUIDE.md`. No ADR id appears in any human-facing doc. Unchanged across the last four cleanup runs.
- **source:** scan rule `CLN-ADR-1` against `bionic/adrs/index.md`, `README.md`, `USER_GUIDE.md`
- **proposed action:** Optional for a content site — mention `[[adrs/ADR-0000-record-architecture-decisions]]` in `USER_GUIDE.md` if you want the decision trail discoverable, or dismiss if README/ADR cross-linking isn't a goal here. **Four runs unchanged: dismissing the five as a group is the cheaper resolution.**
- **refs:** [[adrs/ADR-0000-record-architecture-decisions]]

### 2. [P2] ADR-0001 not referenced in human-facing docs
- **id:** `cleanup-CLN-ADR-1-ADR-0001`
- **category:** adr-review
- **severity:** P2
- **finding:** `ADR-0001` (Accepted 2026-07-08) is not mentioned by id in `README.md` or `USER_GUIDE.md`. Unchanged across the last four cleanup runs.
- **source:** scan rule `CLN-ADR-1` against `bionic/adrs/index.md`, `README.md`, `USER_GUIDE.md`
- **proposed action:** Optional for a content site — link it from `USER_GUIDE.md` §build/tooling, or dismiss.
- **refs:** [[adrs/ADR-0001-use-jekyll-4-4-with-ruby-pinned-to-4-0-5]]

### 3. [P2] ADR-0002 not referenced in human-facing docs
- **id:** `cleanup-CLN-ADR-1-ADR-0002`
- **category:** adr-review
- **severity:** P2
- **finding:** `ADR-0002` (Accepted 2026-07-08) is not mentioned by id in `README.md` or `USER_GUIDE.md`. Unchanged across the last four cleanup runs.
- **source:** scan rule `CLN-ADR-1` against `bionic/adrs/index.md`, `README.md`, `USER_GUIDE.md`
- **proposed action:** Optional for a content site — link it from `USER_GUIDE.md` §deploy, or dismiss.
- **refs:** [[adrs/ADR-0002-deploy-to-github-pages-via-github-actions]]

### 4. [P2] ADR-0003 not referenced in human-facing docs
- **id:** `cleanup-CLN-ADR-1-ADR-0003`
- **category:** adr-review
- **severity:** P2
- **finding:** `ADR-0003` (Accepted 2026-07-08) is not mentioned by id in `README.md` or `USER_GUIDE.md`. Unchanged across the last four cleanup runs.
- **source:** scan rule `CLN-ADR-1` against `bionic/adrs/index.md`, `README.md`, `USER_GUIDE.md`
- **proposed action:** Optional for a content site — link it from `USER_GUIDE.md` §presentation, or dismiss.
- **refs:** [[adrs/ADR-0003-ship-a-custom-presentation-layer-over-minima]]

### 5. [P2] ADR-0004 not referenced in human-facing docs
- **id:** `cleanup-CLN-ADR-1-ADR-0004`
- **category:** adr-review
- **severity:** P2
- **finding:** `ADR-0004` (Accepted 2026-07-08) is not mentioned by id in `README.md` or `USER_GUIDE.md`. Unchanged across the last four cleanup runs.
- **source:** scan rule `CLN-ADR-1` against `bionic/adrs/index.md`, `README.md`, `USER_GUIDE.md`
- **proposed action:** Optional for a content site — link it from `USER_GUIDE.md` §content-plan, or dismiss.
- **refs:** [[adrs/ADR-0004-single-source-the-manifesto-homepage-from-research]]

### 6. [P2] ADR-0004 cites a raw-capture path the schema 5 migration moved
- **id:** `cleanup-CLN-ADR-3-ADR-0004-docs-research-raw-2026-07-07-bionic-coding-manifesto-manifesto-md`
- **category:** adr-followon
- **severity:** P2
- **finding:** ADR-0004's body cites `docs/research/raw/2026-07-07/bionic-coding-manifesto/manifesto.md` in prose. That path no longer exists — the schema 4→5 migration (2026-07-30) moved the tree to `bionic/`, so the file now lives at `bionic/research/raw/2026-07-07/bionic-coding-manifesto/manifesto.md`. **New this run**: the migration created the drift, and this is the first cleanup pass since it landed.
- **source:** scan rule `CLN-ADR-3` against `bionic/adrs/ADR-0004-single-source-the-manifesto-homepage-from-research.md`
- **proposed action:** **Do not edit the ADR body — it is frozen after Accepted.** Two defensible options: (a) treat it as covered by the `docs/CLAUDE.md` §14.2 normative-definition clause, which makes a literal `docs/` segment denote `<docs_dir>/` — but note that clause names skills, agent definitions, and templates, not ADR bodies, so relying on it here is an extension; or (b) write a short brief recording that ADR-0000–0004 bodies carry pre-migration `docs/` paths and that the reader should resolve them against `bionic/`. Option (b) is the cleaner audit trail and covers every ADR at once.
- **refs:** [[adrs/ADR-0004-single-source-the-manifesto-homepage-from-research]] [[research/sources/bionic-coding-manifesto]]

### 7. [P2] ADR-0004 cites a source-page path the schema 5 migration moved
- **id:** `cleanup-CLN-ADR-3-ADR-0004-docs-research-sources-bionic-coding-manifesto-md`
- **category:** adr-followon
- **severity:** P2
- **finding:** ADR-0004's body cites `docs/research/sources/bionic-coding-manifesto.md` in prose. Same cause as finding 6 — the file is now at `bionic/research/sources/bionic-coding-manifesto.md`. **New this run.**
- **source:** scan rule `CLN-ADR-3` against `bionic/adrs/ADR-0004-single-source-the-manifesto-homepage-from-research.md`
- **proposed action:** Same as finding 6 — resolve both together. **Do not edit the ADR body.**
- **refs:** [[adrs/ADR-0004-single-source-the-manifesto-homepage-from-research]] [[research/sources/bionic-coding-manifesto]]

## Recently closed (since last run)
- ~~`cleanup-CLN-AUD-1-recency`~~ — addressed 2026-07-30 (condition no longer reproduces). `audit-docs` ran 2026-07-30, 2 days ago, inside the 14-day `audit_stale_days` window. **Caveat carried forward, not a cleanup finding:** that run logged `3 broken (pending), 1 drift fixed, 3 warnings`. Recency is satisfied; whether those three BROKEN findings were resolved is an `audit-docs` question, not one this rule can answer.
