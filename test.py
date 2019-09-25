#!/usr/bin/env python3
# coding: utf-8

from subprocess import run
from subprocess import Popen
import csv
import sys

def launchProc(commands):
    output = {}

    currentProc = commands[0]
    output['clientName'] = currentProc
    print('starting', output['clientName'])
    Popen(commands[0:]) # capture PID here!

    currentPID = run(['pidof', '-s', currentProc], capture_output=True) # wont be needed
    currentPIDtoStr = currentPID.stdout.decode('utf-8').strip()
    output['clientPID'] = currentPIDtoStr
    print('client:', output['clientName']+',', 'client PID:', output['clientPID'])

    print('waiting for', output['clientName'], 'to open')
    windowID = run(['xdotool', 'search', '--sync', '--onlyvisible', '--class', currentProc], capture_output=True) # NOT ROBUST - BUG IF instance already exists
    windowIDtoStr = windowID.stdout.decode('utf-8').strip()
    output['windowID'] = windowIDtoStr
    print('window ID:', output['windowID'])
    windowName = run(['xdotool', 'getwindowname', windowIDtoStr], capture_output=True)
    output['windowName'] = windowName.stdout.decode('utf-8').strip()
    print('window title:', output['windowName'])
    
    print(output['clientName'], 'started', '\n')
    return output


def launchSession(sessionFileName):
    print('Starting Session:', sessionFileName,'\n')
    output = []

    with open(sessionFileName) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=' ')
        for row in csvReader:
            currentProcessDict = launchProc(row)
            output.append(currentProcessDict)
    print('all processes started')
    return output


def printSession(aList):
    for i in range(len(aList)):
        print(aList[i])


##############################################################################

 
def main():
    
    launch = launchSession(sessionFileName)
    printSession(launch)


##############################################################################
 
if __name__ == "__main__":
    main()