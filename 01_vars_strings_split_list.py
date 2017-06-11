#!/usr/bin/python
# -*- coding: utf-8 -*-

var1 = "something"

print id(var1) # memory location
print hex(id(var1))
print var1.__repr__

var2 = r'raw, no new \n live'
print var2

var3 = """
multi
line
etc"""
print var3

var3 = unicode(var3) # unicode is used for internationalization, also dont forget line after #! !

print var1[1]

#var1[1]="f" # this won't work because python cant change only part of the memory of the string, just the whole

buf = "A" * 66
buf= "qwertyuiopaa"

print buf[5:10:2]

#vars = var1.split['a']

print var1.find('me')
print var1.split('me') # splits into list
print var1.split('me')[1] # split, then print list [1], starts from 0!
print var1.replace('some', 'any') # replaces, but it returns new object, not modifying original var1: immutable strings!

dis = "dis"
print "fug %s" % dis
l = "lol"
print "fug %s %s" % (dis, l)
print "fug %(dis)s %(l)s" % {"dis":"DIS","l":"lel"} # "s" is still required after the %() !


mylist = [1,2,3,4]
print len(mylist)
mylist2 = [1,2,3,[4,5]]
print len(mylist2)
print len(mylist2[3])
print mylist[1]
mylist.insert(2,"a") # etc
print mylist[2]
