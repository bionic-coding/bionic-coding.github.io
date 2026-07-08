---
layout: page
title: About
permalink: /about/
---

**Bionic Coding** is a publication about a single, load-bearing idea: *code is not the asset — intent is.*

For fifty years we treated source code as the thing worth preserving — versioning it, guarding it, mourning it when it rots. This site starts from the opposite premise. Code is an *intermediary*: a lossy, disposable projection of intent onto a machine. The durable artifacts are the **invariants** — the things that must survive regeneration — plus the ability to rebuild a faithful implementation from them, on demand, cheaply, and provably.

The name is deliberate. *Bionic*, not automatic. The human is not removed from the loop; the human is augmented — and the augmentation runs the opposite direction from autocomplete. The machine takes over the *manufacturing* of code. The human keeps the judgment that manufacturing cannot supply: what must be true, what must never break, and how you would know.

## What you'll find here

- **[The Manifesto]({{ "/" | relative_url }})** — the foundational statement: durable intent, disposable code. It's written in two movements — *the Steady State* (how you work once your invariants are pinned and your code is disposable) and *the Crossing* (the harder, more honest discipline of getting there from a legacy codebase whose intent was never written down).
- **Essays** working the idea into practice — pinning invariants, verifying against them, and earning disposability one module at a time.

## The stance in one paragraph

You do not maintain code; you maintain a set of pinned, executable invariants and regenerate the implementation as freely as you recompile. Data, structure, behavior, contracts, and experience are the load-bearing walls a regeneration must never move. Disposability extends exactly as far as verification reaches — so the highest-leverage work is making one more invariant testable. And on the far shore, where most software actually lives, unpinned does not mean free; it means *unsurveyed*.

---

This is a working publication, not a finished doctrine — the ideas here are meant to be argued with. Find the project on [GitHub](https://github.com/{{ site.github_username }}).
