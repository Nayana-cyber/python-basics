# identity operators - is and is not checking  if 2 obj have same memmory loc

a="TutorialPoint"
b=a
print("id(a), id(b):", id(a), id(b))  #memmory location
print("a is b :", a is b)
print("b is not a:",b is not a)

a=[1,2,3]
b=[1,2,3]
print("id(a),id(b):",id(a), id(b))
print("a is b;", a is b)
print("b is not a:", b is not a)
