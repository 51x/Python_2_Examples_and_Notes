#!/usr/bin/python
# -*- coding: utf-8 -*-

# Note: general solution posted multiple times.

from scapy.all import sniff, Dot11

aps = []

def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 8:
            if pkt.addr2 not in aps :
                aps.append(pkt.addr2)
                print "SSID found: %s " %(pkt.info)

sniff(iface="wlan0mon", prn=PacketHandler)
