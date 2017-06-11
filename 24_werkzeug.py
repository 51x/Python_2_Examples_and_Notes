#!/usr/bin/python
# -*- coding: utf-8 -*-

from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response('ok')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
