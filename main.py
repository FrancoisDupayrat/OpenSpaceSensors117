#!/usr/bin/env python  
   
import led
import temperature
import light

#Temperature use Analog pin 1
temperature.init()
#LED use Digital pin 13
led.init()
#Light is on I2C, doesn't use a specific pin
light.init()


while True:  
	led.loop() #will add a 0.4sec delay
	temperature.loop()
	light.loop()

