---
layout: post
title: 逻辑分析
categories: [工]
mathjax: true
date: 2026-10-23 14:00
---

逻辑分析：以形式逻辑与批判性思维为核心，涵盖翻译推理、真假推理、分析推理、加强削弱、图形与类比推理等方法。每个方法配动态图解与真实案例，突出"怎么想、怎么破"。

---


## 一、数学教材中的逻辑
### 充分条件与必要条件

**故事**：孟子说"得道多助，失道寡助"。"得道"是"多助"的充分条件（有道者必多助），"多助"是"得道"的必要条件（不多助必无道）。古人讲"修身齐家治国平天下"，修身是齐家的必要条件（不修身不能齐家），但不是充分条件（修身了不一定能齐家）——逻辑关系藏在古语里。

**原理**：
- $p \Rightarrow q$：p是q的**充分条件**（有p必有q），q是p的**必要条件**（无q必无p）
- $p \Leftrightarrow q$：p是q的**充要条件**（等价关系）
- 判断口诀："充分条件"有之必然，"必要条件"无之必不然

<div align="center">
<svg width="380" height="180" viewBox="-40 0 420 180" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<rect x="30" y="30" width="120" height="50" rx="6" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2"/>
<text x="60" y="60" class="t">p：x>3</text>
<line x1="150" y1="55" x2="230" y2="55" stroke="#2b7bba" stroke-width="2" stroke-dasharray="80"><animate attributeName="stroke-dashoffset" from="80" to="0" dur="1s" fill="freeze"/></line>
<polygon points="230,50 240,55 230,60" fill="#2b7bba"/>
<rect x="250" y="30" width="120" height="50" rx="6" fill="#fff3e0" stroke="#f26522" stroke-width="2"/>
<text x="275" y="60" class="t">q：x>1</text>
<text x="40" y="115" class="lbl">p ⇒ q（x>3 必有 x>1）</text>
<text x="40" y="140" class="lbl">p是q的充分条件；q是p的必要条件</text>
<text x="40" y="165" class="lbl">反例：x>1 推不出 x>3（不充分）</text>
</svg>
</div>

**应用方向**：高中数学必修第一册常用逻辑用语；函数、数列、几何中判断条件关系。

**真实案例**：
> "两直线平行"是"同位角相等"的什么条件？
>
> 分析：两直线平行 ⇒ 同位角相等；同位角相等 ⇒ 两直线平行。互为充要条件。
>
> "x²=1"是"x=1"的什么条件？x=1 ⇒ x²=1；但x²=1 推不出 x=1（x=-1也可以）。所以x²=1是x=1的必要不充分条件。

---

### 四种命题

**故事**：柏拉图说"吾爱吾师，吾更爱真理"。原命题：老师说的话如果对，我们就听。逆否命题：我们不听的话，说明老师说错了。逆命题：我们听老师的话（不代表老师说得对）。四种命题的转换，就是区分"听话"和"认同"——古人尊师但不盲从，正是这个逻辑。

**原理**：
- **原命题**：若p则q
- **逆命题**：若q则p
- **否命题**：若¬p则¬q
- **逆否命题**：若¬q则¬p
- 原命题与逆否命题**等价**（同真同假）；逆命题与否命题等价

<div align="center">
<svg width="380" height="200" viewBox="-40 0 420 200" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#c00}</style></defs>
<rect x="30" y="20" width="140" height="45" rx="6" fill="#e8f3fc" stroke="#2b7bba"/>
<text x="50" y="47" class="t">原命题：若p则q</text>
<rect x="220" y="20" width="140" height="45" rx="6" fill="#ffe0e0" stroke="#c00"/>
<text x="240" y="47" class="t">逆否命题：若¬q则¬p</text>
<line x1="170" y1="42" x2="220" y2="42" stroke="#c00" stroke-width="2"/>
<text x="180" y="35" class="lbl">等价</text>
<rect x="30" y="110" width="140" height="45" rx="6" fill="#f5f5f5" stroke="#999"/>
<text x="50" y="137" class="t">逆命题：若q则p</text>
<rect x="220" y="110" width="140" height="45" rx="6" fill="#f5f5f5" stroke="#999"/>
<text x="240" y="137" class="t">否命题：若¬p则¬q</text>
<line x1="170" y1="132" x2="220" y2="132" stroke="#666" stroke-width="1.5"/>
<text x="185" y="125" class="lbl" fill="#666">等价</text>
<text x="50" y="180" class="lbl">原命题与逆否命题同真同假；逆命题与否命题同真同假</text>
</svg>
</div>

