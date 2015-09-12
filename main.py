#!/usr/bin/env python  
   
import led
import temperature
import light
import sound
import lcd

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

while True:  
	led.loop() #will add a 0.4sec delay
	db = sound.loop() # time.sleep 0.5s
	degree = temperature.loop()
	lux = light.loop()
	lcd.setText("%d db, %.01f C\n%.0f lux" % (db, degree, lux))

