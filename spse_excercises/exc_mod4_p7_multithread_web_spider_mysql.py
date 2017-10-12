#!/usr/bin/python
# -*- coding: utf-8 -*-

# A project for parsing a website, then inserting the data into mysql and serving the mysql data through socket http server.
# All is managed through multithreading.
#
# If the mysql table does not exist, this script will create it, but the database and user should be created in advance!

import multiprocessing
import MySQLdb as mdb
from lxml import html
import requests
import time
from time import gmtime, strftime
import SocketServer
import SimpleHTTPServer

# Proxy
proxies = {
    'http': "socks5://127.0.0.1:9050",
    'https': "socks5://127.0.0.1:9050"}

# Spidering
def spidering_l(proc):
    while True:
        # Sprudeling
        # Get the page
        page = requests.get('https://riskdiscovery.com/'), proxies=proxies)
        tree = html.fromstring(page.content)
        # Vars
        state_time = strftime("%Y%m%d%H%M%S", gmtime())
        spider_list_link = []
        spider_list_text = []
        spider_state = str(state_time)
        # Loop around links //a
        for link in tree.xpath('//a'):
            spider_list_link.append(link.get('href'))
            spider_list_text.append(link.text)
        # MySQL
        con = ""
        try:
            con = mdb.connect('localhost', 'someuser', 'somepass', 'news_parse')
            cur = con.cursor()
            zp = zip(spider_list_link,spider_list_text)
            for zipo in zp:
                link_c = zipo[0]
                text_c = zipo[1]
                cur.execute("CREATE TABLE IF NOT EXISTS news_data ( id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, state_time VARCHAR(30) NOT NULL, link VARCHAR(512) NOT NULL, text VARCHAR(1024))")
                con.commit()
                cur.execute("INSERT INTO news_data (id, state_time, link, text) VALUES (NULL, %s, %s, %s)",(state_time,link_c,text_c))
                con.commit()
        except mdb.Error, e:
            print e
        finally:
            if con:
                con.close()
        time.sleep(60)
    return


# Serve HTTP
class HttpRequestHandler (SimpleHTTPServer.SimpleHTTPRequestHandler) :
    def do_GET(self) :
        last_list=""
        if self.path == "/":
            try:
                con = mdb.connect('localhost', 'someuser', 'somepass', 'news_parse')
                cur = con.cursor()
                cur.execute("SELECT * FROM news_data")
                data = cur.fetchall()

                # Unique identifiers (that's why it's a set)
                sset=set()
                for x in data:
                    sset.add(x[2])
                for xx in sset:
                    last_list = last_list + xx + '\n'

# Note, playing with sets
#                final_out = []
#                for xx in sset:
#                    curr_st = xx
#                        for x in data:
#                            if curr_st == x[1]:
#                                final_out.(x[2][3])


            except mdb.Error, e:
                print e
            finally:
                if con:
                    con.close()
            self.wfile.write('The latest news from the past 72 hours: \n' + str(last_list))
            
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

def serve_http(proc):
    SocketServer.TCPServer.allow_reuse_address = True
    httpServer = SocketServer.TCPServer(("127.0.0.1", 8080), HttpRequestHandler)
    print "It should listen on 8080."
    httpServer.serve_forever()

    pass


if __name__ == '__main__':

    jobs = []

    # Start spidering
    mp = multiprocessing.Process(target=spidering_l, args=(0,))
    jobs.append(mp)
    mp.start()

    # Serve the results on HTTP
    hp = multiprocessing.Process(target=serve_http, args=(0,))
    jobs.append(hp)
    hp.start()
