#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

#rawSocket.bind(("eth0", socket.htons(0x0800)))
rawSocket.bind(("enp0s31f6", socket.htons(0x0800)))

# layer 2 message, then data
# src mac / dst mac / eth type
inet_header = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb','\x08\x00') # 14 bytes

print len(inet_header)

rawSocket.send(inet_header + "Anything")
