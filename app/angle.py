from math import cos, sin, radians, sqrt, asin, acos, atan2, atan, degrees, pi
R = 6371e3

class setAngle: 
    
    #** aircraft and station *** tuple(latitude, longitude, altitude) ***
    #** latitude & longitude convert to radians
    #** altitude in kilometres    
    
    def __init__(self, aircraft, station, id=None):
        self.aircraft = tuple((radians(aircraft[0]), radians(aircraft[1]), aircraft[2]))
        self.station  = tuple((radians(station[0]), radians(station[1]), station[2]))
        self.aircraft_id = id
        self.calculateDelta()
        self.calculatedisDistance()
        self.calculatePan()
        self.calculateTilt()

    def calculateDelta(self):
        self.deltaLat = self.aircraft[0] - self.station[0]
        self.deltaLong = self.aircraft[1] - self.station[1]

    def printInfo(self):
        print("Aircraft (Lat: {}, long: {}, altitude: {}) : ".format( self.aircraft[0],self.aircraft[1], self.aircraft[2]))
        print("Station  (Lat: {}, long: {}, altitude: {})  : ".format(self.station[0],self.station[1], self.station[2]))
        print("Distance : {}".format(self.distance))
        print("pan : {}\u00B0".format( self.pan))
        print("tilt : {}\u00B0".format(self.tilt))

    #* Function for calculate distance 
    def calculatedisDistance(self):
        self.distance = 2*R*asin(sqrt(sin(self.deltaLat/2)**2 + cos(self.station[0]) * cos(self.aircraft[0]) * sin(self.deltaLong/2)**2))
    
    #* Function for calculate Pan angle (side by side)
    def calculatePan(self):
        y = sin(self.deltaLong) * cos(self.aircraft[0])
        x = (cos(self.station[0]) * sin(self.aircraft[0]) ) - (sin(self.station[0]) * cos(self.aircraft[0]) * cos(self.deltaLong)) 
        
        self.pan = ((atan2(y, x) * 180)/pi + 360) %360
        # self.pan = degrees(atan2(y, x))
        
        # self.alpha2 = acos((R*self.deltaLat)/self.distance)
        # self.pan = self.alpha2 - THETA - THETAD
    
    #* Function for calculate Tilt Angle (up and down)
    def calculateTilt(self):
        self.deltaAltitude = self.aircraft[2] - self.station[2]
        self.tilt = degrees(atan(self.deltaAltitude/self.distance))

    def update(self, aircraft):
        self.aircraft = tuple((radians(aircraft[0]), radians(aircraft[1]), aircraft[2]))
        self.calculateDelta()
        self.calculatedisDistance()
        self.calculatePan()
        self.calculateTilt()





class setServoduty: #** format (pan, tilt)
    #** Get pan & tilt angle and convert to duty for servo motors
    #** ServoMotor = mg90s || mg90s duty = [2,12] or [2.5,12.5]

    def __init__(self, pan, tilt):
        self.pan = pan
        self.tilt = tilt
        self.angle_to_duty()


    def prinInfo(self):
        print("PanServo Duty:  {}".format(self.pan_servo))
        print("TiltServo Duty: {}".format(self.tilt_servo))

    def update(self,pan, tilt):
        self.pan = pan
        self.tilt = tilt
        self.angle_to_duty()
    
    def angle_to_duty(self):
        if 0<=self.pan<=90:
            self.pan_servo = (self.pan/18)
            self.pan = 7 - self.pan
        elif 270<=self.pan<360:
            tempPan = 360 - self.pan
            self.pan_servo = (tempPan/18)
            self.pan_servo +=7
        else:
            self.pan = 7
        self.tilt_servo = (self.tilt/18)+2
