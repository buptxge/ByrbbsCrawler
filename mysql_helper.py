#coding:utf-8

import MySQLdb
from passwd import *

class MysqlHelper():

    def __init__(self):
        self.conn = MySQLdb.connect(host="localhost",
                                   user="root",
                                   passwd=LOCAL_MYSQL_PASSWD,
                                   db="Byrbbscrawler")
        self.cur = self.conn.cursor()

    def insert(self,table,dic):
        placeholders = ', '.join(['%s'] * len(dic))
        columns = ', '.join(myDict.keys())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, placeholders)
        self.cur.execute(sql, myDict.values())

if __name__ == "__main__":
    db = MysqlHelper()
    dic = {"order":"123123","money":"asdfsadf"}
    db.insert('testtable',dic)
    



