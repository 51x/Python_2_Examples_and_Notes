#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'ok'

if __name__ == '__main__':
    app.run('127.0.0.1',4001)
