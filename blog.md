---
layout: default
title: 博客
permalink: /blog/
---

# 博客文章

<div class="post-list">
{% for post in site.posts %}
<div class="post-item">
  <a href="{{ post.url | relative_url }}" class="title">{{ post.title }}</a>
  <div class="meta">
    {{ post.date | date: "%Y年%m月%d日" }}
    {% for cat in post.categories %}
    <span class="tag">{{ cat }}</span>
    {% endfor %}
  </div>
</div>
{% endfor %}
</div>
