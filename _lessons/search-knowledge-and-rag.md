---
title: Search, Knowledge, and RAG
order: 8
summary: "How AI reaches past its training date: search, memory, and RAG."
status: published
updated: 2026-07-17
---

Models have a **training cutoff** — their built-in knowledge only runs up to the data they were trained on, and it gets patchy near the end. So for a *fixed* model answering right now, the way it learns about something new — or something private, like *your* documents — is to have that information added to its **context window**, the working memory it reads before it answers. (You *can* also retrain a model on new data — that's fine-tuning, below — but that changes the model itself; everything else in this lesson feeds it context instead.)

In its most basic form, you just hand the model a document — or a URL, *if the app has a tool that fetches the page* — and it reads that into context and uses it to answer. Simple, and often enough.

But early on it was clear that pasting things in by hand doesn't scale, so a handful of techniques grew up to get the right information in front of the model at the right moment: **search**, **memory**, **fine-tuning**, and **RAG**. We're going to skip fine-tuning for now — it's a different beast, actually *adjusting the model* rather than feeding it context — and focus on the others. The thread running through all of them: none of them makes the model *know* more; they make the right facts *show up in the context* while it's answering.

## Search

The simplest reach past the cutoff is to let the assistant **search the web**. Most AI apps can now do this through **tool calling** (the [Skills]({{ "/learn/skills/" | relative_url }}) lesson): the model decides it needs current information, emits a search request, a search tool runs it, and the results come back as text in the context. From there the model answers — ideally **citing what it found** so you can check it.

I'll almost always **supplement a model's built-in web search with a dedicated search tool** — [Perplexity](https://www.perplexity.ai) is my go-to — that the model can call for up-to-date, better-sourced results. Why add one when the model can already browse? Two reasons: a purpose-built search service often returns fresher, cleaner, better-ranked results than a model's built-in browsing, and it's one consistent tool you control across whichever model you're using.

Two cautions worth burning in:

- **The app usually decides *when* to search.** In most chat apps the model chooses whether to reach for the search tool — and it'll answer from what it already knows unless it recognizes the question needs something current, which it doesn't always. (Some apps always search; some let you force it.) If freshness matters, say so: *"search for the latest…"*
- **Fresh is not the same as true.** A search result is just a web page the model read, and the web is full of wrong, outdated, and low-quality pages. Searching gets you *recent*; it does not get you *right*. Treat a cited source as a lead to verify, not a verdict.

## Memory

"Memory" here means something specific: **carrying facts or preferences across sessions** so you don't repeat yourself. Tell an assistant once that you write in British English and like short replies, and a system with memory still knows it next week.

Three things sound like "remembering" and are worth keeping straight:

- The **context window** is *this* conversation's working memory — and it **resets** when you start a new chat.
- **Memory** is a small, durable store of facts the app keeps *between* chats and quietly slips back into the context when they're relevant.
- **RAG** (below) pulls from a whole *library* on demand.

Memory shines for stable preferences and recurring facts. Its failure mode is **drift**: something you set months ago goes stale — you changed jobs, or changed your mind — and the model keeps acting on the old fact. Good memory systems let you *see and edit* what's stored; look at it now and then.

## MCP

MCP is another way to reach past the training date — a standard that lets an AI app connect the model to live tools and data (a search tool, your files, a database) so it can pull in current information without a one-off integration for each. In practice it's often the **plumbing underneath** the search and RAG you set up: the search tool above, or the document library below, frequently shows up as an MCP server.

Full picture: [MCP]({{ '/learn/mcp/' | relative_url }}).

## RAG: answering from your own material

**Search reaches the public web. RAG reaches a body of material *you* choose** — your documents, a company wiki, a database, a folder of PDFs. RAG stands for *retrieval-augmented generation*, and the plain version is exactly that order of operations: **retrieve** the handful of passages relevant to the question, then **generate** an answer from them.

Here's the mental model to keep for the whole rest of this lesson: **RAG turns a closed-book exam into an open-book test.** The model doesn't need to have memorized your handbook. When you ask, the system looks up the relevant pages and hands them over to answer from — a grounded answer, with a citation, from material the model never saw in training.

## Wikis and knowledge bases

RAG is only ever as good as the library it retrieves from. That library — a wiki, a knowledge base, a well-organized folder — is a **durable asset**: curate it once and *every* answer your assistant gives gets better. It's the idea this whole site is built on — the enduring thing isn't any single answer, it's the well-kept body of knowledge the answers are drawn from. Put the effort into the library, not just the questions.

## Why not just paste it all in?

If context is the answer, why not paste your entire wiki in and skip the retrieval? Two reasons. First, the **context window has a limit** — large in 2026, and *prompt caching* makes re-reading a big pasted document cheaper than it used to be, but it's still not infinite, and a truly large library (millions of pages) won't fit at all. Second, and more important, **more isn't better**: bury the two relevant paragraphs inside five hundred pages and the model is *more* likely to lose them — the "lost in the middle" problem — not less. Search and RAG both exist to fetch *only the relevant part* — a sharp answer from a small, on-point slice beats a fuzzy one from everything.

## RAG, step by step

Setting up RAG is a short pipeline. You rarely build it by hand — plenty of tools do it for you — but knowing the steps tells you where it can go wrong:

1. **Collect** — gather the source material.
2. **Clean** — strip the junk (nav bars, boilerplate) so you index content, not clutter.
3. **Chunk** — split it into bite-sized passages (see below).
4. **Embed & index** — turn each chunk into searchable math and store it (see below).
5. **Retrieve** — for a question, pull the most relevant chunks. Good systems don't rely on meaning-search alone: they mix it with plain keyword search and metadata filters, which catches the exact things — a name, a part number — that pure meaning-matching can miss.
6. **Rank** — reorder the candidates and keep the best few (this step is often called *reranking*).
7. **Generate** — hand those chunks to the model and have it answer *from them*, with citations — and, ideally, told to say *"not in the sources"* when the answer isn't there, rather than guessing.
8. **Evaluate** — check the results. The [Evals]({{ "/learn/prompting-and-evals/" | relative_url }}) lesson applies directly: did it retrieve the right passage, answer from it, and cite honestly?

In practice this often isn't a rigid one-shot pipeline: retrieval is frequently just *another tool the model calls* (like web search), so it can write its own query, read what comes back, and search again before answering. And most RAG failures trace back to an early step — bad chunking or a thin library — not to the model.

## Chunking and embeddings, briefly

Two bits of jargon worth demystifying, no linear algebra required.

**Chunking** is just splitting your material into passages — a few paragraphs each — because you retrieve *pieces*, not whole documents. Chunk too big and you drag in irrelevant text; too small and you slice an idea in half. It's more craft than science.

**Embeddings** are how a computer searches by *meaning* instead of by keyword. Each chunk gets turned into a long list of numbers — think of them as coordinates that place the chunk on a giant map of meaning, where passages about similar things land near each other. Your question gets its own coordinates, and retrieval simply grabs the nearest chunks. That's why RAG can surface the paragraph about "paid time off" when you asked about "vacation days" — same neighborhood on the map, different words. (The best systems keep plain keyword search *alongside* this, because meaning-search can fumble exact terms like a product code or a person's name — so they use both.)

## Knowledge hygiene

An open-book test is only as good as the book, and a neglected library quietly poisons every answer. A real knowledge base needs tending:

- **Ownership** — someone is responsible for each source.
- **Freshness** — stale docs get retrieved just as eagerly as current ones; prune or date them.
- **Contradictions** — two pages that disagree produce confident, conflicting answers. Reconcile them.
- **Access permissions** — the library should respect who is allowed to see what (see Limits).
- **Metadata** — titles, dates, and tags help retrieval find the right thing.
- **An update process** — a plan for keeping it current, not a one-time dump.

The unglamorous work here *is* the work. A tidy library beats a clever pipeline.

## Limits

RAG is powerful, and it is not magic. Where it breaks:

- **Retrieval misses.** If the right passage isn't retrieved, the model answers without it — often without noticing it's missing.
- **Bad chunks.** A passage split in the wrong place can lose the context that made it make sense.
- **Citation hallucination.** A model can cite a source that doesn't actually support its claim — or invent one. A citation is a claim, not a proof; open it.
- **Access-control leaks.** If the library isn't permission-aware, RAG can surface a document the asker was never meant to see. That's a real security risk, not a nuisance.
- **Garbage in.** Search and RAG retrieve whatever is there — wrong, outdated, and low-quality sources included.

None of this makes the model actually *know* your material. It stays an open-book test: better than guessing, and only as good as the book and the looking-up.

## Worked example

Say your company handbook runs a hundred pages, and someone asks the assistant: *"How many vacation days do I get in my first year?"*

Without RAG, the model guesses from whatever generic HR text it happened to see in training — plausible, possibly wrong. With RAG, the system:

1. turns the question into coordinates and **retrieves** the two paragraphs of *your* handbook nearest in meaning — the ones under "Paid Time Off," even though they never use the word "vacation";
2. hands *just those two paragraphs* to the model; and
3. the model answers — *"15 days in your first year, accruing monthly"* — **quoting the handbook and linking the section.**

Same model, no retraining. The only difference is that the right two paragraphs showed up in the context at the right moment — which is the whole idea behind every technique in this lesson.

## Further reading

A short, still-live (2026) list — where to go deeper.

- **[Lewis et al. — Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401)** — the 2020 paper that named the technique; the abstract alone is a clear statement of the idea.
- **[Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)** — a practical, readable writeup on making retrieval actually work well (better chunking and ranking).
- Next door: **[MCP]({{ "/learn/mcp/" | relative_url }})** (the plumbing that often connects the search tool and the library) and **[Prompting and Evals]({{ "/learn/prompting-and-evals/" | relative_url }})** (how to check a RAG system's answers).
