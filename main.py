#!/usr/bin/env python  
   
import led
import temperature
import light
import sound
import lcd
import air_quality
import time

#Temperature use Analog pin 1
temperature.init()

#LED use Digital pin 13
led.init()

#Light is on I2C, doesn't use a specific pin
light.init()

#Sound uses A0 Grove Port
sound.init()

#LCD is on I2C, doesn't use a specific pin
lcd.init()
lcd.setRGB(0,255,0)

#Air Quality is on Analog Pin 1
air_quality.init()

while True:  
	led.loop() #will add a 0.4sec delay
	db = sound.loop() # time.sleep 0.5s
	degree = temperature.loop()
	lux = light.loop()
	quality = air_quality.loop()
	lcd.setText("%.0f lux, %.01f C\n%d db, %s" % (lux, degree, db, quality))
	time.sleep(.5)

