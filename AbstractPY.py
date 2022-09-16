from abc import ABC,abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
class Car(Vehicle):
    
    def go(self):
        print("The Car is moving!!")
        
class Bike(Vehicle):
    
    def go(self):
        print("The Bike is moving!!")
        
car = Car()
bike = Bike()

car.go()
bike.go()