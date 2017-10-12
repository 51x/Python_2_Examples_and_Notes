#!/usr/bin/python
# -*- coding: utf-8 -*-

import multiprocessing
from scapy.all import *

ip = "127.0.0.1"
ports = [20,21,22,23,53,80,139,443,445,5222,8080]

def worker(ip,cur_port):
    syn=IP(dst=ip)/TCP(dport=cur_port, flags="S")  # "sr1" is used as only one packet is needed to be received.
    answer = sr1(syn, verbose=0, timeout=2)
    print answer.summary()
    return

if __name__ == '__main__':
    jobs = []
    for port in ports:
        p = multiprocessing.Process(target=worker, args=(ip,port))
        jobs.append(p)
        p.start()
