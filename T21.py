list1 = [1, 'apple', 3.5, 'banana', 42, 'cherry', 7.8]

# Separate non-numeric items
non_numeric_items = [item for item in list1 if not isinstance(item, (int, float))]

print(non_numeric_items)
