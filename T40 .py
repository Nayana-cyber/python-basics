
#Python Program to Find the Largest Among Three Numbers?

a = int(input("Enter the number"))
b = int(input("Enter the number"))
c = int(input("Enter the number"))

if a > b and a > c:
    print("a is the largest")
elif b > a and b > c :
    print("b is the largest")
else :
    print("c is the largest")