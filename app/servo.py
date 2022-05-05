import RPi.GPIO as GPIO
from time import sleep

pinOut1 = 33

freq = 50


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinOut1, GPIO.OUT)

servo = GPIO.PWM(pinOut1, freq)
servo.start(2)

dutyServo = 2

while dutyServo<12:
    servo.ChangeDutyCycle(dutyServo)
    sleep(1)
    dutyServo+=1

servo.stop()
GPIO.cleanup()