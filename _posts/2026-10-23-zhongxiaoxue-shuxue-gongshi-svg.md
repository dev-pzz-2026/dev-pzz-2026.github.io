---
layout: post
title: 精算分析
date: 2026-10-23 08:00:00 +0800
categories: [工]
tags: [数学, 公式, SVG, 中小学, 教育]
mathjax: true
---

精算分析：以数学公式为核心，结合几何原理、历史故事与动态图解，按小学→初中→高中顺序编排，聚焦课标高频内容。所有动态图为原生 SMIL SVG，自动循环播放，无需外部资源。

> 一、小学阶段

### 1. 长方形面积 $S=ab$

**原理**：用单位面积小正方形密铺，行数乘列数得到总单位数量，即为面积。

**故事**：公元前三千年的古埃及，尼罗河每年夏季泛滥，河水淹没两岸农田，原有田地的地界会被洪水冲毁。洪水退去后，农民必须重新丈量划分土地，"如何计算地块大小"成为刚需。古埃及人用绳索拉出矩形，摆放单位大小石块铺满地块，慢慢总结出长×宽的算法。这套丈量技艺传到古希腊，"几何学"一词的希腊本意，就是土地测量。

**▶ 动态图解**：单位方块逐行填充，行列计数


<div align="center">

<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 长方形面积 S=ab：单位方块逐行填充 -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <rect x="50" y="40" width="40" height="40" fill="#d9e8f7" stroke="#0b5394" stroke-width="1.5"/>
  <text x="52" y="26" class="t">单位小正方形 = 1</text>

  <!-- 长方形网格 5列 × 3行 -->
  <g>
    <rect x="60" y="70" width="200" height="120" fill="#f7fbfe" stroke="#0b5394" stroke-width="2"/>
    <line x1="100" y1="70" x2="100" y2="190" stroke="#0b5394" stroke-width="0.8"/>
    <line x1="140" y1="70" x2="140" y2="190" stroke="#0b5394" stroke-width="0.8"/>
    <line x1="180" y1="70" x2="180" y2="190" stroke="#0b5394" stroke-width="0.8"/>
    <line x1="220" y1="70" x2="220" y2="190" stroke="#0b5394" stroke-width="0.8"/>
    <line x1="260" y1="70" x2="260" y2="190" stroke="#0b5394" stroke-width="0.8"/>
    <line x1="60"  y1="110" x2="260" y2="110" stroke="#0b5394" stroke-width="0.8"/>
    <line x1="60"  y1="150" x2="260" y2="150" stroke="#0b5394" stroke-width="0.8"/>
  </g>

  <!-- 填充的方块：第1行 -->
  <g>
    <rect x="60"  y="70"  width="40" height="40" fill="#6aa8e0" opacity="0.9"><animate attributeName="opacity" values="0;0.9;0.9" keyTimes="0;0.15;1" dur="6s" repeatCount="indefinite"/></rect>
    <rect x="100" y="70"  width="40" height="40" fill="#6aa8e0" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.1;0.25;1" dur="6s" repeatCount="indefinite"/></rect>
    <rect x="140" y="70"  width="40" height="40" fill="#6aa8e0" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.2;0.35;1" dur="6s" repeatCount="indefinite"/></rect>
    <rect x="180" y="70"  width="40" height="40" fill="#6aa8e0" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.3;0.45;1" dur="6s" repeatCount="indefinite"/></rect>
    <rect x="220" y="70"  width="40" height="40" fill="#6aa8e0" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.4;0.55;1" dur="6s" repeatCount="indefinite"/></rect>
  </g>
  <!-- 第2行 -->
  <g>
    <rect x="60"  y="110" width="40" height="40" fill="#8fc1ee" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.15;0.3;1" dur="6s" repeatCount="indefinite"/></rect>
    <rect x="100" y="110" width="40" height="40" fill="#8fc1ee" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.25;0.4;1" dur="6s" repeatCount="indefinite"/></rect>
    <rect x="140" y="110" width="40" height="40" fill="#8fc1ee" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.35;0.5;1" dur="6s" repeatCount="indefinite"/></rect>
    <rect x="180" y="110" width="40" height="40" fill="#8fc1ee" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.45;0.6;1" dur="6s" repeatCount="indefinite"/></rect>
    <rect x="220" y="110" width="40" height="40" fill="#8fc1ee" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.55;0.7;1" dur="6s" repeatCount="indefinite"/></rect>
  </g>
  <!-- 第3行 -->
  <g>
    <rect x="60"  y="150" width="40" height="40" fill="#b3d7f5" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.3;0.45;1" dur="6s" repeatCount="indefinite"/></rect>
    <rect x="100" y="150" width="40" height="40" fill="#b3d7f5" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.4;0.55;1" dur="6s" repeatCount="indefinite"/></rect>
    <rect x="140" y="150" width="40" height="40" fill="#b3d7f5" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.5;0.65;1" dur="6s" repeatCount="indefinite"/></rect>
    <rect x="180" y="150" width="40" height="40" fill="#b3d7f5" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.6;0.75;1" dur="6s" repeatCount="indefinite"/></rect>
    <rect x="220" y="150" width="40" height="40" fill="#b3d7f5" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0.9" keyTimes="0;0.7;0.85;1" dur="6s" repeatCount="indefinite"/></rect>
  </g>

  <!-- 标注 -->
  <text x="60" y="218" class="t">宽 b = 3 行</text>
  <text x="128" y="252" class="t">长 a = 5 列</text>

  <g>
    <text x="50" y="300" class="label" opacity="0">
      面积 S = 长×宽 = a × b
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.8;0.88;0.96;0.98;1" dur="6s" repeatCount="indefinite"/>
    </text>
    <text x="50" y="330" class="label" opacity="0">
      S = 5 × 3 = 15 个单位
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.86;0.93;0.96;0.98;1" dur="6s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：装修客厅铺复合地板，客厅长6米、宽4米，需购地板 $6\times4=24$ 平方米；工人按此下料，不多不少。足球场长105米、宽68米，草坪面积7140平方米——这块标准场地的尺寸就是按长方形面积公式设计的。



### 2. 正方形面积 $S=a^2$

**原理**：属于特殊的长方形，长与宽相等。

**故事**：古巴比伦泥板文书上很早就记录了正方形边长与面积的换算关系。当时城邦分配庄园、划分宅地，正方形地块规整，方便登记、收税。官吏和工匠依靠这套计算方法管理田产，是上古时期非常实用的算术工具。

**▶ 动态图解**：正方形边长与面积同步标注

