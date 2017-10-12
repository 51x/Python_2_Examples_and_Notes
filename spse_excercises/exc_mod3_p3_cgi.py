#!/usr/bin/python
# -*- coding: utf-8 -*-

# - Python can be used as CGI script
# - There is cgi module
# - Flask can handle cgi scripts too

# https://docs.python.org/2/library/cgi.html
# http://cgi.tutorial.codepoint.net/hellow-world
# http://flask.pocoo.org/docs/0.12/deploying/cgi/

import cgitb
cgitb.enable(display=1)
# ..and cgi scripting

# Or cgi called directly by other app:
print "Content-Type: text/html"
print
print """\
<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
"""
