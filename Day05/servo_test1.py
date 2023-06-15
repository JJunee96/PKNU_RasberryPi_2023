# servoMotor TEST
import RPi.GPIO as GPIO
import time

pwm_pin = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 100)
angle = 3
pwm.start(angle)

while True:
    cmd = input('키 입력 [f|r] ')
    direction = cmd[0]
    if direction == 'f': # forward
        while angle <= 20:
            angle += 1
            print(f'angle = {(angle-3)*10}')
            pwm.ChangeDutyCycle(angle)
    elif direction == 'r':
        angle = 20
        while angle >= 3:
            angle -= 1
            print(f'angle = {(angle-3)*10}')
            pwm.ChangeDutyCycle(angle)
    

    