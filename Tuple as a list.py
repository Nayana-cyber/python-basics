#Asterrisk

# if the number odf variables is less than the number of values
# you can adda  * to the variable name
# and the values will be assigned  to the variable as a list
# assign the rest of the values as a list called "red :

fruits = ("apple","banana","cherry", "strwabeery", "rasberry")
(green , yellow ,*red) = fruits
print(green)
print(yellow)
print(red)
