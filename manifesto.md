---
layout: page
title: "The Bionic Coding Manifesto"
nav_label: Manifesto
permalink: /manifesto/
description: "Durable intent, disposable code."
---

## Introduction

For fifty years we have treated source code as the asset. We version it, review it, refactor it, and mourn it when it rots. We hire around it. We let it define the shape of our teams.

This was always a category error. Code is not the asset. Code is an *intermediary* — a lossy, disposable projection of intent onto a machine, no more precious than the assembly it compiles down to. We stopped reading assembly the moment compilers earned our trust. We are now reaching the same moment with code itself.

**Bionic Coding** is a methodology for building software in which the code is understood to be throwaway, and the *invariants* — the things that must survive regeneration — are the only durable artifacts. You do not maintain code. You maintain a set of pinned invariants and the ability to regenerate a faithful implementation from them, on demand, cheaply, and provably.

The word is deliberate. *Bionic*, not automatic. The human is not removed from the loop; the human is augmented. And the augmentation runs in the opposite direction from autocomplete: the machine is not helping the human write code — the human is supplying the judgment the machine's manufacturing cannot. The machine takes over the manufacturing of code. The human keeps what manufacturing cannot supply: what must be true, what must never break, and how you would know.

## Bionic Coding vs. everything before it

**Traditional applications** treat the code as the source of truth. Everything downstream is derived from the code, and the code is derived from a developer's head. When the developer leaves, the intent leaves with them, and the code becomes an archaeological dig — one nobody chose to run.

**Vibe coding**, at least in its purest form, treats the code as throwaway but treats the *intent* as throwaway too. It is prompting without pinning: you ask, you get something that runs, you ship it, and neither you nor anyone else can say precisely what it guarantees. Fast, and fragile. It discards the discipline along with the code.

**Bionic coding** throws away the code and keeps the discipline — moving that discipline to where it belongs. The code was never the thing worth preserving. The invariants were. So pin those, make them executable, and let the implementation be regenerated as freely as you recompile.

|                     | Source of truth | Code | Intent / invariants |
| ------------------- | --------------- | ---- | ------------------- |
| Traditional         | The code        | Kept, guarded | Implicit, in people's heads |
| Vibe coding         | The last prompt | Thrown away | Thrown away |
| **Bionic coding**   | **The invariants** | **Thrown away** | **Pinned, executable, owned** |

## Two states and the crossing between them

There is a state in which Bionic Coding is simply how you work: invariants are pinned, code is disposable, regeneration is routine. Call it **the Steady State**. Everything confident in this manifesto describes that state.

Almost no one starts there. Almost all software begins on the far side — a codebase whose invariants were never written down, whose intent lives in the code itself and in the heads of people who may be gone. Between where you are and the Steady State lies **the Crossing**, and the Crossing is where every real adopter actually lives. Read the two movements as what they are — a destination, and the discipline of getting there. The Steady State's confidence is not license for the far shore: "code is disposable" is true once you are across; said on day one to a team still holding unsurveyed legacy code, it is the most dangerous sentence in the document.

---

# Movement I — The Steady State

*What Bionic Coding is once you are across. The confident voice below assumes the invariants have already been recovered, pinned, and ratified. If that is not yet true of your system, this movement describes where you are going, not where you may act.*

The factors divide into two kinds, and they read as an arc. The opening **practices** (1–2) establish the stance: intent is the source of truth, and code is held loosely. The **invariants** (3–7) are *what you preserve* — the load-bearing walls a regeneration must never move: state, structure, behavior, boundary, and experience. The closing **practices** (8–11) make the stance safe to hold: verification, amendment, augmentation, and regeneration itself.

## 1. Intent

### The pinned invariants are the source of truth; code is derived

Write down what must be true, not how to make it true. The durable artifact is the set of explicitly pinned invariants — and an invariant that is not written down is not an invariant, it is a hope. Pinning is the act of drawing the line between the contract and the implementation detail; everything on the implementation side of that line is free. Intent also includes the trail of decisions that explains *why* the invariants are what they are — keep that record, though its form is still unsettled (Architecture Decision Records are one attempt, not the answer). The codebase demotes from *the* artifact to *an* artifact: one of many valid outputs.

## 2. Disposability

### Code is a build artifact; hold it loosely

You do not hand-edit assembly and check it back in — you fix the source and recompile. Generated code earns the same status: downstream, replaceable, never guarded. Attachment to a piece of code is a smell that its intent was never captured and the code is silently acting as the specification. The goal state is that code is the cheapest, most replaceable thing you own, and the team feels free to throw it away. *(In the Steady State this is a standing freedom. On the far shore it is not yet true — disposability is earned, module by module. See the Crossing.)*

## 3. Preserve the data

### Data outlives every implementation

