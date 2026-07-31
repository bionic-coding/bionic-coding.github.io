# CLAUDE.md

Guidance for Claude Code working in this repository.

## What this is

**Bionic Coding** (bionic-coding.com) — a Jekyll 4.4 static site publishing a manifesto,
a plain-language AI field guide ("Lessons"), and a weekly-ish news column ("Articles").
There is no application code: this repo is content, Liquid templates, and one stylesheet.

See `bionic/CLAUDE.md` for documentation operations — the `bionic/` tree is maintained by the
`crux` Claude Code plugin and has its own ownership rules.

## Commands

```sh
bundle install                              # Ruby 4.0.5 (.ruby-version), bundler 4.x
bundle exec jekyll serve                    # local dev at :4000; renders lesson drafts
bundle exec jekyll serve --drafts           # also renders _drafts/ posts
bundle exec jekyll build --config _config.yml,_config_production.yml   # what CI builds
```

Deployment is automatic: pushing to `main` triggers `.github/workflows/jekyll.yml`, which
builds with the production overlay and deploys to GitHub Pages. There are no tests or linters.

## Draft mechanics

Two parallel draft systems, both of which render locally and disappear in production:

| Content | Draft location | Published location | Hidden in prod by |
| --- | --- | --- | --- |
| Posts | `_drafts/` | `_posts/YYYY-MM-DD-slug.md` | Jekyll's built-in `--drafts` flag |
| Lessons | `_lesson_drafts/` | `_lessons/` | `_config_production.yml` (`output: false`) |

Publishing is a file move, nothing else. A lesson can *also* be soft-drafted in place:
`_layouts/lesson.html` renders a "coming soon" card in production for any lesson whose
frontmatter `status` is not `published`, so links stay alive and unfinished prose never leaks.

## Content conventions

**Posts** (`_posts/`) — `layout: post`, `title`, `date`, `description` (the scannable teaser
used on the homepage and index), `tags`. The recurring column has a template at
`_templates/this-week-in-ai.md`; its full format contract lives in
`bionic/briefs/BRIEF-this-week-in-ai-format.md` (3–5 stories biggest-first, annotated dated
links, a permanent `## What I'm actually using` closer, claimed-vs-verified marking).

**Lessons** (`_lessons/`) — `title`, `order` (drives sort on `/learn/`), `summary`,
`status` (`published` | `stub`), `updated` (rendered as "Last reviewed"). Bump `updated`
when you revise a lesson; the freshness review depends on it.

**Scaffold, don't generate.** Templates, outlines, and structure are Claude's job; the
sentences are the author's. Do not fill a template's prose placeholders unless asked.

**Voice.** "Bionic" means *augmented, not replaced* — the human keeps judgment and control,
the machine takes over manufacturing. Content must never drift toward displacement or
"the machines take over" framing. See `about.md` and `manifesto.md` for the register.

## Writing rules

Applies to prose: docs, comments, commit messages, PR descriptions, and explanations in chat. Does not apply to code, identifiers, quoted material, error strings, or anything you are reproducing verbatim.

The principle behind all six rules: one idea, one sentence, one name. Accuracy outranks every rule below — if following a rule would make a statement false or imprecise, break the rule and keep the truth.

1. One name per thing. Pick one term for each concept and repeat it. Repetition is correct here; variation signals a new concept and makes the reader look for a difference that isn't there. If two words in a document mean the same thing, one of them is wrong. The inverse also holds: don't use one word for two concepts.

2. No hedge without a cause. Delete any qualifier you cannot justify. If something is genuinely conditional, name the condition instead of gesturing at it.

Not: "This may fail under certain conditions." But: "This fails when the port is already bound."

3. Verbs stay verbs. Write the action as the main verb, not as a noun with a filler verb attached.

Not: "Perform a validation of the payload." But: "Validate the payload."

4. Adjectives must be checkable. Drop any adjective the reader cannot verify. Replace it with the number, the mechanism, or the failure it survives — or cut it. If nobody would ever claim the opposite about their own work, the word carries no information.

Not: "a robust, high-performance cache" But: "a cache that serves reads during a Redis failover, at ~40k req/s"

5. One idea per sentence. Aim for 20 words in instructions, 25 in explanation. Two independent clauses joined by "and" or "but" are usually two sentences. Length is the symptom; the test is how many ideas are in there.

6. Single-word verbs. Prefer "configure" over "set up", "review" over "go through", "delete" over "get rid of", "start" over "kick off". Keep the two-word form only when it is the established name of the thing — log in, shut down, roll back, fall back, check out — and then use it consistently, because rule 1 wins over this rule.

When in doubt: write the shorter sentence and state the fact.

## Site structure

- `index.md` — `layout: home`; the hero, manifesto pull-quote, latest 3 posts, and a
  `featured_lessons` list of lesson slugs, all set in frontmatter.
- `manifesto.md` — the canonical manifesto, served at `/manifesto/` and reached via the
  site title. (Root `README.md` is an older plain-markdown copy of the same text; treat
  `manifesto.md` as authoritative.)
- `articles.md`, `learn.md` — index pages that loop over `site.posts` / `site.lessons`.
- Top nav is driven by `header_pages` in `_config.yml`; a page can override its nav text
  with `nav_label`.
- `_layouts/` — `default` (head, header, nav, footer, mermaid loader) wraps `home`, `page`,
  `post`, and `lesson`.

## Rendering gotchas

- **Never leave a blank line inside an HTML comment.** kramdown ends the HTML block at the
  blank line and stops converting Markdown for the *rest of the file* — headings and links
  render as literal text. Use a lone `.` on the line as a spacer.
- Markdown is GFM via kramdown with `hard_wrap: false`, so hand-wrapped paragraphs do not
  become `<br>` tags.
- `assets/main.scss` fully replaces Minima's stylesheet — the theme gem is a dependency but
  none of its CSS is used. All styling changes go in that one file.
- Mermaid is lazy-loaded from `assets/mermaid.min.js` by `_layouts/default.html`, and only
  on pages that actually contain a ` ```mermaid ` block.
- Internal links in content use `{{ "/path/" | relative_url }}`.
