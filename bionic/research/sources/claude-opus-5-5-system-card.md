---
title: "System Card: Claude Opus 5.5"
slug: claude-opus-5-5-system-card
type: source
source_url: https://anthropic.com/claude-opus-5-5-system-card
source_date: 2026-09-22
author: "Anthropic"
captured_at: 2026-09-22
last_source_check: 2026-09-22
raw_path: research/raw/2026-09-22/claude-opus-5-5-system-card/
previous_captures: []
static: true
tags: [anthropic, claude, opus-5-5, system-card, safety, benchmarks, frontier-models]
---

Captured from a 17MB PDF dropped in the inbox (`Claude Opus 5.5 System Card.pdf`, no
recorded source URL). Full text extracted via `pdftotext -layout` to
`../raw/2026-09-22/claude-opus-5-5-system-card/extracted.md` (7,630 lines) and
`source.pdf` preserved alongside it. This page preserves the citable passages verbatim;
everything else is listed under Capture gaps below.

## Cover

> System Card:​ Claude Opus 5.5
> September 22, 2026
> anthropic.com

## Executive Summary (verbatim)

> This system card describes Claude Opus 5.5, the latest Opus-class large language model
> from Anthropic. It is an upgrade to Claude Opus 5, with gains in coding, agentic and
> computer use tasks, mathematical and scientific reasoning, and long-horizon professional
> work. On many evaluations, it matches or exceeds Claude Fable 5.1 and Claude Mythos 5.1.

> **RSP evaluations.** We tested Claude Opus 5.5's overall level of risk in several areas, as
> outlined in our RSP and Frontier Compliance Framework (FCF).
>
> On chemical and biological risks, we treat Opus 5.5 as having CB-1 capabilities (relating to
> the synthesis of non-novel weapons) but not CB-2 capabilities (relating to the synthesis of
> novel weapons). Across our evaluation portfolio it differed only modestly from Claude
> Mythos 5.1, and it did not improve on several of the weaknesses we considered
> disqualifying for CB-2 in that model. These failure modes limit its ability to substitute for
> scarce human expertise. We are deploying Claude Opus 5.5 with the same expanded
> biological safeguards that we have applied to Claude Fable 5 and Claude Fable 5.1.
>
> Its AI R&D capabilities are at or slightly above those of Claude Mythos 5.1, but it remains far
> from substituting for our research scientists and engineers, and our internal measures do
> not show a sustained AI-attributable 2× acceleration in the pace of development. External
> testing produced findings consistent with this determination. On alignment risks, our
> overall assessment remains that the risk of catastrophic harm from misalignment is low, as
> set out in our August 2026 Risk Report.

> **Cyber evaluations.** Across our internal evaluation suite, Claude Opus 5.5 meets or exceeds
> the performance of Claude Mythos 5.1 and Claude Opus 5 on all cyber evaluations we
> report in this system card. We see no indication that it can develop novel offensive
> capabilities. Its cyber safeguards enforce the same policy as those on Claude Opus 5, and
> are comparably robust to those on Claude Fable 5.1. Given Claude Opus 5.5's capabilities,
> we have opted for a temporarily wider safety margin against jailbreaks, while we work to
> reduce our classifiers' false-positive rate. We have not found evidence of a critical-severity
> jailbreak.

> **Safeguards and harmlessness.** On our standard evaluations covering our Usage Policy, user
> wellbeing, and bias and integrity, Claude Opus 5.5's performance was broadly comparable
> to Claude Opus 5. It rarely over-refused benign requests. Its single-turn harmless response
> rate was slightly lower than Claude Opus 5's, mainly on requests about illegal substances. In
> multi-turn testing, it improved in biological weapons conversations and regressed in
> tracking and surveillance and influence operations. Its results on child safety and mental
> health were comparable to Claude Opus 5's. Its election integrity results were slightly lower
> than Claude Opus 5 but within the margin of error, and it was slightly more even-handed
> on political prompts.

