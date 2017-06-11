#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP - STREAM

tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(("127.0.0.1", 8001)) # Should be passed as tuple

tcpSocket.listen(2) # 2 is the number of concurr to handle

(client, ( ip, port)) = tcpSocket.accept() # accept by default is blocking call

data = "empty"

while len(data) :
    data = client.recv(2048)
    print "Client sent: ",data
    client.send(data)

client.close()
tcpSocket.close()

