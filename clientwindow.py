#!/usr/bin/env python3
from subprocess import run

class ClientWindow:
    def __init__(self, aCompletedProcess):
        self._CLIENT = aCompletedProcess.args[0]
        # grab window ID here with helper method. Throw if cannot find window ID at all.
        self._WINDOW_ID = __getWindowID(aCompletedProcess)
        # self.title = run(['xdotool', 'getwindowname', windowID], capture_output=True).stdout.decode('utf-8').strip()
        self.proc = aCompletedProcess

    def __str__(self):
        return 'Client: ' + self.CLIENT + ',' + \
               'Window Title: ' + self.title + '\n' + \
               'PID: ' + self.PID + ',' + \
               'Window ID: ' + self.WINDOW_ID + '\n'


    @property
    def WINDOW_ID(self):
        return self._WINDOW_ID
    @property
    def CLIENT(self):
        return self._CLIENT
    @property
    def PID(self):
        return self._PID


    def setTitleToClientName(self):
        """Sets the window title to that of the client (no path etc)"""
        self.title = self.CLIENT
        run(['xdotool', 'set_window', '--name', self.title ], capture_output=True).stdout.decode('utf-8').strip()
        
    def getClientPID(self):
        """Returns a client's PID as an int"""
        return self.proc.pid


