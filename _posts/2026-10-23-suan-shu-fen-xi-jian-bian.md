---
layout: post
title: 算术简编
categories: [工]
mathjax: true
date: 2026-10-23 10:00
---

算术简编：系统整理数学思维的核心方法——数形结合、分类讨论、转化化归、函数方程、建模、归纳演绎、极限、概率统计、空间想象、优化、对称守恒、公理化。每种方法配动态SVG图解、通俗案例与历史典故，适合各年级学生理解数学思想。

---

## 1. 数形结合

**归纳**：看几个例子，猜出规律（从特殊到一般）。
**演绎**：知道一般规律，推出具体结论（从一般到特殊）。

<div align="center">
<svg width="380" height="220" viewBox="-40 0 420 220" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<!-- 左侧：数字 -->
<rect x="20" y="40" width="120" height="60" rx="8" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2"/>
<text x="45" y="65" class="t">x²=4</text>
<text x="45" y="85" class="lbl">抽象数字</text>
<!-- 中间箭头：动态 -->
<line x1="140" y1="70" x2="200" y2="70" stroke="#f26522" stroke-width="2.5" stroke-dasharray="60">
<animate attributeName="stroke-dashoffset" from="60" to="0" dur="1.5s" repeatCount="indefinite"/>
</line>
<polygon points="200,65 210,70 200,75" fill="#f26522"/>
<text x="155" y="55" class="lbl">画图</text>
<!-- 右侧：图形 -->
<rect x="220" y="30" width="150" height="80" rx="8" fill="#fff3e0" stroke="#f26522" stroke-width="2"/>
<!-- 抛物线 -->
<path d="M 240 90 Q 295 40 350 90" fill="none" stroke="#2b7bba" stroke-width="2.5"/>
<!-- 与x轴交点，动态闪烁 -->
<circle cx="265" cy="90" r="5" fill="#c00">
<animate attributeName="r" values="5;7;5" dur="1s" repeatCount="indefinite"/>
</circle>
<circle cx="325" cy="90" r="5" fill="#c00">
<animate attributeName="r" values="5;7;5" dur="1s" begin="0.5s" repeatCount="indefinite"/>
</circle>
<line x1="230" y1="90" x2="360" y2="90" stroke="#999" stroke-width="1"/>
<text x="250" y="130" class="lbl">交点就是解：x=±2</text>
</svg>
</div>

**应用案例**：
- 小学生：$3+2=$？画3个苹果再画2个苹果，数一下一共5个。
- 初中生：解方程 $x^2-4=0$，画抛物线 $y=x^2-4$，与x轴交叉的地方就是解。
- 高中生：解不等式 $x^2-4<0$，看抛物线在x轴下面的部分。

**历史来源故事**：
笛卡尔生病卧床，看到蜘蛛在天花板织网，灵光一闪——用坐标定位蜘蛛位置，创立解析几何。恩格斯说："笛卡尔的变数是数学的转折点，运动和辩证法进入了数学。"

---

## 2. 分类讨论

**归纳**：看几个例子，猜出规律（从特殊到一般）。
**演绎**：知道一般规律，推出具体结论（从一般到特殊）。

