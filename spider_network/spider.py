# 利用爬虫爬取博客园
import time
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
# 设置 CSV 文件路径
csv_filename = 'data.csv'

# 准备 CSV 文件，写入表头
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['标题', '日期', '链接', '作者'])


def get_info(url, headers):
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    print(res.status_code)
    soup = BeautifulSoup(res.text, 'html.parser')

    # print(soup.text)
    # 找到包含所有文章的父级容器
    articles_page = soup.find('div', id='post_list')

    # 提取每篇文章的标题和链接   提取section标签不需要添加class 同理article也是一样的
    articles_list = articles_page.find_all('article')
    # print(articles_list)
    # 提取数据并写入 CSV
    with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for articles in articles_list:
            # 提取标题
            title = articles.find('a', class_='post-item-title').get_text().strip()
            # 提取日期
            date = articles.find('span', class_='post-meta-item').get_text().strip()
            # 提取链接
            link = articles.find('a', class_='post-item-title')['href'].strip()
            # 提取作者
            author = articles.find('a', class_='post-item-author').get_text().strip()
            # 打印提取结果

            # print("标题:", title)
            # print("日期:", date)
            # print("链接:", link)
            # print("作者:", author)
            # 将数据写入 CSV 文件
            writer.writerow([title, date, link, author])


if __name__ == '__main__':
    url = 'https://www.cnblogs.com'
    header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
            }

    for i in range(1, 11):
        if i == 1:
            get_info(url, header)
        else:
            get_info(url + '/#p' + str(i), header)


#     /#p2
