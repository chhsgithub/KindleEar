#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return yichang

class yichang(BaseFeedBook):
    title                 = u'异常生物见闻录'
    description           = u'远瞳'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 1
    feeds = [
            (u'正文', 'http://feed43.com/3282680737133808.xml')
           ]
