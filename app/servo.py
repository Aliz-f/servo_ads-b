import RPi.GPIO as GPIO
from time import sleep

pinOut1 = 33
pinOut2 = 32
freq = 50


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinOut1, GPIO.OUT)
GPIO.setup(pinOut2, GPIO.OUT)

#***tilt : up and down and pan : side by side

tilt = GPIO.PWM(pinOut1, freq)
pan = GPIO.PWM(pinOut2, freq)

tilt.start(2)
pan.start(2)


dutyServo = 2

while dutyServo<12:
    tilt.ChangeDutyCycle(dutyServo)
    pan.ChangeDutyCycle(dutyServo)
    sleep(1)
    dutyServo+=1

tilt.stop()
GPIO.cleanup()