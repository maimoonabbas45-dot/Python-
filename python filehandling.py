f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("file.txt","r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

fileptr = open("file.txt","r")
if fileptr:
    print("file is open sucessfully")
f.close()

f1 = open("file1.txt","w")
f1.write("python is great language.\nyeah it's also a good!\njava is also good\nmight ai will come in hospital\n your end sem is coming nearby so study it.")
f1.close()


#to remove folder use os.rmdir("folder name") and also os.remove("folder name")
import os
#os.rename("demo.txt","hello.txt")