**真实案例**：
> 原命题：若a=0，则ab=0。（真）
> 逆否命题：若ab≠0，则a≠0。（真，等价）
> 逆命题：若ab=0，则a=0。（假，因为b=0也可以）
> 否命题：若a≠0，则ab≠0。（假）

---

### 全称量词与存在量词

**故事**：庄子说"吾生也有涯，而知也无涯"——人的生命是有限的（存在有限的生命），但知识是无限的（存在无限的知识）。惠子与庄子辩论"子非鱼，安知鱼之乐"，就是在争：你（存在个体）能否知道所有鱼的感受（全称命题）？古人辩论中处处是量词的较量。

**原理**：
- **全称量词** ∀（所有、任意、每一个）：∀x∈M，p(x)成立
- **存在量词** ∃（存在、至少有一个）：∃x∈M，p(x)成立
- **否定规则**：
  - ¬(∀x p(x)) = ∃x ¬p(x)
  - ¬(∃x p(x)) = ∀x ¬p(x)

<div align="center">
<svg width="380" height="160" viewBox="-40 0 420 160" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="20" y="30" class="t">∀ x∈R，x²≥0 （真命题）</text>
<text x="20" y="65" class="t">∃ x∈R，x²=-1 （假命题）</text>
<line x1="20" y1="90" x2="350" y2="90" stroke="#2b7bba" stroke-width="1.5"/>
<text x="20" y="120" class="lbl">否定：¬(∀x p(x)) = ∃x ¬p(x)</text>
<text x="20" y="145" class="lbl">全称命题的否定是存在命题；存在命题的否定是全称命题</text>
</svg>
</div>

**真实案例**：
> 命题"所有三角形内角和都是180°"的否定：
>
> ¬(∀三角形，内角和=180°) = ∃三角形，内角和≠180°。
>
> 在非欧几何中确实存在这样的三角形（球面几何内角和>180°）。

---

### 或且非（逻辑运算）

**故事**：孙子兵法说"上兵伐谋，其次伐交，其次伐兵，其下攻城"。伐谋成功（p）或伐交成功（q），都算胜利（p∨q）；但必须避免攻城失败（¬r）。"或且非"就是军事决策：只要有一条路走通就赢，但不能犯致命错误。古人打仗讲"不战而屈人之兵"，就是同时满足p且q。

**原理**：
- **且** ∧（合取）：p∧q，p和q同时为真才真
- **或** ∨（析取）：p∨q，p和q至少一个为真就真
- **非** ¬（否定）：¬p，与p真假相反
- **德摩根律**：¬(p∧q) = ¬p∨¬q；¬(p∨q) = ¬p∧¬q

<div align="center">
<svg width="380" height="180" viewBox="-40 0 420 180" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="20" y="25" class="t">真值表：</text>
<text x="20" y="50" class="t">p真 q真 → p∧q真  p∨q真</text>
<text x="20" y="72" class="t">p真 q假 → p∧q假  p∨q真</text>
<text x="20" y="94" class="t">p假 q真 → p∧q假  p∨q真</text>
<text x="20" y="116" class="t">p假 q假 → p∧q假  p∨q假</text>
<line x1="20" y1="130" x2="350" y2="130" stroke="#2b7bba" stroke-width="1.5"/>
<text x="20" y="155" class="lbl">德摩根律：否定"且"变"或"，否定"或"变"且"</text>
</svg>
</div>

