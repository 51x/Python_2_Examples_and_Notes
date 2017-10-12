#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
from threading import Thread
import time

def func1():
    print 'Function 1'
    time.sleep(2)
def func2():
    print 'Function 2'
    time.sleep(2)

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()
