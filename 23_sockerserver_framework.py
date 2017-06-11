#!/usr/bin/python
# -*- coding: utf-8 -*-

import SocketServer

class EchoHandler(SocketServer.BaseRequestHandler) :
    def handle(self) :
        print "Connection from: ", self.client_address
        data = 'dummy'

        while len(data) :
            data = self.request.recv(1024)
            self.request.send(data)
        print "Client left."

serverAddr = ("127.0.0.1", 4000)

server = SocketServer.TCPServer(serverAddr, EchoHandler)

server.serve_forever()
