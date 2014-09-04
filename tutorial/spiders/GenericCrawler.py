'''
Created on 2014-9-1

@author: dash
'''
from scrapy.spider import Spider 
from scrapy.http.request import Request
from scrapy.selector import Selector
# from scrapy.utils.response import get_base_url

import json

class TestParser:
    def parse(self , response):
        sel = Selector(response)
        commentdivs = sel.xpath("//div[contains(@class,'l_post')]")
#         base_url = get_base_url(response)
        for commentdiv in commentdivs:
            data = commentdiv.xpath("@data-field")
            try:
                json_data = json.loads(data.extract()[0])
                json_content = json_data['content']  
#                 json_author =  json_data['author']
            except Exception:
                print 'this comment is an ad!'
                continue
            print json_content.get('post_id')
            commentdetaildiv = commentdiv.xpath("div[contains(@class,'d_post_content_main')]/div/cc/div[1]")
            contentlines = commentdetaildiv.xpath("text()").extract()
            content = ""
            for line in contentlines:
                content += line
            print content
    
class TestCrawler(Spider):
    name = 'Test'
    allowed_domains = ["tieba.baidu.com"]

    def start_requests(self):
        url = "http://tieba.baidu.com/p/988780556"
        yield Request(url , callback=self.test_response)
        
    def test_response(self , response):
        tp = TestParser()
        tp.parse(response)
    