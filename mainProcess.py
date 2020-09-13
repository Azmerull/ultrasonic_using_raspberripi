#! usr/bin/python3

#==================================== ultrasonic sensor pin =========================================================#
triggerPin = 10
echoPin = 8


#======================================== Main process ==============================================================#
""" importing ultrasonic modules """
from sensorObject import*

""" initializing ultrasonic object """
""" you can initialized more than one ultrasonic object """
ultasonicSensor1 = Ultrasonic(triggerPin, echoPin, "FrontSensor")
#ultasonicSensor2 = Ultrasonic(triggerPin2, echoPin2, "BackSensor")

try:
    while True:
        """ trigger method of Ultrasonic class to activate the sensor"""
        ultasonicSensor1.Trigger()
        """ distance measurement method to calculate & display the distance """
        ultasonicSensor1.DistanceMeasurement()
        """ method for printing the result (for observation & verification) """
        ultasonicSensor1.Result()
        print(" ")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("System stopped by user!")