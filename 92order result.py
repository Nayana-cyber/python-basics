#Order the Result

# The json.dumps() method has parameters to order the keys in the result:
#Use the sort_keys parameter
# to specify if the result should be sorted or not:


import json 

x = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x, indent=4,sort_keys=True)) #format the result