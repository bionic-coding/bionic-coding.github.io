---
title: Glossary
order: 11
summary: "Plain-language definitions of the words AI people throw around."
status: published
updated: 2026-07-11
---

The vocabulary of modern AI, one or two sentences each, no math required. Terms are alphabetical. Where a word has its own lesson, there's a link to it.

## Terms

**Agent** – An AI setup that doesn't just answer but takes actions in a loop: it decides on a step, does it (calls a tool, reads a file), looks at the result, and goes again until the job is done or it hits a stop. An agent is not a new kind of **model**; it's a model wrapped in that loop, with tools and permissions. Because it acts on its own, it can loop or make mistakes, so it usually runs with limits and approvals. See [Agents]({{ '/learn/agents/' | relative_url }}).

**AGI (artificial general intelligence)** – A hypothetical AI that can handle any intellectual task a person can, across the board, rather than being good at particular jobs. There's no agreed definition or test, and no agreement on whether today's systems are close. You'll mostly meet the term in headlines and debates.

**Alignment (RLHF)** – Alignment is the work of getting a model to behave helpfully and safely, so it acts like a useful assistant instead of raw autocomplete; it reduces bad behavior without fully removing it. Reinforcement learning from human feedback (RLHF) is one common method: people rate answers, and the model learns from the ratings.

**API** – A way for one piece of software to use another. An AI API lets a program send prompts to a model and get answers back, which is how apps build AI features in. If you use a chat app, it reaches the model through a backend like this; you aren't calling the API yourself.

**Benchmark** – A standard test used to compare models, like a set of exam questions or coding tasks. Benchmarks are useful but easy to over-read: topping a leaderboard doesn't mean a model is better for your actual work. See [Prompting and Evals]({{ '/learn/prompting-and-evals/' | relative_url }}) for checking output on your own tasks.

**Chain-of-thought** – When a model works through a problem in steps before committing to an answer, the way you might use scratch paper. It tends to help on multi-step problems. When a product shows you this "thinking," it's often a summary or a tidied-up trace, not a literal window into how the model works.

**Context window** – How much text a model can take in for a single reply: your prompt, the conversation so far, any documents or tool results, and the answer it's writing. It's measured in **tokens**. Go past the limit and something has to give: the app trims or summarizes older material, fetches only the relevant parts, or returns an error. The model doesn't quietly remember past its window; the app decides what fits. See [Search, Knowledge, and RAG]({{ '/learn/search-knowledge-and-rag/' | relative_url }}).

**Diffusion** – The method behind many current image and video generators. The model starts from random noise and cleans it up in steps until a picture appears that fits your prompt. It's a different technique from the next-word prediction that language models use.

**Distillation** – Training a smaller, cheaper model on a bigger model's output so it takes on much of the bigger one's behavior at lower cost and higher speed. The smaller model is the "distilled" version, and it usually gives up some capability in the trade.

**Embedding** – A way of turning text (or an image) into a list of numbers that captures patterns in its meaning, so software can measure how similar two things are. Passages about the same topic get similar numbers. Embeddings are what make semantic search and **RAG** work.

**Eval (evaluation)** – A deliberate check of whether AI output is actually good, rather than glancing at it once and moving on. An eval might be a checklist, a set of questions with known-good answers, or a scoring rubric you re-run every time you change a prompt. See [Prompting and Evals]({{ '/learn/prompting-and-evals/' | relative_url }}).

**Few-shot / zero-shot** – How many examples you put in the prompt. Zero-shot means you just ask. Few-shot means you include a couple of worked examples first to show the format or style you want. A few examples often make the output more consistent.

**Fine-tuning** – Training an existing model further on your own examples so it picks up a specific task, format, or voice. It changes the model's **parameters**. It's better at teaching style and format than at adding new facts, and it's not the same as prompting (giving instructions) or **RAG** (handing the model documents to read). In practice you rarely need it; good prompting or RAG solves most problems first.

**Foundation model** – See **Model**.

**Generative AI** – The umbrella term for AI that creates new content — text, images, audio, video, code — rather than just sorting things into categories. Chat assistants and image generators are both generative AI.

**Guardrail** – A rule or filter placed around a model to keep its behavior in bounds: blocking unsafe requests, keeping it on topic, or checking output before it reaches you. Guardrails sit around the model and are separate from its own training.

**Hallucination** – When a model produces something false or unsupported and presents it as fact: a made-up citation, a wrong date, a confident but invented answer. It usually sounds completely sure, so the tone tells you nothing about whether it's true. This is the main reason to check sources.

**Harness (agentic harness)** – The app around a model that gives it hands: a place to type, access to your files, and the tools it can run. The model decides what to do; the harness actually does it and feeds back the result. Claude Code, Codex, and OpenCode are examples. (Here, Codex means the rebuilt coding agent, not the older code model of the same name.) See [Agentic Harnesses]({{ '/learn/agentic-harnesses/' | relative_url }}).

**Inference** – Running a trained model to get an answer. Training is teaching the model; inference is using it. Every prompt-and-reply is inference, and it's the part that costs money to run.

