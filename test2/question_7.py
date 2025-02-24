import math


def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root * root == n


def find_number():
    # 从较小的数开始遍历
    for number in range(100):
        if is_perfect_square(number + 100) and is_perfect_square(number + 100 + 168):
            return number
    return None


result = find_number()
print(f"满足条件的整数是: {result}")