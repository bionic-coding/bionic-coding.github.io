---
generated_at: 2026-07-30T22:42:16Z
generator: cleanup
generator_version: "1.7.0"
scan_findings: 6
suggestions_open: 6
suggestions_dismissed_carried: 0
dismissed: []
---

# What's next

_Generated 2026-07-30 22:42 by `cleanup-campsite` v1.7.0. **Body regenerated end-to-end on every run; only the `dismissed:` frontmatter list persists.** Hand-edits below the frontmatter are blown away. To dismiss a suggestion, move its `id:` into the `dismissed:` frontmatter list with a `reason:`._

## Open suggestions (6)

### 1. [P1] audit-docs is overdue
- **id:** `cleanup-CLN-AUD-1-recency`
- **category:** whats-next-stale
- **severity:** P1
- **finding:** Last `audit` log entry is `## [2026-07-13] audit | 1 broken (pending), 0 drift fixed, 2 warnings` — 17 days ago, past the 14-day `audit_stale_days` threshold. No audit has run since.
- **source:** scan rule `CLN-AUD-1` against `docs/log.md`
- **proposed action:** Run `audit-docs` to check graph integrity — schema, frontmatter, cross-refs, indexes, and rollups across all enabled concerns. The 2026-07-13 run also left 1 broken finding marked "pending"; confirm whether it was ever resolved.
- **refs:** [[log]]

### 2. [P2] ADR-0000 not referenced in human-facing docs
- **id:** `cleanup-CLN-ADR-1-ADR-0000`
- **category:** adr-review
- **severity:** P2
- **finding:** `ADR-0000` (Accepted 2026-07-07) is not mentioned by id in `README.md` or `USER_GUIDE.md`. Unchanged since the 2026-07-13 run.
- **source:** scan rule `CLN-ADR-1` against `docs/adrs/index.md`, `README.md`, `USER_GUIDE.md`
- **proposed action:** Optional for a content site — mention `[[adrs/ADR-0000-record-architecture-decisions]]` in `USER_GUIDE.md` if you want the decision trail discoverable, or dismiss if README/ADR cross-linking isn't a goal here.
- **refs:** [[adrs/ADR-0000-record-architecture-decisions]]

### 3. [P2] ADR-0001 not referenced in human-facing docs
- **id:** `cleanup-CLN-ADR-1-ADR-0001`
- **category:** adr-review
- **severity:** P2
- **finding:** `ADR-0001` (Accepted 2026-07-08) is not mentioned by id in `README.md` or `USER_GUIDE.md`. Unchanged since the 2026-07-13 run.
- **source:** scan rule `CLN-ADR-1` against `docs/adrs/index.md`, `README.md`, `USER_GUIDE.md`
- **proposed action:** Optional for a content site — link it from `USER_GUIDE.md` §build/tooling, or dismiss.
- **refs:** [[adrs/ADR-0001-use-jekyll-4-4-with-ruby-pinned-to-4-0-5]]

### 4. [P2] ADR-0002 not referenced in human-facing docs
- **id:** `cleanup-CLN-ADR-1-ADR-0002`
- **category:** adr-review
- **severity:** P2
- **finding:** `ADR-0002` (Accepted 2026-07-08) is not mentioned by id in `README.md` or `USER_GUIDE.md`. Unchanged since the 2026-07-13 run.
- **source:** scan rule `CLN-ADR-1` against `docs/adrs/index.md`, `README.md`, `USER_GUIDE.md`
- **proposed action:** Optional for a content site — link it from `USER_GUIDE.md` §deploy, or dismiss.
- **refs:** [[adrs/ADR-0002-deploy-to-github-pages-via-github-actions]]

### 5. [P2] ADR-0003 not referenced in human-facing docs
- **id:** `cleanup-CLN-ADR-1-ADR-0003`
- **category:** adr-review
- **severity:** P2
- **finding:** `ADR-0003` (Accepted 2026-07-08) is not mentioned by id in `README.md` or `USER_GUIDE.md`. Unchanged since the 2026-07-13 run.
- **source:** scan rule `CLN-ADR-1` against `docs/adrs/index.md`, `README.md`, `USER_GUIDE.md`
- **proposed action:** Optional for a content site — link it from `USER_GUIDE.md` §presentation, or dismiss.
- **refs:** [[adrs/ADR-0003-ship-a-custom-presentation-layer-over-minima]]

### 6. [P2] ADR-0004 not referenced in human-facing docs
- **id:** `cleanup-CLN-ADR-1-ADR-0004`
- **category:** adr-review
- **severity:** P2
- **finding:** `ADR-0004` (Accepted 2026-07-08) is not mentioned by id in `README.md` or `USER_GUIDE.md`. Unchanged since the 2026-07-13 run.
- **source:** scan rule `CLN-ADR-1` against `docs/adrs/index.md`, `README.md`, `USER_GUIDE.md`
- **proposed action:** Optional for a content site — link it from `USER_GUIDE.md` §content-plan, or dismiss.
- **refs:** [[adrs/ADR-0004-single-source-the-manifesto-homepage-from-research]]

## Recently closed (since last run)
- (none — all 5 CLN-ADR-1 findings from the prior run remain open; CLN-AUD-1 is a new finding this run, not a closure.)
