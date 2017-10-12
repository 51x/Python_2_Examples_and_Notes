#!/usr/bin/python
# -*- coding: utf-8 -*-

from scapy.all import sniff

def http_header(packet):
        http_packet=str(packet)
        if http_packet.find('GET') or http_packet.find('POST'):
                return GET_print(packet)

def GET_print(packet1):
    http_out = "\n".join(packet1.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n")) + "\n"
    return http_out

sniff(iface="eth0", prn=http_header, filter="tcp port 80", count=99)


# Another solution: pip install scapy-http
