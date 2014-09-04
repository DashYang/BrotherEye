#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2014-8-20

@author: dash
'''
import json
import re
import time

from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from tutorial.items import CommentItem
from tutorial.items import EntryItem
from tutorial.items import MultiMediaItem
from tutorial.items import ReplyItem
from tutorial.DBconnector import MySqlConnector
_metaclass_ = type

class HtmlParser:
    
    db = MySqlConnector()
    
    def __init__(self):
        pass
    
    '''
        get real time, maybe not so correct
    '''
    def getRealTime(self , timestamp):
        timeArray = time.localtime(timestamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return  otherStyleTime
    
    #parse entry's content
    def parserEntry(self , Xpathelments):
        pass
    
    def extractUserid(self , tag):
        return tag[tag.rindex(":")+1 : len(tag) - 1].strip()
    
    def extractAuthor(self , tag):
        return tag[tag.rindex(":") +1: len(tag) - 1].strip()
    
    def parserSite(self , response):
        sel = Selector(response)
        entries = sel.xpath("//div[@class='t_con cleafix']")
        base_url = get_base_url(response)
        entrylist = [];
        for entry in entries:
            item = EntryItem()
            replydiv = entry.xpath("div[@class='threadlist_li_left j_threadlist_li_left']");
            
            reply = replydiv.xpath("div[@class='threadlist_rep_num']/text()").extract()[0]
            
            detaildiv = entry.xpath("div[@class='threadlist_li_right j_threadlist_li_right']/div[@class='threadlist_lz clearfix']")
             
            titlediv = detaildiv.xpath("div[1]")
            
            title = titlediv.xpath('a/text()').extract()[0]
            link =  urljoin_rfc(base_url , titlediv.xpath('a/@href').extract()[0])
            
            try:
                authordiv = detaildiv.xpath("div[@class='threadlist_author']/span[contains(@class,'tb_icon_author ')]")
                author  = self.extractAuthor(authordiv.xpath("@title").extract()[0])
                userid = self.extractUserid(authordiv.xpath("@data-field").extract()[0])
            except Exception as e:
                print e
                
            item['id'] = link[link.rindex("/")+1:len(link)]
            item['belongto'] = base_url
            item['reply'] = reply
            item['author'] = author
            item['userid'] = userid
            item['title'] = title
            item['link'] = link
#             print item
            self.db.storageItem(item);
            
#             print item
#             print "reply:%s author:%s userid:%s title:%s link:%s "   % (reply , author , userid , title , link ) 
            entrylist.append(link)
        
        return entrylist
    
    def parseComment(self , response):
        sel = Selector(response)
        commentdivs = sel.xpath("//div[contains(@class,'l_post')]")
        base_url = get_base_url(response)
#         print base_url
#         print "len %d" % len(commentdivs)
        for commentdiv in commentdivs:
#             print commentdiv.extract();
            data = commentdiv.xpath("@data-field")
            try:
                json_data = json.loads(data.extract()[0])
                json_content = json_data['content']  
                json_author =  json_data['author']
            except Exception:
                print 'this comment is an ad!'
                continue
            
            item = CommentItem() 
            if '?' in base_url:
                item['belongto'] =  base_url[base_url.rindex('/')+1:base_url.rindex('?')]
            else:
                item['belongto'] =  base_url[base_url.rindex('/')+1:len(base_url)]
            item['user_id'] = json_author.get('user_id')
            item['user_name'] = json_author.get('user_name')
            item['user_sex'] = json_author.get('user_sex')
            item['level_id'] = json_author.get('level_id')
            item['level_name'] = json_author.get('level_name')
            item['bawu'] = json_author.get('bawu')
            
            item['post_id'] = json_content.get('post_id')     #primary key
            item['open_type'] = json_content.get('open_type')
            item['date'] = json_content.get('date')

            
            commentdetaildiv = commentdiv.xpath("div[contains(@class,'d_post_content_main')]/div/cc/div[1]")
#             print get_base_url(response)
            contentlines = commentdetaildiv.xpath("text()").extract()
            content = ""
            for line in contentlines:
                content += line
            
            item['content'] = content    
#             print item
            self.db.storageItem(item);
            multimedias = commentdetaildiv.xpath("img[@class='BDE_Image']/@src")
            for multimedia in multimedias:
                imgitem =  MultiMediaItem()
                imgitem['belongto'] = item['post_id']
                imgitem['url'] = multimedia.extract()
#                 print imgitem
                self.db.storageItem(imgitem);
            
        self.parserReply(response.body)
            
    def parserReply(self , html):
        regex = r'commentList" : (.*?),    "isAdThread"'
        pattern = re.compile(regex)
        match = pattern.findall(html)
        if match == []:
            return
        json_data = json.loads(match[0],encoding='gbk')
        for post_id in json_data:
            if json_data[post_id] != []:
                for replydetail in json_data[post_id]:
                        item = ReplyItem()
                        item['comment_id'] = replydetail['comment_id']
                        item['content'] = replydetail['content']
                        item['user_id'] = replydetail['user_id']
                        item['now_time'] = self.getRealTime(replydetail['now_time'])
                        item['belongto'] = post_id
#                         print item    
                        self.db.storageItem(item);
                        
if __name__ == "__main__":
    ts = 1409562088696
    timeArray = time.localtime(ts)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print otherStyleTime
    pass
