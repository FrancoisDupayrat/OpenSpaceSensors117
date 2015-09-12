import mraa  
import math


#Get Temperature on an Analog input
TEMPERATURE_PIN = 1
THERMISTOR_VALUE=3975;


def init():
	global temperature
	temperature = mraa.Aio(TEMPERATURE_PIN)

def loop():	
	global temperature
	temperatureReading = temperature.read()
	resistance=(float)(1023-temperatureReading)*10000/temperatureReading; #get the resistance of the sensor;
	temperatureValue=1/(math.log(resistance/10000)/THERMISTOR_VALUE+1/298.15)-273.15; #convert to temperature via datasheet
	print("Temperature: %.2f°C" % temperatureValue)