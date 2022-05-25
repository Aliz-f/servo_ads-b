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

tilt.start(7)
pan.start(7)

print('Help:')
print('location format for station : latitude,longtitude,altitude')
print('location format for aircraft : latitude,longtitude,altitude')
print('*************************')
station = input('Enter station information: ')
station = tuple((float(station.split(',')[0]), float(station.split(',')[1]), float(station.split(',')[2])))

while True:

    aircraft = input('Enter aircraft information: ')
    aircraft = tuple((float(aircraft.split(',')[0]), float(aircraft.split(',')[1]), float(aircraft.split(',')[2])))

    angle = setAngle(aircraft,station)
    duty = setServoduty(angle.pan, angle.tilt)
    print('*************************')
    print(angle.printInfo())
    print('*************************')
    
    tilt.ChangeDutyCycle(duty.tilt_servo)
    print(duty.tilt_servo)
    print(angle.tilt)
    sleep(1)
    pan.ChangeDutyCycle(duty.pan_servo)
    print(duty.pan_servo)
    print(angle.pan)
    sleep(1)



