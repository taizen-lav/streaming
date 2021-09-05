#!/usr/bin/python
# -*- coding: utf-8 -*-

# urlticker.py by Link Valiant
# Copyright © 2021 Link Valiant
#
# This script displays various URLs as defined within this script in
#   defined time intervals and writes/rewrites it into a text file.  The
#   purprose of this is to use it a text overlay for streaming broadcast
#   applications such as OBS Studio, Streamlabs OBS, and OBSLive.
#

# Importing necessary libraries.
from os import setregid
import os.path
import time
from os.path import expanduser
from time import sleep

# Setting constant and initial variables.
FolderHome = os.path.expanduser("~")
FolderRest = "Studio/Streaming Shows/Video Games/Overlays"
FileName = "urlticker.txt"
FilePath = os.path.join(FolderHome, FolderRest, FileName)
FetchCount = 0
global StrURLPrefix
global StrWebsite
global StrTwitter
global StrFB
global StrIG
global ArrTwitterSplit
global ArrFBSplit
global ArrIGSplit
global StrURLWebsite
global StrURLTwitter
global StrURLFB
global StrURLIG
global StrShowTwitter
global StrShowFB
global StrShowIG
StrURLPrefix = "HTTPS://"
StrWebsite = "TAIZEN.ORG\n"
StrTwitter = "TWITTER.COM/TAIZENORG"
StrFB = "FACEBOOK.COM/TAIZENORG"
StrIG = "INSTAGRAM.COM/TAIZENORG"
StrURLWebsite = StrURLPrefix + StrWebsite
StrURLTwitter = StrURLPrefix + StrTwitter
StrURLFB = StrURLPrefix + StrFB
StrURLIG = StrURLPrefix + StrIG
StrShowTwitter = StrURLWebsite + StrURLTwitter
StrShowFB = StrURLWebsite + StrURLFB
StrShowIG = StrURLWebsite + StrURLIG
ArrTwitterSplit = list(StrShowTwitter)
ArrFBSplit = list(StrShowFB)
ArrIGSplit = list(StrShowIG)

# Creating functions for placing various URLs in the text file.
def ShowWebsiteOnly():
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsite)
    sleep(299)

def ShowTwitter():
    sleep(1)
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrShowTwitter)
    sleep(5)
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsite)

def ShowFB():
    sleep(1)
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrShowFB)
    sleep(5)
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsite)

def ShowIG():
    sleep(1)
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrShowIG)
    sleep(5)
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsite)

# Calling the function repeatedly once every second until the script is stopped by.
#   way of a keyboard initiated break (CTRL+C on Windows and Linux,^C on macOS).
while True:
    ShowTwitter()
    ShowFB()
    ShowIG()
    ShowWebsiteOnly()