<div align="center">
<svg width="380" height="220" viewBox="-40 0 420 220" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<!-- 顶部：问题 -->
<circle cx="190" cy="35" r="25" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2.5"/>
<text x="178" y="40" class="t">问题</text>
<!-- 分支线，动态绘制 -->
<path d="M 190 60 L 100 100" fill="none" stroke="#2b7bba" stroke-width="2">
<animate attributeName="stroke-dasharray" values="0,100;100,0" dur="1.5s" repeatCount="indefinite"/>
</path>
<path d="M 190 60 L 190 100" fill="none" stroke="#2b7bba" stroke-width="2">
<animate attributeName="stroke-dasharray" values="0,100;100,0" dur="1.5s" begin="0.3s" repeatCount="indefinite"/>
</path>
<path d="M 190 60 L 280 100" fill="none" stroke="#2b7bba" stroke-width="2">
<animate attributeName="stroke-dasharray" values="0,100;100,0" dur="1.5s" begin="0.6s" repeatCount="indefinite"/>
</path>
<!-- 三个分支，依次出现 -->
<circle cx="100" cy="125" r="22" fill="#fff3e0" stroke="#f26522" stroke-width="2">
<animate attributeName="opacity" values="0;1;1" dur="2s" repeatCount="indefinite"/>
</circle>
<text x="88" y="130" class="t">a>0</text>
<circle cx="190" cy="125" r="22" fill="#fff3e0" stroke="#f26522" stroke-width="2">
<animate attributeName="opacity" values="0;0;1;1" dur="2s" repeatCount="indefinite"/>
</circle>
<text x="178" y="130" class="t">a=0</text>
<circle cx="280" cy="125" r="22" fill="#fff3e0" stroke="#f26522" stroke-width="2">
<animate attributeName="opacity" values="0;0;0;1;1" dur="2s" repeatCount="indefinite"/>
</circle>
<text x="268" y="130" class="t">a<0</text>
<text x="60" y="175" class="lbl">逐类讨论 → 综合答案</text>
<text x="60" y="195" class="lbl">不重复、不遗漏</text>
</svg>
</div>

**应用案例**：
- 小学生：一个数的绝对值等于5，这个数是多少？正数5和负数-5都可能。
- 初中生：解 $\lvert x-2\rvert+\lvert x+3\rvert=7$，分三段讨论。
- 高中生：讨论参数 $a$ 对二次方程根的影响。

**历史来源故事**：
《九章算术》"盈不足"问题，古人把问题分成两种情况讨论。刘徽注《九章》时强调"各类不重不漏"——这是中国最早的分类讨论思想。

---

## 3. 转化化归

**归纳**：看几个例子，猜出规律（从特殊到一般）。
**演绎**：知道一般规律，推出具体结论（从一般到特殊）。

<div align="center">
<svg width="380" height="200" viewBox="-40 0 420 200" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<!-- 左侧：难题 -->
<rect x="20" y="50" width="110" height="55" rx="8" fill="#ffe0e0" stroke="#c00" stroke-width="2.5"/>
<text x="45" y="75" class="t">难题</text>
<text x="45" y="95" class="lbl">陌生复杂</text>
<!-- 变形箭头，动态 -->
<path d="M 130 77 Q 170 50 210 77" fill="none" stroke="#f26522" stroke-width="2.5" stroke-dasharray="80">
<animate attributeName="stroke-dashoffset" from="80" to="0" dur="1.5s" repeatCount="indefinite"/>
</path>
<polygon points="210,72 220,77 210,82" fill="#f26522"/>
<text x="150" y="55" class="lbl">转化</text>
<!-- 右侧：简单题 -->
<rect x="230" y="50" width="110" height="55" rx="8" fill="#e8f5e9" stroke="#2b7bba" stroke-width="2.5"/>
<text x="255" y="75" class="t">简单题</text>
<text x="255" y="95" class="lbl">熟悉会做</text>
<text x="40" y="140" class="lbl">例：分数方程 → 两边同乘分母 → 整数方程</text>
<text x="40" y="165" class="lbl">例：不规则图形 → 割补成熟悉图形</text>
</svg>
</div>

**应用案例**：
- 小学生：$\frac12+\frac13=$？通分变成 $\frac36+\frac26=\frac56$。
- 初中生：解分式方程，两边同乘分母变整数方程。
- 高中生：求不规则图形面积，割补成长方形和三角形。

**历史来源故事**：
欧拉解决哥尼斯堡七桥问题，把陆地画成点、桥画成线，变成"一笔画"问题——不解决具体问题，而是转化为模型。

---

## 4. 函数与方程

