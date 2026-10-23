---
layout: post
title: 概算分析
categories: [工]
mathjax: true
date: 2026-10-23 10:00
---

**符号约定**：$A$=现期量；$B$=基期量；$r$=增长率；$a$=分子增速；$b$=分母增速；$\Delta$=增长量；$n$=年份差

---

## 1. 化除为乘

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:13px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">A/(1+r) ≈ A(1−r)</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<circle cx="80" cy="65" r="4" fill="#2b7bba" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.8s" dur="0.3s" fill="freeze"/></circle>
<text x="95" y="69" class="lbl">舍弃 r² 高阶小项</text>
<line x1="80" y1="65" x2="80" y2="90" stroke="#2b7bba" stroke-width="1" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="1s" dur="0.3s" fill="freeze"/></line>
<text x="55" y="110" class="lbl">一阶近似</text>
</svg>
</div>

- **原理**：$\dfrac{1}{1+r}$ 泰勒一阶展开，$\\lvert r\\rvert$ 很小时，舍弃高阶小项 $r^2$
- **公式**：$\dfrac{A}{1+r}\approx A(1-r)\quad(r>0)$；$\dfrac{A}{1-r}\approx A(1+r)\quad(r<0)$
- **适用场景**：求基期量；限制条件 $\\lvert r\\rvert\le5\%$，增长率偏大时误差显著
- **应用案例**：现期1024，增速3%，基期≈$1024\times(1-3\%)=993.28$
- **误差方向**：$r>0$（正增长）估算结果**偏小**；$r<0$（负增长）估算结果**偏大**

---


**真实案例**：某省2025年GDP为5.2万亿元，同比增长3.2%，求2024年GDP。

计算：$B=\frac{A}{1+r}=\frac{5.2}{1+3.2\%}$。用化除为乘：$B\approx5.2\times(1-3.2\%)=5.2\times0.968=5.034$ 万亿元。

精算验证：$5.2/1.032\approx5.039$，误差仅0.1%，完全满足资料分析选项精度。关键启示：增长率≤5%时，化除为乘一步出答案，省去除法。

## 2. 百化分（特征数字法）

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:13px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">r = 1/n → Δ = A/(n+1)</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<rect x="70" y="52" width="55" height="22" fill="#e8f3fc" stroke="#2b7bba" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.8s" dur="0.4s" fill="freeze"/></rect>
<text x="135" y="67" class="lbl">百分数 ↔ 单位分数替换</text>
<text x="60" y="105" class="lbl">拟合替换</text>
</svg>
</div>

- **原理**：百分数替换为单位分数，把复杂乘除化简为一步除法，属于数值拟合替换
- **公式**：$r=\dfrac1n,\quad 增长量\ \Delta=\dfrac{A}{n+1}$；$r=-\dfrac1n,\quad 减少量=\dfrac{A}{n-1}$
- **常用百化分对照表**：

| 百分数 | 分数 | 百分数 | 分数 |
|---|---|---|---|
| 50% | 1/2 | 14.3% | 1/7 |
| 33.3% | 1/3 | 12.5% | 1/8 |
| 25% | 1/4 | 11.1% | 1/9 |
| 20% | 1/5 | 10% | 1/10 |
| 16.7% | 1/6 | 9.1% | 1/11 |

- **适用场景**：求增长量、减少量；百分数接近常见特征分数
- **应用案例**：现期286，增速14.3%（≈1/7），增长量≈$286\div8=35.75$
- **误差方向**：实际增速＞匹配的 $1/n$ → 估算偏大；实际增速＜匹配的 $1/n$ → 估算偏小

---


**真实案例**：某市2025年社会消费品零售总额为4860亿元，同比增长14.3%，求增长量。

计算：14.3%≈1/7，增长量 $\Delta=\frac{A}{n+1}=\frac{4860}{8}=607.5$ 亿元。

精算验证：$4860\times\frac{14.3\%}{1+14.3\%}=4860\times0.125=607.5$，分毫不差。关键启示：熟记1/2~1/11对应百分数，增长量题直接除(n+1)。

## 3. 截位直除

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:13px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">A/B ≈ A截 / B截</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<path d="M60 52 L95 52 L95 75 L60 75 Z" fill="none" stroke="#2b7bba" stroke-width="1.5" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.8s" dur="0.4s" fill="freeze"/></path>
<text x="105" y="67" class="lbl">保留2~3位有效数字</text>
<text x="55" y="105" class="lbl">截断控相对误差</text>
</svg>
</div>

