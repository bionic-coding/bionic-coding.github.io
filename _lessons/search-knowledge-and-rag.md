---
title: Search, Knowledge, and RAG
order: 8
summary: "How AI reaches past its training date: search, memory, and RAG."
status: stub
updated: 2026-07-11
---

Models have a training date and once trained the only way they can be aware of
new things is by adding information to their context window.

It the most basic form you can give the model a document or URL to add to it's 
context window, and it will use that information to answer questions and generate
responses.

But early on we recognized that wasn't enough and needed add some additional techniques to make the model aware of new things. These inlcude search, memory, fine-tuning, and RAG.

We're going to skip fine-tuning for now, and focus on the other techniques.

## Search

 - tool calling to do web searches in most models.
 - I will almost always suplement this with a Perplexity Search tool that a model can call to get up-to-date information in addition to the model's web search tool.

_TODO: how a search result actually lands in the context window; when the model decides to search vs. answer from what it already has; freshness vs. trustworthiness of results; citing what it found; built-in web search vs. an external search tool (like Perplexity) and why you'd add one._

## Memory
_TODO: what "memory" means here — carrying facts or preferences across sessions so you don't repeat yourself. How it differs from the context window (which resets each chat) and from RAG (which pulls from a library). Where it helps, and where it drifts or goes stale._

## MCP
_TODO: MCP is another way to reach past the training date — a standard that connects the model to live tools and data (a search tool, your files, a database) so it can pull in current information without a one-off integration for each. In practice it's often the plumbing under the search and RAG you set up. Keep it short here; the full story lives in its own lesson._

Full picture: [MCP]({{ '/learn/mcp/' | relative_url }}).

## RAG: answering from your own material
_TODO: the pitch — search reaches the public web; RAG reaches a body of material you choose (your docs, a wiki, a database). Retrieve the relevant passages, then answer from them._

## Wikis and knowledge bases
_TODO: curated knowledge as a durable asset — the library RAG retrieves from._

## Why not just paste it all in?
_TODO: the context-window limit — why search and RAG both fetch only the relevant parts instead of dumping everything in._

## RAG, step by step
_TODO: collect → clean → chunk → embed/index → retrieve → rank → generate with citations → evaluate._

## Chunking and embeddings, briefly
_TODO: how plain text becomes searchable math, without the linear algebra._

## Knowledge hygiene
_TODO: source ownership, stale docs, contradictory pages, access permissions, metadata, an update process._

## Limits
_TODO: retrieval misses, bad chunks, citation hallucination, access-control leaks; and search can pull wrong, low-quality, or outdated sources. None of these make the model actually "know" everything._

## Common misconceptions
_TODO: RAG is not fine-tuning and not human-style memory — it's an open-book test. A citation is not proof of correctness. A web search result is not automatically trustworthy._

## Worked example
_TODO: an employee-handbook Q&A that retrieves the two paragraphs that answer the question._

## References
_RAG explainers from reputable providers, vector-database docs, an enterprise knowledge-management source, and retrieval/citation evaluation methods; plus docs for the search tools you use (built-in web search, Perplexity). Route through crux; cite the source page._
