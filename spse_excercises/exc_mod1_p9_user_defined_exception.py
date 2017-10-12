#!/usr/bin/python
# -*- coding: utf-8 -*-

# Derive from Exception class (inheritance)
class MyError(Exception):
    def __init__(self, value):
        self.value = "...oooops!"
 
try:
    raise(MyError(3*2))

except MyError as error:
    print('User defined exception says: ',error.value)
