my_list = [1,2,3,4,5,8,9,10,11]
new_list = list(filter(lambda x : (x%2 == 0) , my_list))
print(new_list)