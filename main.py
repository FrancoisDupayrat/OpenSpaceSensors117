#!/usr/bin/env python  
   
import led
import temperature
import light
import sound
import lcd
import air_quality
import time
import ConfigParser
import led_bar


def getValues():
    config = ConfigParser.ConfigParser()
    config.read("values.ini")
    db = config.get("Values", "db")
    degree = config.get("Values", "degree")
    lux = config.get("Values", "lux")
    quality = config.get("Values", "quality")
    qualityValue = config.get("Values", "qualityValue")
    data = [db, degree, lux, qualityValue]
    return data

def init():
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
    
    #Led bar is on pin D8, uses pin 8 and 9
    led_bar.init()

if __name__=="__main__":
    init()
    config = ConfigParser.ConfigParser()
    config.add_section('Values')
    while True:  
    	led.loop() #will add a 0.4sec delay
    	db = sound.loop() # time.sleep 0.5s
    	degree = temperature.loop()
    	lux = light.loop()
    	quality = air_quality.getString()
    	qualityValue = air_quality.getValue()
    	lcd.setText("%.0f lux, %.01f C\n%d db, %s" % (lux, degree, db, quality))
        level = 0    
        if qualityValue > 300:
            level = level + 1
        
        if lux < 200:
            level = level + 2
        elif lux < 100:
            level = level + 1
        
        if degree > 30 or degree < 18:
            level = level + 2
        elif degree > 26 or degree < 22:
            level = level + 1
        
        if db > 100:
            level = level + 1
            
        led_bar.setLevel(level)
        
        cfgfile = open("values.ini",'w')
        config.set('Values', 'db', db)
        config.set('Values', 'lux', lux)
        config.set('Values', 'degree', degree)
        config.set('Values', 'quality', quality)
        config.set('Values', 'qualityValue', qualityValue)
        config.write(cfgfile)  
        cfgfile.close()
    	time.sleep(.5)