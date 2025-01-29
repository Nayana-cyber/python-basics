x = "awsome"

def my_func():
    a = "Fantastic"
    print("This is a local variable " , a)
    print("This is a global variable ", x)
my_func()

print(" I am trying to access local variable   from main code" , a)