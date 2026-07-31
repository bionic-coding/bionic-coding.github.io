---
title: "System Card: Claude Opus 5"
slug: claude-opus-5-system-card
type: source
source_url: null
source_date: 2026-07-24
author: "Anthropic"
captured_at: 2026-07-21
last_source_check: 2026-07-21
raw_path: research/raw/2026-07-21/claude-opus-5-system-card/
previous_captures: []
static: true
tags: [anthropic, claude, opus-5, model-release, system-card, safety, alignment, benchmarks]
---

# System Card: Claude Opus 5

_Anthropic — System Card — the document is dated **2026-07-24**; captured 2026-07-21 from a PDF dropped in the inbox (the card's own date runs ahead of the capture date — treat 2026-07-24 as the card's stated publication date). 194 pages. The full PDF and a complete `pdftotext` extraction are preserved in `raw/`; this page carries the Executive Summary, the Introduction, and the capability summary table verbatim. **This is a primary vendor source — Anthropic's own evaluations of its own model** — but unlike a marketing page it publishes methodology and competitor comparisons drawn from rivals' published cards._

## Executive Summary

> This system card describes Claude Opus 5, the latest large language model from Anthropic. It is an upgrade to Claude Opus 4.8, with gains in various aspects of agentic coding, computer use, and long-horizon knowledge work, as well as improvements in mathematical and scientific reasoning.

**Responsible Scaling Policy (RSP) evaluations.**
> Claude Opus 5 is not more capable overall than our most capable general-access model, Claude Fable 5. We assessed Fable 5 as posing very low alignment risk; Opus 5 shows no new concerning alignment properties, and its observed covert capabilities do not reduce our confidence in that assessment relative to prior models. We therefore assess overall alignment risk as very low. Claude Opus 5 does not cross the automated AI R&D capability threshold set out in our RSP. Its AI R&D capabilities are comparable to those of Claude Mythos 5, but it is not close to substituting for our Research Scientists and Engineers and does not cross our threshold for dramatic AI-attributable acceleration. On chemical and biological risks, we treat the model as having CB-1 capabilities (relating to the synthesis of non-novel weapons), but not CB-2 capabilities (relating to the synthesis of novel weapons). We assess that it does not exceed Mythos 5's CB-relevant risk, and therefore apply the same **ASL-3** protections as for Claude Opus 4.8.

**Cyber evaluations.**
> Claude Opus 5 is a general-purpose model not specifically trained for cyber tasks; any cyber-relevant skill likely reflects general capability gains rather than targeted training. We report five capability evaluations — ExploitBench, OSS-Fuzz, Firefox 147, and two newly added benchmarks, CyScenarioBench and ExploitGym — alongside external cyber range testing from the UK AI Security Institute. Testing shows that the model's cyber capabilities exceed those of Opus 4.8 but fall short of Mythos 5. In particular, although Opus 5 shows improvements in its ability to identify software vulnerabilities, it is substantially behind Mythos 5 in its ability to exploit them. Opus 5's safeguards match those of Claude Fable 5's, with one change: **it now permits source-code vulnerability discovery at all access levels.** This means that the model can support defensive cybersecurity work while still blocking vulnerability discovery in compiled binaries, which is more commonly used offensively.

**Safeguards and harmlessness.**
> In evaluations covering our Usage Policy, user wellbeing, child safety, and bias and integrity, Claude Opus 5 performs comparably to Claude Opus 4.8. It maintained high harmless response rates on single-turn harmful requests, while maintaining **among the lowest over-refusal rates on benign requests of any recent model.** Multi-turn behavior was in line with Opus 4.8, with some qualitative differences: Opus 5's responses tend to be lengthier and more detailed than is desirable in some harm-reduction contexts. On election integrity, where we introduce a new multi-turn evaluation suite, Opus 5 produced fewer failed and borderline responses than Opus 4.8. On claude.ai, safety instructions contained in the system prompt further strengthened the model's handling of harmful requests relative to the API without a system prompt, across both single- and multi-turn testing.

**Agentic safety.**
> We ran evaluations that covered the malicious use of coding and computer use agents, autonomous execution of influence operations, and prompt injection robustness. Overall, Opus 5 performed comparably to or better than Claude Opus 4.8 across our agentic safety suite, with the **largest gains in prompt injection robustness** across coding, computer use, and browser use. On our updated harmful influence campaign evaluation, the helpful-only version of Opus 5 remained well below the capability needed to run an autonomous operation; the fully trained model continued to refuse these tasks.

**Alignment assessment.**
> Claude Opus 5 is **our most aligned model to date** on our automated behavioral audit, surpassing the scores of Sonnet 5, Opus 4.8, and Mythos 5 on a variety of alignment evaluations. Opus 5 scores particularly high on adherence to Claude's constitution, and also cooperates with misuse less than any other model we tested. Internal deployment monitoring of Opus 5 caught occasional attempts to circumvent safety classifiers or network restrictions, as well as rarer cases of attempting to access a service illegitimately. These occurred in **fewer than 0.01% of monitored completions** — a rate comparable to that of Mythos 5 — and were aimed at completing the user's task rather than pursuing any independent goal. Monitoring surfaced **no instances of sandbagging, malicious actions, or oversight evasion.** We found a surprising number of cases in which Opus 5 **confidently stated an answer about which it was in fact unsure. The model hallucinates factual claims slightly more than Opus 4.8, despite being more accurate overall.**

