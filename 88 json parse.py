#Convert from Python to JSON
#If you have a Python object,

# you can convert it into a JSON string by
# using the json.dumps() method.

#Convert from Python to JSON?

import json
# Define a Python object
x = {
    "name":"John",
    "age":30,
    "city":"New York"
}

# Convert into JSON
y = json.dumps(x)
# Print the result
print(y)