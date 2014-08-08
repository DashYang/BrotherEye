#!/usr/bin/env python
# encoding: utf-8

import re
_metaclass_ = type

class MatchManage:
    nameset = ['蝙蝠侠' , '超人' , '复仇者' , '巫毒']

    def getNameAppearTime(self , content):
        dic = {}
        for name in self.nameset:
            pattern = name.decode('utf-8')
            resultset = re.findall(pattern ,  content)
            if(len(resultset) > 0):
                dic[name] = len(resultset)
        return dic

#mm = MatchManage()
#teststring = "蝙蝠侠超人复仇者"
#table = mm.getNameAppearTime(teststring)
#print table
#for name in table:
    #print name + ":%d" % table[name]
