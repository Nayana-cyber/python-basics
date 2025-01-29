#The _str_() Function

#The _str_() function controls what should be returned
# when the class object is represented as a string.

#If the _str_() function is not set,
# the string representation of the object is returned:

#The string representation of an object WITHOUT the _str_() function ?

# Create a class named Person, use the _init_() function to assign values for name and age ?

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1)

#The string representation of an object WITH the _str_() function ?

# Create a class named Person, use the _init_() function to assign values for name and age ?
# Use the _str_() function to print the name and age of a person ?

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person name is {self.name} and age is {self.age}"
p1 = Person("John", 36)
print(p1)