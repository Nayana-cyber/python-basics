# Create a class named Car.
# Use the __init__() function
# to assign values for make, model, and year.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
c1 = Car("Ford", "Mustang", 1964)
# Print the values of make, model, and year.
print(c1.make)
print(c1.model)
print(c1.year)