**归纳**：看几个例子，猜出规律（从特殊到一般）。
**演绎**：知道一般规律，推出具体结论（从一般到特殊）。

<div align="center">
<svg width="380" height="220" viewBox="-40 0 420 220" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<!-- 坐标轴 -->
<line x1="30" y1="170" x2="360" y2="170" stroke="#999" stroke-width="1.5"/>
<line x1="30" y1="30" x2="30" y2="180" stroke="#999" stroke-width="1.5"/>
<!-- 曲线，动态绘制 -->
<path d="M 50 150 Q 150 50 250 110 T 350 80" fill="none" stroke="#2b7bba" stroke-width="3" stroke-dasharray="400">
<animate attributeName="stroke-dashoffset" from="400" to="0" dur="3s" fill="freeze"/>
</path>
<!-- 动点，沿曲线移动 -->
<circle cx="50" cy="150" r="6" fill="#f26522">
<animate attributeName="cx" values="50;150;250;350;50" dur="6s" repeatCount="indefinite"/>
<animate attributeName="cy" values="150;70;110;80;150" dur="6s" repeatCount="indefinite"/>
</circle>
<text x="60" y="200" class="lbl">x变化 → y随之变化</text>
<text x="60" y="215" class="lbl">例：出租车费 = 起步价 + 超出里程×单价</text>
</svg>
</div>

**应用案例**：
- 小学生：买铅笔2元一支，买3支多少钱？$2\times3=6$ 元。
- 初中生：出租车起步价10元（含3公里），超出每公里2元。坐10公里 $10+2\times7=24$ 元。
- 高中生：产量随时间变化 $P(t)=P_0 e^{rt}$。

**历史来源故事**：
伽利略在比萨斜塔实验，用函数描述自由落体距离 $s=\frac12gt^2$。牛顿在《自然哲学的数学原理》中用函数描述万有引力——函数成为现代科学的通用语言。

---

## 5. 建模思维

**归纳**：看几个例子，猜出规律（从特殊到一般）。
**演绎**：知道一般规律，推出具体结论（从一般到特殊）。

<div align="center">
<svg width="380" height="200" viewBox="-40 0 420 200" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:12px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<!-- 流程：实际问题→数学模型→求解检验，依次出现 -->
<rect x="15" y="50" width="95" height="45" rx="6" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2">
<animate attributeName="opacity" values="0;1;1;1;1" dur="4s" repeatCount="indefinite"/>
</rect>
<text x="30" y="77" class="t">实际问题</text>
<line x1="110" y1="72" x2="135" y2="72" stroke="#2b7bba" stroke-width="1.5">
<animate attributeName="stroke-dasharray" values="0,30;30,0" dur="4s" repeatCount="indefinite"/>
</line>
<polygon points="135,67 145,72 135,77" fill="#2b7bba"/>
<rect x="150" y="50" width="95" height="45" rx="6" fill="#fff3e0" stroke="#f26522" stroke-width="2">
<animate attributeName="opacity" values="0;0;1;1;1" dur="4s" repeatCount="indefinite"/>
</rect>
<text x="165" y="77" class="t">数学模型</text>
<line x1="245" y1="72" x2="270" y2="72" stroke="#2b7bba" stroke-width="1.5">
<animate attributeName="stroke-dasharray" values="0,30;0,0;30,0" dur="4s" repeatCount="indefinite"/>
</line>
<polygon points="270,67 280,72 270,77" fill="#2b7bba"/>
<rect x="285" y="50" width="95" height="45" rx="6" fill="#e8f5e9" stroke="#2b7bba" stroke-width="2">
<animate attributeName="opacity" values="0;0;0;1;1" dur="4s" repeatCount="indefinite"/>
</rect>
<text x="300" y="77" class="t">求解检验</text>
<text x="30" y="130" class="lbl">例：人口增长 P(t)=P₀e^(rt)</text>
<text x="30" y="155" class="lbl">例：传染病 SIR 模型</text>
</svg>
</div>

