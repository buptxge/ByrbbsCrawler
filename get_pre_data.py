#coding:utf-8

import requests
from lxml import html

#获取论坛所有版块分区名及URL
BBS_SECTION_URL = "http://m.byr.cn/section"
r = requests.get(BBS_SECTION_URL)

root = html.fromstring(r.content)

section_name = root.xpath("//ul[@class='slist sec']//li//a[1]/text()")
section_url = root.xpath("//ul[@class='slist sec']//li/a[1]/@href")

section_url = map(lambda x: "http://m.byr.cn"+x,section_url)
sections = dict(zip(section_name,section_url))

with open('board_name_url.txt','w') as f:
    for url in section_url:
        r = requests.get(url)
        root = html.fromstring(r.content)

        board_name = root.xpath("//ul[@class='slist sec']//li//a[1]/text()")
        board_url = root.xpath("//ul[@class='slist sec']/li/a/@href")
        
        board_url = map(lambda x: "http://m.byr.cn"+x,board_url)

        for i in range(len(board_name)):
            f.write(board_name[i].encode('utf-8')+'\t'+board_url[i]+'\n')

