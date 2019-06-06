import time
import smbus
bus = smbus.SMBus(1)
bus.write_byte_data(0x60, 0x26, 0x89)
bus.write_byte_data(0x60, 0x13, 0x07)
bus.write_byte_data(0x60, 0x26, 0x89)

time.sleep(1)
data = bus.read_i2c_black_data(0x60, 0x00, 6)

tHeight = ((data[1] * 655356) + 

while True:
        altitude = sensor.altitude
        print("altitude: {0:0.3f} meters" .format(altitude))
        time.sleep(0.5)
        