**真实案例**：
> 命题"这个数既是偶数又是3的倍数"（p∧q）。
> 否定："这个数不是偶数，或者不是3的倍数"（¬p∨¬q）。
>
> 不是"这个数既不是偶数也不是3的倍数"（那是¬p∧¬q，错误）。

---

### 反证法

**故事**：伽利略比萨斜塔实验，证明"重物比轻物下落快"是错的。反证法：假设重物下落快，那么把轻重两物绑在一起，轻物会拖慢重物（矛盾），所以假设不成立。数学史上√2无理数的证明，也是反证法的经典——不正面证明，而是假设反面成立，推出矛盾。

**原理**：要证明命题p为真，先假设¬p为真，推出矛盾，从而¬p为假，p为真。

步骤：
1. 反设：假设结论不成立
2. 归谬：从反设出发推出矛盾
3. 结论：原命题成立

<div align="center">
<svg width="380" height="180" viewBox="-40 0 420 180" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#c00}</style></defs>
<rect x="20" y="20" width="130" height="40" rx="6" fill="#e8f3fc" stroke="#2b7bba"/>
<text x="35" y="45" class="t">①假设¬p</text>
<line x1="150" y1="40" x2="190" y2="40" stroke="#2b7bba" stroke-width="1.5"/>
<polygon points="190,35 200,40 190,45" fill="#2b7bba"/>
<rect x="210" y="20" width="130" height="40" rx="6" fill="#ffe0e0" stroke="#c00"/>
<text x="225" y="45" class="t">②推出矛盾</text>
<line x1="275" y1="60" x2="275" y2="100" stroke="#c00" stroke-width="1.5"/>
<polygon points="270,100 275,110 280,100" fill="#c00"/>
<rect x="210" y="120" width="130" height="40" rx="6" fill="#e8f5e9" stroke="#2b7bba"/>
<text x="225" y="145" class="t">③原命题p真</text>
<text x="20" y="160" class="lbl">经典案例：证明√2是无理数</text>
</svg>
</div>

**真实案例**：
> 证明√2是无理数。
>
> 反设：假设√2是有理数，则√2=p/q（p,q互质整数）。
> 归谬：p²=2q² → p²是偶数 → p是偶数 → p=2k → 4k²=2q² → q²=2k² → q也是偶数。p和q都是偶数，与互质矛盾。
> 结论：√2不是有理数，是无理数。

---


## 二、行测考试中的逻辑方法
## 1. 翻译推理（如果…那么…）

**故事**：三国演义中，曹操"挟天子以令诸侯"，汉献帝是名义上的君主但无实权。谋士判断"如果曹操赢了，汉献帝必退位"——这就是充分条件推理。反过来，汉献帝退位推不出曹操赢了（可能是其他诸侯赢了），这就是否前无结论。古人打仗前的"若…则…"判断，本质就是翻译推理。

**原理**：将自然语言条件句翻译为逻辑表达式，利用逆否等价规则推理。

- 如果 A，那么 B  →  A → B
- 逆否等价：A → B  ⟺  ¬B → ¬A
- 肯前必肯后，否后必否前；否前肯后无必然结论

<div align="center">
<svg width="380" height="180" viewBox="-40 0 420 180" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:13px;fill:#2b7bba}</style></defs>
<rect x="20" y="20" width="100" height="50" rx="6" fill="#e8f3fc" stroke="#2b7bba" stroke-width="1.5"/>
<text x="45" y="50" class="t">A → B</text>
<line x1="120" y1="45" x2="200" y2="45" stroke="#2b7bba" stroke-width="1.5" stroke-dasharray="80"><animate attributeName="stroke-dashoffset" from="80" to="0" dur="1s" fill="freeze"/></line>
<polygon points="200,40 210,45 200,50" fill="#2b7bba"/>
<rect x="220" y="20" width="100" height="50" rx="6" fill="#fff3e0" stroke="#f26522" stroke-width="1.5"/>
<text x="245" y="50" class="t">¬B → ¬A</text>
<text x="20" y="110" class="lbl">逆否等价：原命题与逆否命题同真同假</text>
<text x="20" y="140" class="lbl">否前（¬A）或肯后（B）→ 推不出必然结论</text>
</svg>
</div>

