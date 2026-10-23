# Crux learning catalog — blog intake

This four-file package is a draft handoff for the Bionic Coding site's Crux section.
It teaches how to work with the team, not how to memorize skill commands.
It does not publish pages, install agents, or change Crux's contracts.

## Files

- `crux-learning-catalog.json`: complete ingestion payload, with counts derived from the current source.
- `crux-learning-catalog-guide.json`: editable teaching guidance and classifications.
- `crux-learning-catalog-export.py`: regenerates the payload from that guide and a Crux source checkout.
- `crux-learning-catalog-instructions.md`: this handoff.

Keep these four files together when filing them from the inbox. Do not ingest the Python file as a research article.
The inbox has no concern index to update. The exporter writes only its four package files; it does not change public pages.

## Editorial assignment

Build an outcome-led guide for the Crux section. Lead with two entry points:

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

This snapshot describes the Crux version and source revision recorded in the payload.
Each role and skill includes its source-file SHA-256.
The exporter also records the manifest, guide, and exporter digests.
Source paths are relative to the Crux plugin root; they are not paths within this blog.

The private-beta report is not evidence of official public availability.
Before publishing version-specific claims or source links, verify the official release and map these plugin-relative paths to it.
Do not expose private repository URLs, local machine paths, private ADRs, or unreleased project records in public pages.
The payload contains no private decision bodies or runtime secrets.

A consuming project's local `bionic/AGENTS.md` can predate this snapshot.
Follow it for that repository's documentation operations, but use versioned Crux sources for product claims.
Updating a local schema is separate work, not part of this package.

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

## Maintainer shortcut

The canonical exporter lives at `tools/export-bionic-catalog.py` in the Crux authoring repository.
Its editorial inputs live under `tools/bionic-catalog/`. The package copies are portable snapshots, not a second source of truth.
When the blog edits teaching guidance, reconcile those changes into the canonical guide before replacing a handoff.

From the Crux checkout, export with:

```sh
uv run tools/export-bionic-catalog.py --output-dir ../bionic-coding/bionic/inbox
```

Use `--dry-run` with that destination to compare without writing. Exit 1 means differences or validation findings.
An identical export is a no-op. Differing existing package files require `--replace`; review local edits before using it.
Unrelated inbox items remain untouched. The write is atomic per replacement file, not across the whole package.
After an interrupted write, inspect the package and rerun with `--replace` to complete it.
No automatic release hook is installed; run the exporter when a new handoff is wanted.

## Refresh assignment: 3.16.1 to 4.5.1

Update the existing manual, not only its searchable catalog. The receiving site's
`_data/crux_catalog.json` currently describes 3.16.1. This handoff describes the
4.5.1 source checkout; it does not attest public release availability.

Preserve the site's capitalization of Crux and its outcome-led teaching model.
Review these existing pages together: `crux/index.md`, `crux/installation.md`,
`crux/setup.md`, `crux/team.md`, `crux/in-practice.md`, `crux/catalog.md`, and
`crux/reference.md`. Reconcile `_tools/crux-catalog/` with this package and use
the regenerated JSON for `_data/crux_catalog.json`. Preserve unrelated work.

Cover these changes against the versioned source:

- Cycles replace new promptbook authoring. Explain dev, iterate, refactor,
  simplify, quick-fix, and release. Historical promptbooks remain readable.
  Compatibility skill names route new work to cycles; they are not additional workflows.
- Explain phases, pass limits, pause/resume, queue requests, and closed cycles.
  Release has fixed beta and official step lists with no pass limit.
- Explain IDRs separately from ADRs. New-policy ADR acceptance makes rules binding;
  human acceptance is required by default unless council-only is configured.
- Explain Lite, Standard, and Strict councils, architect agreement, and dissent.
  Keep council approval distinct from independent implementation review.
- Explain proportional scrutiny and shared test evidence. Reuse depends on matching
  inputs and environment, not merely moving to a new phase or release.
- Cover current authority versus historical decisions, clause-level migration,
  and preservation of historical evidence.
- Cover Claude Code, Codex, OpenCode, and OMP installation and role names.
  The catalog's runtime_names map omits OMP; consult install-omp-agents and
  the versioned OMP guide rather than treating that omission as lack of support.
- Cover micro-crux, current init-docs behavior, and instruction migration.
  Distinguish a standalone guide from the full plugin and its executable workflows.
- Review the current council output-budget behavior where the manual documents
  advanced configuration. Do not turn model-specific limits into beginner instructions.

Use the catalog for inventory, descriptions, triggers, audiences and provenance.
It is not a complete manual specification: consult each relevant SKILL.md and its
references, the user guide, and harness installation guides at the recorded revision.
Never apply the blog's older local documentation schema as the current product contract.
Report unavailable sources as gaps instead of inventing behavior.

Compare old and new catalog IDs. Remove obsolete current-feature cards while
preserving useful historical links. Check page navigation, examples, source links,
counts and cross-references. Preview the Jekyll build before publication.
Keep beta-only claims visibly versioned until public availability is verified.
This handoff authorizes no push or deployment.

The handoff guide corrects stale release and council notes in the canonical export
inputs. Reconcile these editorial corrections into the authoring repository after
its active release verification finishes; those inputs were left unchanged here.
