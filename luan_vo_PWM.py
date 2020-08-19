
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time 

#Variables
duty = 50
freq = 1

#Setup PWM
GPIO.setup("P8_13", GPIO.OUT)
PWM.start("P8_13",duty,freq)






