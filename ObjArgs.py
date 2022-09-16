class Car:
    
    color = None
    
class Motorcycle:
    
    color = None
    
def changecolor(vehicle, color):
    vehicle.color = color
    
car_1 = Car()
bike = Motorcycle()

changecolor(car_1, "Red")
changecolor(bike, "Black")

print(car_1.color)
print(bike.color)