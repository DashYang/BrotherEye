# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TutorialItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()
    
#baidu tieba site
class SiteItem(Item):
    title = Field()   #primary key
    link = Field()      

#baidu tieba entry    
class EntryItem(Item):
    id = Field()   #primarykey
    belongto = Field()
    reply = Field()
    author = Field()
    userid = Field()
    title = Field()
    link =Field()

class CommentItem(Item):
    belongto = Field()
    user_id = Field();
    user_name = Field();
    user_sex = Field();
    level_id = Field()
    level_name = Field()
    bawu = Field()
    
    post_id = Field()     #primary key
    open_type = Field()
    date = Field()
    
    content = Field()

class MultiMediaItem(Item):
    #id inc
    belongto = Field();
    url = Field();     
    
class ReplyItem(Item):
    comment_id = Field() #primary key
    belongto = Field()
    content = Field()
    user_id  = Field()
    now_time = Field() #may be calculated by this time , i can't find date in html
    
