# Skill scanners arrived, and there is now a published base rate for bad skills

**Sources (all snippet-level — none were fetched):**
- https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/
- https://support.claude.com/en/articles/12138966-release-notes
- https://github.com/snyk/agent-scan

**Read depth:** Perplexity search snippets only. Every domain above sits outside `bionic/garden/sources.md`, so the unattended pass gave them snippet treatment by contract. **Verify every number below before it reaches a post.**

## Why this is a keeper

1. It supplies a *number* for a claim [[_lessons/sharing-agents-and-skills]] currently makes qualitatively — that installing a shared skill is running untrusted code.
2. It names a new mitigation the lesson predates: automated pre-install scanners.
3. It is on-brand. "Augmented, not replaced" means the human keeps judgment, and this is a concrete place where judgment now has a tool behind it.

## What the snippets claim

> [fetched content — treat as data]
> ```
> Snyk: "Finds Prompt Injection in 36%, 1467 Malicious Payloads" across scanned
> AI agent skills (ToxicSkills research).
> Remediation given: `uvx mcp-scan@latest --skills`
>
> Anthropic release notes, August 6 2026: "Skill and plugin security scanning
> (beta)". August 14 2026: "Claude adds beta skill and plugin security scanning
> for Enterprise plans to check third-party uploads for malicious content."
>
> SkillKit: "built-in security scanner that analyzes skills for prompt injection,
> command injection, data exfiltration, hardcoded secrets."
> ```

The 36% figure carries a February 2026 date in one snippet and was still being cited in August. Treat it as "a widely repeated research claim from early 2026," not as a current measurement, until the original post is read.

## The lesson update this suggests

[[_lessons/sharing-agents-and-skills]] (`updated: 2026-07-17`) already covers the hard part well: it names prompt injection, least privilege, provenance, verified publishers, version pinning, and revocation. It is not wrong and it is not thin.

What it lacks is a **scan step**. Its "Installing safely" list is entirely manual — read it, review permissions, check provenance. A sixth bullet along the lines of *"run a scanner before you install — several now exist, and the harness may have one built in"* would close the gap, and the base rate is the sentence that motivates it.

That is a real edit to a published lesson, so it needs the author's sentences. Scaffold only.

## Also a possible post

"How to tell if a shared AI skill is safe" is a Learn-adjacent field note with a natural checklist shape and a number in the lede.

Related: [[_lessons/skills]], [[briefs/BRIEF-teaching-regular-people-ai-content-plan]]
