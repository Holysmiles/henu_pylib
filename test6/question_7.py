import random


def generator_list():
    return [random.randint(1, 100) for _ in range(50)]


def delete_odd_numbers(random_list):
    for i in random_list[::-1]:
        if i % 2 != 0:
            random_list.remove(i)
    return random_list


if __name__ == "__main__":
    # 切片操作是视图操作，对切片的修改会影响到原始数据
    random_list = generator_list()
    print("原始列表:", random_list)

    cleaned_list = delete_odd_numbers(random_list)
    print("删除列表:", cleaned_list)