- **原理**：有效数字截断，控制整体相对误差；分子分母同步取舍抵消部分误差
- **公式**：$\dfrac{A}{B}\approx\dfrac{A_{截}}{B_{截}}$
- **截位规则**：
  - 选项首位不同 → 截2位
  - 选项首位相同、第二位不同 → 截3位
  - 选项差距极小 → 截4位或精算
- **适用场景**：通用除法；任何求比值、倍数、比重的题目
- **应用案例**：$\dfrac{5421}{1236}$，首位不同，截两位：$54\div12=4.5$
- **误差方向**：分子分母同向四舍五入可抵消；单独进分子/舍分母，结果偏大，反之偏小

---


**真实案例**：某企业2025年营收24568万元，2024年为19873万元，求同比增速。

计算：增速 $=\frac{24568-19873}{19873}=\frac{4695}{19873}$。选项首位不同（20%、24%、28%、32%），截两位：$\frac{47}{20}=2.35$，即约23.5%，选最接近的24%。

关键启示：选项差距大时，截2位就够；差距小再截3位，避免无效精算。

## 4. 错位加减法

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">A/B ≈ (A+ΔA)/(B+ΔB)</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<line x1="50" y1="65" x2="110" y2="65" stroke="#2b7bba" stroke-width="1.5" stroke-dasharray="60"><animate attributeName="stroke-dashoffset" from="60" to="0" begin="0.8s" dur="0.6s" fill="freeze"/></line>
<line x1="150" y1="65" x2="210" y2="65" stroke="#2b7bba" stroke-width="1.5" stroke-dasharray="60"><animate attributeName="stroke-dashoffset" from="60" to="0" begin="1.1s" dur="0.6s" fill="freeze"/></line>
<text x="70" y="95" class="lbl">ΔA/A ≈ ΔB/B 同比例变化</text>
</svg>
</div>

- **原理**：分数近似不变条件：分子分母变化率近似相等 $\dfrac{\Delta A}{A}\approx\dfrac{\Delta B}{B}$，微分近似
- **公式**：$\dfrac{A}{B}\approx\dfrac{A+\Delta A}{B+\Delta B}$
- **操作技巧**：分母加/减多少，分子按比例同步加/减多少
- **适用场景**：多步连乘除、基期比重、基期平均数
- **应用案例**：$\dfrac{432}{1256}\times\dfrac{1+6.2\%}{1+12.5\%}$，同步调整分子分母简化运算
- **误差方向**：调整比例越接近，误差越小；比例不一致会引入单向偏差

---


**真实案例**：计算 $\frac{432}{1256}\times\frac{1+6.2\%}{1+12.5\%}$。

计算：分母1256加12.5%约157变成1413；分子432按比例加 $432\times\frac{157}{1256}\approx54$ 变成486。原式 $\approx\frac{486}{1413}=0.344$。

精算验证：原式 $=0.3439\times0.944=0.325$，误差约6%。关键启示：多步乘除时同比例调整分子分母，减少计算步骤。

## 5. 差分法

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">差分=(A₂−A₁)/(B₂−B₁)</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<text x="55" y="65" class="lbl">差分数 ↔ 小分数对比</text>
<line x1="50" y1="80" x2="280" y2="80" stroke-dasharray="4 3" stroke="#2b7bba" stroke-width="1.5" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.8s" dur="0.4s" fill="freeze"/></line>
<text x="65" y="108" class="lbl">等价交叉比较，无系统偏误</text>
</svg>
</div>

- **原理**：分式作差等价变形，避开大数交叉相乘
- **公式**：大分数 $\dfrac{A_2}{B_2}$、小分数 $\dfrac{A_1}{B_1}$（$A_2>A_1,B_2>B_1$）；$差分数=\dfrac{A_2-A_1}{B_2-B_1}$；差分数＞小分数 ⇒ 大分数更大
- **适用场景**：两个分数数值接近，比较大小
- **应用案例**：比较$\dfrac{512}{247}$与$\dfrac{534}{256}$，构造差分数$\dfrac{22}{9}$对比判断
- **误差方向**：纯等价推导，**无估算误差**，结论可靠

---


**真实案例**：比较 $\frac{512}{247}$ 与 $\frac{534}{256}$ 的大小。

计算：大分数 $\frac{534}{256}$，小分数 $\frac{512}{247}$。差分数 $=\frac{534-512}{256-247}=\frac{22}{9}\approx2.44$。比较差分数与小分数：$\frac{22}{9}\approx2.44$ vs $\frac{512}{247}\approx2.07$。差分数＞小分数，所以大分数更大。

关键启示：两个分数接近时，不用交叉相乘，构造差分数一步比出大小。

