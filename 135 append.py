#Python File Write

#Write to an Existing File
#To write to an existing file,
# you must add a parameter to the open() function:

#  "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

#Open the file "demofile2.txt" and append content to the file ?


f = open("demo.file.txt", "a")
f.write("Now the file has more content!")
f.close()
#Open the file read the file ater the appending the content
f = open("demo.file.txt", "r")
print(f.read())
f.clos1e()