from tkinter import *
from angle import setAngle, setServoduty
import RPi.GPIO as GPIO
from time import sleep

class servo():
    def gpio(self):
        self.pinOut1 = 33 #tilt
        self.pinOut2 = 32 #pan
        self.freq = 50
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinOut1, GPIO.OUT)
        GPIO.setup(self.pinOut2, GPIO.OUT)

        #***tilt : up and down and pan : side by side

        self.tilt = GPIO.PWM(self.pinOut1, self.freq)
        self.pan = GPIO.PWM(self.pinOut2, self.freq)

        self.tilt.start(7)
        self.pan.start(7)
        return


    def setServo(self,aircraft, station):
        aircraft = tuple((float(), float(), float()))
        station = tuple((float(), float(), float()))

        angle = setAngle(aircraft,station)
        duty = setServoduty(angle.pan, angle.tilt)
        self.tilt.ChangeDutyCycle(duty.tilt_servo)
        sleep(1)
        self.pan.ChangeDutyCycle(duty.pan_servo)
        sleep(1)

class MyWindow():
    def __init__(self, win):
        Label(win,text="Station Information",
            fg="white",
            bg="black").place(x=0, y=0)

        Label(win,text="Station Latitude",
            fg="black",
        ).place(x=0, y=65)
        self.stationLat=Entry(win,
            fg="black",
            bg="white",
            bd=6)
        self.stationLat.place(x=150, y=60)

        Label(win,text="Station Longtitude",
            fg="black",
        ).place(x=0, y=125)
        self.stationLong=Entry(win,
            fg="black",
            bg="white",
            bd=6)
        self.stationLong.place(x=150, y=120)
        
        Label(win,text="Station Altitude",
            fg="black",
        ).place(x=0, y=185)
        self.stationAlt=Entry(win,
            fg="black",
            bg="white",
            bd=6)
        self.stationAlt.place(x=150, y=180)


        Label(win,text="Aircraft Information",
            fg="white",
            bg="black").place(x=0, y=240)

        Label(win,text="Aircraft Latitude",
            fg="black",
        ).place(x=0, y=305)
        self.aircraftLat=Entry(win,
            fg="black",
            bd=6)
        self.aircraftLat.place(x=150, y=300)

        Label(win,text="Aircraft Longtitude",
            fg="black",
        ).place(x=0, y=365)
        self.aircraftLong=Entry(win,
            fg="black",
            bd=6)
        self.aircraftLong.place(x=150, y=360)
        
        Label(win,text="Aircraft Altitude",
            fg="black",
        ).place(x=0, y=425)
        self.aircraftAlt=Entry(win,
            fg="black",
            bd=6)
        self.aircraftAlt.place(x=150, y=420)
        
        self.btn = Button(win,
        text='submit', command=self.setServo)
        self.btn.place(x=250, y=500)
        self.gpio()

    def gpio(self):
        self.pinOut1 = 33 #tilt
        self.pinOut2 = 32 #pan
        self.freq = 50
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinOut1, GPIO.OUT)
        GPIO.setup(self.pinOut2, GPIO.OUT)

        #***tilt : up and down and pan : side by side

        self.tilt = GPIO.PWM(self.pinOut1, self.freq)
        self.pan = GPIO.PWM(self.pinOut2, self.freq)

        self.tilt.start(7)
        self.pan.start(7)
        return


    def setServo(self):
        aircraft = tuple((float(self.aircraftLat.get() or 0.0), float(self.aircraftLong.get() or 0.0), float(self.aircraftAlt.get() or 0.0)))
        station = tuple((float(self.stationLat.get() or 0.0), float(self.stationLong.get() or 0.0), float(self.stationAlt.get() or 0.0)))

        angle = setAngle(aircraft,station)
        duty = setServoduty(angle.pan, angle.tilt)
        self.tilt.ChangeDutyCycle(duty.tilt_servo)
        # print(angle.pan)
        sleep(1)
        self.pan.ChangeDutyCycle(duty.pan_servo)
        # print(angle.tilt)
        sleep(1)

window = Tk()
mywin = MyWindow(window)
window.title('ads-b Simulation')
window.geometry("600x600+10+10")
window.mainloop()
