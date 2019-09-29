#!/usr/bin/env python3
from subprocess import Popen, run
import clientwindow
import csv
import sys
import configparser

############## pyxl - Python X application launcher / manager #######################


 
def writeConfigFile(aConfigFile, sessionFileName):
    config = configparser.ConfigParser()

    config['DEFAULT'] = {'last_session': 'test.txt',
                         'last_run_date': 'never'}
    config['session_info'] = {}
    config['session_info']['last_session'] = sessionFileName
    config['session_info']['last_run_date'] = time.strftime('%Y-%m-%d')
    with open(aConfigFile, 'w') as configfile:
        config.write(configfile)
 

def getSessionFileName():
    configFile = '.pyxl'
    # need to check if file exists etc.
    if len(sys.argv) > 1:
        sessionFileName = 'savedSessions/' + sys.argv[1]
    else:
        sessionFileName = getSessionFileNameFromConfig(configFile)
    writeConfigFile(configFile, sessionFileName)
    return sessionFileName

    
def getSessionFileNameFromConfig(aConfigFile):

    config = configparser.ConfigParser()
    config.read(aConfigFile)
    sessionToLoad = config.get('session_info', 'last_session')
    if (sessionToLoad == None) or (sessionToLoad == ''):
        return config.get('DEFAULT', 'last_session')
    else:
        return config.get('session_info', 'last_session')
    

def __getWindowID(aCompletedProcess):
    """may return more than one window ID,
    constructor for this class must not run if this function fails to find window id"""
    clientPID = aCompletedProcess.pid
    client = aCompletedProcess.args[0]
    windowID = run(['xdotool', 'search', '--onlyvisible', '--pid', clientPID], capture_output=True).stdout.decode('utf-8').strip()
    # may not work in all cases as an x window won't always supply its PID
    if (windowID == '' or windowID == None):
        # try something else
        windowID = run(['xdotool', 'search', '--onlyvisible', '--class', client], capture_output=True).stdout.decode('utf-8').strip()
    elif expression:
    #    find another way
        pass
    else:
        raise AttributeError('unable to locate window ID for process', client)
    return windowID

def launchProc(commands):
    proc = Popen(commands)
    try:
        __getWindowID(proc)
    except Exception as e:
        print(e)
    return proc

##############################################################################

def main():
    # launchSession()
    # wait for window
    # writeConfigFile('.pyxl', 'test2.txt')
    print(getSessionFileName())

 
##############################################################################
 
if __name__ == "__main__":
    main()