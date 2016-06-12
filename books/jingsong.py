#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return jingsong

class jingsong(BaseFeedBook):
    title                 = u'惊悚乐园'
    description           = u'三天两觉'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    coverfile = "cv_jingsong.jpg"
    oldest_article        = 1
    feeds = [
            (u'正文', 'http://feed43.com/1270304742610646.xml')
           ]
