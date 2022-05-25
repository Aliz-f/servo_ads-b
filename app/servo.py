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

# while True:
#     inpu = int(input("Enter angle: "))
#     if inpu == 0:
#         break
#     angle = (inpu/18) + 2
#     tilt.ChangeDutyCycle(angle)
#     sleep(1)
#     pan.ChangeDutyCycle(angle)
#     sleep(1)


# while dutyServo<=12:
#     tilt.ChangeDutyCycle(dutyServo)
# #    pan.ChangeDutyCycle(dutyServo)
#     sleep(1)
#     dutyServo+=1

# tilt.ChangeDutyCycle(7)
# sleep(0.02)
# pan.ChangeDutyCycle(2)
# sleep(0.02)
tilt.stop()
pan.stop()

GPIO.cleanup()