**应用方向**：
- 题干出现"如果…那么…""只有…才…""只要…就…"
- 选项要求推出必然结论
- 假言命题链式推理

**真实案例**：
> 题干：如果天下雨，地面就会湿。现在地面没有湿。
>
> 推理：雨 → 湿；逆否：¬湿 → ¬雨。地面没湿 → 天没下雨。
>
> 易错：地面湿了推不出下雨（可能洒水）；天没下雨推不出地面不湿（可能洒水）。

---

## 2. 真假推理（矛盾关系）

**故事**：《水浒传》中梁山好汉排座次，宋江说"玉麒麟卢俊义活捉史文恭者为山寨之主"。结果卢俊义捉了史文恭，宋江却让位——这就是真假推理：宋江说的话是真的（卢俊义捉了史文恭），但"为山寨之主"被宋江自己推翻。现实中找矛盾、辨真假，就像军师在宴会上分辨谁在说谎。

**原理**：找到矛盾关系的两命题，必定一真一假，其余命题真假可定。

常见矛盾关系：
- "所有都是" 与 "有的不是"
- "所有都不是" 与 "有的是"
- "A → B" 与 "A ∧ ¬B"
- "A ∧ B" 与 "¬A ∨ ¬B"

<div align="center">
<svg width="380" height="200" viewBox="-40 0 420 200" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#c00}</style></defs>
<circle cx="100" cy="60" r="35" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2"/>
<text x="75" y="65" class="t">命题A</text>
<circle cx="280" cy="60" r="35" fill="#ffe0e0" stroke="#c00" stroke-width="2"/>
<text x="255" y="65" class="t">命题B</text>
<line x1="135" y1="60" x2="245" y2="60" stroke="#c00" stroke-width="2"/>
<text x="165" y="50" class="lbl">矛盾关系</text>
<text x="155" y="85" class="lbl">一真一假</text>
<text x="60" y="140" class="lbl">找到矛盾 → 锁定唯一真话/假话位置 → 其余命题真假全出</text>
<text x="60" y="165" class="lbl">口诀：绕过矛盾看其余</text>
</svg>
</div>

**应用方向**：
- 题干给出多个陈述，告知只有一真/一假
- 选项要求判断谁说真话、事实是什么
- 多人对话类真假话题

**真实案例**：
> 甲说：所有同学都及格了。
> 乙说：有的同学没及格。
> 丙说：班长及格了。
> 已知只有一人说真话。
>
> 分析：甲和乙矛盾，必有一真一假。真话在甲乙中，丙说假话→班长没及格。班长没及格说明"有的没及格"，乙说真话，甲说假话。结论：乙真，甲乙丙三人中班长没及格。

---

## 3. 分析推理（排除法/最大信息法）

**故事**：《隋唐演义》中秦琼卖马，单雄信认出秦琼是因为他的黄骠马。军师排座位时，从"马"这个最大信息（出现次数最多）切入，推出每个人的身份。这就是分析推理：从最显眼的线索入手，顺藤摸瓜，逐一排除不可能。

**原理**：当题干给出对象与信息的匹配关系时，用排除法或从最大信息（出现次数最多的元素）入手推理。