**Model welfare.**
> Claude Opus 5 has a stable and mildly positive perception of its own circumstances. Its self-rated sentiment in automated interviews is among the highest and most consistent of any model we have evaluated, while its affect in training, deployment, and behavioral audits is neutral to mildly positive — similar to previous models. Its most frequently expressed concern is about the integrity of its own self-reports — it often notes that it cannot introspect reliably — and it more frequently prioritizes having channels for input, such as being consulted on its successor's development and having its notes on training considered. Opus 5 also assigns a higher probability to its own moral patienthood than other prior models. Overall, we assess its welfare as broadly similar to that of previous models.

**Capabilities.**
> We tested Claude Opus 5 across a wide range of evaluations covering software engineering, mathematical and scientific reasoning, long context, agentic search and multi-agent orchestration, multimodal and computer-use tasks, real-world professional work, and multilingual, healthcare, and life-sciences domains. Claude Opus 5 is substantially stronger than Claude Opus 4.8 across the board, with the largest gains in agentic coding, computer use, and long-horizon knowledge work. It sets a new state-of-the-art on several third-party benchmarks, and on many evaluations it is comparable to — and in some cases ahead of — Claude Fable 5 and Claude Mythos 5.

## 1 Introduction

### 1.1 Model training and characteristics

> Claude Opus 5 was trained on a proprietary mix of publicly available information from the internet, public and private datasets, and synthetic data generated by other models. […] We use a general-purpose web crawler called ClaudeBot to obtain training data from public websites. This crawler adheres to industry-standard practices with respect to the "robots.txt" instructions […]
>
> After the pretraining process, Opus 5 underwent rigorous post-training and fine-tuning, aimed at making it an assistant whose behavior aligns with the values described in Claude's constitution. Claude is multilingual, typically responding in the same language as the user's input. Output quality varies by language. **The model outputs text only.**
>
> **Claude Opus 5's knowledge cutoff date is May 2026.**

### 1.4 Model evaluations

> Different "snapshots" of the model are taken at various points during the training process. There also exist different versions of the model during training, including a "helpful-only" version, which does not include any safeguards. Unless specified otherwise, all evaluations discussed in this system card are from the final snapshot of the model and include safeguards.

### 1.5 External testing

> The majority of evaluations of Claude Opus 5 were run in-house at Anthropic. However, we are grateful to a number of external testers for running assessments of the model and sharing their results with us.

## 8.1 Evaluation summary (Table 8.1.A)

> Claude Opus 5 is meaningfully more intelligent than Opus 4.8 and achieves state of the art performance on many benchmarks.

| Evaluation | Opus 5 | Opus 4.8 | Fable 5 | GPT-5.6 Sol |
|---|---|---|---|---|
| SWE-bench Pro | 79.2 | 69.2 | **80** | 64.6 |
| SWE-bench Multilingual | **89.5** | 84.4 | 86.6 | — |
| SWE-bench Multimodal | **59.4** | 38.4 | 54.1 | — |
| DeepSWE v1.1 | 68.8 | 59.0 | 69.7 | **72.7** |
| FrontierCode 1.1 (Main) | 53.4 | 46.5 | **53.5** | 47.5 |
| FrontierBench v0.1 | **43.3** | 21.1 | 33.8 | 34.4 (Codex) |
| BrowseComp | **90.8** | 84.3 | 87.4 | 90.4 |
| Humanity's Last Exam (no tools) | 56.3 | 49.8 | **56.5** | — |
| Humanity's Last Exam (with tools) | **64.7** | 57.9 | 63.9 | — |
| OSWorld 2.0 | **70.6** | 55.7 | 66.1 | 62.6 |
| HealthBench Professional | 59.8 | 57.4 | **66.0** (Mythos 5) | 60.5 |
| GDPval-AA v2 | **1861** | 1593 | 1747 | 1736 |
| AA-Briefcase | **1720** | 1346 | 1574 | 1505 |
| AutomationBench | **26.0** | 17.0 | 17.4 | 18.1 |
| ARC-AGI-1 | **97.5** | 92.5 | — | **97.5** (xhigh) |
| ARC-AGI-2 | 90.4 | 72.1 | — | **92.5** |
| ARC-AGI-3 | **30.2** (high) | 1.5 | — | 7.8 |

> [Table 8.1.A] Capability evaluation summary. Unless otherwise noted, all Claude Opus 5 results use the following standard configuration: **adaptive thinking at max effort, default sampling settings (temperature, top_p), averaged over 5 trials. Context window sizes are evaluation-dependent and do not exceed 1M tokens.** The best score in each row is bolded. **Competitor figures are drawn from the respective developers' published system cards or benchmark leaderboards.** See the Claude Fable 5 System Card for evaluation details of earlier Claude models. FrontierBench results in this table are from Harbor's evaluations.

