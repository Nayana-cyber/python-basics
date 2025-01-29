# keep only  the duplicates
#the intersection ()  method will return a new set
#that only contains  the items  that are  presrent  in both sets
#join set1 and set2 , but keep only the duplicate ?
set1 = {"apple","banana", "cherry"}
set2 = {"google","microsoft", "cherry"}
set3= set1.intersection(set2)
print(set3)