from angle import setAngle, setServoduty
from time import sleep
import sys, os.path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
import datetime
import py1090 


import RPi.GPIO as GPIO
from time import sleep

pinOut1 = 33
pinOut2 = 32
freq = 50

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinOut1, GPIO.OUT)
GPIO.setup(pinOut2, GPIO.OUT)


tilt = GPIO.PWM(pinOut1, freq)
pan = GPIO.PWM(pinOut2, freq)

tilt.start(2)
pan.start(2)


dutyServo = 2

print('station information : 32.444,54.4545,1888')
station = input('Enter station information: ')
station = tuple((float(station.split(',')[0]), float(station.split(',')[1]), float(station.split(',')[2])))

# perviousAircraft = ''

with py1090.Connection() as connection:
    print('Start')
    counter = 0
    for line in connection:
        message = py1090.Message.from_string(line)
        if counter==0 and message.aircraft_id:
            perviousAircraft = message 
            if message.latitude and message.longitude:
                print(f"switch to {message.aircraft_id}")
                angle = setAngle(tuple((float(message.latitude), float(message.longitude), float(message.altitude))),station, message.aircraft_id)
                duty = setServoduty(angle.pan, angle.tilt)
                tilt.ChangeDutyCycle(duty.tilt_servo)
                sleep(1)
                pan.ChangeDutyCycle(duty.pan_servo)
                sleep(1)
                counter += 1
            else:
                print(f"lat and long data for{message.aircraft_id} not valid")
        elif counter!=0 and message.aircraft_id:
            if message.aircraft_id == perviousAircraft.aircraft_id:
                if message.latitude and message.longitude:
                    angle.update(tuple((message.latitude, message.longitude)))
                    duty.update(angle.pan, angle.tilt)
                else:
                    print(f"lat and long data for{message.aircraft_id} not valid")
            else:
                print(f"switch to {message.aircraft_id}")
                perviousAircraft = message 
                if message.latitude and message.longitude:
                    angle = setAngle(tuple((message.latitude, message.longitude)),station, message.aircraft_id)
                    duty = setServoduty(angle.pan, angle.tilt)
                    tilt.ChangeDutyCycle(duty.tilt_servo)
                    sleep(1)
                    pan.ChangeDutyCycle(duty.pan_servo)
                    sleep(1)
                    counter += 1
