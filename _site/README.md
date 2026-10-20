# 个人网站

基于 Jekyll + GitHub Pages 的静态个人网站。

## 🚀 本地预览

```bash
# 安装依赖
bundle install

# 本地启动
bundle exec jekyll serve

# 访问 http://localhost:4000
```

## 📦 部署到 GitHub Pages

### 方法一：GitHub 自动构建（推荐）

1. 在 GitHub 新建仓库 `<用户名>.github.io`
2. 推送代码到 main 分支
3. 仓库 Settings → Pages → Source 选择 "GitHub Actions"
4. 等待 Actions 完成，访问 `https://<用户名>.github.io`

### 方法二：GitHub Actions 工作流

创建 `.github/workflows/jekyll.yml`：

```yaml
name: Deploy Jekyll site to Pages
on:
  push:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v4
      - uses: actions/jekyll-build-pages@v1
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

## 📝 目录结构

```
personal-site/
├── _config.yml          # 站点配置
├── _layouts/
│   └── default.html     # 默认布局
├── _posts/
│   └── 2026-10-20-first-post.md  # 博客文章
├── assets/              # 静态资源
├── index.md             # 首页
├── Gemfile              # Ruby 依赖
└── README.md
```

## ✏️ 写博客

在 `_posts/` 目录创建文件，命名格式：`YYYY-MM-DD-标题.md`

```markdown
---
layout: default
title: "文章标题"
date: 2026-10-20 10:00:00 +0800
categories: 分类
---

正文内容...
```
