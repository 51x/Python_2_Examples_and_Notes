#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def child_proc():
    print "I am the child with PID: %d" % os.getpid()
    print "Child exits."

def parent_proc():
    print "I am the parent with PID %d" % os.getpid()

    childpid = os.fork() # Replica of the parent, runs after

    if childpid == 0: # Runs if child is created and returned 0
        print "We have entered a child process."
        child_proc()
    else:
        print "We have entered the parent process."
        print "Our child's PID is: %d" % childpid

#    while True:
#        pass

parent_proc()
