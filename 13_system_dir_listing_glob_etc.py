#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

os.getcwd()

os.mkdir("NewDir")

os.rmdir("NewDir")

os.listdir(".")  # List
os.listdir("/")

for item in os.listdir(".") :
    if os.path.isfile(item) :
        print item + " is a file."
    elif os.path.isdir(item) :
        print item + " is a dir."
    else :
        print "couldn't identify."


import glob

for item in glob.glob(os.path.join(".","*.py")) :
    print item