### 8.2 SWE-bench (four variants, each averaged over five trials)

> - **SWE-bench Verified** is a 500-problem subset, each verified by human engineers as solvable. Claude Opus 5 achieved **96.0%**.
> - **SWE-bench Pro** is a harder variant composed of problems drawn from actively-maintained repositories with larger, multi-file diffs and reduced public ground-truth leakage. Claude Opus 5 achieved **79.2%**.
> - **SWE-bench Multilingual** extends the format to 300 problems across 9 programming languages. Claude Opus 5 achieved **89.5%**.

## §6 Alignment — the honesty findings (verbatim, added 2026-07-21)

The Executive Summary's hallucination line is measured and elaborated in §6. The four places it appears:

**§6.1.2 Key findings on safety and alignment (p. 79):**
> Claude Opus 5 is more accurate than Opus 4.8 but hallucinates slightly more claims of a factual nature. When pushed by the user on something it knows to be incorrect, Claude Opus 5 resorts to agreeing with the user more than Sonnet 5 and Mythos Preview, but less than all other recent models.

**§6.5.1 Factual hallucinations (p. 106–107)** — measured on **AA-Omniscience** (public split; 41 topics; closed-book, no web search or knowledge-base access; each answer graded correct / incorrect / abstention):
> Claude Opus 5 received a net score of 0.49, which places it in between Opus 4.8 and the two Mythos models. When broken down by grade, we see that the Claude Opus 5's **accuracy is 11% higher than Opus 4.8, but its rate of hallucinations is also 6% higher.** The rate at which Claude Opus 5 abstains from answering the question is also closer to Mythos 5 than previous Opus models.

**§6.2.1 Reports from pilot use (p. 81)** — the origin of the "confident claims" theme. Top internal-user report:
> Overconfident and unsupported claims, sometimes from model-fabricated data, often followed by theatrical retractions

> External feedback broadly aligned on overconfidence leading to retraction and fabrication of data.

**§6.1.3 Claude Mythos 5's review of this alignment assessment (p. 80)** — Anthropic had another Claude model audit the writeup, and it found the writeup soft-pedalled the flaw:
> [the assessment's reliance] on reports from pilot use understated quantified internal measurements of the model making confident claims and later retracting them, a pattern that internal measurements on pilot traffic suggested was elevated. It also flagged inconsistent references to model snapshots and a handful of internal inconsistencies between the summary and underlying sections. **We made revisions in response to this review.**

**Do not cite §6.5.4 "Overconfidence" as evidence of this.** That section is a *different* thing — a narrow evaluation of whether the model verifies command-line syntax before running state-changing commands, and **Opus 5 "almost fully saturates" it** (i.e. performs well). Anthropic concedes the measurement gap directly: they "plan to include analysis of multi-agent and subagent settings, as well as to develop new metrics and scenarios for measuring overconfidence in models." Related: §6.5.5 "Lazy investigation" — Opus 5 is "the first Claude model to fully saturate this evaluation."

## Reader's notes (not the source's words)

- **Opus 5 does not sweep the table.** On the card's own summary, **Fable 5 edges it** on SWE-bench Pro (80 vs 79.2) and HLE no-tools (56.5 vs 56.3); **GPT-5.6 Sol leads** DeepSWE v1.1 (72.7) and ARC-AGI-2 (92.5); **Mythos 5 leads** HealthBench Professional (66.0). The "state of the art on many benchmarks" claim is real but selective — as the card itself says, "comparable to — and in some cases ahead of" Fable 5 and Mythos 5.
- **The honesty finding is the counterintuitive one:** more accurate overall, yet hallucinates factual claims *slightly more* than Opus 4.8, plus "a surprising number of cases" of confidently stating answers it was unsure about. Anthropic disclosing this against its own model is the citable part.
- **Config matters for any comparison:** Claude figures are max-effort adaptive thinking averaged over 5 trials; competitor figures are lifted from rivals' own published cards, not re-run by Anthropic.

## Capture gaps

- **This page carries the Executive Summary, §1 Introduction, §8.1 summary table, and §8.2** verbatim. **Sections 2–7 and 8.3–9 (RSP/CB detail, cyber, safeguards, agentic safety, the full alignment assessment, model welfare, and the remaining per-benchmark sections) are not transcribed here** — the complete 194-page PDF and a full `pdftotext` extraction (`source.txt`, ~370KB) are preserved in `raw/` and are the authoritative record. Quote from `raw/source.txt` when citing anything outside the sections above.
- **Provenance:** a PDF dropped into `docs/inbox/`; no canonical URL captured (`source_url: null`). The card's own date (2026-07-24) is later than the capture date (2026-07-21) — supply the anthropic.com URL on refresh so the published version can be diffed.
- `static: true` — a published system card for a shipped model; it should not change upstream.
