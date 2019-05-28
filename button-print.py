#!/usr/bin/python

import time
import RPi.GPIO as GPIO
from lib.Adafruit_Thermal import *

ledPin = 12
btn1Pin = 23
btn2Pin = 24
bounceTime = 400
printerBaudRate = 9600
printerTimeout = 5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(btn1Pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(btn2Pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
printer = Adafruit_Thermal("/dev/serial0", printerBaudRate, timeout = printerTimeout)

def btn1_callback(channel):
    print("Personal Business Card requested.")
    printer.feed(1)
    printer.justify('C')
    printer.setSize('L')
    printer.println("Kevin Cefalu")
    printer.setSize('M')
    printer.println("PsiBit Development, Owner")
    printer.feed(2)
    printer.println("Mandeville, La 70448")
    printer.println("Kevin.Cefalu@GMail.com")
    printer.println("+1 (504) 252-6382")
    printer.feed(4)
    # # Restore printer to defaults
    printer.setDefault()

def btn2_callback(channel):
    print("Personal Business Card requested.")
    printer.feed(1)
    printer.justify('C')
    printer.setSize('L')
    printer.println("Kevin Cefalu")
    printer.setSize('M')
    printer.println("Netchex, DevOps Engineer II")
    printer.feed(2)
    printer.println("Mandeville, La 70448")
    printer.println("KCefalu@NetchexOnline.com")
    printer.feed(4)
    # # Restore printer to defaults
    printer.setDefault()

GPIO.add_event_detect(btn1Pin, GPIO.FALLING, callback = btn1_callback, bouncetime = bounceTime)
GPIO.add_event_detect(btn2Pin, GPIO.FALLING, callback = btn2_callback, bouncetime = bounceTime)

message = input("Press enter to quit\n\n")
GPIO.cleanup()
