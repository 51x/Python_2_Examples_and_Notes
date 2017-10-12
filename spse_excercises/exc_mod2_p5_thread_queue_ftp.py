#!/usr/bin/python
# -*- coding: utf-8 -*-

from Queue import Queue
from threading import Thread
import ftplib

# Random list from random hosts
# For complete excercie, 10 ftp sites... but it's working already at least.
ftp_list = ["210.222.148.126","81.177.6.66", "69.168.79.145", "79.24.166.214", "103.209.143.86"]


def do_work(q,cur_ftp):
  while True:
    ftp = ftplib.FTP(cur_ftp)
    ftp.login("anonymous", "")
    data = []
    ftp.dir(data.append)
    ftp.quit()
    for line in data:
        print "-", line

    q.task_done()

q = Queue(maxsize=0)
num_threads = 5

for cur_ftp in ftp_list:
  worker = Thread(target=do_work, args=(q,cur_ftp))
  worker.setDaemon(True)
  worker.start()

# Wait until threads finish
for x in range(50):
  q.put(x)
q.join()
