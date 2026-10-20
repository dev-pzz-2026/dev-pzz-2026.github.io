import base64

# 读取PNG图片
with open(r"D:\Projects\ai-projects\personal-site\assets\plum-branch.png", "rb") as f:
    img_data = base64.b64encode(f.read()).decode("utf-8")

# 生成SVG，内嵌PNG
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="420">
  <image href="data:image/png;base64,{img_data}" width="800" height="600" preserveAspectRatio="xMidYMid meet"/>
</svg>'''

with open(r"D:\Projects\ai-projects\personal-site\assets\plum-branch-converted.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("转换完成")
