#!/usr/bin/env python
# encoding: gbk

import scrapy
import hashlib
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

from tutorial.MatchManage import MatchManage
from tutorial.SqlConnector import SqlConnector

class BaiduSpider(Spider):
    name = "justice_league"
    allowed_domains = ["tieba.baidu.com"]
    start_urls = [
            r"http://tieba.baidu.com/f?kw=%D5%FD%D2%E5%C1%AA%C3%CB"
            ]
    filename = "imglist.html"
    md5_set = []

    def collect_img(self , response):
        sel = Selector(response)
        units = sel.xpath('//div[@class="d_post_content j_d_post_content  "]')
        webtitle = sel.xpath('//h1[@class]/text()').extract()[0]
        mm = MatchManage()
#         title_appeartable = mm.getNameAppearTime(webtitle);
        source_url = get_base_url(response)
        print "帖子数目 %d" % len(units)
        for unit in units:
            img = unit.xpath('img[@class="BDE_Image"]/@src').extract()
            description = unit.xpath('text()').extract()
            description_content = ""
            for des in description:
                description_content += des.strip() + "\n"
            content_appeartable = mm.getNameAppearTime(description_content)
            unit_appeartable = {};
            for name in content_appeartable:
                if(unit_appeartable.get(name) == None):
                    unit_appeartable[name] = content_appeartable[name]
                else:
                    unit_appeartable[name] = 3 * unit_appeartable[name] + content_appeartable[name]

            if(img != None and len(img) > 0 and unit_appeartable != None and len(unit_appeartable) > 0):
                print "title: " + webtitle
                print 'content: '
                print description_content[0:100]
                database_content = description_content[0:100]
                print "url: " + img[0]
                database_url = img[0]
                print "url len: %d" % len(img[0])
                print "MD5: " + hashlib.md5(img[0]).hexdigest().upper()
                database_md5 =  hashlib.md5(img[0]).hexdigest().upper()
                print "source: " + source_url
                database_source = source_url

                if( self.md5_set.count(database_md5) == 0):
                    sqlconnector = SqlConnector()
                    sqlconnector.insertImage(webtitle ,database_content , database_url , database_md5 , database_source)
                    print "match result:"
                    for name in unit_appeartable:
                        print name + ":%d" % unit_appeartable[name]
                        sqlconnector = SqlConnector()
                        sqlconnector.attachImageTag(database_md5 , name , unit_appeartable[name])
                    print '\n'


    def parse(self , response):
        print 'spider begin to crawl'
        sel = Selector(response)
        webtitle = sel.xpath('//head/title/text()').extract()
        entries = sel.xpath('//div[@class="threadlist_text threadlist_title j_th_tit  "]')
 #      print "webtitle:%s " % webtitle[0]
        cnt = 1;
        base_url = get_base_url(response)
        sqlconnector = SqlConnector()
        self.md5_set = sqlconnector.getImageMD5()
        print webtitle[0]
        print "entry length %s" % len(entries)
        for entry in entries:
            title = entry.xpath('a/text()').extract()[0]
            link = entry.xpath('a/@href').extract()[0]
            if(title != ['']):
                print "%d title : %s \nlink : %s \n" % (cnt , title , link)
            cnt += 1
            nexturl = urljoin_rfc(base_url, link)
#           print 'nexturlis: ' + nexturl
            yield scrapy.Request(nexturl , callback=self.collect_img)
