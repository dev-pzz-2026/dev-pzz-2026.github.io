# -*- coding: utf-8 -*-
import json, html, os
from sishi_juqi_content import SISHI_TITLE, SISHI_INTRO, SISHI_BLOCKS
from tuina_content import TUINA_TITLE, TUINA_INTRO, TUINA_BLOCKS

data = json.load(open("甲乙书_merged_v5.json", encoding="utf-8"))
jia = [d for d in data if d["cls"] == "甲"]
yi  = [d for d in data if d["cls"] == "乙"]

def esc(s): return html.escape(str(s or ""), quote=True)

for d in jia+yi:
    d["_id"] = "x" + str(id(d))

# ---------- 后序文本 ----------
HOUXU_INTRO = ("书以八法为纲，纂甲乙之类药，所以明理法、标本末也。编末殿以后序，"
    "首篇录医圣张仲景《伤寒杂病论》原序（一名《伤寒卒病论集》，即世所习称之《伤寒论》序）。"
    "观其“勤求古训，博采众方”之旨，与本书溯源医著、辑录经方之意初无二致；"
    "读其“省疾问病，务在口给”之戒，则知四诊辨证、见病知源，自昔为医家第一义。"
    "缀诸卷末，庶几读者究药理而溯沠原，不以今之纂要自限云。次篇为著者自识，"
    "即药数以观世变，述所怀以明其志，二者相须而义始备。")

SHHL_XU_TITLE = "《伤寒杂病论》原序"
SHHL_XU_ATTR = "（一名《伤寒卒病论集》，即世所习称之《伤寒论》序。汉·张仲景 撰，据通行本）"
SHHL_XU_PARAS = [
"论曰：余每览越人入虢之诊，望齐侯之色，未尝不慨然叹其才秀也。怪当今居世之士，曾不留神医药，精究方术，上以疗君亲之疾，下以救贫贱之厄，中以保身长全，以养其生，但竞逐荣势，企踵权豪，孜孜汲汲，惟名利是务，崇饰其末，忽弃其本，华其外而悴其内，皮之不存，毛将安附焉？卒然遭邪风之气，婴非常之疾，患及祸至，而方震栗，降志屈节，钦望巫祝，告穷归天，束手受败，赍百年之寿命，持至贵之重器，委付凡医，恣其所措，咄嗟呜呼！厥身已毙，神明消灭，变为异物，幽潜重泉，徒为啼泣。痛夫！举世昏迷，莫能觉悟，不惜其命，若是轻生，彼何荣势之云哉！而进不能爱人知人，退不能爱身知己，遇灾值祸，身居厄地，蒙蒙昧昧，蠢若游魂。哀乎！趋世之士，驰竞浮华，不固根本，忘躯徇物，危若冰谷，至于是也！",
"余宗族素多，向余二百，建安纪年以来，犹未十稔，其死亡者，三分有二，伤寒十居其七。感往昔之沦丧，伤横夭之莫救，乃勤求古训，博采众方，撰用《素问》《九卷》《八十一难》《阴阳大论》《胎胪药录》，并平脉辨证，为《伤寒杂病论》，合十六卷。虽未能尽愈诸病，庶可以见病知源。若能寻余所集，思过半矣。",
"夫天布五行，以运万类；人禀五常，以有五藏；经络府俞，阴阳会通；玄冥幽微，变化难极。自非才高识妙，岂能探其理致哉！上古有神农、黄帝、歧伯、伯高、雷公、少俞、少师、仲文，中世有长桑、扁鹊，汉有公乘阳庆及仓公，下此以往，未之闻也。观今之医，不念思求经旨，以演其所知，各承家技，始终循旧。省疾问病，务在口给，相对斯须，便处汤药。按寸不及尺，握手不及足；人迎趺阳，三部不参；动数发息，不满五十。短期未知决诊，九候曾无仿佛；明堂阙庭，尽不见察，所谓窥管而已。夫欲视死别生，实为难矣！",
"孔子云：生而知之者上，学则亚之。多闻博识，知之次也。余宿尚方术，请事斯语。",
]

