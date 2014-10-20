#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

list = []
for line in open("address.txt", "r"):
    columns = line.split("\t")
    if columns[0] in list:
        pass
    else:
        list.append(columns[0])

print len(list)
