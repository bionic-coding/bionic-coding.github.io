---
generated_at: 2026-09-01T19:01:46Z
generator: cleanup
generator_version: "3.5.0"
scan_findings: 0
suggestions_open: 0
suggestions_dismissed_carried: 0
dismissed: []
---

# What's next

_Generated 2026-09-01 19:01 by `cleanup-campsite` v3.5.0. **Body regenerated end-to-end on every run; only the `dismissed:` frontmatter list persists.** Hand-edits below the frontmatter are blown away. To dismiss a suggestion, move its `id:` into the `dismissed:` frontmatter list with a `reason:`._

## Open suggestions (0)

_No open suggestions. Every implemented rule reported clean or skipped on its existence gate._

## Recently closed (since last run)

- ~~`cleanup-CLN-ADR-1-ADR-0005`~~ — closed 2026-09-01 (rule `CLN-ADR-1` was retired in crux 3.5.0; its standing findings closed with it. The ADR is unchanged and correctly Accepted).

## Rules that reported clean

Recorded so a future run can tell "checked and clean" from "never checked":

- `CLN-ADR-2` — no ADR sits in `Proposed` (six ADRs: five Accepted, one Superseded).
- `CLN-ADR-4` — no phantom `ADR-NNNN` reference in `README.md` or `CLAUDE.md`; no `USER_GUIDE.md` in this repo.
- `CLN-PB-1` … `CLN-PB-4` — `bionic/promptbooks/active/` is empty; PB-0001 is archived and both of its run snapshots are `.yaml`, so the duplicate-heading rule is a no-op.
- `CLN-JR-1` — no `adr`/`promptbook`/`schema` op with `accept`/`archived`/`migration` in the last 7 days. The last seven days carried 10 `ingest` ops only.
- `CLN-JR-2` — two closed months. July 2026: 5 journal entries against 52 log ops. August 2026: 2 journal entries against 42 log ops, which meets the rule's floor of 2 exactly. Not flagged, but August is one entry away from thin; a reflective entry on the August research pass (Fable 5.1, GLM-5.3-Flash, the OpenRouter working set) would be well placed.
- `CLN-AUD-1` — last `audit` op ran 2026-08-25, 7 days ago, inside the 14-day window. `audit-docs` runs immediately after this scan regardless.
- `CLN-RETRO-1` — 1 book archived against a threshold of 5. No retrospective is due.
- `CLN-WN-1` — the `dismissed:` list is empty; nothing to prune.
- `CLN-PJ-1a` … `CLN-PJ-2`, `CLN-FG-1`, `CLN-FG-2`, `CLN-TMPL-1` — skipped by their existence gates. This repo is a Jekyll site: no plugin manifest, no forge log, no parity manifest.
