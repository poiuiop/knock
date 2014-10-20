#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

list = []
for line in open("address.txt", "r"):
    columns = line.split("\t")
    list.append(columns)

sorted_list = sorted(list, key=lambda x: x[1], reverse=True)

list1 = []
list2 = []
for val in sorted_list:
    if len(list2) > 0:
        if val[1] == list2[-1][1]:
            list2.append(val)
        else:
            list2 = sorted(list2, key=lambda x: x[0], reverse=True)
            list1 += list2
            list2 = []
            list1.append(val)
    else:
        list2.append(val)

for val in list1:
    print "\t".join(val).strip()
