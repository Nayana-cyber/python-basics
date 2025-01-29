#if  you do not know  how many arguments that will be passed  into your function  ,
# add a * before a parameter  name in the function definition .
# this way the function  will receive  a tuple  of arguments,
# and can access the items  accordingly :

# if the number f arguments  is unknown , add a * before  the parameter  name :

def my_function(*kids):
    print("youngest child is  "  + kids[2])

my_function("emil","nayana","karthu")