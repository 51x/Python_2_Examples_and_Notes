#!/usr/bin/python
# -*- coding: utf-8 -*-

import mechanize

# Note: mechanize takes care of cookies.

br=mechanize.Browser()

br.open('http://student.securitytube.net/login/index.php')

for form in br.forms():
    print form

br.select_form(nr=0)

br.form['username'] = 'demo-user'
br.form['password'] = 'demouser1]M'  # It won't work ;)

br.submit()
print br.response().read

for link in br.links():
    print link.url + ' + ' + link.text

# It's different url now, just for example:
#new_link = br.click_link(text='moodle[IMG]Change Password')
#br.open(new_link)
#print br.response().read()

#for form in br.forms():
#    print form
