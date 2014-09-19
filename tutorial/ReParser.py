#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2014-9-2

@author: dash
'''
import re

from tutorial.useritems import UserInfo
from tutorial.useritems import FavoriteTieba
from tutorial.useritems import Tiezi
from tutorial.DBconnector import MySqlConnector

class ReParser:
    db = MySqlConnector()
    
    def reg_match(self, regex , html):
        pattern = re.compile(regex)
        match = pattern.findall(html)
        if match != []:
            return match
        else:
            return [""]
     
    def parser_userinfo(self , html , username):
        userinfo = UserInfo()
        userinfo['username'] = username
        print "username:" + username + "%s" % type(username)
        regex = r"<div class=info>(.*?)<\\/div>"
        userinfo['sex'] = self.reg_match(regex , html)[0]
        
        regex = r"<div class=\"liveaddr info\" title=\"(.*?)\">"
        userinfo['location'] = self.reg_match(regex , html)[0]
        
        regex = r"<div class=\"birthaddr info\" title=\"(.*?)\">"
        userinfo['birthplace'] = self.reg_match(regex , html)[0]
        
        regex = r"fans : (\d*),"
        userinfo['fans'] = self.reg_match(regex, html)[0]
        
        regex = r"follows: (\d*)"
        userinfo['follows'] = self.reg_match(regex, html)[0]
        
        regex = r" 'portrait' : '(\w.*)',"
        userinfo['portrait'] = self.reg_match(regex, html)[0]
        self.db.storageItem(userinfo)
        return userinfo
    
    def parse_favoritetieba(self , html , username ):
        regex = r"<span class=level>(\d*).*?<\\/span> .*?<div class=tieba-name> (.*?)<\\/div>"
        tiebalist =  self.reg_match(regex, html)
        for level,name in tiebalist:
            favtieba = FavoriteTieba()
            favtieba['username'] = username
            favtieba['level'] = level
            favtieba['name'] = name
            self.db.storageItem(favtieba)
    
    def parse_tiezi(self , html , username):
        regex = r"<li class=\"feed-item clearfix item-reply\">.*? "
        regex += r"<a href=\"(.*?)\" .*?>(.*?)<\\/a>.*?<a class=feed-content .*?>(.*?)<\\/a>"
        regex += r".*?<a class=feed-from .*?>(.*?)<\\/a>.*?<\\/div>";
        replylist = self.reg_match(regex, html)
        if replylist != ['']:
            for url,reply,comment,tieba in replylist:
                tiezi = Tiezi()
                tiezi['username'] = username
                tiezi["reply"] = reply
                
                print "reply:" + reply + ":%s" % type(username)
                tiezi["url"] = url
                
                tiezi["comment"] = comment
                print "comment:" + comment + ":%s"  % type(username)                
                tiezi["tieba"] = tieba[0:len(tieba)-3] 
                self.db.storageItem(tiezi)
            
        regex = r"<li class=\"feed-item clearfix item-zhuti\">.*? <a class=feed-content href=\"(.*?)\".*?>(.*?)<\\/a>.*?<a class=feed-from .*?>(.*?)<\\/a>.*?<\\/div>"
        commentlist = self.reg_match(regex, html)
        if commentlist != ['']:
            for url,comment,tieba in commentlist:
                tiezi = Tiezi()
                tiezi['username'] = username
                tiezi["reply"] = "None"
                tiezi["url"] = url
                tiezi["comment"] = comment
                tiezi["tieba"] = tieba[0:len(tieba)-3]
                self.db.storageItem(tiezi) 
        
        
    def parse_info(self , html , username):
        html = html.decode('string_escape')
        userinfo = self.parser_userinfo(html, username)
        self.parse_favoritetieba(html, username)
        self.parse_tiezi(html, username)
        return userinfo
        
    def parse_asyncinfo(self , html  ,username):
        html = html.decode('string_escape')
        regex = r"\"hasMore\": \"(.*?)\""
        flag =  self.reg_match(regex, html)[0]
        regex = r"\"tplContent\":\"(.*)\""
        commenthtml = self.reg_match(regex, html)[0]
        self.parse_tiezi(commenthtml, username)
        return flag