#!/usr/bin/python
# -*- coding: utf-8 -*-

import SocketServer

class EchoHandler(SocketServer.BaseRequestHandler) :
    def handle(self) :
        print "Connection from: ", self.client_address
        data = 'dummy'

        while len(data) :
            data = self.request.recv(1024)
            self.request.send("""HTTP/1.0 200 OK
Content-Type: text/html

<html>
<head>
<title>Latest news from the past 24 hours</title>
</head>
<body>Wooooo</body>
</html>
""")
        print "Client left."

serverAddr = ("127.0.0.1", 8080)

server = SocketServer.TCPServer(serverAddr, EchoHandler)

server.serve_forever()
