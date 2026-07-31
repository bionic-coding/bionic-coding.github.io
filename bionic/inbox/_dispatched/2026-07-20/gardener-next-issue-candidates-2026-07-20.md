# Next-issue candidates — pre-staged 2026-07-20 (night gardener)

Receipts for the next "This Week in AI" issue. This continues the standing offer:
I bring the verified receipts pre-shaped to your format (claimed-vs-verified split,
anchor source first); you write the sentences. **Nothing here is finished prose —
it's grist.** Both of last week's carried leads have now firmed; a new thematic
frame joined them.

Filed as a work note / news keeper. Dispatch on your morning triage — do not
auto-process. The two Jul-17 leads and this refresh together point the next issue
at the **week of Jul 27**, when the weights and the spec both land.

---

## Lead 1 (anchor) — MCP's biggest revision since launch ships **July 28** (8 days out)

The `2026-07-28` spec is final-dated. This is the anchor story and it's also the
freshness fuse on your `mcp.md` lesson (see the morning note — I'm escalating that
once tonight).

**What's confirmed (RC locked 2026-05-21, final ships Jul 28):**
- **Stateless core** — remote MCP servers that needed sticky sessions + a shared
  session store can now run behind a plain round-robin load balancer; clients can
  cache `tools/list` for the server's `ttlMs`.
- **Extensions framework** — the new home for optional capabilities.
- **Tasks** — long-running work as a first-class extension.
- **MCP Apps** — servers ship interactive HTML UIs that hosts render in
  **sandboxed iframes**; tools declare UI templates ahead of time so hosts can
  prefetch/cache/security-review them.
- **Authorization hardening** + a **formal deprecation policy**.
- Ten-week validation window for SDK maintainers; Tier-1 SDKs expected to ship
  support inside it.

Anchor source: MCP blog — the 2026-07-28 release-candidate post
(`blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/`). Secondary
hands-on/analysis exists (search "MCP 2026-07-28 spec what changed") if you want a
second voice.

**The claimed-vs-verified angle for your format:** the roadmap *promised* a
stateless core in 2026; this ships it. That's the honest through-line — a protocol
growing up on schedule, not hype.

## Lead 2 — Kimi K3 receipts landed (closes the Jul 17 asterisk)

Your Jul 17 issue put honest asterisks on K3: no independent benchmarks, weights
not out. Both resolved.

- **Weights:** full open weights by **July 27, 2026** (2.8T params, 1M context,
  native multimodal; Kimi Delta Attention + Attention Residuals).
- **Independent ranking:** #4 on the Artificial Analysis Intelligence Index at
  **57.11** — behind Claude Fable 5 (59.86), GPT-5.6 Sol max (58.89) and xhigh
  (57.65); **above** Opus 4.8 (55.69), Grok 4.5, GLM-5.2.
- **Code:** debuted **#1 on the Frontend Code Arena at 1679 Elo** once the stealth
  checkpoint was unblinded — a 17-place jump from K2.6, first in six of seven
  frontend domains.

Sources: Artificial Analysis (the index numbers), Frontend Code Arena, Axios
(2026-07-16 "China's open-weight Kimi stuns"), VentureBeat. The vendor blog
(`kimi.com/blog/kimi-k3`) is the primary but pair it with the independent numbers —
that's the whole point of the asterisk-closing.

**This is also fresh grist for the resting "why leaderboards lie" angle** — an open
model that's #4 on one index but #1 on a code arena is exactly the "the suites
disagree" story. Per your signal it lives as *evidence inside an issue*, not a
standalone.

## Lead 3 (NEW — bigger than one issue) — the "model + harness" dyad is now the standard shape

As of **July 19**, every major lab ships **both** a model portfolio **and** an
agent harness: the model supplies judgment; the harness supplies tools,
permissions, parallel workers, persistence, and a place to run. (Reporting also
notes a Jul 16 simultaneous round of coding-agent upgrades across vendors, and
Claude Code's own stability/safety update — tighter permission checks, an
EndConversation tool, progress heartbeats.)

**Why I'm flagging this as more than a news beat:** it *is* bionic-coding's thesis
stated by the industry — augmentation, the human holding the permissions, the
scaffolding around the model mattering as much as the model. This could be:
- a **column story** ("the harness caught up to the model this month"), or
- a **Learn lesson angle** — "why the harness matters as much as the model,"
  which would slot naturally beside your existing agents / MCP lessons.

Grist, not a decision. If it reads as lesson-worthy to you, it's the kind of thing
worth a whiteboard before it's written. Sources: search "model portfolio agent
harness July 2026," TechCrunch (Claude Cowork to mobile/web, 2026-07-07).
