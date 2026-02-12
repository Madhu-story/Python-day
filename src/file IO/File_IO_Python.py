# print("-------------type 1---------------")
# # To read the file
# f = open("sample.txt", "r")
# data = f.read()
# print(data)
# f.close()

# print("-------------type 2---------------")
# # To read the file only for given length 
# f = open("sample.txt", "r")
# data = f.read(10)
# print(data)
# f.close()

# print("-------------type 3---------------")
# # To read the file line by line.
# f = open("sample.txt", "rt")
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)
# f.close()

# print("-------------type 4---------------")
# # To write a file.

# f = open("demo.txt","w")
# f.write("This 'Write' file always truncate means wipes out all data in the file.\n" \
# "This function also helps to create a file as well as to write.")
# f.close()

# print("-------------type 5---------------")
# # To append a file.

# f = open("demo.txt","a")
# f.write("\nIts my first line of code using append.\n In append, the pointer will always points at the end")
# f.close()

print("-------------type 6---------------")
# To Read and write a file.

f = open("demo.txt","r+")
f.read()
f.write("This is my new file.")
f.close()


print("-------------type 7---------------")
# To Read and write a file.

f = open("demo.txt","w+")
f.write("'r+' the pointer always points at the start. \n" \
"So no truncate only wipes the existing and replaces with this line\n" \
"whereas 'w+' truncates means wipes out all old data and print only this.")
f.close()

print("-------------type 8---------------")
# To Read and write a file.

f = open("demo.txt","a+")
f.write("\nWrite file always truncates the file, where as append() always add the text into the file.\n"\
"The pointer will always points at the end.")
f.close()


print("-------------type 9 Using with---------------")
# To read a file. Using with, no need to open the file, 
# as with keyword will close the file automatically.

with open("sample.txt", "r") as f:
    data = f.read()
    print(data)

# To write a file:
with open("demo2.txt", "w") as f:
    f.write("This is my new line using with......")
    

print("-------------To delete a file---------------")

import os

os.remove("sample.txt")