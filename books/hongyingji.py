#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return hongyingji

class hongyingji(BaseFeedBook):
    title                 = u'红缨记'
    description           = u'东郊林公子'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    coverfile = "cv_hongyingji.jpg"
    oldest_article        = 1
    feeds = [
            (u'正文', 'http://feed43.com/7761656613741403.xml')
           ]
