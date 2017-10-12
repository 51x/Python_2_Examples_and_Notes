#!/usr/bin/python
# -*- coding: utf-8 -*-

# Thanks: https://www.troyfawkes.com/learn-python-multithreading-queues-basics/

from Queue import Queue
from threading import Thread

def do_work(q):
  while True:
    print q.get()
    q.task_done()

q = Queue(maxsize=0)
num_threads = 5

for i in range(num_threads):
  worker = Thread(target=do_work, args=(q,))
  worker.setDaemon(True)
  worker.start()

for a in range (10):
  for b in range(50):
    q.put(a+b*50)
  q.join()
  print "Work " + str(y) + ": done."
