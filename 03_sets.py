#!/usr/bin/python
# -*- coding: utf-8 -*-

setA = set([1,2,3,3,2])

setB = set([3,4,5])

setA|setB # Union

setA&setB # Intersection

setA-setB # In set A, but not set B

setB-setA # In set B, but not set A

var = setA&setB 
print var
