#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2014-9-2

@author: dash
'''
import time

from scrapy.spider import Spider
from scrapy.http.request import Request
from tutorial.ReParser import ReParser
from tutorial.FileReader import FileReader

class UserCrawler(Spider):
    name = 'fetchuser'
    allowed_domains = ["baidu.com"]
    asyncurl = "http://www.baidu.com/p/sys/data/tieba/feed?rec=%d&portrait=%s&pn=%d&type=all&t=%s"
    
    def start_requests(self):
        fr = FileReader();
        nameset = fr.readLines('userlist');
        for name in nameset:
            url = "http://www.baidu.com/p/%s?from=tieba"  % name
            print url
            request =  Request(url , callback=self.parse_response)
            request.meta['username'] = name
            yield request
        
    def parse_response(self , response):
        p = ReParser()
        username = response.meta['username']
        portrait = p.parse_info(response.body , username).get("portrait")
        timestamp = int(time.time())
        pn = 2
        rec = 0
        url = self.asyncurl % (1000000,portrait,pn,timestamp)
        request =  Request(url , callback=self.parse_asyncinfo)
        request.meta['portrait'] = portrait
        request.meta['pn'] = pn
        request.meta['username'] = username
        request.meta['timestamp'] = timestamp
        request.meta['rec'] = rec
        yield request
        
    def parse_asyncinfo(self , response):
        p = ReParser()
        pn = response.meta['pn']
        portrait = response.meta['portrait']
        username = response.meta['username']
        timestamp = response.meta['timestamp']
        rec = response.meta['rec']
        print "page number  %s" % pn
        flag = p.parse_asyncinfo(response.body , username)
        
        print flag
        print "rec:",rec
        if flag == 'moreFeed':
            pn += 1
            url = self.asyncurl % (1000000,portrait,pn,timestamp)
            request =  Request(url , callback=self.parse_asyncinfo)
            request.meta['portrait'] = portrait
            request.meta['pn'] = pn
            request.meta['username'] = username
            request.meta['timestamp'] = timestamp
            request.meta['rec'] = 0
#             time.sleep(2)
            yield request
        elif rec < 10:
            rec += 1
            url = self.asyncurl % (1000000 + rec,portrait,pn,timestamp)
            request =  Request(url , callback=self.parse_asyncinfo)
            request.meta['portrait'] = portrait
            request.meta['pn'] = pn
            request.meta['username'] = username
            request.meta['timestamp'] = timestamp
            request.meta['rec'] = rec
#             time.sleep(2)
            yield request
