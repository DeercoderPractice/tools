#!/usr/bin/env python

import os

PATH = "./"

for path in os.listdir(PATH):
	print str(path)
	if os.path.isfile(path):
		continue	
	for f in os.listdir(path):
		str(f)	
		if f.endswith("tar.gz"):
			os.system("tar xvzf "+os.path.join(PATH, path, f) + " -C "+os.path.join(PATH, path))
