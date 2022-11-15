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
global StrHandle
global StrURLWebsite
global StrURLWebsiteAndPrefix
global StrURLTwitter
global StrURLFB
global StrURLIG
global StrShowTwitter
global StrShowFB
global StrShowIG
global StrShowInsideDharma
StrURLPrefix = "HTTPS://"
StrWebsite = "TAIZEN.ORG\n"
StrTwitter = "TWITTER.COM/"
StrFB = "FACEBOOK.COM/"
StrIG = "INSTAGRAM.COM/"
StrHandle = "TAIZENORG"
StrInsideDharma = "INSIDEDHARMA.ORG"
StrURLWebsite = StrURLPrefix + StrWebsite
StrURLWebsiteAndPrefix = StrURLWebsite + StrURLPrefix
TickerCount = 0

# Creating functions for placing various URLs in the text file.
def ShowWebsiteOnly():
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsite)
    sleep(300)

def ShowPrefix():
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsiteAndPrefix)
    sleep(2)

def ShowTwitter():
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsiteAndPrefix + StrTwitter)
    sleep(2)
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsiteAndPrefix + StrTwitter + StrHandle)
    sleep(6)
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsiteAndPrefix + StrTwitter)
    sleep(2)

def ShowFB():
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsiteAndPrefix + StrFB)
    sleep(2)
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsiteAndPrefix + StrFB + StrHandle)
    sleep(6)
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsiteAndPrefix + StrFB)
    sleep(2)

def ShowIG():
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsiteAndPrefix + StrIG)
    sleep(2)
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsiteAndPrefix + StrIG + StrHandle)
    sleep(6)
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsiteAndPrefix + StrIG)
    sleep(2)

def ShowInsideDharma():
    with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsiteAndPrefix + StrInsideDharma)
    sleep(6)

# Calling the function repeatedly once every second until the script is stopped by.
#   way of a keyboard initiated break (CTRL+C on Windows and Linux,^C on macOS).
print ("URL ticking has begun.")
with open(FilePath, 'w', encoding='utf-8') as ThisFile:
        ThisFile.write(StrURLWebsite)
sleep(5)

while True:
    ShowPrefix()
    ShowTwitter()
    ShowPrefix()
    ShowFB()
    ShowPrefix()
    ShowIG()
    ShowPrefix()
    ShowInsideDharma()
    ShowPrefix()
    ShowWebsiteOnly()
    TickerCount += 1
    print ("--> " + str(TickerCount) + " URL ticks.")