## 6. 插值法

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">判断 A/B > k 或 < k</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<line x1="100" y1="52" x2="100" y2="80" stroke="#2b7bba" stroke-width="2" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.8s" dur="0.3s" fill="freeze"/></line>
<text x="115" y="68" class="lbl">k=1/2,1/3,1/4…</text>
<text x="55" y="105" class="lbl">区间判定，不放缩计算</text>
</svg>
</div>

- **原理**：不等式放缩，引入易算参照分数，只判定区间，不精算结果
- **公式**：判定 $\dfrac{A}{B}>k$ 或 $\dfrac{A}{B}<k$（$k$ 为特征分数）
- **适用场景**：选项刚好分布在熟悉特征分数两侧
- **应用案例**：判断$\dfrac{215}{620}$和1/3大小，$620\times \dfrac13\approx206.7$，原式＞1/3
- **误差方向**：精确比较，**无估算误差**

---


**真实案例**：判断 $\frac{215}{620}$ 与1/3的大小关系。

计算：$620\times\frac13=206.7$。因为215＞206.7，所以 $\frac{215}{620}>\frac13\approx33.3\%$。

关键启示：不需要算出具体值，只需和特征分数比较大小，区间判定后直接排除选项。

## 7. 尾数法

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">(A±B)尾数 = (尾A±尾B)尾数</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<circle cx="80" cy="65" r="4" fill="#2b7bba" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.8s" dur="0.3s" fill="freeze"/></circle>
<text x="95" y="69" class="lbl">模10同余</text>
<text x="55" y="105" class="lbl">仅加减可用</text>
</svg>
</div>

- **原理**：十进制模10同余，和差尾数由尾数运算决定
- **公式**：$(A\pm B)$尾数 = $(A_{尾}\pm B_{尾})$尾数（减法需要借位修正）
- **适用场景**：单纯加减求和、求差；除法不可用
- **应用案例**：$3451+2789+1246$，尾数$1+9+6=16$，尾数为6
- **误差方向**：精确运算，**无估算误差**，注意减法借位

---


**真实案例**：某项目全年支出：3451万+2789万+1246万+893万=？

计算：尾数 $1+9+6+3=19$，尾数为9。选项中只有尾数为9的答案可选。

关键启示：加减题看尾数，秒出答案；但乘除题不能用尾数法。

## 8. 放缩法

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">A↑B↓ → 值↑；A↓B↑ → 值↓</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<line x1="50" y1="60" x2="120" y2="50" stroke="#2b7bba" stroke-width="1.5" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.8s" dur="0.4s" fill="freeze"/></line>
<line x1="50" y1="75" x2="120" y2="85" stroke="#2b7bba" stroke-width="1.5" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="1s" dur="0.4s" fill="freeze"/></line>
<text x="140" y="68" class="lbl">单调性锁定区间</text>
<text x="55" y="105" class="lbl">定向放缩</text>
</svg>
</div>

- **原理**：分式单调性，分子分母单独变化单向改变结果
- **公式**：$A\uparrow,B\downarrow \Rightarrow \dfrac{A}{B}\uparrow$；$A\downarrow,B\uparrow \Rightarrow \dfrac{A}{B}\downarrow$
- **适用场景**：判断估算值偏大偏小，锁定数值区间、排除选项
- **应用案例**：估算值算出来是126，已知估算偏小，直接排除小于126的选项
- **误差方向**：人为可控；主动放大估算，则真实值更小；主动缩小估算，则真实值更大

---


**真实案例**：估算某产品单价 $\frac{总价12600}{数量100}=126$ 元。已知估算时把数量看大了（100实际为98），问真实单价偏大还是偏小？

分析：分母看大→商偏小，所以真实单价＞126元。选项中大于126的只有130，直接选。

关键启示：放缩法用来判断方向，不计算具体值，快速排除选项。

## 9. 间隔增长率概算

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">R = r₁ + r₂ + r₁·r₂</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<rect x="70" y="52" width="45" height="22" fill="#e8f3fc" stroke="#2b7bba" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.8s" dur="0.4s" fill="freeze"/></rect>
<text x="125" y="67" class="lbl">小r舍弃 r₁·r₂</text>
<text x="55" y="105" class="lbl">复利展开</text>
</svg>
</div>

- **原理**：$(1+r_1)(1+r_2)-1$ 展开；增速很小时舍弃二阶乘积项
- **公式**：$R=r_1+r_2+r_1r_2$；概算：$R\approx r_1+r_2\quad(r_1,r_2<5\%)$
- **适用场景**：求间隔增长率（隔一年增长）
- **应用案例**：两年增速分别2%、3%，间隔增速≈5%
- **误差方向**：概算丢掉 $r_1r_2$，估算结果**一定偏小**

