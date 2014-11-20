# coding=utf-8

import os,sys


sys.stdout = open("update.sql", "w")


print """
USE dlrcDB;
SELECT * FROM elecFirm;	#查看
DELETE FROM elecFirm;	#删除全表内容

# elecFirm(devTypeNums, name, fullName, url, detial)
"""

for name in os.listdir("./"):
	if ".bin" in name:
		machine = "none"
		if "diancilu" in name:
			machine = "diancilu00001"
		if "dianfanbao" in name: 
			machine = "dianfanbao00001"
		print "INSERT INTO elecFirm VALUE(\"%s\", \"%s\", \"%s\", \"/download/firmware/\", \"fun\");" % (machine, name.strip(".bin"), name)