---
layout: page
title: Articles
permalink: /articles/
description: "Weekly-ish news for AI and software development."
---

Timely, plain-language takes on what's new and why it matters. Follow new posts through the [RSS feed]({{ '/feed.xml' | relative_url }}).

News posts distinguish verified facts, vendor claims, outside reporting, and rumors. Sources appear with each story, and material corrections stay visible on the article.

{% if site.posts.size > 0 %}
{% assign weekly_posts = site.tags.weekly %}
{% if weekly_posts.size > 0 %}
## This Week in AI

<ul class="index-list">
{% for post in weekly_posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span class="index-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    {% if post.tags.size > 0 %}<span class="index-tags" aria-label="Tags">{% for tag in post.tags %}<span class="index-tag">{{ tag | replace: '-', ' ' }}</span>{% endfor %}</span>{% endif %}
    {% if post.description %}<span class="index-summary">{{ post.description }}</span>{% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}

## More articles

<ul class="index-list">
{% for post in site.posts %}
  {% unless post.tags contains "weekly" %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span class="index-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    {% if post.tags.size > 0 %}<span class="index-tags" aria-label="Tags">{% for tag in post.tags %}<span class="index-tag">{{ tag | replace: '-', ' ' }}</span>{% endfor %}</span>{% endif %}
    {% if post.description %}<span class="index-summary">{{ post.description }}</span>{% endif %}
  </li>
  {% endunless %}
{% endfor %}
</ul>
{% else %}
_No published articles yet — several are drafted. (Drafts live in `_drafts/`; preview them with `bundle exec jekyll serve --drafts`.)_
{% endif %}