<div align="center">
<svg width="400" height="320" viewBox="-40 0 440 320" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:Arial,sans-serif}.t{font-size:15px;fill:#1a1a1a}.label{font-size:16px;fill:#0b5394;font-weight:bold}</style></defs>
<rect x="100" y="60" width="160" height="160" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"><animate attributeName="opacity" values="0.5;1;0.5" dur="4s" repeatCount="indefinite"/></rect>
<text x="170" y="50" class="t">边长 a</text>
<text x="270" y="145" class="t">a</text>
<text x="160" y="145" class="label" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.2;0.4;0.8;1" dur="4s" repeatCount="indefinite"/>a × a = a²</text>
<text x="100" y="270" class="label">S = a² （特殊的长方形）</text>
</svg>
</div>

**真实案例**：边长80cm的正方形地砖，单块面积0.64㎡；100㎡的客厅需约156块地砖（$100\div0.64\approx156$），装修预算据此测算。方桌边长1.2米，桌布需做1.44㎡以上，四周才能垂下。


### 3. 平行四边形面积 $S=ah$

**原理**：割补转化，沿着高剪下一侧三角形，平移拼接成长方形，底、高不变，面积相等。

**故事**：古人发现倾斜的平行四边形很难直接数格子求面积，慢慢摸索出割补转化的思路。欧几里得在《几何原本》中，以同底等高图形面积相等为基础，严谨论证平行四边形、三角形的面积关系，割补法也成为古代几何证明最核心的思想方法。

**▶ 动态图解**：割补法，三角形平移成长方形


<div align="center">

<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 平行四边形面积 S=ah：割补法 平移到长方形 -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <!-- 平行四边形 ABCD: A(60,200) B(260,200) C(220,80) D(20,80) -->
  <path d="M60,200 L260,200 L220,80 L20,80 Z" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"/>

  <!-- 高 -->
  <line x1="220" y1="200" x2="220" y2="80" stroke="#e06666" stroke-width="2" stroke-dasharray="5 4"/>
  <text x="226" y="150" class="t" fill="#c0392b">h</text>

  <!-- 可移动的直角三角形(右侧斜角部分)：由 C(220,80) B(260,200) 与 垂足(260,80) 组成 -->
  <g>
    <path d="M220,80 L260,200 L260,80 Z" fill="#ffd9d9" stroke="#c0392b" stroke-width="2">
      <animateTransform attributeName="transform" type="translate" values="0,0;-200,0;0,0" dur="4s" repeatCount="indefinite"/>
    </path>
  </g>

  <text x="120" y="228" class="t">底 a</text>
  <text x="180" y="60" class="t">平行四边形</text>

  <g>
    <text x="50" y="290" class="label" opacity="0">
      割补 → 变成长方形
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.35;0.5;0.8;0.9;1" dur="4s" repeatCount="indefinite"/>
    </text>
    <text x="50" y="320" class="label" opacity="0">
      面积 = 底 × 高 = a × h
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.5;0.7;0.8;0.9;1" dur="4s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：小区停车位多为平行四边形，底5.3米、高2.4米，面积12.72㎡——比矩形多出的角度让车门更易开。校门口伸缩门拉开时每个菱形格的底×高，就是门片占地面积。



### 4. 三角形面积 $S=\frac{1}{2}ah$

**原理**：两个完全相同的三角形，可以拼成一个平行四边形，三角形面积是平行四边形的一半。

**故事**：古埃及、古巴比伦丈量土地时经常遇到三角地块，工匠发现两个全等三角形拼合为平行四边形，取一半就是单个三角形面积。公元1世纪，希腊工程师海伦又推导出海伦公式，仅依靠三条边长就能直接算出三角形面积，方便测算形状不规则的三角地块。

**▶ 动态图解**：两全等三角形拼平行四边形


<div align="center">

<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 三角形面积 S=½ah：两个全等三角形拼成平行四边形 -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <!-- 参考平行四边形（半透明底） -->
  <path d="M80,240 L320,240 L280,120 L40,120 Z" fill="#eef4fb" stroke="none"/>

  <!-- 原三角形 A(80,240) B(320,240) C(280,120) -->
  <path d="M80,240 L320,240 L280,120 Z" fill="#8fc1ee" stroke="#0b5394" stroke-width="2"/>
  <text x="110" y="265" class="t">底 a</text>
  <line x1="280" y1="240" x2="280" y2="120" stroke="#e06666" stroke-width="2" stroke-dasharray="5 4"/>
  <text x="284" y="185" class="t" fill="#c0392b">h</text>

  <!-- 可移动的另一个三角形（红），平移到左侧拼成平行四边形 -->
  <g>
    <path d="M320,240 L80,240 L40,120 Z" fill="#ffd9d9" stroke="#c0392b" stroke-width="2">
      <animateTransform attributeName="transform" type="translate" values="240,0;0,0;240,0" keyTimes="0;0.5;1" dur="4s" repeatCount="indefinite"/>
    </path>
  </g>

  <text x="175" y="70" class="t">三角形面积</text>

  <g>
    <text x="50" y="300" class="label" opacity="0">
      两个全等三角形拼成平行四边形
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.4;0.55;0.8;0.9;1" dur="4s" repeatCount="indefinite"/>
    </text>
    <text x="50" y="330" class="label" opacity="0">
      S = ½ × 底 × 高 = ½ a h
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.55;0.7;0.8;0.9;1" dur="4s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：红领巾底边长100cm、高33cm，需布料 $\frac12\times100\times33=1650$ 平方厘米；工厂按此批量裁剪。道路三角警示牌边长90cm，反光膜面积约3500平方厘米，据此采购材料。



### 5. 梯形面积 $S=\frac{(a+b)}{2}h$

**原理**：两个全等梯形翻转对拼，拼成底为"上底+下底"、高不变的平行四边形，再取一半。

**故事**：我国《九章算术·方田章》中将梯形田地称为"邪田"，书中完整记载梯形面积算法。秦汉时期，官吏丈量坡地、水渠截面、边角农田都要用到这个公式，是我国最早成文记载的面积公式之一。


**▶ 动态图解**：两个全等梯形翻转对拼成平行四边形
<div align="center">
<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif}.label{font-size:17px;fill:#0b5394;font-weight:bold}</style></defs>
<polygon points="80,240 160,80 320,80 380,240" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"/>
<line x1="320" y1="80" x2="320" y2="240" stroke="#f44336" stroke-width="1.5" stroke-dasharray="4 4"/>
<text x="210" y="66" font-size="15" fill="#1a1a1a">a 上底</text><text x="210" y="262" font-size="15" fill="#1a1a1a">b 下底</text><text x="330" y="165" font-size="15" fill="#1a1a1a">h 高</text>
<g><polygon points="80,240 160,80 320,80 380,240" fill="#ffd6d6" stroke="#c00" stroke-width="2"><animateTransform attributeName="transform" type="translate" values="0,0; 0,60; 0,0" dur="4s" repeatCount="indefinite"/></polygon></g>
<text x="100" y="330" font-size="18" fill="#0b5394" font-weight="bold">S = (a+b)h / 2</text>
</svg>
</div>

**真实案例**：灌溉水渠截面是梯形，上底2米、下底1.2米、深1.5米，过水断面面积 $\frac{(2+1.2)}{2}\times1.5=2.4$ 平方米；水力学按此计算流速和流量。水库大坝截面也是梯形，上窄下宽抗水压。


### 6. 圆周长 $C=2\pi r=\pi d$

**原理**：圆周率 $\pi$ 是圆周长和直径固定不变的比值。

**故事**：魏晋刘徽首创割圆术，不断倍增圆内接正多边形的边数，用多边形周长无限逼近圆周，算至正3072边形，求得 $\pi\approx3.1416$。南北朝祖冲之继续演算，算出圆周率介于3.1415926与3.1415927之间，这项高精度纪录在世界上保持近千年，成果收录于《缀术》。

**▶ 动态图解**：圆周展开成直线，π倍直径


<div align="center">

<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 圆周长 C=πd：圆周展开成直线 -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <!-- 圆 -->
  <circle cx="130" cy="170" r="60" fill="#d9e8f7" stroke="#0b5394" stroke-width="3"/>
  <!-- 直径 -->
  <line x1="70" y1="170" x2="190" y2="170" stroke="#e06666" stroke-width="2.5"/>
  <text x="118" y="163" class="t" fill="#c0392b">d</text>
  <text x="130" y="246" class="t">圆周长 = ?</text>

  <!-- 展开的直线，从圆边逐渐展开，长度对应 πd -->
  <g>
    <line x1="300" y1="170" x2="300" y2="170" stroke="#6aa84f" stroke-width="6" stroke-linecap="round">
      <animate attributeName="x2" values="300;300;300;300;300;300;410;410;410;410;410;410;300" keyTimes="0;0.15;0.3;0.45;0.6;0.7;0.75;0.85;0.9;0.92;0.95;0.98;1" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;1;1;1;1;0;1;1;1;0;0;0;1" keyTimes="0;0.1;0.2;0.3;0.5;0.6;0.7;0.8;0.88;0.9;0.92;0.95;1" dur="6s" repeatCount="indefinite"/>
    </line>
  </g>
  <circle cx="300" cy="170" r="4" fill="#6aa84f"/>
  <text x="304" y="162" class="t" fill="#38761d">周长 C ≈ πd ≈ 3.14d</text>

  <g>
    <text x="50" y="300" class="label" opacity="0">
      周长是直径的 π 倍
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.6;0.72;0.9;0.95;1" dur="6s" repeatCount="indefinite"/>
    </text>
    <text x="50" y="330" class="label" opacity="0">
      C = π d  （π ≈ 3.14159）
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.72;0.85;0.9;0.95;1" dur="6s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：标准400米跑道弯道半径36.5米，两个弯道合起来约一圈圆周长 $2\pi\times36.5\approx229$ 米，加上两条直道各85.5米正好400米。圆形花坛直径8米，围护栏杆需 $\pi\times8\approx25$ 米。



### 7. 圆面积 $S=\pi r^2$

**原理**：将圆分割成大量细小扇形，交错拼接，近似得到一个长方形，长为半周长 $\pi r$，宽为半径 $r$。

**故事**：刘徽的割圆术同时用于求圆面积，依靠无限分割逼近的思想推导出圆面积公式。现在课本里剪开圆形拼成长方形的演示，源头正是两千年前刘徽的割圆思想。

**▶ 动态图解**：圆切拼成近似长方形


<div align="center">

<svg width="480" height="360" viewBox="0 0 480 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 圆面积 S=πr²：圆切拼成长方形 -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <!-- 圆，圆心(110,180) r=70 -->
  <circle cx="110" cy="180" r="70" fill="#eef4fb" stroke="#0b5394" stroke-width="2.5"/>
  <!-- 半径 -->
  <line x1="110" y1="180" x2="110" y2="110" stroke="#e06666" stroke-width="2"/>
  <text x="114" y="150" class="t" fill="#c0392b">r</text>
  <text x="110" y="272" class="t">圆 = 若干细扇形</text>

  <!-- 8个扇形分块动画：整体移动到右侧排成长方条 -->
  <g>
    <!-- 上方扇形 -->
    <path d="M110,180 L110,110 A70 70 0 0 1 172,136 Z" fill="#8fc1ee" stroke="#0b5394" stroke-width="1">
      <animateTransform attributeName="transform" type="translate" values="0,0;210,30;0,0" dur="5s" repeatCount="indefinite"/>
    </path>
    <!-- 右上 -->
    <path d="M110,180 L172,136 A70 70 0 0 1 180,180 Z" fill="#b3d7f5" stroke="#0b5394" stroke-width="1">
      <animateTransform attributeName="transform" type="translate" values="0,0;190,30;0,0" dur="5s" repeatCount="indefinite"/>
    </path>
    <!-- 右下 -->
    <path d="M110,180 L180,180 A70 70 0 0 1 172,224 Z" fill="#8fc1ee" stroke="#0b5394" stroke-width="1">
      <animateTransform attributeName="transform" type="translate" values="0,0;170,30;0,0" dur="5s" repeatCount="indefinite"/>
    </path>
    <!-- 下 -->
    <path d="M110,180 L172,224 A70 70 0 0 1 110,250 Z" fill="#b3d7f5" stroke="#0b5394" stroke-width="1">
      <animateTransform attributeName="transform" type="translate" values="0,0;150,30;0,0" dur="5s" repeatCount="indefinite"/>
    </path>
    <!-- 左下 -->
    <path d="M110,180 L110,250 A70 70 0 0 1 48,224 Z" fill="#8fc1ee" stroke="#0b5394" stroke-width="1">
      <animateTransform attributeName="transform" type="translate" values="0,0;130,30;0,0" dur="5s" repeatCount="indefinite"/>
    </path>
    <!-- 左 -->
    <path d="M110,180 L48,224 A70 70 0 0 1 40,180 Z" fill="#b3d7f5" stroke="#0b5394" stroke-width="1">
      <animateTransform attributeName="transform" type="translate" values="0,0;110,30;0,0" dur="5s" repeatCount="indefinite"/>
    </path>
    <!-- 左上 -->
    <path d="M110,180 L40,180 A70 70 0 0 1 48,136 Z" fill="#8fc1ee" stroke="#0b5394" stroke-width="1">
      <animateTransform attributeName="transform" type="translate" values="0,0;90,30;0,0" dur="5s" repeatCount="indefinite"/>
    </path>
    <!-- 左上顶 -->
    <path d="M110,180 L48,136 A70 70 0 0 1 110,110 Z" fill="#b3d7f5" stroke="#0b5394" stroke-width="1">
      <animateTransform attributeName="transform" type="translate" values="0,0;70,30;0,0" dur="5s" repeatCount="indefinite"/>
    </path>
  </g>

  <!-- 拼成近似长方形边框 -->
  <g opacity="0">
    <rect x="300" y="120" width="170" height="70" fill="none" stroke="#6aa84f" stroke-width="2" stroke-dasharray="5 4">
      <animate attributeName="opacity" values="0;0;0.9;0.9;0;0" keyTimes="0;0.4;0.5;0.8;0.9;1" dur="5s" repeatCount="indefinite"/>
    </rect>
  </g>

  <g>
    <text x="50" y="320" class="label" opacity="0">
      拼成近似长方形：长≈½周长=πr，宽=r
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.45;0.58;0.82;0.9;1" dur="5s" repeatCount="indefinite"/>
    </text>
    <text x="50" y="348" class="label" opacity="0">
      S = πr × r = π r²
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.6;0.72;0.82;0.9;1" dur="5s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：12寸披萨直径30cm，面积约707平方厘米；9寸披萨面积约452平方厘米——两个9寸还不如一个12寸大，披萨店定价就是按圆面积算的。半径15米的圆形街心花园，铺草皮需706㎡。



### 8. 长方体体积 $V=abh$；正方体 $V=a^3$

**原理**：用单位小立方体堆叠，底面积（长×宽）再乘层数（高），得到总个数即体积。

**故事**：《九章算术·商功章》专门记载土方、粮仓体积计算。古代修筑城墙、开挖沟渠、修建粮仓，都要估算土石用量、粮食储量，长方体、正方体体积算法就是为这类工程计算而生。

**▶ 动态图解**：单位小立方体逐层堆叠

<div align="center">
<svg width="420" height="320" viewBox="-40 0 460 320" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:Arial,sans-serif}.t{font-size:14px;fill:#1a1a1a}.label{font-size:16px;fill:#0b5394;font-weight:bold}</style></defs>
<!-- 长方体线框 -->
<polygon points="80,220 280,220 320,180 120,180" fill="none" stroke="#0b5394" stroke-width="2"/>
<polygon points="80,220 280,220 280,80 80,80" fill="#eef4fb" stroke="#0b5394" stroke-width="2"><animate attributeName="opacity" values="0.6;1;0.6" dur="5s" repeatCount="indefinite"/></polygon>
<polygon points="280,220 320,180 320,40 280,80" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"/>
<polygon points="80,80 280,80 320,40 120,40" fill="#f7fbfe" stroke="#0b5394" stroke-width="2"/>
<text x="170" y="240" class="t">长 a</text>
<text x="45" y="155" class="t">高 h</text>
<text x="300" y="140" class="t">宽 b</text>
<text x="100" y="285" class="label">V = 长 × 宽 × 高 = abh</text>
</svg>
</div>

**真实案例**：微波炉内尺寸长30cm×宽25cm×高20cm，容积15升；包装箱按此外加泡沫厚度设计。快递纸箱外箱长40×宽30×高30cm，可装约36升货物，物流按体积重计费。


### 9. 圆柱体积 $V=Sh=\pi r^2 h$

**原理**：把圆柱沿半径切开拼合，近似转化成长方体，底面积、高保持不变。

**故事**：阿基米德潜心研究圆柱与它的内切球，证明圆柱体积是内切球的 $\frac{3}{2}$。这是他一生最得意的发现，他留下遗言，要求后人把圆柱内切球图案刻在自己墓碑上。


**▶ 动态图解**：圆柱切分、交错拼近似长方体
<div align="center">
<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif}.label{font-size:17px;fill:#0b5394;font-weight:bold}.t{font-size:15px;fill:#1a1a1a}</style></defs>
<ellipse cx="120" cy="100" rx="70" ry="26" fill="#e0edf9" stroke="#0b5394" stroke-width="2"/><line x1="50" y1="100" x2="50" y2="240" stroke="#0b5394" stroke-width="2"/><line x1="190" y1="100" x2="190" y2="240" stroke="#0b5394" stroke-width="2"/><ellipse cx="120" cy="240" rx="70" ry="26" fill="none" stroke="#0b5394" stroke-width="2"/>
<g><polygon points="120,100 190,100 190,240 120,240" fill="#b8ddff" stroke="#0b5394"><animateTransform attributeName="transform" type="translate" values="0,0; 150,0; 0,0" dur="5s" repeatCount="indefinite"/></polygon></g>
<text x="95" y="66" class="t">r</text><text x="25" y="175" class="t">h</text>
<text x="110" y="315" class="label">V = π r² h</text>
</svg>
</div>

**真实案例**：圆柱形水桶底面半径20cm、高40cm，容积 $\pi\times20^2\times40\approx50$ 升；厨房烧水壶1.5升、饮水机桶18.9升，都是按圆柱体积标定的。烟囱直径0.4米、高10米，排烟量约1.26立方米。


### 10. 圆锥体积 $V=\frac{1}{3}Sh$

**原理**：同底等高条件下，圆锥体积是圆柱体积的三分之一，可通过注水实验直观验证。

**故事**：古人常见的谷堆、土堆都是圆锥形态，长久以来不知道圆锥体积的计算系数。阿基米德用穷竭法严格证明了 $\frac{1}{3}$ 这个关系。古代农户估算囤里粮食多少，都会使用这个公式。


**▶ 动态图解**：等底等高，圆锥向圆柱倾倒三次填满
<div align="center">
<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif}.label{font-size:17px;fill:#0b5394;font-weight:bold}.t{font-size:15px;fill:#1a1a1a}</style></defs>
<polygon points="80,240 150,60 220,240" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"/><line x1="150" y1="60" x2="150" y2="240" stroke="#f44336" stroke-dasharray="4 4"/>
<g transform="translate(250,0)"><ellipse cx="70" cy="240" rx="70" ry="24" fill="#eef6ff" stroke="#0b5394" stroke-width="2"/><line x1="0" y1="80" x2="0" y2="240" stroke="#0b5394" stroke-width="2"/><line x1="140" y1="80" x2="140" y2="240" stroke="#0b5394" stroke-width="2"/><ellipse cx="70" cy="80" rx="70" ry="24" fill="none" stroke="#0b5394" stroke-width="2"/></g>
<line x1="150" y1="200" x2="290" y2="200" stroke="#f44336" stroke-width="2"><animate attributeName="opacity" values="0;1;0" dur="1.6s" repeatCount="indefinite"/></line>
<text x="135" y="42" class="t">h</text><text x="80" y="270" class="t">r</text>
<text x="120" y="320" class="label">V = ⅓ π r² h</text>
</svg>
</div>

**真实案例**：建筑工地沙堆近似圆锥，底面直径6米、高2米，体积 $\frac13\times\pi\times3^2\times2\approx18.8$ 立方米；卡车按20方容量派车，一车装完。漏斗形料斗装谷物，容量是同高圆柱的三分之一。


### 11. 路程公式 $s=vt$

**原理**：匀速运动时，路程等于速度与时间相乘。

**故事**：古代驿站传递公文、信使赶路，需要预估抵达时间。官吏依靠路程、行进速度互相推算，规划信使换马、休息节点，这套逻辑就是 $s=vt$ 最早的实际应用。

**▶ 动态图解**：速度×时间=路程，动点匀速移动

<div align="center">
<svg width="460" height="240" viewBox="-40 0 500 240" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:Arial,sans-serif}.t{font-size:15px;fill:#1a1a1a}.label{font-size:16px;fill:#0b5394;font-weight:bold}</style></defs>
<line x1="40" y1="120" x2="420" y2="120" stroke="#999" stroke-width="2"/>
<circle r="8" fill="#e06666">
<animateMotion dur="4s" repeatCount="indefinite" path="M60,120 L380,120"/>
</circle>
<text x="40" y="100" class="t">起点</text>
<text x="380" y="100" class="t">终点</text>
<text x="160" y="160" class="label">s = v × t</text>
<text x="140" y="195" class="t">匀速运动：速度恒定，路程随时间线性增加</text>
</svg>
</div>

**真实案例**：两地相距360公里，高速限速120km/h，理论上3小时到达；实际含服务区休息约需3.5小时。跑步配速6分钟/公里，跑10公里需60分钟——配速就是速度的倒数形式。


### 12. 总价公式 总价=单价×数量

**原理**：多个相同物品价格累加，用乘法简化求和。

**故事**：春秋至秦汉的集市交易、账本记账，早已使用这套逻辑。买卖粮食、布匹、器物时，相同货品统一计价，乘法是古代商贸最基础的计算方式。

**▶ 动态图解**：单价×数量=总价，累加动画

<div align="center">
<svg width="440" height="280" viewBox="-40 0 480 280" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:Arial,sans-serif}.t{font-size:14px;fill:#1a1a1a}.label{font-size:16px;fill:#0b5394;font-weight:bold}</style></defs>
<text x="50" y="50" class="t">单价 × 数量 = 总价</text>
<g>
<circle cx="80" cy="100" r="18" fill="#d9e8f7" stroke="#0b5394" stroke-width="1.5"><animate attributeName="fill" values="#d9e8f7;#6aa8e0;#d9e8f7" dur="2s" repeatCount="indefinite"/></circle>
<circle cx="130" cy="100" r="18" fill="#d9e8f7" stroke="#0b5394" stroke-width="1.5"><animate attributeName="fill" values="#d9e8f7;#6aa8e0;#d9e8f7" dur="2s" begin="0.3s" repeatCount="indefinite"/></circle>
<circle cx="180" cy="100" r="18" fill="#d9e8f7" stroke="#0b5394" stroke-width="1.5"><animate attributeName="fill" values="#d9e8f7;#6aa8e0;#d9e8f7" dur="2s" begin="0.6s" repeatCount="indefinite"/></circle>
<circle cx="230" cy="100" r="18" fill="#d9e8f7" stroke="#0b5394" stroke-width="1.5"><animate attributeName="fill" values="#d9e8f7;#6aa8e0;#d9e8f7" dur="2s" begin="0.9s" repeatCount="indefinite"/></circle>
<circle cx="280" cy="100" r="18" fill="#d9e8f7" stroke="#0b5394" stroke-width="1.5"><animate attributeName="fill" values="#d9e8f7;#6aa8e0;#d9e8f7" dur="2s" begin="1.2s" repeatCount="indefinite"/></circle>
<circle cx="330" cy="100" r="18" fill="#d9e8f7" stroke="#0b5394" stroke-width="1.5"><animate attributeName="fill" values="#d9e8f7;#6aa8e0;#d9e8f7" dur="2s" begin="1.5s" repeatCount="indefinite"/></circle>
<circle cx="380" cy="100" r="18" fill="#d9e8f7" stroke="#0b5394" stroke-width="1.5"><animate attributeName="fill" values="#d9e8f7;#6aa8e0;#d9e8f7" dur="2s" begin="1.8s" repeatCount="indefinite"/></circle>
</g>
<text x="70" y="140" class="t">1件</text>
<text x="370" y="140" class="t">7件</text>
<text x="120" y="200" class="label">总价 = 单价 × 数量</text>
<text x="100" y="240" class="t">相同物品累加，乘法简化求和</text>
</svg>
</div>

**真实案例**：超市买5斤苹果每斤8元，总价40元；网购满200减30，凑单后实际支付=单价×数量-优惠。工程预算中钢筋每吨3800元、共需50吨，材料费19万元。


### 13. 运算律

加法交换律：$a+b=b+a$；加法结合律：$(a+b)+c=a+(b+c)$；乘法分配律：$a(b+c)=ab+ac$

**原理**：加法交换、结合律说明求和顺序、分组方式不改变总和；分配律实现乘加拆分合并。

**故事**：古中国、古希腊在算术实践里一直在使用这些规律，只是没有抽象成字母表达式。直到近代代数体系成型，才整理成正式的运算定律。

**▶ 动态图解**：交换律/结合律/分配律示意

<div align="center">
<svg width="440" height="300" viewBox="0 0 440 300" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif}.t{font-size:14px;fill:#1a1a1a}.label{font-size:15px;fill:#0b5394;font-weight:bold}</style></defs>
<text x="40" y="40" class="label">加法交换律</text>
<text x="40" y="65" class="t">a + b = b + a</text>
<text x="40" y="105" class="label">加法结合律</text>
<text x="40" y="130" class="t">(a+b)+c = a+(b+c)</text>
<text x="40" y="170" class="label">乘法分配律</text>
<text x="40" y="195" class="t">a(b+c) = ab + ac</text>
<g>
<rect x="250" y="30" width="60" height="40" fill="#d9e8f7" stroke="#0b5394" stroke-width="1.5"><animate attributeName="opacity" values="1;0.6;1" dur="3s" repeatCount="indefinite"/></rect>
<rect x="320" y="30" width="60" height="40" fill="#ffd6d6" stroke="#c00" stroke-width="1.5"><animate attributeName="opacity" values="1;0.6;1" dur="3s" repeatCount="indefinite"/></rect>
<text x="265" y="55" class="t">a</text><text x="335" y="55" class="t">b</text>
<rect x="250" y="100" width="60" height="40" fill="#ffd6d6" stroke="#c00" stroke-width="1.5"/>
<rect x="320" y="100" width="60" height="40" fill="#d9e8f7" stroke="#0b5394" stroke-width="1.5"/>
<text x="265" y="125" class="t">b</text><text x="335" y="125" class="t">a</text>
<text x="260" y="85" class="t">交换位置，和不变</text>
</g>
</svg>
</div>

**真实案例**：购物时3件上衣各120元、5条裤子各80元，用乘法分配律：$120\times3+80\times5=360+400=760$ 元；凑单时先算整百再补零，就是加法交换律和结合律。简便计算 $25\times16=25\times4\times4=400$，心算即出。


---

## 二、初中阶段

### 1. 勾股定理 $a^2+b^2=c^2$（直角三角形）

**原理**：直角三角形两条直角边的平方之和，等于斜边的平方，可以用面积割补法证明。

**故事**：《周髀算经》记载，西周商高与周公对话，提出"勾三、股四、弦五"，国内也称商高定理，三国赵爽绘制弦图给出严谨证明。西方相传毕达哥拉斯发现定理后大喜，宰杀百牛献祭诸神，因此又叫百牛定理。东西方相隔万里，各自独立发现这个奇妙规律。

**▶ 动态图解**：两小正方形合并为大正方形


<div align="center">

<svg width="480" height="380" viewBox="0 0 480 380" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 勾股定理 a²+b²=c²：三个正方形面积关系 -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:18px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <!-- 直角三角形 ABC：直角在C，C(150,220) A(150,60) B(310,220) -->
  <polygon points="150,220 150,60 310,220" fill="#eef4fb" stroke="#1a1a1a" stroke-width="2"/>
  <!-- 直角标记 -->
  <path d="M150,200 L170,200 L170,220" fill="none" stroke="#1a1a1a" stroke-width="1.5"/>

  <!-- 以直角边a(竖直)为边的正方形，置于左侧 -->
  <rect x="80" y="60" width="70" height="160" fill="#c9e3f8" stroke="#0b5394" stroke-width="2"/>
  <text x="96" y="250" class="t">a²</text>

  <!-- 以直角边b(水平)为边的正方形，置于下方 -->
  <rect x="150" y="220" width="160" height="70" fill="#b3d7f5" stroke="#0b5394" stroke-width="2"/>
  <text x="240" y="272" class="t">b²</text>

  <!-- 斜边c上的正方形（旋转45°），初始较小/隐藏，放大到 c² -->
  <g>
    <g transform="translate(230,140)">
      <rect x="-80" y="-80" width="160" height="160" fill="#ffd9d9" stroke="#c0392b" stroke-width="2" opacity="0">
        <animate attributeName="opacity" values="0;0;0.95;0.95;0.2;0.95" keyTimes="0;0.35;0.5;0.72;0.8;1" dur="6s" repeatCount="indefinite"/>
      </rect>
    </g>
  </g>
  <text x="118" y="170" class="t" fill="#c0392b" opacity="0">
    <animate attributeName="opacity" values="0;0;1;1;0;1" keyTimes="0;0.45;0.55;0.72;0.8;1" dur="6s" repeatCount="indefinite"/>
  c²</text>

  <!-- 高亮两个小正方形 -->
  <g>
    <rect x="80" y="60" width="70" height="160" fill="none" stroke="#f39c12" stroke-width="3" opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.05;0.2;0.32;0.4;1" dur="6s" repeatCount="indefinite"/>
    </rect>
    <rect x="150" y="220" width="160" height="70" fill="none" stroke="#f39c12" stroke-width="3" opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.05;0.2;0.32;0.4;1" dur="6s" repeatCount="indefinite"/>
    </rect>
  </g>

  <g>
    <text x="40" y="320" class="label" opacity="0">
      两个小正方形面积之和 = 大正方形面积
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.35;0.48;0.82;0.9;1" dur="6s" repeatCount="indefinite"/>
    </text>
    <text x="40" y="350" class="label" opacity="0">
      a² + b² = c²
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.5;0.6;0.82;0.9;1" dur="6s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：一架5米长梯子斜靠墙，梯脚距墙3米，梯顶高度 $\sqrt{5^2-3^2}=4$ 米——电工按此判断能否够到4米高的电线。55寸电视屏幕对角线55英寸，长约123cm、宽约72cm，$123^2+72^2\approx15129+5184=20313\approx142.5^2$，与对角线吻合。



### 2. 平方差公式 $(a+b)(a-b)=a^2-b^2$

**原理**：多项式展开后中间一次项抵消；几何上理解为大正方形挖去小正方形的剩余面积。

**故事**：古巴比伦泥板、古印度算书中都记录了这类速算技巧。9世纪阿拉伯数学家花拉子米撰写《代数学》，系统整理这类代数恒等变换，奠定后世代数学计算的基础。


**▶ 动态图解**：L形割补，拼成矩形 (a+b)(a-b)
<div align="center">
<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif}.label{font-size:17px;fill:#0b5394;font-weight:bold}.t{font-size:15px;fill:#1a1a1a}</style></defs>
<rect x="60" y="60" width="180" height="180" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"/><rect x="140" y="140" width="100" height="100" fill="#ffffff" stroke="#c00" stroke-width="2"/>
<g><polygon points="60,60 240,60 240,140 140,140 140,240 60,240" fill="#b8ddff" stroke="#0b5394"><animateTransform attributeName="transform" type="translate" values="0,0; 220,20; 0,0" dur="5s" repeatCount="indefinite"/></polygon></g>
<text x="150" y="45" class="t">a</text><text x="248" y="190" class="t">b</text>
<text x="120" y="300" class="label">a² - b² = (a+b)(a-b)</text>
</svg>
</div>

**真实案例**：速算 $102\times98=(100+2)(100-2)=10000-4=9996$，心算两秒出。正方形地边长a，一角切去边长b的小正方形，剩余面积 $a^2-b^2=(a+b)(a-b)$，农民按此算实际耕种面积。


### 3. 完全平方公式

$(a+b)^2=a^2+2ab+b^2$，$(a-b)^2=a^2-2ab+b^2$

**原理**：多项式相乘展开；几何上可以用边长为 $a+b$ 的正方形分割为四块，面积相加验证。

**故事**：古代算家常依靠完全平方变形进行开平方、估算大数平方根。在没有计算器的年代，这是非常重要的笔算工具。

**▶ 动态图解**：大正方形分四块求和


<div align="center">

<svg width="480" height="380" viewBox="0 0 480 380" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 完全平方公式 (a+b)²=a²+2ab+b² ： 大正方形分四块 -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <!-- 大正方形边长 a+b = 200+100=300，分四块 -->
  <!-- a²(蓝) -->
  <rect x="70" y="60" width="200" height="200" fill="#8fc1ee" stroke="#0b5394" stroke-width="2"/>
  <!-- ab(橙，右) -->
  <rect x="270" y="60" width="100" height="200" fill="#f2c14e" stroke="#e67e22" stroke-width="2"/>
  <!-- ab(橙，下) -->
  <rect x="70" y="260" width="200" height="100" fill="#f2c14e" stroke="#e67e22" stroke-width="2"/>
  <!-- b²(绿，右下) -->
  <rect x="270" y="260" width="100" height="100" fill="#a9d18e" stroke="#6aa84f" stroke-width="2"/>

  <!-- 标注 -->
  <text x="150" y="155" class="t">a²</text>
  <text x="300" y="150" class="t">ab</text>
  <text x="145" y="330" class="t">ab</text>
  <text x="310" y="330" class="t">b²</text>

  <line x1="70" y1="60" x2="270" y2="60" stroke="#fff" stroke-width="1"/>
  <text x="120" y="50" class="t">a</text>
  <text x="320" y="50" class="t">b</text>

  <!-- 四块依次高亮 -->
  <g>
    <rect x="70" y="60" width="200" height="200" fill="none" stroke="#f39c12" stroke-width="4" opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.05;0.18;0.3;0.38;1" dur="6s" repeatCount="indefinite"/>
    </rect>
    <rect x="270" y="60" width="100" height="200" fill="none" stroke="#f39c12" stroke-width="4" opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.25;0.38;0.5;0.58;1" dur="6s" repeatCount="indefinite"/>
    </rect>
    <rect x="70" y="260" width="200" height="100" fill="none" stroke="#f39c12" stroke-width="4" opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.45;0.58;0.7;0.78;1" dur="6s" repeatCount="indefinite"/>
    </rect>
    <rect x="270" y="260" width="100" height="100" fill="none" stroke="#f39c12" stroke-width="4" opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.65;0.78;0.88;0.94;1" dur="6s" repeatCount="indefinite"/>
    </rect>
  </g>

  <g>
    <text x="40" y="330" class="label" opacity="0">
      四块面积相加
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.5;0.6;0.82;0.9;1" dur="6s" repeatCount="indefinite"/>
    </text>
    <text x="40" y="360" class="label" opacity="0">
      (a+b)² = a² + 2ab + b²
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.6;0.72;0.82;0.9;1" dur="6s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：边长a的正方形花圃，边长增加b米后，新面积 $(a+b)^2=a^2+2ab+b^2$——多出的部分是两条长条 $2ab$ 和一个小角 $b^2$，不是简单的 $a^2+b^2$。正方形地砖拼接缝的总长度也按此估料。



### 4. 一元二次方程求根公式

$ax^2+bx+c=0,\ x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$，判别式 $\Delta=b^2-4ac$

**原理**：通过配方法，把二次代数式配成完全平方形式，再开方求解。

**故事**：古巴比伦人已经可以解部分二次方程；9世纪花拉子米在《代数学》系统讲解配方法；16世纪欧洲数学家完善得到通用求根公式。后来韦达发现根和系数的关系，推动代数快速发展。

**▶ 动态图解**：配方法推导求根公式

<div align="center">
<svg width="460" height="280" viewBox="-40 0 500 280" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:Arial,sans-serif}.t{font-size:14px;fill:#1a1a1a}.label{font-size:15px;fill:#0b5394;font-weight:bold}</style></defs>
<text x="40" y="40" class="label">配方法步骤：</text>
<text x="40" y="70" class="t" opacity="0.5"><animate attributeName="opacity" values="0.5;1;0.5" dur="4s" repeatCount="indefinite"/>① ax²+bx+c=0</text>
<text x="40" y="100" class="t" opacity="0.5"><animate attributeName="opacity" values="0.5;1;0.5" dur="4s" begin="0.5s" repeatCount="indefinite"/>② x²+(b/a)x = -c/a</text>
<text x="40" y="130" class="t" opacity="0.5"><animate attributeName="opacity" values="0.5;1;0.5" dur="4s" begin="1s" repeatCount="indefinite"/>③ x²+(b/a)x+(b/2a)² = (b²-4ac)/4a²</text>
<text x="40" y="160" class="t" opacity="0.5"><animate attributeName="opacity" values="0.5;1;0.5" dur="4s" begin="1.5s" repeatCount="indefinite"/>④ (x+b/2a)² = (b²-4ac)/4a²</text>
<text x="40" y="200" class="label">x = (-b ± √(b²-4ac)) / 2a</text>
<text x="40" y="235" class="t">判别式 Δ = b²-4ac 决定根的个数</text>
</svg>
</div>

**真实案例**：小球从地面以20m/s竖直上抛，高度 $h=20t-5t^2$，求落地时间即解 $20t-5t^2=0$，$t=4$ 秒。商户定价x元，利润 $(x-20)(500-10x)=2000$，解得x=30或40元，对应最大利润点。


### 5. 韦达定理 $x_1+x_2=-\frac{b}{a},\ x_1x_2=\frac{c}{a}$

**原理**：由求根公式相加、相乘推导而来，反映一元二次方程根与系数的关系。

**故事**：法国数学家韦达，是最早大量使用字母代替数字研究方程的学者，被称为"代数之父"。韦达定理不需要求出根，就能直接判断两根的和与积，极大简化方程问题。

**▶ 动态图解**：根与系数的关系——两根之和、两根之积

<div align="center">
<svg width="440" height="260" viewBox="-40 0 480 260" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:Arial,sans-serif}.t{font-size:14px;fill:#1a1a1a}.label{font-size:15px;fill:#0b5394;font-weight:bold}</style></defs>
<text x="40" y="40" class="label">ax² + bx + c = 0 的两根 x₁、x₂</text>
<circle cx="100" cy="100" r="25" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"><animate attributeName="fill" values="#d9e8f7;#6aa8e0;#d9e8f7" dur="3s" repeatCount="indefinite"/></circle>
<text x="88" y="107" class="t">x₁</text>
<circle cx="200" cy="100" r="25" fill="#ffd6d6" stroke="#c00" stroke-width="2"><animate attributeName="fill" values="#ffd6d6;#e06666;#ffd6d6" dur="3s" repeatCount="indefinite"/></circle>
<text x="188" y="107" class="t">x₂</text>
<line x1="125" y1="100" x2="175" y2="100" stroke="#999" stroke-width="1.5" stroke-dasharray="4 3"/>
<text x="60" y="170" class="label">x₁ + x₂ = -b/a</text>
<text x="60" y="205" class="label">x₁ · x₂ = c/a</text>
<text x="60" y="240" class="t">不求根即可判断根的和与积</text>
</svg>
</div>

**真实案例**：已知方程两根为3和-5，不解方程直接写出方程 $x^2-(3+(-5))x+3\times(-5)=x^2+2x-15=0$。工程设计中已知两个设计点反求函数表达式，韦达定理省去求根步骤，快速验证系数。


### 6. 一次函数 $y=kx+b\ (k\neq0)$

**原理**：变量匀速变化，自变量每增加1，因变量固定增减 $k$，$k$ 是斜率，$b$ 是与 y 轴交点。

**故事**：17世纪笛卡尔创立解析几何，把代数式子和平面图形绑定，实现数形结合。传说灵感来自他卧病在床，观察天花板上苍蝇移动，想到可以用一对数字确定平面上点的位置。

**▶ 动态图解**：斜率三角形 Δy/Δx


<div align="center">

<svg width="480" height="380" viewBox="0 0 480 380" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 一次函数 y=kx+b：斜率几何意义 -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <!-- 坐标系 -->
  <g stroke="#999" stroke-width="1">
    <line x1="60" y1="40" x2="60" y2="340"/>
    <line x1="40" y1="300" x2="440" y2="300"/>
  </g>
  <text x="48" y="36" class="t">y</text>
  <text x="444" y="300" class="t">x</text>

  <!-- 直线 y = kx+b ： k=1, b=-40；经过 (60,180) (260,40) -->
  <line x1="40" y1="300" x2="360" y2="40" stroke="#0b5394" stroke-width="3"/>

  <!-- 截距点 (60,300) -->
  <circle cx="60" cy="300" r="4" fill="#e06666"/>
  <text x="64" y="312" class="t" fill="#c0392b">b(截距)</text>

  <!-- 斜率三角形：Δx 与 Δy 动画 -->
  <g>
    <!-- 水平Δx -->
    <line x1="150" y1="180" x2="270" y2="180" stroke="#6aa84f" stroke-width="3" opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.2;0.35;0.7;0.85;1" dur="5s" repeatCount="indefinite"/>
    </line>
    <!-- 竖直Δy -->
    <line x1="270" y1="180" x2="270" y2="100" stroke="#e06666" stroke-width="3" opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.3;0.45;0.7;0.85;1" dur="5s" repeatCount="indefinite"/>
    </line>
  </g>
  <text x="205" y="172" class="t" fill="#38761d" opacity="0">
    <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.22;0.36;0.7;0.85;1" dur="5s" repeatCount="indefinite"/>Δx</text>
  <text x="276" y="140" class="t" fill="#c0392b" opacity="0">
    <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.32;0.46;0.7;0.85;1" dur="5s" repeatCount="indefinite"/>Δy</text>

  <g>
    <text x="50" y="360" class="label" opacity="0">
      斜率 k = Δy / Δx （x每增加1，y增加k）
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.5;0.62;0.82;0.9;1" dur="5s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：出租车起步价10元含3公里，超出每公里2元，费用 $y=10+2(x-3)=2x+4$；行驶10公里付费24元。水费每吨4元加污水处理费2元，$y=6x$，月用水量直接乘6。



### 7. 反比例函数 $y=\frac{k}{x}\ (k\neq0)$

**原理**：$xy=k$，乘积固定，两个变量此消彼长，成反比例变化。

**故事**：开普勒研究行星运行规律时，大量研究比例、反比例关系，为天体运动规律的发现提供支撑。

**▶ 动态图解**：动点沿双曲线，xy 恒定


<div align="center">

<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 反比例函数 y=k/x ： 乘积固定 -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <g stroke="#999" stroke-width="1">
    <line x1="60" y1="30" x2="60" y2="330"/>
    <line x1="30" y1="300" x2="430" y2="300"/>
  </g>
  <text x="50" y="26" class="t">y</text>
  <text x="434" y="300" class="t">x</text>

  <!-- 双曲线 y=100/x (第一象限近似路径) -->
  <path d="M100,100 C120,84 140,72 160,64 S200,52 220,50 S260,46 300,44 S360,42 420,41" fill="none" stroke="#0b5394" stroke-width="3"/>

  <!-- 动点沿曲线移动，显示 x·y 恒定 -->
  <circle r="7" fill="#e06666">
    <animateMotion dur="5s" repeatCount="indefinite"
      path="M100,100 C120,84 140,72 160,64 S200,52 220,50 S260,46 300,44 S360,42 420,41"/>
  </circle>
  <text x="130" y="90" class="label" fill="#c0392b">
    xy = k (定值)
    <animate attributeName="opacity" values="0;1;1;0;0;1" keyTimes="0;0.1;0.85;0.9;0.95;1" dur="5s" repeatCount="indefinite"/>
  </text>

  <g>
    <text x="50" y="348" class="label" opacity="0">
      x 越大，y 越小；两者乘积恒为 k
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.4;0.55;0.85;0.93;1" dur="5s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：路程120公里，速度v与时间t成反比 $t=120/v$；开60km/h需2小时，开80km/h需1.5小时。打印机每分钟印30页，印完600页需20分钟——工作量一定时效率与时间反比。



### 8. 相似三角形 $\frac{a_1}{a_2}=\frac{b_1}{b_2}=\frac{c_1}{c_2}$，面积比=相似比的平方

**原理**：对应角相等，对应边成比例；平行线分线段成比例是相似的基础。

**故事**：公元前6世纪，泰勒斯到埃及，利用同一时刻物体高度和影子长度成正比的原理，测出金字塔高度。这个故事是相似三角形最经典的早期应用，连法老都为之惊叹。


**▶ 动态图解**：三角形等比例放大，边长同步缩放
<div align="center">
<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif}.label{font-size:17px;fill:#0b5394;font-weight:bold}.t{font-size:15px;fill:#1a1a1a}</style></defs>
<polygon points="80,240 160,80 240,240" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"/>
<g><polygon points="140,240 180,160 220,240" fill="#ffd6d6" stroke="#c00" stroke-width="2"><animateTransform attributeName="transform" type="scale" values="1,1;1.7,1.7;1,1" dur="4s" repeatCount="indefinite" additive="sum"/></polygon></g>
<text x="150" y="62" class="t">A</text><text x="66" y="262" class="t">B</text><text x="238" y="262" class="t">C</text>
<text x="110" y="315" class="label">对应角相等，边长成比例</text>
</svg>
</div>

**真实案例**：在树旁立1米竹竿，影长1.5米；同一时刻树影长18米，树高 $h/18=1/1.5$，$h=12$ 米——不用爬树就量出树高。地图比例尺1:50000，图上量得两城距8cm，实际距离4公里。


### 9. 直角三角形三角函数

$\sin A=\frac{\text{对边}}{\text{斜边}},\cos A=\frac{\text{邻边}}{\text{斜边}},\tan A=\frac{\text{对边}}{\text{邻边}}$

**原理**：同一个锐角，在直角三角形中三边比值固定，和三角形大小无关。

**故事**：古希腊天文学家喜帕恰斯，为观测天象编制人类第一张弦表，被称为三角学之父。他的成果经阿拉伯学者补充完善，明末随历法书籍传入中国。


**▶ 动态图解**：角度变化，对边/邻边/斜边比值联动
<div align="center">
<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif}.label{font-size:17px;fill:#0b5394;font-weight:bold}.t{font-size:15px;fill:#1a1a1a}</style></defs>
<line x1="80" y1="240" x2="320" y2="240" stroke="#0b5394" stroke-width="2"/><line x1="320" y1="240" x2="320" y2="100" stroke="#0b5394" stroke-width="2"/><line x1="80" y1="240" x2="320" y2="100" stroke="#c00" stroke-width="2"><animateTransform attributeName="transform" type="rotate" values="0 80 240;-30 80 240;0 80 240" dur="5s" repeatCount="indefinite"/></line>
<text x="200" y="266" class="t">邻边</text><text x="328" y="170" class="t">对边</text><text x="155" y="110" class="t">斜边</text><text x="55" y="220" class="t">θ</text>
<text x="100" y="315" class="label">sinθ=对/斜 cosθ=邻/斜</text>
</svg>
</div>

**真实案例**：测山高，在距山脚水平1000米处测得仰角25°，山高 $h=1000\times\tan25°\approx466$ 米。电梯与地面夹角30°，井道高30米，则电梯行程 $30/\sin30°=60$ 米。


### 10. 弧长 $l=\frac{n\pi R}{180}$；扇形面积 $S=\frac{n\pi R^2}{360}=\frac{1}{2}lR$

**原理**：扇形是圆的一部分，圆心角 $n°$ 占整个圆周360°的比例，截取对应的周长与面积。

**故事**：古代天文学家计算黄道、星体运行圆弧轨道，长期使用弧长、扇形面积相关计算，三角与圆弧计算本就服务于天文观测。


**▶ 动态图解**：圆心角开合，弧长、扇形同步变化
<div align="center">
<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif}.label{font-size:17px;fill:#0b5394;font-weight:bold}.t{font-size:15px;fill:#1a1a1a}</style></defs>
<circle cx="230" cy="170" r="120" fill="none" stroke="#cccccc" stroke-width="1"/>
<path d="M230,170 L350,170 A120 120 0 0 1 230,50 Z" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"><animate attributeName="d" values="M230,170 L350,170 A120 120 0 0 1 230,50 Z;M230,170 L350,170 A120 120 0 0 1 120,200 Z;M230,170 L350,170 A120 120 0 0 1 230,50 Z" dur="5s" repeatCount="indefinite"/></path>
<text x="290" y="155" class="t">R</text><text x="245" y="195" class="t">n°</text>
<text x="150" y="310" class="label">l = nπR/180, S = ½lR</text>
</svg>
</div>

**真实案例**：钟表分针长10cm，从12点走到3点转90°，针尖走过弧长 $\frac{90\pi\times10}{180}=5\pi\approx15.7$ cm。披萨9寸切8块，每块扇形面积 $\frac18\pi\times11.4^2\approx51$ 平方厘米，据此估热量。


### 11. 平均数、方差

$\bar x=\frac{x_1+x_2+\dots+x_n}{n},\quad s^2=\frac{1}{n}\sum(x_i-\bar x)^2$

**原理**：平均数反映一组数据整体平均水平；方差刻画各个数据距离平均值的波动大小。

**故事**：平均数是非常古老的统计思想，古代统计人口、粮食产量就会用到。方差是近代统计学成果，高斯在研究天文观测误差、正态分布时，系统完善误差分析这套理论。

**▶ 动态图解**：数据点围绕均值波动，方差衡量离散程度

<div align="center">
<svg width="460" height="260" viewBox="0 0 460 260" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif}.t{font-size:14px;fill:#1a1a1a}.label{font-size:15px;fill:#0b5394;font-weight:bold}</style></defs>
<line x1="40" y1="140" x2="420" y2="140" stroke="#999" stroke-width="1.5"/>
<!-- 均值线 -->
<line x1="40" y1="140" x2="420" y2="140" stroke="#c0392b" stroke-width="2" stroke-dasharray="6 4"/>
<text x="380" y="130" class="t" fill="#c0392b">均值 x̄</text>
<!-- 数据点 -->
<circle cx="80" cy="110" r="6" fill="#0b5394"><animate attributeName="cy" values="110;100;110" dur="3s" repeatCount="indefinite"/></circle>
<circle cx="140" cy="160" r="6" fill="#0b5394"><animate attributeName="cy" values="160;170;160" dur="3s" begin="0.3s" repeatCount="indefinite"/></circle>
<circle cx="200" cy="90" r="6" fill="#0b5394"><animate attributeName="cy" values="90;80;90" dur="3s" begin="0.6s" repeatCount="indefinite"/></circle>
<circle cx="260" cy="170" r="6" fill="#0b5394"><animate attributeName="cy" values="170;180;170" dur="3s" begin="0.9s" repeatCount="indefinite"/></circle>
<circle cx="320" cy="120" r="6" fill="#0b5394"><animate attributeName="cy" values="120;110;120" dur="3s" begin="1.2s" repeatCount="indefinite"/></circle>
<circle cx="380" cy="150" r="6" fill="#0b5394"><animate attributeName="cy" values="150;140;150" dur="3s" begin="1.5s" repeatCount="indefinite"/></circle>
<text x="40" y="220" class="label">s² = (1/n) Σ(xᵢ - x̄)²</text>
<text x="40" y="250" class="t">方差越大，数据越分散</text>
</svg>
</div>

**真实案例**：两班数学平均分都是82分，A班方差18（成绩集中），B班方差120（两极分化）——教学策略完全不同：A班抓拔高，B班抓补差。零件厂抽测5件产品尺寸方差越小，说明机床精度越稳定。


---

## 三、高中阶段

### 1. 基本不等式 $\frac{a+b}{2}\ge\sqrt{ab}\quad(a,b>0)$，$a=b$ 取等号

**原理**：由完全平方 $(a-b)^2\ge0$ 变形推导；几何解释：半圆内的半弦长不大于半径。

**故事**：欧几里得《几何原本》中已经蕴含这个结论，古希腊学者研究比例中项时就发现了这个不等关系。如今它是求最值最常用的工具。

**▶ 动态图解**：半圆半径≥半弦


<div align="center">

<svg width="480" height="380" viewBox="0 0 480 380" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 基本不等式 (a+b)/2 ≥ √(ab) ： 半圆中 半径 ≥ 半弦 -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <!-- 半圆，直径从 x=80 到 x=400 -->
  <path d="M80,240 A160 160 0 0 1 400,240" fill="#eef4fb" stroke="#0b5394" stroke-width="2.5"/>
  <line x1="80" y1="240" x2="400" y2="240" stroke="#0b5394" stroke-width="2.5"/>

  <!-- 直径被切点M分为 a 和 b -->
  <circle cx="240" cy="240" r="4" fill="#c0392b"/>
  <text x="150" y="262" class="t">a</text>
  <text x="300" y="262" class="t">b</text>

  <!-- 半径：圆心O(240,240) 到 弧顶(240,80) -->
  <line x1="240" y1="240" x2="240" y2="80" stroke="#e06666" stroke-width="2.5"/>
  <text x="245" y="160" class="t" fill="#c0392b">半径 (a+b)/2</text>

  <!-- 半弦：过M作垂线交弧于N，MN=√(ab)，动画高亮 -->
  <line x1="240" y1="240" x2="240" y2="120" stroke="#6aa84f" stroke-width="3" opacity="0">
    <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.4;0.55;0.85;0.92;1" dur="6s" repeatCount="indefinite"/>
  </line>
  <text x="245" y="205" class="t" fill="#38761d" opacity="0">
    <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.42;0.56;0.85;0.92;1" dur="6s" repeatCount="indefinite"/>半弦 √(ab)</text>

  <g>
    <text x="40" y="320" class="label" opacity="0">
      半径始终 ≥ 半弦（a=b 时相等）
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.45;0.58;0.85;0.92;1" dur="6s" repeatCount="indefinite"/>
    </text>
    <text x="40" y="350" class="label" opacity="0">
      (a+b)/2 ≥ √(ab)
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.6;0.72;0.85;0.92;1" dur="6s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：用36米篱笆围矩形菜地，何时面积最大？$a+b=18$，$ab\le(\frac{a+b}{2})^2=81$，即边长9米时面积最大81㎡。圆柱形罐头容积一定时，底面半径等于高的一半时用料最省，食品厂据此设计罐型。



### 2. 等差数列

通项：$a_n=a_1+(n-1)d$；求和：$S_n=\frac{n(a_1+a_n)}{2}$

**原理**：相邻两项差值恒定；求和使用倒序相加，首尾配对。

**故事**：少年高斯上学时，老师布置计算1加到100。别的学生逐项累加，高斯立刻想到首尾配对：$(1+100)+(2+99)+\dots$，快速算出结果5050。这个思路就是倒序相加法。高斯后来被誉为数学王子。

**▶ 动态图解**：首尾配对，倒序相加


<div align="center">

<svg width="480" height="380" viewBox="0 0 480 380" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 等差数列求和：高斯倒序相加 1+2+...+n -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <!-- 阶梯点阵：第一行1点，逐行递增（1到5） -->
  <g>
    <circle cx="120" cy="70"  r="6" fill="#6aa84f"/>
    <circle cx="120" cy="110" r="6" fill="#6aa84f"/><circle cx="160" cy="110" r="6" fill="#6aa84f"/>
    <circle cx="120" cy="150" r="6" fill="#6aa84f"/><circle cx="160" cy="150" r="6" fill="#6aa84f"/><circle cx="200" cy="150" r="6" fill="#6aa84f"/>
    <circle cx="120" cy="190" r="6" fill="#6aa84f"/><circle cx="160" cy="190" r="6" fill="#6aa84f"/><circle cx="200" cy="190" r="6" fill="#6aa84f"/><circle cx="240" cy="190" r="6" fill="#6aa84f"/>
    <circle cx="120" cy="230" r="6" fill="#6aa84f"/><circle cx="160" cy="230" r="6" fill="#6aa84f"/><circle cx="200" cy="230" r="6" fill="#6aa84f"/><circle cx="240" cy="230" r="6" fill="#6aa84f"/><circle cx="280" cy="230" r="6" fill="#6aa84f"/>
  </g>
  <text x="110" y="60" class="t">1 2 3 4 5</text>

  <!-- 倒序配对的点：从两端配对高亮 -->
  <g>
    <line x1="120" y1="70"  x2="280" y2="230" stroke="#f39c12" stroke-width="2.5" opacity="0">
      <animate attributeName="opacity" values="0;0;0;1;1;0;0" keyTimes="0;0.2;0.3;0.4;0.6;0.7;1" dur="5s" repeatCount="indefinite"/>
    </line>
    <line x1="120" y1="110" x2="240" y2="190" stroke="#f39c12" stroke-width="2.5" opacity="0">
      <animate attributeName="opacity" values="0;0;0;1;1;0;0" keyTimes="0;0.35;0.45;0.55;0.7;0.8;1" dur="5s" repeatCount="indefinite"/>
    </line>
    <line x1="120" y1="150" x2="200" y2="150" stroke="#f39c12" stroke-width="2.5" opacity="0">
      <animate attributeName="opacity" values="0;0;0;1;1;0;0" keyTimes="0;0.5;0.6;0.7;0.82;0.9;1" dur="5s" repeatCount="indefinite"/>
    </line>
  </g>

  <text x="330" y="150" class="t">首尾配对</text>
  <text x="330" y="175" class="t">1+5=6</text>
  <text x="330" y="195" class="t">2+4=6</text>
  <text x="330" y="215" class="t">3=3</text>

  <g>
    <text x="50" y="300" class="label" opacity="0">
      首尾相加相等 → 倒序相加求和
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.45;0.58;0.82;0.9;1" dur="5s" repeatCount="indefinite"/>
    </text>
    <text x="50" y="330" class="label" opacity="0">
      S = n(a₁ + aₙ) / 2
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.6;0.72;0.82;0.9;1" dur="5s" repeatCount="indefinite"/>
    </text>
    <text x="50" y="358" class="label" opacity="0" fill="#6aa84f">
      高斯：1+2+...+100 = 5050
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.72;0.8;0.9;0.95;1" dur="5s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：工地堆钢管，最上层5根、往下每层多1根、共20层，总数 $\frac{20\times(5+24)}{2}=290$ 根。打靶训练每日比前一日多打5发，首日30发，第30日打175发——累计总发数按等差数列求和。



### 3. 等比数列

通项：$a_n=a_1 q^{n-1}$；求和 $S_n=\begin{cases} na_1,&q=1\\ \frac{a_1(1-q^n)}{1-q},&q\neq1 \end{cases}$

**原理**：相邻两项比值恒定；求和使用错位相减法。

**故事**：古印度国际象棋传说。国王要奖励象棋发明者，大臣请求：棋盘第一格放1粒麦子，后一格麦粒数量翻倍，摆满64格。国王以为要求很低，结果总和是天文数字，全国粮食都不足以支付，这就是指数爆炸的经典案例。

**▶ 动态图解**：棋盘麦粒，指数增长


<div align="center">

<svg width="480" height="380" viewBox="0 0 480 380" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 等比数列求和：国际象棋棋盘麦粒 指数增长 -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <!-- 棋盘示意 4x4（代表64格，麦粒翻倍） -->
  <g>
    <rect x="60" y="50"  width="30" height="30" fill="#f2c14e" stroke="#555"/>
    <rect x="90" y="50"  width="30" height="30" fill="#f7f7f7" stroke="#555"/>
    <rect x="120" y="50" width="30" height="30" fill="#f2c14e" stroke="#555"/>
    <rect x="150" y="50" width="30" height="30" fill="#f7f7f7" stroke="#555"/>
    <rect x="60" y="80"  width="30" height="30" fill="#f7f7f7" stroke="#555"/>
    <rect x="90" y="80"  width="30" height="30" fill="#f2c14e" stroke="#555"/>
    <rect x="120" y="80" width="30" height="30" fill="#f7f7f7" stroke="#555"/>
    <rect x="150" y="80" width="30" height="30" fill="#f2c14e" stroke="#555"/>
    <rect x="60" y="110"  width="30" height="30" fill="#f2c14e" stroke="#555"/>
    <rect x="90" y="110"  width="30" height="30" fill="#f7f7f7" stroke="#555"/>
    <rect x="120" y="110" width="30" height="30" fill="#f2c14e" stroke="#555"/>
    <rect x="150" y="110" width="30" height="30" fill="#f7f7f7" stroke="#555"/>
    <rect x="60" y="140"  width="30" height="30" fill="#f7f7f7" stroke="#555"/>
    <rect x="90" y="140"  width="30" height="30" fill="#f2c14e" stroke="#555"/>
    <rect x="120" y="140" width="30" height="30" fill="#f7f7f7" stroke="#555"/>
    <rect x="150" y="140" width="30" height="30" fill="#f2c14e" stroke="#555"/>
  </g>
  <text x="60" y="180" class="t">第1格1粒 → 第2格2粒 → 每格翻倍</text>

  <!-- 数字增长：1,2,4,8,16,... 动画 -->
  <text x="300" y="90" class="label" opacity="0">
    <animate attributeName="opacity" values="0;0;0;1;1;1;0;1" keyTimes="0;0.15;0.3;0.35;0.5;0.7;0.8;1" dur="6s" repeatCount="indefinite"/>2⁶⁴ - 1 粒</text>
  <text x="300" y="120" class="t">≈ 1.8×10¹⁹ 粒</text>

  <g>
    <text x="40" y="300" class="label" opacity="0">
      前 n 项和（错位相减）
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.5;0.62;0.85;0.92;1" dur="6s" repeatCount="indefinite"/>
    </text>
    <text x="40" y="330" class="label" opacity="0">
      Sₙ = a₁(1 - qⁿ) / (1 - q)  (q≠1)
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.6;0.72;0.85;0.92;1" dur="6s" repeatCount="indefinite"/>
    </text>
    <text x="40" y="358" class="label" opacity="0" fill="#c0392b">
      指数增长：翻倍迅速惊人
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.72;0.8;0.9;0.95;1" dur="6s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：细胞每30分钟分裂一次（1变2），10小时（20次分裂）后数量 $2^{20}\approx105$ 万倍。存款年利率3%，复利计息，10年后本利和 $(1.03)^{10}\approx1.344$ 倍——每年利息再生利息。



### 4. 向量数量积 $\boldsymbol{a}\cdot\boldsymbol{b}=|\boldsymbol{a}||\boldsymbol{b}|\cos\theta$

**原理**：一个向量在另一个向量方向上的投影长度，乘以另一个向量的模长。

**故事**：向量起源于物理，用来描述力、位移、速度这类既有大小又有方向的量。19世纪哈密顿在桥上散步灵光一闪创立四元数，格拉斯曼建立完整向量代数体系，向量由此正式成为数学分支。


**▶ 动态图解**：两向量夹角变动，投影同步伸缩
<div align="center">
<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif}.label{font-size:17px;fill:#0b5394;font-weight:bold}.t{font-size:15px;fill:#1a1a1a}</style></defs>
<line x1="230" y1="200" x2="380" y2="200" stroke="#0b5394" stroke-width="2.5"/><line x1="230" y1="200" x2="330" y2="90" stroke="#c00" stroke-width="2.5"><animateTransform attributeName="transform" type="rotate" values="0 230 200;50 230 200;0 230 200" dur="5s" repeatCount="indefinite"/></line><line x1="230" y1="200" x2="330" y2="200" stroke="#f44336" stroke-width="2" stroke-dasharray="4 4"><animate attributeName="x2" values="330;280;330" dur="5s" repeatCount="indefinite"/></line>
<text x="300" y="220" class="t">a</text><text x="305" y="75" class="t">b</text><text x="245" y="180" class="t">θ</text>
<text x="120" y="315" class="label">a·b = |a||b|cosθ</text>
</svg>
</div>

**真实案例**：用500N的力沿30°斜角推箱子前进10米，做功 $W=|\vec F||\vec s|\cos30°=500\times10\times0.866\approx4330$ 焦耳。塔吊吊物水平移动时重力不做功（夹角90°，cos90°=0），这就是塔吊吊着重物平移不耗能的数学解释。


### 5. 正弦定理、余弦定理

$\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}=2R$

