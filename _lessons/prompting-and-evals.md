---
title: Prompting and Evals
order: 2
summary: "How to ask well — and how to tell if the answer is any good."
status: published
updated: 2026-07-14
---

Probably the most important thing to understand about an LLM is that it works by predicting the next word (token) in a sequence. Because of this, the quality of the response is directly tied to the contents of the prompt that you provide.

I'm sure you've seen examples where people use poor prompts that generate irrelevant or incorrect responses. But it goes deeper than a vague question — because the model is *predicting* the next word rather than calculating or looking anything up, it can get a perfectly clear question wrong. Ask one, in a plain chat, **"How many times does the letter _r_ appear in the word _strawberry_?"** and for a long time the answer came back **two**. It's three. The model hadn't spelled the word out and counted — it predicted the most likely next token right after your question, and a small number *reads* right there. Tell it instead to *write the word out one letter at a time and tally the r's as it goes*, and it gets it: now the correct answer is the natural continuation of the work already on the page, not a snap guess. (Newer models that quietly work a problem through before answering often get this right on their own now — which is the same fix, just done for you.)

The opposite is also true: you can craft good prompts that generate high-quality responses by giving the model enough context, examples of the expected output, and a clear task. As noted "thinking models" often do this work for you but you can use this as an opportunity to provide specific direction and instructions to help ensure the model generates the desired output.

## What a prompt really is

A prompt is just *the text you hand the model* — but it helps to stop thinking of it as a command and start thinking of it as **context**. You're not typing keywords into a search box or hunting for the magic words; you're giving the model something to continue. Clear intent in, useful text out. The same request said more specifically is a *different* prompt, and usually a better one — not because you found a secret phrase, but because you left less to guess.

Under the hood there are usually **two** prompts stacked together:

- **The system prompt** sets the standing rules — who the model should act as, what it should always or never do, the format to answer in. Think of it as the job description you'd hand a new assistant on day one.
- **The user prompt** is today's actual ask — the specific question or task.

In a consumer app like ChatGPT or Claude, the system prompt is written for you and hidden; you only type the user prompt. But it's still there, shaping every answer — and most apps now let you edit your slice of it (as "custom instructions," a "project," or a saved persona). That's the highest-leverage place to put anything you catch yourself repeating: your role, your preferences, the format you always want. Set it once and every later ask inherits it. (When a prompt is worth keeping for good, it graduates into a *skill* — see the [Skills]({{ "/learn/skills/" | relative_url }}) lesson.) When you build on a provider's API instead of a chat app, you write that system prompt yourself.

## Patterns that work

A handful of habits do most of the heavy lifting. You won't need all of them every time — reach for the ones the task calls for.

**Name the role, task, context, and constraints.** Most good prompts fill in four blanks: a **role** ("you're a careful copy editor"), the **task** (what to actually do), the **context** (the material to work from), and the **constraints** (length, format, what to avoid). The wording doesn't need to be clever — you just can't leave the blanks empty. "Fix this" leaves all four to the model's imagination; "You're a copy editor. Tighten this paragraph to under 100 words, keep my voice, and don't add new claims: …" leaves nothing to guess.

**Show, don't just tell — "few-shot."** Asking cold is *zero-shot*. *Few-shot* is handing the model a couple of examples of the input and the output you want, so it matches the pattern instead of guessing at it. A small one:

```text
Turn each product name into a short, friendly tagline.

Name: Solar Desk Lamp
Tagline: Sunlight for your desk, minus the sunburn.

Name: Insulated Travel Mug
Tagline: Your coffee's still hot three meetings later.

Name: Noise-Cancelling Earbuds
Tagline:
```

Two examples are enough to pin down the length, tone, and shape; the model completes the last line to match. A good example teaches faster than a paragraph of adjectives describing what you want.

