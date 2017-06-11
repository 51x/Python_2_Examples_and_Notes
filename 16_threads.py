#!/usr/bin/python
# -*- coding: utf-8 -*-

# "Global Interpreter Lock" - Only one thread :(
# Don't expect more.

import thread
import time

def worker_thread(id) :

    print "Thread ID start: %d" % id

    count = 1

    while True :
        print "Thread ID: %d with value %d" % (id, count)
        time.sleep(2)
        count += 1

for i in range(5) :
    thread.start_new_thread(worker_thread, (i,))

print "Main thread goes with an infinite loop."

while True :
    pass
