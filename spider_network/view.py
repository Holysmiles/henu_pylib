from math import pi

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 配置字体
plt.rcParams["font.family"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False


df = pd.read_csv('data.csv')
# 数据清洗
# 去除链接为空的行
df = df[df['链接'].notna()]
#  删除链接重复的行，保留一个
# df = df.drop_duplicates(subset='链接', keep='first')

#  按作者分组统计
author_counts = df['作者'].value_counts()

# # 创建画布
plt.figure(figsize=(15, 5))

# 可视化：柱状图
plt.subplot(221)
author_counts.plot(kind='bar', color='skyblue')
plt.title('作者作品数量')
plt.xlabel('作者')
plt.ylabel('作品数量')
plt.xticks(rotation=90)

# 可视化：饼图
plt.subplot(222)
author_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('作者作品占比')
plt.ylabel('')  # 去掉 y 轴标签

# 可视化：词云
plt.subplot(223)
wordcloud = WordCloud(
    font_path='C:/Windows/Fonts/simkai.ttf',  # 中文字体路径
    background_color='white',
    width=800,
    height=600
).generate_from_frequencies(author_counts.to_dict())

# 这段代码的功能是使用 matplotlib 库中的 imshow 函数显示一个词云图像。具体来说：
# plt.imshow(wordcloud, interpolation='bilinear')：将 wordcloud 对象作为图像显示，并使用双线性插值方法来平滑图像
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('作者词云')


# 准备雷达图数据
authors = author_counts.index[:6]  # 取前6位作者（如需要调整数量可以修改这里）
values = author_counts.values[:6]
num_vars = len(authors)

# 将数据封闭成一个闭合环
values = list(values) + [values[0]]

# 创建角度数组
angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
angles += angles[:1]

# 绘制雷达图
ax = plt.subplot(224, polar=True)
ax.fill(angles, values, color='skyblue', alpha=0.4)
ax.plot(angles, values, color='blue', linewidth=2)

# 添加标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(authors)

# 添加标题
plt.title('作者数据雷达图', size=15, y=1.1)

# 调整布局并显示
plt.tight_layout()
plt.show()