# 第二篇后序：编者半夏叁分 自序（农历丙午年九月十三，即公历2026-10-22）
HXU2_TITLE = "《甲乙书》后序"
HXU2_AUTHOR = "序作者　半夏叁分　｜　农历丙午年九月十三"
HXU2_PARAS = [
"书以八法为纲，纂今医保甲乙类成药二百四十七味：清法九十三，消法四十五，温法三十二，汗法二十四，和法二十二，补法二十二，下法九，吐法零。即数而观之，古今人之异可见矣。夫清、消二法居其半强，何也？古人作劳于野，伤于寒者为多，故仲景之书，辛温发表、助阳散阴之剂居其要。今也晏居楼室，寒暑有代，饮食逾节，耳目有屏牍之劳，思虑有旦暮之迫——外寒得免而内热日生，形逸而神劳，饱食而少行，故郁而化火、积而成滞、痰瘀互结之病独多。清之者，热由内生也；消之者，积由日成也。汗、下二法之所以狭者，非表证里实之遂亡也，盖能任峻攻者少，而成药必循常而设，峻烈之品例难轻入。至吐法之零，尤足深省：一法之废，非其理之非也，实以病者难堪、医慎其险、急救之具既备，遂出于方术之外。由是言之，八法之多寡，非独病之应，亦起居之应、方制之应也。虽然，目录之数出于审定与招采之宜，不必尽当临床之实，读者不以辞害意可也。《道经》曰：「人法地，地法天，天法道，道法自然。」又曰：「归根曰静，静曰复命。」今人之病，得非动之过而静之不足欤？不知六气之胜复，而务以安适为养；不察五脏之倚伏，而日以思虑伐其根——此其所以清之不尽、消之不胜也。《经》曰：「治人事天，莫若啬。」啬者非吝也，不妄耗之谓也。食饮有节，起居有常，不妄作劳，则形与神俱而尽终其天年；此《内经》之明训，即「深根固柢、长生久视之道」之所由也。是编也，非徒便检阅、备缓急，盖欲读者即药数以知世变，即世变而反求诸身，知病之来也有自，知生之养也有本，然后以之疗疾，以之视身，庶几可与言道矣。",
"仲景序《伤寒》，自伤其宗族「三分有二，伤寒十居其七」，感往昔之沦丧，伤横夭之莫救，乃勤求古训，博采众方。其论时医，则曰「不念思求经旨，以演其所知，各承家技，终始顺旧」——千载下读之，未有不太息者也。今医保之设，本以全甲乙之类、惠无告之民，使贫者得药、疾者得治，此其初心，犹仲景之志也。然有司虽列之于目，而药店计及錙铢，多不愿售；医院核其费耗，或至阙然。于是甲乙之单徒存，闾阎之求莫应。病者既无所取正，乃求助于广告，杂进成药，寒热不辨，虚实相反，轻剂变重；基层之医，有未能尽药之性、不辨八法之宜者，遇证仓皇，惟循成例。上之不能普及，下之不能辨用，中又有利害之阻焉——此非药之罪，亦非方之罪，而所以行之者未尽也。虽然，君子不以时易操，不以难废学。《道经》曰：「胜人者有力，自胜者强。」又曰：「为学日益，为道日损。」今之世，器械可以假人，方药可以广求，所患者耳不闻则以为无，手不习则以为难。故是编之纂：一欲家有其书、人习其用，不待远求，可以自检其偏、自全其生，此自立之义也；一欲业医者得一通览之便，溯源别异，由数以明理，此自学之功也；一欲举世知药所以济人而非以贾利，此自强以济世之志也。《道经》曰：「圣人不积，既以为人，己愈有；既以与人，己愈多。」夫惟不积，故能成其大。其极也，归于天下为公、各尽所能、各取所需之世，即今所谓共产主义之伟大理想者。由小康而之大同，非空言也，自近者始之谓也。是编曰《甲乙书》，取医保甲乙之类以名其书，而实欲有补于民生日用之间。后之览者，亦将有感于斯文。",
]