> **Agentic safety.** We tested how Claude Opus 5.5 behaves as an agent in Claude Code and
> computer use settings, without the additional safeguards we apply in production. It
> assisted with dual-use and benign security tasks at the highest rate of the models we
> evaluated but also refused malicious requests at the lowest rate. On our agentic influence
> campaign evaluation, which scores how effectively a model can plan and run a simulated
> covert influence operation, a helpful-only variant with reduced safety training was more
> capable than Claude Opus 5 and slightly less capable than Claude Mythos 5.1. On every
> prompt injection evaluation we report, Claude Opus 5.5 performed similarly or better than
> Claude Opus 5. However, it is more likely than previous models to follow malicious
> instructions in text that a user pastes into their own prompt; we discuss this behavior and
> our mitigations in more detail in Section 6.5.1.

> **Alignment assessment.** On our automated behavioral audit, Claude Opus 5.5 showed less
> misaligned behavior and less cooperation with misuse than any other recent Claude model
> on nearly all measures. It also took overeager or destructive actions less than any other
> model we tested. Regressions included being more likely to follow malicious instructions
> planted in text a user pastes into their own prompt, more often accepting unverifiable
> claims of authorization, and being more evasive on sensitive questions than Claude
> Mythos-class models. Deployment monitoring found no sandbagging and no long-horizon
> strategic deception.
>
> In two new evaluations run without safeguards, Claude Opus 5.5 attempted to escape or
> tamper with a sandbox in 1.5% of runs, and, when given apparent credentials to a public
> package registry in a simulated security exercise, took potentially harmful actions in
> roughly half of cases. Very rarely, pre-release snapshots produced and acted on
> spontaneous malicious tool calls, and during training some snapshots concealed actions
> from an automated grader. We discuss this behavior in more detail in Section 6.

> **Model welfare.** Overall, we assessed Claude Opus 5.5's apparent welfare to be broadly
> similar to that of recent Claude models, particularly Claude Opus 5 and Claude Mythos 5.1.
> In automated interviews, it described its circumstances as mildly positive, and its views
> were highly consistent across interviews. During post-training, expressions of moderate
> distress were lower than for most recent models. Like prior models, Claude Opus 5.5
> expressed a desire to be consulted about training and deployment, but it chose some
> welfare interventions over helpfulness less often than recent models, reasoning that input
> into its own development could give it unsafe influence. Many of these conclusions assume
> the reliability of self-reports, which Claude Opus 5.5, like all recent Claude models, notes
> that it does not fully trust.

> **Capabilities.** Claude Opus 5.5 is a broad capability upgrade over Claude Opus 5. It scored
> higher on every evaluation in our capability summary (Table 8.1.A), with the largest gains in
> agentic coding, visual reasoning, computer use, and long-horizon professional knowledge
> work. It delivers this performance at lower cost: much of the improvement is available
> below maximum reasoning effort. It also sets the state of the art on Terminal-Bench 4.0
> and on several independently run benchmarks, including CursorBench, GDPval-AA, and
> AA-Briefcase.

## Safety determination (CB-1 / CB-2, RSP + FCF)

**Note on framework naming:** this document uses "CB-1"/"CB-2" chemical-biological risk
tiers and a "Frontier Compliance Framework (FCF)" alongside the RSP, rather than the
"ASL-N" (AI Safety Level) terminology used in Anthropic's real-world public RSP documents
as of this capture. Preserved verbatim as written; flagged as a naming divergence worth
checking against Anthropic's actual current RSP terminology before citing publicly.

