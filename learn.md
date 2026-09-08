---
layout: page
title: Lessons
permalink: /learn/
description: "A plain-language field guide to the ideas and tools behind modern AI."
---

The Bionic Coding AI field guide. Pick the route that matches what you need today.

<div class="learning-paths">
  <div class="learning-path">
    <strong>New to AI?</strong>
    <span>Start with <a href="{{ '/learn/prompting-and-evals/' | relative_url }}">Prompting</a> → <a href="{{ '/learn/agents/' | relative_url }}">Agents</a> → <a href="{{ '/learn/skills/' | relative_url }}">Skills</a> → <a href="{{ '/learn/agentic-harnesses/' | relative_url }}">Harnesses</a> → <a href="{{ '/learn/mcp/' | relative_url }}">MCP</a>.</span>
  </div>
  <div class="learning-path">
    <strong>Looking something up?</strong>
    <span>Use the <a href="{{ '/learn/glossary/' | relative_url }}">glossary</a>, or browse every lesson below.</span>
  </div>
</div>

## All lessons

{% assign items = site.lessons | sort: "order" %}
<ol class="index-list">
{% for item in items %}
  <li>
    <a href="{{ item.url | relative_url }}">{{ item.title }}</a>{% unless item.status == "published" %} <span class="soon-tag">soon</span>{% endunless %}
    {% if item.summary %}<span class="index-summary">{{ item.summary }}</span>{% endif %}
  </li>
{% endfor %}
</ol>
