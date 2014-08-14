#!/usr/bin/env python
# encoding: utf-8

import re
import os
_metaclass_ = type

class MatchManage:
    nameset = []

    def __init__(self):
        absolutepath =  os.path.split(os.path.realpath(__file__))[0]
        namefile = open(absolutepath + '/namefile')
        try:
            for line in namefile:
                self.nameset.append(line.strip('\n'))
        finally:
                 namefile.close( )

    def getNameAppearTime(self , content):
        dic = {}
        for name in self.nameset:
            pattern = name.decode('utf-8')
            resultset = re.findall(pattern ,  content)
            if(len(resultset) > 0):
                dic[name] = len(resultset)
        return dic

mm = MatchManage()
#teststring = "蝙蝠侠超人复仇者"
#table = mm.getNameAppearTime(teststring)
#print table
#for name in table:
    #print name + ":%d" % table[name]
