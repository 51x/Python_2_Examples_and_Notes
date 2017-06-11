#!/usr/bin/python
# -*- coding: utf-8 -*-

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


import struct # For packing/unpacking binary data

print struct.pack("B", 1) # Packet as byte "B", little endian ordering here
print struct.pack("H", 1) # Etc...

print struct.pack(">H", 1) # Big endian ordering here because of ">"
print struct.pack("!L", 1) # Unsigned long, 4 bytes, network byte format "!"

struct.unpack("!L", "\x00\x00\x00\x01") # With the, computer unpacks "1"
