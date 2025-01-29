#Inheritance Class Polymorphism

# the child classes inherits the Vehicle methods

# Create a class called Vehicle and make
# Car, Boat, Plane child classes of Vehicle ?

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
     def move(self):
         print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

#Create objects

car = Car("Ford", "Mustang")
boat = Boat("Titanic", "Cruise")
plane = Plane("Boeing", "747")

for x in (car, boat, plane):
    print(x.brand, x.model)
    x.move()

# Inheritance Class Polymorphism
