#remove odd num
list1 = [1, 2, 3, 4, 5, 6, 7]
print("Original list:", list1)

# Removing odd numbers
list1 = [num for num in list1 if num % 2 == 0]
print("List after removing odd numbers:", list1)

