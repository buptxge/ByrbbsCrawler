#coding:utf-8

import redis
from passwd import LOCAL_REDIS_PASSWD

redis_client = redis.StrictRedis(host='localhost',port=6379,db=0,password=LOCAL_REDIS_PASSWD)

def get_article_latest_time(board_url):
"""
    获取某一板块最后一次抓取过的时间
    时间格式统一为："%Y-%m-%d %H:%M:%S"
"""
    return redis_client.hget("LATEST_ARTICLE_DATE",board_url)

def set_article_latest_time(board_url,datestr)
""" 
    设置某一论坛板块最后一次抓取的时间
    时间格式统一为："%Y-%m-%d %H:%M:%S"
"""
    redis_client.hset("LATEST_ARTICLE_DATE",board_url,datestr)
    
    


