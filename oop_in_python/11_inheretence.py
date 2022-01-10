class Vehicle:
    def __init__(self,make,color,model) -> None:
        self.make = make
        self.color = color
        self.model =model

    def printDetails(self):
        print("Manufacturer : ",self.make)
        print("color : ",self.color)
        print("model : ",self.model)

#here calss Car is Extending Vehicle class
class Car(Vehicle):
    def __init__(self, make, color, model,doors) -> None:
        #calling the constructor from parent class
        Vehicle.__init__(self,make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors :",self.doors)

obj1 = Car("Maruti","green","2020",4)

obj1.printCarDetails()


#multilevel inheritance
print()
print("output of multi-level inheritance")
print()
class Vehicle:
    def setTopSpeed(self,speed):
        self.topSpeed = speed
        print("top speed is",self.topSpeed)

class car(Vehicle):
    def openTruck(self):
        print("truck is open")

class hybridcar(car):
    def turnOnHybrid(self):
        print("Hybrid mode")


prime = hybridcar()
prime.setTopSpeed(230)
prime.openTruck()
prime.turnOnHybrid()


#hierarchal inheritance
class vehicle:
    def setTopSpeed(self,speed):
        self.topSpeed = speed
        print("top speed is",self.topSpeed)

class bike(vehicle):
    pass

class truck(vehicle):
    pass

yo = bike()
yo.setTopSpeed(40)
y2 = truck()
y2.setTopSpeed(120)



#hirearchal inheritance 
print()
print("output of hirearchal inheritance")
print()
class engine:
    def setTankCapacity(self,capacity):
        self.capacity = capacity

class electric_engine:
    def setChargeCapacity(self,charge_capacity):
        self.charge_capacity = charge_capacity

#child class inherited from bothclassed
class hybrid_engine(engine , electric_engine):
    def printDetails(self):
        print("tank capacity",self.capacity)
        print("charge capacity",self.charge_capacity)


car2 = hybrid_engine()

car2.setTankCapacity("20 l")
car2.setChargeCapacity("330 W")
car2.printDetails()


#Hybrid inheritance
print()
print("output of hybrid inheritance")
print()

class Engine:
    def setPower(self,power):
        self.power = power
    
class CombustionEngine(Engine):
    def setTankCapacity(self,tankCapacity):
        self.tankCapacity = tankCapacity
class ElectricEngine(Engine):
    def setChargeCapcity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

#child class inherited form combkustion engine and Electric engine

class HyberidEngine(CombustionEngine,ElectricEngine):
    def printDetails(self):
        print("power :",self.power)
        print("tank capacity :",self.tankCapacity)
        print("charge capacity :",self.chargeCapacity)

car3 = HyberidEngine()

car3.setPower("2000 cc")
car3.setChargeCapcity("230 V")
car3.setTankCapacity("15 l")
car3.printDetails()