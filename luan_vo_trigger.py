from datetime import datetime
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
 
#create a variable called PIR, which refers to the P8_9 pin
PIR = "P8_9"

#minutes in micro-seconds resolution
minutes2 = 120000000   #for 10KHz
minutes20 = 1200000000 #for 1Hz and 100Hz
 
#initialize the pin as an INPUT

GPIO.setup(PIR, GPIO.IN)
GPIO.add_event_detect(PIR, GPIO.RISING)

#Create a now and future time for while loop
now = datetime.now()
timestampStr = now.strftime("%s%f \n")

future = float(datetime.now().strftime("%s%f")) + minutes20
file1 = open("/home/debian/freq1Hz.txt","w+")
file1.write("This is time stamp for 1Hz \n")

file1.writelines(["Time Elasped: ", timestampStr])
file1.writelines(["Time Done:    ",(str(future))])


#Detects Rising Edge
while float(timestampStr) < future:
	now = datetime.now()	
        timestampStr = now.strftime("%s%f \n")
	if GPIO.event_detected(PIR):
		file1.write(timestampStr)

	

GPIO.cleanup()
