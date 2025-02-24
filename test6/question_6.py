import random

random_list = [random.randint(1, 100) for _ in range(20)]
print("生成的随机数为：")
print(random_list)

even_index = random_list[::2]
even_index.sort(reverse=True)
print("偶数下标的数字有：")
print(even_index)
random_list[::2] = even_index
print("偶数下标降序排列后的结果是：")
print(random_list)

