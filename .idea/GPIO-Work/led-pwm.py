#!/usr/bin/python

import time
import RPi.GPIO as GPIO

ledPin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin, GPIO.OUT)

# channel=12 frequency=50Hz
ledPWM = GPIO.PWM(ledPin, 50)
ledPWM.start(0)

try:
    while 1:
        for dc in range(0, 101, 5):
            ledPWM.ChangeDutyCycle(dc)
            time.sleep(0.1)

        for dc in range(100, -1, -5):
            ledPWM.ChangeDutyCycle(dc)
            time.sleep(0.1)

except KeyboardInterrupt:
    pass

ledPWM.stop()
GPIO.cleanup()
