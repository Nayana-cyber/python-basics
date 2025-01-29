

def factorial(x):

    if x ==1:
        return 1
    else :
        return (x * factorial (x-1))    # 3*2

num = 3
print("The  factorial of", num , "is", factorial(num))
