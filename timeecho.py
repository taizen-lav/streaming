#!/usr/bin/python
# -*- coding: utf-8 -*-

# timeecho.py by Link Valiant
# Copyright © 2021 Link Valiant
#
# This script gathers the current time as reported by the operating
#   system and writes/rewrites it into a text file.  The purprose
#   of this is to use it a text overlay for streaming broadcast
#   applications such as OBS Studio, Streamlabs OBS, and OBSLive.
#

# Importing necessary libraries.
import os.path
import time
from os.path import expanduser
from time import sleep

# Setting constant and initial variables.
FolderHome = os.path.expanduser("~")
FolderRest = "Studio/Streaming Shows/Video Games/Overlays"
FileName = "timeecho.txt"
FilePath = os.path.join(FolderHome, FolderRest, FileName)
FetchCount = 0

# Creating function for collecting the current time and placing it in the text file.
#   Dynamically set variable are defined here.
def GetTime():
    Now = time.localtime()
    TimeNow = (time.strftime("%a,%b%d,%y\n%I:%M %p %Z", Now)).upper()
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(TimeNow)
    print (TimeNow)

# Calling the function repeatedly once every second until the script is stopped by.
#   way of a keyboard initiated break (CTRL+C on Windows and Linux,^C on macOS).
while True:
    FetchCount += 1
    print ("--> " + str(FetchCount) + " time echoes.")
    GetTime()
    sleep(1)
