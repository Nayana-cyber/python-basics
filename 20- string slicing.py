stg="helloworld"

slice1 = stg[0:5] #[starting position: ending position ]
print(slice)

slice2 = stg[0:-1]
print(slice2)

slice3 = stg[3:5]
print(slice3)


String='ASTIRING'
# using slice  constructor

s1 = slice(3)
s2 = slice(1,5,2)
s3 = slice(-1,-12,-2)

print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])