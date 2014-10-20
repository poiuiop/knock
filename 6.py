#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

N = int(sys.argv[1])

list = []
for line in open("address.txt", "r"):
    list.append(line)

for val in list[-N:]:
    print val.strip()
