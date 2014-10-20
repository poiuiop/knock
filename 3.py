#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

file1 = open("col1.txt", "w")
file2 = open("col2.txt", "w")

for line in open("address.txt", "r"):
    columns = line.split("\t")
    file1.write(columns[0].strip() + "\n")
    file2.write(columns[1].strip() + "\n")
