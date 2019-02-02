"""
テラスハウスハワイ編で流れた曲をまとめてくれるサイトの曲、アーティストをスクレイピングする
"""

import csv
import linecache
import requests
import os

from bs4 import BeautifulSoup

url = "https://mora.jp/topics/osusume/terracehouse_bgm/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
title = soup.find_all("p", class_="title")

print(len(title))
for t in title:
    print(t.string)


with open("hawai_music.csv", "w") as csv_file:
    fieldnames = ["Title/Artist"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    for t in title:
        writer.writerow({'Title/Artist': t.string})



