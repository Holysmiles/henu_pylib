import cmath
import math


# (1)编写函数，检查获取传入列表或者元组对象的所有奇数位索引对应的元素。
def select_odd_index_position(sequence):
    if not isinstance(sequence, (list, tuple)):
        return "please input list or tuple"
    return [sequence[i] for i in range(len(sequence)) if i % 2 != 0]


# (2)编写函数，判断用户传入的对象（字符串、元组、列表）长度是否大于6。
def is_len_than_6(sequence):
    if not isinstance(sequence, (str, list, tuple)):
        return "please input str list or tuple"
    return len(sequence) > 6


# (3)编写函数，检查传入列表的长度，如果大于2，将列表的前两项内容返回给调用者。
def check_len(sequence):
    if not isinstance(sequence, list):
        return "please input list "
    if len(sequence) > 2:
        return [sequence[i] for i in range(2)]
    else:
        return "len < 2"


# (4)编写函数，计算传入函数的字符串中，数字、字母、空格以及其他内容的个数，并返回
def count_number(String):
    if not isinstance(String, str):
        return "please input sreting"

    dic = {"digit": 0, "letter": 0, "space": 0, "other": 0}
    for i in String:
        if i.isdigit():
            dic["digit"] += 1
        elif i.isspace():
            dic["space"] += 1
        elif i.isalpha():
            dic["letter"] += 1
        else:
            dic["other"] += 1
    return dic


# (5)编写函数，返回两个数字参数中较大的那个数字
def bigger_number(a, b):
    if a > b:
        return a
    else:
        return b


# (6)编写函数，接收多个数字，求和并返回。
def sum_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


# (7)编写函数，参数为一个字符串，返回这个字符串所有子串里面构成回文串的最大子串。
def judge_it_len(arr: str, x: int, y: int):
    length = len(arr)
    while x >= 0 and y < length and arr[x] == arr[y]:
        x -= 1
        y += 1
    return y - x + 1 - 2


def longest_hui_wen(s):
    if not isinstance(s, str):
        return "please input string"
    if len(s) < 2:
        return s
    max_len = 1
    begin = 0
    for i in range(0, len(s) - 1):
        odd_len = judge_it_len(s, i, i)
        even_len = judge_it_len(s, i, i + 1)
        cur_len = max(even_len, odd_len)
        if cur_len > max_len:
            max_len = cur_len
            begin = i - (max_len - 1) / 2
            begin = int(begin)

    return s[begin:begin+max_len:1]


# (8)编写函数，输入不定长参数，将其中是整型的全部相加，忽略非整型的参数。（提示：判断是否是整型可以使用isinstance函数）
def add_int(*args):
    total = 0
    for i in args:
        if isinstance(i, int):
            i = int(i)
            total += i

    return total


# (9)编写函数，传入函数中多个实参（均为可迭代对象，如字符串、元组、列表、集合等），将每个实参的每个元素依次加入到函数的动态参数args里面，例如传入两个参数[1, 2, 3] (10, 20）最终args为（1,2,3,10,20)
def merge_iterables(*iterables):
    args = [element for iterable in iterables for element in iterable]
    args = tuple(args)
    return args


# (10)编写函数，传入函数中多个实参（均为字典），将每个实参的每个元素依次加入到函数的动态参数kwargs里面，例如传入两个参数{'one':1} {'two':2}, 最终kwargs为{'one': 1, 'two': 2}。
def merge_dicts(*dicts):
    dict = {}
    for i in dicts:
        dict.update(i)

    return dict

# (11)解一元二次方程。func（a, b, c）求x1， x2
def solve_func(a, b ,c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)

        return root1, root2
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

        return root1, root2


if __name__ == "__main__":
    print("func 1")
    print(select_odd_index_position((1, 2, 3, 4, 5, 6, 7, 8, 9)))
    print("func 2")
    print(is_len_than_6((1, 2, 3, 4, 5, 6, 7)))
    print("func 3")
    print(check_len((1, 3, 5, 6)))
    print("func 4")
    print(count_number("dfh123   +++"))
    print("func 5")
    print(bigger_number(3, 5))
    print("func 6")
    print(sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9))
    print("func 7")
    longest_hui_wen("asdfghjkl;lkjhgfdsadddddd")
    print("func 8")
    print(add_int(1, 3, 5, "ss", "+++"))
    print("func 9")
    print(merge_iterables((1, 2, 4, 5), ("22", "ff")))
    print("func 10")
    merge_dicts({'one': 1}, {'two': 2})
    print("func 11")
    print(solve_func(3, 1, -4))

