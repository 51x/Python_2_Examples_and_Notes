#!/usr/bin/python
# -*- coding: utf-8 -*-

def funkcion():
    print "done"

funkcion()


def funkcion2(vvv):
    print vvv

funkcion2("vav")


def funkcion3(vvv):
    return vvv

print funkcion3("vuv")
out = funkcion3("viv")
print out


import sys # take argument from command line, handle if its not given
def fromsys(this):
    print this

thisinto = ""
try:
    thisinto = sys.argv[1]
except:
    pass
fromsys(thisinto)
