#!/usr/bin/env bash

for i in `ls`
do
	echo `du -sh "$i"` >> log.txt
done

## in order to keep the original format, I need to add " " outside the result of sort
echo  "`sort -h log.txt`"
rm log.txt
	
