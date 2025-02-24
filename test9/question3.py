import csv

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False


def data_generator():
    data = [
        ["编号", "姓名", "身高"],
        ["2011", "小王", "165"],
        ["2012", "赵小", "175"],
        ["2013", "小黄", "168"],
        ["2016", "", ""],
        ["", "小雨", ""],
        ["2015", "小周", "165"],
        ["2014", "小罗", "171"],
        ["2015", "小周", "165"]
    ]

    with open("classInfo.csv", "w", newline="", encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def get_data(ls):
    with open('classInfo.csv', 'r') as f:
        csv_read = csv.reader(f)
        for i in csv_read:
            ls.append(i)


def average_heights_and_number170(heights: list):
    # heights_sorted = sorted(heights)[::-1]
    # 对给定的数组进行排序，并返回排序后的索引值（而不是直接返回排序后的数组元素本身）
    heights_index = np.argsort(heights)[::-1]
    sorted_data = data[:-1][heights_index]

    # 平均身高
    height_mean = np.mean(heights)
    average_height = round(height_mean, 2)

    # 学生身高在170以上的人数
    student_number = np.sum(heights > 170)
    return average_height, student_number


def draw_bar(data):
    # 身高数据
    heights = data[:-1, 2].astype(int)
    # 统计每个身高出现的人数（使用字典来辅助统计）
    height_count_dict = {}
    for height in heights:
        if height in height_count_dict:
            height_count_dict[height] += 1
        else:
            height_count_dict[height] = 1

    # 从字典中提取横坐标（身高）和纵坐标（对应身高的人数）数据用于绘图
    heights_x = np.array(list(height_count_dict.keys()))
    counts_y = np.array(list(height_count_dict.values()))

    plt.bar(heights_x, counts_y, width=0.8, color='skyblue')

    plt.xticks(heights_x)

    plt.title('班级学生身高分布情况')
    plt.xlabel('身高')
    plt.ylabel('人数')
    plt.show()



if __name__ == "__main__":
    # data_generator()
    ls = []
    get_data(ls)
    data = np.array(ls)
    mask = (data[:, 0] != "") & (data[:, 1] != "") & (data[:, 2] != "")
    print(mask)
    data = data[mask]
    # print(data)
    data = np.unique(data, axis=0)
    print(data)
    heights = data[:-1, 2].astype(int)

    ls = average_heights_and_number170(heights)

    average_height = ls[0]
    number_than_170 = ls[1]

    print(f'平均身高: {average_height}')
    print(f'身高高于170的人数: {number_than_170}')

    draw_bar(data)











