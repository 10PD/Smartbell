#Program to test pin output
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #BCM or BOARD
#CHANGEME to the right pin
pin = 23
GPIO.setup(pin, GPIO.OUT)
#Sets pin to on
GPIO.output(pin, True)
sleep(5)
GPIO.output(pin, False)
