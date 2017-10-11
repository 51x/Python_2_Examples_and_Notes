#!/usr/bin/python
# -*- coding: utf-8 -*-

# Place this file into PyCommands directory to use with Immunity Debugger.

import immlib

DESC = "This will be the Description in ID."

def main(args):

    imm = immlib.Debugger() # This is what we attach to.

    imm.log("Write that into ID log window!")

    imm.updateLog() # Any pending line will be printed immediately!


    td = imm.createTable("Any name", ['PID', 'Name', 'Path', 'Services'])

    psList = imm.ps()
    for process in psList:
        td.add(0, [ str(process[0], process[1], process[2], str(process[3]))])

    return "Welcome to ID Scripting."
