# LED RGB 깜빡이기
import RPi.GPIO as GPIO
import time

red = 17
green = 22
blue = 27
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, True)
GPIO.output(green, True)
GPIO.output(blue, True)

try:
    while True:
        GPIO.output(red, False)
        GPIO.output(green, True)
        GPIO.output(blue, True)
        time.sleep(0.1)
        GPIO.output(red, True)
        GPIO.output(green, False)
        GPIO.output(blue, True)
        time.sleep(0.1)
        GPIO.output(red, True)
        GPIO.output(green, True)
        GPIO.output(blue, False)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()