#!/usr/bin/python

import RPi.GPIO as GPIO

btn1Pin = 23
btn2Pin = 24
bounceTime = 400

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(btn1Pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(btn2Pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def btn1_callback(channel):
    print("Button 1 was pushed!")

def btn2_callback(channel):
    print("Button 2 was pushed!")

GPIO.add_event_detect(btn1Pin, GPIO.FALLING, callback = btn1_callback, bouncetime = bounceTime)
GPIO.add_event_detect(btn2Pin, GPIO.FALLING, callback = btn2_callback, bouncetime = bounceTime)

message = input("Press enter to quit\n\n")
GPIO.cleanup()
