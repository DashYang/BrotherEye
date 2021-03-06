#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2014-8-21

@author: dash
'''

import MySQLdb
import traceback
import ConfigParser
import os

from tutorial.items import CommentItem
from tutorial.items import EntryItem
from tutorial.items import SiteItem
from tutorial.items import MultiMediaItem
from tutorial.items import ReplyItem
from tutorial.useritems import UserInfo
from tutorial.useritems import FavoriteTieba
from tutorial.useritems import Tiezi

_metaclass_ = type

class MySqlConnector:
    url = "127.0.0.1"
    username = "root"
    password = "123456"
    basename = "BrotherEye"
    db = None

    def __init__(self):
        absolutepath =  os.path.split(os.path.realpath(__file__))[0]
        config = ConfigParser.ConfigParser()
        config.readfp(open(absolutepath + '/database.conf',"rb"))
        self.url = config.get("global" , "url")
        self.username = config.get("global" , "username")
        self.password = config.get("global" , "password")
        self.basename = config.get("global" , "basename")

        self.db = MySQLdb.connect(self.url , self.username , self.password , self.basename , charset = "utf8")
    
    '''
        storage site info
    '''
    def insertSiteItem(self , item):
        cursor = self.db.cursor()
        sql = "INSERT INTO site (`title`, `link`) VALUES ('%s', '%s');" % (item['title'] , item['link'])
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception:
            self.db.rollback()
            var = traceback.format_exc()
            print var
        cursor.close()
        
    '''
        storage entry info
    '''
    def insertEntryItem(self , item):
        cursor = self.db.cursor()
        sql = "INSERT INTO entry (`id`, `belongto` ,`reply` , `author` , `userid` , `title` , `link`) VALUES (%s,  %s , %s,  %s  , %s ,  %s  ,  %s );"  #% \
#             (item[ id'] , item['belongto'] ,item['reply'] , item['author'] , item['userid'] , item['title'] , item['link'])
        try:
            cursor.execute(sql ,(item['id'] , item['belongto'] ,item['reply'] , item['author'] , item['userid'] , item['title'] , item['link']))
            self.db.commit()
        except Exception:
            self.db.rollback()
            var = traceback.format_exc()
            print var
        cursor.close()
#         self.db.close()
     
        
    def  insertCommentItem(self , item):
        cursor = self.db.cursor()
        sql = "INSERT INTO comment (`post_id`, `belongto` , `user_id` , `user_name` , `user_sex`, `level_id` , `level_name` , `bawu` , `open_type` , `date`, `content`) \
         VALUES ( %s ,  %s  ,  %s  ,  %s , %s, %s,  %s , %s,  %s ,  %s ,  %s  );"  #% \
        try:
            cursor.execute(sql , (item['post_id'] , item['belongto'] , item['user_id'] , item['user_name'] , item['user_sex'] , item['level_id'] ,  item['level_name'], item['bawu'] \
             , item['open_type'] , item['date'] , item['content']))
            self.db.commit()
        except Exception:
            self.db.rollback()
            var = traceback.format_exc()
            print var
        cursor.close()
#         self.db.close()
        
    '''
        storage MultimediaItem info
    '''
    def insertMutiMediaItem(self , item):
        cursor = self.db.cursor()
        sql = "INSERT INTO multimedia (`belongto`, `url`) VALUES ('%s', '%s');" % (item['belongto'] , item['url'])
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception:
            self.db.rollback()
            var = traceback.format_exc()
            print var
        cursor.close()
#         self.db.close()
    
    '''
        storage ReplyItem info
    '''
    def insertReplyitem(self , item):
        cursor = self.db.cursor()
        sql = "INSERT INTO reply (`comment_id`, `belongto` , `content` , `user_id` , `now_time`) VALUES ( %s ,  %s  ,  %s  , %s  ,  %s );"  #%  \
#         (item['comment_id'] , item['belongto'] , item['content'] , item['user_id'], item['now_time'])
        try:
            cursor.execute(sql , (item['comment_id'] , item['belongto'] , item['content'] , item['user_id'], item['now_time']))
            self.db.commit()
        except Exception:
            self.db.rollback()
            var = traceback.format_exc()
            print var
        cursor.close()
#         self.db.close() 
    
    def insertUserInfo(self , item):
        cursor = self.db.cursor()
        sql = "INSERT INTO userinfo (`username`, `sex` , `location` , `birthplace` , `fans`, `follows`, `portrait`) VALUES ( %s ,  %s  ,  %s  , %s  , %s , %s , %s );"  #%  \
        try:
            cursor.execute(sql , (item['username'] , item['sex'] , item['location'] , item['birthplace'], item['fans'] , item['follows'] , item['portrait']))
            self.db.commit()
        except Exception:
            self.db.rollback()
            var = traceback.format_exc()
            print var
            print item['username']
            print item['portrait']
        cursor.close()
        
    def insertFavoriteTieba(self , item):
        cursor = self.db.cursor()
        sql = "INSERT INTO favoritetieba (`username`, `level` , `name` ) VALUES ( %s ,  %s  ,  %s );"  
        try:
            cursor.execute(sql , (item['username'] , item['level'] , item['name'] ))
            self.db.commit()
        except Exception:
            self.db.rollback()
            var = traceback.format_exc()
            print var
            print item['username']
        cursor.close()
        
    def insertTiezi(self , item):
        cursor = self.db.cursor()
        sql = "INSERT INTO tiezi (`username`, `reply` , `url`, `comment`, `tieba` ) VALUES ( %s ,  %s  ,  %s , %s , %s );"  
        try:
            cursor.execute(sql , (item['username'] , item['reply'] , item['url'] , item['comment'] , item['tieba'] ))
            self.db.commit()
        except Exception:
            self.db.rollback()
            var = traceback.format_exc()
            print var
            print item['url']
            print item['username']
        cursor.close()        
    
    def storageItem(self ,item): 
        if isinstance(item , SiteItem):
            self.insertSiteItem(item)
        elif isinstance(item , EntryItem):
            self.insertEntryItem(item)
        elif isinstance(item , CommentItem):
            self.insertCommentItem(item)
        elif isinstance(item , MultiMediaItem):
            self.insertMutiMediaItem(item)
        elif isinstance(item , ReplyItem):
            self.insertReplyitem(item)
        elif isinstance(item , UserInfo):
            self.insertUserInfo(item)
        elif isinstance(item , FavoriteTieba):
            self.insertFavoriteTieba(item)
        elif isinstance(item , Tiezi):
            self.insertTiezi(item)

    def __del__(self):
        self.db.close()    
    
if __name__ == "__main__":
    db = MySqlConnector()
    item = SiteItem()
    db.storageItem(item)
            