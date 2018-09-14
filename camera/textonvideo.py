from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (1280, 720)

camera.start_preview()
camera.annotate_text = "I am what I am"
camera.start_recording('video.h264')
time.sleep(10)
camera.stop_recording()
camera.stop_preview()
