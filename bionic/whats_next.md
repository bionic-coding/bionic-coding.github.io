---
generated_at: 2026-08-15T18:08:49Z
generator: cleanup
generator_version: "1.8.2"
scan_findings: 1
suggestions_open: 1
suggestions_dismissed_carried: 0
dismissed: []
---

# What's next

_Generated 2026-08-15 12:08 by `cleanup-campsite` v1.8.2. **Body regenerated end-to-end on every run; only the `dismissed:` frontmatter list persists.** Hand-edits below the frontmatter are blown away. To dismiss a suggestion, move its `id:` into the `dismissed:` frontmatter list with a `reason:`._

## Open suggestions (1)

### 1. [P2] ADR-0005 not referenced in human-facing docs
- **id:** `cleanup-CLN-ADR-1-ADR-0005`
- **category:** adr-review
- **severity:** P2
- **finding:** `ADR-0005` (Accepted 2026-08-14) is not mentioned by id in `README.md` or `USER_GUIDE.md`. No ADR id appears in any human-facing doc. This is the same shape as the four ADR-0000..0003 findings that just aged out of the 30-day window — the pattern recurs on every acceptance because the repo has never cross-linked decisions into its human-facing docs.
- **source:** scan rule `CLN-ADR-1` against `bionic/adrs/index.md`, `README.md`, `USER_GUIDE.md`
- **proposed action:** ADR-0005 governs the homepage and the five-item top nav — the most user-visible decision on the site. Mention `[[adrs/ADR-0005-serve-a-landing-homepage-and-a-five-item-top-nav]]` in `USER_GUIDE.md` where navigation and page structure are described, or dismiss this id if README/ADR cross-linking is not a goal for a content site. Dismissing once ends the recurrence for this id only; the next accepted ADR raises a fresh one.
- **refs:** [[adrs/ADR-0005-serve-a-landing-homepage-and-a-five-item-top-nav]]

## Recently closed (since last run)

- ~~`cleanup-CLN-ADR-1-ADR-0000`~~ — addressed 2026-08-15 (condition no longer reproduces). Accepted 2026-07-07, now outside the rule's 30-day window.
- ~~`cleanup-CLN-ADR-1-ADR-0001`~~ — addressed 2026-08-15 (condition no longer reproduces). Accepted 2026-07-08, now outside the 30-day window.
- ~~`cleanup-CLN-ADR-1-ADR-0002`~~ — addressed 2026-08-15 (condition no longer reproduces). Accepted 2026-07-08, now outside the 30-day window.
- ~~`cleanup-CLN-ADR-1-ADR-0003`~~ — addressed 2026-08-15 (condition no longer reproduces). Accepted 2026-07-08, now outside the 30-day window.
- ~~`cleanup-CLN-ADR-1-ADR-0004`~~ — addressed 2026-08-15 (condition no longer reproduces). ADR-0004 is `Superseded` as of 2026-08-14; the rule scopes to `Accepted` ADRs only.
- ~~`cleanup-CLN-ADR-3-ADR-0004-docs-research-raw-2026-07-07-bionic-coding-manifesto-manifesto-md`~~ — addressed 2026-08-15 (condition no longer reproduces). Closed by supersession, not by repair: ADR-0004 left `Accepted` status, so CLN-ADR-3 no longer scans it. The `docs/research/...` prose path it cites is still stale text inside a superseded decision, which is the correct resting place for it — superseded bodies are historical records.
- ~~`cleanup-CLN-ADR-3-ADR-0004-docs-research-sources-bionic-coding-manifesto-md`~~ — addressed 2026-08-15 (condition no longer reproduces). Same cause as the entry above.

_Four of these closed by the calendar, three by [[adrs/ADR-0005-serve-a-landing-homepage-and-a-five-item-top-nav]] superseding ADR-0004. Only one is a fresh finding._
