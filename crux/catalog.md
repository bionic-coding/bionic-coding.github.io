---
layout: crux
title: Catalog
permalink: /crux/catalog/
description: "Every role and every skill, generated from the crux source."
updated: 2026-09-15
role_order:
  - brainstormer
  - commander
  - night-gardener
  - architect
  - dev-lead
  - developer
  - reviewer
  - historian
  - librarian
  - wayfinder
categories:
  - id: planning
    title: Planning and running work
    blurb: "Choosing a workflow, writing the plan, and moving a run through its gates."
  - id: decisions
    title: Decisions and records
    blurb: "Proposing, transitioning, and reviewing the records that hold the why."
  - id: documentation
    title: Documentation and drift
    blurb: "Filing, regenerating, auditing, and checking the tree against its sources."
  - id: research
    title: Research
    blurb: "Bringing outside material in, keeping captures current, and reconciling synthesis."
  - id: collaboration
    title: Collaboration and improvement
    blurb: "Multi-model review, dissent resolution, retrospectives, and the night pass."
  - id: runtime
    title: Runtime and installation
    blurb: "Installing crux into a harness and instrumenting how it runs."
---

{% assign cat = site.data.crux_catalog %}
{% assign roles = cat.agents %}
{% assign skills = cat.skills %}
This is the full inventory: {{ roles.size }} roles and {{ skills.size }} skills, generated from crux {{ cat.source.plugin_version | escape }}. [Using Crux]({{ "/crux/team/" | relative_url }}) is the page to read first. This one is for looking things up.

Descriptions, declared triggers, tool lists, and invocation flags are copied from the crux source. Everything under a **Guidance** label is editorial: it says how we recommend you work, not what the software enforces. Nothing here was observed at runtime.

## How to read a badge

### A badge is our recommendation about audience. The Declared line beneath it is the source metadata.

| Badge | Means |
|---|---|
| **Ask for it** | {% include crux-text.html t=cat.audience_definitions.human_request %} |
| **Human invocation** | {% include crux-text.html t=cat.audience_definitions.explicit_human %} |
| **Inside a workflow** | {% include crux-text.html t=cat.audience_definitions.workflow_support %} |
| **Runtime support** | {% include crux-text.html t=cat.audience_definitions.agent_internal %} |

> [!IMPORTANT]
> Declared triggers are the phrases a skill's own definition lists. They show the shape of a request that matches.
> They are not commands, they are not slash commands, and no phrase selects a skill deterministically.

Where a source invocation flag is undeclared, it is reported as undeclared, which is not the same as forbidden.

## Roles

### {% include crux-text.html t=cat.teaching_model.agent %}

Three roles are built for you to address. The other seven are reached through them by default. That is guidance, not a lock: five of the seven declare phrases a person can say directly, and a direct request to any of them still works. [Using Crux]({{ "/crux/team/" | relative_url }}) explains why the habit is worth keeping.

<div class="cat-roles">
{%- assign shown = "" | split: "" -%}
{%- for id in page.role_order -%}{%- assign role = roles | where: "id", id | first -%}{%- if role -%}{%- assign shown = shown | push: id -%}
{%- assign aud = role.learning.audience -%}
{%- case aud -%}
{%- when "human_entry_point" -%}{%- assign badge = "Start here" -%}{%- assign bclass = "badge-entry" -%}
{%- when "scheduled_or_explicit" -%}{%- assign badge = "You ask or you schedule" -%}{%- assign bclass = "badge-explicit" -%}
{%- else -%}{%- assign badge = "Delegated" -%}{%- assign bclass = "badge-workflow" -%}
{%- endcase -%}
{% include crux-role.html role=role badge=badge class=bclass %}
{%- endif -%}{%- endfor -%}
{%- for role in roles -%}{%- unless shown contains role.id -%}
{% include crux-role.html role=role badge="Cataloged" class="badge-workflow" %}
{%- endunless -%}{%- endfor -%}
</div>

A role's declared skill list records which skills its own definition binds. It is not a promise that every one of them runs inside that role's tool limits. It is not a complete map of who calls what. Tool lists are source contracts too: what a harness enforces depends on the harness and how you configured it.

## Skills

### {% include crux-text.html t=cat.teaching_model.skill %}

{% assign everyday = skills | where_exp: "s", "s.learning.audience == 'human_request' or s.learning.audience == 'explicit_human'" %}
{% assign advanced = skills | where_exp: "s", "s.learning.audience == 'workflow_support' or s.learning.audience == 'agent_internal'" %}
{% assign plain = skills | where_exp: "s", "s.learning.audience == 'human_request'" %}{% assign selfinvoke = skills | where_exp: "s", "s.learning.audience == 'explicit_human'" %}{{ plain.size }} of these answer a plain-language request. {{ selfinvoke.size }} more are yours to invoke yourself. The remaining {{ advanced.size }} are listed under [Advanced and internal](#advanced-and-internal), because a newcomer never needs to name them.

{% for group in page.categories %}{% assign items = everyday | where: "category", group.id | sort: "id" %}
### {{ group.title }} — {{ items.size }} skills

{{ group.blurb | escape }}

<div class="cat-skills">
{%- for s in items -%}
{%- if s.learning.audience == "explicit_human" -%}{%- assign badge = "Human invocation" -%}{%- assign bclass = "badge-explicit" -%}
{%- else -%}{%- assign badge = "Ask for it" -%}{%- assign bclass = "badge-ask" -%}{%- endif -%}
{% include crux-skill.html s=s badge=badge class=bclass %}
{%- endfor -%}
</div>
{% endfor %}

### Advanced and internal — {{ advanced.size }} skills
{: #advanced-and-internal}

{% assign wsupport = advanced | where_exp: "s", "s.learning.audience == 'workflow_support'" %}{% assign internal = advanced | where_exp: "s", "s.learning.audience == 'agent_internal'" %}
{{ wsupport.size }} of these are reached inside a workflow that already runs them. {{ internal.size }} are team plumbing. Neither group belongs in a newcomer's vocabulary. Both are listed so the inventory is complete.

<div class="cat-skills">
{%- assign adv = advanced | sort: "id" -%}
{%- for s in adv -%}
{%- if s.learning.audience == "workflow_support" -%}{%- assign badge = "Inside a workflow" -%}{%- else -%}{%- assign badge = "Runtime support" -%}{%- endif -%}
{% include crux-skill.html s=s badge=badge class="badge-workflow" cat=true %}
{%- endfor -%}
</div>

## Provenance

Last updated for Crux version {{ cat.source.plugin_version | escape }} on {{ page.updated | date: "%B %-d, %Y" }}.
