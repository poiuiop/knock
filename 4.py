#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

file1 = open("col1.txt", "r")
file2 = open("col2.txt", "r")

list = []
for line in file1:
    list.append([line.strip()])

c = 0
for line in file2:
    list[c].append(line.strip())
    c += 1

for val in list:
    print "\t".join(val)
