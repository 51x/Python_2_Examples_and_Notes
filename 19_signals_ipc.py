#!/usr/bin/python
# -*- coding: utf-8 -*-

import signal

def ctrlc_handler(signum, frm) :
    print "Can't ctrlc this."

print "Signal handler..."
signal.signal(signal.SIGINT, ctrlc_handler)
print "Done."

while True:
    pass
