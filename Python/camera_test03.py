from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview(fullscreen=False, window = (100,20,640,480))
camera.start_recording('/home/pi/videotest.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
