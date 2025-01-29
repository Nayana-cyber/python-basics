#So far we have created a child class that inherits the properties
# and methods from its parent.

#We want to add the _init_() function to the child class
# (instead of the pass keyword).

# The _init_() function is called automatically every time the class
# is being used to create a new object.


#Add the _init_() function to the Student class ?

#When you add the _init_() function,
# the child class will no longer inherit the parent's _init_() function.

# The child's _init_() function overrides
# the inheritance of the parent's _init_() function.

#To keep the inheritance of the parent's _init_() function,
# add a call to the parent's _init_() function:
# super()._init_(name, age)


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
            print(self.firstname, self.lastname)

class Student(Person):
                def __init__(self, fname, lname):
                  Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()

