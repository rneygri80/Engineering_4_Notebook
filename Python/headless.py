import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

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
font = ImageFont.load_default()

data = []
length = 50
graphWidth = 50
graphHeight = 50
xPadding = 50
spacing = graphWidth / length
yAxisText = "accel"
showIcon = False

def mapNum(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)
                       
while True:
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    
    accel_x/= 100
    accel_y/= 100
    accel_z/= 100

    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    data.append(accel_x)
    if(len(data) > length):
        data.pop(0)

    draw.line((xPadding, 5, xPadding, graphHeight), fill = 255)
    draw.line((xPadding, graphHeight, width - 5, graphHeight), fill = 255)
    draw.text((width - 50, graphHeight + 5), "t(s)", font = font, fill = 255)
    draw.text((width - width, graphHeight / 2), yAxisText, font = font, fill = 255)

    rotImg = Image.new("1",
        (font.getsize(yAxisText)[0] + 2,
        font.getsize(yAxisText)[1] + 2), color=0)
    rotDraw = ImageDraw.Draw(rotImg)
    rotDraw.text((0, 0), yAxisText, fill = 255)
    rotImg = rotImg.rotate(90, expand = 1)

    for x, y in enumerate(data):
        if (x < len(data) -1):
            draw.line((
                (x + spacing) + xPadding,
                ((mapNum(y, -10, 10, 0, graphHeight))),
                ((x+1) * spacing) + xPadding,
                ((mapNum(data[x+1],-10, 10, 0, graphHeight)))),
                fill = 255)

    disp.image(image)
    disp.display()
