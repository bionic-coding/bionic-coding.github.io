---
title: "Kimi K3: Open Frontier Intelligence — Technical Report"
slug: kimi-k3-technical-report
type: source
source_url: null
source_date: null
author: "Kimi Team (Moonshot AI)"
captured_at: 2026-07-21
last_source_check: 2026-07-21
raw_path: research/raw/2026-07-21/kimi-k3-technical-report/
previous_captures: []
static: true
tags: [kimi, kimi-k3, open-weights, moe, model-release, technical-report, benchmarks, vision]
---

# Kimi K3: Open Frontier Intelligence — Technical Report

_The Kimi K3 technical report (47pp), captured 2026-07-21 from a PDF dropped in the inbox. **This is the document [[research/sources/kimi-k3-docs]] flagged as missing** — that capture noted "the benchmarks and case studies live there, uncaptured" because the technical blog was unreachable. This report closes both open gaps on K3: the **activated-parameter count** and the **benchmark table**. No explicit publication date on the document; it cites Artificial Analysis data "as of July 23, 2026." Full PDF + `pdftotext` extraction in `raw/`._

## Abstract (verbatim)

> We introduce Kimi K3, a **2.8T parameter Mixture-of-Experts model with 104 billion activated parameters**, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention [63] and Attention Residuals [57], which improve information flow across sequence length and model depth. Together with **Stable LatentMoE, which effectively activates 16 of 896 routed experts per token**, and refined training and data recipes, these advances yield an approximately **2.5× improvement in overall scaling efficiency over Kimi K2** [58]. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm–system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations.
>
> Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. **While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite.** We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

Footnote 1 on the abstract page: `https://huggingface.co/moonshotai/Kimi-K3`

## The scaling argument (§1 Introduction, verbatim excerpt)

> …while the open-source model ecosystem has advanced rapidly on the second axis, it has progressed slowly on the first: many recent models remain within or slightly above the 1T-class parameter regime. As increasingly sophisticated reasoning and agentic reinforcement learning methods are applied to pre-trained foundations of similar scale, **open-source progress risks converging while the gap to the strongest proprietary systems widens.** With Kimi K3, we pursue both scaling axes together to the frontier: scaling the pre-trained foundation to unprecedented 3T-class parameters while scaling reinforcement learning, reasoning effort, and long-horizon interaction at 1M context length.

## Figure 1 — main results (verbatim scores)

**All entries "maxed out on thinking effort: max or xhigh."** Kimi K3's own row is bolded below for readability; the report bolds nothing.

### Coding

| Benchmark | Ranking (as printed) |
|---|---|
| DeepSWE | GPT-5.6 Sol 73.0 · Fable 5 70.0 · **Kimi K3 67.5** · GPT-5.5 67.0 · Opus 4.8 59.0 · GLM-5.2 46.2 |
| Terminal-Bench 2.1 | GPT-5.6 Sol 88.8 · **Kimi K3 88.3** · Fable 5 88.0 · Opus 4.8 84.6 · GPT-5.5 83.4 · GLM-5.2 82.7 |
| FrontierSWE | Fable 5 86.6 · **Kimi K3 81.2** · GPT-5.6 Sol 71.3 · GLM-5.2 67.3 · Opus 4.8 66.7 · GPT-5.5 64.9 |
| Kimi Code Bench 2.0 (Internal) | Fable 5 76.9 · **Kimi K3 72.9** · Opus 4.8 71.7 · GPT-5.5 69.0 · GPT-5.6 Sol 64.8 · GLM-5.2 64.2 |
| ProgramBench | **Kimi K3 77.8** · GPT-5.6 Sol 77.6 · Fable 5 76.8 · Opus 4.8 71.9 · GPT-5.5 70.8 · GLM-5.2 63.7 |
| SWE-Marathon | **Kimi K3 42.0** · Opus 4.8 40.0 · GPT-5.6 Sol 39.0 · Fable 5 35.0 · GPT-5.5 14.0 · GLM-5.2 13.0 |

### General & visual agents

