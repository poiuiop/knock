#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

file = open("col2.txt", "r")

dict = {}
for line in file:
    if line in dict:
        dict[line] += 1
    else:
        dict[line] = 1

sorted_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)

for val in sorted_list:
    print str(val[1]) + " " + val[0].strip()
