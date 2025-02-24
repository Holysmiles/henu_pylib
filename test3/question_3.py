# 获取字符串中的第一个唯一字符。
# 要求：给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 示例：
# 输入: "leetcode"
# 输出: 0

def find_character(string):
    string = str(string)
    for i in string:
        if string.count(i) == 1:
            return string.index(i)

    return -1


str_in = input("请输入一段字符串：")
result = find_character(str_in)
print(result)