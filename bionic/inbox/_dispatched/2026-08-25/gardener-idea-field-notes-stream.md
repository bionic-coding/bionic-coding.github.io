# A third content stream showed up without being planned

**Kind:** idea / pre-decision exploration. This is options, not a decision. If it gets pursued it wants a brief first, then an ADR — it touches the information architecture that [[adrs/ADR-0005-serve-a-landing-homepage-and-a-five-item-top-nav]] governs.

## What I noticed

The site now publishes nine posts. Four are "This Week in AI" issues. Five are not:

| post | shape |
|---|---|
| `2026-07-11-my-ai-kit` | what I use |
| `2026-07-19-qwen3-8-max-preview` | hands-on with a model |
| `2026-07-20-opus-update-predictions` | opinion |
| `2026-08-15-fixing-claude-code-sigkill-in-zed` | debugging field note |
| `2026-08-16-running-qwen3-8-27b-locally` | measured experiment |

The last two shipped on consecutive days. Both are the same genre: *I hit a thing, here is what happened, here are the numbers or the commands.* Neither is news, and neither is an evergreen lesson.

So there are three content types, and only two of them have contracts:

- **Column** — [[briefs/BRIEF-this-week-in-ai-format]] plus `_templates/this-week-in-ai.md`.
- **Lessons** — `order`, `summary`, `status`, `updated`, a freshness review, a soft-draft mechanism.
- **Field notes** — nothing.

## Why it is worth a decision rather than drift

Three concrete edges, all checkable today:

1. **The Articles page promises something it no longer only delivers.** `articles.md` describes itself as "Weekly-ish news for AI and software development" and "Timely, plain-language takes on what's new and why it matters." A reader arriving for that finds a Gatekeeper debugging walkthrough second in the list. The page is honest about the column and silent about the rest.

2. **The differentiator already exists in the data and renders nowhere.** Every post carries `tags:` — `[model-news, weekly]` on the four issues, `[claude-code, zed]` and `[local-models, qwen]` on the new ones. Nothing in `_layouts/` or any page reads `site.tags`. The taxonomy is written on every post and displayed on none. One post (`my-ai-kit`) carries `tags: []`.

3. **Field notes age differently from both neighbours.** The column brief makes a point of this: an issue is a dated snapshot and its links are *allowed* to go stale. Lessons are the inverse — they carry `updated` and get reviewed. A field note is a third case: the *finding* stays true (Gatekeeper killed the binary) while the *fix path* rots fast (a vendored adapter path, a Homebrew Node version). Neither existing policy fits.

## Options, roughly cheapest first

**A. Do nothing, deliberately.** Nine posts is small. Write it down as a choice so it stops being drift, and revisit at ~20 posts.

**B. Render the tags that already exist.** Group the Articles index by tag, or add a filter row. No new nav item, no ADR-0005 amendment, no new frontmatter. Smallest change that repays the metadata already being written.

**C. Split the index in place.** Two sections on `/articles/` — "The column" and "Field notes" — driven by the presence of the `weekly` tag. Still one nav item, so ADR-0005's five-item nav holds.

**D. A fourth content type with its own contract.** A `_notes/` collection with its own layout, its own index, and a `verified:` date field that says "these commands worked on this date." Highest cost; the only option that solves the staleness mismatch properly.

## What I would want to know before choosing

- Is the field note a genre worth committing to, or were these two just what happened this week?
- Does a reader arriving at `/articles/` want them mixed or separated?
- Is "these commands worked on 2026-08-15" a promise worth making? That is the real question inside option D, and it is an editorial commitment, not a template.

## A smaller thing in the same neighbourhood

Whatever gets decided, `tags: []` on `my-ai-kit` should either be filled or the key removed. An empty taxonomy field is the kind of thing that quietly breaks a `site.tags` loop the first time one gets written.
