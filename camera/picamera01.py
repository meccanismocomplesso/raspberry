from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.start_preview()
time.sleep(5)
camera.capture('image01.jpg')
camera.stop_preview()

