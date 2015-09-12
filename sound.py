#!/usr/bin/env python 

import mraa
import sys
import time

def init():
	global sound 
	sound = mraa.Aio(0) 
	
def loop():
	global sound
	soundVal = int(sound.read())
	print soundVal
	time.sleep(.5)
