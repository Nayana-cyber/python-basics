#convert all python bject containing all the legal data types

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

print(json.dumps(x))