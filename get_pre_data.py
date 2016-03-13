#coding:utf-8

import requests
from lxml import html

#获取论坛所有版块分区名
BBS_SECTION_URL = "http://m.byr.cn/section"
r = requests.get(BBS_SECTION_URL)

root = html.fromstring(r.content)

section_name = root.xpath("//ul[@class='slist sec']//li//a[1]/text()")
section_url = root.xpath("//ul[@class='slist sec']//li/a[1]/@href")

section_url = map(lambda x: "http://m.byr.cn"+x,section_url)
sections = dict(zip(section_name,section_url))

for url in section_url:
    r = requests.get(url)
    board_name = root.xpath("//ul[@class='slist sec']//li//a[1]/text()")
    board_url = root.xpath("//ul[@class='slist sec']/li/a/@href")
    
    board_url = map(lambda x: "http://m.byr.cn"+x,section_url)

    #TODO：找到版面名字和URL
