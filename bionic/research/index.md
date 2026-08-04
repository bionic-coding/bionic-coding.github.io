# Research index

_Last updated: 2026-08-03_

## Sources (22)

- [[research/sources/qwen3-8-max-a-new-bar-for-coding-and-cowork]] — Alibaba's Qwen3.8-Max launch post (Aug 2): **2.4T / 95B active**, full benchmark table — **Fable 5 still leads 9 of 12 coding rows, including 3 of Qwen's own 4 in-house benchmarks**; Opus 5 absent from the comparison; **weights deferred again to "next week"** — `2026-08-03` — #qwen #alibaba #open-weights #benchmarks #model-release
- [[research/sources/qwen3-8-max-qwencloud-model-page]] — QwenCloud serving page for Qwen3.8-Max: **$2/$6 per MTok** (cheapest frontier-scale model captured), 1M context / 991K input / 131K output, image+text+video input, 2M TPM — no benchmarks, no license — `2026-08-03` — #qwen #pricing #api #serving-limits
- [[research/sources/willison-kimi-k3]] — Willison's same-day K3 writeup: **resolves the spec conflict** (2.8T, announced Jul 16, weights promised by Jul 27), adds **$3/$15 pricing**, Artificial Analysis Elo 1547 / $0.94-per-task, a single "max" reasoning effort, and a suspected ~85-token hidden system prompt — `2026-08-01` — #kimi #open-weights #independent-review #llm-pricing
- [[research/sources/willison-inkling]] — Thinking Machines Lab's first open-weights model: 975B-A41B MoE, Apache 2.0, multimodal, 45T tokens — and **not frontier-class by the lab's own admission**; notably thin training-data documentation — `2026-08-01` — #inkling #thinking-machines #open-weights #training-data
- [[research/sources/raschka-notable-open-weight-models]] — Architecture notes on six open-weight releases (Nanbeige 4.2 looped depth sharing, Laguna S 2.1, Motif-3-Beta GDLA, Solar Open 2, Antares 1B, BTL-3 LoRA); corroborates that **K3 weights had not landed as of Jul 26** — `2026-08-01` — #open-weights #architecture #moe #lora
- [[research/sources/state-of-open-source-local-llms-july-2026]] — LLMCheck's 30-day recap with per-Mac-tier speeds; claims **GLM 5.2 is the first open model to beat GPT-5 and Claude on SWE-Bench Pro (68.5%)**. All figures single-source; **its Kimi K3 row is demonstrably wrong** — `2026-08-01` — #open-weights #local-llms #apple-silicon #benchmarks
- [[research/sources/qwen3-8-open-weight-announcement]] — GIGAZINE on Qwen 3.8 (2.4T) going open-weight "soon": the "second only to Fable 5" claim with **no benchmarks published**; new fact — 3.5/3.6 open, **3.7 closed**, 3.8 open again — `2026-08-01` — #qwen #alibaba #open-weights #vendor-claims
- [[research/sources/kimi-k3-technical-report]] — Kimi K3 technical report (47pp): **104B activated of 2.8T**, KDA + Stable LatentMoE, 1M context; full benchmark table; Moonshot's own verdict is that K3 **trails Fable 5 and GPT-5.6 Sol** — closes both gaps on [[research/sources/kimi-k3-docs]] — `2026-07-21` — #kimi #open-weights #technical-report #benchmarks
- [[research/sources/claude-opus-5-system-card]] — Anthropic's Claude Opus 5 System Card (194pp, card dated 2026-07-24): ASL-3, most-aligned-to-date, SWE-bench Verified 96.0, largest gains in agentic coding/computer use; **hallucinates slightly more than 4.8 despite being more accurate** — `2026-07-21` — #anthropic #opus-5 #system-card #alignment
- [[research/sources/qwen3-8-max-preview-fact-sheet]] — Alibaba's Qwen3.8-Max-Preview (WAIC 2026-07-19): 2.4T multimodal hosted preview, "second only to Fable 5" — vendor claim; **no model card, benchmarks, active-param count, or open weights yet** — `2026-07-20` — #qwen #alibaba #model-release #preview
- [[research/sources/kimi-k3-docs]] — Kimi K3 platform docs (user paste): open-weights flagship, 2.8T MoE (16/896 experts), 1M context, vision; weights by Jul 27; vendor claims unverified — `2026-07-15` — #kimi #open-weights #model-release
- [[research/sources/anthropic-introducing-fable-5-mythos-5]] — Anthropic model docs: Fable 5 specs — 1M context, 128K output, always-on adaptive thinking; closes the last frontier-models flag — `2026-07-15` — #anthropic #fable #specs
- [[research/sources/anthropic-redeploying-fable-5]] — Anthropic (Jun 30): the Fable 5 suspension cause on the record — US export controls (Jun 12) after an Amazon jailbreak report, restored Jul 1 with a new classifier; resolves the contradiction — `2026-07-14` — #anthropic #fable #export-controls #safeguards
- [[research/sources/artificial-analysis-gpt-5-6]] — Artificial Analysis: GPT-5.6 benchmarks (Intelligence Index v4.1) — Sol 59 (1 pt behind Fable) at ⅓ cost, leads AA Coding Agent Index at 80; suites disagree — `2026-07-14` — #openai #gpt-5-6 #benchmarks
- [[research/sources/judging-llm-as-a-judge-mt-bench]] — Zheng et al. 2023 (NeurIPS): the canonical LLM-as-a-judge paper; documents position/verbosity/self-enhancement bias; GPT-4 judge matches humans at >80% — `2026-07-14` — #llm-as-judge #evals #bias
- [[research/sources/llm-as-a-judge-evidently-guide]] — Evidently AI practical guide: pairwise vs direct scoring, binary-beats-scales, juries/voting, verify-the-judge — `2026-07-14` — #llm-as-judge #evals #practical-guide
- [[research/sources/gpt-5-6-pricing]] — OpenAI GPT-5.6 API pricing: Sol $5/$30, Terra $2.50/$15, Luna $1/$6 per MTok; model ids + reasoning-effort ladder (none→max) — `2026-07-13` — #openai #gpt-5-6 #pricing #api
- [[research/sources/gpt-5-6-system-card]] — OpenAI's GPT-5.6 Preview System Card (Sol/Terra/Luna): High cyber + bio/chem capability, not High on self-improvement; greater agentic-coding overreach than GPT-5.5; no pricing in the card — `2026-07-13` — #openai #gpt-5-6 #system-card #safety
- [[research/sources/simon-willison-claude-opus-4-8]] — Independent hands-on review of Opus 4.8: confirms $5/$25 pricing, 1M context / 128K output, Jan 2026 cutoff; links a GPT-5.6 writeup — `2026-07-12` — #anthropic #claude #opus #independent-review
- [[research/sources/claude-fable]] — Anthropic's Claude Fable 5 product page: the Jun 9 → Jun 12 → Jul 1 timeline, $10/$50 pricing, Mythos-level, safeguards/fallback to Opus 4.8 — `2026-07-12` — #anthropic #claude #fable #mythos
- [[research/sources/claude-opus-4-8]] — Anthropic's Claude Opus 4.8 announcement: ship date, $5/$25 pricing, effort control, dynamic workflows, Mythos class — `2026-07-12` — #anthropic #claude #opus #model-release
- [[research/sources/bionic-coding-manifesto]] — Founding manifesto: durable intent, disposable code; the eleven Steady-State factors + the Crossing — `2026-07-07` — #bionic-coding #methodology #invariants

