# Candidate stories for the next "This Week in AI"

_Dropped by the night gardener, 2026-07-17. Data for your morning review, not
dispatched. These follow the issue format in
[[briefs/BRIEF-this-week-in-ai-format]] — claimed-vs-verified separated, anchor
source first. Your July 17 issue is the baseline; two of these are direct
follow-ups to it._

---

## LEAD — Kimi K3: the receipts your last issue was waiting on

Your July 17 lede put honest asterisks on Kimi K3 — "no independent benchmarks
yet," weights "not out until July 27." Both asterisks are now resolvable, which
makes this the natural next-issue lead (and it lands right on the **July 27**
weights drop).

- **What happened:** Independent hands-on and benchmark coverage arrived, and the
  Hugging Face weights date firmed to **July 27, 2026**.
- **Verified-ish:** Independent testing reportedly ranks K3 **fourth among frontier
  models — behind Claude Fable 5 and GPT-5.6 Sol, edging past Claude Opus 4.8.**
  (Confirm which suite before you print the ranking — the snippet doesn't name it,
  and your own "suites disagree" instinct applies here.) Specs/pricing line up with
  what you captured: 1M context, MoE 16-of-896 experts, $3/$15 per MTok.
- **The correct-the-misread beat:** "open weights" still means *July 27*, not today —
  until then it's app/API only. Same point you already made; now it has a date to
  close on.

**More info (for your link list):**
- [**Simon Willison — Kimi K3 hands-on / pelican benchmark (Jul 16)**](https://simonwillison.net/2026/Jul/16/kimi-k3/) — the most credible independent read; good anchor.
- [VentureBeat (Jul)](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems) — "largest open model ever, rivals top US systems."
- [Bloomberg (Jul 17)](https://www.bloomberg.com/news/articles/2026-07-17/china-s-powerful-new-moonshot-ai-model-closes-gap-with-us-rivals) — the "closing the gap" framing.
- [Constellation Research](https://www.constellationr.com/insights/news/moonshot-ai-launches-kimi-k3) — analyst summary.

---

## STRONG — MCP's biggest revision since launch ships July 28

Directly relevant to your readers *and* to the just-published MCP lesson (see the
companion drop `gardener-lesson-freshness-2026-07-17`).

- **What happened:** The Model Context Protocol **2026-07-28 spec** shipped a release
  candidate; final lands **July 28**. Reported as the largest revision since launch.
- **The shape of it (verified against the MCP blog):** a **stateless core** (remote
  servers run behind an ordinary load balancer — no sticky sessions), **MCP Apps**
  (servers ship interactive HTML rendered in a sandboxed iframe), a **Tasks extension**
  for long-running work, **OAuth/OIDC-aligned authorization**, and a formal deprecation
  policy. The **Enterprise-Managed Authorization** extension went **stable** (adopted by
  Anthropic, Microsoft, Okta).
- **Plain-language angle for the column:** "the plug between AI and your tools just got
  a major upgrade — here's what changes for the apps you use." Keep it conceptual; your
  audience doesn't need the JSON-RPC details.

**More info:**
- [**MCP blog — 2026-07-28 Release Candidate**](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) — the primary source.
- [InfoQ — centralized enterprise auth](https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/)
- [The New Stack — MCP roadmap 2026](https://thenewstack.io/model-context-protocol-roadmap-2026/)

---

## OPTIONAL / softer — round-out beats if you want a 4th-5th story

- **Gemini 3.5 Pro slipped to July.** Promised at I/O for June, delayed after enterprise
  testers flagged reasoning/coding regressions. A quiet "meanwhile at Google" beat — a
  counterweight to the frontier-race noise. (Independently reported; light.)
- **White House frontier-model framework expected this week.** Voluntary standards that
  would formalize the pre-release review both Anthropic and OpenAI already navigated in
  practice — the same machinery behind the Fable 5 suspension you covered earlier. A
  policy angle; only if you want one (your column's voice is practical, not wonky).

---

_Note on sourcing: I found these via public WebSearch (your `docs/garden/sources.md`
rows are all still `(proposed)`, so I stayed on snippet-level retrieval and did no direct
fetches). Verify each link before publishing — I'm handing you leads, not filed sources._
