---
snoozed: []
dismissed: []
---

# Tending — your control surface

This is the **only** file you edit to steer the night gardener. She reads it; she
never writes below this frontmatter.

- **snoozed:** hide an item until a date. `{ id, until: YYYY-MM-DD, reason }`.
  Snoozes are scheduling only — they teach the gardener nothing about your taste.
- **dismissed:** stop an item for good. `{ id, dismissed_at: YYYY-MM-DD, reason }`.
  An id-level dismissal vetoes that exact item forever; it also adds weight that
  damps *new* items of the same `kind` (see `preferences.md` for the arithmetic).

Item ids look like `garden-<kind>-<slug>` and appear in each morning note's
frontmatter. Copy the id here to snooze or dismiss it.

Free-form notes below the frontmatter are never parsed — write whatever you like.
