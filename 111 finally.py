#Finally
#The finally block, if specified,
# will be executed regardless if the try block raises an error or not.

try:
    print(x)
except:
    print("An error occurred")
finally:
    print("This will always be executed")