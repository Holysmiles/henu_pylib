
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# # 将文件staff.csv中的数据读入，并根据所学知识，选用一种合适的存储结构存储到内存中。

staff_list = pd.read_csv('staff.csv')

# 选用合适的一种方法，清除表中的不完整数据（含有空值的数据记录均要清除）
print("------------------数据清洗--------------")
# print(staff_list)
staff_list = pd.DataFrame(staff_list, columns=['编号', '姓名', '计分'])
print(staff_list)
staff_list.dropna(axis=0, subset=['编号', '计分'], inplace=True)
print(staff_list)

# 统计计算出所有有效人员的平均计分及90分以上的人员数
print("------------------数据统计--------------")
staff_list['计分'] = staff_list['计分'].astype(int)
staff_mean = staff_list['计分'].mean()

staff_number = staff_list[staff_list['计分'] >= 90].shape[0]
print(f'平均计分：{staff_mean}')
print(f'90分以上的人数：{staff_number}')

# 选用一种合适的图表展示所有有效人员的计分值，显示姓名和计分。--采用折线图
print("------------------数据可视化--------------")
staff_list.plot(x='姓名', y='计分', kind='line')
x_position = range(len(staff_list))
# zip的输入是可迭代对象，所以需要用list()转换一下
for x, y in zip(x_position, staff_list['计分']):
    plt.text(x, y+0.05, str(round(y*1.435, 2)), ha='center', va='bottom')

plt.show()