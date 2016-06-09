#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return zuijingengxin

class zuijingengxin(BaseFeedBook):
    title                 = u'最近更新'
    description           = u'小说更新。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile = "mh_zhihudaily.gif"
    coverfile = "cv_zhihudaily.jpg"
    oldest_article        = 1
    feeds = [
            (u'异常生物见闻录', 'http://ftr.fivefilters.org/makefulltextfeed.php?url=http%3A%2F%2Ffeed43.com%2F6820851543660080.xml&max=3')
            ('惊悚乐园', 'http://ftr.fivefilters.org/makefulltextfeed.php?url=http%3A%2F%2Ffeed43.com%2F6374563070402853.xml&max=3'),
            ('Leaders', 'http://www.economist.com/rss/leaders_rss.xml'),
            ('Briefings', 'http://www.economist.com/rss/briefings_rss.xml'),
            ('Special reports', 'http://www.economist.com/rss/special_reports_rss.xml'),
           ]
