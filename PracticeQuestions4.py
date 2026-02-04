# print("-----------File I/O - example 36------------------")
# # Create a new file "practice.txt" using python and add the following data.

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\n" \
#     "We are learning File I/O\n" \
#     "using Java\n"
#     "I like programming in Java.")


# print("-----------File I/O - example 37------------------")
# # WAF that replaces all occurrences of "Java" with "Python"

# def replacing():
#     with open("practice.txt", "r") as f:
#         data = f.read()

#     new_data = data.replace("Java", "Python")
#     print(new_data)

#     with open("practice.txt", "w") as f:
#         f.write(new_data)


# print("-----------File I/O - example 38------------------")
# # Search if the word "learning" exists in the file or not.

# def check_for_word():
#     word = "xearning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not found")


# replacing()
# print()
# check_for_word()


# print("-----------File I/O - example 39------------------")
# # WAF to find in which lineof the file does the word "learning" occurs first.
# # Print -1 fif not found

# def check_for_line():
#     word = "use"
#     data = True
#     line_no = 1
    
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print("Word occurs in line -->", line_no)
#                 return
#             line_no += 1
#     return -1

# print(check_for_line())


print("-----------File I/O - example 40------------------")
# From a file containing numbers seperated by comma, print the count of even number.

count = 0
with open("practice2.txt", "r") as f:
    data = f.read()
 
    nums = data.split(",")
    print(nums)   
    for i in nums:
        if (int(i) % 2 == 0):
            count += 1
    print("Count of even numbers:", count)


""" This method is very basic so we are going for another method to solve the problem"""
    # num = ""
    # count = 0
    # length = len(data)
    # for i in range(length):           
    #     if (data[i] == ","):
    #         numb = int(num)
    #         print(numb)
    #         num = ""
    #     else:
    #         num += data[i]
