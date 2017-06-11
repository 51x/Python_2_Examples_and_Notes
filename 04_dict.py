#!/usr/bin/python
# -*- coding: utf-8 -*-

myBio = {'name' : "unknown", 'age' : 666, 'hobby' : 'hacking'}

print myBio

myBio.has_key('hobby')

myBio.has_key('notinside')

myBio.values()

print myBio.get('age')

del myBio['age'] # Delete age
print myBio

dict_tuple = myBio.items() # into tuples
print dict_tuple

'name' in myBio

print myBio.has_key('hobby')

print dir(myBio)
help(myBio.update)
help(myBio.has_key)
