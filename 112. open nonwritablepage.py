# try to open and write to  a  file that is not writable:

try:
    f = open("demo.file.txt")
    try:
      
      f.write("Lorum ipsum")
    except:
       print("Something went wrong when writting to the file")

    finally:
       f.close()
except:
      print("Something went wrong when closing the file")