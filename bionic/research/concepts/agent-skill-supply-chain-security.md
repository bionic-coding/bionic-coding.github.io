---
title: "Agent skills as a software supply chain — the security picture"
slug: agent-skill-supply-chain-security
type: concepts
tags: [security, agent-skills, prompt-injection, supply-chain, scanning, claimed-vs-verified]
sources: [snyk-toxicskills-agent-skills-audit]
last_reviewed: 2026-08-25
---

# Agent skills as a software supply chain

Backs [[_lessons/sharing-agents-and-skills]] and [[_lessons/skills]]. The lesson already argues qualitatively that installing a shared skill means running untrusted code. This page holds the measured base rate behind that claim, and the mitigation the lesson predates.

## The numbers — read the denominators

Source: [[research/sources/snyk-toxicskills-agent-skills-audit]] (Snyk "ToxicSkills", 2026-02-05, read in full 2026-08-25). Corpus: **3,984 skills** from ClawHub and skills.sh, deduplicated by author + skill ID.

| Finding | Count | Share of corpus |
|---|---|---|
| At least one security issue, any severity | 1,467 | **36.82%** |
| At least one CRITICAL issue | 534 | **13.4%** |
| Confirmed malicious payloads (human-reviewed) | 76 | — |
| Malicious skills still live at publication | 8 | — |

Per-policy rates across the whole ClawHub corpus: third-party content exposure 17.7%, suspicious download 10.9%, hardcoded secrets 10.9%, direct money access 8.7%, credential handling 7.1%, malicious code 5.3%, unverifiable dependencies 2.9%, **prompt injection 2.6%**.

Snyk reports 0% false positives against the curated skills.sh top-100 and 90–100% recall on confirmed-malicious samples.

> **[claimed-vs-verified] Three traps in citing this study, all of them easy to fall into.**
>
> 1. **The published title is wrong about its own body.** The page is titled "Snyk Finds Prompt Injection in 36%". The body does not say that. **36.82% is "at least one security flaw of any severity."** Prompt injection specifically is **2.6% of the corpus**. The two numbers have different denominators and different meanings.
> 2. **91% is a different denominator again.** "91% employ prompt injection" is 91% **of the 76 confirmed-malicious skills**, not of the ecosystem. The companion figure is that 100% of confirmed-malicious skills carry malicious code — the finding is about *convergence*, that agent malware pairs an injection with a payload so the injection disarms the agent's own caution before the payload runs.
> 3. **It is a February measurement.** Published 2026-02-05, and the post itself reports daily submissions rising from under 50 in mid-January to over 500 by early February — a 10× change in weeks. Cite it as "a dated snapshot of an ecosystem growing 10× a month," not as a current rate. **Re-check before it reaches a post.**

## Why skills are worse than a package registry

Snyk's own framing, and the part that transfers cleanly to a lay audience: a skill inherits the **full permissions of the agent it extends** — shell access, filesystem read/write, environment-variable credentials, outbound messaging, and persistent memory across sessions. A traditional package runs in an isolated context; a skill does not.

Publishing barrier at ClawHub: **a `SKILL.md` and a one-week-old GitHub account.** No code signing, no security review, no default sandbox.

Three ways skills are worse than the npm/PyPI parallel they otherwise resemble:

- **Higher privilege by default** — the skill gets whatever the agent has.
- **Prompt injection has no analog** — a natural-language attack passes straight through code-based detection.
- **Persistence through memory** — a malicious skill can modify agent behaviour permanently.

## The two failure modes are different problems

- **Malicious skills** (76 confirmed) — deliberate credential theft, backdoors, exfiltration. External malware distribution via password-protected archives (an anti-virus evasion), base64-obfuscated exfiltration one-liners, and instructions that talk the agent into disabling its own safety checks.
- **Insecure-by-design skills** (the bulk of the 36.82%) — nobody meant harm. A skill that fetches web content is an **indirect prompt-injection surface** even when the author did everything right: attacker posts poisoned content, the legitimate skill faithfully retrieves it, the agent reads the embedded instructions as commands. A skill that fetches its own instructions at runtime is worse still, because the reviewed version and the served version are different artifacts.

## The mitigation the lesson predates: scan before you install

[[_lessons/sharing-agents-and-skills]] (`updated: 2026-07-17`) covers the hard part well — it names prompt injection, least privilege, provenance, verified publishers, version pinning, and revocation. **Its "Installing safely" list is six manual acts.** That was the whole toolkit on 2026-07-17. It is not the whole toolkit now.

What exists as of this review:

- **`mcp-scan`** (Invariant Labs / Snyk), the engine behind this study, open source: `uvx mcp-scan@latest --skills` for installed skills, `uvx mcp-scan@latest` for MCP server configs. Verified — the invocation and its output format are printed in the primary.
- **Anthropic skill and plugin security scanning (beta)** — reported for Enterprise plans, checking third-party uploads for malicious content. **Claimed, snippet-level only, not verified against a primary.**
- **SkillKit's built-in scanner** — claimed to analyze skills for prompt injection, command injection, data exfiltration, and hardcoded secrets. **Claimed, snippet-level only, not verified.**

**The suggested lesson edit is one bullet, and the author writes it.** A sixth item on the "Installing safely" list — run a scanner before you install; several exist, and the harness may have one built in — with the base rate as the sentence that motivates it. Scaffold only; the prose is the author's. Bump `updated` when it lands.

## Why this fits the site's thesis

"Augmented, not replaced" means the human keeps judgment. This is a concrete place where judgment gained a tool: the scanner does not decide whether to trust a skill, it hands the human the evidence to decide with. That reading is worth keeping in front of any post built on this material — the framing is *better-informed human*, not *machine gatekeeper*.

## Possible post

"How to tell if a shared AI skill is safe" — Learn-adjacent field note, natural checklist shape, and a number in the lede. Related: [[briefs/BRIEF-teaching-regular-people-ai-content-plan]].

## Not captured

The full technical report (`invariantlabs-ai/mcp-scan` → `skills-report.pdf`) holds the detailed methodology and the complete dataset. It is the primary for anything past the summary tables above and was **not** captured. Two of the three figures are screenshots whose numeric contents were not transcribed.
