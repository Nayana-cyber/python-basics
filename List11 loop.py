list = [25 , 1 , 2 , 10 , -21 , 10 , 100]
for x in list:
    print(x, end = ' ')

list = [25 , 1 , 2 , 10 , -21 , 10 , 100]
indices = range(len(list)) # range (6) -> 0 to 5


for i in indices :
    print("list[{}]:" .format(i), list[i])