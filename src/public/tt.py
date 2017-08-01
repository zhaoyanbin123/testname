#coding=utf-8

import ConfigParser
cf = ConfigParser.ConfigParser()

cf.read("D:/EclipseWorkSapce/misUIAutoTest/src/config/proper.ini")
name=cf.get("info", "input1")
print name