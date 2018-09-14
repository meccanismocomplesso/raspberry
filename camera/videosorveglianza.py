from picamera import PiCamera
import datetime as dt
import time

camera = PiCamera()
camera.resolution = (1280, 720)

camera.start_preview()
camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
camera.start_recording('video.h264')

start = dt.datetime.now()
while (dt.datetime.now() - start).seconds &lt; 30:
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.wait_recording(0.2)
camera.stop_recording() camera.stop_preview()

