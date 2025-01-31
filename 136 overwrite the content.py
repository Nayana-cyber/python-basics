#openthe file "Demofile" andd overwrite tye content


f = open("demo.file.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demo.file.txt", "r")
print(f.read())
f.close()