**应用案例**：
- 小学生：班里30人，每人发2个苹果，买多少个？$30\times2=60$ 个。
- 初中生：初始人口100万，年增2%，10年后 $P=100\times1.02^{10}\approx122$ 万。
- 高中生：SIR传染病模型预测疫情趋势。

**历史来源故事**：
马尔萨斯1798年提出人口论，用指数函数 $P=P_0e^{rt}$ 描述人口增长——这是最早的社会现象数学建模。后来Logistic模型考虑资源限制修正了它。

---

## 6. 归纳与演绎

**归纳**：看几个例子，猜出规律（从特殊到一般）。
**演绎**：知道一般规律，推出具体结论（从一般到特殊）。

<div align="center">
<svg width="380" height="220" viewBox="-40 0 420 220" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:12px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<!-- 归纳过程：逐个显示例子 -->
<text x="20" y="30" class="t">归纳：逐个看例子</text>
<rect x="20" y="45" width="100" height="25" rx="4" fill="#e8f3fc" stroke="#2b7bba">
<animate attributeName="opacity" values="0;1;1;1;1;1" dur="5s" repeatCount="indefinite"/>
</rect>
<text x="30" y="62" class="lbl">1=1²</text>
<rect x="20" y="75" width="100" height="25" rx="4" fill="#e8f3fc" stroke="#2b7bba">
<animate attributeName="opacity" values="0;0;1;1;1;1" dur="5s" repeatCount="indefinite"/>
</rect>
<text x="30" y="92" class="lbl">1+3=2²</text>
<rect x="20" y="105" width="100" height="25" rx="4" fill="#e8f3fc" stroke="#2b7bba">
<animate attributeName="opacity" values="0;0;0;1;1;1" dur="5s" repeatCount="indefinite"/>
</rect>
<text x="30" y="122" class="lbl">1+3+5=3²</text>
<!-- 猜想 -->
<rect x="140" y="70" width="120" height="40" rx="6" fill="#fff3e0" stroke="#f26522" stroke-width="2">
<animate attributeName="opacity" values="0;0;0;0;1;1" dur="5s" repeatCount="indefinite"/>
</rect>
<text x="155" y="95" class="t">猜想：前n奇数和=n²</text>
<!-- 演绎验证 -->
<text x="140" y="145" class="lbl">演绎：验证 n=4</text>
<text x="140" y="165" class="t">1+3+5+7=16=4² ✓</text>
</svg>
</div>

**应用案例**：
- 小学生：观察 $1=1^2$，$1+3=2^2$，$1+3+5=3^2$，猜前n个奇数和是 $n^2$。
- 初中生：验证 $n=4$：$1+3+5+7=16=4^2$ ✓。
- 高中生：观察数列 2,4,8,16…，归纳通项 $a_n=2^n$。

**历史来源故事**：
高斯小时候算 $1+2+\cdots+100$，发现首尾相加都是101，共50对，得5050——归纳的典范。毕达哥拉斯学派从勾股数归纳出定理，再演绎证明。

---

## 7. 极限思想

**归纳**：看几个例子，猜出规律（从特殊到一般）。
**演绎**：知道一般规律，推出具体结论（从一般到特殊）。

<div align="center">
<svg width="380" height="240" viewBox="-40 0 420 240" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<!-- 圆 -->
<circle cx="190" cy="110" r="70" fill="none" stroke="#999" stroke-width="1.5"/>
<!-- 内接多边形，边数动态增加 -->
<polygon points="190,40 251,75 251,145 190,180 129,145 129,75" fill="none" stroke="#f26522" stroke-width="2.5">
<animate attributeName="points" 
  values="
    190,40 251,75 251,145 190,180 129,145 129,75;
    190,40 245,62 265,110 245,158 190,180 135,158 115,110 135,62;
    190,40 230,52 260,85 268,125 245,160 200,178 155,160 132,125 140,85 160,52;
    190,40 251,75 251,145 190,180 129,145 129,75"
  dur="6s" repeatCount="indefinite"/>
