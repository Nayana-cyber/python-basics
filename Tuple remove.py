#Tuple are unchagable , so you cannot remove items from it
# but you can use the same workaround as we used for changing and adding tuple items:
#convert the tuple into a list , remove "apple" , and convert it back into a tuple:

thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)