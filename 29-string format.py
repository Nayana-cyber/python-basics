#use the format() method to insert numbers into strings:

age=20
txt="My name is nayana , andi am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars ."
print(myorder.format(quantity,itemno,price))