import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("StudentInfo.csv")

print(df.info())
# print(df.describe())
print("-----------------------空值处理——--------------------")
df["平时成绩"] = df["平时成绩"].fillna(0)
df["期末成绩"] = df["期末成绩"].fillna(0)
print(df.info())

print("-----------------------重复值处理——--------------------")
df.drop_duplicates(subset='学号', keep='last', inplace=True)
print(df.info())

print("-----------------------异常值处理——--------------------")
abnormal_values = df[(df['期末成绩'] < 0) | (df['期末成绩'] > 100)]
if len(abnormal_values) > 0:
    print("发现异常值：")
    print(abnormal_values)
else:
    print("未发现期末成绩的异常值")
df["期末成绩"] = df["期末成绩"].apply(lambda x: 0 if x < 0 else (100 if x > 100 else x))
abnormal_values = df[(df['期末成绩'] < 0) | (df['期末成绩'] > 100)]
if len(abnormal_values) > 0:
    print("发现异常值：")
    print(abnormal_values)
else:
    print("未发现期末成绩的异常值")

print("-----------------------统计信息——--------------------")
print(df.describe())
score_mean = df["期末成绩"].mean()
score_max = df["期末成绩"].max()
score_min = df["期末成绩"].min()
score_ge_90 = df["期末成绩"] >= 90
score_ge_90 = df[score_ge_90]

print(f'期末成绩平均分：{score_mean:.2f}')
print(f'期末成绩最高分：{score_max:.2f}')
print(f'期末成绩最低分：{score_min:.2f}')
print(f'期末成绩90分以上：{score_ge_90}')

print("-----------------------绘图——--------------------")
# 定义分数区间边界
my_bins = np.array([0, 60, 70, 80, 90, 100])
# 定义区间对应的标签
my_labels = ['60分以下', '60-70分', '70-80分', '80-90分', '90-100分']
# 使用cut函数对成绩进行分组统计，得到一个新的Series，其内容是每个成绩所属的区间标签
score_kind = pd.cut(df["期末成绩"], bins=my_bins, labels=my_labels, right=False)
score_distribution = df.groupby(score_kind)["期末成绩"].count()
# print(score_kind)
print(score_distribution)
hits = score_distribution.tolist()
print(hits)

# 获取柱状图的x轴位置索引（整数索引）
x_positions = range(len(my_labels))
for x, y in zip(x_positions, hits):
    plt.text(x, y + 0.05, str(y), ha='center', va='bottom')

score_distribution.plot(kind='bar', color='skyblue')
plt.title("期末成绩分布")
plt.xlabel("分数区间")
plt.ylabel("学生人数")
plt.xticks(x_positions, my_labels, rotation=0)

plt.show()
