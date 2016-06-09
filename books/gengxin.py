#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return gengxin

class gengxin(BaseFeedBook):
    title                 = u'gengxin'
    description           = u'测试book.py文件修改。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile = "mh_zhihudaily.gif"
    coverfile = "cv_zhihudaily.jpg"
    oldest_article        = 1
    feeds = [
            (u'知乎日报', 'http://ftr.fivefilters.org/makefulltextfeed.php?url=http%3A%2F%2Ffeed43.com%2F6820851543660080.xml&max=3', True)
           ]
