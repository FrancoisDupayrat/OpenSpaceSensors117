import mraa

# Aio is the analogue port

# Arduino takes the average of 5 mins as initial voltage

# Delay may required for 20000 to get Sensor warm
AIR_QUALITY_PIN = 3

def init():
    global sensor
    sensor = mraa.Aio(AIR_QUALITY_PIN)


def loop():
    global sensor
    sensor_v = sensor.read()
    text = "No pollution"
    if sensor_v > 700:
        text = "High pollution"
    elif sensor_v > 300:
        text = "Low pollution"

    print ("Air quality: %d, text: %s" % (sensor_v, text))
    return str(text)

