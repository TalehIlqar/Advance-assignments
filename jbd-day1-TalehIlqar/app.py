class Vehicle:
    def __init__(self,numofWheels, color, engine, positionX, positionY, speed, isOn=False):
        self.numofWheels=numofWheels
        self.color = color
        self.engine = engine
        self.positionX = positionX
        self.positionY = positionY
        self.speed = speed
        self.isOn = isOn

    # def introduce(self):
    #     return f"{self.numofWheels},{self.color},{self.engine},{self.positionX},{self.positionY},{self.speed}, {self.isOn}"
    
    def accelerate(self):
        self.speed += 1
        print(self.speed)

    def moveForward(self, x, y):
        self.positionX += x
        self.positionY += y
        print(f'{self.positionX}, {self.positionY}')
    
    # def moveBackwards(self, x, y):
    #     if (x < 0 and y < 0 ):
    #         self.positionX = -(x)
    #         self.positionY = -(y)
    #     else:
    #         self.positionX = x
    #         self.positionY = y
    #     return f'{self.positionX}, {self.positionY}'

    
    def moveBackwards(self,a,b):
        self.positionX = abs(a)
        self.positionY = abs(b)
        print(f'{self.positionX}, {self.positionY}')

    

    def ignition(self):
        if (self.isOn == False):
            self.isOn = True
        else:
            self.isOn = False
        print(self.isOn)


    def getnumOfWheels1(self):
        self.numofWheels
        print(self.numofWheels)
    

    def setnumOfWheels(self,x):
        self.numofWheels = x
        print(self.numofWheels)

    def getcolorr(self):
        self.color
        print(self.color)

    def setcolorrr(self,x):
        self.color = x
        print(self.color)

class Motocycle(Vehicle):
    def __init__(self,color, engine, numofWheels, brand, seats, positionX, positionY, speed):
        self.brand = brand
        self.seats = seats
        super().__init__(color, engine, numofWheels, positionX, positionY, speed)

    def getBrand(self):
        print(self.brand)
     
    def getnumofSeats(self):
        print(self.seats)
     
    def setBrand(self,newbrand):
        self.brand = newbrand
        print(newbrand)
    
    def setnumofSeats(self,newnumofSeats):
        self.seats = newnumofSeats
        print(newnumofSeats)
    
    def accelerate(self):
        self.speed += 10
        print(self.speed)
    
    def decelerate(self):
        self.speed -= 10
        print(self.speed)

# from app import *   
# v = Vehicle(4, 'Black', 1.8, 0, 0, 90, True)
# l = Motocycle('color', 'engine', 'numofWheels', 'xxxx', '4', 'positionX', 'positionY', 3)
v.moveForward(10,10)
# l.setcolorrr('lepe')
