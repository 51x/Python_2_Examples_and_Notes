#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

rawSocket.bind(("eth0", socket.htons(0x0800)))

# layer 2 message, then data
# src mac / dst mac / eth type
# arpaket = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb','\x08\x60') # 14 bytes

# ARP --> dst mac / src mac / type 8006 / |ARP ~ hw type / proto type / hw addr / proto addr / operation code / 
# / src hw addr / src proto addr / target hw addr / target proto addr | / Padding / CRC - note here is that padding and crc is not mandatory :)
# https://www.netometer.com/qa/arp.html

arpaket = struct.pack("!6s6s2s2s2s1s1s2s6s4s6s4s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x06','\x00\x01','\x08\x00','\x06','\x04','\x00\x01','\xcc\xcc\xcc\xcc\xcc\xcc','\xc0\xa8\x06\x06','\xdd\xdd\xdd\xdd\xdd\xdd','\xc0\xa8\x06\x07')

rawSocket.send(arpaket)

#print "Length of the ARP packet sent: " + str(len(arpaket))

#arpreply = struct.pack("!6s6s2s2s2s1s1s2s6s4s6s4s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x06','\x00\x01','\x08\x00','\x06','\x04','\x00\x02','\xcc\xcc\xcc\xcc\xcc\xcc','\xc0\xa8\x06\x06','\xdd\xdd\xdd\xdd\xdd\xdd','\xc0\xa8\x06\x07')
#rawSocket.send(arpreply)
