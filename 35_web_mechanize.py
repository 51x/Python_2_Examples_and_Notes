#!/usr/bin/python
# -*- coding: utf-8 -*-

import mechanize

br = mechanize.Browser()
br.open('https://www.gentoo.org/donate')


# Dump all forms from gentoo.org/donate
for form in br.forms():
    print form

br.select_form(nr=0)  # 0 because of first form - it references to the first form.
br.form['amount'] = 'thanks!'

br.submit() # Done, submitted!
# Better idea is to implement it with: https://searx.me/


# Print list of links
for link in br.links():
    print link.url + ' : ' + link.text
