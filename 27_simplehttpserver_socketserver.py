#!/usr/bin/python
# -*- coding: utf-8 -*-

import SocketServer
import SimpleHTTPServer

class HttpRequestHandler (SimpleHTTPServer.SimpleHTTPRequestHandler) :
    def do_GET(self) :
        if self.path == "/admin" :
            self.wfile.write('This page is only for admins lol')
            self.wfile.write(self.headers)
        else :
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpServer = SocketServer.TCPServer(("", 7777), HttpRequestHandler)

print "It should listen on 7777."

httpServer.serve_forever()
