import RPi.GPIO as GPIO
import time
<strong>from picamera import PiCamera</strong>

GPIO.setmode(GPIO.BCM)

pirPin = 7
GPIO.setup(pirPin, GPIO.IN, <strong>GPIO.PUD_UP</strong>)
camera = PiCamera()
counter = 1

while True:
    if GPIO.input(pirPin) == GPIO.LOW:
       try: 
           camera.start_preview()
           time.sleep(1)
           camera.capture('/home/pi/image%s.jpg' % counter)
           counter = counter + 1
           camera.stop_preview()
       except:
           camera.stop_preview()
    time.sleep(3)
