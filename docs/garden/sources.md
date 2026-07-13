# News sources

Curated feeds the night gardener's news pass (`read-news`) reads. Oldest
`last_seen` first, capped per pass. **Every row below is seeded `(proposed)`** —
on the first night the gardener writes the list but treats proposed rows as
snippet-only (a search snippet is enough to judge relevance; no direct fetch).
A row becomes fully readable — and eligible to seed the network allow-list — only
when **you** remove its `(proposed)` marker. That edit is the acceptance gate.

| source | url | topics | last_seen | notes |
|--------|-----|--------|-----------|-------|
| Anthropic News | https://www.anthropic.com/news | claude, models, safety, releases | — | (proposed) |
| OpenAI News | https://openai.com/news | gpt, models, api, releases | — | (proposed) |
| Google DeepMind Blog | https://deepmind.google/discover/blog/ | gemini, research, releases | — | (proposed) |
| Simon Willison's Weblog | https://simonwillison.net/ | llm, practical, tools, hands-on | — | (proposed) |
| Model Context Protocol | https://modelcontextprotocol.io/ | mcp, tools, protocol | — | (proposed) |
| Hacker News | https://news.ycombinator.com/ | ecosystem, launches, discussion | — | (proposed) |
| Latent Space | https://www.latent.space/ | ai-engineering, interviews, analysis | — | (proposed) |
| Ars Technica AI | https://arstechnica.com/ai/ | news, analysis, policy | — | (proposed) |

_Review these and keep the ones you want. Remove `(proposed)` from a row to let
the gardener read it in full and add its domain to the egress allow-list. Delete
rows you don't want. Add your own (Perplexity, a favorite newsletter, a subreddit)
in the same shape._
