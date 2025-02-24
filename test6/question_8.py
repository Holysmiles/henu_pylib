import re
from collections import Counter

def count_word_frequency(text):
    # 使用正则表达式去除文本中的标点符号，并将文本分割成单词
    text = re.sub(r'[^\w\s]', '', text)  # 去掉所有非字母和数字的字符
    # print(text)
    words = text.lower().split()  # 转换为小写并按空格分割成单词列表,None（默认值）表示根据任何空格进行拆分
    # print(words)
    # 使用 Counter 统计每个单词出现的频率
    word_counts = Counter(words)

    return word_counts

# 示例文本
text = "who have an apple apple is free .....free is money you know"

# 统计词频
word_counts = count_word_frequency(text)

# 输出词频统计结果
print(word_counts)
