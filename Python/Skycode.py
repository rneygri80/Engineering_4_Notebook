import Adafruit_BMP.BMP085 as BMP085
import Adafruit_LSM303
import time
import RPi.GPIO as GPIO

from time import sleep

sensor = BMP085.BMP085()
lsm303 = Adafruit_LSM303.LSM303()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
led = GPIO.input(17)

GPIO.output(17, GPIO.HIGH)
time.sleep(3)
GPIO.output(17, GPIO.LOW)

counter = 1

f = open("skydatafilefinal.txt", "w+")
oldAlt = 0
alt = 0
time.sleep(60) 


while counter <= 60: #120
    
    alt = sensor.read_altitude()
    if oldAlt > alt:
        GPIO.output(17, GPIO.HIGH)
        f.write(" Peak!")
        time.sleep(.35)
        GPIO.output(17, GPIO.LOW)
    oldAlt = alt
    
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    
    accel_x/= 100
    accel_y/= 100
    accel_z/= 100
    
    f.write(' Altitude = {0:0.2f} m, '.format(sensor.read_altitude()))
    f.write('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))

    #print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
     #accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))    
    #print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
    #print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
    #print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
    #print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))


    counter = counter + 1
    time.sleep(.5) #.5

f.close()

    

