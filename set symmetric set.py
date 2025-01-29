# WILL KEEP ONLY the elements that are NOT present in both sets .
# the keep items  thata re not present  in both sets ?

set1 = {"apple","banana", "cherry"}
set2 = {"google","microsoft", "cherry"}
set3= set1.symmetric_difference(set2)
print(set3)

#you can use ^ operator instes of the symmetric_difference()

set1 = {"apple","banana", "cherry"}
set2 = {"google","microsoft", "cherry"}
set3= set1 ^ (set2)
print(set3)