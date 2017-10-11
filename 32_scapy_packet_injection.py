#!/usr/bin/python
# -*- coding: utf-8 -*-

#import scapy
from scapy.all import Ether, IP, ICMP, TCP, sr, sr1

pkt = IP(dst="gentoo.org")  # Simple packet creation
#print pkt.show()

pkt = IP(dst="gentoo.org")/ICMP()/"Not-Vivek was here"  # ICMP packet creation with message

sr1(pkt)



# More tricks / tips

# sendp(Ether()/IP(dst="gentoo.org")/ICMP()/"any", iface="enp0s31f6", loop=1, inter=1) # Sending on layer 2 level, plus loop, but be carefule with that : ) + this is interactive command!


# Layer 3 send and receive: sr() sr1()
# Layer 2 send and receive: srp() srp1()

#srp1(Ether()/IP(dst="gentoo.org", ttl=22)/ICMP/"any")

#sr(IP(dst="gentoo.org", ttl=22)/ICMP()/"any")
#response, no_response = _
#print response[0]  # print answer


#r1(IP(dst="gentoo.org"), timeout=4)

