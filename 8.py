#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

list = []
for line in open("address.txt", "r"):
    columns = line.split("\t")
    list.append(columns)

sorted_list = sorted(list, key=lambda x: x[1])

for val in sorted_list:
    print "\t".join(val).strip()
