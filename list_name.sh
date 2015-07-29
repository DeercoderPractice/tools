#!/usr/bin/env bash

for x in /data3/users/cliu/dataset_backup/ImageNet-RCNN-Data-VOC2007/VOCdevkit/VOC2007/JPEGImages/*
do
        echo `basename $x`
        echo `basename $x` >> log.txt
done