| Benchmark | Ranking (as printed) |
|---|---|
| GDPval-AA v2 (Elo) | Fable 5 1747 · GPT-5.6 Sol 1736 · **Kimi K3 1686** · Opus 4.8 1593 · GLM-5.2 1510 · GPT-5.5 1491 |
| BrowseComp | **Kimi K3 91.2** · GPT-5.6 Sol 90.4 · Fable 5 88.0 · GPT-5.5 84.4 · Opus 4.8 84.3 |
| AutomationBench | **Kimi K3 30.8** · GPT-5.6 Sol 29.7 · Fable 5 29.1 · Opus 4.8 27.2 · GPT-5.5 22.7 · GLM-5.2 12.9 |
| JobBench | Fable 5 57.4 · **Kimi K3 54.3** · Opus 4.8 48.4 · GPT-5.6 Sol 45.4 · GLM-5.2 43.4 · GPT-5.5 38.3 |
| CharXiv (RQ) w/ tool | Fable 5 93.5 · **Kimi K3 91.3** · Opus 4.8 89.9 · GPT-5.6 Sol 89.1 · GPT-5.5 89.0 |
| Zerobench w/ tool (Pass@5) | Fable 5 46.0 · **Kimi K3 41.0** · GPT-5.5 41.0 · GPT-5.6 Sol 35.0 · Opus 4.8 34.0 |

**The report's own footnotes on this figure — carry these with any citation:**
> The GDPval-AA v2 scores are from Artificial Analysis, as of July 23, 2026.

> Note: All Fable 5 results are with potential fallbacks. All GPT-5.6 Sol results include potential cyberguards.

## Stated contributions (§1, verbatim excerpts)

> **An open frontier model.** We release the full Kimi K3 model weights, making frontier intelligence available for [the community].

> **Infrastructure for multi-trillion-parameter, million-token intelligence.** We introduce KDA systems co-designs; […] resumable sandboxes for million-token agentic trajectories; and more infrastructure innovations.

## Reader's notes (not the source's words)

- **This resolves the single most important open number on K3.** The prior capture could only say active params were "a small fraction of 2.8T." The report states **104B activated of 2.8T total** — a ~3.7% activation ratio. That is the figure serving-cost estimates need.
- **The vendor undercuts its own marketing, which makes this the citable source.** The earlier platform-docs capture led with "the world's first open-source model in the 3-trillion-parameter class." The technical report instead states plainly that K3 **"still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol."** Where the two framings differ, prefer this one — it is the more conservative claim *and* from the more rigorous document.
- **The benchmark table is still vendor-run.** These are Moonshot's numbers on Moonshot's harness (one benchmark, Kimi Code Bench 2.0, is explicitly "Internal"), with competitor results carrying the fallback/cyberguard caveats above. GDPval-AA v2 is the one third-party-sourced row (Artificial Analysis).
- **K3 does lead several rows** — ProgramBench, SWE-Marathon, BrowseComp, AutomationBench — and is within ~0.5 pt of the leader on Terminal-Bench 2.1. "Trails overall" and "leads on specific agentic/long-horizon tasks" are both true.
- **Do not merge these numbers with the Opus 5 card's table.** [[research/sources/claude-opus-5-system-card]] reports Opus 5 at GDPval-AA v2 **1861**, AutomationBench **26.0**, BrowseComp **90.8** — but that is a different report, different harness, and **Opus 5 does not appear in this report at all** (the comparison set stops at Opus 4.8). Cross-report deltas are not head-to-head results.

## Capture gaps

- **Not transcribed:** §§2–9 (architecture detail, KDA design, training/infrastructure, post-training RL, full evaluation methodology, appendices). The full 47-page PDF and `source.txt` (~265KB) in `raw/` are authoritative for anything beyond the abstract, §1, and Figure 1.
- **No license named in the report.** It links the Hugging Face repo but does not state the weights license — check the repo before making any licensing claim.
- **No pretraining token count / data scale disclosed** in the captured sections.
- **No publication date on the document**; `source_date: null`. It cites Artificial Analysis data as of 2026-07-23. `source_url: null` — a PDF drop; supply the canonical URL on refresh.