Files, databases, configuration, secrets, accumulated state. The invariant here is survival, not the data itself: data is the asset the pins exist to protect, and the one thing in the system you cannot regenerate — code can be rebuilt from intent; data cannot. Any regeneration that touches data must do so through explicit, reversible, verified migration, never as a side effect of rewriting the code that owns it. This is the most sacred pin in the set, precisely because it guards the only irreplaceable thing.

## 4. Preserve the shape

### The structure of data is a contract even when the code that reads it is not

Schemas, models, facades, serialization formats, the field a downstream consumer depends on being an integer. The *shape* of structured data is an interface with everything that touches it — including future versions of the app. Pin the shape; let the code that maps to and from it be regenerated at will.

## 5. Preserve the behavior

### The rules the logic must obey are invariants, even when nothing at the boundary reveals them

Some invariants are neither state, nor structure, nor a boundary promise, nor a user-facing flow — they are the correctness rules the domain itself imposes. An order's total equals the sum of its line items. A balance never goes negative. A state machine only advances along legal edges. These functional invariants are the easiest to lose, because they live only in the logic and rarely announce themselves. Pin them as properties and rules, independent of the code that currently enforces them. This is the class characterization tests most often recover — which is why it is also the class where *observed is not ratified* bites hardest.

## 6. Preserve the contracts

### Pin the boundary; the interior is fluid

Every API the system exposes and every API it depends on — inbound and outbound, synchronous calls and webhooks, public and internal. These are the promises the system makes to the outside world and relies on from it. The boundary is where regeneration is dangerous, and therefore where pinning is mandatory. Behind it, the code is free.

## 7. Preserve the experience

### Pin the behaviors users rely on, not the widgets that render them

The user has a contract too, even if it was never written down: the flow that must not add a step, the shortcut that must keep working, the latency they expect, the words on the button that support tickets reference. Capture the experience-level invariants explicitly. Then the UI implementation — components, framework, markup — becomes as disposable as any other code.

## 8. Verify against the invariants

### Disposability extends exactly as far as verification reaches

The factor that makes the rest safe — and the one place this manifesto must not overclaim. A test suite is a sample, not a proof: a regeneration that passes every pin has been shown to honor the suite, and nothing more. So the discipline is twofold.

First, make every invariant as executable as it can be — a contract test, a golden test, a property, a schema check, a migration assertion. A pinned invariant with no verification at all is decoration.

Second, be honest about the invariants that resist execution: security properties, latency budgets, concurrency behavior, resource cost. These do not stop being invariants because they are hard to test — they stop being *cheap to regenerate around*. Verification strength is a dimension of every pin, and disposability extends exactly as far as it reaches. Where verification is strong, regenerate freely. Where it is weak, the surrounding code is less disposable than you would like, and the honest move is to say so. The suite is not the definition of the system — it is the strongest available approximation, and making one more invariant executable is some of the highest-leverage work in the methodology, because every pin that becomes testable makes a region of code freer.

## 9. Amend the invariants

### Durable is not frozen; change the system by changing its pins

Requirements change. That is not an exception to Bionic Coding — it is most of what development *is* in the Steady State. A change of requirements is an amendment to the invariant set: a pin added, a pin revised, a pin retired — followed by regeneration. Never the reverse. If you find yourself changing code first, then either the change was implementation detail all along (fine, that side of the line is free) or an invariant just moved without anyone deciding it (not fine — that is how the suite and the intent drift apart until the suite is silently the wrong definition of the system).

Amendment is a judgment act, so it carries the full weight of factor 1: a human decides, the decision is recorded, and the *why* joins the decision trail. Retirement is explicit — a pin you quietly stop enforcing becomes a lie in the suite. And conflict is a feature, not an embarrassment: when a new invariant contradicts a ratified old one, the contradiction surfaces at the pin level, where it can be argued about and resolved, instead of at the code level, where it becomes a bug.

## 10. Augment, don't abdicate

### The human owns the invariants; the machine owns the manufacturing

Bionic, not automatic. Deciding what must be true, what must never break, and how correctness is proven is judgment, and judgment does not delegate. Generating, refactoring, and rewriting the code that satisfies those decisions is manufacturing, and manufacturing should be handed to the machine as completely as possible. Keep the manufacturing and you are back to traditional cost; give away the judgment and you are back to vibe-coding amnesia.

## 11. Regeneration

### Rebuild from intent on demand; the capability is the asset

The ability to regenerate the system from its invariants is worth more than any output it produces. Exercise it constantly. If regeneration is a rare, terrifying event, you have quietly slipped back into treating the code as precious. If you are holding code you could not regenerate, you do not understand it, and it owns you rather than the reverse — *and the way out is not to distrust it forever, but to recover it. That is the Crossing.*

---

# Movement II — The Crossing

*How you get from a legacy codebase to the Steady State. The voice here is deliberately more cautious than Movement I, because on the far shore certainty is the thing you have least of.*