**Ask for a shape — a format or schema.** Any time you'll *do* something with the output rather than just read it — drop it in a spreadsheet, hand it to another tool — tell the model the exact shape to return. This is how you turn a messy document into tidy data. Say you've handed it an invoice PDF and want the fields out of it:

```text
Extract the following from the attached invoice.
Return JSON only — no prose. If a field is missing, use null.

{
  "invoice_number": string,
  "invoice_date": "YYYY-MM-DD",
  "vendor_name": string,
  "total_amount": number,
  "currency": string,
  "line_items": [
    { "description": string, "quantity": number, "unit_price": number }
  ]
}
```

The schema does two jobs at once: it tells the model *what* to pull out, and it guarantees the answer comes back in a shape your next step can actually use. Run the same schema across a hundred invoices and you've got a table.

**Have it check its own work — critique-and-revise.** For anything that matters, a second pass pays off: after the first answer, ask the model to *find the weakest part of that response and improve it*, or to check it against the constraints you set. It's the cheapest quality bump there is — and it's the same "show your work" move from the top of this lesson, pointed at its own output.

## Evals: verifying your prompt by evaluating it

Once a prompt matters — you'll reuse it, or you're trusting its answer — "it looked fine" stops being good enough. An **eval** is just a deliberate way to check whether the output is actually good, instead of eyeballing it once and hoping. Start simple and add rigor as the stakes rise:

- **The vibe check.** Read the output and judge it yourself. Honest, fast, and fine for a one-off — but it doesn't scale, and it quietly drifts as you get tired or get used to the model's style.
- **Golden-answer tests.** Collect a handful of real inputs where you *know* the right answer (or the key facts the answer must contain), and check the model against them. When you change the prompt, you re-run the set instead of guessing whether you made it better.
- **Rubric scoring.** Write down what "good" means — a short checklist (Did it answer the actual question? Cite a source? Stay in the right format? Avoid making things up?) — and grade each output against it. Writing the rubric is the real work; once you have it, grading is easy.
- **LLM as judge.** Hand the output *and your rubric* to a second model (or the same model in a fresh chat) and ask it to grade. This is the technique that makes evals scale: a judge model can score hundreds of answers against your criteria in minutes, and it's surprisingly good at fuzzy calls like "is this a helpful, on-topic reply?" It's often best run **pairwise** — *"which of these two answers is better, and why?"* — because "better than" is an easier, more reliable judgment than an absolute score.
- **Regression checks.** Keep your golden set and rubric around and re-run them every time you change the prompt, swap models, or a provider ships an update. This is how you catch the fix that quietly broke something else.
- **Adversarial / edge cases.** Deliberately try to break it: empty input, a hostile or off-topic request, an ambiguous question, the weird real-world input you didn't design for. The failures you find on purpose are the ones your users won't find for you.

> [!NOTE]
> **A single judge is still a model — so it can share the very failure mode you're testing for.** The way we get around that is a **council**: three models grade the output and vote, and we take the consensus. The trick is that they come from **different providers — Google, Anthropic, and OpenAI** — so a blind spot baked into one lab's model is unlikely to be shared by the other two. That's a real improvement over trusting a single judge, but it isn't a guarantee: the three can still land on the same wrong answer. So before you lean on a council at scale, spot-check its verdicts against your own.

The point of all this isn't ceremony. It's to turn "the answer felt right" into something you can check, repeat, and trust — especially once a prompt is doing real work.

## Reproducibility

Ask a model the same question twice and you can get two different answers. That's not a bug — it's how generation works. At each step the model has a *spread* of likely next words, and a setting called **temperature** decides how much it gambles: higher temperature means more varied, surprising output; **temperature 0** means "always take the most likely word," which is about as repeatable as these things get. (Even at zero you're not promised a byte-for-byte identical result — the machinery underneath can still wobble — but it's close.)

Two things follow if you're relying on a prompt:

