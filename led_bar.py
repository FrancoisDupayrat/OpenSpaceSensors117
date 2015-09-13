import mraa
import math
import time

CLOCK_PIN = 9
DATA_PIN = 8

#Send the latch command
def latchData():
    global data
    data.write(0)
    time.sleep(0.00001)
    for x in range(0, 4):
        data.write(1)
        data.write(0)


# Send 16 bits of data
def sendData(value):
    global nextClockSign, data, clock
    nextClockSign = 0
    for x in range(0, 16):
        data.write(1 if (value & 0x8000) else 0)  
        clock.write(nextClockSign)
        nextClockSign = 0 if (nextClockSign == 1) else 1
        value <<= 1;

def setData(__state):
    sendData(0x00);

    for i in range(0, 10):
        sendData(__state[10-i-1])

    #Two extra empty bits for padding the command to the correct length
    sendData(0x00);
    sendData(0x00);

    latchData();

def init():
	global data, clock
	data = mraa.Gpio(DATA_PIN)  
	data.dir(mraa.DIR_OUT)  
	clock = mraa.Gpio(CLOCK_PIN)  
	clock.dir(mraa.DIR_OUT)  

#must be 0 to 10
def setLevel(level):
    global data, clock
    level = max(0, min(10, level))
    level *= 8; # there are 8 (noticable) levels of brightness on each segment

    # Place number of 'level' of 1-bits on __state
    __state = []
    for i in range(0, 10):
        __state.append(~0 if(level > 8) else ~(~0 << level) if (level > 0) else 0)
        level -= 8;

    setData(__state)