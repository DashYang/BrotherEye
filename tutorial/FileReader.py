#!/usr/bin/env python
# encoding: utf-8

'''
Created on 2014-9-1

@author: dash
'''
import os

class FileReader:
    
    def readLines(self , name):
        absolutepath =  os.path.split(os.path.realpath(__file__))[0]
        namefile = open(absolutepath + '/' + name)
        nameset = []
        try:
            for line in namefile:
                nameset.append(line.strip('\n'))
        except Exception,e:
            print e
        finally:
                namefile.close( )
        return nameset