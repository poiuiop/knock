#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

N = int(sys.argv[1])

c = 0
for line in open("address.txt", "r"):
    print line.strip()
    c += 1
    if c == N:
        break
