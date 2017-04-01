#Program to test pin output
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #BCM or BOARD
#CHANGEME to the right pin
pin = 24
GPIO.setup(pin, GPIO.OUT)
#Sets pin to on
GPIO.output(pin, True)
