---
layout: page
title: AI Literacy
permalink: /learn/
description: "A plain-language field guide to the ideas and tools behind modern AI."
---

A plain-language field guide to modern AI — the words, the tools, and how to actually use them. Start anywhere.

{% assign items = site.lessons | sort: "order" %}
<ol class="index-list">
{% for item in items %}
  <li>
    <a href="{{ item.url | relative_url }}">{{ item.title }}</a>{% unless item.status == "published" %} <span class="soon-tag">soon</span>{% endunless %}
    {% if item.summary %}<span class="index-summary">{{ item.summary }}</span>{% endif %}
  </li>
{% endfor %}
</ol>
