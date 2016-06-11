#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return gengxin

class gengxin(BaseFeedBook):
    title                 = u'异常生物'
    description           = u'测试。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile = "mh_zhihudaily.gif"
    coverfile = "cv_zhihudaily.jpg"
    oldest_article        = 1
    feeds = [
            (u'异常', 'http://feed43.com/5454041806035373.xml', True)
           ]
