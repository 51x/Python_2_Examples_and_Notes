#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python multi-thread syn scanner

#import thread
from threading import Thread
from scapy.all import *
import time

ip = "127.0.0.1"
ports = [20,21,22,23,53,80,139,443,445,5222,8080]

result=""

def scan(ip,cur_port):
    syn=IP(dst=ip)/TCP(dport=cur_port, flags="S")  # "sr1" is used as only one packet is needed to be received.
    answer = sr1(syn, verbose=0, timeout=2)
    print answer.summary()
    # For return values and communiaction between Threads: use queue

for port in ports:
    th = Thread(target=scan, args=(ip,port))
    th.start()
