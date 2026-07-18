---
layout: page
title: Lessons
permalink: /learn/
description: "A plain-language field guide to the ideas and tools behind modern AI."
---

The Bionic Coding AI field guide. Start anywhere.

{% assign items = site.lessons | sort: "order" %}
<ol class="index-list">
{% for item in items %}
  <li>
    <a href="{{ item.url | relative_url }}">{{ item.title }}</a>{% unless item.status == "published" %} <span class="soon-tag">soon</span>{% endunless %}
    {% if item.summary %}<span class="index-summary">{{ item.summary }}</span>{% endif %}
  </li>
{% endfor %}
</ol>
