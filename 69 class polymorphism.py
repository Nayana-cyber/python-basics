#Class Polymorphism

#Polymorphism is often used in Class methods,
# where we can have multiple classes with the same method name.

#Different classes with the same method ?

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

#Create objects
car = Car("Ford", "Mustang")
boat = Boat("Titanic", "Cruise")
plane = Plane("Boeing", "747")
            
#Call the move method

for x in (car, boat, plane):
    x.move()

#Output:
#Drive!
#Sail!
#Fly!
#In the example above we have three classes: Car, Boat, and Plane.
#Each of them has a method called move().
#We can call the move() method on each object, even though they have different implementations,
#because of polymorphism.