---
title: "Measure the cost of an accepted change in the current coding workflow"
date: 2026-09-03
kind: research
item_id: garden-research-cost-per-accepted-change
origin: night-gardener
status: proposed
---

# Measure the cost of an accepted change

The September 3 column describes a working arrangement: Qwen directs, GLM supervises, and GLM Flash writes code. It also warns that token prices do not measure task cost. A small measurement of that arrangement would connect the warning to the author's own experience.

This is a research suggestion for morning review. No models were called, no experiment was run, and no results are implied.

## Question

Does the current division of work reduce total billed cost without increasing human review time or failures?

## Smallest useful comparison

Use three representative, reversible tasks with acceptance checks written before either attempt. Include one straightforward edit, one debugging task, and one task with an ambiguous requirement. Run each task once with the current division of work and once with the owner's chosen comparison workflow. Use separate checkouts, the same initial commit, and the same acceptance checks.

This is an initial observation, not a benchmark with statistical power. Record an interrupted or failed attempt rather than replacing it with a successful rerun. If the two workflows use different harnesses or permissions, describe those differences as part of the comparison.

For each attempt, record:

| Field | Why it matters |
|---|---|
| Task and initial commit | Keeps the starting work comparable |
| Model, provider, version, and harness | Makes the actual configuration identifiable |
| Input, output, cache, and retry charges | Counts the whole attempt, including supervision |
| Human review and repair minutes | Shows where cheaper tokens transfer work to the author |
| Elapsed time | Captures waiting as a separate cost |
| Acceptance result and failed checks | Keeps unsuccessful work in the denominator |
| Pricing date and promotional terms | Allows later readers to reconstruct the bill |

Report total billed cost divided by accepted changes, alongside the acceptance fraction. Report human minutes separately; do not assign them an invented dollar value. Keep subscription charges separate from API charges unless a stated allocation method makes them comparable.

## Possible output

A field note could publish the task descriptions, the acceptance checks, a small result table, and the author's explanation of what surprised them. Stop after three task pairs and decide whether the measurement changed a workflow choice. More samples are justified only if the first comparison leaves a useful question open.

## Local evidence

- `_posts/2026-09-03-this-week-in-ai.md`, especially the open Flash section and closing workflow description.
- [[briefs/BRIEF-a-third-content-stream-field-notes]] — an existing place to consider the eventual article's form; this suggestion does not choose a new content type.
- [[research/references/frontier-models-2026]] and [[research/references/open-weights-landscape-2026]] — provider and pricing context already captured.

Dispatch is deferred to the owner's morning review.
