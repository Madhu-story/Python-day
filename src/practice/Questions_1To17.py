# # PRACTICE QUESTIONS:

# print("---------------------Question 1-------------------------")
# # 1. Write a program to input 2 numbers and print their sum.

# num1 = 10
# num2 = 5
# # num1 = int(input("Enter the first value: "))
# # num2 = int(input("Enter the second value: "))

# sum = num1 + num2
# print("The sum of 2 numbers is: ", sum)

# print("---------------------Question 2-------------------------")
# # 2. WAP to input side of a square and print its area.

# side = 4
# # side = float(input("Enter the side os a square: "))
# print("Area of a Square =", (side**2))

# print("--------------------Question 3--------------------------")

# # 3. WAP to input 2 floating point numbers amd print their average.

# numb1 = 15.5
# numb2 = 4.5
# # numb1 = float(input("Enter the first value: "))
# # numb2 = float(input("Enter the second value: "))

# print("Average of 2 numbers =", ((numb1 + numb2)/2))


# print("--------------------Question 4--------------------------")
# # 4. WAP to input 2 int numbers, a and b.
# #    Print True if a is greater than or equal to b. If not print False.

# a = 19
# b = 15
# # a = int(input("Enter first value: "))
# # b = int(input("Enter second value: "))

# print(a >= b)


# print("--------------------Question 5--------------------------")
# # 5. WAP to input user's first name and print its length.

# name = "Rahul"
# # name = input("Enter your first name: ")

# print("Welcome ", name + "," + "\nLength of your first name is ", len(name))


# print("---------------------Question 6-------------------------")
# # 6. WAP to find the occurrence of '$' in a string.

# str = "Hi, $ I am a $ dollar symbol $, He has $99.88"
# print(str.count("$"))


# print("-----------------------Question 7-----------------------")
# # 7. WAP to check if number is entered by the user is even or odd.

# num = 17
# # num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")


# print("-----------------------Question 8-----------------------")
# # 8. WAP to find the greatest of 3 numbers entered by the user.

# num1 = 15
# num2 = 97
# num3 = 64
# # num1 = int(input("Enter the first number: "))
# # num2 = int(input("Enter the second number: "))
# # num3 = int(input("Enter the third number: "))

# if num1 >= num2 and num1 >= num3:
#     print(num1,", first number is the greatest")
# elif num2 >= num3:
#     print(num2,", second number is the greatest")
# else:
#     print(num3,", Third number is the greatest")


# print("-----------------------Question 9-----------------------")
# # 9. WAP to check if a number is a multiple of 7 or not.

# number = 41
# if number % 7 == 0:
#     print("Number is multiplicand of 7")
# else:
#     print("Number is NOT a multiplicand of 7")


# print("-----------------------Question 10-----------------------")
# # WAP to ask the user to enter names of their favourite movies and store them in  a list.

# # movies = []
# # movie_name = input("Enter your 1st favourite movie name: ")
# # movies.append(movie_name)
# # movie_name = input("Enter your 2nd favourite movie name: ")
# # movies.append(movie_name)
# # movies.append(input("Enter your 3rd favourite movie name: "))
# # print(movies)


# print("-----------------------Question 11-----------------------")
# # WAP to to check if a list contains a palindrome of elements. (HINT: Use copy() method)

# list = [1, 2, 3, 2, 1]
# print(list)

# list1 = list.copy()
# list1.reverse()
# print(list1)

# if list1 == list:
#     print("The given list contains Palindrome elements")
# else:
#     print("The list DOESNOT contain palindrome elements")


# print("-----------------------Question 12-----------------------")
# # WAP to count the number of students with "A" grade in the given tuple: ["C", "D", "A", "A", "B", "B", "A"]

# grades = ("C", "D", "A", "A", "B", "B", "A")
# scored = grades.count("A")
# print("Number of students scored grade 'A' are", scored)


# print("-----------------------Question 13-----------------------")
# # Store the above values in a list and sort them from "A" to "D"

# grades_list = ["C", "D", "A", "A", "B", "B", "A"]
# grades_list.sort()
# print(grades_list)


# print("-----------------------Question 14-----------------------")
# # Store the following word meaning in a python dictionary:
# #       table = a piece of furniture, list of facts and figures
# #       cat = a small animal

# dict = {
#     "table" : ["a piece of furniture", "list of facts and figures"],
#     "cat" : "a small animal",
#     }
# print(dict)


print("-----------------------Question 15-----------------------")
# You are given a list of subjects for students. Assume 1 classroom is required for 1 student. How many classrooms are needed by all students
#    "Python", "Java", "C++", "Python", "Javascript", "Java", "Python", "Java", "C++", "C"

subjects = {"Python", "Java", "C++", "Python", "Javascript", "Java", "Python", "Java", "C++", "C"}
classroom = len(subjects)
print("Number of classrooms needed by all students =", classroom)


print("-----------------------Question 16-----------------------")
# WAP to enter the marks of 3 subjects from the user and store them in the dictionary. Start with an empty dictionary and add one by one. 
# Use subject name as key and marks as value.

score = {}
# sub1 = input("Enter the marks of Chemistry: ")
# sub2 = input("Enter the marks of Physics: ")
# sub3 = input("Enter the marks of Mathematics: ")

# score.update({"Chemistry" : sub1})
# score.update({"Physics" : sub2})
# score.update({"Mathematics" : sub3})

print(score)


print("-----------------------Question 17-----------------------")
# Figure out a way to store 9 & 9.0 as seperate values in the set.(You can take help of built-in data types)

values = {'9', 9.0}
print(values)
# or, one more method

val1 = ("float", 9.0)
val2 = ("int", 9)
values1 = {val1, val2}
print(values1)