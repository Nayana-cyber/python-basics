# append () method

#convert the tuple into a list , add "orange" , and convert  it back into tuple ?

thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)