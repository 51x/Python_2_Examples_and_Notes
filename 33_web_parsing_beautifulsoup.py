#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# GET with requests, then parse with BeautifulSoup
r = requests.get("https://gentoo.org/")
print r.content
bt = BeautifulSoup(r.content, "lxml")  # It's recommended to use LXML, not the default html parser.
print bt.title
print bt.title.string


# Find all metatags
allMetaTags = bt.find_all('meta')
print allMetaTags


allMetaTags = bt.find_all('meta')
print allMetaTags[2]

#allMetaTags = bt.find_all('meta')
#print allMetaTags[0]['content']  # Works in video, not here. wat?


# Print all links from the site
allLinks = bt.find_all('a')
print len(allLinks) # How many links do we have?
#print allLinks[1]
print allLinks[4]['href']
#print allLinks[1].string


# Print all text output, could be great for password list generations
print bt.get_text()


#Print all links
for link in allLinks:
    print link['href']


# print bt.meta.next.next.next.next.next.next  # Don't.