- **For consistency, turn the temperature down.** Extracting invoice fields or sorting tickets? You want the boring, repeatable answer. Brainstorming names? Turn it back up. Chat apps hide this dial; developer tools and APIs expose it.
- **One good run is not an eval.** This is the important one. If you try a prompt once and it works, you've learned that it *can* work — not that it *will*. The failure you didn't happen to see is still in the deck. That's why a real eval runs your prompt across several inputs (and, for the shaky ones, several times): a single success is a story, not evidence.

It's also the second reason the council helps — different models catch different mistakes, *and* re-running smooths out the luck of any one roll.

## Worked example

Say you run a small shop and want help answering an unhappy customer. Here's the whole loop — naive prompt, engineered prompt, and the rubric that tells them apart.

**The naive prompt:**

```text
Write a reply to this angry customer.
```

You'll get *a* reply — polite, generic, and hollow. It doesn't know what the customer is angry about, what you're able to offer, or how you talk to people, so it fills the blanks with the blandest plausible apology.

**The engineered prompt** names the role, context, and constraints, and hands over the actual email:

```text
You're the owner of a small coffee-roasting shop, replying to a customer.
Be warm, take responsibility, and don't promise a refund — offer a
replacement or store credit instead. Keep it under 120 words, no corporate
jargon. Reply to this email:

"My beans arrived stale and the bag was torn. Third time this year. I'm done."
```

Now the model has something to work with: it can name the specific problem (stale beans, a torn bag, a repeat issue), match your tone, and stay inside the lines you set.

**The rubric** is how you grade *both* — and how you'd tell a judge (or a council) what "good" means:

```text
Score each 0-2:
- Addresses the specific complaint (stale beans, torn bag, repeat problem)?
- Warm, human tone — no corporate jargon?
- Takes responsibility without promising a refund?
- Under 120 words?
- Offers a concrete next step (replacement or credit)?
```

Run both prompts against that rubric and the gap is obvious — the naive reply scores near zero on "addresses the specific complaint," because it never saw the complaint. And the rubric is the reusable part: point it at the next unhappy-customer email, or hand it to a judge, and you've turned "that reads nicely" into a score you can actually trust.

## References

First-party prompting guides worth sharing. Provider docs move around and per-model pages get renamed, so these are the **stable overview pages** — all still live as of 2026.

- **[Anthropic — Prompt engineering overview](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)** — the best structured on-ramp: when prompting helps, the core techniques, and links onward to the living [best-practices reference](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices) and the Console prompt-improver tools.
- **[OpenAI — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)** — core strategies, message roles, and format advice. Pair it with **[Reasoning best practices](https://platform.openai.com/docs/guides/reasoning-best-practices)**, which echoes the top of this lesson: *don't* tell a reasoning model to "think step by step" — it already does that work for you.
- **[Google — Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)** — clear instructions, few-shot examples, constraints, and response formatting for Gemini.
- **[Google / Kaggle — "Prompt Engineering" whitepaper (Lee Boonstra)](https://www.kaggle.com/whitepaper-prompt-engineering)** — the deepest single free resource for a general reader: ~70 pages on zero/few-shot, role and system prompting, chain-of-thought, self-consistency, and more.
- **[Anthropic — Interactive Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)** — a hands-on, nine-chapter course with exercises and an answer key; the linked Google Sheets version is the friendlier one if you don't write code.

On checking the output — evals and LLM-as-a-judge:

- **[Zheng et al. — "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"](https://arxiv.org/abs/2306.05685)** — the paper that named the technique, and the source for the judge biases in the note above (position, verbosity, self-enhancement). It also found a strong judge agrees with people about as often as people agree with each other.
- **[Evidently AI — "LLM-as-a-judge: a complete guide"](https://www.evidentlyai.com/llm-guide/llm-as-a-judge)** — a practical, plain-language walkthrough: pairwise vs. direct scoring, why binary labels beat 1–5 scales, and using a jury of judges to cut variance.