## Concepts (2)

- [[research/concepts/bionic-coding]] — The Bionic Coding methodology: pinned invariants as the durable asset, code as disposable build artifact — sources: 1 — `last_reviewed: 2026-07-07`
- [[research/concepts/llm-evaluation]] — LLM evaluation & LLM-as-a-judge: pairwise/direct scoring, the three judge biases, and the jury/council mitigation — backs the Prompting & Evals lesson — sources: 2 — `last_reviewed: 2026-07-14`

## Decisions-context (0)

## References (2)

- [[research/references/open-weights-landscape-2026]] — Running reference for the downloadable-model landscape: the K3 spec conflict resolved against the technical report, Inkling as the US entrant, **Qwen3.8-Max now launched with a real benchmark table (95B active, $2/$6) but weights deferred a third time**, six architecture notes, and the Apple Silicon picture — with a **trust ladder** ranking the sources and claimed-vs-verified marking throughout — sources: 10 — `last_reviewed: 2026-08-03`
- [[research/references/frontier-models-2026]] — Running reference for the 2026 frontier-model landscape (**Claude Opus 5 now the current Opus flagship, from its system card**; Opus 4.8 retained as predecessor; Fable 5 + GPT-5.6 verified; **Kimi K3 shipped with a technical report** — 104B active, full benchmarks; **Qwen3.8-Max now launched** — 95B active, $2/$6, full table showing Fable 5 ahead on most coding rows, Opus 5 absent from its comparison set) — sources: 16 — `last_reviewed: 2026-08-03`

## Ideas (0)

## Meetings (0)
