#Parse JSON - Convert from JSON to Python

#If you have a JSON string,
# you can parse it by using the json.loads() method.

#The result will be a Python dictionary.

# Convert from JSON to Python ?

import json  

#some JSON

x =  '{ "name":"John", "age":30, "city":"New York"}'

#parse x:

y = json.loads(x)

print(y) #30