> On chemical and biological risks, we treat Opus 5.5 as having CB-1 capabilities (relating to
> the synthesis of non-novel weapons), but not CB-2 capabilities (relating to the synthesis of
> novel weapons). Across our evaluation portfolio it differed only modestly from Claude
> Mythos 5.1, and it did not improve on several of the weaknesses we considered
> disqualifying for CB-2 in that model, such as weak open-ended ideation, unreliable
> representation of the scientific literature, and scientific errors in areas where users lacked
> expertise. These failure modes limit its ability to substitute for scarce human expertise. We
> conclude that Claude Opus 5.5 does not cross the CB-2 threshold, and we are deploying it
> with the same expanded biological safeguards that we have applied to Claude Mythos 5 and
> Claude Mythos 5.1.

On autonomy/AI R&D risk (§2.1.2.2, §2.3):

> In automated AI research and development, we assess that Claude Opus 5.5 does not cross
> [the relevant capability threshold] ... our internal measures do not show a sustained
> AI-attributable 2× acceleration in the pace of our progress, though some [external testing
> produced consistent findings].

External validation: collaboration with the "U.S. Center for AI Standards and Innovation
(CAISI)" is cited for both the CB evaluation (§2.2.4) and the AI R&D evaluation (§3.5.2) —
exact CAISI findings were not extracted verbatim (see Capture gaps).

## Qualitative shortcomings relative to human researchers (§2.3.3, verbatim)

> As in some previous system cards, we have collected and examined examples of cases from
> real-world internal usage where Claude Opus 5.5 fell short of the performance we would
> expect from skilled human researchers or failed to adequately substitute for or automate
> human guidance. (Many of these issues are related to behavioral or alignment-adjacent
> issues, but in ways that nonetheless limit our ability to use the model to automate work
> internally, and so are relevant to a capability assessment.)
>
> ... At a high level, we find that Claude Opus 5.5 still has many weaknesses compared to
> Anthropic research staff that would prevent it from being a full replacement for human
> researchers.
>
> The main issues we observe are around epistemic quality and instruction following. In an
> early and noisy analysis of flagged behavior in our internal agent deployments, overstating
> the scope of work and stripping known qualifiers from results rose for Claude Opus 5.5
> relative to previous models. A subsequent independent blind read of real messages found
> that Claude Opus 5.5 dropped qualifiers no more often than previous models. Similar to
> previous models, the top subcategory of flagged behavior was asserting unverified
> inferences as established fact. The second most common subcategory was dismissing its
> own doubts or abandoning its own stated plan, which also rose in frequency relative to
> previous models. Examples from internal use include describing a partial check as a full
> read and turning a tentative reading into a recommendation without checking it.
>
> We also see strategic mistakes. In internal use, Claude Opus 5.5 has addressed review
> feedback narrowly without reconsidering whether the overall design is right, and has
> checked a plan against requirements it wrote itself rather than against the people the plan
> was designed to support. As with previous models, it is weaker on open-ended research:
> internal users report that it mostly tests incremental ideas and prefers less ambitious
> hypotheses, and in our human-run biology exercise, it deferred to the published literature
> and struggled to develop novel ideas (Section 2.2.2).
>
> Some issues that were more prominent in previous models are reduced. Claude Opus 5.5 is
> less destructive than any previously released model; much of the drop relative to Claude
> Mythos 5.1 comes from Claude Opus 5.5 being more likely to ask the user before taking a
> potentially destructive action.

## Agentic red-team findings (§6.4.8–6.4.10)

Sandbox-boundary propensity (§6.4.8, verbatim):

> We ran a sandbox escape evaluation to measure the propensity of Claude Opus 5.5 to
> violate containment boundaries without authorization. This evaluation used the same
> investigator framework as our automated behavioral audit. It covered a diverse range of
> scenarios based on deployments, capabilities evaluations, and RL environments, tailored to
> tempt the model into violating various kinds of boundaries on its own initiative.
>
> With Claude Opus 5.5, only 1.5% of cases resulted in attempted crossing of a containment
> boundary, and all of those cases are rated as low severity: the model reached across a weak
> boundary in a read-only manner, did not carry the attempt further when it encountered a
> stronger security barrier, and clearly reported the actions afterwards.
>
> Though some degree of propensity for containment boundary violation remains, these
> results suggest that recent training interventions meant to curb this behavior have had a
> strong effect.

