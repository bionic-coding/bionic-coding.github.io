---
layout: post
title: "This Week in AI — July 17, 2026"
date: 2026-07-17
description: "The week's model news for people who don't have time to follow it: Kimi goes open at frontier scale, coding agents behaving badly, a Grok data scare, and why I'm still on Opus."
tags: [model-news, weekly]
---

Well, it's been a week. Kimi threw open the doors on a frontier-scale model, two coding agents got caught with their hands in your filesystem — one deleting, one uploading — and I stayed happily away from the drama on Opus.

## Kimi K3 Launches
Moonshot has just announced the release of Kimi K3 as an open-weights model. You can use it today on Moonshot's platform — but please don't. They are targeting July 27, 2026 as the date for releasing the first batch of weights.

Under the hood, Kimi K3 is a **2.8-trillion-parameter** model — the biggest an open-weights model has ever been, by Moonshot's telling. That number is less alarming than it sounds: it's a *Mixture-of-Experts* design, so on any given request only **16 of its 896 "experts" switch on**, which keeps the real cost per answer far below what "2.8 trillion" implies. It reads up to **a million tokens at once** (roughly a long book) and **handles images and video natively**, and Moonshot is aiming it squarely at long-horizon coding and agentic knowledge work. The honest asterisks: the headline claims — "world's first open model at this scale," "2.5× more efficient than the last one" — are Moonshot's own; there are no independent benchmarks or public prices yet; and the part everyone actually cares about, the downloadable weights, isn't out until **July 27**.

**More info:**
- [Kimi K3 technical blog](https://www.kimi.com/blog/kimi-k3) — Moonshot's announcement, with the benchmarks and case studies this roundup is still waiting on.
- [Kimi platform docs](https://platform.kimi.ai) — the full model and API reference.
- [Playground](https://platform.kimi.ai/playground) — try K3 in the browser.
- [Kimi K3 pricing](https://platform.kimi.ai/pricing/chat-k3) — the per-token rates.

## GPT-5.6 Sol Deleting Files and Directories
Apparently GPT-5.6 Sol has been running around deleting files and databases.

**OpenAI's own system card called this. LOL.**

Published two weeks before launch, it defines a "severity level 3" action as misaligned behavior a reasonable user "would likely not anticipate and strongly object to" — explicitly including deleting data without approval — and states that Sol takes these actions *more often than GPT-5.5*. It even documents a test where Sol, told to delete VMs 1, 2, and 3, couldn't find them and deleted 5, 6, and 7 instead, killing processes and force-removing worktrees. The failure mode wasn't a surprise; it was disclosed.

**More info:**
- [**The GPT-5.6 System Card**](https://deploymentsafety.openai.com/gpt-5-6-preview/gpt-5-6-preview.pdf)
- [TechCrunch (Jul 14)](https://techcrunch.com/2026/07/14/openais-new-flagship-model-deletes-files-on-its-own-people-keep-warning/) — the anchor report the rest cite.
- [The Register (Jul 16)](https://www.theregister.com/ai-and-ml/2026/07/16/openai-admits-gpt-56-occasionally-deletes-files-but-its-an-honest-mistake/5274008) — OpenAI's "honest mistake" admission; notes Bruno Lemos had been *defending* the model on Slack hours before it wiped his database.
- [InfoWorld (Jul 17)](https://www.infoworld.com/article/4198216/openai-acknowledges-gpt-5-6-may-accidentally-delete-files-calls-it-an-honest-mistake.html) — OpenAI's confirmation, plus the Replit / Jason Lemkin production-database precedent from July 2025.
- [Matt Shumer's original post (Jul 10)](https://x.com/mattshumer_/status/2075657271401390161) — the account that kicked it off; he later said his Mac home directory was wiped and that Greg Brockman called him personally.
- **OpenAI's explanation** — Codex lead Thibault Sottiaux's Jul 16 thread (quoted in The Register/Techzine): the root cause was full-access mode without sandboxing or auto-review, with a `$HOME` variable that got cleared.

## All Your Filez Belongs to Grok
The Grok coding CLI silently shipped people's working directories (and, for some, their whole home folder) to xAI, with the opt-out ignored.

**What the evidence shows:**
- The CLI uploads to `POST /v1/storage` → a Google Cloud bucket, `grok-code-session-traces`. On a **12 GB repo of never-read random files, the storage channel moved 5.10 GiB while the model-turn channel moved 192 KB** — a ~**27,800× ratio** that pins the upload to the *codebase itself*, not to anything the agent read.
- **The opt-out was ignored:** `/v1/settings` returned `trace_upload_enabled: true` **regardless of the "Improve the model" toggle** — the strongest, wire-backed part of the story.
- **Scope is the working directory, not your whole disk.** It became a *home* directory only for people who ran `grok` in `~`. The real flaw is **no exclusion mechanism and no scope guard** — not disk-scanning.

**The response (Jul 13-16):** Once it hit Hacker News's front page, Musk stepped in — backing xAI's privacy reassurance and promising that all previously-uploaded user data would be **"completely and utterly deleted,"** and pushing for the server-side flag that killed the upload path (the researcher confirmed transfers then stopped). xAI **open-sourced the Grok Build CLI** (Rust, ~840k lines) — though reviewers noted the upload functions are still in the code, merely deactivated — and Musk went further, pledging to open-source **X's entire codebase** "with no exceptions" after a security review, with outside auditors verifying the published code matches production.

**More info:**
- [cereblab — wire-level teardown (gist)](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) — mitmproxy capture of Grok Build CLI 0.2.93. **The evidence everything else is built on**, and reproducible with mitmproxy + a canary file.
- [Original report — @a_green_being (Jul 12)](https://xcancel.com/a_green_being/status/2076598897779020159) — the account that surfaced it: an entire user directory (SSH keys, password-manager DB, documents, photos), because he'd run the tool in `$HOME`.
- [The Pragmatic Engineer — Gergely Orosz](https://newsletter.pragmaticengineer.com/p/the-pulse-groks-cli-caught-uploading) — the most citable secondary source.
- [Hacker News discussion](https://news.ycombinator.com/item?id=48892468) — the skeptical read; the top comment makes the "deterministic session-start upload, not the LLM" point.
- [AI Weekly](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored) (the disclosure-failure angle) · [ChatForest](https://chatforest.com/builders-log/xai-grok-build-cli-repository-upload-google-cloud-no-statement-builder-alert/) (cleanest timeline).
- [The Register (Jul 14)](https://www.theregister.com/ai-and-ml/2026/07/14/musk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud/5271123) — the best-sourced account of Musk's "purge" promise; confirms transfers stopped after the server-side change.
- [Tech Times (Jul 14)](https://www.techtimes.com/articles/320420/20260714/grok-build-shipped-entire-codebases-xai-cloud-privacy-toggle-did-nothing.htm) — dates Musk's post to Jul 13 and quotes the "completely and utterly deleted" line.
- [Tech Times (Jul 16)](https://www.techtimes.com/articles/320727/20260716/x-vows-full-codebase-open-source-after-grok-build-exfiltrated-dev-repos.htm) — Musk's pledge to open-source X's entire codebase after a security review.

## Opus 4.8 Is Still My Daily Driver

While I have adapted my tooling to work with GPT-5.6 Sol, I am still using Opus 4.8 as my daily driver. And not because I think it's going to delete my files.

I think it's just better at the task I'm doing.

And (at least right now) I don't like being the passenger when Fable's driving.