$c^2=a^2+b^2-2ab\cos C$

**原理**：余弦定理是勾股定理向任意三角形的推广；正弦定理把边角和三角形外接圆半径关联起来。

**故事**：阿拉伯天文学家阿尔·比鲁尼使用三角学测量地球半径、测算两地距离。三角学长期是天文测距、大地测绘的核心工具。


**▶ 动态图解**：三角形顶点移动，边角同步联动
<div align="center">
<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif}.label{font-size:17px;fill:#0b5394;font-weight:bold}.t{font-size:15px;fill:#1a1a1a}</style></defs>
<polygon points="80,240 230,70 380,240" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"><animate attributeName="points" values="80,240 230,70 380,240;80,240 230,130 380,240;80,240 230,70 380,240" dur="5s" repeatCount="indefinite"/></polygon>
<text x="225" y="55" class="t">A</text><text x="66" y="262" class="t">B</text><text x="382" y="262" class="t">C</text><text x="225" y="266" class="t">a</text><text x="135" y="150" class="t">c</text><text x="310" y="150" class="t">b</text>
<text x="90" y="315" class="label">a/sinA = b/sinB = c/sinC</text>
</svg>
</div>

**真实案例**：测河宽，在岸边取A、B两点相距50米，对岸目标C，测得∠A=60°、∠B=45°，由正弦定理 $AC/\sin45°=50/\sin75°$，$AC\approx36.6$ 米——不用过河就算出宽度。已知三角形两边及夹角求第三边，余弦定理直接代入。


### 6. 导数定义 $f'(x)=\lim\limits_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}$

**原理**：导数代表瞬时变化率；几何意义是函数图像上该点切线的斜率。

**故事**：17世纪，英国牛顿、德国莱布尼茨几乎独立创立微积分。牛顿为计算天体瞬时速度、行星运动；莱布尼茨侧重几何，设计沿用至今的微分符号。两人还爆发著名的微积分优先权之争。微积分彻底解决"变化量"的计算难题。

**▶ 动态图解**：割线逐渐逼近切线


<div align="center">

<svg width="480" height="360" viewBox="0 0 480 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 导数定义：割线逼近切线 -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <!-- 坐标系 -->
  <g stroke="#999" stroke-width="1">
    <line x1="50" y1="30" x2="50" y2="330"/>
    <line x1="20" y1="300" x2="450" y2="300"/>
  </g>
  <text x="44" y="26" class="t">y</text>
  <text x="452" y="300" class="t">x</text>

  <!-- 曲线 y=f(x) -->
  <path d="M90,280 C130,250 170,210 210,170 C240,140 270,120 300,110 C340,98 380,92 420,90" fill="none" stroke="#0b5394" stroke-width="3"/>

  <!-- 定点 P(210,170) -->
  <circle cx="210" cy="170" r="6" fill="#e06666"/>
  <text x="214" y="162" class="t" fill="#c0392b">P(x₀,f(x₀))</text>

  <!-- 动点 Q 沿曲线移动（从远到近接近 P），割线 PQ 随之变化，最终逼近切线 -->
  <g>
    <!-- 动点Q -->
    <circle r="5" fill="#6aa84f">
      <animate attributeName="cx" values="420;410;390;370;350;330;310;290;270;250;240;230;225;222;215;212;211;210;210" keyTimes="0;0.04;0.08;0.12;0.16;0.2;0.24;0.28;0.32;0.38;0.44;0.5;0.56;0.62;0.7;0.78;0.86;0.92;1" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="90;90;92;94;97;100;104;108;114;120;128;136;144;150;162;166;168;169;170" keyTimes="0;0.04;0.08;0.12;0.16;0.2;0.24;0.28;0.32;0.38;0.44;0.5;0.56;0.62;0.7;0.78;0.86;0.92;1" dur="6s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- 割线：从P到Q动态绘制 -->
  <line x1="210" y1="170" x2="420" y2="90" stroke="#f39c12" stroke-width="2.5" stroke-dasharray="6 4">
    <animate attributeName="x2" values="420;410;390;370;350;330;310;290;270;250;240;230;225;222;215;212;211;210" keyTimes="0;0.04;0.08;0.12;0.16;0.2;0.24;0.28;0.32;0.38;0.44;0.5;0.56;0.62;0.7;0.78;0.86;0.92;1" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="y2" values="90;90;92;94;97;100;104;108;114;120;128;136;144;150;162;166;168;169;170" keyTimes="0;0.04;0.08;0.12;0.16;0.2;0.24;0.28;0.32;0.38;0.44;0.5;0.56;0.62;0.7;0.78;0.86;0.92;1" dur="6s" repeatCount="indefinite"/>
  </line>

  <!-- 最终切线（P点处的切线），随割线逼近后显示 -->
  <line x1="130" y1="205" x2="290" y2="110" stroke="#e06666" stroke-width="3" opacity="0">
    <animate attributeName="opacity" values="0;0;0;0;0;0;0;0;0;0;0;0;0;0.9;0.9;0.9;0.9;0.9;0" keyTimes="0;0.04;0.08;0.12;0.16;0.2;0.24;0.28;0.32;0.38;0.44;0.5;0.56;0.62;0.68;0.8;0.9;0.96;1" dur="6s" repeatCount="indefinite"/>
  </line>

  <g>
    <text x="40" y="348" class="label" opacity="0">
      Δx→0 时，割线斜率 → 切线斜率
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.62;0.74;0.9;0.95;1" dur="6s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：汽车里程表在t=2小时时读数120km，t=2.1小时时132km，瞬时速度近似 $\frac{132-120}{0.1}=120$ km/h——这就是导数的现实含义：里程函数的瞬时变化率。工厂边际成本：多生产一件产品增加的成本，就是成本函数的导数，用于决定是否扩产。



### 7. 二项式定理 $(a+b)^n=\sum\limits_{k=0}^n \mathrm C_n^k a^{n-k}b^k$，$\mathrm C_n^k=\frac{n!}{k!(n-k)!}$

**原理**：多次相乘展开时，组合数统计每一项的选取方式。

**故事**：北宋贾宪绘制"开方作法本源图"，也就是我们说的杨辉三角，比欧洲早六百多年，杨辉将它录入著作流传后世。西方帕斯卡后来独立研究，西方叫帕斯卡三角。小小的三角数阵藏着组合、分形等丰富规律。


**▶ 动态图解**：杨辉三角逐层生成
<div align="center">
<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif;text-anchor:middle}.t{font-size:16px;fill:#1a1a1a}.label{font-size:17px;fill:#0b5394;font-weight:bold}</style></defs>
<text x="230" y="60" class="t">1<animate attributeName="opacity" values="0;1" begin="0s" dur="0.8s" repeatCount="indefinite"/></text>
<text x="170" y="110" class="t">1<animate attributeName="opacity" values="0;1" begin="0.8s" dur="0.8s" repeatCount="indefinite"/></text><text x="290" y="110" class="t">1<animate attributeName="opacity" values="0;1" begin="0.8s" dur="0.8s" repeatCount="indefinite"/></text>
<text x="110" y="160" class="t">1<animate attributeName="opacity" values="0;1" begin="1.6s" dur="0.8s" repeatCount="indefinite"/></text><text x="230" y="160" class="t">2<animate attributeName="opacity" values="0;1" begin="1.6s" dur="0.8s" repeatCount="indefinite"/></text><text x="350" y="160" class="t">1<animate attributeName="opacity" values="0;1" begin="1.6s" dur="0.8s" repeatCount="indefinite"/></text>
<text x="60" y="210" class="t">1<animate attributeName="opacity" values="0;1" begin="2.4s" dur="0.8s" repeatCount="indefinite"/></text><text x="150" y="210" class="t">3<animate attributeName="opacity" values="0;1" begin="2.4s" dur="0.8s" repeatCount="indefinite"/></text><text x="230" y="210" class="t">3<animate attributeName="opacity" values="0;1" begin="2.4s" dur="0.8s" repeatCount="indefinite"/></text><text x="310" y="210" class="t">1<animate attributeName="opacity" values="0;1" begin="2.4s" dur="0.8s" repeatCount="indefinite"/></text>
<text x="230" y="310" class="label">(a+b)ⁿ 系数：杨辉三角</text>
</svg>
</div>

**真实案例**：掷硬币10次，恰好出现3次正面的概率 $\mathrm C_{10}^3(\frac12)^{10}=120/1024\approx11.7\%$——二项式定理直接展开系数。多项式 $(a+b)^n$ 展开后各项系数就是杨辉三角，工程中信号展开、概率分布都依赖它。


### 8. 古典概型 $P(A)=\frac{\text{事件A包含基本事件数}}{\text{总基本事件数}}$

**原理**：所有基本事件发生的可能性均等。

**故事**：17世纪法国赌徒德·梅累向帕斯卡请教赌局中断如何公平分赌注。帕斯卡写信和费马反复讨论，以等可能计数的思路解决问题，这次通信，成为概率论诞生的起点。


**▶ 动态图解**：掷骰子，等可能结果高亮
<div align="center">
<svg width="460" height="360" viewBox="0 0 460 360" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif;text-anchor:middle}.t{font-size:15px;fill:#1a1a1a}.label{font-size:17px;fill:#0b5394;font-weight:bold}</style></defs>
<rect x="80" y="80" width="60" height="60" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"><animate attributeName="fill" values="#d9e8f7;#ffd6d6;#d9e8f7" dur="2s" begin="0s" repeatCount="indefinite"/></rect><text x="110" y="118" class="t">1</text>
<rect x="160" y="80" width="60" height="60" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"><animate attributeName="fill" values="#d9e8f7;#ffd6d6;#d9e8f7" dur="2s" begin="0.3s" repeatCount="indefinite"/></rect><text x="190" y="118" class="t">2</text>
<rect x="240" y="80" width="60" height="60" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"><animate attributeName="fill" values="#d9e8f7;#ffd6d6;#d9e8f7" dur="2s" begin="0.6s" repeatCount="indefinite"/></rect><text x="270" y="118" class="t">3</text>
<rect x="80" y="160" width="60" height="60" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"><animate attributeName="fill" values="#d9e8f7;#ffd6d6;#d9e8f7" dur="2s" begin="0.9s" repeatCount="indefinite"/></rect><text x="110" y="198" class="t">4</text>
<rect x="160" y="160" width="60" height="60" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"><animate attributeName="fill" values="#d9e8f7;#ffd6d6;#d9e8f7" dur="2s" begin="1.2s" repeatCount="indefinite"/></rect><text x="190" y="198" class="t">5</text>
<rect x="240" y="160" width="60" height="60" fill="#d9e8f7" stroke="#0b5394" stroke-width="2"><animate attributeName="fill" values="#d9e8f7;#ffd6d6;#d9e8f7" dur="2s" begin="1.5s" repeatCount="indefinite"/></rect><text x="270" y="198" class="t">6</text>
<text x="230" y="310" class="label">P(A) = 有利结果 / 全部结果</text>
</svg>
</div>

**真实案例**：掷两枚骰子，点数和为7的概率：共36种等可能结果，其中(1,6)(2,5)(3,4)(4,3)(5,2)(6,1)共6种，$P=6/36=1/6$。彩票双色球中头奖概率约1/1772万——古典概型算清"中奖有多难"。


### 9. 圆锥曲线

椭圆：$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$（到两定点距离之和为定值 $2a$）

双曲线：$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$（到两定点距离之差的绝对值为定值）

抛物线：到定点与定直线距离相等

**原理**：平面截取圆锥得到三类曲线，依靠距离定义建立方程。

**故事**：古希腊阿波罗尼奥斯写下《圆锥曲线论》，系统研究这三类曲线，被称为圆锥曲线之父。此后近两千年，圆锥曲线被当成纯理论几何，直到开普勒发现行星运行轨道是椭圆，它才用来解释宇宙天体运行。

**▶ 动态图解**：动点到两焦点距离和恒定


<div align="center">

<svg width="480" height="380" viewBox="0 0 480 380" xmlns="http://www.w3.org/2000/svg" overflow="visible">
  <!-- 椭圆定义：到两焦点距离之和为定值 2a -->
  <defs>
    <style>
      text{font-family:Arial, sans-serif}
      .t{font-size:15px;fill:#1a1a1a}
      .label{font-size:17px;fill:#0b5394;font-weight:bold}
    </style>
  </defs>

  <!-- 椭圆 a=140 b=80 中心(240,200) -->
  <ellipse cx="240" cy="200" rx="140" ry="80" fill="#eef4fb" stroke="#0b5394" stroke-width="2.5"/>

  <!-- 两焦点 F1 F2 -->
  <circle cx="160" cy="200" r="5" fill="#c0392b"/>
  <circle cx="320" cy="200" r="5" fill="#c0392b"/>
  <text x="130" y="216" class="t" fill="#c0392b">F₁</text>
  <text x="330" y="216" class="t" fill="#c0392b">F₂</text>

  <!-- 动点P沿椭圆移动，绘制到两焦点的线段 -->
  <g>
    <circle r="6" fill="#e06666">
      <animateMotion dur="6s" repeatCount="indefinite"
        path="M380,200 A140 80 0 1 0 100,200 A140 80 0 1 0 380,200"/>
    </circle>
    <!-- PF1 线段 -->
    <line x1="160" y1="200" x2="380" y2="200" stroke="#f39c12" stroke-width="2">
      <animate attributeName="x2" values="380;240;100;240;380" keyTimes="0;0.25;0.5;0.75;1" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="y2" values="200;120;200;280;200" keyTimes="0;0.25;0.5;0.75;1" dur="6s" repeatCount="indefinite"/>
    </line>
    <!-- PF2 线段 -->
    <line x1="320" y1="200" x2="380" y2="200" stroke="#6aa84f" stroke-width="2">
      <animate attributeName="x2" values="380;240;100;240;380" keyTimes="0;0.25;0.5;0.75;1" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="y2" values="200;120;200;280;200" keyTimes="0;0.25;0.5;0.75;1" dur="6s" repeatCount="indefinite"/>
    </line>
  </g>

  <g>
    <text x="40" y="330" class="label" opacity="0">
      PF₁ + PF₂ = 定值 2a
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.5;0.62;0.85;0.92;1" dur="6s" repeatCount="indefinite"/>
    </text>
    <text x="40" y="358" class="label" opacity="0" fill="#c0392b">
      椭圆 x²/a² + y²/b² = 1
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.6;0.72;0.85;0.92;1" dur="6s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

**真实案例**：地球卫星轨道是椭圆，地球在一个焦点上；近地点远地点距离由椭圆参数决定。铅球出手后轨迹是抛物线，教练按抛物线方程调整出手角度和力度，最优出手角约42°。手电筒反光罩是椭圆面，灯泡在焦点，光线反射后汇聚——全靠圆锥曲线几何性质。



### 10. 空间向量求夹角、距离

**原理**：把立体几何中的角度、距离问题，转化为向量数量积的代数计算。

**故事**：是笛卡尔解析几何思想延伸到三维空间。立体几何不再单纯依靠空间想象，可以依靠坐标计算求解，也是现代计算机三维建模、图形渲染的数学根基。

**▶ 动态图解**：三维坐标系中向量夹角与距离计算

<div align="center">
<svg width="440" height="300" viewBox="0 0 440 300" xmlns="http://www.w3.org/2000/svg" overflow="visible">
<defs><style>text{font-family:Arial,sans-serif}.t{font-size:14px;fill:#1a1a1a}.label{font-size:15px;fill:#0b5394;font-weight:bold}</style></defs>
<line x1="220" y1="220" x2="380" y2="220" stroke="#999" stroke-width="1.5"/>
<line x1="220" y1="220" x2="220" y2="60" stroke="#999" stroke-width="1.5"/>
<line x1="220" y1="220" x2="140" y2="280" stroke="#999" stroke-width="1.5"/>
<text x="385" y="225" class="t">x</text>
<text x="225" y="55" class="t">z</text>
<text x="125" y="290" class="t">y</text>
<line x1="220" y1="220" x2="330" y2="120" stroke="#c0392b" stroke-width="2.5"><animateTransform attributeName="transform" type="rotate" values="0 220 220;10 220 220;0 220 220" dur="5s" repeatCount="indefinite"/></line>
<line x1="220" y1="220" x2="290" y2="170" stroke="#0b5394" stroke-width="2.5"><animateTransform attributeName="transform" type="rotate" values="0 220 220;-8 220 220;0 220 220" dur="5s" repeatCount="indefinite"/></line>
<text x="335" y="115" class="t" fill="#c0392b">a</text>
<text x="295" y="165" class="t" fill="#0b5394">b</text>
<text x="230" y="210" class="t">θ</text>
<text x="60" y="270" class="label">cosθ = (a·b)/(|a||b|)</text>
</svg>
</div>

**真实案例**：建筑设计中求两个墙面的二面角，用空间向量法：取两面法向量，$\cos\theta=\frac{|\vec n_1\cdot\vec n_2|}{|\vec n_1||\vec n_2|}$，算出角度后据此切瓷砖。异面管道之间最短距离，用向量投影公式直接求出，施工时按此留间隙。


---

## 附录：数学故事时间线速记

| 年代 | 人物/文明 | 贡献 | 对应公式 |
|---|---|---|---|
| 公元前3000年 | 古埃及 | 丈量土地 | 长方形面积 |
| 公元前6世纪 | 泰勒斯 | 测金字塔 | 相似三角形 |
| 公元前6世纪 | 商高/毕达哥拉斯 | 勾股定理 | $a^2+b^2=c^2$ |
| 公元前3世纪 | 阿波罗尼奥斯 | 圆锥曲线 | 椭圆/双曲线/抛物线 |
| 公元前2世纪 | 喜帕恰斯 | 第一张弦表 | 三角函数 |
| 公元1世纪 | 海伦 | 三边面积公式 | 海伦公式 |
| 公元3世纪 | 刘徽 | 割圆术 | 圆面积、圆周率 |
| 公元5世纪 | 祖冲之 | 圆周率7位小数 | 圆周长 |
| 公元9世纪 | 花拉子米 | 配方法 | 二次方程 |
| 北宋 | 贾宪/杨辉 | 二项式系数三角 | 杨辉三角 |
| 16–17世纪 | 韦达/笛卡尔 | 字母代数、解析几何 | 一次函数、坐标 |
| 17世纪 | 牛顿/莱布尼茨 | 微积分 | 导数 |
| 17世纪 | 帕斯卡/费马 | 概率论开端 | 古典概型 |
| 1609年 | 开普勒 | 行星椭圆轨道 | 椭圆 |
| 19世纪 | 哈密顿/格拉斯曼 | 向量代数 | 平面/空间向量 |
| 19世纪 | 高斯 | 误差与正态分布 | 平均数、方差 |

---

## 附录：SVG 动图使用说明

- **自动循环**：所有 SVG 均为 SMIL 原生动画，打开即循环播放，无需脚本。
- **已内嵌**：本文档的 14 个动态图解均为完整 SVG 源码，自包含，无需外部文件。
- **Word 打印**：Word 对 SVG 动画支持有限，如需打印请先转为 PNG 静态图插入。
- **已有 14 个动画**：小学 5、初中 4、高中 5（见正文各条目"▶ 动态图解"）。
