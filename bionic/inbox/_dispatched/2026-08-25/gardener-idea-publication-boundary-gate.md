# Wire the V7 published-file-set oracle into CI

**Filed:** 2026-08-15 by the night gardener
**Kind:** engineering-gap / proposal for a decision
**Status:** proposal only — no ADR, no decision taken

## The evidence that prompted this

Tonight I verified that `CHANGELOG.md` was live at the site root. It has no frontmatter, so
Jekyll copies it verbatim as a static file rather than rendering it — which is why it slipped
past the `exclude:` pass that caught `README.md`, `USER_GUIDE.md`, and `CLAUDE.md`.

Then I ran PB-0001/RUN-002's own V7 oracle against the shipped build:

| build | V7 inventory count | expected |
|---|---|---|
| `main` at `daeef0d` | **28** | 27 |
| `garden/exclude-changelog-from-build` | **27** | 27 |

The oracle is `find _site -type f ! -path '*/assets/*' ! -path '*/fonts/*'`, recorded in
[[promptbooks/runs/PB-0001-fix-mobile-nav-and-restore-about/run-RUN-002]] with a baseline of
26 intended files. Twenty-six plus the new 2026-08-14 post is 27. The build shipped 28.

**The detector already existed, already worked, and was not plugged into anything.** The same
run snapshot records the reason: "no CI gate for any V-unit (systemic — deferred: deploy-pipeline
changes are out of this loop's scope)." [[adrs/ADR-0005-serve-a-landing-homepage-and-a-five-item-top-nav]]
carries the matching follow-on: "Add a durable assertion for the publication boundary... that check
is run by hand today. Integrating it into CI is the candidate. Recorded, not resolved."

Nine days elapsed between recording the deferral and shipping a file the check would have caught.

## The design question worth deciding

The narrow fix is on `garden/exclude-changelog-from-build`. It closes the instance. The class
stays open until something runs on every build. The open questions:

1. **Which oracle?** The run snapshot is explicit that the extension denylist (`find _site -name '*.md' -o -name '*.yml'`) is *not* durable — an extensionless or wrong-extension root file defeats it, and the cycle demonstrated this with a published `NOTES.txt` and `SECURITY`. Tonight the denylist happened to catch `CHANGELOG.md` because it ends in `.md`; that is luck, not coverage. The inventory count is the load-bearing oracle.
2. **Count, or allowlist?** A bare count (`== 27`) is brittle — it fails on every legitimate new post, which is weekly. An allowlist of intended path *patterns* (posts, lessons, the five top-level pages, `feed.xml`, `CNAME`, `404.html`) fails only on genuinely unintended files. The second is more work and much less noisy. Given the site publishes a post most weeks, a bare count would be disabled within a month.
3. **Where does it run?** `.github/workflows/jekyll.yml` already builds with the production overlay. A post-build step there is the cheapest home and gates the actual deploy.
4. **Fail or warn?** Failing the deploy on an unexpected file is the strong form. Given the failure mode is "private repo documentation becomes public," failing is defensible.

## Why this is worth more than it looks

This is the second time this exact boundary has failed — `ff17186` published three repo docs,
and the cycle that fixed it created a fourth file that then published. The pattern is not
carelessness; it is that the boundary is enforced by a hand-maintained list with no feedback
signal. Every future root-level file is a fresh chance to trip it, and the cost is asymmetric:
publishing private documentation is not a rendering bug, it is a disclosure.

## Suggested disposition

Worth an ADR, because it touches the deploy pipeline and sets a fail-vs-warn policy. If that is
too heavy, an `iterate` cycle also fits — the diagnosis is already verified and the remediation
is bounded. I have deliberately not authored either; the architect decides.

## Related

- [[adrs/ADR-0005-serve-a-landing-homepage-and-a-five-item-top-nav]] — decision 4 and its recorded follow-on work
- [[promptbooks/runs/PB-0001-fix-mobile-nav-and-restore-about/run-RUN-002]] — V7/V8 units, the mutation control, and the deferral
- `garden/exclude-changelog-from-build` — the one-line branch that closes the instance
