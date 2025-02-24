import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('animal.csv')
plt.rcParams["font.family"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
print(data)
print('----------------------------------sort-----------------------------')
# 1）	请按照动物的速度从高到低进行排序，并输出这组动物的最高速度，最低速度和平均速度，平均速度保留两位小数。
speed_sorted = data['speed'].sort_values(ascending=False)
print(speed_sorted)
print(f'最高速度：{speed_sorted.max()}')
print(f'最低速度：{speed_sorted.min()}')
print(f'平均速度：{round(speed_sorted.mean(), 2)}')

# 2）	统计计算出所有动物中大于平均速度的数量。
speed_gt_avg = data[data['speed'] > speed_sorted.mean()].shape[0]
print(f'大于平均速度的数量：{speed_gt_avg}')

# 3）可视化展示数据，让用户能够直观的看出动物奔跑速度间的差异
print('----------------------------------可视化-----------------------------')
data.plot(x='name', y='speed', kind='line')
# data.plot( kind='line')
plt.title('动物速度')
plt.xlabel('动物名称')
plt.ylabel('速度')
x_position = range(len(data))
for x, y in zip(x_position, data['speed']):
    plt.text(x, y+0.1, str((y + 1000)), va='bottom', ha='center')

plt.show()