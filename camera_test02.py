from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()

x = ['film', 'negative', 'solarize', 'sketch', 'emboss',]


for effect in camera.IMAGE_EFFECTS:
    
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    
    sleep(2)

    if effect in x:
        camera.capture("filename" + str(x.index(effect)) + ".jpg")
        
camera.stop_preview()
