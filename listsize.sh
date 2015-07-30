#!/usr/bin/env bash
# List the sub-folder size under the parent folder

for i in `ls`
do
	echo `du -sh "$i"`
done
	
