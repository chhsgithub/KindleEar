#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseUrlBook

def getBook():
    return text

class text(BaseUrlBook):
    title                 = u'孺子帝'
    description           = u'冰临神下'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    coverfile = "cv_ruzidi.jpg"
    oldest_article        = 1
    feeds = [
            (u'正文', 'http://feed43.com/4753287776175011.xml')
           ]
