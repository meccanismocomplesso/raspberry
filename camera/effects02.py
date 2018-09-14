from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (2592, 1944)

camera.start_preview()
time.sleep(5)

for effect in camera.IMAGE_EFFECTS:
    filename = "image_%s.jpg" % effect
    camera.image_effect = effect
    camera.capture(filename)
    time.sleep(1)
camera.stop_preview()