</polygon>
<text x="60" y="210" class="lbl">边数越多 → 多边形越接近圆</text>
<text x="60" y="228" class="lbl">刘徽割圆术：割之弥细，所失弥少</text>
</svg>
</div>

**应用案例**：
- 小学生：$\frac12=0.5$，$\frac14=0.25$……越来越接近0。
- 初中生：刘徽割圆术，边数从6→12→24→48……逼近圆面积。
- 高中生：导数——瞬时变化率，无限短时间内的平均变化率。

**历史来源故事**：
刘徽公元263年提出割圆术："割之弥细，所失弥少，割之又割，以至于不可割，则与圆合体而无所失矣。"祖冲之用此法把π精确到小数点后7位，保持世界纪录近千年。

---

## 8. 概率统计

**归纳**：看几个例子，猜出规律（从特殊到一般）。
**演绎**：知道一般规律，推出具体结论（从一般到特殊）。

<div align="center">
<svg width="380" height="220" viewBox="-40 0 420 220" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="20" y="30" class="t">掷骰子：每个面概率1/6</text>
<!-- 六个骰子，动态随机变换 -->
<g>
<rect x="20" y="50" width="45" height="45" rx="6" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2"/>
<text x="35" y="78" class="t">1</text>
<animate attributeName="opacity" values="1;1;1;1" dur="6s" repeatCount="indefinite"/>
</g>
<g>
<rect x="75" y="50" width="45" height="45" rx="6" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2"/>
<text x="90" y="78" class="t">2</text>
</g>
<g>
<rect x="130" y="50" width="45" height="45" rx="6" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2"/>
<text x="145" y="78" class="t">3</text>
</g>
<g>
<rect x="185" y="50" width="45" height="45" rx="6" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2"/>
<text x="200" y="78" class="t">4</text>
</g>
<g>
<rect x="240" y="50" width="45" height="45" rx="6" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2"/>
<text x="255" y="78" class="t">5</text>
</g>
<g>
<rect x="295" y="50" width="45" height="45" rx="6" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2"/>
<text x="310" y="78" class="t">6</text>
</g>
<!-- 频率条，动态增长 -->
<text x="20" y="130" class="lbl">大量重复试验 → 频率稳定在概率附近</text>
<rect x="20" y="145" width="280" height="15" rx="3" fill="#f0f0f0"/>
<rect x="20" y="145" width="0" height="15" rx="3" fill="#2b7bba">
<animate attributeName="width" values="0;280;280" dur="6s" repeatCount="indefinite"/>
</rect>
<text x="20" y="180" class="lbl">大数定律：样本越大，估计越准</text>
</svg>
</div>

**应用案例**：
- 小学生：掷硬币正面朝上概率1/2，掷骰子掷出6的概率1/6。
- 初中生：掷两枚骰子，点数和为7的概率 $P=6/36=1/6$。
- 高中生：彩票中奖、天气预报降水概率、疾病检测准确率。

**历史来源故事**：
帕斯卡和费马17世纪通信讨论赌金分配问题，奠定概率论基础。凯特勒用统计方法分析犯罪率、死亡率，开创数理统计。

---

## 9. 空间想象

**归纳**：看几个例子，猜出规律（从特殊到一般）。
**演绎**：知道一般规律，推出具体结论（从一般到特殊）。

<div align="center">
<svg width="380" height="220" viewBox="-40 0 420 220" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<!-- 立方体，动态旋转 -->
<g>
<!-- 前面 -->
<rect x="80" y="60" width="80" height="80" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2"/>
<!-- 顶面 -->
<polygon points="80,60 100,45 180,45 160,60" fill="#fff3e0" stroke="#f26522" stroke-width="2"/>
<!-- 右面 -->
<polygon points="160,60 180,45 180,125 160,140" fill="#e8f5e9" stroke="#2b7bba" stroke-width="2"/>
<!-- 动态旋转效果 -->
<animateTransform attributeName="transform" type="rotate" from="0 130 100" to="360 130 100" dur="8s" repeatCount="indefinite"/>
</g>
<text x="60" y="180" class="lbl">立方体：正视图/侧视图/俯视图</text>
<text x="60" y="200" class="lbl">三视图还原立体图形</text>
</svg>
</div>

