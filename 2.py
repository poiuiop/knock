#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

for line in open("address.txt", "r"):
    line = line.replace("\t", " ")
    print line.strip()
