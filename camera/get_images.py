from picamera import PiCamera
import time

camera.start_preview()
for i in range(9):
    time.sleep(5)
    camera.capture('/home/pi/image%s.jpg' % i)
camera.stop_preview()