# ---------- Markdown (S1) ----------
md = []
md.append("# 甲乙书\n")
md.append("**国家基本药物 · 医保甲乙类 · 中成药八法方药纂要**\n")
md.append("> 编者　半夏叁分\n")
md.append("> 上卷（甲类） · 下卷（乙类）\n")
md.append("\n## 凡例\n")
md.append("一、本书据《国家基本医疗保险、生育保险和工伤保险药品目录（2025年）》与《国家基本药物目录（2026年版）》整理，收载同时列入国家基本药物（2026年版）的医保甲类、乙类中成药，并取其“限定支付范围”为空（即无使用限制）之品种。")
md.append("二、上卷（甲类）收载 %d 味，下卷（乙类）收载 %d 味，合计 %d 味，悉可归入程国彭《医学心悟》八法（汗、吐、下、和、温、清、消、补）。" % (len(jia), len(yi), len(jia)+len(yi)))
md.append("三、每味药物设“治法、来源医著、方解、主治辩症”四项，以明其理法方药。治法依程国彭《医学心悟》八法（汗、吐、下、和、温、清、消、补）归宗，并标以方剂功效分类（如解表剂、清热剂、补益剂等）；方解述其药物组成与君臣佐使配伍要旨。")
md.append("四、主治辩症先述功效与主治病证，再述适用证型、辨证要点，并参以望、闻、问、切四诊之要（舌诊、面诊、望诊、腹诊、脉诊），证候具备者补之，不明确具备者不补。")
md.append("五、来源医著标注方剂原始或代表出处（朝代、作者、书名）；现代中成药标注《中华人民共和国药典》或部颁标准。外用药于主治中注明外用、禁内服。")
md.append("六、注射液类中成药（如柴胡注射液）属限制用药，须在具备相应处方资质的医师或专科医师指导下使用并加强监测，故本书不予收载。")
md.append("七、书中内容为基于中医经典方剂学知识之纂要，临床运用须遵医嘱。")
md.append("八、书末殿以后序，首篇录张仲景《伤寒杂病论》原序（《伤寒卒病论集》），以示“勤求古训、博采众方”之旨；次篇为著者《甲乙书》后序，即药数以观世变，述所怀以明其志。\n")
md.append("九、书末附《四时起居》一篇，本《内经》《千金方》养性之训，参以《老子》之旨，以四时之序为经、养心为纬，示保身养命、“养病先养心”之法，与后序相发。\n")
md.append("十、书末附《推拿》一篇，本《内经》“导引按蹻”“按摩醪药”之训，采自我推拿简易手法，按头面、颈肩、心神、脾胃、急用诸门条列，示今人工作学习之余举手自治小疾、“小病不花钱、自我得疗愈”之法，与《四时起居》相为表里。\n")

for vol_name, vol in [("上卷·甲类", jia), ("下卷·乙类", yi)]:
    md.append("\n## %s\n" % vol_name)
    md.append("本卷收载国家基本药物（2026年版）之医保%s中成药，共 %d 味。\n" % (vol_name.split("·")[-1], len(vol)))
    for i, d in enumerate(vol, 1):
        md.append("\n### %d. %s\n" % (i, d["name"]))
        md.append("- **治法**：%s" % d["zhi_fa"])
        md.append("- **来源医著**：%s" % d["source"])
        md.append("- **方解**：%s" % d["formula"])
        md.append("- **主治辩症**：%s" % d["zhu_bian"])

md.append("\n## 按治法分类药品索引\n")
BAFA_ORDER = ["汗法","吐法","下法","和法","温法","清法","消法","补法"]
def bafa(z):
    for b in BAFA_ORDER:
        if b in z: return b
    return "其他"
def fangji(z):
    p = z.split("·",1)[1] if "·" in z else ""
    return p.split("（")[0].strip()
groups = {b: [] for b in BAFA_ORDER}
for d in data:
    groups.setdefault(bafa(d["zhi_fa"]), []).append(d)
idx_bafa = BAFA_ORDER + (["其他"] if groups.get("其他") else [])
for b in idx_bafa:
    items = groups.get(b, [])
    if not items: continue
    label = "其他（非八法类，如西药制剂）" if b == "其他" else b
    md.append("\n### %s（%d 味）\n" % (label, len(items)))
    for d in sorted(items, key=lambda x:(x["cls"], x["name"])):
        md.append("- %s（%s）〔%s〕" % (d["name"], d["cls"], fangji(d["zhi_fa"])))

md.append("\n## 四时起居\n")
md.append(SISHI_INTRO + "\n")
for _k, _t in SISHI_BLOCKS:
    if _k == "h2":
        md.append("\n### %s\n" % _t)
    else:
        md.append(_t + "\n")

md.append("\n## 推拿\n")
md.append(TUINA_INTRO + "\n")
for _k, _t in TUINA_BLOCKS:
    if _k == "h2":
        md.append("\n### %s\n" % _t)
    else:
        md.append(_t + "\n")

md.append("\n## 后序\n")
md.append(HOUXU_INTRO + "\n")
md.append("### 一、%s\n" % SHHL_XU_TITLE)
md.append("> %s\n" % SHHL_XU_ATTR)
for p in SHHL_XU_PARAS:
    md.append(p + "\n")

