# Import libraries
import RPi.GPIO as GPIO
from time import sleep

# Declare pin number standard
GPIO.setmode(GPIO.BOARD)

# Setup LED
LED_PIN = 11
GPIO.setup(LED_PIN, GPIO.OUT)

# Create a function to blink
def blink(led, dur):
    GPIO.output(led, GPIO.HIGH)
    sleep(dur)
    GPIO.output(led, GPIO.LOW)
    sleep(dur)

# Repeat forever
try:
    while True:
        blink(LED_PIN, 0.25)
except KeyboardInterrupt:
    GPIO.cleanup()
