#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ZhihuDaily

class ZhihuDaily(BaseFeedBook):
    title                 = u'知乎日報'
    description           = u'测试book.py文件修改。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile = "mh_zhihudaily.gif"
    coverfile = "cv_zhihudaily.jpg"
    oldest_article        = 1
    feeds = [
            (u'知乎日报', 'http://zhihudaily.dev.malash.net/', True)
           ]
