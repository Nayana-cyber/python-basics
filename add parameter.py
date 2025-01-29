#Add a year parameter,
# and pass the correct year when creating objects ?

class Person:
    def __init__(self, fname, lname, year):
        self.firstname = fname
        self.lastname = lname
        self.year = year
    def printname(self):
            print(self.firstname, self.lastname, self.year)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x= Student("Mike", "Olsen", 2019)
print(x.graduationyear)
