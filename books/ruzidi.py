#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ruzidi

class ruzidi(BaseFeedBook):
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
           
    def processtitle(self, title):
        title = BaseFeedBook.processtitle(self,title)
        if title.endswith(u',飘天文学'):
            return title.replace(u',飘天文学','')
        else:
            return title
