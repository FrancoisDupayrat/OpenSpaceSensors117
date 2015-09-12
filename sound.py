#!/usr/bin/env python 

import mraa
import sys
import time

# A0 on Grove Shield
sound = mraa.Aio(0)   

while 1:
    soundVal = int(sound.read())
    print soundVal
    time.sleep(.5)