Movement I ended on a distrust it never resolved: code you cannot regenerate owns you. Distrust is a diagnosis, not a cure. The cure is to **recover** — to turn code you cannot regenerate into invariants you can regenerate against. That work has a name the introduction used as an insult. We reclaim it here.

## i. Start by admitting where you are

### Almost all software begins on the far shore

The three-way table is not three places you might sit; it is a journey most teams have to make. Your system's invariants are real but unwritten — encoded in behavior, in schemas, in the boundary, and thinnest of all in anyone's memory of *why*. The transition is not a preamble to Bionic Coding. For most adopters it *is* the work, and pretending you are already in the Steady State is how teams delete things they did not know were load-bearing.

## ii. Recover before you regenerate

### Archaeology is the method, not the failure state

When intent is lost, the code becomes an archaeological dig — the introduction meant that as the fate of an abandoned system. Here it is the discipline that gets you out. Before you may treat any code as disposable, you excavate it: read the state, the schema, the behavior, the boundary, the flows, and the history, and lift the buried invariants into the light. The classes recover with very different confidence. Shape and contracts come almost mechanically — the schema and the boundary are already legible. Behavior comes at scale but only as *candidates*, since a characterization test captures what the code does, bugs and all — and this is the class the dig turns up most of. Data you do not recover so much as guard: it is simply there, and must survive the crossing uncorrupted. Experience you recover by observation. And the *why* barely recovers at all — it can only be reconstructed, and only provisionally. Recovery is not a phase you rush; it is the price of the freedom Movement I describes.

## iii. Unpinned is unsurveyed, not free

### On legacy code, the default inverts

This is the single most important correction to Movement I. In the Steady State, everything unpinned is free to regenerate. On the far shore, **unpinned does not mean free — it means unsurveyed.** Most load-bearing intent in old code is unpinned precisely because nobody wrote it down. To treat unpinned as disposable there is to license deleting the exact truth you have not recovered yet. Until a region is surveyed, unpinned code is unexplored territory to map, never licensed to delete.

## iv. Observed is not ratified

### Recovery produces candidates; judgment produces invariants

A characterization test cements whatever the code currently does — *bugs included*. A behavior lifted from running code is therefore a *candidate*, not an invariant: it might be a three-year-old bug you are about to make permanent. Factor 10 — augment, don't abdicate — reaches backward in time here. Recovery produces candidates at machine scale; a human converts a candidate into an invariant by examining it and deciding it is intended. What you cannot yet examine is not a failure and not a lie; it is an honest known-unknown that must be *marked* as such rather than silently promoted.

## v. Mark provenance; never launder a guess into a guarantee

### Every invariant carries where it came from

The *why* is categorically less recoverable than the *what*. Behavior, shape, and contracts you recover; intent you can only reconstruct from git history, pull requests, and tickets — and a reconstruction is a guess. So every invariant carries a provenance, and the provenance travels with it:

- **authored** — written by a human as intent. First-class.
- **recovered-and-ratified** — extracted from behavior, then examined and confirmed as intended. Trustworthy.
- **observed-unratified** — faithfully reproduced from behavior but not yet examined. A known-unknown; this is where the risk concentrates.
- **reconstructed-and-provisional** — the inferred *why*. A guess, marked as a guess, never laundered into authority.

Treating a guess as a guarantee is its own failure mode, and it is the one that hurts most later. Provenance also outlives the Crossing: when a pin is later amended (factor 9), the amendment is a human decision, so the pin is re-authored — amendment is one of the ways a recovered invariant graduates to first-class.

## vi. Earn disposability, module by module

### Freedom is granted per region as its invariants become trustworthy — not by a number

Disposability is not a state you switch on; it is a gradient you earn, and two independent questions govern it: **is the invariant real** — ratification, the judgment of iv and v — and **can we prove an implementation honors it** — verification, the strength factor 8 measures. Every combination of the two exists. Ratified and strongly verified is freedom. Ratified but weakly verified is a real invariant with narrow freedom around it — the latency budget everyone agrees is load-bearing but nobody can test reliably. Unratified but strongly verified is the trap: a passing characterization test that may be cementing a three-year-old bug, dangerous precisely because the green check makes it look trustworthy. Unratified and unverified is simply unsurveyed. A module becomes safe to regenerate to the degree the invariants around it answer *yes* to both questions — and only then does Movement I's confidence apply to it. Resist the urge to make this a metric. There is no coverage percentage that licenses deletion; line-coverage is the cautionary tale, since you can reach a hundred percent and pin nothing real. The threshold is qualitative and human: *do we trust the invariants here enough to throw the code away?* When the answer is yes for a region, that region has crossed. When it is yes everywhere, you are in the Steady State — and Movement I is simply how you live, with one caveat you carry across the water: even there, disposability extends only as far as verification reaches (factor 8). The gradient never fully disappears; it just stops being frightening.