**LLM (large language model)** – The kind of AI behind most chat assistants. It learns from huge amounts of text to predict the next **token**. Later training (see **Alignment**) turns that raw predictor into something that follows instructions and acts like an assistant. "Large" refers mainly to the number of **parameters**.

**MCP (Model Context Protocol)** – A shared standard that lets an assistant connect to outside tools and data (your files, a calendar, a database) through one common plug instead of a separate custom integration for each. It's a protocol, not a product or a model. See [MCP]({{ '/learn/mcp/' | relative_url }}).

**Model** – The trained system itself: the part that takes input and produces output. Most chat models take text in and give text out, but many are **multimodal** and also handle images or audio. A **foundation model** is a large, general-purpose model, trained on broad data, that many products are built on. Worth separating the model from the app you reach it through: ChatGPT and Claude are products wrapped around models.

**Multimodal** – A model that handles more than text — images, audio, sometimes video — as input, output, or both. A multimodal model can look at a photo or a screenshot you upload and describe what's in it.

**Open source / open weights** – Models you can download and run yourself rather than only reach through someone's service. "Open weights" means the trained **parameters** are public, so you can run and adapt the model; fully "open source" also shares the training code and often the data. This is the main line between models like Llama and closed ones like GPT or Claude. (Llama is usually called open-weight rather than strictly open source, since its license still sets some limits.)

**Parameters (weights)** – The numbers a model adjusts during training; together they hold what it has learned. Big models have billions, and a model's quoted "size" usually means its parameter count. "Weights" is used loosely for the same thing.

**Pretraining** – The first and largest training stage, where a model learns language and general knowledge by predicting text across an enormous dataset. Everything after it, including **fine-tuning** and **alignment**, builds on this base.

**Prompt (and system prompt)** – A prompt is what you hand the model to work with: your request plus any context. A **system prompt** is a separate set of standing instructions that sits above the whole conversation and shapes how the model behaves (its role, rules, and tone). You write the user prompts; the app usually sets the system prompt. See [Prompting and Evals]({{ '/learn/prompting-and-evals/' | relative_url }}).

**Prompt injection (and jailbreak)** – Tricks that get a model to ignore its instructions. A **jailbreak** is a user coaxing the model into doing something it's meant to refuse. Prompt injection is sneakier: hidden instructions planted in a web page, document, or email that the model reads and follows. It becomes a real risk the moment an assistant can browse the web or use your tools. See [Sharing Agents and Skills]({{ '/learn/sharing-agents-and-skills/' | relative_url }}) and [MCP]({{ '/learn/mcp/' | relative_url }}).

**RAG (retrieval-augmented generation)** – A way to let a model answer from specific material rather than only what it learned in training. The system searches a source — your documents, a database, sometimes the web — pulls the relevant passages, and drops them into the prompt. It's an open-book test, not extra training, so RAG does not change the model or teach it your data. See [Search, Knowledge, and RAG]({{ '/learn/search-knowledge-and-rag/' | relative_url }}).

**Reasoning** – A model spending extra effort before it answers: planning, working through steps, or checking itself, sometimes in hidden intermediate steps you never see. "Reasoning models" are tuned to do more of this, which helps on hard problems but costs more time and money. More reasoning is not a guarantee of a correct answer. The visible, step-by-step version is **chain-of-thought** — though what a product shows you is often a summary, not the model's actual internal steps.

**Skill** – A packaged capability an **agent** can pick up and reuse: instructions plus, often, the specific tools it's allowed to call. Think of it as a saved way of doing one job. See [Skills]({{ '/learn/skills/' | relative_url }}).

**Temperature** – A dial for how predictable or varied the output is. Low temperature gives more focused, consistent answers, which suits facts and code. High temperature gives looser, more surprising answers, which suits brainstorming. It makes output more or less predictable, not perfectly repeatable.

**Token** – The unit a model reads and writes in, roughly a chunk of a word. "Cats" is one token; a longer word might be split into two. Models measure both their limits and their pricing in tokens, so tokens are what you're really paying for. A rough guide for English is about 750 words per 1,000 tokens; code and non-English languages often use more tokens per word, so fewer words fit in the same budget.

**Tool call (function calling)** – When a model, instead of just replying, asks to run a specific function: search the web, look up an order, send a message. The model doesn't run the code itself. It produces a structured request, and the **harness** runs it and hands back the result. This is the machinery underneath **agents** and **skills**. See [Skills]({{ '/learn/skills/' | relative_url }}).

**Training data** – The material a model learns from. Its quality and coverage shape what the model knows and where it's weak, and a model generally knows nothing about events after its data was collected (its "cutoff"), unless the app feeds it newer information through browsing, tools, or **RAG**.

## References
These are standard definitions; spot-check the fast-moving ones against a current source. Good anchors: the vendor glossaries (OpenAI, Anthropic, and the Google Machine Learning Glossary), one stable ML reference for the core terms, and product docs for the newer entries (**MCP**, tool calling).