<div align="center">
<svg width="380" height="200" viewBox="-40 0 420 200" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="20" y="25" class="lbl">步骤1：列出所有对象与属性</text>
<rect x="20" y="35" width="80" height="30" fill="#f5f5f5" stroke="#999"/>
<text x="40" y="55" class="t">甲</text>
<rect x="110" y="35" width="80" height="30" fill="#f5f5f5" stroke="#999"/>
<text x="130" y="55" class="t">乙</text>
<rect x="200" y="35" width="80" height="30" fill="#f5f5f5" stroke="#999"/>
<text x="220" y="55" class="t">丙</text>
<text x="20" y="95" class="lbl">步骤2：从最大信息（出现最多的元素）切入</text>
<circle cx="60" cy="120" r="20" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2"><animate attributeName="r" values="20;23;20" dur="2s" repeatCount="indefinite"/></circle>
<text x="45" y="125" class="t">红</text>
<text x="100" y="125" class="lbl">← 出现3次，先锁定它的位置</text>
<text x="20" y="170" class="lbl">步骤3：逐一排除不可能选项，剩余即答案</text>
</svg>
</div>

**应用方向**：
- 排列顺序题（谁在左谁在右）
- 匹配题（职业、籍贯、颜色）
- 多人多条件对应题

**真实案例**：
> 甲、乙、丙三人分别来自北京、上海、广州。已知：
> ①甲不是北京人；②乙不是上海人；③北京人不是丙。
>
> 推理：由③北京人是甲或乙；由①甲不是北京人→乙是北京人。由②乙不是上海人（已是北京人，符合）。剩甲和丙对应上海和广州；没有更多条件，看选项排除。

---

## 4. 加强削弱（论证结构）

**故事**：战国时蔺相如完璧归赵，秦昭王说"以十五城换和氏璧"。蔺相如分析：秦王说的话（论据）推不出真给城（结论），因为秦国从不兑现盟约——这就是削弱。后来蔺相如派人偷偷送璧回赵国，就是"拆桥"。而秦国想要璧（加强论据），但给城的承诺（结论）不可信。

**原理**：论证 = 论据 → 结论。削弱即拆桥，加强即搭桥。

削弱方式（力度从强到弱）：
1. 否定论点（最强）
2. 拆桥：论据推不出结论
3. 反向论据
4. 他因削弱

加强方式：
1. 搭桥（论据与结论间建立联系）
2. 补充论据
3. 排除他因

<div align="center">
<svg width="380" height="160" viewBox="-40 0 420 160" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px}</style></defs>
<rect x="20" y="50" width="90" height="50" rx="6" fill="#e8f3fc" stroke="#2b7bba"/>
<text x="40" y="80" class="t">论据</text>
<line x1="110" y1="75" x2="200" y2="75" stroke="#2b7bba" stroke-width="2" stroke-dasharray="90"><animate attributeName="stroke-dashoffset" from="90" to="0" dur="1.2s" fill="freeze"/></line>
<polygon points="200,70 210,75 200,80" fill="#2b7bba"/>
<rect x="220" y="50" width="90" height="50" rx="6" fill="#fff3e0" stroke="#f26522"/>
<text x="240" y="80" class="t">结论</text>
<text x="30" y="130" class="lbl" fill="#c00">削弱：断箭（论据→结论）  |  加强：接箭（论据→结论）</text>
</svg>
</div>

**应用方向**：
- 题干给出研究或调查，问"以下哪项最能削弱/支持"
- 因果类论证（A导致B）
- 调查统计类论证

**真实案例**：
> 研究发现：每天喝咖啡的人寿命更长。结论：喝咖啡延长寿命。
>
> 削弱：喝咖啡的人也更注重锻炼和饮食（他因削弱）；
> 加强：控制饮食运动变量后，咖啡仍与长寿相关（排除他因）；
> 最强削弱：该研究样本中喝咖啡的都是富人，富人本身寿命长（样本偏差）。

---

## 5. 图形推理

**故事**：鲁班造锯，手被野草叶划破，发现叶子边缘有很多小齿——观察图形规律，发明了锯子。古人观星象，记录北斗七星的位置变化，也是图形推理：从点线面的排列中找规律。现实中看建筑图纸、辨地图，都是图形推理的延伸。

**原理**：观察图形的数量、位置、样式、属性规律。

常见规律：
- **数量类**：点、线、角、面、素的个数
- **位置类**：平移、旋转、翻转
- **样式类**：遍历、加减同异
- **属性类**：对称、曲直、开闭

