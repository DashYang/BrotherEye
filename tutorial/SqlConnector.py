#!/usr/bin/env python
# encoding: utf-8

import MySQLdb
import traceback
import ConfigParser
_metaclass_ = type

class SqlConnector:
    url = "127.0.0.1"
    username = "root"
    password = "123456"
    basename = "BrotherEye"
    db = None

    def __init__(self):
#         absolutepath =  os.path.split(os.path.realpath(__file__))[0]
        config = ConfigParser.ConfigParser()
        config.readfp(open('database.conf',"rb"))
        self.url = config.get("global" , "url")
        self.username = config.get("global" , "username")
        self.password = config.get("global" , "password")
        self.basename = config.get("global" , "basename")

        self.db = MySQLdb.connect(self.url , self.username , self.password , self.basename , charset = "utf8")

    def insertImage(self , title , content , url , md5 ,source):
        cursor = self.db.cursor()
        sql = "INSERT INTO hero_image (`title`, `content`, `url`, `md5`, `source`) VALUES ('%s', '%s', '%s', '%s', '%s');" % (title , content , url , md5 , source)
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception:
            self.db.rollback()
            var = traceback.format_exc()
            print var
        cursor.close()
        self.db.close()

    def getImageMD5(self):
        cursor = self.db.cursor()
        sql = "SELECT md5 FROM hero_image;"
        sqlresultset = []
        try:
            cursor.execute(sql)
            sqlresultset = cursor.fetchall()
        except Exception:
            self.db.rollback()
            var = traceback.format_exc()
            print var
        cursor.close()
        self.db.close()
        resultset = []
        for md5 in sqlresultset:
            resultset.append(md5[0])
        return resultset

    def attachImageTag(self , md5 , tag , weight):
        cursor = self.db.cursor()
        sql = "INSERT INTO image_tag (`md5`, `tag` , `weight`) VALUES ('%s', '%s' , %d);" % (md5 ,tag , weight)
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception:
            self.db.rollback()
            var = traceback.format_exc()
            print var
        cursor.close()
        self.db.close()






#sqlconnector.attachImageTag("3CAE0392B63FACCD9EB30F24DD" , "蝙蝠侠" , 1)
#resultset = sqlconnector.getImageMD5()
#for md5 in resultset:
    #print md5
#title = "【黑历史资源】老爷真正的超能力！"
#content = "在故事<<Batman The Widening Gyre>>里,蝙蝠侠Bruce Wayne把未婚妻Silver.t.Cloud带来见管家阿福.阿尔弗雷德询问为何Silver.t.Cloud称Bru"
#url = "http://imgsrc.baidu.com/forum/w%3D580/sign=65649f0e08d162d985ee621421dea950/a39e63224f4a20a4214fed0d92529822730ed034.jpg"
#md5 = "7025B93CAE0392B63FACCD9EB30F24DD"
#source = "http://tieba.baidu.com/p/3176135761"
#sqlconnector.insertImage(title , content , url , md5 , source)

