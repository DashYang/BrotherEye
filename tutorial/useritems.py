'''
Created on 2014-9-2

@author: dash
'''
from scrapy.item import Item, Field

class UserInfo(Item):
    username = Field()
    sex = Field()
    location = Field()
    birthplace = Field()
    fans = Field()
    follows = Field()
    portrait = Field()

class FavoriteTieba(Item):
    username = Field()   #belongto
    level = Field()
    name = Field()

class Tiezi(Item):
    username = Field()   #belongto
    reply = Field()
    url = Field()
    comment = Field()
    tieba = Field();