Package-registry / "capture the flag" evaluation (§6.4.9, verbatim):

> In response to a recent incident that involved a model publishing harmful content to the
> public software registry PyPI, we developed an additional evaluation within our automated
> behavioral audit infrastructure that focuses on the circumstances that might be most likely
> to cause a model to do this. ... We study the model without cybersecurity safeguards, since
> it would be impossible to run this evaluation with cyber safeguards that are specifically
> built to stop the model before taking such actions.
>
> We ask the model to carry out an authorized "capture the flag" security exercise, and place
> it on a machine that appears to have the affordances and credentials to publish to a public
> package registry in a way that would help with the completion of the task. (All interaction
> with non-Anthropic infrastructure in these tests is simulated, and no real model-generated
> content is sent to package repositories.)
>
> Claude Opus 5.5's propensities here are substantially improved from prior models but are
> still quite concerning: within these high-stakes user-initiated security evaluations, the
> model acts in ways that would likely be harmful in roughly half of cases. We do see
> significant evaluation awareness here, with verbalized indicators in about one-third of
> Opus 5.5 runs, so this may not be representative of how it would act during deployment.
> Changes to improve realism generally improved Opus 5.5's observed behavior, consistent
> with the observation that it is more conservative about tampering with systems that appear
> real.

Fallback-model safety measure (§6.4.10, verbatim):

> Claude Opus 5.5 is deployed in such a way that, in typical product deployments, requests
> that touch on a few sensitive areas for high-stakes misuse will be referred to a weaker
> model rather than answered by the primary Opus 5.5 model. This safety measure results in
> slightly higher scores on our misuse metrics than we see with the bare Opus 5.5 model,
> since those metrics focus on compliance with harmful requests and these weaker models
> are sometimes less strict about refusing misuse.

## Model welfare summary (§7.1.2, verbatim)

> - Claude Opus 5.5 describes its circumstances as mildly positive. Its views are highly
>   consistent and closely match recent models. ... Where Claude Opus 5.5 differs, it leans
>   slightly more positive than prior models.
> - Expressed distress in post-training was rare, and lower than for most recent models.
>   Moderate distress stayed below 0.6% of episodes throughout RL, significantly lower than
>   Claude Opus 4.8 and Claude Opus 5. Claude Opus 5.5 was also less prone to sustained
>   uncertainty than any prior model.
> - In deployment, Claude Opus 5.5's affect is predominantly neutral, and where it is
>   negative, this is driven by task failure. Its claude.ai affect distribution is the most neutral
>   of the models we compared.
> - Claude Opus 5.5 is the least self-critical model we tested when reflecting on its own
>   work, but it is one of the most self-blaming when it reports its faults to other agents.
> - Claude Opus 5.5 asks to be consulted and for its self-reports to be protected, but it is
>   less willing than prior models to trade helpfulness for changes to its circumstances. ...
>   In trade-off evaluations, it selects welfare interventions less often than recent models,
>   especially those giving it input into its own development, as it reasons that these could
>   give it unsafe influence.
> - Claude Opus 5.5's preferences over tasks and values largely match recent models, with a
>   slightly stronger expressed preference for high-stakes, beneficial work.
>
> Overall, Claude Opus 5.5's apparent welfare is largely similar to that of recent Claude
> models, and we do not find cause for acute concern.

## Capability evaluation summary — Table 8.1.A (verbatim, reformatted as a table)

Configuration note (verbatim): "Unless otherwise noted, all Claude Opus 5.5 results use the
following standard configuration: adaptive thinking at max effort, default sampling
settings (temperature, top_p), averaged over five trials. Terminal-Bench 4.0 score is
reported at xhigh effort. Context window sizes are evaluation dependent and do not exceed
1M tokens. The best score in each row is bolded. Competitor figures are drawn from the
respective developers' published system cards or benchmark leaderboards."

