#!/usr/bin/env python
from sys import argv
import random 
import urllib

def fetch(src_url, level):
	## first fetch the source HTML page
	num = 100000 * random.random()
	filename = str(num)
	urllib.urlretrieve(src_url, filename=filename)
	txt = open(filename, "r")
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
					if fetch_url.find("<") == -1 or fetch_url.find(">") == -1:
						print fetch_url + " ---> " + name
						urllib.urlretrieve(fetch_url, filename=name)
				# for absolute path, just use it
	                        else:
	                                name = str(ret).split("/")[-1]
					# fix bugs: ret may not contain "http", just with "ppt/pdf"(line has but ret not)	
					if ret.find("http:") != -1:
						print ret + " ---> " + name
	                                	urllib.urlretrieve(ret, filename=name)
		else:
			if line.find("http:") != -1 and level != 0: # there is an url
				lists = line.split("\"")
				rets = [list for list in lists if list.find(".htm") != -1 or list.find(".html") != -1]
				for ret in rets:
					if ret.find("http:") != -1:
						print "Now there is a new url, fetch it:%s"%ret
						fetch(ret, 0)


### This needs to make sure again and again!
url="http://cs224d.stanford.edu/"
print "NOTE: add url webpage and make sure the fetch url is correct, especially the base url!"

src_url = argv[1]
level = argv[2]
print "source webpage: " + src_url
fetch(src_url, level)
