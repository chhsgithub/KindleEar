#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ruzit

class ruzit(BaseFeedBook):
    title                 = u'text'
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
        return title[:-4] if title.endswith(u'飘天文学') else title
        
