---
layout: page
title: Articles
permalink: /articles/
description: "Weekly-ish news for AI and software development."
---

Timely, plain-language takes on what's new and why it matters.

{% if site.posts.size > 0 %}
<ul class="index-list">
{% for post in site.posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span class="index-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    {% if post.description %}<span class="index-summary">{{ post.description }}</span>{% endif %}
  </li>
{% endfor %}
</ul>
{% else %}
_No published articles yet — several are drafted. (Drafts live in `_drafts/`; preview them with `bundle exec jekyll serve --drafts`.)_
{% endif %}
