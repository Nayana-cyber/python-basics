#print string passed into the function

import re

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w", txt)
print(x.string)