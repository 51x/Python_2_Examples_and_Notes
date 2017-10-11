#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# GET with requests, then parse with BeautifulSoup
#r = requests.get("https://gentoo.org/")
#print r.content


r = requests.get("http://securitytube.net/video/3000")

bs = BeautifulSoup(r.content, "lxml")  # It's recommended to use LXML, not the default html parser.
print bs.title

videoLink = bs.find('iframe', {'title' : 'YouTube video player'})
print videoLink
print videoLink['src']

# To Be Continued !

