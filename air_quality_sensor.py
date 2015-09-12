import mraa
import time


# Aio is the analogue port

# Arduino takes the average of 5 mins as initial voltage

# Delay may required for 20000 to get Sensor warm

while True:
    try:
    	sensorpin = mraa.Aio(3)
    	sensor_v = sensorpin.read()

        if sensor_v > 700:
            print ("High pollution")
        elif sensor_v > 300:
            print ("Low pollution")
        else:
            print ("Air fresh")

        print ("sensor_value =", sensor_v)
        time.sleep(.5)

    except IOError:
        print ("Error")

