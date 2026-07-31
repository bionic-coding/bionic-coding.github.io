---
title: "Bionic Coding"
slug: bionic-coding
type: concepts
tags: [bionic-coding, methodology, invariants, regeneration, software-philosophy]
sources: [bionic-coding-manifesto]
last_reviewed: 2026-07-07
---

# Bionic Coding

A methodology for building software in which **code is treated as a disposable build
artifact and the pinned invariants are the only durable asset**. You do not maintain
code; you maintain a set of explicitly pinned invariants plus the ability to regenerate
a faithful implementation from them on demand, cheaply and provably. *Bionic*, not
automatic: the machine takes over the manufacturing of code; the human keeps the
judgment — what must be true, what must never break, and how you would know.

Source: [[research/sources/bionic-coding-manifesto]].

## Positioning

| Approach | Source of truth | Code | Intent / invariants |
|---|---|---|---|
| Traditional | The code | Kept, guarded | Implicit, in people's heads |
| Vibe coding | The last prompt | Thrown away | Thrown away |
| **Bionic coding** | **The invariants** | **Thrown away** | **Pinned, executable, owned** |

Bionic coding throws away the code but *keeps the discipline*, relocating it from the
implementation to the invariant set.

## Two states

- **The Steady State** — invariants are pinned, code is disposable, regeneration is
  routine. Movement I describes this.
- **The Crossing** — the path from a legacy codebase (invariants real but unwritten) to
  the Steady State. Movement II describes this, in a deliberately more cautious voice.
  The manifesto's sharpest warning: "code is disposable" is true only once you are
  across; said to a team still holding unsurveyed legacy code it is dangerous.

## Movement I — the eleven factors (Steady State)

Two **practices** frame five **invariants** (the load-bearing walls a regeneration must
never move):

1. **Intent** — pinned invariants are the source of truth; code is derived. An invariant
   not written down is a hope, not an invariant.
2. **Disposability** — code is a build artifact; hold it loosely.
3. **Preserve the data** — data outlives every implementation; the only thing that cannot
   be regenerated. The most sacred pin.
4. **Preserve the shape** — the structure of data is a contract even when the code reading
   it is not.
5. **Preserve the behavior** — domain correctness rules (functional invariants) are
   invariants even when nothing at the boundary reveals them.
6. **Preserve the contracts** — pin the boundary (inbound + outbound APIs); the interior
   is fluid.
7. **Preserve the experience** — pin the user-facing behaviors, not the widgets.
8. **Verify against the invariants** — *disposability extends exactly as far as
   verification reaches.* A test suite is a sample, not a proof.
9. **Amend the invariants** — durable is not frozen; change the system by changing its
   pins, then regenerate — never the reverse.
10. **Augment, don't abdicate** — the human owns the invariants; the machine owns the
    manufacturing.
11. **Regeneration** — rebuild from intent on demand; the *capability* is the asset.

## Movement II — the Crossing (legacy → Steady State)

1. **Admit where you are** — almost all software begins on the far shore.
2. **Recover before you regenerate** — archaeology is the method, not the failure state.
3. **Unpinned is unsurveyed, not free** — on legacy code the default inverts; unpinned
   code is territory to map, never licensed to delete.
4. **Observed is not ratified** — recovery produces candidates (characterization tests
   cement bugs included); a human ratifies a candidate into an invariant.
5. **Mark provenance** — every invariant carries where it came from: `authored`,
   `recovered-and-ratified`, `observed-unratified`, `reconstructed-and-provisional`.
   Never launder a guess into a guarantee.
6. **Earn disposability, module by module** — freedom is granted per region as its
   invariants become both *ratified* and *verifiable* — a qualitative human threshold,
   never a coverage number.

## Relevance to this project

This is the founding vision document for the **bionic-coding** blog. Future blog posts,
ADRs, and briefs can cite it as the canonical statement of the methodology.
