import requests
from bs4 import BeautifulSoup
import csv

base_url = 'https://movie.douban.com/top250'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
title_list, grade_list, link_list = [], [], []

for num in range(0, 250, 25):
    content = requests.get(f'https://movie.douban.com/top250?start={num}&filter=', headers=header)
    content.encoding = 'utf-8'
    soup = BeautifulSoup(content.text, "html.parser")
    all_titles = soup.findAll("span", attrs={"class": "title"})
    all_grade = soup.findAll("span", attrs={"class": "rating_num"})
    a_tags = soup.select('div.hd a[href]')
    for title in all_titles:
        cont = title.string
        if "/" not in cont:
            title_list.append(title.string)
    for grade in all_grade:
        grade_list.append(grade.string)
    for a_tag in a_tags:
        link = a_tag['href']
        link_list.append(link)


film_list = []
# print(title_list)
# print(grade_list)
# print(link_list)

film_list = list(zip(title_list, grade_list, link_list))

with open("film.csv", 'w', newline="", encoding='utf-8') as cvsfile:
    writer = csv.writer(cvsfile)
    writer.writerow(['电影名称', '评分', '链接'])
    writer.writerows(film_list)
