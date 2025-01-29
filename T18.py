# same number in both list
list1 = [1,2,3,4,5]
list2 = [6,7,2,5,3,]
result = [ num for num in list1 if num in list2]
print(result)