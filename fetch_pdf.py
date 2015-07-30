#!/usr/bin/env python
from sys import argv
import re
import urllib

### This needs to make sure again and again!
url="http://vision.stanford.edu/teaching/cs231b_spring1415/"
#src_url="http://vision.stanford.edu/teaching/cs231b_spring1415/syllabus.html"

print "NOTE: add url webpage and make sure the fetch url is correct, especially the base url!"

src_url = argv[1]
print "source webpage: " + src_url

## first fetch the source HTML page
urllib.urlretrieve(src_url, filename="syllabus.html")

txt = open("syllabus.html", "r")
for line in txt:
        index = line.find(".pdf")
	index_ppt = line.find(".ppt")
        if index != -1 or index_ppt != -1:
                lists = line.split("\"")
                rets = [list for list in lists if list.find(".pdf") != -1 or list.find(".ppt") != -1]
                for ret in rets:
			# for relative path, combine it with previous path
                        if line.find("http:") == -1:
                                fetch_url = url + str(ret)
                                name = str(ret).split("/")[-1]
                                print fetch_url + " ---> " + name
                                urllib.urlretrieve(fetch_url, filename=name)
			# for absolute path, just use it
                        else:
                                name = str(ret).split("/")[-1]
				# fix bugs: ret may not contain "http", just with "ppt/pdf"(line has but ret not)	
				if ret.find("http:") != -1:
					print ret + " ---> " + name
                                	urllib.urlretrieve(ret, filename=name)
