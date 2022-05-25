from angle import setAngle, setServoduty
import RPi.GPIO as GPIO
from time import sleep

pinOut1 = 33 #tilt
pinOut2 = 32 #pan
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

print('location format for station : latitude,longtitude,altitude')
station = input('Enter station information: ')
station = tuple((float(station.split(',')[0]), float(station.split(',')[1]), float(station.split(',')[2])))

print('location format for aircraft : latitude,longtitude,altitude')
while True:

    aircraft = input('Enter aircraft information: ')
    aircraft = tuple((float(aircraft.split(',')[0]), float(aircraft.split(',')[1]), float(aircraft.split(',')[2])))

    angle = setAngle(aircraft,station)
    duty = setServoduty(angle.pan, angle.tilt)
    tilt.ChangeDutyCycle(duty.tilt_servo)
    sleep(1)
    pan.ChangeDutyCycle(duty.pan_servo)
    sleep(1)



