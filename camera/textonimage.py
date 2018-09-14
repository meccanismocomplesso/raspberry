from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (2592, 1944)

camera.start_preview()
camera.annotate_text = "I am what I am"
camera.annotate_text_size = 120
time.sleep(5)
camera.capture('image02.jpg')
camera.stop_preview()



