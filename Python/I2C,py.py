import time
import Adafruit_LSM303
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
lsm303 = Adafruit_LSM303.LSM303()

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

padding = 2
shape_width = 20
top = padding
bottom = height-padding
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
while True:
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    time.sleep(0.5)

    draw.rectangle((0,0,width,height), outline=0, fill=0)   

    draw.text((10, top),    'x: ' + str(accel_x/100),  font=font, fill=255)
    draw.text((10, top+20), 'y: ' + str(accel_y/100), font=font, fill=255)
    draw.text((10, top+40), 'z: ' + str(accel_z/100), font=font, fill=255)

    disp.image(image)
    disp.display()
