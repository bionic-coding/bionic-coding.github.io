---
layout: crux
title: Using Crux
permalink: /crux/team/
description: "Two places to start, seven specialists, and the judgments that stay yours."
specialist_order:
  - architect
  - dev-lead
  - developer
  - reviewer
  - historian
  - librarian
  - wayfinder
---

{% assign cat = site.data.crux_catalog %}
Crux installs {{ cat.counts.agents }} roles and {{ cat.counts.skills }} skills. You do not need to learn all {{ cat.counts.skills }}. You need to know where to start, what to ask for, and which judgments stay yours.

This page teaches the working relationship. The [catalog]({{ "/crux/catalog/" | relative_url }}) lists every role and every skill, generated from the crux source.

## Using Crux

### Delegate to agents to build. You drive the planning.

Each prompt to an agent should include four things.

| You state | The question it answers |
|---|---|
| Outcome | {% include crux-text.html t=cat.handoff_template.outcome %} |
| Evidence | {% include crux-text.html t=cat.handoff_template.evidence %} |
| Constraint | {% include crux-text.html t=cat.handoff_template.constraint %} |
| Authority | How far does this request let the team go? |

The first three shape the work. The fourth bounds it. {% include crux-text.html t=cat.teaching_model.authorization %}

## Roles and skills are different things

### Two words that are easy to blur, and worth keeping apart.

- **Role** — {% include crux-text.html t=cat.teaching_model.agent %} Crux's own files call these agents.
- **Skill** — {% include crux-text.html t=cat.teaching_model.skill %}

`propose-adr` is a skill. The architect is a role that runs it. The historian runs a different set. Roles are who; skills are how.

{% assign everyday = cat.skills | where_exp: "s", "s.learning.audience == 'human_request'" %}
You ask for outcomes in plain language. "Audit docs" reaches a skill directly; "implement the approved plan" reaches a role. Either way you do not pick the specialist. {{ everyday.size }} of the {{ cat.counts.skills }} skills answer a request phrased that way.

## Two places to start

### Which one you want depends on whether you have decided what to build.

{% for id in cat.teaching_model.default_entry_points %}{% assign role = cat.agents | where: "id", id | first %}
#### {{ id | capitalize }}

{% include crux-text.html t=role.learning.purpose %}

- **When** — {% include crux-text.html t=role.learning.when %}
- **Ask for it like this** — "{% include crux-text.html t=role.learning.ask %}"
- **Give it** — {% assign j = role.learning.provide | join: ". " %}{% include crux-text.html t=j %}.
- **It returns** — {% assign j = role.learning.expect | join: ". " %}{% include crux-text.html t=j %}.
- **Avoid** — {% assign j = role.learning.avoid | join: ". " %}{% include crux-text.html t=j %}.
{% endfor %}

The brainstormer explores; it does not build. The commander coordinates; it does not edit files. Each one hands the next step to the role that owns it.

## The night gardener

{% assign gardener = cat.agents | where: "id", "night-gardener" | first %}
### An automated nightly review intended to provide research and suggestions for improvement.

You set the schedule. Crux does not install one, and it does not run a pass you did not ask for.

- **When** — {% include crux-text.html t=gardener.learning.when %}
- **Ask for it like this** — "{% include crux-text.html t=gardener.learning.ask %}"
- **Give it** — {% assign j = gardener.learning.provide | join: ". " %}{% include crux-text.html t=j %}.
- **It returns** — {% assign j = gardener.learning.expect | join: ". " %}{% include crux-text.html t=j %}.
- **Avoid** — {% assign j = gardener.learning.avoid | join: ". " %}{% include crux-text.html t=j %}.
- **Then** — {% include crux-handoff.html t=gardener.learning.handoff %}

> [!NOTE]
> A pass that finds only its own earlier notes ends without a morning note. Silence is a valid result, not a failure.

What the gardener writes is a proposal, and the proposal is yours to accept or reject.

## The seven specialists

### Ask for the outcome. Let your coding agent assign the role that owns it.

That is a working habit, not a lock. Five of the seven declare phrases a person can say directly, and a direct request to any of them still works. Delegation is the default for two reasons.

The first is that each role's tool list is the guardrail, and it binds only the role it belongs to. The librarian has no tool that writes. The reviewer has no tool that edits the diff it is judging. Routing the work to the right role is what puts the fence around it. Not every boundary is a tool list — the catalog shows each role's, so you can tell which is which.

The second is that review has to be commissioned by whoever assigned the work, never by its author. When you hand each specialist its own instructions, you become the only thing holding that separation together.

Below, **the coordinator** is your coding agent — or the commander, while a promptbook runs.

{% assign known = "" | split: "" %}{% for id in page.specialist_order %}{% assign role = cat.agents | where: "id", id | first %}{% if role %}{% assign known = known | push: id %}
#### {{ role.id }}

