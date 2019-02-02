"""
テラスハウス軽井沢編で流れた曲をまとめてくれるサイトの曲、アーティストをスクレイピングする
"""

import csv
import linecache
import requests
import os

from bs4 import BeautifulSoup

url = "https://mora.jp/topics/osusume/terracehouse_bgm_karuizawa/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
title = soup.find_all("p", class_="title")
artist = soup.find_all("p", class_="artist")

print(len(artist))
for t, a in zip(title, artist):
    print(t.string," : ", a.string)


with open("karuizawa_music.csv", "w") as csv_file:
    fieldnames = ["Title", 'Artist']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    for t, a in zip(title, artist):
        writer.writerow({'Title': t.string, "Artist": a.string})



