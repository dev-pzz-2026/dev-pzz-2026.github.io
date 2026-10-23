---
layout: default
title: 栏目
permalink: /columns/
---

# 栏目

> 医 · 工 · 艺 —— 文字分科，各安其位。

## 医

医，岐黄之术。收录中医经典与医理笔记。

{% for post in site.categories["医"] %}
- {{ post.date | date: "%Y年%m月%d日" }}　[{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}

## 工

工，营造之技。收录技术开发与工程实践。

{% assign has_gong = false %}
{% for post in site.categories["工"] %}
- {{ post.date | date: "%Y年%m月%d日" }}　[{{ post.title }}]({{ post.url | relative_url }})
{% assign has_gong = true %}
{% endfor %}
{% unless has_gong %}
*虚位以待*
{% endunless %}

## 艺

艺，心性之游。收录读书、随笔与生活记录。

- [🎵 音乐播放器（内置曲库）]({{ '/music/' | relative_url }})

{% assign has_yi = false %}
{% for post in site.categories["艺"] %}
- {{ post.date | date: "%Y年%m月%d日" }}　[{{ post.title }}]({{ post.url | relative_url }})
{% assign has_yi = true %}
{% endfor %}
{% unless has_yi %}
*虚位以待*
{% endunless %}
