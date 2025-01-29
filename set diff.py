#the difference method will rwturn a new set
#this will contain only the  item from the first set
# that are not present in the other set
# keep all items  from set1 that are not in set2


set1 = {"apple","banana", "cherry"}
set2 = {"google","microsoft", "cherry"}
set3= set1.difference(set2)
print(set3)

#you can use -operator instead of the difference () method
set1 = {"apple","banana", "cherry"}
set2 = {"google","microsoft", "cherry"}
set3= set1-(set2)
print(set3)