#!/usr/bin/python
# -*- coding: utf-8 -*-

# timedown.py by Link Valiant
# Copyright © 2021 Link Valiant
#
# This script counts down minutes and seconds.  It uses nothing
#   fancy.  It simply takes argument integers for the minute
#   and second values and places them in a formatted text file
#   every second to use it a text overlay for streaming broadcast
#   applications such as OBS Studio, Streamlabs OBS, and OBSLive.
#

# Importing necessary libraries.
import argparse
import os.path
from os.path import expanduser
from time import sleep

# Collect information from command line parameters.
parser = argparse.ArgumentParser()
parser.add_argument("-m", "-minutes", help="The number of minutes (required).", type=int)
parser.add_argument("-s", "-seconds", help="The number of seconds (required).", type=int)
args = parser.parse_args()

# Setting constant and initial variables and display.
FolderHome = os.path.expanduser("~")
FolderRest = "Studio/Streaming Shows/Video Games/Overlays"
FileName = "timedown.txt"
FilePath = os.path.join(FolderHome, FolderRest, FileName)
global IntMinutes
global IntSeconds
global StrHourUnits
global StrMinuteUnits
global StrSecondUnits
global StrOutput1
global StrOutput2
global StrOutput
IntMinutes = args.m
IntSeconds = args.s

# Creating function for checking the time variables for zeroes.  If the 
#    seconds are zero, it'll check for whether or not the minutes variable
#    is also zero.  The results will depend on what us to be displayed in
#    the text file.  This will also determine when the script ends.
def CheckForZero():
    global IntMinutes
    global IntSeconds
    if IntSeconds == 0:
        if IntMinutes == 0:
            StrOutput = "THE SHOW WILL\nCOMMENCE VERY\nSHORTLY."
            with open(FilePath, 'w', encoding='utf-8') as ThisFile:
                ThisFile.write(StrOutput)
            # print (StrOutput + "\n\n")
            exit(0)
        else:
            IntSeconds = 60

# Creating function for counting down the set time values.
def CountDown():
    global IntMinutes
    global IntSeconds
    if IntSeconds == 60:
        IntMinutes -= 1
    IntSeconds -= 1

# Creating function builds the properly formatted output and places it
#    into the text file.  Dynamically set variables are defined here. 
def MakeOutput():
    if IntMinutes < 10 and IntMinutes > 0 :
        StrMinutes = " " + str(IntMinutes)
    elif IntMinutes == 0:
        StrMinutes = ""
    else:
        StrMinutes = str(IntMinutes)
    
    if IntSeconds < 10:
        StrSeconds = " " + str(IntSeconds)
    else:
        StrSeconds = str(IntSeconds)
    
    if IntMinutes == 1:
        StrMinuteUnits = " MINUTE  &\n"
    elif IntMinutes == 0:
        StrMinuteUnits = ""
    else:
        StrMinuteUnits = " MINUTES &\n"

    if IntSeconds == 1:
        StrSecondUnits = " SECOND"
    else:
        StrSecondUnits = " SECONDS"
    
    StrOutput2 = StrMinutes + StrMinuteUnits + StrSeconds + StrSecondUnits
    StrOutput = StrOutput1 + StrOutput2

    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrOutput)

# Putting the initial output into the text file.
with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write("")
StrOutput1 = "THE SHOW WILL\nCOMMENCE IN:\n\n"
CheckForZero()
CountDown()
MakeOutput()
sleep(1)

# Calling the function repeatedly once every second until the script is stopped
#    when it checks for zeroes and finds both the minutes and seconds values are
#    zero and it has changed output one last time.
while True:
    CheckForZero()
    CountDown()
    MakeOutput()
    sleep(1)
