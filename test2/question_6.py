import math


def is_sushu(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


def is_huiwen(num):
    str1 = str(num)
    return str1 == str1[::-1]


def tell(start, end):
    arr = []
    for num in range(start, end + 1):
        if is_sushu(num) and is_huiwen(num):
            arr.append(num)
    return arr


result = tell(2, 1000)
print("2到1000之间的回文素数有：", result)
