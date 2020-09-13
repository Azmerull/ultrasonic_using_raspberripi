#========================================= External library =========================================================#
import RPi.GPIO as GPIO
import time

#===================================== GPIO pin numbering setup =====================================================#
""" Using physical numbering on raspi pin """
GPIO.setmode(GPIO.BOARD)          
""" ignore all warnings"""
GPIO.setwarnings(False)


class Ultrasonic:

    """ trigger: trigger pin,  echo: echo pin,  position: name indicator of which ultrasonic """
    def __init__(self, trigger, echo, position):
        """ Initialzing the attributes for every sensors """
        self.trigger = trigger
        self.echo = echo
        self.position = position

        """ setting up the trigger & echo pin for every sensors """
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

        self.pulseStartTime = 0
        self.pulseEndTime = 0
        self.pulseDuration = 0
        self.distance = 0

    def Trigger(self):
        GPIO.output(self.trigger, GPIO.LOW)
        GPIO.output(self.trigger, GPIO.HIGH)

        """ sleep time to let the sensor settle down """
        time.sleep(0.02)
        GPIO.output(self.trigger, GPIO.LOW)
    
    def DistanceMeasurement(self):
        while GPIO.input(self.echo) == 0:
            """ recording the time when the ultrasound is blasted """
            self.pulseStartTime = time.time()
        
        while GPIO.input(self.echo) == 1:
            """ recording the time when the blasted ultrasound is received """
            self.pulseEndTime = time.time()
        
        """ getting the total time travelled by the blasted ultrasound """
        self.pulseDuration = self.pulseEndTime - self.pulseStartTime

        """ sound speed in cm is 34300 cm per second """
        """ original formula is 34300 = (Distance/(pulse duration/2)) """
        """ distance = pulse duration * 17150 """
        self.distance = round(self.pulseDuration*17150, 1)

    def Result(self):
        """ 10 is in cm """
        if (self.distance < 10):
            """ printing is for testing & observation purpose """
            print(f"{self.position}: WARNING!", end = " ")
        elif (self.distance > 150):
            """ printing is for testing & observation purpose """
            print(f"{self.position}: CLEAR!", end = " ")
        else:
            """ printing is for testing & observation purpose """
            print(f"{self.position}: Object: {self.distance} cm", end = " ")
