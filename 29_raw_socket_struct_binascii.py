#!/usr/bin/python
# -*- coding: utf-8 -*-

# How to unpack raw packets

# Ethernet / IP / TCP / Application
#
# Ethernet header: 14 bytes
#
# 0         5 6       11 12      14 
# | EthDHost | EthSHost | EthType |
# |     Ethernet Packet Data      |

# 0         3 4    7 8              15 16           31
# | Version  | IDL  | Type of Service | Total Length |
# | Identification  |  Flags  |    Fragment Offser   | 
# | TTL |  Protocol |        Header Checksum         |
# |                 Source Address                   |
# |               Destination Address                |
# |        Options       |         Padding           |

# Note here when interpreting: Network Byte Order is indicated by first byte (eg. Big-Endian)

import socket
import struct
import binascii

# PF_PACKET for layer2 modifications
# For addresses: /usr/include/linux/if_ether.h
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

pkt = rawSocket.recvfrom(2048)

ethernetHeader = pkt[0][0:14]
eth_hdr = struct.unpack("!6s6s2s", ethernetHeader)

binascii.hexlify(eth_hdr[0]) # Take values and print out
binascii.hexlify(eth_hdr[1])
binascii.hexlify(eth_hdr[2])

ipHeader = pkt[0][14:34] # IP Header, 20 bytes

ip_hdr = struct.unpack("12s4s4s", ipHeader)

print "Source IP addr: " + socket.inet_ntoa(ip_hdr[1])
print "Destin IP addr: " + socket.inet_ntoa(ip_hdr[2])

# tcp header part

tcpHeader = pkt[0][34:54]
tcp_hdr = struct.unpack("!HH16s", tcpHeader)
