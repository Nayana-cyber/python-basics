# once a tuple is created you cannot change its value
#Tuple are unchangeble , or immutable  as it also is called.

#you can convert the tuple into a list
#change the list , and convert  the list back into a tuple
#convert the tuple into a list to be able ti change list?

x=  ("apple","banana","cherry")
y = list(x)
y [1]
x = tuple(y)
print(x)