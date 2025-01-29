#Add Methods
#Add a method called welcome to the Student class ?

class Person:
    def __init__(self, fname, lname, year):
        self.firstname = fname
        self.lastname = lname
       
    def printname(self):
            print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
         print(f"Hello, my name is {self.firstname} {self.lastname} and I am graduating in {self.graduationyear}")

x= Student("Mike", "Olsen", 2019)
x.welcome()