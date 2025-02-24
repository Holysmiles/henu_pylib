import csv

import requests
from bs4 import BeautifulSoup

url = 'https://www.tiobe.com/tiobe-index/'
content = requests.get(url)
print(content.status_code)
soup = BeautifulSoup(content.text, "html.parser")
language_info = []
table = soup.find('table', class_='table table-striped table-top20')
if table:
    rows = table.find_all('tr')[1:]
    for row in rows:
        cols = row.findAll('td')
        rank = cols[0].text.strip()
        language_name = cols[4].text.strip()
        rating = cols[5].text.strip()
        language_info.append([rank, language_name, rating])





with open('result.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['排名', '编程语言名', '评级'])  # 写入表头
    writer.writerows(language_info)  # 写入数据行