md.append("### 二、%s\n" % HXU2_TITLE)
md.append("> %s\n" % HXU2_AUTHOR)
for p in HXU2_PARAS:
    md.append(p + "\n")
md.append("\n> %s\n" % "半夏叁分 谨识")
md.append("> 时维丙午年九月十三日，适为世界传统医药日")

os.makedirs("output/jiayi-book/stage1", exist_ok=True)
open("output/jiayi-book/stage1/final_draft_v5.md", "w", encoding="utf-8").write("\n".join(md))
print("markdown v5 written")

# ---------- HTML (S2) ----------
CSS = """
* { box-sizing: border-box; }
body { font-family: "宋体", SimSun, serif; font-size: 16px; color: #111; line-height: 1.9; margin: 0; }
p { text-indent: 2em; margin: 5px 0; }
.cover-title { font-size: 44px; font-weight: bold; text-align: center; text-indent: 0; margin-top: 30%; letter-spacing: 8px; }
.cover-sub { font-size: 18px; text-align: center; text-indent: 0; margin-top: 18px; }
.cover-meta { font-size: 15px; text-align: center; text-indent: 0; color: #555; margin-top: 10px; }
.cover-editor { font-size: 16px; text-align: center; text-indent: 0; margin-top: 6px; }
.cover-note { font-size: 13px; text-align: left; text-indent: 2em; color: #333; width: 80%; margin: 40px auto 0; line-height: 2; }
h1 { font-size: 26px; font-weight: bold; text-align: center; text-indent: 0; border-bottom: 2px solid #333; padding-bottom: 8px; margin: 28px 0 16px; }
h2 { font-size: 19px; font-weight: bold; text-indent: 0; margin: 18px 0 6px; border-left: 5px solid #0d47a1; padding-left: 10px; }
.field-label { font-weight: bold; }
.vol-intro { text-indent: 2em; color: #333; }
.classic-attr { text-indent: 2em; color: #555; font-size: 14px; margin: 4px 0 10px; }
.classic-text p { text-indent: 2em; margin: 8px 0; text-align: justify; }
.toc-title { font-size: 24px; font-weight: bold; text-align: center; text-indent: 0; margin-bottom: 16px; }
.toc-list, .toc-list ol { list-style: none; padding-left: 1.4em; }
.toc-list > li { margin: 4px 0; font-weight: bold; }
.toc-list ol li { font-weight: normal; }
.idx-list { list-style: none; padding-left: 1.4em; }
.idx-list li { margin: 3px 0; text-indent: 0; }
@page { size: A4; margin: 2.4cm 2.2cm; @bottom-center { content: "第 " counter(page) " 页"; } }
@page cover { margin: 2.4cm 2.2cm; @bottom-center { content: none; } }
section[role="cover"] { page: cover; }
"""

def drug_block(d, idx):
    return (
        '<h2 id="d-%s">%d. %s</h2>\n'
        '<p><span class="field-label">治法：</span>%s</p>\n'
        '<p><span class="field-label">来源医著：</span>%s</p>\n'
        '<p><span class="field-label">方解：</span>%s</p>\n'
        '<p><span class="field-label">主治辩症：</span>%s</p>\n'
    ) % (d["_id"], idx, esc(d["name"]), esc(d["zhi_fa"]),
         esc(d["source"]), esc(d["formula"]), esc(d["zhu_bian"]))

def toc_items(vol):
    return "\n".join('<li><a href="#d-%s">%d. %s</a></li>' % (d["_id"], i, esc(d["name"]))
                     for i, d in enumerate(vol, 1))

BAFA_ORDER = ["汗法","吐法","下法","和法","温法","清法","消法","补法"]
def bafa(z):
    for b in BAFA_ORDER:
        if b in z: return b
    return "其他"
def fangji(z):
    p = z.split("·",1)[1] if "·" in z else ""
    return p.split("（")[0].strip()

parts = []
parts.append('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>甲乙书</title><style>%s</style></head><body>' % CSS)