<div align="center">
<svg width="380" height="200" viewBox="-40 0 420 200" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:12px;fill:#1a1a1a}</style></defs>
<text x="20" y="25" class="t">数量规律：线条数递增</text>
<circle cx="50" cy="70" r="15" fill="none" stroke="#2b7bba" stroke-width="2"/>
<line x1="90" y1="70" x2="120" y2="70" stroke="#999" stroke-width="1"/>
<polygon points="140,55 155,80 125,80" fill="none" stroke="#2b7bba" stroke-width="2"/>
<line x1="165" y1="70" x2="195" y2="70" stroke="#999" stroke-width="1"/>
<rect x="210" y="55" width="30" height="30" fill="none" stroke="#2b7bba" stroke-width="2"/>
<text x="255" y="75" class="t">→ 下一个应是五边形</text>
<text x="20" y="130" class="t">位置规律：顺时针旋转</text>
<rect x="40" y="150" width="25" height="25" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2">
<animateTransform attributeName="transform" type="rotate" from="0 52 162" to="360 52 162" dur="4s" repeatCount="indefinite"/>
</rect>
<text x="90" y="165" class="t">图形每次旋转90°，找旋转后的位置</text>
</svg>
</div>

**应用方向**：
- 类比型（两组图找规律）
- 顺推型（一串图推下一个）
- 九宫格型（横看竖看）

**真实案例**：
> 一组图：1个圆、2条线、3个三角形、4个方块……下一个应是5条边的图形。
>
> 解题思路：先看数量（数个数），再看位置（动不动），最后看样式（叠加/求同）。三步排除法。

---

## 6. 类比推理

**故事**：《诗经》"关关雎鸠，在河之洲"——用雎鸠鸟和鸣比喻君子好逑，就是类比推理。古人论说文常用"譬如"开头，用已知事物类比未知道理。爱因斯坦说"想象力比知识更重要"，类比就是把陌生事物和熟悉事物联系起来的桥梁。

**原理**：分析两词间的逻辑关系，找出与题干关系一致的选项。

常见关系：
- **语义关系**：近义、反义、比喻象征
- **逻辑关系**：全同、包含、交叉、并列
- **对应关系**：功能、材料、因果、属性
- **语法关系**：主谓、动宾、偏正

<div align="center">
<svg width="380" height="160" viewBox="-40 0 420 160" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<circle cx="80" cy="60" r="30" fill="#e8f3fc" stroke="#2b7bba" stroke-width="2"/>
<text x="65" y="65" class="t">A词</text>
<line x1="110" y1="60" x2="190" y2="60" stroke="#2b7bba" stroke-width="1.5"/>
<polygon points="190,55 200,60 190,65" fill="#2b7bba"/>
<text x="125" y="50" class="lbl">关系类型</text>
<circle cx="230" cy="60" r="30" fill="#fff3e0" stroke="#f26522" stroke-width="2"/>
<text x="215" y="65" class="t">B词</text>
<text x="40" y="125" class="lbl">造句法：A词___B词，关系一致即答案</text>
</svg>
</div>

**应用方向**：
- 两词型（A：B）
- 三词型（A：B：C）
- 填空型（A 对于 （ ） 相当于 B 对于 （ ））

**真实案例**：
> 钢笔：书写
> A. 篮球：投掷  B. 饭碗：米饭  C. 犁：耕地  D. 鼠标：游戏
>
> 分析：钢笔用于书写（工具：功能）。C犁用于耕地，关系一致。B饭碗盛米饭（容器：内容物），D鼠标用于操作电脑而非游戏。选C。

---

## 7. 数字推理

**故事**：高斯小时候算1+2+…+100，发现首尾相加都是101，共50对，直接得5050——这就是数字推理的极致：不是硬算，而是找规律。斐波那契从兔子繁殖中发现1,1,2,3,5,8…的数列，也是数字推理：从已知项中发现递推关系。

**原理**：观察数列各项间的运算关系，找规律推下一项。

