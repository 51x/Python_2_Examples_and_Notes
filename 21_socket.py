#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP - STREAM

tcpSocket.bind(("127.0.0.1", 8001)) # Should be passed as tuple

tcpSocket.listen(2) # 2 is the number of concurr to handle

(client, ( ip, port)) = tcpSocket.accept() # accept by default is blocking call

# client.send("Message to client.")
data = client.recv(2048)

print ip
print port
print data