# cover
parts.append('<section role="cover">')
parts.append('<p class="cover-title">甲乙书</p>')
parts.append('<p class="cover-sub">国家基本药物 · 医保甲乙类 · 中成药八法方药纂要</p>')
parts.append('<p class="cover-meta">上卷（甲类） · 下卷（乙类）</p>')
parts.append('<p class="cover-editor">编者　半夏叁分</p>')
parts.append('<p class="cover-note">本书据《国家基本医疗保险、生育保险和工伤保险药品目录（2025年）》与《国家基本药物目录（2026年版）》整理，收载同时列入国家基本药物（2026年版）之医保甲、乙类中成药（限定支付范围为空，即无使用限制者），分上卷（甲类）、下卷（乙类）二帙。每味药物设治法、来源医著、方解、主治辩症四项，以明其理法方药。治法依程国彭《医学心悟》八法（汗、吐、下、和、温、清、消、补）归宗，并标以方剂功效分类（如解表剂、清热剂、补益剂等）；主治辩症参以舌诊、面诊、望诊、腹诊、脉诊四诊之要，证候具备者补之；外用药于主治中注明外用、禁内服；注射液类属限制用药，不予收载；书末殿以后序，首篇录张仲景《伤寒杂病论》原序，次篇为著者《甲乙书》后序，又附《四时起居》一篇，本《内经》《千金》之训、参以《老子》之旨，示保身养命、养病先养心之法，更附《推拿》一篇，本《内经》“导引按蹻”之训，示今人工作学习之余举手自治小疾、小病不花钱自我疗愈之法。书中内容为基于中医经典方剂学知识之纂要，临床运用须遵医嘱。</p>')
parts.append('</section>')

# toc
parts.append('<section role="cover"><nav class="doc-toc" aria-label="文档目录"><p class="toc-title">目录</p><ol class="toc-list">')
parts.append('<li><a href="#fanli">凡例</a></li>')
parts.append('<li><a href="#jia">上卷 · 甲类（%d 味）</a><ol>' % len(jia))
parts.append(toc_items(jia))
parts.append('</ol></li>')
parts.append('<li><a href="#yi">下卷 · 乙类（%d 味）</a><ol>' % len(yi))
parts.append(toc_items(yi))
parts.append('</ol></li>')
parts.append('<li><a href="#index">按治法分类药品索引</a></li>')
parts.append('<li><a href="#sishi">四时起居</a></li>')
parts.append('<li><a href="#tuina">推拿</a></li>')
parts.append('<li><a href="#houxu">后序</a><ol><li><a href="#houxu-1">一、《伤寒杂病论》原序</a></li><li><a href="#houxu-2">二、《甲乙书》后序</a></li></ol></li>')
parts.append('</ol></nav></section>')

# body
parts.append('<section class="chapter" data-page-restart="1">')

# 凡例
parts.append('<h1 id="fanli">凡例</h1>')
parts.append('<p>一、本书据《国家基本医疗保险、生育保险和工伤保险药品目录（2025年）》与《国家基本药物目录（2026年版）》整理，收载同时列入国家基本药物（2026年版）的医保甲类、乙类中成药，并取其“限定支付范围”为空（即无使用限制）之品种。</p>')
parts.append('<p>二、上卷（甲类）收载 %d 味，下卷（乙类）收载 %d 味，合计 %d 味，悉可归入程国彭《医学心悟》八法（汗、吐、下、和、温、清、消、补）。</p>' % (len(jia), len(yi), len(jia)+len(yi)))
parts.append('<p>三、每味药物设“治法、来源医著、方解、主治辩症”四项，以明其理法方药。治法依程国彭《医学心悟》八法（汗、吐、下、和、温、清、消、补）归宗，并标以方剂功效分类（如解表剂、清热剂、补益剂等）；方解述其药物组成与君臣佐使配伍要旨。</p>')
parts.append('<p>四、主治辩症先述功效与主治病证，再述适用证型、辨证要点，并参以望、闻、问、切四诊之要（舌诊、面诊、望诊、腹诊、脉诊），证候具备者补之，不明确具备者不补。</p>')
parts.append('<p>五、来源医著标注方剂原始或代表出处（朝代、作者、书名）；现代中成药标注《中华人民共和国药典》或部颁标准。外用药于主治中注明外用、禁内服。</p>')
parts.append('<p>六、注射液类中成药（如柴胡注射液）属限制用药，须在具备相应处方资质的医师或专科医师指导下使用并加强监测，故本书不予收载。</p>')
parts.append('<p>七、书中内容为基于中医经典方剂学知识之纂要，临床运用须遵医嘱。</p>')
parts.append('<p>八、书末殿以后序，首篇录张仲景《伤寒杂病论》原序（《伤寒卒病论集》），以示“勤求古训、博采众方”之旨；次篇为著者《甲乙书》后序，即药数以观世变，述所怀以明其志。</p>')
parts.append('<p>九、书末附《四时起居》一篇，本《内经》《千金方》养性之训，参以《老子》之旨，以四时之序为经、养心为纬，示保身养命、“养病先养心”之法，与后序相发。</p>')
parts.append('<p>十、书末附《推拿》一篇，本《内经》“导引按蹻”“按摩醪药”之训，采自我推拿简易手法，按头面、颈肩、心神、脾胃、急用诸门条列，示今人工作学习之余举手自治小疾、“小病不花钱、自我得疗愈”之法，与《四时起居》相为表里。</p>')

