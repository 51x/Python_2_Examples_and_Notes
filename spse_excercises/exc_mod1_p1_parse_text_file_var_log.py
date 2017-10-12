#!/usr/bin/python
# -*- coding: utf-8 -*-

# I am not reading /var/log/messages because it needs root.
# Therefore I chose another file which allows read for standard user: dpkg.log

# I am reading the fully installed packages from dpkg.log.

for line in open("/var/log/dpkg.log"):
    if " installed" in line:
        print line

# Other way of doing this
file_descriptor = open("/var/log/dpkg.log", "r")
for line in file_descriptor:
    if " installed" in line:
        #print line # prints full lines
        print line.split()[4]
file_descriptor.close()
