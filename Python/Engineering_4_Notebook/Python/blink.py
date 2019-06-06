import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
counter=1
while (counter<=11):
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)
    time.sleep(1)
    counter = counter + 1

