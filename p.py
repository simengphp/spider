#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
# 先获取到html
request = urllib2.Request('http://simengphp.com/index.php?s=/List/newsDetail/id/52')
response = urllib2.urlopen(request)
html_doc = response.read()

# 使用第三方插件beautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
# 获取一下html
# print soup.prettify()

# 获取一下标签为title的标签 title
# print soup.title.name
# 获取一下title的值 PHP面向对象编程基本原则
# print soup.title.string
# body = soup.body

# 获取一下a标签
# print soup.a

# 获取所有的a标签，然后打印一下a标签包含的内容
# for v in soup.find_all('a'):
#     print v.text

# 获取多个标签

for v in soup.find_all(['a', 'div']):
    print v.text


