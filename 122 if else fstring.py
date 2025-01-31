#You can perform if...else statements inside the placeholders:

#Return "Expensive" if the price is over 50, otherwise return "Cheap" ?

price = 49
txt = f"The price is {'Expensive' if price > 30 else 'Cheap'}"
print(txt)  # Output: The price is Expensive