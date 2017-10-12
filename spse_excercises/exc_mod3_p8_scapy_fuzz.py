#!/usr/bin/python
#-*- coding: utf-8 -*-

# Docs for interactive use
# https://scapy.readthedocs.io/en/latest/usage.html?highlight=fuzz#fuzzing
# Interactive example: >>> send(IP(dst="127.0.0.1")/fuzz(UDP()/NTP(version=4)),loop=1)

from scapy.all import sr1,IP,fuzz,UDP,NTP

target="127.0.0.1"
target="192.168.49.39"
while True:
    sr1(IP(dst=target)/fuzz(UDP()/NTP(version=4)),inter=4,timeout=1)
