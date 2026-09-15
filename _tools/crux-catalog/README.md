# crux catalog — refresh procedure

`_data/crux_catalog.json` powers `/crux/team/` and `/crux/catalog/`. It is **generated**.
Never hand-edit it: the next refresh overwrites the edit, and `--check` fails in the meantime.

Files here:

| File | Role |
| --- | --- |
| `crux-learning-catalog-export.py` | the exporter; reads a crux source checkout, writes JSON to stdout |
| `crux-learning-catalog-guide.json` | editorial guidance — categories, role teaching, skill notes, audience overrides |
| `crux-learning-catalog-instructions.md` | the original handoff, kept as the authoritative long form |

Teaching changes go in the guide, never in the payload. `_tools/` starts with an underscore,
so Jekyll never copies it into `_site/`.

Use this catalog for product claims about crux. Use `bionic/CLAUDE.md` for this repository's
documentation operations — it predates this snapshot and carries older skill-contract details.

## Refresh

The exporter needs a clean crux source checkout. `--plugin-root` is the `crux/` directory
**inside** the authoring repo, not the repo root. The guide resolves as a sibling of the
script, so no `--guide` flag is needed while both live here.

```sh
cd _tools/crux-catalog

# 1. Produce a candidate.
uv run crux-learning-catalog-export.py --plugin-root /path/to/crux/crux > candidate.json

# 2. Read the diff before trusting it.
diff <(python3 -m json.tool ../../_data/crux_catalog.json) <(python3 -m json.tool candidate.json)

# 3. Publish it, then reread both pages locally.
mv candidate.json ../../_data/crux_catalog.json
cd ../.. && bundle exec jekyll serve

# 4. Confirm. Exits non-zero when the published payload and the source disagree.
uv run _tools/crux-catalog/crux-learning-catalog-export.py \
  --plugin-root /path/to/crux/crux --check _data/crux_catalog.json
```

Step 2 is the review, not a formality. A changed invocation flag, a changed role handoff, or a
changed example request changes what the pages teach.

## Where to point `--plugin-root`

Use the **released plugin distribution** — the versioned directory the marketplace installs:

```
~/.claude/plugins/cache/crux/crux/<version>
```

That directory is not a git checkout, so the exporter stamps `revision: null` and
`git_state: not_available`, and `--check` compares cleanly. Point `--plugin-root` at a git
checkout instead and `source.revision` records that checkout's HEAD, which differs between any
two clones of the same version and makes `--check` exit 1 on a payload that is otherwise
identical. Read such a failure by diffing, not by trusting the exit code.

Verified on 2026-09-15 against crux 3.16.1: the published payload's `agents`, `skills`, `counts`,
`teaching_model`, `audience_definitions`, `journeys`, `handoff_template` and `publication_notes`
are byte-identical to a fresh export, and `manifest_sha256`, `guide_sha256` and `exporter_sha256`
all match. That is the confirmation that these pages describe the released version.

## What the published payload does not carry

`source.revision` is `null` by design: this repository is public, and a checkout revision is a
local identifier with no public meaning. Provenance is carried by `plugin_version`, the manifest
digest, and a SHA-256 for every role and skill file. No page renders any of them — the acceptance
check `grep -rEi 'sha256|SKILL\.md|/Users/' _site/crux/` exists for that reason.

## What the exporter refuses

- **A version it has not been told about.** It aborts when `plugin.json`'s version differs from
  the guide's `reviewed_plugin_version`. Bump that field after rereading the contracts, never to
  unblock a refresh.
- **A dirty plugin subtree.** Commit the crux checkout first.
- **Incomplete editorial coverage.** Every skill must sit in exactly one guide category, every
  role must have guidance, and every `skill_notes` and `skill_audience_overrides` key must
  name a real skill. A new crux skill cannot publish until someone writes its category. That is
  the design.

## What the pages compute rather than state

Counts, the category sizes, the version label, and the badge legend all render from the payload.
Never type "60 skills" or a version number into a page: a refresh has to be able to move the
pages by itself.

## Not wired into CI

`.github/workflows/jekyll.yml` has no crux checkout and no `uv`. Step 4 is a manual pre-publish
check, not a build step.
