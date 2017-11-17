#!/usr/bin/python
# encoding: utf-8
import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "sql", charset="utf8")
cursor = db.cursor()
cursor.execute("select * from tb_article")
data = cursor.fetchall()
# print data
for row in data:
    print "id = %s name = %s \n" % (row[0], row[1])
db.close()
