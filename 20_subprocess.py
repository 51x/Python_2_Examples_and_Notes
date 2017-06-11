#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

subprocess.call(['ps', 'aux']) # Just exec.

lines = subprocess.check_output(['ls']) # Get output into vari

print type(lines)

print lines


# Popen for handle stds

handle = subprocess.Popen("ls", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)  # True here can be a sec issue.

handle.stdout.read()
