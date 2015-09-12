import mraa  
import time

#Flash a LED to show it's working. Requires a GPIO OUT
LED_PIN = 13


def init():
	global led 
	led = mraa.Gpio(LED_PIN)  
	led.dir(mraa.DIR_OUT)  

def loop():
    global led
    led.write(1)  
    time.sleep(0.5)  
    led.write(0)