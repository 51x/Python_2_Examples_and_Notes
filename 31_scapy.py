#!/usr/bin/python
# -*- coding: utf-8 -*-

#import scapy
from scapy.all import sniff

# from intractive mode: conf, ls(), ls(IP)
# note" conf.route.add(host="192.168.2.4", gw="192.168.2.5") / conf.route.resync() / etc...

pkts = sniff(iface="enp0s31f6", count=5)

print pkts[0]
print pkts[0].show

print hexdump(pkts[1])

# wrpcap("test.pcap", pkts)  # write the packets into pcap file
# read_pkts = rdpcap("test.pcap")  # read pcap
# read_pkts[0]  # print pcap

pkts_filtered = sniff(iface="enp0s31f6", filter="icmp", count=5) # BPS filters
print pkts_filtered[1]

pks_live = sniff(iface="enp0s31f6", filter="icmp", count=2, prn=lambda x: x.summary())


# icmp_str = str(pkts[1])
# recon = Ether(icmp_str)
# print recon  # this is more for fun  / converting pkts to str and back using Ether

# newPkt = export_object(icmp_str)  # packet into base64
# import_object(newPkt)  # packet from base64
# Ether(newPkt)  # and so on... :)
