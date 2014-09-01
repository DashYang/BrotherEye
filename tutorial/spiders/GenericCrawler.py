'''
Created on 2014-9-1

@author: dash
'''
from scrapy.spider import Spider 
from scrapy.http.request import Request

class TestCrawler(Spider):
    name = 'Test'
    allowed_domains = ["tieba.baidu.com"]

    def start_requests(self):
        url = ""
        return Request(url , callback=self.collect_entries)
        