{% include crux-text.html t=role.learning.purpose %}

- **When** — {% include crux-text.html t=role.learning.when %}
- **How to ask** — {% include crux-text.html t=role.learning.request_via %}
- **Give it** — {% assign j = role.learning.provide | join: ". " %}{% include crux-text.html t=j %}.
- **It returns** — {% assign j = role.learning.expect | join: ". " %}{% include crux-text.html t=j %}.
- **Avoid** — {% assign j = role.learning.avoid | join: ". " %}{% include crux-text.html t=j %}.
- **Then** — {% include crux-handoff.html t=role.learning.handoff %}
{% endif %}{% endfor %}
{%- assign specialists = cat.agents | where_exp: "a", "a.learning.audience == 'delegated_specialist'" -%}
{%- assign missing = "" | split: "" -%}
{%- for role in specialists -%}{%- unless known contains role.id -%}{%- assign missing = missing | push: role.id -%}{%- endunless -%}{%- endfor -%}
{% if missing.size > 0 %}
Also cataloged and not described above: {{ missing | join: ", " }}. The [catalog]({{ "/crux/catalog/" | relative_url }}) covers them.
{% endif %}

## What happens after you ask

### {{ cat.journeys.size }} shapes a request takes. They illustrate the handoffs; they are not a checklist.

<div class="journeys">
{%- for journey in cat.journeys -%}
<div class="journey"><p class="journey-ask">“{% include crux-text.html t=journey.user_request %}”</p><p class="journey-chain">{% if journey.roles %}<span class="journey-label">Roles</span>{% assign j = journey.roles | join: " → " %}{% include crux-text.html t=j %}{% endif %}{% if journey.skills %}<span class="journey-label">Skills</span>{% for s in journey.skills %}<code>{{ s | escape }}</code>{% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}</p><p class="journey-note">{% include crux-text.html t=journey.note %}</p></div>
{%- endfor -%}
</div>

Notice how short the single-role journeys are. One question reaches one role. One bounded defect reaches one skill.

## Keep small work small

### Not every task needs a commander or a promptbook. The smallest workflow that fits is the right one.

Crux has four workflows of decreasing rigor — cycle, iterate, patch, and fix-directly. [Reference]({{ "/crux/reference/" | relative_url }}) explains how to choose between them. Nothing on this page adds a step to that choice.

The commander exists for a plan that already has gates. It is not a toll booth every task passes through. A question is a question, and a typo is a typo.

## What stays yours

### Some judgments are reserved for you, and for most of them a declared flag holds the line rather than an instruction.

- **Accepting a decision.** The architect that drafted an ADR does not accept it. Acceptance runs through the decision process, with a different reader.
- **Sign-off.** The survey, reconciliation, and backfill skills take the verdict and the rationale from you, one pairing at a time. The skill records what you said. It does not decide what you would have said.
- **Ratifying an invariant.** A mined candidate stays an observation until you ratify it.
- **Publishing.** Pushing, merging, deploying, and sending anything outward stay with you. A plan you approved is not a publication you approved.

{% assign explicit = cat.skills | where_exp: "s", "s.learning.audience == 'explicit_human'" %}{{ explicit.size }} of the {{ cat.counts.skills }} cataloged skills require you to invoke them yourself. {% include crux-text.html t=cat.audience_definitions.explicit_human %} The [catalog]({{ "/crux/catalog/" | relative_url }}) marks each one.

## Asking is not authorizing

### A question about the project is answered from the record, not by rebuilding it.

| You ask | You get | You do not get |
|---|---|---|
| "Summarize the current architecture" | An answer from the documentation tree, with citations | A regenerated architecture map |
| "What supersedes ADR-0003?" | The lineage as recorded | A regenerated lineage graph |
| "Where is the run?" | The current prompt and how to resume | A run moved forward a prompt |
| "Any drift?" | A drift report | Regenerated or repaired outputs |

Every entry in the third column names a skill that its own request starts. "Audit docs" repairs the safe drift, and it is its own request. Retrieval is not permission to write, and a status answer is not permission to advance.

## Where the limits are

### Three limits on what this page claims.

**Trigger phrases are not commands.** The phrases in the catalog are copied from the skill definitions. They show you the shape of a request that matches. They are not slash commands, they do not carry across harnesses, and no phrase deterministically selects a skill.

**Role names are identifiers, not proof.** The catalog records what each role is called in Claude Code, Codex, and OpenCode. A name there means the role is defined in the source, not that it is installed and callable in your session.

**Tool limits are source contracts.** Every role's tool list comes from its definition. What a harness enforces depends on the harness and how you configured it.

## Next

The [catalog]({{ "/crux/catalog/" | relative_url }}) has every role and every skill, grouped by what it is for.