常见规律：
- **等差数列**：相邻项差相等
- **等比数列**：相邻项比相等
- **递推数列**：前两项运算得第三项（和/差/积/商）
- **幂次数列**：平方、立方附近
- **分数数列**：分子分母分别看

<div align="center">
<svg width="380" height="160" viewBox="-40 0 420 160" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:14px;fill:#1a1a1a}.lbl{font-size:12px;fill:#2b7bba}</style></defs>
<text x="20" y="30" class="t">例：2，6，12，20，30，（ ）</text>
<text x="20" y="65" class="lbl">二级差：4，6，8，10 → 下一个差12 → 30+12=42</text>
<line x1="30" y1="90" x2="350" y2="90" stroke="#2b7bba" stroke-width="1.5"/>
<circle cx="80" cy="90" r="6" fill="#2b7bba"><animate attributeName="cx" values="80;320;80" dur="3s" repeatCount="indefinite"/></circle>
<text x="20" y="130" class="lbl">思路：先看差→再看比→最后看递推</text>
</svg>
</div>

**应用方向**：
- 整数数列
- 分数数列
- 组合数列（奇偶项分开看）

**真实案例**：
> 数列：1，4，9，16，25，（ ）
>
> 分析：1²，2²，3²，4²，5² → 下一项6²=36。
>
> 进阶：2，5，10，17，26 → n²+1 规律，下一项37。

---

## 8. 定义判断（关键词法）

**故事**：韩非子在《五蠹》中定义"学者、言谈者、带剑者、患御者、商工之民"为五蠹（五种蛀虫）。他逐条圈出关键词——不事耕战、空谈、私斗、逃避兵役、逐利——然后对照各国现象判断谁属于"五蠹"。这就是定义判断：先划定义，再对号入座。

**原理**：提取定义中的关键词（主体、客体、方式、目的、条件），逐一匹配选项。

<div align="center">
<svg width="380" height="200" viewBox="-40 0 420 200" overflow="visible" xmlns="http://www.w3.org/2000/svg">
<defs><style>text{font-family:system-ui,sans-serif}.t{font-size:13px;fill:#1a1a1a}.lbl{font-size:12px;fill:#c00}</style></defs>
<rect x="20" y="20" width="340" height="60" rx="6" fill="#f5f5f5" stroke="#999"/>
<text x="35" y="45" class="t">定义：指人们在社会交往中……</text>
<text x="35" y="68" class="lbl">↑ 圈出关键词：主体、方式、目的、条件</text>
<text x="20" y="110" class="t">选项A：……</text>
<text x="20" y="130" class="t">选项B：……</text>
<text x="20" y="150" class="t">选项C：……</text>
<text x="20" y="175" class="lbl">逐一比对关键词，全匹配才是答案；任一不符即排除</text>
</svg>
</div>

**应用方向**：
- 法律类定义（行政、民事）
- 心理学类定义
- 经济学类定义
- 社会学类定义

**真实案例**：
> 定义："沉没成本"指已经付出且不可收回的成本。
>
> 选项：
> A. 买电影票后发现电影难看，但票已不能退——继续看只为"不浪费票钱"
> B. 投资股票后股价下跌，止损卖出
>
> A中电影票钱已花且不可退，继续看是受沉没成本影响，符合定义。B止损是理性决策，不是沉没成本。

---


## 速查表：逻辑方法一句话

| 方法 | 一句话 |
|---|---|
| 翻译推理 | A→B 等价于 ¬B→¬A，否前肯后无结论 |
| 真假推理 | 找矛盾关系，绕过矛盾看其余 |
| 分析推理 | 从最大信息切入，逐一排除 |
| 加强削弱 | 削弱拆桥，加强搭桥；否定论点最强 |
| 图形推理 | 数数量→看位置→比样式 |
| 类比推理 | 造句法，关系一致即答案 |
| 数字推理 | 先差→再比→最后递推 |
| 定义判断 | 圈关键词，全匹配才选 |
