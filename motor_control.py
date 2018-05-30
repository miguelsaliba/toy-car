o1 = 17
o2 = 22
o3 = 27
o4 = 18

import time
import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(o1,GPIO.OUT)
    GPIO.setup(o2,GPIO.OUT)
    GPIO.setup(o3,GPIO.OUT)
    GPIO.setup(o4,GPIO.OUT)

    GPIO.output(o1,True)
    GPIO.output(o2,False)
    GPIO.output(o3,False)
    GPIO.output(o4,True)

    time.sleep(3)

    GPIO.cleanup()

except:
   GPIO.cleanup()
