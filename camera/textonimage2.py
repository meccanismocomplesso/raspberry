from picamera import PiCamera
from picamera import Color
import time

camera = PiCamera()
camera.resolution = (2592, 1944)

camera.start_preview()
camera.annotate_size = 120
camera.annotate_foreground = Color('black')
camera.annotate_background = Color('white')
camera.annotate_text = " I am what I am "
time.sleep(5)
camera.capture('image02.jpg')
camera.stop_preview()