---


**真实案例**：某市2024年增速4%，2025年增速5%，求2025年相对2023年的间隔增速。

计算：$R=r_1+r_2+r_1r_2=4\%+5\%+4\%\times5\%=9\%+0.2\%=9.2\%$。概算 $R\approx9\%$。

精算验证：$(1.04)(1.05)-1=1.092-1=9.2\%$，精确。关键启示：小r时乘积项可舍，但记住概算结果偏小。

## 10. 混合增长率

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">r混 介于 r₁、r₂之间</text>
<line x1="40" y1="55" x2="300" y2="55" stroke="#666" stroke-width="1" stroke-dasharray="260"><animate attributeName="stroke-dashoffset" from="260" to="0" dur="1.2s" fill="freeze"/></line>
<circle cx="80" cy="55" r="4" fill="#2b7bba" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.8s" dur="0.3s" fill="freeze"/></circle>
<circle cx="240" cy="55" r="4" fill="#2b7bba" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.9s" dur="0.3s" fill="freeze"/></circle>
<circle cx="150" cy="55" r="4" fill="#f26522" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="1.1s" dur="0.3s" fill="freeze"/></circle>
<text x="120" y="80" class="lbl">偏向基期量大一侧</text>
</svg>
</div>

- **原理**：加权平均数，权重为基期量，不是现期量
- **公式**：$r_{混}=\dfrac{B_1 r_1+B_2 r_2}{B_1+B_2}$
- **适用场景**：整体由两部分组成：进出口、城乡、上下半年等
- **应用案例**：进口增速5%，出口增速12%，进出口整体增速在5%~12%之间
- **误差方向**：定性判断无误差；用现期代替基期估算权重时会引入偏差

---


**真实案例**：某省进口增速5%，出口增速12%，进口额2000亿、出口额3000亿，求进出口整体增速。

计算：混合增速介于5%~12%之间。出口权重更大（3000亿 vs 2000亿），整体增速偏向出口12%一侧，估算约 $5\%+\frac{3000}{5000}\times7\%=9.2\%$。

精算验证：$\frac{2000\times5\%+3000\times12\%}{5000}=\frac{100+360}{5000}=9.2\%$，精确。关键启示：混合增速居中不正中，偏向权重大的一方。

## 11. 两期比重差

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">Δ比重 = A/B · (a−b)/(1+a)</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<text x="55" y="65" class="lbl">a>b上升，a<b下降</text>
<text x="55" y="100" class="lbl">|Δ| < |a−b|</text>
</svg>
</div>

- **原理**：现期比重减去基期比重代数推导
- **公式**：$\Delta比重=\dfrac{A}{B}\cdot\dfrac{a-b}{1+a}$
- **速判结论**：
  - $a>b$ → 比重上升
  - $a<b$ → 比重下降
  - $a=b$ → 比重不变
  - 变化幅度＜$\\lvert a-b\\rvert$
- **适用场景**：判断比重升降、估算比重变化幅度
- **应用案例**：分子增速10%，分母增速6%，比重上升，变化值＜$\\lvert 10\\%-6\\%\\rvert=4\\%$
- **误差方向**：公式精确；做题直接取 $\\lvert a-b\\rvert$ 作为上限预判时，预判上限偏大

---


**真实案例**：某企业2025年营收增速10%（分子A），行业总营收增速6%（分母B），求该企业占行业比重的变化。

计算：$a=10\%$，$b=6\%$。$a>b$ → 比重上升。变化幅度 $\Delta=\frac{A}{B}\cdot\frac{a-b}{1+a}$。即使不知道具体A/B，变化值一定＜$\lvert a-b\rvert=4\%$。

关键启示：先判断升降，再估上限，两步排除选项。

## 12. 平均数增长率

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">r平均 = (a−b)/(1+b)</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<text x="55" y="65" class="lbl">平均数 A/B 的增长率</text>
<text x="55" y="100" class="lbl">增长率定义式推导</text>
</svg>
</div>

- **原理**：平均数 $\dfrac{A}{B}$，套用增长率定义推导
- **公式**：$r_{平均}=\dfrac{a-b}{1+b}$
- **适用场景**：人均、单价、单位产量等平均数的增长率
- **应用案例**：产量增速15%，人数增速7%，人均产量增速$=\dfrac{15\%-7\%}{1+7\%}\approx7.5\%$
- **误差方向**：公式本身精确，无估算误差

---


**真实案例**：某地区粮食产量增速15%，播种面积增速7%，求平均亩产增速。

