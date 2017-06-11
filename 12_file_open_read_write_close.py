#!/usr/bin/python
# -*- coding: utf-8 -*-

# Note, buffering in open() and byte_count in read() can be set

fdesc = open("/tmp/any.txt", "w")
print fdesc
for count in range(0,99):
    fdesc.write(str(count) + "\n")
fdesc.close


fdesc = open("/tmp/any.txt", "a")
for count in range(0,999):
    fdesc.write(str(count) + "\n")
fdesc.close


fdesc = open("/tmp/any.txt", "r")
for line in fdesc.readlines() :
    print line.strip()
fdesc.close


import os
os.rename("/tmp/any.txt", "/tmp/nyuu.txt")
#os.remove("/tmp/any.txt")
# os.rmdir("/tmp/emptydir") # ... etc
