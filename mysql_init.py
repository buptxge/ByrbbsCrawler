#coding:utf-8

from mysql_helper import MysqlHelper

db = MysqlHelper()

#创建论坛board表
sql = "CREATE TABLE board(id int(4) not null primary key auto_increment,\
                           chs_name varchar(100) not null,\
                           eng_name varchar(100) not null,\
                           latest_article_time datetime)"
db.cur.execute(sql)

#创建论坛article表
sql = "CREATE TABLE article(id int(8) not null primary key auto_increment,\
                            url varchar(1000) not null,\
                            board_id int(4) not null,\
                            author varchar(100) not null,\
                            publsh_time datetime not null,\
                            image_count int(4),\
                            media_count int(4))"
db.cur.execute(sql)