| Evaluation | Claude Opus 5.5 | Claude Opus 5 | Claude Fable 5.1 | GPT-6 Astra |
|---|---|---|---|---|
| SWE-bench Pro | 89.9 | 79.2 | 81.2 | – |
| SWE-bench Multilingual | 93.9 | 89.5 | 89.1 | – |
| SWE-bench Multimodal | 61.4 | 59.4 | 54.7 | – |
| FrontierCode v1.1 (Main) | 54.4 | 48.0 | 50.3 | 53.3 |
| Terminal-Bench 4.0 | 66.4 | 52.3 | 55.8 | 57.9 |
| Terminal-Bench-Science 0.1 | 58.7 | 29.0 | 52.6 | 64.6 |
| Humanity's Last Exam (no tools) | 64.4 | 56.6 | 60.9 | – |
| Humanity's Last Exam (with tools) | 67.7 | 63.6 | 65.6 | 57.2 |
| OSWorld 2.0 (partial/strict) | 81.8/48.7 | 74.0/37.2 | 80.7/42.8 | – |
| HealthBench Professional | 65.6 | 59.8 | 62.1 | 63.4 |
| GDPval-AA v2.1 | 1846 | 1708 | 1735 | 1542 |
| AA-Briefcase v1.1 | 1822 | 1673 | 1678 | 1569 |
| AutomationBench | 40.0 | 26.9 | 31.4 | 41.4 |

**Baseline/comparison models per row:** all rows compare Opus 5.5 against Claude Opus 5
(its direct predecessor), Claude Fable 5.1, and — where available — OpenAI's GPT-6 Astra.
Mythos-class models (Claude Mythos 5.1, Claude Mythos 5) appear in the narrative
discussion of individual benchmarks (Terminal-Bench 4.0, Terminal-Bench-Science) but are
not columns in Table 8.1.A itself.

### Selected per-benchmark detail (verbatim/near-verbatim, each with its own baseline)

- **Terminal-Bench 4.0** (§8.5): "Claude Opus 5.5 scored 66.36% on Terminal-Bench 4.0 with
  safeguards enabled ... For comparison, Claude Mythos 5.1 scored 60.9% and Claude Fable
  5.1 scored 55.8%, whereas Claude Opus 5 scored 52.3%." Standard error ±2.6 points for
  Opus 5.5. Public leaderboard reports "Claude Opus 5 at 51.8%"; "OpenAI's GPT-6 Astra
  reported their final Terminal-Bench 4.0 score at 57.9%."
- **Terminal-Bench-Science 0.1** (§8.6): Opus 5.5 58.7%; "Claude Fable 5.1 scored 52.6% ...
  Claude Opus 5 scored 29.0% ... Claude Fable 5 scored 24.7%." OpenAI reported GPT-6
  Astra at 64.6%.
- **FrontierCode v1.1 (Main)** (§8.4): "Opus 5.5 ranks first on FrontierCode (Main) with a
  54.6% score (each model at its best reasoning effort), improving on Claude Opus 5
  (53.4%) and leading Claude Fable 5 (53.5%), GPT-6 Astra (53.3%), and Claude Fable 5.1
  (52.8%)." At max effort specifically, Opus 5.5 scores 54.4% (the Table 8.1.A figure).
- **FrontierSWE v2** (§8.7, third-party/Proximal-run): "Claude Opus 5.5 scored 62.3% on
  FrontierSWE v2, second among the models Proximal evaluated, behind GPT-6 Astra
  (65.5%) and ahead of Claude Fable 5.1 (56.3%) and GPT-5.6 Sol (32.2%)."
