#Read Only Parts of the File

#By default the read() method returns the whole text,

# but you can also specify how many characters you want to return:


# Return the 5 first characters of the file ?

f = open("demo.file.txt", "r")
print(f.read(5))  # Output: Hello1