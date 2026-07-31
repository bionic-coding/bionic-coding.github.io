# Invariants index

_Last updated: 2026-07-30_

## Pins (0)

_No pins yet — the ledger was scaffolded on 2026-07-30 (schema 3→4 rung, invariants concern opt-in) but not yet populated. Run `recover-invariants` to mine candidates from source; every candidate lands `provenance: recovered, ratification: observed` — never pre-ratified. A human disposes of each candidate via `transition-invariant`._

Each pin, once it exists, gets a page at `docs/invariants/<slug>.md` (frontmatter: `id`, `class`, `provenance`, `ratification`, `verification`, `related_adrs`, `related_briefs`, `checks`) reconciled against its executable form(s) in `bionic/invariants/` via `bionic/invariants/reconciliation.yml`. See `docs/CLAUDE.md` §15 for the full contract.
