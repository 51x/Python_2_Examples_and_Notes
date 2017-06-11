#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('/System/Library/Frameworks/CoreLocation.framework/Support/timezone.db')

cur = conn.cursor()

for zone in cur.execute("select * from Names") :
    print zone
