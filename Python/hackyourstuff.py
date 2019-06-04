import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

While True:
    if(GPIO.input(17)):
        GPIO.output(18, GPIO.HIGH)
    
