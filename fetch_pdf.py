#!/usr/bin/env python
from sys import argv
import re
import urllib

url="http://vision.stanford.edu/teaching/cs231b_spring1415/"

txt = open("syllabus.html", "r")
for line in txt:
        index = line.find(".pdf")
        if index != -1:
                lists = line.split("\"")
                rets = [list for list in lists if list.find(".pdf") != -1]
                for ret in rets:
                        if line.find("http:") == -1:
                                fetch_url = url + str(ret)
                                name = str(ret).split("/")[-1]
                                print fetch_url + " ---> " + name
                                urllib.urlretrieve(fetch_url, filename=name)
                        else:
                                name = str(ret).split("/")[-1]
				print ret + " ---> " + name
                                urllib.urlretrieve(ret, filename=name)