计算：$r_{平均}=\frac{a-b}{1+b}=\frac{15\%-7\%}{1+7\%}=\frac{8\%}{1.07}\approx7.5\%$。

关键启示：平均数增长率不是两个增速直接相减，要除以(1+b)，这是高频易错点。

## 13. 年均增长率

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">(1+r)ⁿ = A/B → r ≈ (A/B−1)/n</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<rect x="70" y="52" width="55" height="22" fill="#fff3e0" stroke="#f26522" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.8s" dur="0.4s" fill="freeze"/></rect>
<text x="135" y="67" class="lbl">r小，近似线性展开</text>
<text x="55" y="105" class="lbl">复利概算</text>
</svg>
</div>

- **原理**：$(1+r)^n$ 二项式展开，$r$ 很小时舍弃高阶项
- **公式**：$A=B(1+r)^n$，概算：$r\approx\dfrac{A/B-1}{n}$
- **精确公式**：$r=\sqrt[n]{\dfrac{A}{B}}-1$
- **适用场景**：多年平均增速
- **应用案例**：5年从1000涨到1611，$1+r=\sqrt[5]{1.611}\approx1.1$，$r\approx10\%$
- **误差方向**：概算结果**偏大**（舍弃了高阶正项）

---


**真实案例**：某市GDP从2020年的8000亿增长到2025年的12000亿，求年均增速。

计算：$\frac{A}{B}=\frac{12000}{8000}=1.5$，$n=5$。$(1+r)^5=1.5$。概算 $r\approx\frac{1.5-1}{5}=10\%$。精算 $r=\sqrt[5]{1.5}-1\approx8.4\%$。

关键启示：概算结果偏大，实际值约8%~9%。开方题不用硬算，区间判断即可。

## 14. 贡献率与拉动增长率

<div align="center">
<svg width="360" height="120" viewBox="-40 0 400 120" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="10" y="25" class="t">贡献率=Δ部分/Δ总体；拉动=贡献率×总增速</text>
<line x1="20" y1="40" x2="320" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="280"><animate attributeName="stroke-dashoffset" from="280" to="0" dur="1.2s" fill="freeze"/></line>
<text x="55" y="65" class="lbl">部分增长对总体增长的贡献</text>
<text x="55" y="100" class="lbl">两个公式配套使用</text>
</svg>
</div>

- **原理**：分解总体增长的来源，量化各部分贡献
- **公式**：
  - 贡献率 $=\dfrac{\Delta_{部分}}{\Delta_{总体}}\times100\%$
  - 拉动增长率 $=$ 贡献率 $\times$ 总体增速
- **关系**：拉动增长率 = 贡献率 × 总体增速
- **适用场景**：GDP增长中各产业贡献、进出口对增长的拉动
- **应用案例**：总体增长8%，某产业贡献率30%，则拉动增长 $8\%\times30\%=2.4\%$
- **误差方向**：公式精确，注意贡献率和拉动增长率的区别（贡献率是比值，拉动是百分点）

---


**真实案例**：某省GDP增长8%，其中工业增加值贡献3个百分点，求工业对GDP增长的贡献率。

计算：拉动增长率=3个百分点，总体增速=8%。贡献率 $=\frac{拉动}{总增速}=\frac{3\%}{8\%}=37.5\%$。

关键启示：贡献率是比值（%），拉动是百分点，两者配套使用，不要混淆。

## 速查表：14种方法一句话总结

| 方法 | 一句话 |
|---|---|
| 化除为乘 | $\frac{A}{1+r}\approx A(1-r)$，限 $\|r\|\le5\%$ |
| 百化分 | $r=1/n$，增长量 $=A/(n+1)$ |
| 截位直除 | 选项差距大截2位，小截3位 |
| 错位加减 | 分子分母同比例变化，比值近似不变 |
| 差分法 | 构造差分数与小分数比较大小 |
| 插值法 | 与特征分数 $k$ 比较，不放缩 |
| 尾数法 | 只做加减，看尾数选答案 |
| 放缩法 | 分子↑分母↓ → 值↑，定向锁定区间 |
| 间隔增长率 | $R=r_1+r_2+r_1r_2$，小r可舍乘积 |
| 混合增长率 | 居中不正中，偏向基期量大的 |
| 两期比重差 | $a>b$ 上升，变化＜$\|a-b\|$ |
| 平均数增长率 | $\frac{a-b}{1+b}$ |
| 年均增长率 | $(1+r)^n=A/B$，概算偏大 |
| 贡献率/拉动 | 贡献率=Δ部分/Δ总体，拉动=贡献率×总增速 |