**应用案例**：
- 小学生：魔方从前面看是正方形。
- 初中生：圆柱从正面看是长方形，从上面看是圆形。
- 高中生：立方体切一刀，截面可能是三角形、四边形、五边形。

**历史来源故事**：
阿波罗尼乌斯《圆锥曲线论》系统研究圆锥被平面切开的截面——椭圆、抛物线、双曲线，这是空间想象的巅峰。欧拉在哥尼斯堡七桥问题中开创拓扑学。

---

## 10. 优化思想

**归纳**：看几个例子，猜出规律（从特殊到一般）。
**演绎**：知道一般规律，推出具体结论（从一般到特殊）。

<div align="center">
<svg width="380" height="220" viewBox="-40 0 420 220" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<!-- 坐标轴 -->
<line x1="30" y1="180" x2="360" y2="180" stroke="#999" stroke-width="1.5"/>
<line x1="30" y1="30" x2="30" y2="190" stroke="#999" stroke-width="1.5"/>
<!-- 抛物线曲线 -->
<path d="M 50 160 Q 190 40 330 160" fill="none" stroke="#2b7bba" stroke-width="3"/>
<!-- 最低点，动态闪烁 -->
<circle cx="190" cy="60" r="8" fill="#f26522">
<animate attributeName="r" values="8;12;8" dur="1.5s" repeatCount="indefinite"/>
<animate attributeName="opacity" values="1;0.7;1" dur="1.5s" repeatCount="indefinite"/>
</circle>
<text x="205" y="55" class="t">最小值点</text>
<text x="50" y="210" class="lbl">约束条件下求极值</text>
<text x="50" y="225" class="lbl">例：36米篱笆围菜地，正方形面积最大</text>
</svg>
</div>

**应用案例**：
- 小学生：36米篱笆围长方形，长=宽=9米时面积最大（81㎡）。
- 初中生：出租车费问题，找最省钱方案。
- 高中生：线性规划——资源限制下求最大利润。

**历史来源故事**：
欧拉研究最速降线问题——小球从A到B走什么路径最快。约翰·伯努利向全欧洲挑战，欧拉用变分法解决，发现最快路径是摆线。这开创了优化理论。

---

## 11. 对称与守恒

**归纳**：看几个例子，猜出规律（从特殊到一般）。
**演绎**：知道一般规律，推出具体结论（从一般到特殊）。

<div align="center">
<svg width="380" height="220" viewBox="-40 0 420 220" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<!-- 对称轴 -->
<line x1="190" y1="20" x2="190" y2="180" stroke="#999" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="195" y="35" class="lbl">对称轴</text>
<!-- 左侧图形 -->
<polygon points="80,100 120,70 160,100 120,130" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2.5">
<animate attributeName="opacity" values="1;1;1" dur="2s" repeatCount="indefinite"/>
</polygon>
<!-- 右侧镜像，动态显示 -->
<polygon points="300,100 260,70 220,100 260,130" fill="#ffe0e0" stroke="#c00" stroke-width="2.5">
<animate attributeName="opacity" values="0;1;1" dur="2s" repeatCount="indefinite"/>
</polygon>
<!-- 动态标注：面积相等 -->
<text x="100" y="160" class="lbl">左</text>
<text x="250" y="160" class="lbl">右</text>
<text x="130" y="180" class="lbl">镜像对称，面积相等</text>
<text x="130" y="200" class="lbl">利用对称性，只需算一半</text>
</svg>
</div>

