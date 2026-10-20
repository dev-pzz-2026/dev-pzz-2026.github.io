---
layout: default
title: 首页
---

> 记录生活，分享成果。

## 最新文章

<div class="post-list">
{% for post in site.posts limit: 5 %}
<div class="post-item">
  <a href="{{ post.url }}" class="title">{{ post.title }}</a>
  <div class="meta">
    {{ post.date | date: "%Y年%m月%d日" }}
    {% for tag in post.tags %}
    <span class="tag">{{ tag }}</span>
    {% endfor %}
  </div>
</div>
{% endfor %}
</div>
