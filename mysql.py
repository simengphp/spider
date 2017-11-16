#!/usr/bin/python
# encoding: utf8
import MySQLdb
db = MySQLdb.connect("localhost", "root", "", "sql")
cursor = db.cursor()
cursor.execute("select * from tb_article")
data = cursor.fetchall()
print data
db.close()
