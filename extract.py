#!/usr/bin/env python

handler = open("pinpow1800MW.out", "r+")
lines = handler.readlines()

output = open("data.out", "w+")

writing = False

for line in lines:
#    print line
    if "Material powers" in line:
        writing = True
    elif "--------------------------------------------------------------" in line:
        if writing == True:
            output.write(line)
            output.write("\n")
        writing = False

    if writing == True:
        output.write(line)

handler.close()
output.close()
