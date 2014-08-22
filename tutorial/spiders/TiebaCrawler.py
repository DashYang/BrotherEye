#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2014-8-20

@author: dash
'''

import scrapy
import hashlib
import os
import time

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

from tutorial.items import SiteItem
from tutorial.Parser import HtmlParser
from tutorial.DBconnector import MySqlConnector

class TiebaCrawler(Spider):
    name = 'tiebacrawler'
    allowed_domains = ["tieba.baidu.com"]
    start_urls =[]
    MAXSIZE = 10
    pagenumber = 0
    
    def count(self):
        self.pagenumber += 1
        if self.pagenumber >= self.MAXSIZE:
            print 'over size'
            os._exit(0)
        
    def __init__(self):
        siteitems = []
        siteitem = SiteItem()
        name = "残疾人"
        link = "http://tieba.baidu.com/f?kw=%s&pn=0" % name
        siteitem['title'] = name
        siteitem['link'] = link
        db = MySqlConnector()
        print siteitem
        db.storageItem(siteitem)
        self.start_urls.append(link)
        self.pagenumber = 0
    
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
#             lastpageindex = 0
        except Exception as e:
            print e
            lastpageindex = 0
        
#         print 'lastpageindex %d' % lastpageindex
        currentpagehref = int(sel.xpath("//span[@class='cur']/text()").extract()[0])
        currentpageindex = (currentpagehref - 1) * 50
        
        base_url = get_base_url(response)
#         print "current url %s " % base_url
        if base_url.find("pn=") != -1:
            next_url = base_url[0:base_url.rindex("pn=")] + 'pn=%d' % (currentpageindex + 50)
        else:
            next_url = base_url + 'pn=%d' % (currentpageindex + 50)
        if currentpageindex < lastpageindex:
#             print "entry %s" % next_url
            yield Request(next_url , callback=self.collect_entries)

    def collect_comment(self , response):
        sel = Selector(response)
        topic = sel.xpath('//div[@class="l_post l_post_bright noborder"]')
        othercomment = sel.xpath('//div[@class="l_post l_post_bright "]')
        htmlparser = HtmlParser()
        htmlparser.parseComment(response)
#         print  "topic:%d othercomment %d"  % (len(topic.extract()) ,len(othercomment.extract()))
        totalpage = sel.xpath("//li[@class='l_reply_num']/span[last()]/text()")
#         print 'pagecontent %s' % totalpage.extract();
        
        pagenum = int(totalpage.extract()[0])
        if pagenum > 1:
            base_url = get_base_url(response)
#             print 'current page %s ' % sel.xpath("//span[@class='tP']/text()").extract()
            currentpage = int(sel.xpath("//span[@class='tP']/text()").extract()[0])
            
            if base_url.find("pn=") != -1:
                next_url = base_url[0:base_url.rindex("pn=")] + 'pn=%d' % (currentpage + 1)
            else:
                next_url = base_url + '?pn=%d' % (currentpage + 1)
            if (currentpage + 1) <= pagenum:
#                 print "next_url %s" % next_url
                time.sleep(10)
#                 print "comment :%s" % next_url
                yield Request(next_url , callback=self.collect_comment)
#         print "topic %d other %d" % (len(topic.extract()) , len(othercomment.extract()))
