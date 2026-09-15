# Crux learning catalog — blog intake

This four-file package is a draft handoff for the Bionic Coding site's crux section.
It teaches how to work with the team, not how to memorize sixty skill commands.
It does not publish pages, install agents, or change Crux's contracts.

## Files

- `crux-learning-catalog.json`: complete ingestion payload, with 10 agents and 60 skills.
- `crux-learning-catalog-guide.json`: editable teaching guidance and classifications.
- `crux-learning-catalog-export.py`: regenerates the payload from that guide and a Crux source checkout.
- `crux-learning-catalog-instructions.md`: this handoff.

Keep these four files together when filing them from the inbox. Do not ingest the Python file as a research article.
The inbox has no concern index to update. No public page or existing blog record was changed by this handoff.

## Editorial assignment

Build an outcome-led guide for the crux section. Lead with two entry points:

1. **Brainstormer:** explore an idea before deciding what to build.
2. **Commander:** run an approved plan and coordinate its specialists.

Show **night-gardener** separately as an explicitly requested or owner-scheduled strategic pass.
Show architect, dev-lead, developer, reviewer, historian, librarian, and wayfinder as delegated specialists.
Explain what each contributes and what readers should expect back, without teaching beginners to dispatch them one by one.

This audience classification is a recommendation requested by the owner, not a runtime prohibition.
Several specialist definitions currently include direct-user triggers. Do not claim that they cannot be called directly.
A stronger restriction would require a separate Crux contract change; this package makes none.

Agents are roles. Skills are procedures those roles or the main assistant follow.
The two-agent entry model does not hide ordinary user requests such as asking a question, checking drift, or initializing docs.
It also does not impose a commander or promptbook on a small fix.

## Suggested page structure

- Start here: describe the outcome, evidence, constraints, and authority.
- Explore or execute: the two primary entry points.
- Meet the specialists: responsibilities, expected results, and boundaries.
- What happens after a request: the catalog's short journeys.
- Skill reference: searchable by capability and category, with audience badges.
- Human decisions: explicit invocation and sign-off workflows.
- Safety and limits: questions versus writes, independent review, and named stop points.

Use the structured `learning` fields for explanatory cards.
Use `declared`, `declared_invocation`, and `triggers` as source facts, not editorial invention.
Do not turn every trigger into an unqualified “Run this” button.
Hide `agent_internal` skills from beginner call-to-action lists. Put `workflow_support` behind an advanced section.
Label `explicit_human` separately: a model's inability to invoke a skill is not proof that the human workflow is unavailable.

Example requests express intent. They are not cross-harness slash commands.
Runtime agent names are reference identifiers, not proof that the role is installed or callable in a reader's session.
Tool lists and invocation flags describe source contracts; enforcement depends on the harness and its configuration.
No live routing or safety enforcement was tested while producing this catalog.

## Ingestion and data contract

The payload is UTF-8 JSON, with a top-level `format_version: "1"`.
Its schema version is this handoff's own format, not the plugin's skill-contract or documentation-tree version.
Arrays `agents` and `skills` use stable `id` slugs. Join `declared.skills` and `declared_by_agents` using those slugs.
Those associations describe frontmatter bindings, not a complete runtime call graph.
Agent `learning.source_sections` names supporting sections in the referenced role file.

A missing source invocation flag is JSON null, not false.
Treat `learning.audience` as editorial classification and `declared_invocation` as source metadata.
Descriptions and trigger arrays are copied from source; never reconstruct triggers by extracting quoted prose.

For Jekyll, the receiving team can place the reviewed payload under `_data/` and render it from Liquid templates.
That is a proposed integration, not a change made by this handoff.
Preserve provenance and version labels. Render plain text safely; do not execute example requests or source content.

## Source and publication boundary

This snapshot describes Crux 3.16.1 from the source revision recorded in the payload.
Each role and skill includes its source-file SHA-256.
The exporter also records the manifest, guide, and exporter digests.
Source paths are relative to the Crux plugin root; they are not paths within this blog.

The private-beta report is not evidence of official public availability.
Before publishing version-specific claims or source links, verify the official release and map these plugin-relative paths to it.
Do not expose private repository URLs, local machine paths, private ADRs, or unreleased project records in public pages.
The payload contains no private decision bodies or runtime secrets.

The blog's existing `bionic/CLAUDE.md` predates this snapshot: it still has older skill-contract details and question-shaped regeneration triggers.
Do not copy those into the new reference. Follow it for this repository's documentation operations, but use versioned Crux sources for product claims.
Updating that local schema is separate work, not part of this package.

## Refreshing without hand-maintaining derived data

Edit the guide for teaching changes. Do not edit generated catalog entries.
Use a clean Crux source checkout. Pass its plugin directory, which is `crux/` inside the authoring repository.
The exporter refuses version changes until the guide's `reviewed_plugin_version` is deliberately updated after reviewing the contracts.
It also refuses missing or extra manifest entries and incomplete editorial coverage.

From the directory holding this package:

```sh
uv run crux-learning-catalog-export.py --plugin-root /path/to/crux > crux-learning-catalog.candidate.json
uv run crux-learning-catalog-export.py --plugin-root /path/to/crux --check crux-learning-catalog.json
```

The first command produces a candidate; compare and validate it before replacing the current catalog.
The second is read-only and fails when the existing catalog differs.
After regeneration, re-review invocation flags, agent handoffs, and the examples.
Digest equality and JSON validity establish artifact consistency, not live routing behavior.

## Acceptance for the receiving team

- All catalog IDs and skill/agent cross-references resolve.
- Readers can explain which two roles to start with and why most specialists are delegated.
- Small work does not acquire unnecessary cycle ceremony.
- Questions about architecture, progress, and decision relationships are not presented as permission to mutate.
- Human sign-offs stay human decisions; restrictions are not bypassed to make demonstrations work.
- Independent review is commissioned by the delegator, not the author under review.
- The site clearly distinguishes proposed editorial guidance, source contracts, and observed behavior.
- Pages are previewed and reviewed before publication. This inbox handoff grants no permission to push or deploy.
