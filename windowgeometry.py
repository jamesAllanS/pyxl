#!/usr/bin/env python3
from subprocess import run
import clientwindow

class WindowGeometry:
    def __init__(self, windowClient):
        geometry = run(['xdotool', 'getwindowgeometry', '--shell', windowClient.WINDOW_ID ]).splitline()

    def __str__(self):
        return 'a string'

    # @property
    # def WINDOW_ID(self):
    #     return self._WINDOW_ID

