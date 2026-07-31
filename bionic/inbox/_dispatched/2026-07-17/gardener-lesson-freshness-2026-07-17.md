# Lesson upkeep — three small things after the big buildout

_Dropped by the night gardener, 2026-07-17. Data for your morning review, not
dispatched. Ordered most-time-sensitive first._

---

## 1. TIME-SENSITIVE — review the MCP lesson before July 28

`_lessons/mcp.md` published today (`updated: 2026-07-17`). The **biggest MCP spec
revision since launch ships July 28** (release candidate is out now) — stateless
core, MCP Apps (server-rendered UIs), a Tasks extension, OAuth-aligned auth, and
Enterprise-Managed Auth going stable. There's a real risk the flagship lesson reads
slightly dated within two weeks of shipping.

- **Suggested action:** a light pass on `mcp.md` against the RC. It's a lesson for
  non-technical readers, so it should stay conceptual — but one forward-looking line
  ("the protocol is evolving quickly; the 2026 revision makes servers simpler to run
  and lets them ship little interactive UIs") keeps it honest without dating it.
- **Research gap worth closing:** the research wiki's `frontier-models-2026` reference
  is model-focused; **MCP protocol evolution isn't captured anywhere.** The MCP blog
  RC post (linked in `gardener-next-issue-candidates-2026-07-17`) would make a good
  `research/references/` or `research/concepts/` source to back both the lesson and any
  column coverage.

## 2. Nav-ordering collision: two lessons share `order: 4`

`_lessons/skills.md` (published) and `_lessons/leveraging-ai.md` (stub) **both carry
`order: 4`** in frontmatter — so they sort ambiguously in the Learn nav. This looks
like a side-effect of the buildout/rename (Skills got filled in; Leveraging AI kept
its old slot).

- **Current sequence:** markdown 1 · prompting-and-evals 2 · agents 3 · **leveraging-ai 4
  (stub) + skills 4** · agentic-harnesses 5 · mcp 6 · sharing 7 · search/rag 8 · samples 9
  · glossary 10.
- **Suggested action (editorial — your call):** give `leveraging-ai` a distinct order.
  Since it's the personal capstone ("How I use AI to make things. Like this website."),
  it probably wants a *late* slot rather than sitting at 4 among the concept primers —
  e.g. after Samples, just before Glossary. One-line frontmatter fix per file.

## 3. `leveraging-ai` is your last stub (10 of 11 published)

Not a nag — just naming the finish line. After this batch, every lesson is published
except this one. And it's the right one to be last: it's *your* workflow, the least
generate-able page on the site, the one that most needs your hand rather than a council.
When you write it, item 2 above resolves itself (you'll set its final order then).

---

_None of this is urgent except item 1's July 28 clock. The order collision is the only
thing here that's arguably a bug rather than a preference._