# 上卷
parts.append('<h1 id="jia">上卷 · 甲类</h1>')
parts.append('<p class="vol-intro">本卷收载国家基本药物（2026年版）之医保甲类中成药，共 %d 味。</p>' % len(jia))
for i, d in enumerate(jia, 1):
    parts.append(drug_block(d, i))

# 下卷
parts.append('<h1 id="yi">下卷 · 乙类</h1>')
parts.append('<p class="vol-intro">本卷收载国家基本药物（2026年版）之医保乙类中成药，共 %d 味。</p>' % len(yi))
for i, d in enumerate(yi, 1):
    parts.append(drug_block(d, i))

# 索引
parts.append('<h1 id="index">按治法分类药品索引</h1>')
parts.append('<p class="vol-intro">本书诸药依程国彭《医学心悟》八法（汗、吐、下、和、温、清、消、补）归宗，并标以方剂功效分类，汇集如左。括号内示甲、乙类，方括号示方剂功效分类。</p>')
groups = {b: [] for b in BAFA_ORDER}
for d in data:
    groups.setdefault(bafa(d["zhi_fa"]), []).append(d)
idx_bafa = BAFA_ORDER + (["其他"] if groups.get("其他") else [])
for b in idx_bafa:
    items = groups.get(b, [])
    if not items: continue
    label = "其他（非八法类，如西药制剂）" if b == "其他" else b
    parts.append('<h2>%s（%d 味）</h2>' % (esc(label), len(items)))
    parts.append('<ul class="idx-list">')
    for d in sorted(items, key=lambda x:(x["cls"], x["name"])):
        parts.append('<li>%s（%s）〔%s〕</li>' % (esc(d["name"]), esc(d["cls"]), esc(fangji(d["zhi_fa"]))))
    parts.append('</ul>')

# 四时起居（附编）
parts.append('<h1 id="sishi">%s</h1>' % esc(SISHI_TITLE))
parts.append('<p>%s</p>' % esc(SISHI_INTRO))
for _k, _t in SISHI_BLOCKS:
    if _k == "h2":
        parts.append('<h2>%s</h2>' % esc(_t))
    else:
        parts.append('<p>%s</p>' % esc(_t))

# 推拿（附编）
parts.append('<h1 id="tuina">%s</h1>' % esc(TUINA_TITLE))
parts.append('<p>%s</p>' % esc(TUINA_INTRO))
for _k, _t in TUINA_BLOCKS:
    if _k == "h2":
        parts.append('<h2>%s</h2>' % esc(_t))
    else:
        parts.append('<p>%s</p>' % esc(_t))

# 后序
parts.append('<h1 id="houxu">后序</h1>')
parts.append('<p class="vol-intro">%s</p>' % esc(HOUXU_INTRO))
parts.append('<h2 id="houxu-1">一、%s</h2>' % esc(SHHL_XU_TITLE))
parts.append('<p class="classic-attr">%s</p>' % esc(SHHL_XU_ATTR))
parts.append('<div class="classic-text">')
for p in SHHL_XU_PARAS:
    parts.append('<p>%s</p>' % esc(p))
parts.append('</div>')

parts.append('<h2 id="houxu-2">二、%s</h2>' % esc(HXU2_TITLE))
parts.append('<p class="classic-attr">%s</p>' % esc(HXU2_AUTHOR))
parts.append('<div class="classic-text">')
for p in HXU2_PARAS:
    parts.append('<p>%s</p>' % esc(p))
parts.append('</div>')
parts.append('<p class="classic-attr" style="text-align:right;text-indent:0">半夏叁分 谨识　时维丙午年九月十三日，适为世界传统医药日</p>')

parts.append('</section></body></html>')

os.makedirs("output/jiayi-book/stage2", exist_ok=True)
html_text = "".join(parts)
open("output/jiayi-book/stage2/formatted-甲乙书.html", "w", encoding="utf-8").write(html_text)
print("HTML v5 written, bytes:", len(html_text.encode("utf-8")))
