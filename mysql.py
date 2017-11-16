#!/usr/bin/python
# encoding: utf-8
import sys
import MySQLdb


db = MySQLdb.connect("localhost", "root", "", "sql", charset="utf8")
cursor = db.cursor()
cursor.execute("select * from tb_article")
data = cursor.fetchall()
# print data
for row in data:
    fname = row[0]
    lname = row[1]
    # 打印结果
    print "fname=%s,lname=%s" % \
          (fname, lname)
db.close()
