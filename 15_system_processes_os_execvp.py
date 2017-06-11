#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

os.execvp("ping", ["ping", "127.0.0.1", "-c", "4"])
