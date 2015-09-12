#!/usr/bin/env python  
   
import led
import temperature

#Temperature use Analog pin 1
#LED use Digital pin 13
temperature.init()
led.init()


while True:  
	led.loop() #will add a 0.4sec delay
	temperature.loop()

