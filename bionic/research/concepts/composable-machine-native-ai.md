---
title: "Composable, machine-native AI"
slug: composable-machine-native-ai
type: concepts
tags: [typesafe, composable-ai, automation, reliability]
sources: [typesafe-manifesto, introducing-system-one-models-and-jev, typesafe-introduction]
last_reviewed: 2026-09-17
---

# Composable, machine-native AI

## TypeSafe's thesis

[[research/sources/typesafe-manifesto]] argues that the main barrier to economic value is not insufficient general intelligence but difficulty integrating it into dependable software. Its proposed primitive is semantic judgment invoked from code, while exact computation and explicit control flow remain conventional software.

The manifesto makes inspectability, testing, and constraints prerequisites for composing unattended components. This is a design position, not evidence that a particular model already provides dependable decisions.

## What the appendix adds

- The company's preferred economic success criterion is global total factor productivity growth reaching 3% within five years and remaining there for ten. This is an aspiration, not a measured outcome or established forecast.
- It connects the proposal to neuro-symbolic AI: neural perception paired with symbolic reasoning, described as “smart if-statements.”
- Its contrast between human-preference training and programmatically evaluated reasoning is the company's framing. The manifesto does not supply an empirical training comparison.
- Its roadmap starts with machine-native models, then reliability for automation, then stable higher-level abstractions.

## Jev: the September 15 launch

[[research/sources/introducing-system-one-models-and-jev]] announces Jev in early access, with a waitlist. Diogo Almeida describes a new architecture, parallel sampling, and Reinforcement Learning for Calibrated Decisions (RLCD). The proposed interface accepts unstructured state and returns typed probabilistic decisions; it gives up free-form string generation. The FAQ says it is neither a small model nor an LLM, but the post does not disclose enough architecture detail to assess that characterization independently.

The launch lists $0.042 per million input tokens, free output tokens, and 70–500 ms end-to-end responses. These are dated vendor claims, not measurements we reproduced. The post notes that evaluations generally run from West Coast laptops near the service and that long-term pricing sustainability remains unproven.

### What the evaluations establish—and do not

- The headline 193.6× speed and 444.6× cost comparisons come from four internally authored workflows. TypeSafe calls these gains the higher end of expected real-world results.
- Reference answers are the average probabilities of GPT-6 Astra and Fable 5.1, not independently established ground truth. The chart's “accuracy” should be read with that definition.
- Competitor models use TypeSafe's adapter to produce compatible structured decisions and probabilities. The post acknowledges that this is slower and more expensive than asking for decisions without probabilities.
- The cost chart visually places Jev near Terra in agreement with the reference, below Sol and Opus 5, at much lower cost. It does not establish that Jev is universally more capable.
- The short side-by-side input favors Jev. Wikiracing comparisons use non-reasoning modes except Astra's lowest setting; the author says reasoning improves the LLMs' results.
- Jev supports up to 255 choices. The Wikiracing demo uses a two-stage selection for larger sets. Doom uses structured text state, not visual input.

### Type safety is not decision correctness

The opening “can’t hallucinate” claim is broader than its stated evidence. The type-safety section says Jev's plotted 0% error is **not empirical**: it follows from its claimed schema guarantee. Preventing an invalid output does not prevent a wrong but valid classification, score, or choice. The competitor error charts also use OpenRouter observations, with acknowledged routing bias.

Calibration is a separate claim: confidence should track correctness across relevant cases. This post does not independently establish calibration on a reader's workload or under distribution shift. The FAQ explicitly declines public benchmark reporting and encourages use-case evaluations.

The FAQ says TypeSafe makes its own training data and does not train on customer data. That is a vendor statement, not a review of contractual privacy or retention guarantees.

## Documentation: three decision primitives

[[research/sources/typesafe-introduction]] documents three question types against a supplied state:

| Primitive | Question | Documented result fields |
|---|---|---|
| Choice | Which listed option applies? | `choice`, `probabilities`, `confidence` |
| Score | How does the state score against a rubric? | `score`, `probabilities`, `confidence` |
| Noul | Is a statement true? | `noul`, a value from 0 to 1 |

The introduction says these question types can share one API call. Each question is evaluated independently and in parallel against the same state. Its claims of little added latency and no question-induced context rot describe the vendor's intended behavior; we have not tested them.

The programming guidance is concrete: ask one bounded question per factor, then combine results in code. Its startup-pitch example separates market size, technical feasibility, and differentiation. The programmer controls their weighting rather than asking the model to make one opaque overall judgment.

The introduction lists fewer result fields for Noul than for Choice and Score. Do not assume every primitive exposes a separate confidence field from the launch's general wording. The linked primitive and confidence pages remain follow-up sources, not captured API contracts.

This capture covers the introduction only, not the full documentation site. It does not establish authentication, SDK syntax, rate limits, or how confidence differs from a probability.

## Relevance and open questions

For Bionic Coding, the useful distinction is between delegating a whole workflow to an agent and putting a bounded model decision inside ordinary program logic. A typed interface can constrain output shape without proving semantic correctness. Reliability still needs task-specific evaluation, failure handling, and review of consequential decisions. These are our implications, not demonstrated results from the manifesto.

The undated manifesto is captured as a rolling source. Raw HTML and two image assets are preserved; duplicated responsive text and navigation are removed from the readable source, with all seven appendix entries retained once. The dated Jev announcement is a static source, including four image assets and all seven FAQ answers recovered from embedded page data. Demo videos and linked evaluation tools were not independently evaluated.