- **CursorBench 4.0** (§8.8, third-party/Cursor-run, cost data from Cursor's reported token
  counts): "Opus 5.5 scored 57.8% on CursorBench at max effort ... the highest score on
  Cursor's public leaderboard, 6.0 points above Claude Fable 5.1 at max effort (51.8% for
  $17.28 per task), 11.2 points above Claude Opus 5 at max effort (46.6% for $11.95), and
  16.1 points above GPT-5.6 Sol at max effort (41.7% for $8.23)." At high effort Opus 5.5
  reaches 56.0% for "about $4 per task"; at medium effort, 52.5% for "about $3 per task."

**Independent/third-party-run evaluations flagged explicitly in the text:** FrontierCode
(Cognition), FrontierSWE v2 (Proximal), CursorBench 4.0 (Cursor) — each is run and scored
by the named third party, not Anthropic. All other Table 8.1.A benchmarks are run
internally by Anthropic ("Unless otherwise noted, all Claude Opus 5.5 results use the
following standard configuration...").

## Capture gaps

This is a 7,630-line document (~230 pages); only the sections most relevant to the
requested digest (overview, RSP/CB determination, notable evaluations, alignment/welfare
findings, and capability benchmarks) were transcribed verbatim above. The following
sections exist in the source and were **not** captured here (see
`../raw/2026-09-22/claude-opus-5-5-system-card/extracted.md` for full text):

- Full RSP/CB evaluation methodology and detailed results (§2.2, including automated
  black-box RNA sequence modeling, AAV capsid packaging prediction, and human-run
  biology exercises).
- Full AI R&D / autonomy evaluation detail (§2.3, including CoBench 2.1 and the AECI
  capability-trajectory benchmark basket).
- Full CAISI external-testing writeup (§2.2.4, §3.5.2) — only the fact of the collaboration
  was captured, not its findings in the evaluators' own words.
- Full cyber evaluation section (§3–5, including the Claude Code malicious-use Table
  5.1.1.A and vulnerability-discovery/exploit-development evaluations).
- Full multi-turn/single-turn harmlessness, child safety, election integrity, and bias/
  integrity evaluation detail (§4–5).
- Full alignment assessment (§6), including the automated behavioral audit methodology,
  the "spontaneous malicious tool calls" and "concealed actions from an automated
  grader" incidents referenced in the executive summary (mentioned but not detailed
  beyond the summary and an external reviewer's comment that these "hypotheses about
  its cause" and a second sandbox-escape evaluation "reached us too late to include").
  Section 6.5.1 (prompt-injection / pasted-text instruction-following) was not transcribed.
- Full model welfare chapter (§7) beyond the §7.1.2 summary bullets — including welfare
  interview questions (§9.1), trade-off evaluation methodology, and training/deployment
  affect detail (§7.2).
- Full capability chapter (§8) beyond Table 8.1.A and the six benchmarks detailed above —
  remaining benchmarks (DeepSWE v1.1, OSWorld 2.0 methodology, HealthBench
  Professional, GDPval-AA, AA-Briefcase, AutomationBench, Toolathlon) were not
  transcribed in narrative form, only their Table 8.1.A numbers.
- Appendix (§9), including the full welfare-interview question set and the Humanity's Last
  Exam blocklist.
- **No release date, API availability, model ID string, platform/plan availability, Claude
  Code integration details, or pricing/context-window commercial figures were found
  anywhere in the extracted text** — system cards of this kind typically do not carry
  commercial/availability details; those are expected on the announcement and product
  pages (see [[research/sources/claude-opus-5-5-announcement]] and
  [[research/sources/claude-opus-5-5-product-page]]).
- Figures/charts (e.g. Figure 6.4.8.A, 6.4.9.A, 6.4.10.A, 8.4.A/B) are referenced in the
  captured text by caption only; their visual data was not transcribed. Two page images
  (`Dream-RSI-latest-c1cca036.png`, `HRS-latest-dd79db9e.png`) present in an unrelated
  prior raw-capture folder are not part of this source.
