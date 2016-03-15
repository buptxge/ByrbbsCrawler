#coding:utf-8
#Url解析模块，包括版块页解析与具体帖子内容解析两部分

from lxml import html
from redis_helper import *
import json
import datetime
import requests

def parse_article(url):
    """
        解析具体帖子内容，获取帖子的标题、作者、发布时间、正文内容、附件（图片、视频、音频）
        返回包含上述内容的Dict
    """

    dic = {}
    
    r = requests.get(url)
    root = html.fromstring(r.content)
    dic["title"] = root.xpath("//ul[@class='list sec']/li[@class='f']/text()")[0]
    dic["author"] = root.xpath("//ul[@class='list sec']/li[2]/div[@class='nav hl']/div[1]/a[2]/text()")[0]
    dic["date"] = root.xpath("//ul[@class='list sec']/li[2]/div[@class='nav hl']/div[1]/a[@class='plant'][2]/text()")[0]
    dic["content"] = "\n".join(map(lambda x:x.encode('utf-8'),root.xpath("//ul[@class='list sec']/li[2]/div[@class='sp']/text()")))
    dic["abbr_images"] = map(lambda x:"http://m.byr.cn"+x , root.xpath("//ul[@class='list sec']/li[2]/div[@class='sp']/img[@class='resizeable']//@src")) #缩略图的URL
    dic["images"] = map(lambda x:"http://m.byr.cn"+x , root.xpath("//ul[@class='list sec']/li[2]/div[@class='sp']/a/@href")) #原图的URL
     
    return dic

def parse_board(url):
    """
        根据上一次抓取到该版面的URL的时间,抓取相应的内容，并持久化保存
    """
    r = requests.get(url)
    root = html.fromstring(r.content)
    latest_time = get_article_latest_time(url)
    latest_datetime = datetime.datetime.strptime(latest_time,"%Y-%m-%d %H:%M:%S")
    
    article_urls = map(lambda x:'http://m.byr.cn'+x,root.xpath("//ul[@class='list sec']/li/div[1]/a[@class!='top']/@href"))
    for url in article_urls:
        data = parse_article(url)
        article_datetime = datetime.datetime.strptime(data['date'],"%Y-%m-%d %H:%M:%S")
        

        
        
        
    


if __name__ == "__main__":
    url = "http://m.byr.cn/article/ParttimeJob/485912"
    parse_article(url)


    
    
    
    
    
    