**应用案例**：
- 小学生：等腰三角形沿高对折完全重合。
- 初中生：圆关于任何直径对称，只需算一半。
- 高中生：物理中能量守恒、动量守恒——变化中总量不变。

**历史来源故事**：
阿基米德发现杠杆原理——两边力矩相等就能平衡。诺特定理证明：每种对称性对应一个守恒量（时间平移→能量守恒，空间平移→动量守恒），这是现代物理的基石。

---

## 12. 公理化思想

**归纳**：看几个例子，猜出规律（从特殊到一般）。
**演绎**：知道一般规律，推出具体结论（从一般到特殊）。

<div align="center">
<svg width="380" height="220" viewBox="-40 0 420 220" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<!-- 公理节点 -->
<rect x="140" y="20" width="100" height="40" rx="6" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2.5"/>
<text x="165" y="45" class="t">公理</text>
<!-- 分支线，动态绘制 -->
<path d="M 190 60 L 100 95" fill="none" stroke="#2b7bba" stroke-width="2">
<animate attributeName="stroke-dasharray" values="0,100;100,0" dur="2s" repeatCount="indefinite"/>
</path>
<path d="M 190 60 L 190 95" fill="none" stroke="#2b7bba" stroke-width="2">
<animate attributeName="stroke-dasharray" values="0,100;100,0" dur="2s" begin="0.3s" repeatCount="indefinite"/>
</path>
<path d="M 190 60 L 280 95" fill="none" stroke="#2b7bba" stroke-width="2">
<animate attributeName="stroke-dasharray" values="0,100;100,0" dur="2s" begin="0.6s" repeatCount="indefinite"/>
</path>
<!-- 定理节点，依次出现 -->
<rect x="70" y="105" width="60" height="35" rx="5" fill="#fff3e0" stroke="#f26522" stroke-width="2">
<animate attributeName="opacity" values="0;1;1;1" dur="3s" repeatCount="indefinite"/>
</rect>
<text x="80" y="127" class="t">定理1</text>
<rect x="160" y="105" width="60" height="35" rx="5" fill="#fff3e0" stroke="#f26522" stroke-width="2">
<animate attributeName="opacity" values="0;0;1;1" dur="3s" repeatCount="indefinite"/>
</rect>
<text x="170" y="127" class="t">定理2</text>
<rect x="250" y="105" width="60" height="35" rx="5" fill="#fff3e0" stroke="#f26522" stroke-width="2">
<animate attributeName="opacity" values="0;0;0;1" dur="3s" repeatCount="indefinite"/>
</rect>
<text x="260" y="127" class="t">定理3</text>
<text x="60" y="170" class="lbl">从公理出发，逻辑推导整个体系</text>
<text x="60" y="190" class="lbl">欧几里得《几何原本》5条公理→465个定理</text>
</svg>
</div>

**应用案例**：
- 小学生：从"两点之间直线最短"推出三角形两边之和大于第三边。
- 初中生：欧几里得从5条公理推出整个平面几何。
- 高中生：牛顿从三大运动定律推出经典力学。

**历史来源故事**：
欧几里得公元前300年编写《几何原本》，从5条不证自明的公理出发，逻辑推导出465个定理。牛顿模仿这个结构写《自然哲学的数学原理》，爱因斯坦的相对论也基于公理化方法。

---

## 速查表：12种数学思维方法

| 方法 | 一句话 |
|---|---|
| 数形结合 | 数字↔图形互译 |
| 分类讨论 | 分情况逐类求解 |
| 转化化归 | 难题→简单题 |
| 函数方程 | 变化与等量 |
| 建模思维 | 现实→数学模型 |
| 归纳演绎 | 猜规律+证规律 |
| 极限思想 | 无限逼近 |
| 概率统计 | 随机规律 |
| 空间想象 | 头脑中三维图形 |
| 优化思想 | 约束下求最优 |
| 对称守恒 | 对称简化问题 |
| 公理化 | 公理推导体系 |
