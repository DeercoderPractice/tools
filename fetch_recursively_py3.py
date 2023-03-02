import random
import urllib
import string
from sys import argv
import urllib.request
import ssl

def fetch(src_url, level):
    ## first fetch the source HTML page
    num = 100000 * random.random()
    filename = str(num)
    urllib.request.urlretrieve(src_url, filename=filename)
    txt = open(filename, "r")
    fail_file = open("failure.txt", "w")
    for line in txt:
        index = line.find(".pdf")
        index_ppt = line.find(".xlsx")
        if index != -1 or index_ppt != -1:
            lists = line.split("\"")
            rets = [list for list in lists if list.find(".pdf") != -1 or list.find(".xlsx") != -1]
            for ret in rets:
                # for relative path, combine it with previous path
                if line.find("http:") == -1:
                    fetch_url = "http://www.chaiwithpabrai.com" + str(ret)
                    name = str(ret).split("/")[-1]
                    if fetch_url.find("<") == -1 or fetch_url.find(">") == -1:
                        print(fetch_url + " ---> " + name)
                        try:
                            urllib.request.urlretrieve(str(fetch_url), filename=name)
                        except urllib.error.HTTPError:
                            print("404")
                            fail_file.write(fetch_url + "\n")
                        except:
                            print("Something else went wrong")
                # for absolute path, just use it
                else:
                    name = str(ret).split("/")[-1]
                    # fix bugs: ret may not contain "http", just with "ppt/pdf"(line has but ret not)
                    if ret.find("http:") != -1:
                        print(ret + " ---> " + name)
                        urllib.request.urlretrieve(ret, filename=name)
        else:
            if line.find("http:") != -1 and level != 0:  # there is an url
                lists = line.split("\"")
                rets = [list for list in lists if list.find(".htm") != -1 or list.find(".html") != -1]
                for ret in rets:
                    if ret.find("http:") != -1:
                        print("Now there is a new url, fetch it:%s" % ret)
                        fetch(ret, 0)


### This needs to make sure again and again!
ssl._create_default_https_context = ssl._create_unverified_context
url = "http://www.chaiwithpabrai.com/transcripts.html"
print("NOTE: add url webpage and make sure the fetch url is correct, especially the base url!")

fetch(url, 1)
