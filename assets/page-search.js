/* 页内内容检索：纯前端，索引当前页面各小节，支持简繁互搜、命中高亮与跳转 */
(function () {
  "use strict";

  var main = document.querySelector("main");
  var box = document.getElementById("searchBox");
  var panel = document.getElementById("searchResults");
  var meta = document.getElementById("searchMeta");
  if (!main || !box || !panel || !meta) return;

  var MAX_RESULTS = 60;   // 面板最多列出多少条
  var MAX_MARKS = 3000;   // 正文高亮上限，避免超大页面卡顿
  var SNIP = 34;          // 摘要上下文长度

  var index = null;       // [{ id, title, norm }]
  var marks = [];         // 当前 <mark>
  var timer = null;

  // 简/繁转换（opencc 缺失时降级为原样匹配）
  var toCN = null, toTW = null;
  try {
    toCN = OpenCC.Converter({ from: "t", to: "cn" });
    toTW = OpenCC.Converter({ from: "cn", to: "t" });
  } catch (e) {}
  function norm(s) { return toCN ? toCN(s) : s; }

  /* ---------- 索引：以标题为界，把正文归入各小节 ---------- */
  function buildIndex() {
    var entries = [];
    var cur = null;
    var els = main.querySelectorAll("h1,h2,h3,h4,h5,h6,p,li,blockquote,td,th,pre");
    Array.prototype.forEach.call(els, function (el) {
      if (/^H[1-6]$/.test(el.tagName)) {
        cur = { id: el.id || "", title: el.textContent.trim(), parts: [] };
        entries.push(cur);
      } else {
        var t = (el.textContent || "").replace(/\s+/g, " ").trim();
        if (!t) return;
        if (!cur) { cur = { id: "", title: "（篇首）", parts: [] }; entries.push(cur); }
        cur.parts.push(t);
      }
    });
    entries.forEach(function (e) {
      e.norm = norm(e.title + " " + e.parts.join(" "));
    });
    return entries;
  }

  /* ---------- 查询词的简繁变体 ---------- */
  function variants(term) {
    var out = [term];
    [toCN, toTW].forEach(function (fn) {
      if (!fn) return;
      try {
        var v = fn(term);
        if (v && out.indexOf(v) < 0) out.push(v);
      } catch (e) {}
    });
    return out;
  }

  function reset() {
    clearMarks();
    panel.innerHTML = "";
    panel.hidden = true;
    meta.textContent = "";
  }

  function run(query) {
    var rawTerms = query.trim().split(/\s+/).filter(Boolean);
    if (!rawTerms.length) { reset(); return; }
    if (!index) index = buildIndex();

    // 每个词取其简繁变体，命中任一即算该词命中；多词之间取交集
    var termSets = rawTerms.map(variants);
    var hits = [];
    index.forEach(function (e) {
      var ok = termSets.every(function (set) {
        return set.some(function (t) { return e.norm.indexOf(norm(t)) >= 0; });
      });
      if (ok) hits.push(e);
    });

    render(hits, termSets[0]);
    highlight(termSets);
  }

  /* ---------- 结果面板 ---------- */
  function render(hits, firstSet) {
    panel.innerHTML = "";
    panel.hidden = hits.length === 0 ? true : false;
    meta.textContent = hits.length
      ? "命中 " + hits.length + " 节" + (hits.length > MAX_RESULTS ? "（列前 " + MAX_RESULTS + "）" : "")
      : "无命中";

    hits.slice(0, MAX_RESULTS).forEach(function (e) {
      var item = document.createElement("div");
      item.className = "sr-item";

      var title = document.createElement("div");
      title.className = "sr-title";
      title.textContent = e.title || "（无题）";
      item.appendChild(title);

      var snip = document.createElement("div");
      snip.className = "sr-snip";
      snip.appendChild(makeSnippet(e, firstSet));
      item.appendChild(snip);

      if (e.id) {
        item.addEventListener("click", function () { jumpTo(e.id); });
      } else {
        item.className += " sr-disabled";
      }
      panel.appendChild(item);
    });
  }

  function makeSnippet(entry, termSet) {
    var frag = document.createDocumentFragment();
    var text = entry.norm;
    var pos = -1, used = "";
    termSet.some(function (t) {
      var n = norm(t);
      var i = text.indexOf(n);
      if (i >= 0) { pos = i; used = n; return true; }
      return false;
    });
    if (pos < 0) {
      frag.appendChild(document.createTextNode(text.slice(0, SNIP * 2) + "…"));
      return frag;
    }
    var from = Math.max(0, pos - SNIP);
    var to = Math.min(text.length, pos + used.length + SNIP);
    if (from > 0) frag.appendChild(document.createTextNode("…" + text.slice(from, pos)));
    var b = document.createElement("b");
    b.textContent = text.slice(pos, pos + used.length);
    frag.appendChild(b);
    var tail = text.slice(pos + used.length, to);
    frag.appendChild(document.createTextNode(tail + (to < text.length ? "…" : "")));
    return frag;
  }

  function jumpTo(id) {
    var el = document.getElementById(id);
    if (!el) return;
    el.scrollIntoView({ block: "start", behavior: "smooth" });
    el.classList.add("sr-target");
    setTimeout(function () { el.classList.remove("sr-target"); }, 1600);
  }

  /* ---------- 正文高亮 ---------- */
  function clearMarks() {
    marks.forEach(function (m) {
      var p = m.parentNode;
      if (p) p.replaceChild(document.createTextNode(m.textContent), m);
    });
    marks = [];
    if (main.normalize) main.normalize();
  }

  function highlight(termSets) {
    clearMarks();
    // 正文里按原样词形匹配（含简繁变体），逐文本节点替换
    var needles = [];
    termSets.forEach(function (set) {
      set.forEach(function (t) { if (t && needles.indexOf(t) < 0) needles.push(t); });
    });
    needles.sort(function (a, b) { return b.length - a.length; });

    var walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.nodeValue || !n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        var tag = n.parentNode && n.parentNode.nodeName;
        if (tag === "SCRIPT" || tag === "STYLE" || tag === "MARK") return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);

    var budget = MAX_MARKS;
    nodes.forEach(function (node) {
      if (budget <= 0) return;
      var text = node.nodeValue;
      var parts = splitByText(text, needles, budget);
      if (!parts.matched) return;
      budget -= parts.count;
      var frag = document.createDocumentFragment();
      parts.list.forEach(function (seg) {
        if (seg.hit) {
          var m = document.createElement("mark");
          m.textContent = seg.text;
          marks.push(m);
          frag.appendChild(m);
        } else {
          frag.appendChild(document.createTextNode(seg.text));
        }
      });
      node.parentNode.replaceChild(frag, node);
    });
  }

  function splitByText(text, needles, limit) {
    var hits = [];
    needles.forEach(function (nd) {
      var i = text.indexOf(nd);
      while (i >= 0 && hits.length < limit) {
        hits.push([i, i + nd.length]);
        i = text.indexOf(nd, i + nd.length);
      }
    });
    if (!hits.length) return { list: [{ text: text, hit: false }], matched: false, count: 0 };

    hits.sort(function (a, b) { return a[0] - b[0]; });
    var merged = [];
    hits.forEach(function (h) {
      var last = merged[merged.length - 1];
      if (last && h[0] < last[1]) last[1] = Math.max(last[1], h[1]);
      else merged.push(h.slice());
    });

    var list = [], at = 0, count = 0;
    merged.forEach(function (h) {
      if (h[0] > at) list.push({ text: text.slice(at, h[0]), hit: false });
      list.push({ text: text.slice(h[0], h[1]), hit: true });
      at = h[1]; count++;
    });
    if (at < text.length) list.push({ text: text.slice(at), hit: false });
    return { list: list, matched: true, count: count };
  }

  /* ---------- 事件 ---------- */
  box.addEventListener("input", function () {
    clearTimeout(timer);
    var v = this.value;
    timer = setTimeout(function () { run(v); }, 160);
  });
  box.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { this.value = ""; reset(); }
    if (e.key === "Enter") {
      var first = panel.querySelector(".sr-item");
      if (first) first.click();
    }
  });

  // 供阅读偏好脚本在简繁切换后重挂高亮（innerHTML 还原会抹掉 <mark>）
  window.__pageSearch = {
    refresh: function () {
      index = null;            // 显示文字已变，重建索引以保证标题与摘要一致
      if (box.value.trim()) run(box.value); else reset();
    },
    clear: function () { box.value = ""; reset(); }
  };
})();
