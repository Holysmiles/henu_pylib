num_map ={
    '0': '零',
    '1': '壹',
    '2': '贰',
    '3': '叁',
    '4': '肆',
    '5': '伍',
    '6': '陆',
    '7': '柒',
    '8': '捌',
    '9': '玖'
}


def num_to_chinese():
    chinese = ""
    num_str = input("请输入数字：")
    for num in num_str:
        chinese += num_map[num]

    print("转换结果是：")
    print(chinese)


if __name__ == "__main__":
    num_to_chinese()
