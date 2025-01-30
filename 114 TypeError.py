# raise a TypeError if x is not an integer



x = "hello"

if not type(x) is int:
    raise TypeError("x is not an integer")