from math import cos, sin, radians, sqrt, asin, acos, atan2, atan, degrees, pi

class setAngle: 
    
    #** aircraft and station *** tuple(latitude, longitude, altitude) ***
    #** latitude & longitude convert to radians
    #** altitude in kilometres    
    
    def __init__(self, aircraft, station):
        self.aircraft = tuple((radians(aircraft[0]), radians(aircraft[1]), aircraft[2]))
        self.station  = tuple((radians(station[0]), radians(station[1]), station[2]))
        self.deltaLat = self.aircraft[0] - self.station[0]
        self.deltaLong = self.aircraft[1] - self.station[1]
        self.calculatedisDistance()
        self.calculatePan()
        self.calculateTilt()
        self.standardPan()



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


    #* Function for check pan angle
    def standardPan(slef):
        pass
