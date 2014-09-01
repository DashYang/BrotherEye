#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2014-8-20

@author: dash
'''

import time

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scrapy.utils.response import get_base_url

from tutorial.items import SiteItem
from tutorial.Parser import HtmlParser
from tutorial.DBconnector import MySqlConnector
from tutorial.FileReader import FileReader

class TiebaCrawler(Spider):
    name = 'tiebacrawler'
    allowed_domains = ["tieba.baidu.com"]
    start_urls =[]
    MAXSIZE = 10
        
    def __init__(self):
        siteitem = SiteItem()
        fr = FileReader();
        nameset = fr.readLines('list');
        db = MySqlConnector()
        for name in nameset:
            link = "http://tieba.baidu.com/f?kw=%s&pn=0" % name
            siteitem['title'] = name
            siteitem['link'] = link
            db.storageItem(siteitem)
            self.start_urls.append(link)
            
        
    
    ## according to start_url to crawl tieba
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url , callback=self.collect_entries)
     
    ## collect entries from specify tieba        
    def collect_entries(self ,response):
        sel = Selector(response)
        htmlparser = HtmlParser()
#         print 'parse site'
        entrylinks = htmlparser.parserSite(response)
        for link in entrylinks:
            print "comment %s" % link
            yield Request(link , callback=self.collect_comment)
        
        try: 
            lastpagehref = sel.xpath("//a[@class='last']/@href").extract()[0]
            lastpageindex = int(lastpagehref[lastpagehref.rindex("pn=")+3:len(lastpagehref)])
        except Exception as e:
            print e
            lastpageindex = 0
        
        currentpagehref = int(sel.xpath("//span[@class='cur']/text()").extract()[0])
        currentpageindex = (currentpagehref - 1) * 50
        
        base_url = get_base_url(response)
        if base_url.find("pn=") != -1:
            next_url = base_url[0:base_url.rindex("pn=")] + 'pn=%d' % (currentpageindex + 50)
        else:
            next_url = base_url + 'pn=%d' % (currentpageindex + 50)
        if currentpageindex < lastpageindex:
            yield Request(next_url , callback=self.collect_entries)

    def collect_comment(self , response):
        sel = Selector(response)
        htmlparser = HtmlParser()
        htmlparser.parseComment(response)
        totalpage = sel.xpath("//li[@class='l_reply_num']/span[last()]/text()")
        
        pagenum = int(totalpage.extract()[0])
        if pagenum > 1:
            base_url = get_base_url(response)
            currentpage = int(sel.xpath("//span[@class='tP']/text()").extract()[0])
            
            if base_url.find("pn=") != -1:
                next_url = base_url[0:base_url.rindex("pn=")] + 'pn=%d' % (currentpage + 1)
            else:
                next_url = base_url + '?pn=%d' % (currentpage + 1)
            if (currentpage + 1) <= pagenum:
                time.sleep(2)
                yield Request(next_url , callback=self.collect_comment)
